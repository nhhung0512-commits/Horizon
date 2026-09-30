---
layout: default
title: "Horizon Summary: 2026-09-30 (EN)"
date: 2026-09-30
lang: en
---

> From 33 items, 4 important content pieces were selected

---

1. [Google Announces Gemini 4 Argon, Its Most Advanced Frontier Model](#item-1) ⭐️ 9.0/10
2. [Blogger reverses anti-MCP stance, reigniting protocol-vs-CLI debate](#item-2) ⭐️ 8.0/10
3. [DeepSeek Open-Sources Full Huawei Ascend Software Stack](#item-3) ⭐️ 8.0/10
4. [Cloudflare to Enter the Public Certificate Authority Market](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google Announces Gemini 4 Argon, Its Most Advanced Frontier Model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 9.0/10

Google announced Gemini 4 Argon, a next-generation frontier model positioned for real-world coding, enterprise knowledge work, and cyber defense, with a reported 1M-token output limit. The model is rolling out first to trusted testers rather than immediately to the public API, enterprises, or consumers, alongside introductory pricing and official benchmark tables. Argon is Google DeepMind's bid to hold the frontier against Anthropic and OpenAI, and its cyber-defense and enterprise-work focus signals that the labs are competing on high-value professional and security workloads rather than chat benchmarks alone. Because agents built on the model are reportedly used inside Google to migrate C/C++ codebases to Rust, it also illustrates how frontier models are moving from novelty to internal production tooling. The notable specifics include a reported 1 million token output limit, an explicit cyber-defense framing, and a gated release that starts with trusted testers instead of a general developer or consumer rollout. Google says it will keep collecting feedback and iterating on guardrails before making Argon more broadly available, which leaves pricing and full API access uncertain for now.

hackernews · bradleyg223 · Sep 30, 20:04 · [Discussion](https://news.ycombinator.com/item?id=49913571)

**Background**: A frontier model is the most advanced class of AI model available at a given moment, typically a large foundation model trained on massive datasets at costs running into hundreds of millions of dollars, and used for reasoning, generation, and agentic workflows. Gemini is Google DeepMind's flagship family of such models, competing directly with OpenAI's GPT series and Anthropic's Claude. An AI agent is a system built on top of these models that can pursue goals, call tools, and autonomously execute multi-step tasks, which is why coding and cybersecurity are common showcases for new frontier releases.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon - The Keyword</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html">Google rolls out Gemini 4 Argon, its most advanced model - CNBC</a></li>
<li><a href="https://agentpedia.codes/blog/gemini-4-argon-complete-guide">Gemini 4 Argon: Complete Guide to Benchmarks, Pricing and ...</a></li>

</ul>
</details>

**Discussion**: Commenters were split: some shared striking capability anecdotes, such as a user who said Gemini 3.8 Flash attached GDB to a GPU driver, reverse-engineered a kernel queue ioctl interface, and wrote an LD_PRELOAD shim to get ROCm llama.cpp running on a Strix Halo machine. Others argued this is further evidence against Dario Amodei's "concentrating" thesis, pointing to a more distributed AI landscape across hyperscalers, neoclouds, startups, GPUs and ASICs, while a third group criticized the gated release, joking that Gemini still has not shaken the "can't release a model" allegations and questioning the value of paying for the AI Ultra plan.

**Tags**: `#AI`, `#LLM`, `#Google Gemini`, `#model release`, `#AI agents`

---

<a id="item-2"></a>
## [Blogger reverses anti-MCP stance, reigniting protocol-vs-CLI debate](https://earendil.com/posts/you-said-no-mcp/) ⭐️ 8.0/10

A blog post titled "You said no MCP" published on earendil.com documents the author's public reversal of a previously strong anti-MCP position, and the piece went on to draw roughly 587 points and 331 comments on Hacker News. Rather than a technical benchmark, it is a reflective account of changing one's mind about how AI agents should connect to tools. The MCP-versus-CLI question directly shapes how agent tooling is built and deployed across the industry, so a well-known practitioner publicly abandoning a hardline anti-MCP stance carries real weight in that argument. It also signals that the early-2026 wave of "MCP is dead" commentary may be giving way to a more nuanced consensus that standardization and ease of deployment matter as much as raw performance. The post is an opinion and analysis piece rather than a research result, so its value comes from the argument and the ensuing discussion. Commenters point to concrete non-coding uses, such as wiring MCP into complex macOS apps like rcmd, Clop and Lunar so they can be configured in natural language even with a local model such as Qwen, while others acknowledge MCP's known weaknesses in performance, robustness and consistency.

hackernews · yarapavan · Sep 30, 09:55 · [Discussion](https://news.ycombinator.com/item?id=49906637)

**Background**: The Model Context Protocol (MCP) is an open standard and open-source framework introduced by Anthropic in November 2024 to standardize how LLM-based AI systems integrate with external tools, systems and data sources, and it is now supported by Claude, ChatGPT, Visual Studio Code, Cursor and many others. In early 2026 a wave of prominent voices argued that command-line interfaces were a better fit for AI agents, citing lower context consumption, greater reliability and easier security review, which turned "MCP vs CLI" into a live community debate. This post sits squarely inside that debate, with the author explaining why a stance he once held firmly no longer seemed right.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://jannikreinhard.com/why-cli-tools-are-beating-mcp-for-ai-agents/">CLI Tools vs MCP: Better AI Agents With Less Context</a></li>

</ul>
</details>

**Discussion**: Sentiment in the thread is broadly supportive of the reversal: alin23 argues MCP is far more than a coding tool, citing MCP-driven natural-language configuration in macOS apps, while gk1 praises the team for publicly admitting a change of mind and quotes Armin Ronacher's essay on outdated strong opinions. CharlieDigital pushes back sharply on the anti-MCP influencer wave of March, noting that security, observability, deployment and operations arguments were ignored, and _fw accepts MCP's flaws but compares it to USB-C or HDMI — imperfect yet universally compatible standards that win anyway.

**Tags**: `#MCP`, `#AI agents`, `#developer tools`, `#LLM integration`, `#protocols`

---

<a id="item-3"></a>
## [DeepSeek Open-Sources Full Huawei Ascend Software Stack](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 8.0/10

On September 30, 2026, DeepSeek open-sourced a suite of foundational components targeting Huawei's Ascend platform, including the TileLang high-level language compilation toolchain, a compute library, and a distributed communication library. The release also bundles DeepGEMM Ascend, DeepEP Ascend, TileKernels, FlashMLA, and DeepSelect, which DeepSeek says reach performance close to hardware limits in multiple benchmarks and are being developed alongside Huawei's 128-card Ascend 950 supernode plan. This is one of the most complete attempts yet to build a CUDA-independent AI software stack for a domestic Chinese accelerator, giving Ascend users kernel-level and communication-level building blocks that were previously only mature on NVIDIA GPUs. It could materially lower the cost and friction of training and serving large models on Ascend, and it strengthens Huawei's position in the AI infrastructure market at a time when access to NVIDIA hardware remains constrained for Chinese firms. The components are explicitly positioned as counterparts to DeepSeek's existing NVIDIA stack, with TileLang serving as the unifying compilation layer; notably, DeepSeek's FlashMLA test script requires TileLang, Tile-Kernels, and DeepGEMM together, and DeepGEMM borrows concepts from NVIDIA's CUTLASS/CuTe while deliberately avoiding heavy reliance on their templates. The performance claims are self-reported by DeepSeek and have not yet been independently reproduced, and no version numbers, benchmark figures, or repository links were given in the announcement.

telegram · zaihuapd · Sep 30, 03:09

**Background**: TileLang is a tile-based domain-specific language and compilation system in which the tile is the core programming object spanning the memory hierarchy from global memory through shared memory and registers to compute and accumulators; it sits between low-level assembly and high-level DSLs, preserving hardware control while reducing programming complexity. FlashMLA (an efficient multi-head attention kernel) and DeepEP (an expert-parallel communication library) were originally released during DeepSeek's February 2025 'open source week' for NVIDIA GPUs, and the new release ports that same class of infrastructure to Ascend. Huawei's Ascend 950 supernode, showcased at WAIC 2026, is described by Huawei as the industry's largest-scale supernode and represents the company's push to provide large-scale compute for the foundation-model era.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnblogs.com/mysterious-llama/articles/20229077">TileLang 学习笔记（二）：从一个 Kernel 看懂 TileLang ...</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head ...</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient ...</a></li>
<li><a href="https://m.21jingji.com/article/20260717/herald/5ad90b573648444c183fea4752a207e8.html">WAIC上的算力重器： 华 为 昇 腾 950 超 节 点 真机现身 - 21财经</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Huawei Ascend`, `#AI Infrastructure`, `#Open Source`, `#LLM Training`, `#Compiler`

---

<a id="item-4"></a>
## [Cloudflare to Enter the Public Certificate Authority Market](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare announced it is applying to the Chrome, Apple, Microsoft and Mozilla root certificate programs to become a public certificate authority, and has signed an agreement with GlobalSign to acquire a widely trusted root certificate; issuance has not yet begun. The new CA will prioritize ACME-based automated issuance and renewal and plans to issue production-grade Merkle Tree Certificates (MTC) in the first quarter of 2027 for the post-quantum internet. Cloudflare becoming a public CA would bring one of the internet's largest infrastructure providers directly into the WebPKI trust ecosystem, potentially reshaping how certificates are issued, trusted and managed for millions of sites that already use its network. The ACME-first approach and the post-quantum MTC roadmap could push the whole industry toward more automated and quantum-resistant certificate issuance. Cloudflare is not starting from zero: it is acquiring an existing trusted root from GlobalSign rather than building trust from scratch, which could shorten the browser root-program review process, though application acceptance and any issuance are still pending. The MTC plan targets production issuance by Q1 2027, a timeline that reflects how costly and large post-quantum signatures would otherwise be in TLS handshakes.

telegram · zaihuapd · Sep 30, 06:26

**Background**: A certificate authority (CA) issues the digital certificates that browsers and operating systems use to verify a website's identity; trust flows from a self-signed root certificate that must be included in root programs such as Chrome's, Mozilla's, Apple's and Microsoft's, and being accepted into those programs is what makes a CA's certificates widely trusted. ACME is a protocol originally designed for Let's Encrypt that automates the issuance, renewal and revocation of certificates, removing manual steps from certificate lifecycle management. Merkle Tree Certificates are an emerging design that uses hash-based Merkle trees instead of large post-quantum signatures, aiming to keep certificates and handshakes small enough for the post-quantum era.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment">Automatic Certificate Management Environment - Wikipedia</a></li>
<li><a href="https://www.encryptionconsulting.com/merkle-tree-certificates/">Merkle Tree Certificates & Post - Quantum WebPKI</a></li>
<li><a href="https://www.thesslstore.com/blog/how-to-become-a-certificate-authority/">How to Become a Certificate Authority... - Hashed Out by The SSL Store</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#PKI`, `#TLS Certificates`, `#ACME`, `#Post-Quantum Cryptography`

---