#!/usr/bin/env python3
"""Push a Horizon summary (Markdown or JSON) into the Supabase `papers` table.

Reads SUPABASE_URL and SUPABASE_KEY from the environment. SUPABASE_KEY must
be the service_role key: the `papers` table only has a public *read* RLS
policy, so writes need a key that bypasses RLS.

Usage:
    python scripts/push_to_supabase.py [path/to/summary.md|.json]

If no path is given, the most recently modified file in data/summaries/ is
used.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx

REPO_ROOT = Path(__file__).resolve().parent.parent
SUMMARIES_DIR = REPO_ROOT / "data" / "summaries"

# "## [Title](https://example.com/paper) ⭐️ 7.0/10"
ITEM_HEADER_RE = re.compile(
    r"^##\s*\[(?P<title>.+?)\]\((?P<url>[^)]+)\)\s*(?:\S*\s*(?P<score>\d+(?:\.\d+)?)/10)?\s*$",
    re.MULTILINE,
)
# "rss · arXiv - Some Feed Name · Jun 14, 19:00"
META_LINE_RE = re.compile(
    r"^(?P<source_type>[\w/ .\-]+?)\s*·\s*(?P<source_name>.+?)\s*·\s*(?P<date_str>.+)$",
    re.MULTILINE,
)
REPORT_DATE_RE = re.compile(r"^#\s*Horizon Daily\s*-\s*(?P<date>\d{4}-\d{2}-\d{2})", re.MULTILINE)


def find_latest_summary() -> Path:
    candidates = list(SUMMARIES_DIR.glob("horizon-*.md")) + list(SUMMARIES_DIR.glob("horizon-*.json"))
    if not candidates:
        raise FileNotFoundError(f"No Horizon summary files found in {SUMMARIES_DIR}")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def parse_short_date(date_str: str, report_date: datetime) -> str | None:
    """Parse a short "Mon D, HH:MM" date, inferring the year from the report date."""
    try:
        parsed = datetime.strptime(date_str.strip(), "%b %d, %H:%M")
    except ValueError:
        return None

    report_date = report_date.replace(tzinfo=timezone.utc)
    candidate = parsed.replace(year=report_date.year, tzinfo=timezone.utc)
    # Item dates are always <= report date; a later date means it was really last year.
    if candidate > report_date + timedelta(days=2):
        candidate = candidate.replace(year=report_date.year - 1)
    return candidate.isoformat()


def parse_markdown(text: str) -> list[dict]:
    report_match = REPORT_DATE_RE.search(text)
    report_date = (
        datetime.strptime(report_match.group("date"), "%Y-%m-%d")
        if report_match
        else datetime.now(timezone.utc)
    )

    headers = list(ITEM_HEADER_RE.finditer(text))
    items = []
    for i, header in enumerate(headers):
        block_start = header.end()
        block_end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[block_start:block_end]

        meta_match = META_LINE_RE.search(block)
        summary_text = block[: meta_match.start()] if meta_match else block
        summary_text = re.sub(r"\n?-{3,}\s*$", "", summary_text).strip()

        source_name = meta_match.group("source_name").strip() if meta_match else None
        published_at = (
            parse_short_date(meta_match.group("date_str"), report_date) if meta_match else None
        )

        score = header.group("score")
        items.append(
            {
                "title": header.group("title").strip(),
                "url": header.group("url").strip(),
                "source": source_name,
                "ai_score": float(score) if score else None,
                "ai_summary": summary_text or None,
                "published_at": published_at,
            }
        )
    return items


def parse_json(text: str) -> list[dict]:
    data = json.loads(text)
    if isinstance(data, list):
        records = data
    elif isinstance(data, dict):
        records = data.get("items") or data.get("papers") or data.get("results") or []
    else:
        records = []

    items = []
    for r in records:
        items.append(
            {
                "title": r.get("title"),
                "url": r.get("url") or r.get("link"),
                "source": r.get("source") or r.get("source_name"),
                "ai_score": r.get("ai_score", r.get("score")),
                "ai_summary": r.get("ai_summary") or r.get("summary"),
                "published_at": r.get("published_at") or r.get("published"),
            }
        )
    return items


def load_items(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return parse_json(text)
    return parse_markdown(text)


def upsert_paper(client: httpx.Client, base_url: str, item: dict) -> None:
    if not item.get("url"):
        raise ValueError("item has no url, skipping")

    payload = {k: v for k, v in item.items() if v is not None}
    resp = client.post(
        f"{base_url}/rest/v1/papers",
        params={"on_conflict": "url"},
        json=payload,
    )
    resp.raise_for_status()


def main() -> int:
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    if not supabase_url or not supabase_key:
        print(
            "Error: SUPABASE_URL and SUPABASE_KEY must be set in the environment "
            "(SUPABASE_KEY should be the service_role key).",
            file=sys.stderr,
        )
        return 1

    if len(sys.argv) > 1:
        source_path = Path(sys.argv[1])
    else:
        try:
            source_path = find_latest_summary()
        except FileNotFoundError:
            print("No Horizon summary file found (0 items today) - nothing to push.")
            print("\n0/0 paper(s) written to Supabase.")
            return 0
    print(f"Reading: {source_path}")

    items = load_items(source_path)
    print(f"Parsed {len(items)} item(s).")

    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates",
    }

    written = 0
    with httpx.Client(headers=headers, timeout=30) as client:
        for item in items:
            title = (item.get("title") or "")[:70]
            try:
                upsert_paper(client, supabase_url.rstrip("/"), item)
                written += 1
                print(f"  OK   {title}")
            except Exception as exc:  # noqa: BLE001 - report and continue per item
                print(f"  FAIL {title} -> {exc}", file=sys.stderr)

    print(f"\n{written}/{len(items)} paper(s) written to Supabase.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
