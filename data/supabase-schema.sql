-- Horizon Supabase schema: papers / topics / notes
-- RLS: papers and topics are publicly readable (read-only); notes is
-- per-user (each signed-in user can only see/edit their own rows).

create table if not exists public.topics (
  id uuid primary key default gen_random_uuid(),
  name text not null unique,
  description text,
  created_at timestamptz not null default now()
);

create table if not exists public.papers (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  abstract text,
  authors text[],
  url text unique,
  source text,
  topic_id uuid references public.topics(id) on delete set null,
  ai_score numeric,
  ai_summary text,
  published_at timestamptz,
  created_at timestamptz not null default now(),
  fts tsvector generated always as (
    setweight(to_tsvector('english', coalesce(title, '')), 'A') ||
    setweight(to_tsvector('english', coalesce(abstract, '')), 'B')
  ) stored
);

create index if not exists papers_fts_idx on public.papers using gin (fts);
create index if not exists papers_topic_id_idx on public.papers (topic_id);

create table if not exists public.notes (
  id uuid primary key default gen_random_uuid(),
  paper_id uuid references public.papers(id) on delete cascade,
  user_id uuid references auth.users(id) on delete cascade,
  content text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table public.notes
  add column if not exists user_id uuid references auth.users(id) on delete cascade;

create index if not exists notes_paper_id_idx on public.notes (paper_id);
create index if not exists notes_user_id_idx on public.notes (user_id);

drop index if exists notes_paper_user_unique;
create unique index notes_paper_user_unique on public.notes (paper_id, user_id);

alter table public.topics enable row level security;
alter table public.papers enable row level security;
alter table public.notes enable row level security;

drop policy if exists "Public read access to papers" on public.papers;
create policy "Public read access to papers"
  on public.papers
  for select
  to anon, authenticated
  using (true);

drop policy if exists "Public read access to topics" on public.topics;
create policy "Public read access to topics"
  on public.topics
  for select
  to anon, authenticated
  using (true);

drop policy if exists "Users can view their own notes" on public.notes;
create policy "Users can view their own notes"
  on public.notes
  for select
  to authenticated
  using (user_id = auth.uid());

drop policy if exists "Users can insert their own notes" on public.notes;
create policy "Users can insert their own notes"
  on public.notes
  for insert
  to authenticated
  with check (user_id = auth.uid());

drop policy if exists "Users can update their own notes" on public.notes;
create policy "Users can update their own notes"
  on public.notes
  for update
  to authenticated
  using (user_id = auth.uid())
  with check (user_id = auth.uid());
