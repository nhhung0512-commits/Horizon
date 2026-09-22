---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 39 items, 10 important content pieces were selected

---

1. [OpenAI Releases GPT-6 Sol and Luna Frontier Models](#item-1) ⭐️ 9.0/10
2. [Anthropic Ships Claude Opus 5.5 With Cheaper Tokens](#item-2) ⭐️ 9.0/10
3. [Pentagon: AI Overreliance Contributed to Strike on Iranian School](#item-3) ⭐️ 9.0/10
4. [vLLM v0.30.0 ships 762 commits with Fast Start GPU weight cache](#item-4) ⭐️ 8.0/10
5. [Hackers claim FBI employee data theft via Oracle PeopleSoft zero-day](#item-5) ⭐️ 8.0/10
6. [Claude Opus 5.5 Benchmarked at Max Reasoning Setting](#item-6) ⭐️ 8.0/10
7. [TypeSafe AI launches Jev, a decision model returning typed probabilistic outputs](#item-7) ⭐️ 8.0/10
8. [Xiaomi Releases MiMo-V2.6 Omnimodal Models With $3.5M RL Training Cost](#item-8) ⭐️ 8.0/10
9. [25 Fields Medalists Warn AI May Be Misaligned With Mathematics Research Goals](#item-9) ⭐️ 8.0/10
10. [DeepSeek and Tsinghua Release DSec Sandbox Platform Technical Report](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Releases GPT-6 Sol and Luna Frontier Models](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI announced GPT-6 Sol and Luna, two new frontier models that bring different balances of capability and cost, with Luna notably priced at half the cost of the previous GPT-5.6 Luna. The release arrived less than three months after GPT-5.6 and builds on the advances behind GPT-6 Astra, while claiming major accuracy gains and dramatic cost reductions across key benchmarks. A major frontier model release from OpenAI reshapes the competitive landscape for developers building AI agents, since pricing and capacity directly drive agent economics. The substantial price cut, especially Luna at half the cost of its predecessor, could make large-scale agentic workloads far more affordable and pressure rivals like Anthropic's Claude Code to respond on both cost and usage limits. The models are available in the API, Codex, and ChatGPT, and OpenAI positioned them as bringing much of GPT-6 Astra's strengths into faster, more affordable form factors. The announcement drew comparisons against Anthropic's Claude across key benchmarks, an unusual move that signals intense competition on price-performance in the agent tooling market.

hackernews · OfficialTurkey · Sep 22, 18:00 · [Discussion](https://news.ycombinator.com/item?id=49805509)

**Background**: OpenAI is a leading AI lab that periodically releases frontier large language models, each generation typically improving reasoning, coding, and agentic capabilities while shifting the price-performance curve. GPT-6 Astra was a prior high-end model, and GPT-6 Sol and Luna are positioned as offspring that carry much of Astra's capability into cheaper, faster tiers. "Luna" appears to be the lower-cost tier and "Sol" the higher-capability one. These models matter especially for developers running autonomous agents, where token costs and rate limits accumulate rapidly and directly determine feasibility.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI’s GPT-6 Sol doubles its accuracy rate – for half the cost</a></li>
<li><a href="https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna-in-the-api-codex-and-chatgpt/1399925">Announcing GPT-6 Sol and GPT-6 Luna in the API, Codex and ...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters focused on cost and ergonomics: Simon Willison highlighted that GPT-6 Luna being half the price of GPT-5.6 Luna is a big deal, while jeffnash weighed Codex Pro 20x against Claude Code 20x on usage limits and found Codex currently ahead. Others, like m_fayer, expressed attachment to a previous model's 'personality' and engineering instincts, and leokennis praised ChatGPT Plus as effectively limitless and reliable for average users.

**Tags**: `#AI`, `#LLM`, `#OpenAI`, `#model-release`, `#pricing`

---

<a id="item-2"></a>
## [Anthropic Ships Claude Opus 5.5 With Cheaper Tokens](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic announced Claude Opus 5.5, a new frontier model that the company says communicates more naturally and with clearer writing than Opus 5, whose work is "easier to follow and check." The release also cuts token pricing across the board per million tokens: cache reads from $0.50 to $0.20, input tokens from $5 to $4, output tokens from $25 to $20, and cache writes from $6.25 to $5. This is Anthropic's first release since it publicly called for "pacing the frontier," a tension many commenters immediately flagged, and the across-the-board price cuts directly affect the economics of building on a model that was reportedly the highest-spend model on OpenRouter. Cheaper frontier tokens lower costs for developers and put pressure on competing providers, including low-cost alternatives such as DeepSeek. According to Reuters, Anthropic says Opus 5.5 delivers performance comparable to its top-tier Fable 5.1 while costing 40% less to run than its predecessor. Pricing is quoted per million tokens with separate rates for input, output, cache reads and cache writes, and Anthropic's documentation recommends that existing Opus 5 users consider migrating to 5.5 for improved performance.

hackernews · km144 · Sep 22, 16:29 · [Discussion](https://news.ycombinator.com/item?id=49803892)

**Background**: Frontier models are the most advanced general-purpose AI models, capable of reasoning, multimodal generation and agentic workflows, and they are typically trained on massive datasets with enormous compute. Such models are usually billed by token — a token is roughly a chunk of text of about four characters — with separate per-million-token rates for the prompt (input) and the model's response (output), plus discounted rates for cached context. Claude Opus is Anthropic's flagship model line, and OpenRouter is a third-party marketplace that routes requests to many models and publishes spend rankings, which is how commenters gauge real-world usage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/anthropic-unveils-claude-opus-55-2026-09-22/">Anthropic unveils Claude Opus 5.5 - Reuters</a></li>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.solvimon.com/glossary/ai-token-pricing">What is AI Token Pricing ? | Solvimon Glossary</a></li>

</ul>
</details>

**Discussion**: Commenters fixated on the contrast between Anthropic's recent "pacing the frontier" call and a launch that, in one user's words, "demonstrates with very specific numbers how they absolutely are not pacing." The price cuts were broadly welcomed, with users comparing the new rate card to Opus 5 line by line, while others said they were content sticking with cheaper alternatives like DeepSeek v4.1; developer Simon Willison added his customary pelican test across the low, medium, high and xhigh thinking levels.

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Model Release`

---

<a id="item-3"></a>
## [Pentagon: AI Overreliance Contributed to Strike on Iranian School](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 9.0/10

A Pentagon report concluded that the United States "failed in its obligation to do everything feasible to verify" that a school in Minab, Iran, was a military objective, and that the failure "went beyond mere negligence." The report cited overreliance on the AI-assisted targeting system Maven as a contributing factor in the missile strike that killed civilians. This is one of the first official government findings directly linking AI-assisted targeting to civilian casualties, making it a potential turning point for military AI policy, procurement of systems like Palantir's Maven, and international debate over accountability for algorithmic warfare. It also intensifies pressure to define who — if anyone — is legally responsible when an algorithm contributes to killing non-combatants. According to the reporting, the Minab site had been cataloged as an Islamic Revolutionary Guard Corps facility based on outdated data, was fed into Maven alongside other candidates, and emerged as a recommendation; officials said some users expected Maven to flag stale records or contradictions in the assembled intelligence, though it is unclear why they believed the system would do so. The episode has also produced finger-pointing, with the Pentagon effectively blaming the software while Palantir attributes the outcome to bad input data.

hackernews · devonnull · Sep 22, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49806430)

**Background**: Maven (originally Project Maven) is a U.S. Department of Defense initiative, now closely associated with Palantir software, that applies machine learning to analyze surveillance imagery and intelligence and flag potential targets for human operators. Such systems are usually defended by the presence of a "human in the loop" who is meant to review every machine recommendation, a safeguard critics argue often degrades into rubber-stamping. Central to this debate is "automation bias," the well-documented human tendency to favor suggestions from automated systems and discount contradictory evidence, and the broader question of lethal autonomous weapons systems, which the United Nations has discussed for possible prohibition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.defensenews.com/opinion/2026/03/26/the-militarys-fabled-human-in-the-loop-for-ai-is-dangerously-misleading/">The military’s fabled ‘human in the loop’ for AI is dangerously misleading</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automation_bias">Automation bias</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapons_systems">Lethal autonomous weapons systems</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely rejected the framing that AI itself was the culprit, arguing the root cause was the human decision to delegate significant lethal decision-making authority to a machine, and that an algorithm cannot be put on trial so a responsible human must exist for every action. Others highlighted the accountability vacuum between the Pentagon and Palantir, criticized officials who embraced AI without understanding its limitations, and noted that the system was never designed to detect stale or contradictory data.

**Tags**: `#AI ethics`, `#military AI`, `#accountability`, `#AI safety`, `#civilian casualties`

---

<a id="item-4"></a>
## [vLLM v0.30.0 ships 762 commits with Fast Start GPU weight cache](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM released v0.30.0, a major versioned update containing 762 commits from 315 contributors (104 of them new). The release adds support for a large set of new frontier models — including DeepSeek-V4.1-Flash, DeepSeek-V4-Flash-Vision-Exp, GLM-5.3-Flash, K2-Horizon, Cohere Compass, Bailing V3 VL and Nanbeige4.2 — plus a persistent per-GPU weight-cache "Fast Start" daemon, Gumbel-max watermarking, the HiSparse host-resident KV tier, and expanded quantization and CPU backend kernels. vLLM is one of the most widely used open-source LLM inference and serving engines, so this release immediately affects anyone deploying models in production. The Fast Start weight cache and the new model support reduce cold-start latency and shorten the gap between a model's publication and its availability in a high-throughput serving stack, while the CPU backend and quantization work broaden the hardware vLLM can run on economically. Fast Start keeps post-quantized, tensor-parallel-sharded weights resident in GPU memory so a restarting engine can map them over CUDA IPC via `--load-format ipc_cache` instead of reloading from disk, and it now covers FP4 checkpoints and multi-node tensor parallelism. Other notable specifics include MXFP8 KV storage for DeepSeek-V4.1-Flash through the FlashMLA V4.1 record on SM100, an AVX512/AMX sparse MLA CPU backend for DeepSeek-V4, Model Runner V2 changes that cut CUDA graph capture from 12s to 2s and engine init from 28.9s to 8.2s on H200, and a fix for an approximately 2x RL step-time regression via `--return-sampling-mask`.

github · khluu · Sep 22, 05:20

**Background**: vLLM is a high-throughput serving engine for large language models; its core innovation, PagedAttention, manages the KV cache (the cached key/value tensors that let a model reuse context across tokens) in paged blocks rather than one contiguous buffer, which is what allows it to batch many concurrent requests efficiently. FlashMLA is DeepSeek's library of optimized Multi-head Latent Attention (MLA) kernels, the attention variant used by DeepSeek models to shrink KV cache size. Engram is a DeepSeek conditional-memory technique that uses deterministic hash lookups into a large embedding table, allowing the system to prefetch memory entries from host DRAM while the GPU computes other layers. MXFP8 is a low-precision 8-bit floating-point format with shared block scaling that post-training quantization studies find is close to lossless on many models and tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>
<li><a href="https://generativeai.pub/deepseeks-engram-the-lookup-table-that-eats-transformer-layers-90b5f6a99a90">DeepSeek’s Engram : The Lookup Table That Eats... | Generative AI</a></li>
<li><a href="https://www.alphaxiv.org/abs/2601.09555">Benchmarking Post-Training Quantization of Large... | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#model-serving`, `#deepseek`, `#release`

---

<a id="item-5"></a>
## [Hackers claim FBI employee data theft via Oracle PeopleSoft zero-day](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

Hackers claiming "we hacked the FBI" say they have exfiltrated data covering all FBI employees, according to a report by 404 Media. The attackers allegedly gained access through an Oracle PeopleSoft zero-day, prompting widespread debate about the exposed data and the underlying vulnerability. If confirmed, a breach affecting an entire federal agency's employee roster would be a major national-security incident, exposing personnel to targeting, identity theft, and social-engineering attacks. Because PeopleSoft is widely deployed across government and enterprises, a zero-day in it could signal that many other organizations running the same software are also at risk. The claim is attributed to an Oracle PeopleSoft zero-day, meaning a previously unknown flaw for which the vendor had zero days to prepare a fix before exploitation. Reports circulating in the cybersecurity community describe such a flaw as a critical, remotely exploitable vulnerability in PeopleSoft, though the FBI breach claim itself remains unverified by independent parties.

hackernews · spenvo · Sep 22, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49805278)

**Background**: Oracle PeopleSoft is an enterprise software suite, originally developed by PeopleSoft Corporation and later acquired by Oracle, that centralizes HR, payroll, finance, and student records for large organizations and government agencies. A zero-day vulnerability is a security flaw that was never previously known or reported, giving developers no time to patch it before attackers exploit it. The incident is being compared to the 2015 Office of Personnel Management (OPM) breach, in which roughly 22.1 million records of US government employees were compromised.

<details><summary>References</summary>
<ul>
<li><a href="https://mindmajix.com/what-is-peoplesoft">What is PeopleSoft | PeopleSoft Tutorial</a></li>
<li><a href="https://www.kaspersky.com/resource-center/definitions/zero-day-exploit">Zero - Day Exploits & Zero - Day Attacks</a></li>
<li><a href="https://medium.com/@Inforsecpro/oracle-peoplesoft-zero-day-rce-vulnerability-exposes-enterprise-systems-to-remote-compromise-a2baf6986401">Oracle PeopleSoft Zero Day RCE Vulnerability Exposes... | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters expressed broad pessimism about database security, with one arguing no organization seems capable of protecting large datasets and pointing to the OPM breach as precedent. Others highlighted that the involvement of an Oracle PeopleSoft zero-day likely means many more vulnerable systems exist, while several praised 404 Media for outpacing mainstream outlets and criticized agencies for prioritizing cost-cutting over security expertise.

**Tags**: `#cybersecurity`, `#data-breach`, `#fbi`, `#zero-day`, `#oracle-peoplesoft`

---

<a id="item-6"></a>
## [Claude Opus 5.5 Benchmarked at Max Reasoning Setting](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10

Artificial Analysis published an intelligence, performance and price analysis of Claude Opus 5.5 evaluated at the "max" reasoning setting, with separate companion pages for the "xhigh" and "medium" (default) settings. The analysis drew 202 points and 55 comments on Hacker News, driven largely by practitioners comparing reasoning budgets, cost per task and reliability. Reasoning-budget settings and cost-per-task are becoming decisive criteria for teams choosing a model, not just raw benchmark scores. A reported roughly 2x reduction in cost per task versus Opus 5 at comparable effort could shift real production workloads toward the newer model faster than headline intelligence gains alone would. The "max" setting can consume the entire 128,000-token reasoning budget before producing an answer — one commenter reported two failures on a simple SVG generation task for exactly that reason. Several commenters suggest the "high" setting is the practical sweet spot, since many benchmarks begin to plateau past it while cost continues to rise.

hackernews · theanonymousone · Sep 22, 16:51 · [Discussion](https://news.ycombinator.com/item?id=49804316)

**Background**: Artificial Analysis runs model-agnostic evaluations and publishes an aggregated Intelligence Index that combines reasoning, knowledge, math and coding datasets so models can be compared on a common footing. Reasoning models can spend extra compute at inference time by generating long chains of thought, and vendors expose this as adjustable effort settings such as medium, high, xhigh and max. Because higher effort means more tokens generated per request, it raises both latency and cost — which is why the trade-off between reasoning budget, quality and price per task is now a central topic in model selection.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/methodology/intelligence-benchmarking">Artificial Analysis Intelligence Benchmarking Methodology</a></li>
<li><a href="https://arxiv.org/html/2507.02076v1">Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs</a></li>
<li><a href="https://orq.ai/blog/model-vs-data-drift">Understanding Model Drift and Data Drift in LLMs (2026 Guide)</a></li>

</ul>
</details>

**Discussion**: Commenters were broadly positive but skeptical in the details: simonw documented a concrete failure where max-mode runs exhausted the 128k token budget mid-reasoning, and breckenedge raised the concern that vendors' launch benchmarks may not hold up in re-runs weeks later, warning about providers "pulling the rug" after users switch. On the positive side, hglaser highlighted the roughly 2x cost-per-task improvement over Opus 5, mchusma recommended the "high" setting as the best benchmark-to-cost balance, while linuxrebe1 said they had reverted to Opus 4.8 because Opus 5 was less stable at following instructions and staying on task.

**Tags**: `#LLM`, `#AI benchmarks`, `#Claude`, `#model pricing`, `#reasoning models`

---

<a id="item-7"></a>
## [TypeSafe AI launches Jev, a decision model returning typed probabilistic outputs](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI unveiled Jev, the first example of what it calls a "System One model" (others prefer "decision model"), which accepts text or semi-structured "state" input but returns floating-point numbers instead of text. For each question it can return a confidence score between 0 and 1 for a yes/no ("Noul") statement, a probability distribution over a set of choices, or a numeric score along a described range. It reframes LLM output as typed probabilistic decisions rather than free text, making classification-style tasks such as spam detection, label suggestion, prioritization and search reranking far cheaper and faster to build. With input priced at $0.042 per million tokens and output free, Jev undercuts even OpenAI's GPT-5 Nano ($0.05/million), which could push the industry toward specialized decision models alongside general-purpose chatbots. The API accepts one document plus as many questions as fit in the context window, and questions are evaluated in parallel, so asking many takes roughly the same time as asking one. TypeSafe's own "jaggedness" documentation for Jev 1.13 warns that the model is currently weak on numbers, dates, and adversarial content, and Simon Willison notes the deeper caveat that Jev offers no textual justification at all — just a float.

rss · Simon Willison · Sep 21, 23:09

**Background**: The name "System One" references Daniel Kahneman's distinction in Thinking, Fast and Slow between fast, automatic, intuitive System 1 thinking and slower, effortful System 2 reasoning. The "Noul" question type is short for Bernoulli, meaning the model returns the probability parameter of a Bernoulli distribution — a single number between 0 and 1 expressing how likely a statement is true. Unlike conventional LLMs, which are billed per input and output token with output priced higher, Jev charges only for input, reflecting that it emits a handful of numbers rather than generated text.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow">Thinking , Fast and Slow - Wikipedia</a></li>
<li><a href="https://thedecisionlab.com/reference-guide/philosophy/system-1-and-system-2-thinking">System 1 and System 2 Thinking - The Decision Lab</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#decision models`, `#AI models`, `#probabilistic reasoning`, `#TypeSafe AI`

---

<a id="item-8"></a>
## [Xiaomi Releases MiMo-V2.6 Omnimodal Models With $3.5M RL Training Cost](https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/) ⭐️ 8.0/10

Xiaomi has officially released and open-sourced the MiMo-V2.6 series, consisting of two natively omnimodal models — MiMo-V2.6-Pro and MiMo-V2.6-Flash — with a disclosed total reinforcement learning training cost of just $3.5M. The release also ships with a live "benchmaxxing" dashboard that streams the models' RL training metrics directly from the trainer's logs. A frontier-class multimodal model coming out of a consumer hardware company at a publicly disclosed $3.5M RL cost suggests that frontier-level multimodal post-training is becoming dramatically cheaper, which could lower the barrier for labs outside the usual Big Tech circle. Open-sourcing the weights alongside a live training dashboard also pushes a more transparent norm for how model claims are made and verified. MiMo-V2.6-Pro is described as Xiaomi's most capable model to date, while MiMo-V2.6-Flash targets the best balance of intelligence, efficiency and cost; the RL logs are published at mimo.xiaomi.com/rl/. The framing explicitly nods to "benchmaxxing" — the practice of optimizing for public leaderboards — so the disclosed $3.5M figure should be read as covering the reinforcement learning stage rather than the full pretraining pipeline, and the dashboard is self-reported rather than independently audited.

reddit · r/MachineLearning · /u/we_are_mammals · Sep 22, 07:56

**Background**: MiMo is Xiaomi's in-house large language model line; "omnimodal" means a single model natively handles text, images and audio rather than bolting separate encoders onto a text model. Reinforcement learning post-training on verifiable tasks is currently the main technique labs use to push reasoning and agentic ability beyond what supervised fine-tuning achieves, but it is normally expensive and rarely costed in public. Xiaomi says this release is a step toward RSI (recursive self-improvement) and is being "built in public," meaning weights, training metrics and costs are shared openly as the work progresses.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>
<li><a href="https://mimo.mi.com/docs/en-US/news/latest/v2-6">Xiaomi MiMo-V2.6 Series: 3 New Models Officially Released</a></li>
<li><a href="https://mimo.xiaomi.com/rl/">mimo-v2.6 RL - mimo.xiaomi.com</a></li>
<li><a href="https://ctaio.dev/en/labs/benchmaxxing/">What Is Benchmaxxing? The AI Benchmark Gaming Problem ...</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#LLM`, `#Multimodal`, `#Model Release`, `#Reinforcement Learning`

---

<a id="item-9"></a>
## [25 Fields Medalists Warn AI May Be Misaligned With Mathematics Research Goals](https://t.me/zaihuapd/43973) ⭐️ 8.0/10

A joint statement signed by 25 Fields medalists, including Terence Tao, warns that the rapid deployment of AI to solve mathematical problems may cause a "serious misalignment" between the goals of AI development and the goals of mathematical research. The signatories argue that although large language models have improved dramatically at solving major mathematical problems in recent years, treating math problem-solving as a benchmark for AI capability could damage mathematics research and the broader academic ecosystem. The statement comes from some of the most authoritative voices in mathematics, so it is likely to shape how AI labs, funders, and journals define and evaluate "mathematical ability" in AI systems. It signals growing concern that AI-generated output could distort research incentives, benchmarking priorities, and academic credit systems well beyond mathematics itself. The declaration stresses that the core of mathematical research is forming conceptual understanding and new insights rather than merely obtaining answers, and warns that AI-generated output in bulk could compress the time available for verification, communication, and citing prior work while raising issues of authorship and plagiarism. It also acknowledges that AI may improve research efficiency, with the outcome depending on how people choose to use the technology.

telegram · zaihuapd · Sep 22, 03:00

**Background**: The Fields Medal is widely regarded as the highest honor in mathematics, awarded every four years to up to four mathematicians, usually under the age of 40; Terence Tao, one of the signatories, received it in 2006. In recent years large language models have advanced quickly on mathematical benchmarks and competition-style problems, prompting debate about whether such results truly reflect mathematical reasoning. This declaration is part of a broader academic conversation about research ethics, authorship, and the use of AI in scholarly publishing.

**Tags**: `#AI`, `#Mathematics`, `#Research Ethics`, `#Large Language Models`, `#Academic Publishing`

---

<a id="item-10"></a>
## [DeepSeek and Tsinghua Release DSec Sandbox Platform Technical Report](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI and Tsinghua University jointly published a technical report titled "DeepSeek Elastic Compute (DSec)," detailing a production sandbox infrastructure that serves roughly 3 million sandbox instances per day, peaks at over 380,000 concurrent sandboxes, and creates over 5,000 instances per second. A single production unit of about 160 nodes can host 3,200 containers or 800 microVMs per node, and the platform exposes four backends — FnCall, container, Firecracker microVM, and full VM — through a unified SDK. Sandbox provisioning speed and density are a common bottleneck for reinforcement-learning-based agent training, so publishing concrete production numbers and architecture choices gives the wider AI systems community a reference design for scalable agent environments. It also highlights how deeply agent training now depends on systems-level infrastructure rather than just model or algorithm work. DSec loads EROFS images on demand via the 3FS distributed file system, which compared with traditional full Docker pulls cuts task completion time by 1.7x and disk writes by 57%, while memory sharing and reclamation reduce peak memory usage by roughly 40%. Architecturally, it decouples stateful rollout execution from preemptible GPU training so that RL frameworks can deeply coordinate with the sandbox layer.

telegram · zaihuapd · Sep 22, 04:45

**Background**: Agent training typically requires running untrusted, stateful workloads such as code execution, software engineering tasks, and computer-use interactions inside isolated environments, which is what a sandbox platform provides. DSec builds on Firecracker, AWS's open-source KVM-based lightweight virtualization that offers microVM isolation with fast startup and low memory overhead, and on EROFS, a lightweight read-only Linux file system designed for high-performance immutable images, alongside 3FS, DeepSeek's own distributed file system for AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://firecracker-microvm.github.io/">Firecracker</a></li>
<li><a href="https://en.wikipedia.org/wiki/EROFS">EROFS - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/nidhinkumar06_opensourceweek-3fs-distributedfilesystem-activity-7301297675969118212-UaxW">Introducing 3 FS : A High-Performance File System for AI | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Agent Training`, `#Sandbox Infrastructure`, `#Firecracker`, `#AI Systems`

---