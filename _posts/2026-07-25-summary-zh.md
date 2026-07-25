---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 24 条内容中筛选出 7 条重要资讯。

---

1. [vLLM v0.26.0 增加 Inkling 模型家族和 DeepSeek-V4 优化](#item-1) ⭐️ 9.0/10
2. [SGLang v0.5.16：推出 DSpark 推测解码与 Inkling 支持](#item-2) ⭐️ 8.0/10
3. [开放权重 AI 迎来其 Kubernetes 时刻](#item-3) ⭐️ 8.0/10
4. [Anthropic 发布 Claude Opus 5，价格仅为 Fable 5 的一半](#item-4) ⭐️ 8.0/10
5. [AMD 挑战 CUDA 护城河：内核生成与生产难题](#item-5) ⭐️ 8.0/10
6. [两部门发布离岸信托个税新规：每年须申报纳税](#item-6) ⭐️ 8.0/10
7. [微软借助 TPM 芯片封堵盗版 Windows 激活](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 增加 Inkling 模型家族和 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 9.0/10

vLLM v0.26.0 已发布，包含来自 212 位贡献者的 411 次提交，引入了对 Inkling 模型家族的全面支持、DeepSeek-V4 的重要性能优化、通过 head_dtype 实现的 fp32 lm_head，以及可按 KV 缓存组选择的灵活注意力后端。 此版本显著增强了对 Inkling（9750 亿参数）和 DeepSeek-V4 等大型混合专家模型的推理能力，这些模型处于 LLM 开发的前沿。灵活的注意力后端和 KV 卸载改进使得混合模型和长上下文模型的部署更加高效。 Inkling 的支持包括分段 CUDA 图、Hopper FA4 相对注意力、MTP=1 推测解码和 LoRA 适配器。DeepSeek-V4 获得了专用路由内核（端到端 TPOT 提升 2.94%）和 fused_topk_bias（内核加速 1.5–2 倍）。fp32 lm_head 提高了生成模型的精度，注意力后端现在可以按 KV 缓存组选择以支持混合模型。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，广泛用于服务大型语言模型。Inkling 是 Thinking Machines Lab 推出的 9750 亿参数多模态混合专家模型，支持文本、图像、音频输入和高达 100 万 token 的上下文。分段 CUDA 图是一种将模型计算拆分为多个部分的技术，允许对模型的一部分使用 CUDA 图，同时在 eager 模式下运行注意力，从而提升变长序列的性能。FlashAttention-4 是一款为 Hopper GPU 优化的注意力内核，通过 TMA 预取减少 softmax 流水线停顿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://docs.sglang.io/advanced_features/piecewise_cuda_graph.html">Piecewise CUDA Graph - SGLang Documentation</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#performance optimization`, `#open-source`

---

<a id="item-2"></a>
## [SGLang v0.5.16：推出 DSpark 推测解码与 Inkling 支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 8.0/10

SGLang v0.5.16 引入了 DSpark，一种基于置信度的推测解码算法，在 DeepSeek-V4-Pro 上达到 383.7 tok/s，并增加了对 Inkling 的支持，这是一个 975B 参数的多模态 MoE 模型，具有 1M token 的上下文。 此次发布通过一种新颖的推测解码方法显著提升了 LLM 推理吞吐量，并为最大的开源多模态模型之一提供了服务支持，为 SGLang 生态系统树立了新的性能标杆。 DSpark 以块为单位进行半自回归草稿，并利用置信度调整验证窗口大小；而 Inkling 混合了滑动窗口、全注意力和 Mamba2 线性注意力，并在 Blackwell 硬件上支持 NVFP4 MoE 和 MTP。

github · Qiaolin-Yu · 7月25日 00:13

**背景**: 推测解码通过使用较小模型生成草稿 token 并与目标模型并行验证来加速 LLM 推理。SGLang 是一个大型语言模型推理引擎，通过多种技术优化性能。Inkling 模型由 Thinking Machines Lab 发布，是一个 975B 参数的多模态 MoE，具有 41B 活跃参数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/deepseek-releases-dspark-speculative-decoding-checkpoints-alvaro-cuba-7iope">DeepSeek releases DSpark speculative decoding with checkpoints</a></li>
<li><a href="https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/">Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights Multimodal MoE With 41B Active Parameters And Controllable Thinking Effort - MarkTechPost</a></li>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/Inkling · Hugging Face</a></li>

</ul>
</details>

**标签**: `#speculative decoding`, `#LLM inference`, `#SGLang`, `#multimodal MoE`, `#performance`

---

<a id="item-3"></a>
## [开放权重 AI 迎来其 Kubernetes 时刻](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

文章认为，开放权重 AI 模型正成为标准化的开源 AI 平台，类似于 Kubernetes 在云基础设施中的作用。 这一类比抓住了 AI 基础设施的重要趋势，表明开放权重模型可能成为商品化层，促进广泛创新，类似于 Kubernetes 标准化容器编排的方式。 文章指出，开放权重模型为推理成本提供了基线，使价格波动趋于理性，并强调美国实验室需要以对初创企业友好的许可证发布前沿级开放权重模型。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重 AI 模型发布其训练参数（权重），允许他人运行、微调和适配，但可能不包含训练数据或代码，因此并非完全开源。Kubernetes 是一个用于自动化容器化应用部署、扩展和管理的开源系统，已成为行业标准。文章进行类比，认为开放权重模型可能同样成为 AI 的基础设施层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://medium.com/illumination/someone-just-built-kubernetes-for-ai-agents-and-it-might-change-how-we-deploy-everything-d07681ee1770">Someone Just Built Kubernetes for AI Agents And It Might... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论讨论了禁止中国模型的可行性、定价谜题（'代币经济学'）、合作开发开放模型的必要性，以及对 OpenAI 等主要实验室更频繁更新开放权重模型的期望。

**标签**: `#open-weight models`, `#AI infrastructure`, `#Kubernetes analogy`, `#open source AI`, `#LLM deployment`

---

<a id="item-4"></a>
## [Anthropic 发布 Claude Opus 5，价格仅为 Fable 5 的一半](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 8.0/10

Anthropic 发布了 Claude Opus 5，这款新模型的智能水平接近 Claude Fable 5，但价格仅为后者的一半，定价与 Opus 4.8 相同。该模型目前在 Artificial Analysis 排行榜上领先，甚至超过了 Fable 5。 Claude Opus 5 以显著更低的成本提供接近前沿的 AI 能力，可能使更多用户和应用能够使用先进 AI。其主动行为和改进的漏洞发现能力凸显了 AI 安全与能力的持续进步。 Opus 5 提供“快速模式”，价格为基本模式的两倍；并且故意未接受网络利用任务的训练，但由于通用能力的提升，其在发现漏洞方面仍有改进。Anthropic 还发布了该模型的提示指南。

rss · Simon Willison · 7月24日 23:48

**背景**: Anthropic 的 Claude 系列包括多个层级：Opus 是成本高效的系列，而 Fable 和 Mythos 是前沿模型。Claude Fable 5 于 2026 年 6 月发布，是一个具有安全措施的公开前沿模型。Artificial Analysis 排行榜根据性能、成本和执行时间对 AI 模型进行排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#announcement`

---

<a id="item-5"></a>
## [AMD 挑战 CUDA 护城河：内核生成与生产难题](https://newsletter.semianalysis.com/p/can-amd-break-the-cuda-moat-amd-advancing) ⭐️ 8.0/10

Bryan Shan 的分析详细介绍了 AMD 打破 NVIDIA CUDA 护城河的战略，包括代理内核生成、软件质量改进，以及 Helios MI455X 生产爬坡的挑战——工程财务部门提供了高达 105%的折扣。 这很重要，因为 AMD 成功打破 CUDA 护城河可能重塑 AI 硬件格局，为 NVIDIA 的主导生态系统提供替代方案，并可能降低 AI 基础设施成本。 Helios MI455X 采用 2nm 工艺，配备 432GB HBM4 内存，但生产问题导致内部折扣高达 105%。AMD 还在投资代理内核生成——一种 AI 驱动的自动生成优化 GPU 内核的方法，以减少对 CUDA 的软件依赖。

rss · Semianalysis · 7月25日 00:33

**背景**: NVIDIA 的 CUDA 平台长期以来一直是关键的护城河，通过广泛的软件库和工具将开发者锁定在其生态系统中。AMD 的竞争性 ROCm 软件栈在性能和易用性上历来落后。代理内核生成利用大语言模型自动编写和优化 GPU 代码，可能降低采用 AMD 硬件的门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/rackscale-solutions/helios.html">AMD Helios Rackscale Solution – Powering Frontier AI</a></li>
<li><a href="https://www.phoronix.com/news/AMD-Instinct-MI455X-Helios">AMD Launches Instinct MI455X, Helios AI Rack - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/amd-takes-the-wraps-off-its-instinct-mi455x-ai-accelerator-cdna-5-and-helios-rack-scale-architecture-combine-to-take-the-fight-to-nvidia-in-the-data-center">AMD takes the wraps off its Instinct MI455X AI accelerator — CDNA 5 and Helios rack-scale architecture combine to take the fight to Nvidia in the data center | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#AMD`, `#CUDA`, `#GPU`, `#AI hardware`, `#software ecosystem`

---

<a id="item-6"></a>
## [两部门发布离岸信托个税新规：每年须申报纳税](https://liaoning.chinatax.gov.cn/art/2026/7/24/art_5869_7823.html) ⭐️ 8.0/10

2026 年 7 月 24 日，中国财政部和税务总局联合发布第 21 号公告，要求居民个人就离岸信托装入的财产及信托收益（无论是否实际分配）按年申报纳税。 这封堵了此前通过不分配信托收益或将资产转移至离岸来延迟或逃避纳税的漏洞，对跨境财富管理和中国居民的合规产生重大影响。 税率统一为增值额（现值减原值和成本）的 20%。追溯条款要求在公告实施后 90 天内申报补缴 2023 年至 2025 年期间装入离岸信托及 2026 年前产生收益的应缴未缴税款，不加收滞纳金。

telegram · zaihuapd · 7月25日 00:31

**背景**: 离岸信托常被中国居民用于资产保护和税务规划，利用当地税法的漏洞。此前，信托内部留存收益在分配前不征税，财产装入信托也可能规避资本利得税。新规采用穿透式原则，对增值和收益按个人所得税按年征收。

**社区讨论**: 提供的内容中包含了来自 Telegram 频道的评论，用户对合规负担和追溯适用表示担忧。一些人讨论了 20%的统一税率和 90 天的补缴窗口，对打击逃税的态度不一。

**标签**: `#tax regulation`, `#offshore trust`, `#China`, `#individual tax`, `#crackdown on evasion`

---

<a id="item-7"></a>
## [微软借助 TPM 芯片封堵盗版 Windows 激活](https://www.techspot.com/news/113232-microsoft-using-tpm-chips-crack-down-pirated-windows.html) ⭐️ 8.0/10

微软宣布将为其批量激活工具 KMS 加入基于 TPM 芯片的硬件安全验证，要求 KMS 服务器先证明其硬件身份经过微软认证，之后才能处理激活请求。该功能将从下一版 Windows Server 起成为强制要求，并自 2026 年 8 月起在 Windows Server 2025 中推送准备提示。 此举针对长期被滥用的基于 KMS 的激活漏洞，可能让流行的盗版工具失效。然而，猫鼠游戏仍在继续：Massgrave 组织已推出 TSforge 方法，声称可以绕过微软整个 DRM 激活架构。 TPM 证明机制会检查 KMS 服务器的硬件身份是否经过微软认证且未被篡改。该功能从下一版 Windows Server 起成为强制要求，Windows Server 2025 将从 2026 年 8 月开始收到准备提示。

telegram · zaihuapd · 7月25日 15:55

**背景**: TPM（可信平台模块）是一种硬件芯片，用于安全存储加密密钥并确保系统未被篡改。KMS（密钥管理服务）是微软官方的批量激活机制，允许企业通过本地服务器批量激活 Windows 和 Office 产品。多年来，盗版者通过搭建伪造的 KMS 服务器来激活微软产品，无需付费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.microsoft.com/zh-CN/Windows/Security/Device-Security/what-s-a-trusted-platform-module-tpm">What's a Trusted Platform Module ( TPM )? | Microsoft Support</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1994168045015429993">KMS激活及其原理 - 知乎</a></li>
<li><a href="https://github.com/massgravel/massgrave.dev/blob/main/docs/tsforge.md">massgrave.dev/docs/tsforge.md at main · massgravel ... - GitHub</a></li>

</ul>
</details>

**标签**: `#Windows`, `#TPM`, `#DRM`, `#反盗版`, `#KMS`

---