---
layout: default
title: "Horizon Summary: 2026-10-02 (EN)"
date: 2026-10-02
lang: en
---

> From 32 items, 5 important content pieces were selected

---

1. [2025 Nobel Prize in Medicine Awarded for Peripheral Immune Tolerance Discoveries](#item-1) ⭐️ 9.0/10
2. [New AI Beats Best Stratego Player Using 34x Fewer Games Than DeepNash](#item-2) ⭐️ 8.0/10
3. [Zig v0.17.0 Released With Broader Targets and New Build Integration](#item-3) ⭐️ 8.0/10
4. [Greg Kroah-Hartman: LLM Bug Reports Mostly Collapse Under Scrutiny](#item-4) ⭐️ 8.0/10
5. [arXiv Imposes 1-Year Ban for Unverified LLM-Generated Content](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2025 Nobel Prize in Medicine Awarded for Peripheral Immune Tolerance Discoveries](https://t.me/zaihuapd/44174) ⭐️ 9.0/10

The 2025 Nobel Prize in Physiology or Medicine was awarded to Mary E. Brunkow, Fred Ramsdell, and Shimon Sakaguchi for their discoveries concerning peripheral immune tolerance. Their work explained the mechanisms that keep the immune system from attacking the body's own organs, a recognition announced as a brief summary with no detailed commentary attached. These findings form the foundation of modern regulatory T cell (Treg) biology and are central to understanding autoimmune disease, allergy, and transplant tolerance. They have directly shaped therapeutic strategies ranging from autoimmune disease treatment to cancer immunotherapy, so the award signals a paradigm that the broader biomedical industry now treats as settled science. Sakaguchi identified a subset of T cells expressing CD25 that suppress other immune cells, while Brunkow and Ramsdell traced the underlying gene through the scurfy mouse and the human IPEX syndrome, pinpointing FOXP3. A key caveat is that peripheral tolerance is only one layer of protection: deletion of self-reactive T cells in the thymus (central tolerance) is only about 60–70% efficient, leaving peripheral mechanisms to handle the remainder.

telegram · zaihuapd · Oct 2, 14:15

**Background**: The immune system must distinguish the body's own tissues ("self") from foreign threats, a property called immune tolerance. T cells and B cells mature in the thymus and bone marrow, where central tolerance removes many self-reactive cells, but some escape into lymph nodes and peripheral tissues. Peripheral immune tolerance then controls these escapees through clonal deletion, anergy (functional silencing), and suppression by regulatory T cells, whose master regulator is the transcription factor FOXP3. When that control fails, the result is autoimmune disease; patients with FOXP3 defects develop severe multi-organ autoimmunity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Peripheral_immune_tolerance">Peripheral immune tolerance</a></li>

</ul>
</details>

**Tags**: `#Nobel Prize`, `#Immunology`, `#Peripheral Immune Tolerance`, `#Scientific Research`, `#Biomedical Breakthrough`

---

<a id="item-2"></a>
## [New AI Beats Best Stratego Player Using 34x Fewer Games Than DeepNash](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

A newly published AI system (described in a Nature paper and an accompanying arXiv preprint, 2511.07312) has defeated the best Stratego player in history. According to the report, it did so on a relatively small budget, learning from roughly 34 times fewer games than DeepMind's DeepNash while still ending up considerably stronger. Stratego is a hidden-information game in which the value of a move depends on facts the player cannot observe, which makes the search and learning techniques that conquered chess and Go far less effective. Demonstrating a sample-efficient method that beats the strongest human here suggests similar approaches could transfer to real-world problems such as security, negotiation, and other strategic settings with concealed information. The core difficulty is that hidden information rules out ordinary lookahead — you cannot reason "if I do this, they will do that" because you do not even know which of the opponent's pieces you are facing — so the algorithm must reason over probability distributions instead. Community discussion also highlighted that the AI found non-obvious strategies, such as tucking its flag into a corner behind just two bombs, a setup human players rarely use.

hackernews · PaulHoule · Oct 2, 14:11 · [Discussion](https://news.ycombinator.com/item?id=49933740)

**Background**: In perfect-information games like chess and Go, both players can see the whole board, so AI systems can search ahead and, with enough self-play, surpass humans. Stratego is different: each player's pieces are hidden from the opponent, so it belongs to the same imperfect-information family as poker and much of real-world decision-making. DeepMind's DeepNash, presented in 2022, was the previous milestone for Stratego, and DeepMind has also explored general imperfect-information agents such as Player of Games. Sample efficiency — how much experience a learning algorithm needs to reach a given skill level — is a central open problem in reinforcement learning, and this result is notable primarily for how sharply it improves on prior Stratego work.

<details><summary>References</summary>
<ul>
<li><a href="https://analyticsindiamag.com/ai-features/deepmind-comes-out-with-player-of-games-masters-both-perfect-and-imperfect-information-games">How does DeepMind's Player of Games master diverse games ? | AIM</a></li>
<li><a href="https://arxiv.org/abs/1807.01675">[1807.01675] Sample - Efficient Reinforcement Learning with...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely nostalgic, sharing childhood memories of Stratego — including one who admitted discovering a friend had subtly marked the pieces, and another who was unbeatable locally yet never imagined the game had serious competitive players. The most substantive point came from janalsncm, who argued the 34x reduction in games played is the really critical result, since hidden information makes it impossible to search ahead in the usual way. Others joked about having planned to build the first winning Stratego bot themselves, and rcyeh discussed trying the AI's flag-in-the-corner, two-bomb setup to waste an opponent's expected moves.

**Tags**: `#AI`, `#game-playing`, `#hidden-information`, `#reinforcement-learning`, `#Stratego`

---

<a id="item-3"></a>
## [Zig v0.17.0 Released With Broader Targets and New Build Integration](https://ziglang.org/download/0.17.0/release-notes.html) ⭐️ 8.0/10

The Zig project published the official release notes for Zig v0.17.0 on ziglang.org, announcing the latest version of the systems programming language. Community discussion quickly highlighted the release's extensive target support and new build-system integration, along with questions about the project's AI/LLM policy and pending async I/O work. Zig's unusually broad cross-compilation target support makes it one of the few modern languages that can realistically compete with C in embedded and low-level work, so each release extends where the language can be deployed. Improvements to build integration also ripple outward to the tooling and packaging ecosystem that depends on Zig's build system. Commenters point to two features still on the roadmap rather than finished in this release: a new stackless coroutine I/O implementation and first-class fuzzer tooling. The state of evented I/O and io_uring support in v0.17.0 was also raised as an open question, and Zig already ships limited fuzz-testing primitives such as std.testing.fuzz and std.testing.Smith.

hackernews · ErenayDev · Oct 2, 20:56 · [Discussion](https://news.ycombinator.com/item?id=49938521)

**Background**: Zig is a general-purpose systems programming language and toolchain created by Andrew Kelley and first announced in 2016, positioned as a general-purpose improvement on C. It avoids macros and preprocessor instructions, and instead offers compile-time generics with reflection, manual memory management, packed structs, arbitrary-width integers and multiple pointer types. Development is funded by the Zig Software Foundation (ZSF) through corporate sponsorships and personal donations, and the language is released under an MIT license. Because Zig is still in its 0.x series, releases land frequently and often include breaking changes, which makes each set of release notes closely watched by users.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home Zig Programming Language</a></li>
<li><a href="https://andrewkelley.me/post/zig-new-async-io-text-version.html">Zig's New Async I/O (Text Version) - Andrew Kelley</a></li>

</ul>
</details>

**Discussion**: In a 91-comment Hacker News thread, the dominant sentiment was admiration for Zig's target support, with one commenter calling it possibly the only language that competes with C on that front, plus enthusiasm for what the new build integration could unlock for tooling. Several participants repeatedly asked whether the project's hard-line AI/LLM stance has changed, and one noted that Andrew Kelley, inspired by results from SQLite, is warming up to using LLMs for bug discovery as a path toward bug-free software. Others asked about the current state of evented I/O and io_uring, and listed the new stackless coroutine I/O implementation and first-class fuzzing tooling as their most anticipated features.

**Tags**: `#zig`, `#programming-languages`, `#systems-programming`, `#compilers`, `#release-notes`

---

<a id="item-4"></a>
## [Greg Kroah-Hartman: LLM Bug Reports Mostly Collapse Under Scrutiny](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

In a Kernel Recipes 2026 talk, veteran Linux kernel maintainer Greg Kroah-Hartman dissected Anthropic's Mythos vulnerability disclosure, showing that of the 79 claimed vulnerabilities, 24 had no detail at all, 14 were not bugs, 3 were fabricated, and 15 were already fixed in the latest release — leaving only about 20 that actually required a fix. He summed it up by noting that the whole marketing story came down to roughly one hour of kernel development work. This is a rare, high-signal debunk of LLM-driven security marketing from a maintainer with authority over the world's most widely deployed kernel, and it warns enterprises, journalists, and the public not to treat AI-reported CVE counts as genuine security value. It also feeds a broader credibility debate about frontier labs whose safety messaging claims models are too dangerous to release while their benchmark-style claims fail basic scrutiny. Of the roughly 20 vulnerabilities that did warrant fixes, 7 relied on the assumption of a malicious filesystem image and 2 assumed attacker-controlled input, meaning many are not practical real-world threats. Kroah-Hartman also noted that Mythos essentially pattern-matched decades of previous kernel patches and applied them elsewhere to check for unpatched cases, without crediting the kernel developers who originally fixed those issues.

hackernews · usernomdeguerre · Oct 2, 02:51 · [Discussion](https://news.ycombinator.com/item?id=49929391)

**Background**: Linux kernel bugs and fixes are tracked through CVE identifiers and stable-release backports, work that maintainers like Greg Kroah-Hartman coordinate publicly, which makes the claims verifiable by anyone. Anthropic's Claude Mythos is a restricted-access model series that was kept from general release on the grounds that it could find software vulnerabilities, with access given to select organizations for security scanning. In parallel, the security industry has been raising concerns that LLM-generated CVE descriptions and patch suggestions can degrade the quality and trustworthiness of vulnerability data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Mythos">Anthropic Mythos</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>
<li><a href="https://vuldb.com/article/llm-generated-cve-descriptions-undermine-security-data-quality-and-trust">LLM Generated CVE Descriptions Undermine Security Data Quality...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely praised Kroah-Hartman's candor, with one quoting the slide breakdown to underscore how little of the 79-CVE claim survived review. Others highlighted the dissonance between labs claiming their models are too dangerous to release and then making sloppy marketing claims, criticized Anthropic for not crediting the kernel developers whose patches it pattern-matched, and suggested that specialized kernel-trained models could still make bug discovery faster and more accurate in the future.

**Tags**: `#linux-kernel`, `#security`, `#LLM`, `#AI-hype`, `#vulnerability-research`

---

<a id="item-5"></a>
## [arXiv Imposes 1-Year Ban for Unverified LLM-Generated Content](https://t.me/zaihuapd/44166) ⭐️ 8.0/10

arXiv has clarified enforcement for submissions containing content that proves the author did not check LLM-generated output: such authors face a one-year submission ban. After the ban ends, their subsequent submissions must first be accepted by a trusted peer-reviewed venue before they can be posted to arXiv. This is one of the first concrete, published penalties from a major preprint server targeting unchecked LLM use in research writing, and it signals that academic platforms are moving from vague AI guidelines to enforceable sanctions. It will directly affect how researchers, especially in AI/ML and adjacent fields, use LLMs during drafting, and could set a precedent for other preprint servers and publishers. The penalty applies to cases such as hallucinated citations, leftover LLM meta-comments in the text, and phrases like "table data is only an example, please replace with real experimental data." arXiv's code of conduct states that listing yourself as an author means taking responsibility for all content of the paper, regardless of how that content was produced.

telegram · zaihuapd · Oct 2, 06:21

**Background**: arXiv is a free, open-access repository hosting roughly 2.4 million preprints in physics, mathematics, computer science and other fields; submissions are moderated but not peer reviewed. Large language models can produce "hallucinations" — fluent, confidently stated but false output — including fabricated citations that look plausible but do not exist. Because arXiv historically relied on author responsibility rather than formal peer review, unchecked LLM output slipping into preprints became a visible problem, prompting this explicit enforcement policy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">arXiv - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.promptlayer.com/glossary/citation-hallucination/">What is Citation hallucination ?</a></li>

</ul>
</details>

**Tags**: `#arXiv`, `#LLM`, `#academic-publishing`, `#research-integrity`, `#AI-policy`

---