---
layout: default
title: "Horizon Summary: 2026-07-25 (EN)"
date: 2026-07-25
lang: en
---

> From 24 items, 7 important content pieces were selected

---

1. [vLLM v0.26.0 adds Inkling model family and DeepSeek-V4 optimizations](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.16: DSpark Speculative Decoding and Inkling Support](#item-2) ⭐️ 8.0/10
3. [Open-weight AI is having its Kubernetes moment](#item-3) ⭐️ 8.0/10
4. [Anthropic Releases Claude Opus 5 at Half the Price of Fable 5](#item-4) ⭐️ 8.0/10
5. [AMD's CUDA Moat Challenge: Kernel Generation and Production Hurdles](#item-5) ⭐️ 8.0/10
6. [China Issues Offshore Trust Tax Rules: Annual Declaration Required](#item-6) ⭐️ 8.0/10
7. [Microsoft Uses TPM Chips to Block Pirated Windows Activation](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 adds Inkling model family and DeepSeek-V4 optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 has been released with 411 commits from 212 contributors, introducing full support for the Inkling model family, significant performance optimizations for DeepSeek-V4, fp32 lm_head via head_dtype, and flexible attention backends that can be selected per KV-cache group. This release significantly enhances the serving capabilities for large Mixture-of-Experts models like Inkling (975B parameters) and DeepSeek-V4, which are at the forefront of LLM development. The flexible attention backends and KV offloading improvements enable more efficient deployment of hybrid and long-context models. The Inkling support includes piecewise CUDA graphs, Hopper FA4 relative attention, MTP=1 speculative decoding, and LoRA adapters. DeepSeek-V4 gains a specialized routing kernel (2.94% E2E TPOT improvement) and fused_topk_bias (1.5–2x kernel speedup). fp32 lm_head improves accuracy for generation models, and attention backends can now be selected per KV-cache group for hybrid models.

github · khluu · Jul 25, 10:38

**Background**: vLLM is an open-source high-throughput LLM inference engine widely used for serving large language models. Inkling is a 975B-parameter multimodal Mixture-of-Experts model from Thinking Machines Lab, supporting text, image, audio inputs and up to 1M token context. Piecewise CUDA graph is a technique that splits model computation into pieces, allowing CUDA graphs to be used for parts of the model while running attention in eager mode, improving performance for variable-length sequences. FlashAttention-4 is an optimized attention kernel for Hopper GPUs that reduces softmax pipeline stalls via TMA prefetch.

<details><summary>References</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://docs.sglang.io/advanced_features/piecewise_cuda_graph.html">Piecewise CUDA Graph - SGLang Documentation</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#model serving`, `#performance optimization`, `#open-source`

---

<a id="item-2"></a>
## [SGLang v0.5.16: DSpark Speculative Decoding and Inkling Support](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 8.0/10

SGLang v0.5.16 introduces DSpark, a confidence-driven speculative decoding algorithm achieving 383.7 tok/s on DeepSeek-V4-Pro, and adds support for Inkling, a 975B-parameter multimodal MoE model with 1M-token context. This release significantly boosts LLM inference throughput with a novel speculative decoding method and enables serving one of the largest open-weight multimodal models, setting new performance benchmarks for the SGLang ecosystem. DSpark drafts semi-autoregressively in blocks and uses confidence to size verify windows, while Inkling mixes sliding-window, full, and Mamba2 linear attention with NVFP4 MoE and MTP support on Blackwell hardware.

github · Qiaolin-Yu · Jul 25, 00:13

**Background**: Speculative decoding accelerates LLM inference by generating draft tokens with a smaller model and verifying them in parallel with the target model. SGLang is an inference engine for large language models, optimizing performance through various techniques. The Inkling model, released by Thinking Machines Lab, is a 975B-parameter multimodal MoE with 41B active parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/deepseek-releases-dspark-speculative-decoding-checkpoints-alvaro-cuba-7iope">DeepSeek releases DSpark speculative decoding with checkpoints</a></li>
<li><a href="https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/">Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights Multimodal MoE With 41B Active Parameters And Controllable Thinking Effort - MarkTechPost</a></li>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/Inkling · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#speculative decoding`, `#LLM inference`, `#SGLang`, `#multimodal MoE`, `#performance`

---

<a id="item-3"></a>
## [Open-weight AI is having its Kubernetes moment](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

The article argues that open-weight AI models are becoming the standardized, open-source platform for AI, analogous to Kubernetes' role in cloud infrastructure. This analogy captures a significant trend in AI infrastructure, suggesting that open-weight models could become the commoditized layer that enables broad innovation, similar to how Kubernetes standardized container orchestration. The article notes that open-weight models provide a baseline for inference costs, bringing sanity to pricing fluctuations, and emphasizes the need for American labs to release frontier-grade open-weight models under startup-friendly licenses.

hackernews · tknaup · Jul 25, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49048034)

**Background**: Open-weight AI models release their trained parameters (weights), allowing others to run, fine-tune, and adapt them, but they may not include training data or code, so they are not fully open-source. Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications, which became the industry standard. The article draws a parallel, arguing that open-weight models could similarly become the infrastructure layer for AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://medium.com/illumination/someone-just-built-kubernetes-for-ai-agents-and-it-might-change-how-we-deploy-everything-d07681ee1770">Someone Just Built Kubernetes for AI Agents And It Might... | Medium</a></li>

</ul>
</details>

**Discussion**: The community comments discuss the feasibility of banning Chinese models, pricing puzzles ('tokenomics'), the need for collaboration on open models, and the desire for more frequently updated open-weight models from major labs like OpenAI.

**Tags**: `#open-weight models`, `#AI infrastructure`, `#Kubernetes analogy`, `#open source AI`, `#LLM deployment`

---

<a id="item-4"></a>
## [Anthropic Releases Claude Opus 5 at Half the Price of Fable 5](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 8.0/10

Anthropic announced Claude Opus 5, a new model that approaches the frontier intelligence of Claude Fable 5 at half the price, priced the same as Opus 4.8. It currently leads the Artificial Analysis leaderboard, even ahead of Fable 5. Claude Opus 5 offers near-frontier AI capabilities at a significantly lower cost, potentially democratizing access to advanced AI for more users and applications. Its proactive behavior and improved vulnerability finding highlight ongoing advancements in AI safety and capability. Opus 5 includes a 'fast mode' at twice the base cost and has been deliberately not trained on cyber exploit tasks, yet improved at finding vulnerabilities due to general capability gains. Anthropic also released a prompting guide for the model.

rss · Simon Willison · Jul 24, 23:48

**Background**: Anthropic's Claude family includes multiple tiers: Opus is the cost-efficient line, while Fable and Mythos are frontier models. Claude Fable 5, released in June 2026, is a publicly available frontier model with safeguards. The Artificial Analysis leaderboard ranks AI models based on performance, cost, and execution time.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#announcement`

---

<a id="item-5"></a>
## [AMD's CUDA Moat Challenge: Kernel Generation and Production Hurdles](https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing) ⭐️ 8.0/10

Bryan Shan's analysis details AMD's strategies to break NVIDIA's CUDA moat, including agentic kernel generation, software quality improvements, and the challenging Helios MI455X production ramp with up to 105% discounts from finance engineering. This matters because AMD's success in overcoming the CUDA moat could reshape the AI hardware landscape, offering an alternative to NVIDIA's dominant ecosystem and potentially lowering costs for AI infrastructure. The Helios MI455X features 432GB HBM4 memory on a 2nm process, though production issues led to internal discounts of up to 105%. AMD is also investing in agentic kernel generation, an AI-driven method to automatically generate optimized GPU kernels, to reduce software dependency on CUDA.

rss · Semianalysis · Jul 25, 00:33

**Background**: NVIDIA's CUDA platform has long been a critical moat, locking developers into its ecosystem through extensive software libraries and tooling. AMD's competing ROCm stack has historically lagged in performance and ease of use. Agentic kernel generation uses large language models to automatically write and optimize GPU code, potentially lowering the barrier for AMD hardware adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/rackscale-solutions/helios.html">AMD Helios Rackscale Solution – Powering Frontier AI</a></li>
<li><a href="https://www.phoronix.com/news/AMD-Instinct-MI455X-Helios">AMD Launches Instinct MI455X, Helios AI Rack - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center">AMD takes the wraps off its Instinct MI455X AI accelerator — CDNA 5 and Helios rack-scale architecture combine to take the fight to Nvidia in the data center | Tom's Hardware</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#CUDA`, `#GPU`, `#AI hardware`, `#software ecosystem`

---

<a id="item-6"></a>
## [China Issues Offshore Trust Tax Rules: Annual Declaration Required](https://liaoning.chinatax.gov.cn/art/2026/7/24/art_5869_7823.html) ⭐️ 8.0/10

On July 24, 2026, China's Ministry of Finance and State Administration of Taxation jointly issued Announcement No. 21, requiring resident individuals to declare and pay tax annually on assets placed into offshore trusts and on trust income, regardless of actual distribution. This closes previous loopholes that allowed taxpayers to defer or avoid tax by not distributing trust income or by placing assets offshore. It significantly impacts cross-border wealth management and compliance for Chinese residents. The tax rate is a flat 20% on gains (appreciation minus original value and costs). Retroactive provisions require declaring and paying tax for trust placements from 2023 to 2025 and pre-2026 income within 90 days, without late payment penalties.

telegram · zaihuapd · Jul 25, 00:31

**Background**: Offshore trusts have been used by Chinese residents for asset protection and tax planning, often exploiting gaps in local tax law. Previously, income retained within the trust was not taxed until distribution, and asset transfers could avoid capital gains tax. The new rule adopts a 'look-through' approach, taxing gains and income annually on a personal basis.

**Discussion**: The provided content includes comments from a Telegram channel where users express concerns about compliance burdens and retroactive application. Some discuss the 20% flat rate and the 90-day window for back taxes, with mixed feelings about the crackdown on tax evasion.

**Tags**: `#tax regulation`, `#offshore trust`, `#China`, `#individual tax`, `#crackdown on evasion`

---

<a id="item-7"></a>
## [Microsoft Uses TPM Chips to Block Pirated Windows Activation](https://www.techspot.com/news/113232-microsoft-using-tpm-chips-crack-down-pirated-windows.html) ⭐️ 8.0/10

Microsoft announced it will add TPM-based hardware security verification to its KMS volume activation tool, requiring KMS servers to prove their hardware identity is certified before processing activation requests. This feature will become mandatory in the next Windows Server release, with preparatory prompts rolling out on Windows Server 2025 starting August 2026. This move targets the widely abused KMS-based activation exploits, potentially shutting down popular pirate tools. However, the cat-and-mouse game continues as the Massgrave group has already released TSforge, a method claiming to bypass Microsoft's entire DRM activation architecture. The TPM attestation mechanism checks whether the KMS server's hardware identity has been certified by Microsoft and has not been tampered with. It is a mandatory step from the next Windows Server version, and Windows Server 2025 will receive preparatory notifications starting August 2026.

telegram · zaihuapd · Jul 25, 15:55

**Background**: A Trusted Platform Module (TPM) is a hardware chip that securely stores cryptographic keys and ensures the system has not been tampered with. KMS (Key Management Service) is Microsoft's official volume activation mechanism for enterprises, allowing bulk activation of Windows and Office via a local server. For years, pirates have exploited KMS by setting up fake KMS servers to activate Microsoft products without payment.

<details><summary>References</summary>
<ul>
<li><a href="https://support.microsoft.com/zh-CN/Windows/Security/Device-Security/what-s-a-trusted-platform-module-tpm">What's a Trusted Platform Module ( TPM )? | Microsoft Support</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1994168045015429993">KMS激活及其原理 - 知乎</a></li>
<li><a href="https://github.com/massgravel/massgrave.dev/blob/main/docs/tsforge.md">massgrave.dev/docs/tsforge.md at main · massgravel ... - GitHub</a></li>

</ul>
</details>

**Tags**: `#Windows`, `#TPM`, `#DRM`, `#反盗版`, `#KMS`

---