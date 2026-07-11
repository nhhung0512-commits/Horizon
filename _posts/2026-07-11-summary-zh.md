---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> 从 26 条内容中筛选出 7 条重要资讯。

---

1. [vLLM v0.25.0 发布：MRv2 成为默认，PagedAttention 被移除](#item-1) ⭐️ 9.0/10
2. [人形机器人远程完成全球首例活猪胆囊切除手术](#item-2) ⭐️ 9.0/10
3. [VultronRetriever 模型在 MTEB 上夺得第一，兼顾边缘效率](#item-3) ⭐️ 8.0/10
4. [SK 海力士 CEO 预警 2027 年最严重内存短缺](#item-4) ⭐️ 8.0/10
5. [苹果起诉 OpenAI 系统性窃取商业机密](#item-5) ⭐️ 8.0/10
6. [U-Boot 引导程序漏洞可致操作系统启动前执行代码](#item-6) ⭐️ 8.0/10
7. [OpenAI 发布 GPT-5.6 系列，包含 Sol、Terra、Luna 三个级别](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0 发布：MRv2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 将 Model Runner V2 (MRv2) 设为所有稠密模型的默认执行路径，并移除了旧的 PagedAttention 实现。该版本还新增了 LLaVA-OneVision-2 和 GLM-5 等模型、一个 Stream Parsing Engine，并支持动态投机解码。 该版本标志着 vLLM 架构的重大转变，提升了性能和模块化，将使众多依赖 vLLM 进行 LLM 推理的开发者和组织受益。移除 PagedAttention 以及 MRv2 的成熟预示着更简洁、更快速的代码库。 Model Runner V2 现在处理所有稠密模型，且 Transformers 建模后端的速度已与原生 vLLM 持平。新功能包括支持异构词表的通用投机解码，以及带有 HTTPS/mTLS 支持的 Rust 前端。

github · khluu · 7月11日 20:06

**背景**: PagedAttention 是 vLLM 自诞生以来使用的内存高效注意力算法，而 Model Runner V2 是重新设计的执行核心，它通过使用 GPU 原生 Triton 内核将 CPU 调度与 GPU 执行分离。v0.25.0 版本完全过渡到 MRv2，移除了旧的 PagedAttention 后端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>

</ul>
</details>

**标签**: `#vllm`, `#LLM inference`, `#release`, `#performance`, `#open source`

---

<a id="item-2"></a>
## [人形机器人远程完成全球首例活猪胆囊切除手术](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

外科医生远程操控宇树 G1 人形机器人，成功对活猪完成了两例微创胆囊切除手术，这是全球首次，结果发表在《自然》期刊。 这一里程碑展示了低成本通用人形机器人在手术中的潜力，可能大幅降低费用，并将手术可及性扩展到偏远地区、战场甚至太空。 宇树 G1 配灵巧手后约需 6.7 万美元，远低于达芬奇等专用手术机器人（50 万至数百万美元）。但系统需要多次校准，且存在延迟问题，导致手术速度较慢。

telegram · zaihuapd · 7月11日 02:29

**背景**: 人形机器人模仿人类形态和运动，可适应多种任务。远程手术允许医生远距离操控机器人，但传统手术机器人昂贵且专用。本研究测试了低成本通用人形机器人能否完成精细手术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10796-x">In vivo feasibility study of humanoid robots in surgery | Nature</a></li>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G 1 _ Humanoid Robot ... | Unitree Robotics</a></li>

</ul>
</details>

**标签**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI in healthcare`

---

<a id="item-3"></a>
## [VultronRetriever 模型在 MTEB 上夺得第一，兼顾边缘效率](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

VultronRetriever 系列检索模型已在 HuggingFace 上发布，并在 MTEB 排行榜的每个模型类别中均排名第一，其中 8B Prime 模型成为全球第一。 这些模型相比之前的领先者，索引存储最多减少 16 倍，吞吐量提高 12 倍，从而能够在 iPhone 等边缘设备上完全离线实现最先进的检索，这可能让高精度文档检索在移动和低资源环境中普及。 最小的模型 Flash (0.8B) 性能优于五倍于其大小的模型，离线时每分钟可索引多达 60 张图像。所有模型均在 0% 跨数据集重复和 0% 评估污染的数据集上训练，且在私有 MTEB 评估中未出现过拟合。

reddit · r/MachineLearning · /u/madkimchi · 7月11日 15:22

**背景**: MTEB（大规模文本嵌入基准）是一个标准的公开排行榜，用于评估嵌入模型在检索、分类、聚类、重排序等任务上的表现。VultronRetriever 模型基于 Hydra 架构，该架构在单个视觉语言模型中统一了后期交互检索和自回归生成，从而能够在边缘设备上高效离线运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.vultr.com/vultronretriever">VultronRetriever : Open Visual Document Retrieval Models Built for...</a></li>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>

</ul>
</details>

**标签**: `#retrieval`, `#embedding`, `#transformers`, `#huggingface`, `#MTEB`

---

<a id="item-4"></a>
## [SK 海力士 CEO 预警 2027 年最严重内存短缺](https://www.reuters.com/world/asia-pacific/sk-hynix-ceo-sees-worst-ever-memory-supply-shortage-2027-says-demand-outstrip-2026-07-10/) ⭐️ 8.0/10

SK 海力士 CEO 郭鲁正警告称，全球内存行业将在 2027 年遭遇史上最严重的供应短缺，需求将在 2030 年后仍超过供应能力。 这一预测预示着内存供应将长期紧张，可能导致 DRAM 和 NAND 闪存价格上涨，影响消费电子、数据中心和 AI 基础设施。 该警告是在 SK 海力士在纳斯达克上市首日发布的，当日股价收涨 13.3%至 168.85 美元；该公司 2025 年营业利润达到创纪录的 47 万亿韩元。

telegram · zaihuapd · 7月11日 00:45

**背景**: SK 海力士是全球领先的内存制造商，生产广泛用于计算机、智能手机和服务器的 DRAM 和 NAND 闪存。内存行业具有周期性，受 PC、移动设备以及最近的 AI 加速器需求驱动，会出现供过于求和短缺的交替。

**标签**: `#半导体`, `#内存`, `#供应链`, `#行业预测`

---

<a id="item-5"></a>
## [苹果起诉 OpenAI 系统性窃取商业机密](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 8.0/10

苹果于 2026 年 7 月 10 日在美国加州北区联邦法院起诉 OpenAI、两名前员工及 io Products，指控其系统性窃取与硬件设计、制造和供应链相关的商业机密。 这场诉讼直指人工智能与硬件的交叉领域，可能重塑科技行业的人才流动和知识产权保护格局。它凸显了苹果与 OpenAI 在消费级硬件领域扩张时不断升级的竞争。 苹果称前员工 Chang Liu 离职后仍访问内部网络并下载数十份硬件文件；OpenAI 硬件负责人 Tang Yew Tan 被指将供应商资料发送至个人邮箱，并要求求职者携带苹果零部件参加面试。

telegram · zaihuapd · 7月11日 03:14

**背景**: 商业机密是提供竞争优势的机密商业信息，如产品设计和制造工艺。苹果长期以来严格保护其硬件机密，而 OpenAI 作为以 AI 软件闻名的公司，目前正进军消费硬件领域，从而产生了摩擦。

**标签**: `#苹果`, `#OpenAI`, `#诉讼`, `#商业机密`, `#硬件`

---

<a id="item-6"></a>
## [U-Boot 引导程序漏洞可致操作系统启动前执行代码](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

U-Boot 的 FIT 镜像签名验证中发现了六个漏洞，其中两个可在操作系统启动前执行任意代码，影响自 2013.07 以来的 50 多个稳定版本。 这些漏洞使攻击者能够绕过安全启动并在固件级别执行恶意代码，可能永久危害设备。由于 U-Boot 广泛用于嵌入式系统、服务器和物联网设备，影响范围广泛，修复依赖于厂商的固件更新。 这些漏洞位于 FIT 镜像解析器中，影响已验证和未验证的启动模式。补丁已被 U-Boot 维护者接受，但部署需要硬件厂商集成；已停止支持的设备可能永远无法获得修复。

telegram · zaihuapd · 7月11日 08:32

**背景**: U-Boot 是一种广泛使用的嵌入式系统开源引导程序，负责初始化硬件并加载操作系统。FIT（扁平化镜像树）格式将启动镜像与哈希和签名打包，以确保完整性和真实性。基板管理控制器（BMC）支持远程固件更新，使得无需物理接触即可进行远程利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.u-boot.org/en/latest/usage/fit/index.html">Flat Image Tree (FIT) — Das U-Boot unknown version documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface">Intelligent Platform Management Interface - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#bootloader`, `#vulnerability`, `#firmware`, `#U-Boot`

---

<a id="item-7"></a>
## [OpenAI 发布 GPT-5.6 系列，包含 Sol、Terra、Luna 三个级别](https://t.me/zaihuapd/42497) ⭐️ 8.0/10

OpenAI 正式发布了 GPT-5.6 系列，推出了三个级别：Sol 负责最强性能，Terra 平衡性能与成本，Luna 面向高并发低成本场景。该系列在代码生成、推理、设计、科研和网络安全方面有显著提升，并新增了 max/ultra 推理、多智能体协作和程序化工具调用等能力。 此次发布代表了 AI 模型能力的重大进步，为开发者和企业提供了针对不同用例和预算优化的更灵活选择。多智能体协作和程序化工具调用的引入，有望显著降低构建 AI 驱动应用的复杂性和成本。 GPT-5.6 系列包含三个级别：Sol（旗舰高性能）、Terra（平衡型）和 Luna（面向高吞吐的成本效益型），且 GPT-5.6 将默认指向 Sol。新功能包括 max/ultra 推理努力级别、多智能体协作和程序化工具调用，该功能允许模型通过代码编排工具，而非逐个 API 往返调用。

telegram · zaihuapd · 7月11日 13:34

**背景**: GPT-5.6 是 OpenAI 继 GPT-4 和 GPT-4o 之后的最新大型语言模型系列。这种分级方法类似于其他 AI 实验室的策略，旨在满足从资源密集型任务到轻量级高并发应用的不同需求。多智能体协作允许多个专用 AI 代理协同处理复杂任务，而程序化工具调用则允许模型通过代码执行工具使用，从而提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling">Programmatic tool calling - Claude Platform Docs</a></li>
<li><a href="https://www.toolcolumn.com/learn/gpt-5-6-max-vs-ultra">GPT-5.6 Max vs Ultra: What Actually Changes? | ToolColumn</a></li>
<li><a href="https://www.ibm.com/think/topics/multi-agent-collaboration">What is Multi-Agent Collaboration? | IBM</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#language models`, `#performance`

---