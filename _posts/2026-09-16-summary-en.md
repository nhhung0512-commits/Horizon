---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 33 items, 2 important content pieces were selected

---

1. [A 4B-Parameter Model Generates Query Plans Claimed 81% Faster Than Postgres](#item-1) ⭐️ 8.0/10
2. [Flock Safety Cameras Found Riddled With Flaws and Hard-Coded Credentials](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [A 4B-Parameter Model Generates Query Plans Claimed 81% Faster Than Postgres](https://rohanbansal.com/qorl) ⭐️ 8.0/10

A practitioner published a technical write-up on rohanbansal.com describing how they trained a 4-billion-parameter model to produce SQL query plans for Postgres, claiming the resulting plans run 81% faster on an in-memory benchmark. The post drew 298 upvotes and 55 comments on Hacker News, mixing praise for its accessible explanation of LLM internals with sharp scrutiny of the benchmark setup. Query planning is one of the hardest combinatorial optimization problems in database systems, traditionally solved by hand-written cost models and heuristics, so showing that a small LLM can beat Postgres' planner suggests learned approaches could eventually reshape how optimizers are built. It also illustrates the growing trend of distilling frontier-model behavior into small, deployable models rather than relying on huge hosted models. The benchmark runs on an 8 GB dataset that fits entirely in memory, with shared_buffers constrained to a fraction of that size, caches warmed before measurement, and only read-only SELECT queries, which critics say makes the '81% faster' headline hard to generalize to realistic OLTP workloads. The author also notes that the model was distilled from trajectories produced by a larger frontier model called Astra.

hackernews · polyphilz · Sep 16, 18:50 · [Discussion](https://news.ycombinator.com/item?id=49731285)

**Background**: A database query planner is the component that decides how a SQL statement is physically executed — which tables to scan, in what order to join them, and which indexes to use — and it normally relies on a cost-based optimizer driven by statistics and hand-tuned heuristics. Researchers have explored learned query optimizers such as Neo, which use neural networks to build execution plans instead of relying only on cost models. Benchmarks like TPC-H are the standard way to compare such approaches, and shared_buffers is the Postgres setting that controls how much memory the database devotes to caching pages. The article's claim rests on profile-guided-style optimization, meaning the model was trained using execution feedback rather than pure static reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://vldb.org/pvldb/vol12/p1705-marcus.pdf">Neo: A Learned Query Optimizer</a></li>
<li><a href="https://www.tpc.org/tpch/">TPC-H Homepage</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly skeptical of the headline claim, pointing out that an 8 GB fully in-memory dataset, constrained shared_buffers, warmed caches, and read-only SELECTs make the benchmark unrepresentative and risk overfitting to a narrow workload. Several readers praised the writing for making LLM internals understandable to non-AI engineers, while others argued an LLM is a 'blunt weapon' for a math-heavy problem and that AlphaGo-style learned heuristics or just-in-time indexes might be better directions; a few also raised concerns about production failure modes and about openly admitting to distilling a closed frontier model.

**Tags**: `#databases`, `#query-optimization`, `#llm`, `#postgresql`, `#machine-learning`

---

<a id="item-2"></a>
## [Flock Safety Cameras Found Riddled With Flaws and Hard-Coded Credentials](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

Hackers and security researcher Micah Lee disclosed that Flock Safety's police surveillance cameras contain serious security vulnerabilities, including hard-coded credentials and poor secure-boot and key-management practices, with technical analysis published by Wired and on micahflee.com. Distributed Denial of Secrets also published the extracted partition images of the affected ALPR cameras. The flaws mean anyone with physical access to a camera in a public space may be able to extract data or credentials, undermining trust in a surveillance system that is already controversial for mass ALPR tracking and documented police misuse. It also sharpens the debate over how AI surveillance vendors handle security and vulnerability disclosure. The cameras appear to rely on off-the-shelf hardware and software stacks, and the extracted data was reportedly not suitably encrypted, so it could simply be taken by an unauthorized person who walks up to the device; Flock's vulnerability disclosure policy has also been criticized as a token measure with a carve-out for cases requiring interaction with the device or downloading its data.

hackernews · driverdan · Sep 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=49726586)

**Background**: Flock Safety builds solar-powered cameras mounted on poles along streets and highways that use automated license plate recognition (ALPR) and AI to help law enforcement identify vehicles, and it has partnered widely with police departments across the US. Hard-coded credentials are a well-known weakness (tracked as CWE-798) in which passwords, API keys or cryptographic keys are embedded directly in source code, configuration files or firmware instead of being stored securely. When devices are deployed in unsecured public spaces, attackers' threat model realistically includes local physical access, making such embedded secrets especially dangerous.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnet.com/home/security/when-flock-comes-to-town-how-these-ai-cameras-work-and-what-to-do-about-them/">When Flock Comes to Town: How These AI Cameras Work... - CNET</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/798.html">CWE - CWE-798: Use of Hard - coded Credentials (4.20)</a></li>
<li><a href="https://www.securityscientist.net/blog/12-questions-and-answers-about-hardcoded-credentials-in-code/">12 Questions and Answers About hardcoded credentials in code</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were broadly critical: one called Flock's vulnerability disclosure policy a facade that welcomes reports except when they require interacting with the device, another attributed the flaws to "laziness" and reduced time-to-market that ignored a threat model including physical access, and others framed the case as the inevitable result of "move fast and break things" venture-backed surveillance, while noting the reporting was a collaboration with 404 Media.

**Tags**: `#security`, `#privacy`, `#surveillance`, `#vulnerability-disclosure`, `#iot`

---