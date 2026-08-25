---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 36 条内容中筛选出 9 条重要资讯。

---

1. [苹果发布 M6 与 M5 Ultra 芯片，AI 算力大幅跃升](#item-1) ⭐️ 9.0/10
2. [OpenAI 自研芯片 Jalapeño 宣称能效超越英伟达 Blackwell](#item-2) ⭐️ 9.0/10
3. [苹果推出搭载 M5 Max 和 M5 Ultra 的 Mac Studio，主打 AI 性能](#item-3) ⭐️ 8.0/10
4. [Nitter 项目收到停止函，全部实例关闭](#item-4) ⭐️ 8.0/10
5. [开放权重模型上的持续学习为主权 AI 铺路](#item-5) ⭐️ 8.0/10
6. [SpaceX 计划 2027 年将英伟达 Vera Rubin NVL72 送入太空](#item-6) ⭐️ 8.0/10
7. [英伟达首测 Vera Rubin NVL72：吞吐提升 30 倍、成本降低 35 倍](#item-7) ⭐️ 8.0/10
8. [英伟达 Jetson Orin Nano 2 发布：边缘 AI 推理性能翻倍、功耗降 40%](#item-8) ⭐️ 8.0/10
9. [Anthropic 第二季营收暴涨 14 倍，突破 115 亿美元](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [苹果发布 M6 与 M5 Ultra 芯片，AI 算力大幅跃升](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 9.0/10

苹果于 2026 年 8 月 25 日发布了 M6 与 M5 Ultra 芯片，其中 M6 首发于新款 Mac mini，M5 Ultra 则搭载于新款 Mac Studio。M6 是苹果首款 2 纳米芯片，配备 12 核 CPU、12 核 GPU、双 16 核神经网络引擎，统一内存带宽最高达 170GB/s。 此次发布标志着 Apple Silicon 在性能和 AI 算力上的重大飞跃，强化了苹果在端侧 AI 和高端工作站能力的布局。M6 面向主流设备、M5 Ultra 面向专业用户，使 Mac 产品线大幅扩展，可能重塑行业对价格与性能的预期。 M5 Ultra 采用 M 系列史上首次的四芯片架构，最高配备 36 核 CPU、80 核 GPU，支持最高 512GB 内存，统一内存带宽达 1.2TB/s，比 M3 Ultra 高 50%。M6 版 Mac mini 起售价 6999 元，M5 Pro 版起售价 12999 元；搭载 M5 Max 的 Mac Studio 起售价 19999 元。

hackernews · interpol_p · 8月25日 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49433292)

**背景**: Apple Silicon 是苹果基于 Arm 架构的芯片系列，自 2020 年起取代 Mac 中的 Intel 处理器。M6 是苹果首款采用 2 纳米制程的芯片，而 M5 Ultra 则通过四芯片堆叠设计来扩展性能与内存。这些芯片采用 CPU、GPU 和神经网络引擎共享的统一内存架构，对 AI 工作负载尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/">Apple</a></li>
<li><a href="https://en.m.wikipedia.org/wiki/Apple_Inc.">Apple Inc. - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者情绪复杂，既有人赞叹性能飞跃，并指出经通胀调整后的价格与早期 Mac 相当；也有人批评顶配机型价格惊人，有用户算出一台顶配 Mac Studio 售价达 24699 美元。还有人回忆 90 年代的竞争，认为性价比最高的仍是 450 美元的 M4 Mac mini。

**标签**: `#Apple Silicon`, `#M6`, `#M5 Ultra`, `#AI Compute`, `#Hardware`

---

<a id="item-2"></a>
## [OpenAI 自研芯片 Jalapeño 宣称能效超越英伟达 Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI 公布了其自研推理 ASIC（代号 Jalapeño）的首批测试结果，声称在每兆瓦吞吐量和延迟方面优于英伟达基于 Blackwell 的 GB300 芯片。据称该芯片由 OpenAI 与博通合作开发，计划于今年年底前在 OpenAI 自己的数据中心内部署。 如果得到证实，这将是对英伟达在 AI 加速器领域近乎垄断地位的重大挑战，表明针对特定工作负载定制的 ASIC 可以在成本和效率上胜过通用 GPU。这可能加速大型科技公司自研芯片的行业趋势，削弱英伟达的定价权，并重塑 AI 硬件供应链。 在 GPT-OSS 120B、DeepSeek R1 670B 和 Kimi K2.5 1T 等模型上，Jalapeño 据称每单位功耗产出高性能是对比系统的 1.5 至 1.9 倍，端到端延迟低 1.7 至 3.6 倍，高交互场景性能高 2.1 至 4.1 倍。该芯片额定功耗 700 瓦，持续功耗不高于 550 瓦；基准测试对比对象是英伟达 GB300，而非更新的 Vera Rubin，且该芯片不用于模型训练。

hackernews · Semianalysis · 8月25日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49434378)

**背景**: Jalapeño 是一种专用集成电路（ASIC），即为特定任务（此处是 AI 推理）设计的固定功能芯片，而不是像英伟达 Blackwell 系列那样的通用 GPU。英伟达的 Blackwell 架构（用于 GB200、GB300 等芯片）一直是 AI 训练和推理的主导平台，但针对特定模型工作负载优化的定制 ASIC 可以提供更低功耗和更好的成本效益。OpenAI 的举措延续了谷歌和亚马逊等大型 AI 公司的路径，这些公司也开发自研加速器以减少对英伟达的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/">The Engine Behind AI Factories | NVIDIA Blackwell Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Application-specific_integrated_circuit">Application-specific integrated circuit - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者整体对消息表示欢迎，有人认为硬件持续改进将不可避免导致 token 价格下跌。有评论者推测 OpenAI 和 Anthropic 最终可能将固定的大模型权重直接集成到芯片中，以获得巨大的速度和成本优势；还有评论者开玩笑说，这个万亿美元行业的分析竟由 SemiAnalysis 的前 Reddit 和 4chan 版主主导。也有人指出，人类语音的能效仍比该芯片高 22 倍，并认为 OpenAI 可能寻求 IPO 以筹集资金用于进一步建设硬件。

**标签**: `#OpenAI`, `#AI Hardware`, `#ASIC`, `#Nvidia`, `#Semiconductors`

---

<a id="item-3"></a>
## [苹果推出搭载 M5 Max 和 M5 Ultra 的 Mac Studio，主打 AI 性能](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) ⭐️ 8.0/10

苹果推出了搭载 M5 Max 和全新 M5 Ultra 芯片的新款 Mac Studio，重点强调本地 AI 性能和高内存带宽。此次发布将 Mac Studio 定位为苹果最强大的本地 AI 工作负载设备。 这一发布意义重大，表明苹果持续加码端侧 AI，为专业人士提供高内存带宽的机器，以便在本地运行大型语言模型。它可能会影响 AI 开发者在云端与本地推理之间的选择，并强化苹果在 AI/ML 工作负载上的生态。 M5 Max 支持最高 128GB 统一内存和 614GB/s 内存带宽，而高端 M5 Ultra 配置据报道可提供 256GB 或更多内存以及最高 1.2TB/s 内部内存带宽。新款 Mac Studio 还首发采用 PCIe Gen 6 存储，存储性能最高提升至上一代的两倍。

hackernews · interpol_p · 8月25日 13:03 · [社区讨论](https://news.ycombinator.com/item?id=49433316)

**背景**: Mac Studio 是苹果面向视频剪辑师、3D 艺术家和研究人员等专业人士的高性能台式机。M5 系列于 2025 年底推出，将 CPU、GPU、NPU 和统一内存集成在一个芯片中，其中 M5 Ultra 是最高端版本。统一内存允许 CPU 和 GPU 共享同一内存池，这对运行需要快速数据访问的大型 AI 模型尤其有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://www.notebookcheck.net/Apple-M5-Max-Processor-Benchmarks-and-Specs.1244918.0.html">Apple M5 Max Processor - Benchmarks and Specs - Notebookcheck Tech</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常热烈，用户围绕定价和大型 AI 的实用性展开辩论。有人指出价格高昂（例如 256GB 内存需 1 万美元），并质疑其对于超过 1 万亿参数模型的未来兼容性；也有人欢迎苹果对本地 AI 的重视及其在个人电脑中首次采用 PCIe Gen 6 存储。

**标签**: `#Apple`, `#Mac Studio`, `#M5`, `#hardware`, `#AI`

---

<a id="item-4"></a>
## [Nitter 项目收到停止函，全部实例关闭](https://github.com/zedeus/nitter/issues/1442) ⭐️ 8.0/10

Nitter 项目在 GitHub issue #1442 中宣布已收到停止函（cease and desist）。在维护者寻求法律建议期间，所有公共 Nitter 实例预计将在可预见的未来保持下线。 这标志着开源工具在提供保护隐私的 Twitter/X 访问方面面临的法律压力显著升级。它可能吓阻类似项目，减少用户的隐私选项，并影响那些依靠 Nitter 在没有追踪或账户的情况下浏览 X 的用户。 Nitter 是一个免费开源替代前端，仅支持浏览；用户无法登录或与帖子互动。维护者除了停止函之外没有提供更多细节，所有实例目前在可预见的未来都已关闭。

hackernews · Banditoz · 8月25日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=49437283)

**背景**: Nitter 是一个免费开源的 Twitter/X 替代前端，专注于隐私和性能，让用户无需广告、追踪或账户即可查看个人资料、推文、回复和媒体。它通常通过公共实例访问，而这些实例长期面临速率限制和反机器人措施的困扰。来自 X 的法律行动为该项目能否持续发展增添了新的、可能是决定性的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter</a></li>
<li><a href="https://nitter.tiekoetter.com/about">nitter .tiekoetter.com</a></li>

</ul>
</details>

**社区讨论**: 评论者对 X 的限制表示不满，指出用户现在需要账户才能“潜水”，而且无法轻松配置非算法信息流。有人称赞对社区友好的平台，以 Hacker News 的 dang 为例，他支持非官方克隆项目而非发出法律威胁。总体情绪是对 Nitter 表示同情，并批评 X 日益加强的平台控制。

**标签**: `#nitter`, `#privacy`, `#open-source`, `#legal`, `#twitter`

---

<a id="item-5"></a>
## [开放权重模型上的持续学习为主权 AI 铺路](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 8.0/10

一份新技术报告和开放权重模型 Thomson 提出，通过对开放权重模型进行持续学习，可以缩小与前沿模型性能的差距。该团队在安全、法律、税务、多语言和智能体任务等领域展示了具有竞争力的结果，且所需算力和人力预算远低于通常预期。 这一成果意义重大，因为它挑战了只有少数资金雄厚的实验室才能构建前沿模型的假设。它为政府、中型企业和公共机构提供了一条具体的短期路径，使其能够实现 SovereignAI，即独立拥有模型、工具基础设施、价值观和数据隐私。 Thomson 是一个通用型前沿模型，训练重点放在高风险专业工作上。报告称其评估呈现独特的“π型”模式：在包括未针对性优化的领域在内广泛能力均有提升，同时通过最少数量的高影响力参数干预，几乎消除了灾难性遗忘。

reddit · r/MachineLearning · /u/Forsaken_Scientist · 8月25日 10:30

**背景**: 持续学习（continual learning）又称终身学习，是一种让模型按顺序学习新任务或新数据、同时保留已有知识的训练方式。开放权重模型公开了训练好的参数，任何人都可以下载、运行、研究并修改它们。SovereignAI 指一个组织独立构建、部署和治理 AI 使用的能力，这一目标经常被讨论，但很少给出具体可行的指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open - Weight Model ? - Stanford HAI</a></li>
<li><a href="https://www.linkedin.com/pulse/continual-learning-llms-why-ai-models-need-sleep-nagesh-nama-nbtee">Continual Learning in LLMs: Why AI Models Need Sleep</a></li>

</ul>
</details>

**标签**: `#continual learning`, `#open-weight models`, `#sovereign AI`, `#frontier models`, `#AI policy`

---

<a id="item-6"></a>
## [SpaceX 计划 2027 年将英伟达 Vera Rubin NVL72 送入太空](https://www.theregister.com/off-prem/2026/08/25/spacex-claims-it-will-put-a-vera-rubin-nvl72-rack-scale-system-into-orbit-next-year/5292067) ⭐️ 8.0/10

SpaceX 宣布计划于 2027 年将英伟达 Vera Rubin NVL72 机架级 AI 系统送入轨道，以验证太空数据中心相关技术。这一宣布标志着在太空运行先进 AI 硬件迈出了具体一步。 此事意义重大，因为它可能开创轨道 AI 数据中心的发展，为国防、通信和地球观测等领域提供低延迟的太空计算能力。同时，它也拓展了高性能 AI 基础设施的部署边界。 NVL72 系统由 72 颗 Rubin GPU 与 36 颗 Vera CPU 组成，功耗超过 100 千瓦，通常需要复杂的液冷和供电系统。SpaceX 尚未公布具体发射时间、轨道高度以及系统在太空中的供电与散热方案。

telegram · zaihuapd · 8月25日 08:03

**背景**: Vera Rubin NVL72 是英伟达的下一代机架级 AI 超算平台，基于第三代 MGX NVL72 机架设计，与 Blackwell 相比，能以四分之一数量的 GPU 完成 AI 训练，并将每百万 token 的推理成本降低至十分之一。太空数据中心是一种提出中的概念，旨在利用天基太阳能和边缘计算将 AI 数据中心部署在轨道上，从而绕开地面网络的延迟，其历史渊源可追溯至“Brilliant Pebbles”等军事架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL72</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Nvidia`, `#AI computing`, `#Space data center`

---

<a id="item-7"></a>
## [英伟达首测 Vera Rubin NVL72：吞吐提升 30 倍、成本降低 35 倍](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 8.0/10

英伟达首次公布了新一代机柜级系统 Vera Rubin NVL72 的片上实测数据：在 DeepSeek-V4-Pro 的智能体编码任务中，每兆瓦吞吐量较 GB300 最高提升 30 倍，每百万 Token 成本最高下降 35 倍。同时宣布推理加速芯片 Groq 3 LPX 进入量产，并推出面向智能体工作负载的 Vera CPU。 这一进展意义重大，因为推理性能和成本是大规模部署大语言模型的关键瓶颈，NVL72 表明机柜级协同设计能带来数量级上的提升。这巩固了英伟达在 AI 数据中心市场的地位，也标志着行业正转向 Groq LPX 这类专用推理架构和智能体工作负载。 Vera Rubin NVL72 在一个机柜内整合了 72 颗 Rubin GPU 和 36 颗 Vera CPU，并采用 NVLink-Fusion 和 Spectrum-X 以太网互连。Groq 3 LPX 在运行 Gemma 4 31B 时可达每秒 3400 个输出 Token，单个机柜级部署最多支持 256 个 LP30 加速器。

telegram · zaihuapd · 8月25日 14:48

**背景**: 英伟达的 GB200 和最新 Vera Rubin NVL72 等机柜级系统，将 GPU、CPU 和高带宽网络整合为一台超级计算机，用于生成式 AI 和智能体 AI 工作负载。智能体编码（agentic coding）指的是 AI 智能体自主规划并执行多步骤软件开发任务，这类任务计算密集且对延迟敏感。此次基准测试使用 DeepSeek-V4-Pro 大语言模型运行编码智能体任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference">Vera Rubin NVL72 vs GB200 NVL72? Inference TCO & Architecture Analysis</a></li>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/">NVIDIA Advances Vera Rubin Inference With New LPX ... | NVIDIA Blog</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Vera Rubin`, `#AI hardware`, `#DeepSeek`, `#inference`

---

<a id="item-8"></a>
## [英伟达 Jetson Orin Nano 2 发布：边缘 AI 推理性能翻倍、功耗降 40%](https://www.therobotreport.com/jetson-orin-nano-2-doubles-inference-performance-robotics-edge-says-nvidia/) ⭐️ 8.0/10

英伟达于 2025 年 8 月 25 日发布了入门级边缘 AI 模块 Jetson Orin Nano 2。它提供 78 TOPS 算力和 8 GB 内存，推理性能较上一代 Orin Nano Super 翻倍，并在同等性能下功耗降低 40%。 此次发布显著增强了英伟达的边缘 AI 和机器人生态系统，使 Cosmos、Qwen 3 等大模型能够在设备端实时推理。英伟达称其机器人技术栈拥有超过 300 万开发者，该模块有望推动边缘 AI 在无人机、机器人和嵌入式设备中的低成本、低功耗部署。 该模块与开发套件计划于 2027 年上半年上市。英伟达表示，Wing、Matic 等公司正在评估或采用该产品；该模块专为在边缘侧实时运行 Cosmos 世界基础模型和 Qwen 3 等大语言模型而设计。

telegram · zaihuapd · 8月25日 16:54

**背景**: TOPS（每秒万亿次操作）是衡量 AI 加速器峰值推理性能的关键指标，由每时钟周期操作数、时钟频率和处理单元数量计算得出。英伟达 Jetson 系列定位于边缘计算和机器人领域，本地化推理可降低延迟并提升隐私性。Cosmos 是英伟达面向物理 AI 的生成式世界基础模型平台，而 Qwen 3 是阿里巴巴推出的大语言模型系列，包含稠密和混合专家（MoE）多种架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lenovo.com/us/en/glossary/tops-in-computing/">What is TOPS in computing and How it Affects AI Performance | Lenovo US</a></li>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Edge Computing`, `#AI Hardware`, `#Robotics`, `#Jetson`

---

<a id="item-9"></a>
## [Anthropic 第二季营收暴涨 14 倍，突破 115 亿美元](https://t.me/zaihuapd/43403) ⭐️ 8.0/10

据彭博社援引文件称，Anthropic 第二季初步营收超过 115 亿美元，同比增长逾 14 倍。当季调整后营业利润也转正。 这一里程碑凸显了 Anthropic 在竞争激烈的 AI 市场中的快速商业增长，并可能增强投资者信心。今年秋季可能的 IPO 将是 AI 行业的一大事件，为公开市场投资者提供难得的持有领先 AI 实验室的机会。 这些数字为初步数据，仍可能调整。据文件显示，营收高于去年同期的 7.87 亿美元，也高于 2026 年第一季的 47.3 亿美元。

telegram · zaihuapd · 8月25日 17:32

**背景**: Anthropic 是一家由前 OpenAI 研究人员创立的 AI 安全与研究公司，以其 Claude 系列大语言模型闻名。该公司与 OpenAI、Google 和 Meta 在生成式 AI 市场竞争，企业级 AI 服务的需求推动了营收快速增长。成功的 IPO 将为 Anthropic 提供新资金，用于模型开发和拓展商业业务。

**标签**: `#Anthropic`, `#AI Business`, `#Revenue`, `#IPO`

---