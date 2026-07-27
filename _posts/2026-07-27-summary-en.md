---
layout: default
title: "Horizon Summary: 2026-07-27 (EN)"
date: 2026-07-27
lang: en
---

> From 29 items, 8 important content pieces were selected

---

1. [Kimi K3: Open-Source 2.8T Model Tops Frontend Code Arena](#item-1) ⭐️ 9.0/10
2. [Fastjson 1.x Critical RCE No Gadget Required](#item-2) ⭐️ 9.0/10
3. [vLLM v0.26.0: Inkling Support, DeepSeek-V4 Boost](#item-3) ⭐️ 8.0/10
4. [Libsm64 turns Super Mario 64 into reusable library for game engines](#item-4) ⭐️ 8.0/10
5. [Bun's Rust Rewrite Ships in Claude Code, Release Delayed](#item-5) ⭐️ 8.0/10
6. [Google Announces Gemini 4 as Most Ambitious Pre-Training Yet](#item-6) ⭐️ 8.0/10
7. [China Rejects US Sanctions on AI Distillation, Warns of Countermeasures](#item-7) ⭐️ 8.0/10
8. [SMIC Tests China's First Domestic DUV Lithography Machine](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3: Open-Source 2.8T Model Tops Frontend Code Arena](https://t.me/zaihuapd/42793) ⭐️ 9.0/10

Moon's Dark Side released Kimi K3, the world's first open-source 2.8 trillion parameter model. It achieved the top score of 1679 in the Frontend Code Arena benchmark, surpassing Fable 5. This release pushes the frontier of open-source AI by offering a massive model with novel architecture that outperforms leading proprietary models on coding tasks. It enables broad access to state-of-the-art capabilities for research and enterprise customization. K3 uses Kimi Delta Attention and Attention Residuals architecture, supports native vision and a 1 million token context window. It leads in 6 of 7 evaluation areas, trailing only in games.

telegram · zaihuapd · Jul 27, 06:27

**Background**: Kimi K3 is built on a hybrid linear attention architecture that combines Kimi Delta Attention (KDA), an expressive linear attention mechanism, with Attention Residuals (AttnRes), which replace standard residual connections with learned, input-dependent attention over depth. These innovations aim to improve efficiency and performance, especially for long contexts. The model is trained at 2.8 trillion parameters using a Mixture-of-Experts (MoE) approach.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.15031">[2603.15031] Attention Residuals - arXiv.org GitHub - MoonshotAI/Attention-Residuals Attention Residuals - arXiv.org Images Attention Residuals Explained: Rethinking Transformer Depth Attention Residuals by Kimi AI: A Clear Explanation Standard Transformer Attention vs. Attention-Residuals: A ... Attention Residuals: How Kimi Is Rethinking Transformer Depth</a></li>
<li><a href="https://arxiv.org/pdf/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://aitoolhunt.co/blog/kimi-k3-benchmarks-frontend-code-arena-2026">Kimi K3 Benchmarks : Frontend Leap and Review... | AIToolHunt</a></li>

</ul>
</details>

**Discussion**: Community comments highlight excitement about open-weight access for fine-tuning and IP sovereignty, though some note high hosting costs (estimated ~1.5TB VRAM) and commercial licensing restrictions requiring separate agreements for revenue above $20M. Pricing from initial providers shows $3/M tokens input and $15/M output.

**Tags**: `#AI`, `#open-source`, `#large language model`, `#benchmark`, `#architecture`

---

<a id="item-2"></a>
## [Fastjson 1.x Critical RCE No Gadget Required](https://t.me/zaihuapd/42797) ⭐️ 9.0/10

Security researcher Kirill Firsov disclosed a high-risk remote code execution vulnerability in Fastjson 1.x versions 1.2.68 through 1.2.83 that works without enabling autoType or relying on classpath gadgets on JDK 8, 17, and 21. This is a critical security issue for a widely used JSON library, and the only mitigation is upgrading to Fastjson2 since Fastjson 1.x is end-of-life and no patch will be provided. The vulnerability affects all Fastjson 1.x versions from 1.2.68 to 1.2.83, requires no specific conditions like autoType support, and is exploitable on multiple JDK versions including JDK 8, 17, and 21.

telegram · zaihuapd · Jul 27, 10:31

**Background**: Fastjson is a popular JSON processing library originally developed by Alibaba, widely used in Java applications. AutoType is a feature that allows polymorphic deserialization, which has been a common attack vector for deserialization vulnerabilities. The fact that this RCE works without autoType or gadgets makes it particularly dangerous.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Fastjson">Fastjson</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#RCE`, `#Fastjson`, `#Java`

---

<a id="item-3"></a>
## [vLLM v0.26.0: Inkling Support, DeepSeek-V4 Boost](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 (411 commits, 212 contributors) adds full support for the Thinking Machines Lab Inkling model family (1T-parameter multimodal MoE), delivers major performance improvements for DeepSeek-V4 (up to 2.94% E2E TPOT) via specialized kernels, introduces fp32 lm_head for generation models, and enables flexible attention backends per KV-cache group. This release significantly expands vLLM's model coverage with day-0 support for a major new open-weight model family (Inkling). The DeepSeek-V4 optimizations across NVIDIA, AMD, and Intel hardware lower inference costs for one of the most popular MoE architectures, while features like fp32 lm_head improve generation accuracy for many models. The Inkling support includes base modeling, piecewise CUDA graphs, Hopper FlashAttention-4 relative attention, MTP=1 speculative decoding, LoRA, and ModelOpt NVFP4 quantization. For DeepSeek-V4, a specialized routing kernel improves E2E TPOT by 2.94%, and fused_topk_bias speeds up a kernel by 1.5–2x. The new head_dtype option allows fp32 lm_head for better accuracy, and attention backends can now be selected per KV-cache group.

github · khluu · Jul 27, 01:06

**Background**: vLLM is an open-source high-throughput LLM inference engine widely used for deploying large language models. The Inkling model by Thinking Machines Lab is a 1T-parameter multimodal Mixture-of-Experts (MoE) transformer supporting text, image, and audio inputs with up to 1M context length. FlashAttention-4 is a newer attention algorithm optimized for Hopper GPUs, and speculative decoding is a technique that uses a smaller draft model to accelerate inference of a larger target model without quality loss.

<details><summary>References</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance | vLLM Blog</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#performance optimization`, `#model support`

---

<a id="item-4"></a>
## [Libsm64 turns Super Mario 64 into reusable library for game engines](https://github.com/libsm64/libsm64) ⭐️ 8.0/10

Libsm64 is a software library that extracts the movement and rendering code from the reverse-engineered Super Mario 64 decompilation, providing a clean API for integration into external game engines like Half-Life 2. This enables unprecedented cross-game interoperability by allowing Mario's character to appear and behave naturally in other games, demonstrating the potential of reverse-engineering for creative mashups without needing blockchain or metaverse hype. The library is built on the complete decompilation of Super Mario 64 (Japan, US, Europe, Shindou, iQue releases) and requires the original game ROM to compile. It has been used in projects like Mario in Half-Life 2 and a standalone SDL2 demo.

hackernews · klaussilveira · Jul 27, 10:04 · [Discussion](https://news.ycombinator.com/item?id=49067352)

**Background**: Super Mario 64 was fully decompiled in 2019 by the sm64 decompilation project, yielding readable C code from the original Nintendo 64 binary. This decompilation, while legally distributing only the code (not assets), allows developers to understand and modify the game's logic. Libsm64 builds on that work by packaging key subsystems into a reusable library with a stable API.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/libsm64/libsm64">GitHub - libsm 64 / libsm 64 : Mario 64 as a library for use in external...</a></li>
<li><a href="https://github.com/n64decomp/sm64">GitHub - n64decomp/sm64: A Super Mario 64 decompilation, brought to you by a bunch of clever folks. · GitHub</a></li>

</ul>
</details>

**Discussion**: The community is highly enthusiastic, with commenters calling it 'incredible' and noting it fulfills the promise of the metaverse without the hype. Examples include Mario in Half-Life 2 and a question about ease of setup for non-engineers. A joke about selling Mario 64 as a service was also made.

**Tags**: `#reverse-engineering`, `#game development`, `#interoperability`, `#C++`

---

<a id="item-5"></a>
## [Bun's Rust Rewrite Ships in Claude Code, Release Delayed](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun's creator Jarred announced that the Rust rewrite of Bun has shipped in Claude Code over a month ago, and the Bun 1.4 release is delayed until a promised number of newly passing Node.js tests is achieved. This rewrite from Zig to Rust is a major architectural change for Bun, a popular JavaScript runtime, and could impact performance and compatibility. The delay signals a strong commitment to Node.js compatibility, which is critical for adoption. The Rust rewrite was enabled by using an LLM to translate the codebase, and the release is blocked by pending pull requests to improve Node.js test passing numbers. The target number was mentioned in a previous video but is not yet achieved.

hackernews · tomlockwood · Jul 27, 11:12 · [Discussion](https://news.ycombinator.com/item?id=49067854)

**Background**: Bun is an all-in-one JavaScript runtime, bundler, test runner, and package manager, designed as a fast alternative to Node.js. It was originally written in Zig, but the team decided to rewrite it in Rust for better ecosystem support and performance. Claude Code is an AI-powered coding assistant by Anthropic that can understand and edit codebases.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>

</ul>
</details>

**Discussion**: Jarred's comments provided transparency about the delay and the test number promise. Some commenters questioned the use of LLMs for translation, while another pointed to a Zig fork of Bun that claims sub-second build times by sticking with best practices, suggesting the rewrite may not have been strictly necessary.

**Tags**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#rewrite`, `#community update`

---

<a id="item-6"></a>
## [Google Announces Gemini 4 as Most Ambitious Pre-Training Yet](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

Google CEO Sundar Pichai revealed during Alphabet's Q2 2026 earnings call that Gemini 4 is now in training, describing it as the company's most ambitious pre-training project to date, with a planned release by the end of 2026. This signals Google's continued heavy investment in frontier AI and AGI, aiming to maintain a competitive edge against rivals like OpenAI. The release of Gemini 4 could advance capabilities in reasoning, coding, and multimodal understanding. Pichai emphasized that compute resources are being prioritized for frontier AGI development, and the model is expected to launch around November or December 2026. Meanwhile, the Gemini 3.x Flash series will continue monthly updates focused on coding capabilities.

telegram · zaihuapd · Jul 27, 04:06

**Background**: Pre-training involves training a large machine learning model on a vast, generic dataset to learn general patterns before fine-tuning for specific tasks. Artificial General Intelligence (AGI) refers to a hypothetical AI system that can match or surpass human cognitive abilities across a wide range of tasks. Google, like several other tech companies, has publicly stated AGI as a long-term goal.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre-trained transformer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence</a></li>

</ul>
</details>

**Tags**: `#Google`, `#Gemini 4`, `#AI`, `#Large Language Model`, `#AGI`

---

<a id="item-7"></a>
## [China Rejects US Sanctions on AI Distillation, Warns of Countermeasures](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 8.0/10

China's Ministry of Commerce publicly rejected US allegations that Chinese AI companies engage in illicit model distillation, stating that US firms also use Chinese models for training. The ministry warned of necessary countermeasures if US sanctions harm Chinese interests. This escalates US-China tech tensions and could impact global AI collaboration, as model distillation is a widely used technique. The dispute may lead to fragmented AI ecosystems and increased regulatory barriers for AI development. The Chinese statement cites that nearly 200 US startups have urged their government not to restrict access to Chinese open-source models. It also notes that model distillation is a common industry practice and not inherently illegal.

telegram · zaihuapd · Jul 27, 11:01

**Background**: Model distillation is a machine learning technique where a smaller student model learns from a larger teacher model to achieve similar performance with lower computational cost. US authorities have recently investigated Chinese AI firms for allegedly distilling frontier models from companies like OpenAI, raising intellectual property concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.intellectyx.com/model-distillation-ai-starter-guide-techniques-benefits-and-applications/">AI Model Distillation Guide: Techniques , Benefits & Applications</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#model distillation`, `#geopolitics`, `#China`, `#US sanctions`

---

<a id="item-8"></a>
## [SMIC Tests China's First Domestic DUV Lithography Machine](https://t.me/zaihuapd/42800) ⭐️ 8.0/10

SMIC is trialing China's first domestically developed deep ultraviolet (DUV) lithography machine, built by Shanghai startup Yuliangsheng, for 28nm chip production and exploring multi-patterning to reach 7nm and even 5nm nodes. This marks a significant step toward semiconductor self-sufficiency for China amid US export restrictions that block access to advanced EUV lithography systems from ASML. If successful, it could reduce China's reliance on foreign equipment for mature and advanced nodes. The machine uses mostly domestic components but still relies on some imported parts. SMIC is using it to produce 28nm chips and attempting multi-patterning for 7nm, though yields are currently low; industry insiders estimate mass production with stable yields will take one to two years, with volume production targeted by 2027.

telegram · zaihuapd · Jul 27, 14:10

**Background**: DUV lithography uses ultraviolet light (e.g., 193nm wavelength) to pattern chips, and is less advanced than EUV (13.5nm) which is required for cutting-edge nodes below 7nm. ASML dominates both DUV and EUV markets, but US export controls prevent ASML from selling EUV machines to China. Multi-patterning techniques, such as double or quadruple patterning, allow DUV systems to create smaller features by exposing the wafer multiple times, albeit with higher cost and lower yield.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multiple_patterning">Multiple patterning - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/duv-lithography-systems">See ASML's DUV lithography systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">Extreme ultraviolet lithography</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#lithography`, `#SMIC`, `#DUV`, `#China tech`

---