---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 33 条内容中筛选出 4 条重要资讯。

---

1. [谷歌发布 Gemini 4 Argon，其最先进的前沿模型](#item-1) ⭐️ 9.0/10
2. [博主公开推翻反 MCP 立场，重燃协议与 CLI 之争](#item-2) ⭐️ 8.0/10
3. [DeepSeek 开源完整华为昇腾基础软件栈](#item-3) ⭐️ 8.0/10
4. [Cloudflare 宣布进军公共证书颁发机构市场](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 4 Argon，其最先进的前沿模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 9.0/10

谷歌发布了新一代前沿模型 Gemini 4 Argon，定位为面向真实世界编程、企业知识工作和网络防御的旗舰模型，据称支持 100 万 token 的输出上限。该模型首批仅向受信任的测试者开放，而非立刻登陆公共 API、企业客户和普通消费者，同时公布了入门价格与官方基准测试数据。 Argon 是谷歌 DeepMind 在 Anthropic 与 OpenAI 夹击下守住前沿地位的押注，其聚焦网络防御与企业工作负载，说明各大实验室的竞争已从聊天基准转向高价值的专业与安全场景。由于据称基于该模型的智能体已在谷歌内部被用于把 C/C++ 代码库迁移到 Rust，它也表明前沿模型正从新奇的演示走向企业内部的生产工具。 值得注意的细节包括据称 100 万 token 的输出上限、明确的网络防御定位，以及先从受信任测试者开始、而非直接面向开发者和消费者的受限发布方式。谷歌表示会继续收集反馈并迭代安全护栏，之后才更广泛地开放 Argon，这意味着其价格与完整 API 访问权限目前仍不确定。

hackernews · bradleyg223 · 9月30日 20:04 · [社区讨论](https://news.ycombinator.com/item?id=49913571)

**背景**: 前沿模型指的是在某一时点上最先进的一类 AI 模型，通常是在海量数据上训练、成本高达数亿美元的大型基础模型，用于推理、内容生成和智能体工作流。Gemini 是谷歌 DeepMind 旗下的旗舰模型系列，直接与 OpenAI 的 GPT 系列和 Anthropic 的 Claude 竞争。AI 智能体则是构建在这些模型之上、能够追求目标、调用工具并自主完成多步任务的系统，这也是编程与网络安全常被用作新前沿模型展示场景的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon - The Keyword</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html">Google rolls out Gemini 4 Argon, its most advanced model - CNBC</a></li>
<li><a href="https://agentpedia.codes/blog/gemini-4-argon-complete-guide">Gemini 4 Argon: Complete Guide to Benchmarks, Pricing and ...</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧明显：有人分享了惊人的能力案例，例如一位用户称 Gemini 3.8 Flash 将 GDB 附加到 GPU 驱动上，逆向分析了内核队列的 ioctl 接口，并编写 LD_PRELOAD C 垫片让 ROCm 版 llama.cpp 在 Strix Halo 机器上跑通。也有人认为这进一步证明 Dario Amodei 的“集中化”论断有误，指出 AI 格局正分散于超大规模云厂商、新型云服务商、初创公司以及 GPU 与 ASIC 之间；还有一派批评这种受限发布方式，调侃 Gemini 仍未能摆脱“发布不出模型”的指责，并质疑订阅 AI Ultra 套餐的价值。

**标签**: `#AI`, `#LLM`, `#Google Gemini`, `#model release`, `#AI agents`

---

<a id="item-2"></a>
## [博主公开推翻反 MCP 立场，重燃协议与 CLI 之争](https://earendil.com/posts/you-said-no-mcp/) ⭐️ 8.0/10

earendil.com 上题为《You said no MCP》的博文记录了作者公开推翻自己此前坚定的反 MCP 立场，该文在 Hacker News 上获得了约 587 分和 331 条评论。它并不是一篇技术基准测试，而是一篇反思性文章，讲述作者如何在“AI 智能体该如何连接工具”这一问题上改变了看法。 MCP 与 CLI 之争直接影响整个行业构建和部署智能体工具的方式，因此一位知名实践者公开放弃强硬的反 MCP 立场，在这场争论中颇具分量。这也意味着 2026 年初那波“MCP 已死”的论调可能正在让位于一种更微妙的共识：标准化与易部署的重要性不亚于单纯的性能表现。 这篇文章属于观点与分析类内容，而非研究成果，因此其价值主要来自论证和随之而来的讨论。评论者给出了具体的非编程用途，例如把 MCP 接入 rcmd、Clop、Lunar 等复杂的 macOS 应用，使其即便配合 Qwen 这类本地模型也能用自然语言进行配置；同时也有人承认 MCP 在性能、健壮性和一致性方面存在已知短板。

hackernews · yarapavan · 9月30日 09:55 · [社区讨论](https://news.ycombinator.com/item?id=49906637)

**背景**: Model Context Protocol（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准与开源框架，旨在统一基于大语言模型的 AI 系统与外部工具、系统和数据源之间的集成方式，目前已得到 Claude、ChatGPT、Visual Studio Code、Cursor 等众多客户端的支持。2026 年初，一批知名人士主张命令行界面（CLI）更适合 AI 智能体，理由是上下文消耗更低、可靠性更高、安全审查更容易，这使“MCP 与 CLI 之争”成为社区热议的话题。这篇文章正处在这场争论之中，作者解释了自己曾经坚定持有的立场为何不再成立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://jannikreinhard.com/why-cli-tools-are-beating-mcp-for-ai-agents/">CLI Tools vs MCP: Better AI Agents With Less Context</a></li>

</ul>
</details>

**社区讨论**: 评论区的整体情绪普遍支持作者的立场转变：alin23 认为 MCP 远不止是编程工具，并以 macOS 应用中的 MCP 自然语言配置为例；gk1 则赞赏作者团队公开承认改变想法，并引用了 Armin Ronacher 关于“过时强硬观点”的文章。CharlieDigital 对三月份那波反 MCP 的网红浪潮提出尖锐批评，指出安全、可观测性、部署与运维等论据当时被完全忽视；_fw 则承认 MCP 的缺陷，但将其比作 USB-C 或 HDMI——虽不完美，却因通用兼容而最终胜出。

**标签**: `#MCP`, `#AI agents`, `#developer tools`, `#LLM integration`, `#protocols`

---

<a id="item-3"></a>
## [DeepSeek 开源完整华为昇腾基础软件栈](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 8.0/10

2026 年 9 月 30 日，DeepSeek 开源了一套面向华为昇腾平台的基础组件，包括 TileLang 高级语言编译工具链、计算库和分布式通信库。此次发布还包含 DeepGEMM Ascend、DeepEP Ascend、TileKernels、FlashMLA 和 DeepSelect，DeepSeek 称这些组件在多项测试中性能接近硬件上限，并与华为昇腾 950 的 128 卡超节点方案同步推进。 这是目前为国产加速器构建“去 CUDA 化”AI 软件栈最完整的尝试之一，让昇腾用户第一次获得此前只在英伟达 GPU 上成熟的算子级与通信级基础组件。这可能显著降低在昇腾上训练和推理大模型的成本与门槛，并在中国企业获取英伟达硬件受限的背景下，强化华为在 AI 基础设施市场的地位。 这些组件被明确定位为 DeepSeek 现有英伟达栈的对应版本，TileLang 作为统一的编译层；值得注意的是，DeepSeek 的 FlashMLA 测试脚本需要同时依赖 TileLang、Tile-Kernels 和 DeepGEMM，而 DeepGEMM 借鉴了英伟达 CUTLASS/CuTe 的设计理念，但刻意避免对其模板的深度依赖。性能“接近硬件上限”的说法目前由 DeepSeek 自述，尚无第三方复现，公告中也没有给出具体版本号、基准数据或代码仓库链接。

telegram · zaihuapd · 9月30日 03:09

**背景**: TileLang 是一种基于 tile（数据块）的领域特定语言与编译系统，tile 是贯穿整个内存层级——从全局内存、共享内存、寄存器到计算与累加器——的核心编程对象；它介于底层汇编与高层 DSL 之间，在保留硬件控制力的同时显著降低编程复杂度。FlashMLA（高效多头注意力算子）和 DeepEP（专家并行通信库）最初是 DeepSeek 在 2025 年 2 月“开源周”期间面向英伟达 GPU 发布的，此次发布等于把同一类基础设施移植到昇腾平台。华为昇腾 950 超节点在 2026 年世界人工智能大会上亮相，被华为描述为业界最大规模的超节点，代表其在基础模型时代提供大规模算力的布局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnblogs.com/mysterious-llama/articles/20229077">TileLang 学习笔记（二）：从一个 Kernel 看懂 TileLang ...</a></li>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head ...</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient ...</a></li>
<li><a href="https://m.21jingji.com/article/20260717/herald/5ad90b573648444c183fea4752a207e8.html">WAIC上的算力重器： 华 为 昇 腾 950 超 节 点 真机现身 - 21财经</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Huawei Ascend`, `#AI Infrastructure`, `#Open Source`, `#LLM Training`, `#Compiler`

---

<a id="item-4"></a>
## [Cloudflare 宣布进军公共证书颁发机构市场](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare 宣布正在申请加入 Chrome、Apple、Microsoft 和 Mozilla 的根证书计划，以成为一家公共证书颁发机构，并已与 GlobalSign 签署协议收购一个被广泛信任的根证书，目前尚未开始签发证书。该新 CA 将优先支持基于 ACME 的自动化签发与续期，并计划在 2027 年第一季度签发生产级默克尔树证书（MTC），以服务后量子互联网。 Cloudflare 成为公共 CA 将把这家互联网最大的基础设施提供商之一直接带入 WebPKI 信任生态，可能重塑数以百万计站点签发、信任和管理证书的方式。其以 ACME 为先的策略以及后量子 MTC 路线图，或将推动整个行业走向更自动化、更抗量子攻击的证书签发模式。 Cloudflare 并非从零开始：它选择从 GlobalSign 收购一个现有的受信任根证书，而不是自行从头建立信任，这可能缩短浏览器根证书计划的审核流程，但申请获批与正式签发仍有待确认。MTC 计划的目标是在 2027 年第一季度实现生产级签发，这一时间表也反映出后量子签名若直接用于 TLS 握手会带来多大的体积与性能开销。

telegram · zaihuapd · 9月30日 06:26

**背景**: 证书颁发机构（CA）负责签发数字证书，浏览器和操作系统借此验证网站身份；信任链源自自签名的根证书，它必须被 Chrome、Mozilla、Apple、Microsoft 等根证书计划收录，才能让该 CA 签发的证书被广泛信任。ACME 是最初为 Let's Encrypt 设计的协议，用于自动完成证书的签发、续期和吊销，从而免去证书生命周期管理中的手工操作。默克尔树证书（MTC）是一种新兴方案，用基于哈希的默克尔树取代体积庞大的后量子签名，目的是让证书和握手在后量子时代依然保持足够小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment">Automatic Certificate Management Environment - Wikipedia</a></li>
<li><a href="https://www.encryptionconsulting.com/merkle-tree-certificates/">Merkle Tree Certificates & Post - Quantum WebPKI</a></li>
<li><a href="https://www.thesslstore.com/blog/how-to-become-a-certificate-authority/">How to Become a Certificate Authority... - Hashed Out by The SSL Store</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#PKI`, `#TLS Certificates`, `#ACME`, `#Post-Quantum Cryptography`

---