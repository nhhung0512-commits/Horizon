---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
---

> 从 36 条内容中筛选出 15 条重要资讯。

---

1. [GitHub 推出堆叠式拉取请求](#item-1) ⭐️ 9.0/10
2. [欧足联及其 55 个成员协会抵制 FIFA 赛事](#item-2) ⭐️ 9.0/10
3. [Kimi K3：新型注意力机制、负载均衡与强化学习基础设施](#item-3) ⭐️ 9.0/10
4. [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动](#item-4) ⭐️ 9.0/10
5. [Anthropic AI 发现 NIST 候选算法 HAWK 严重弱点](#item-5) ⭐️ 9.0/10
6. [DeepMind 解散诺贝尔奖团队 AlphaFold，核心成员跳槽 Anthropic](#item-6) ⭐️ 9.0/10
7. [警惕廉价电视流媒体棒中的恶意软件](#item-7) ⭐️ 8.0/10
8. [Gemini Robotics 2 为机器人带来全身智能控制](#item-8) ⭐️ 8.0/10
9. [OpenAI 将 GPT-5.6 Luna 成本降低 80%](#item-9) ⭐️ 8.0/10
10. [AI 时代重构的经济效益分析](#item-10) ⭐️ 8.0/10
11. [GCC 对 AI 贡献采取人工监督政策](#item-11) ⭐️ 8.0/10
12. [教授因审稿流程失去潜在博士生](#item-12) ⭐️ 8.0/10
13. [MLVC：迈向实际部署的多平台学习型视频编解码器](#item-13) ⭐️ 8.0/10
14. [英国 CMA 提议允许应用开发者引导用户使用替代支付](#item-14) ⭐️ 8.0/10
15. [欧盟启动 AI 超级工厂招标，拟撬动 300 亿欧元](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GitHub 推出堆叠式拉取请求](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) ⭐️ 9.0/10

GitHub 已公开预览堆叠式拉取请求，开发者可以创建和管理一组相互依赖的变更堆栈，并独立进行审查和合并。这是 GitHub 多年来最大的变化之一，涉及从 Actions 到 Web UI 的几乎所有服务。 堆叠式 PR 支持更高效的工作流，将复杂功能拆分为可审查的小块，可能提升代码审查质量和开发者生产力。这一工作流在全球最大的代码托管平台上可用，可能影响数百万开发者的软件开发方式。 该功能处于公开预览阶段，可能存在一些问题，例如在某些情况下合并整个堆栈会失败，并且使用 squash 合并时若需审查则需重新批准。GitHub 提供了 CLI 工具和文档帮助开发者上手。

hackernews · tomzorz · 7月30日 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49112232)

**背景**: 堆叠式拉取请求（也称堆叠差异）是一种工作流，将一系列相互依赖的小变更堆叠在一起，每个变更作为单独的拉取请求。这与传统上为整个功能创建一个大型 PR 的方式形成对比，后者难以审查。该工作流在某些开源社区中很流行，并得到 Graphite 等第三方工具的支持，但这是 GitHub 首次原生实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.git-tower.com/blog/stacked-prs">Understanding the Stacked Pull Requests Workflow | Tower Blog</a></li>
<li><a href="https://www.graphite.com/guides/stacked-diffs">Stacked diffs</a></li>
<li><a href="https://www.michaelagreiler.com/stacked-pull-requests/">Stacked pull requests : make code reviews... - Dr. Michaela Greiler</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，许多开发者对这一期待已久的功能感到兴奋。但也存在对稳定性和可用性的担忧，例如合并整个堆栈时出现问题以及需要重新批准。一些评论者还质疑其相对于良好结构的基于提交的审查的优势，尤其是在 AI 生成代码的背景下。

**标签**: `#GitHub`, `#pull requests`, `#software engineering`, `#developer workflow`

---

<a id="item-2"></a>
## [欧足联及其 55 个成员协会抵制 FIFA 赛事](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/) ⭐️ 9.0/10

欧足联及其 55 个成员协会宣布将不参加国际足联（FIFA）的赛事，理由是腐败和治理问题。 这一抵制可能重塑国际足球治理，因为欧足联代表着最强大的足球地区。它标志着可能与 FIFA 分裂，威胁全球足球的统一。 该声明来自欧足联及其全部 55 个成员协会，表明一致支持。未具体说明受影响的 FIFA 赛事，但可能包括未来的世界杯。

hackernews · dickfickling · 7月30日 18:40 · [社区讨论](https://news.ycombinator.com/item?id=49113929)

**背景**: FIFA 是全球足球管理机构，而欧足联负责欧洲足球。频繁的腐败丑闻困扰着 FIFA，招致成员协会的批评。这次抵制的规模前所未有。

**社区讨论**: 评论普遍支持欧足联的立场，用户称 FIFA 腐败，并建议欧足联举办自己的世界杯。一些评论认为此举早已应该发生，并将其比作体育界的宗教分裂。

**标签**: `#football`, `#FIFA`, `#UEFA`, `#sports governance`, `#boycott`

---

<a id="item-3"></a>
## [Kimi K3：新型注意力机制、负载均衡与强化学习基础设施](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 9.0/10

Moonshot AI 发布了 Kimi K3 的技术报告和开源代码，这是一个 2.8 万亿参数的混合专家模型，引入了 Kimi Delta Attention、Quantile Balancing 和 AgentENV 强化学习运行时。 Kimi K3 作为开放权重模型达到了前沿性能，在 Artificial Analysis 上排名第四（共 580 个模型），仅次于 Claude Opus 5、Fable 5 和 GPT-5.6 Sol，表明开放权重模型可与专有系统竞争。 Kimi Delta Attention 在 93 层中的 69 层用每个头的 128x128 矩阵替换了 KV 缓存，将 100 万 token 上下文的记忆体从 104.6 GiB 降至 27.2 GiB。Quantile Balancing 通过路由器分数边缘直接计算偏置，实现每层 896 个专家的均匀负载，且无需超参数。

reddit · r/MachineLearning · /u/noninertialframe96 · 7月30日 16:37

**背景**: 传统 Transformer 注意力机制具有与序列长度 T 相关的二次复杂度 O(T²)，导致长上下文成本高昂。混合专家模型面临负载均衡问题，即某些专家被过度使用。智能体强化学习需要隔离的沙箱来训练智能体与环境交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/kimi-delta-attention">Kimi Delta Attention : Delta ‐Rule Linear Mechanism</a></li>
<li><a href="https://openathena.ai/blog/quantile-balancing/">Mixture of Experts Quantile Balancing: Validated at 32B-A5B (1e22 FLOPs) Scale | Open Athena</a></li>
<li><a href="https://www.marktechpost.com/2026/07/27/kimi-ai-and-kvcache-ai-open-sources-agentenv/">Kimi AI and kvcache-ai Open Sources ' AgentENV ... - MarkTechPost</a></li>

</ul>
</details>

**标签**: `#Kimi K3`, `#attention`, `#mixture of experts`, `#open-weight models`, `#RL training infrastructure`

---

<a id="item-4"></a>
## [俄罗斯指控 Telegram 创始人杜罗夫协助恐怖活动](https://t.me/zaihuapd/42859) ⭐️ 9.0/10

7 月 29 日，俄罗斯联邦安全局（FSB）宣布，已依据《俄罗斯联邦刑法典》第 205.1 条第 1.1 款（协助恐怖活动）对 Telegram 创始人帕维尔·杜罗夫提起刑事指控，并将其列入国际通缉名单。 这一针对知名科技创始人的前所未有的法律行动，可能为平台责任和端到端加密树立危险先例，威胁全球数亿 Telegram 用户的隐私和安全。 FSB 指控 Telegram 管理层拒绝删除被乌克兰情报机构及恐怖、极端主义组织用于策划和协调破坏活动、恐怖袭击、大规模杀戮及网络诈骗的频道、群组和机器人，造成包括妇女儿童在内的多人伤亡和数十亿卢布损失。

telegram · zaihuapd · 7月30日 03:45

**背景**: Telegram 是由帕维尔·杜罗夫创立的加密通讯应用，他于 2014 年因拒绝服从政府封锁反对派团体的要求而离开俄罗斯。《俄罗斯联邦刑法典》第 205.1 条将协助恐怖活动（包括资助或组织）定为刑事犯罪，该指控面临严重刑罚，包括可能的监禁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unodc.org/cld/en/legislation/rus/the_criminal_code_of_the_russian_federation_russianenglish/chapter_24/article_205.1_-_205.3/article_205.1_-_205.3.html">Article 205.1 - 205.3</a></li>
<li><a href="https://www.rightsinrussia.org/law-of-the-week-37/">Law of the Week: Article 205.5 of the Russian Criminal Code (Organisation of and participation in the activities of a terrorist organisation) - Rights in Russia</a></li>

</ul>
</details>

**标签**: `#Pavel Durov`, `#Telegram`, `#FSB`, `#terrorism charges`, `#international wanted list`

---

<a id="item-5"></a>
## [Anthropic AI 发现 NIST 候选算法 HAWK 严重弱点](https://startupfortune.com/claude-mythos-broke-hawk-and-the-nist-post-quantum-timeline-may-not-survive-it/) ⭐️ 9.0/10

Anthropic 的 Claude Mythos Preview AI 在 60 小时内发现了 NIST 后量子算法 HAWK 的严重弱点，将其有效密钥强度从 2^64 降至 2^38，而人类密码分析师两年来一直未发现此漏洞。 这一里程碑表明 AI 可以大幅加速密码分析，直接影响到后量子密码标准化时间表，迫使社区重新考虑算法评估流程。 该攻击花费约 10 万美元 API 费用，且不运行在多项式时间内，意味着更大的密钥仍然安全；NIST 尚未公开撤回 HAWK。

telegram · zaihuapd · 7月30日 05:47

**背景**: 后量子密码学旨在开发能抵抗未来量子计算机的算法。NIST 自 2016 年起举办公开竞赛挑选标准，HAWK 是第三轮候选算法。美国行政令要求联邦机构在 2030-2031 年前迁移至抗量子密码体系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/">Mythos attack on 3rd-round PQC algorithm candidate... - Ars Technica</a></li>
<li><a href="https://www.techzine.eu/news/applications/143290/mythos-knocks-hawk-out-of-the-race-for-a-post-quantum-standard/">Mythos knocks HAWK out of the race for a post - quantum standard</a></li>
<li><a href="https://korben.info/en/claude-breaks-post-quantum-algorithm-60-hours.html">Claude breaks a post - quantum algorithm in 60 hours - Korben</a></li>

</ul>
</details>

**标签**: `#AI`, `#cryptanalysis`, `#post-quantum cryptography`, `#NIST`, `#Anthropic`

---

<a id="item-6"></a>
## [DeepMind 解散诺贝尔奖团队 AlphaFold，核心成员跳槽 Anthropic](https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33?syn-25a6b1a6=1) ⭐️ 9.0/10

谷歌 DeepMind 解散了其荣获诺贝尔奖的 AlphaFold 团队，将许多研究人员调往其他项目，同时三名核心成员已离职加入竞争对手 Anthropic。 这一战略重心从蛋白质折叠研究转向生成式 AI 等领域，可能重塑 AI 研究的竞争格局，并可能减缓计算生物学领域的进展。 近四分之一的 AlphaFold 原始论文作者已离开 DeepMind，包括 John Jumper、Jonas Adler 和 Alexander Pritzel 等核心研究人员，他们加入了 Anthropic。其余团队成员转至 Gemini、酶设计、核聚变或 Isomorphic Labs 等项目。

telegram · zaihuapd · 7月30日 07:45

**背景**: AlphaFold 是 DeepMind 开发的蛋白质结构预测 AI 系统，以其高准确度获得 2024 年诺贝尔化学奖。DeepMind 是 Alphabet 旗下的 AI 研究实验室，而 Isomorphic Labs 是其专注于 AI 驱动药物发现的衍生公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold - Wikipedia</a></li>
<li><a href="https://deepmind.google/science/alphafold/">AlphaFold — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>

</ul>
</details>

**标签**: `#AlphaFold`, `#DeepMind`, `#Anthropic`, `#AI research`, `#protein folding`

---

<a id="item-7"></a>
## [警惕廉价电视流媒体棒中的恶意软件](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/) ⭐️ 8.0/10

Krebs on Security 的一篇文章揭露，廉价电视流媒体棒（如 H96 型号）出厂即感染恶意软件，可被用于住宅代理和广告欺诈，将设备变成点击广告的僵尸网络。 数百万用户可能不知不觉从主流电商平台购买到被入侵的设备，危及家庭网络安全，并助长消耗广告预算的广告欺诈行为。 据 Bitsight 报告，恶意软件使用 Blockly 模块控制设备执行浏览网页和点击广告等任务，并利用视觉和推理系统模拟人类行为。

hackernews · speckx · 7月30日 17:04 · [社区讨论](https://news.ycombinator.com/item?id=49112744)

**背景**: 电视流媒体棒是插入电视 HDMI 端口播放内容的廉价设备。廉价‘无名’品牌常运行修改版 Android 系统，且无安全更新，极易被植入恶意软件。攻击者可利用这些设备模拟网络流量进行广告欺诈，从而牟利。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/">Read This Before You Buy That TV Streaming Stick – Krebs on Security</a></li>
<li><a href="https://www.malwarebytes.com/blog/news/2025/11/illegal-streaming-is-costing-people-real-money-research-finds">The hidden costs of illegal streaming and modded Amazon Fire TV Sticks | Malwarebytes</a></li>

</ul>
</details>

**社区讨论**: 评论者对亚马逊等电商平台销售这些有害产品却不承担责任表示不满。有用户分享个人遭遇广告泛滥的设备，也有人建议将 IoT 设备隔离到独立的 VLAN 中以保护网络安全。

**标签**: `#security`, `#streaming`, `#privacy`, `#malware`, `#IoT`

---

<a id="item-8"></a>
## [Gemini Robotics 2 为机器人带来全身智能控制](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

谷歌 DeepMind 于 2026 年 7 月 30 日发布了 Gemini Robotics 2，这是一个视觉-语言-动作模型，能够实现对完整人形机器人从脚趾到指尖的全身智能控制。 这一突破提升了机器人的适应性和灵巧性，使其能够实现流畅运动、精细操作以及多机器人协作，可能对制造业、医疗保健和家庭辅助等领域产生深远影响。 Gemini Robotics 2 是一个视觉-语言-动作模型（VLA），用于控制 Apptronik Apollo 2 人形机器人，同时还包括一个独立的模型 Gemini Robotics ER 2，用于具身推理和复杂多步规划。

hackernews · ai2027 · 7月30日 15:15 · [社区讨论](https://news.ycombinator.com/item?id=49111237)

**背景**: 传统机器人 AI 通常依赖特定任务的编程，缺乏处理非结构化环境的灵活性。视觉-语言-动作模型（VLA）如 Gemini Robotics 2 将视觉感知、语言理解和运动控制整合到单一系统中，使机器人能够理解并执行现实世界中的自然语言指令。全身智能意味着机器人能够动态协调全身（而不仅仅是手臂或腿部）来执行任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body... — Google DeepMind</a></li>
<li><a href="https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-2-bringing-whole-body-intelligence-and-multi-robot-teams-to-physical-ai">Google DeepMind Unveils Gemini Robotics 2, Bringing Whole - Body ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一位 DeepMind 研究员称赞了该实验室工作范围的广度，而其他人则指出机器人动作缓慢，并强调人形机器人中执行器的局限性仍然存在。一些评论者乐观地认为其进展可能像大语言模型一样迅速，而另一些则对硬件限制持怀疑态度。

**标签**: `#robotics`, `#AI`, `#DeepMind`, `#Gemini`, `#machine learning`

---

<a id="item-9"></a>
## [OpenAI 将 GPT-5.6 Luna 成本降低 80%](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) ⭐️ 8.0/10

OpenAI 宣布推出 GPT-5.6 Luna，这是比以往版本便宜 80% 且更快的成本高效模型，今日起可用。 这一显著降价标志着 AI 模型经济性的转折点，使得以以往成本的一小部分进行大规模推理成为可能，并刺激 AI 提供商进一步降价竞争。 定价为每百万输入 tokens 0.10 美元、每百万输出 tokens 0.60 美元，上下文窗口为 1,050,000 tokens，最大输出 128,000 tokens；OpenAI 还推出了 GPT-5.6 系列中的高端模型 Sol 和 Terra。

hackernews · tedsanders · 7月30日 17:15 · [社区讨论](https://news.ycombinator.com/item?id=49112867)

**背景**: 推理成本——生成模型输出的计算费用——一直是 AI 广泛采用的主要障碍。最近的优化已迅速降低成本，GPT-3.5 级别推理成本从 2022 年底到 2024 年底下降了超过 280 倍。OpenAI 的最新举措延续了这一趋势，使前沿 AI 更加可及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.6-luna">GPT-5.6 Luna Model | OpenAI API</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-luna">GPT-5.6 Luna - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 评论者对 80% 的降价表示兴奋，有人将其比作从拨号到宽带的过渡，并指出可以运行 5 倍更多的并行智能体。其他人则讨论成本降低是否真的能节省数十亿美元，并强调了在选择模型时区分琐碎与非琐碎任务的挑战。

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI pricing`, `#language models`, `#inference cost`

---

<a id="item-10"></a>
## [AI 时代重构的经济效益分析](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html) ⭐️ 8.0/10

Martin Fowler 分析了在生成式 AI 背景下重构的经济效益，主张人类开发者的最佳实践同样适用于 AI 助手。 该分析提供了具体、接地气且定量的视角，探讨 AI 工具如何影响软件工程经济学，反驳了模糊的 AI 评论。 该文章将重构与减少 token 消耗及提升 AI 模型的推理能力联系起来，认为更干净的代码能激发更智能的 AI 行为。

hackernews · javaeeeee · 7月30日 15:10 · [社区讨论](https://news.ycombinator.com/item?id=49111176)

**背景**: 重构是指在不改变外部行为的前提下重组现有代码的过程，旨在提高可读性、可维护性并降低复杂性。在 AI 背景下，重构可以优化大型语言模型的上下文窗口，从而提升性能并降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/top-content/technology/software-engineering-principles/when-software-refactoring-is-not-worthwhile/">When Software Refactoring Is Not Worthwhile</a></li>
<li><a href="https://wasrek.medium.com/bad-smell-and-refactoring-software-engineering-5bb07809b86d">Bad Smell and Refactoring | Software Engineering | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，人类程序员的最佳实践正在为 AI 重新发现，赞赏文章的接地气方法，但质疑 AI 是否能真正理解项目的全局。有人指出重构的好处不仅限于 token 成本，还能增强模型推理。

**标签**: `#refactoring`, `#generative AI`, `#software engineering`, `#best practices`, `#economics`

---

<a id="item-11"></a>
## [GCC 对 AI 贡献采取人工监督政策](https://lwn.net/Articles/1086041/) ⭐️ 8.0/10

GCC 指导委员会宣布了一项新政策，要求对所有 AI 生成的贡献进行人工监督，确保代码合并前有人类承担责任。 这项政策为应对 AI 生成代码的开源项目树立了先例，强调人类责任并解决对低质量自动贡献的担忧。 该政策文档托管在 sourceware.org 上，与 LLVM 现有的 AI 工具政策相似，都要求对 LLM 生成的代码或文本保持人工参与。

hackernews · arto · 7月30日 11:45 · [社区讨论](https://news.ycombinator.com/item?id=49108685)

**背景**: GCC（GNU 编译器套件）是一个重要的开源编译器套件。随着大型语言模型（LLM）的普及，像 GCC 这样的项目面临大量 AI 生成的补丁，因此需要明确的贡献指南来保持质量和责任。

**社区讨论**: 评论者普遍欢迎这项政策，指出它符合 LLVM 的做法。一些人强调了低质量 AI 生成 PR 的问题，而另一些人则赞扬 GNU 在指导新贡献者方面的包容态度。

**标签**: `#GCC`, `#AI policy`, `#open source`, `#contribution guidelines`, `#LLM`

---

<a id="item-12"></a>
## [教授因审稿流程失去潜在博士生](https://www.reddit.com/r/MachineLearning/comments/1vawwb8/i_have_lost_three_and_a_half_potential_phd/) ⭐️ 8.0/10

一位早期职业教授报告称，由于会议同行评审过程让学生感到沮丧，他失去了三位半潜在博士生，尽管这些学生产出了高质量论文并获得了正面评审意见。 这凸显了机器学习研究中的一个系统性问题，即同行评审过程（尤其是在顶级会议上）可能阻碍有才华的年轻研究者攻读博士学位，威胁到未来研究人才的储备。 论文获得了非常正面的评审意见（例如四份一致弱接收），但仍被拒绝，导致无休止的重新提交循环，解决之前的意见后只会引入新的随机批评。这位教授在顶级会议有超过 10 年经验，并判断这些工作远超接收门槛。

reddit · r/MachineLearning · /u/AffectionateLife5693 · 7月30日 15:30

**背景**: 在机器学习研究中，顶级会议（如 NeurIPS、ICML、ICLR）是主要的发表场所，接收竞争非常激烈。同行评审过程常因其随机性、不一致性和高拒绝率而受到批评，导致多次重投。这种压力可能会让早期研究者和考虑在该领域攻读博士学位的学生失去动力。

**标签**: `#ML research`, `#peer review`, `#PhD education`, `#academic culture`

---

<a id="item-13"></a>
## [MLVC：迈向实际部署的多平台学习型视频编解码器](https://www.reddit.com/r/MachineLearning/comments/1vb3xwd/mlvc_multiplatform_learned_video_codec_for/) ⭐️ 8.0/10

MLVC 是一种学习型视频编解码器，它通过超先验显式传输熵模型尺度参数，解决了跨平台不兼容问题，使得在不同 NPU 上无需相同硬件即可实现比特精确解码。 这解决了阻止学习型视频编解码器在实际应用中取代传统编解码器（如 H.264/AV1）的关键障碍，有望在多样化硬件上实现高效的基于 AI 的视频压缩。 MLVC 在消费级 NPU 上对 360p/540p 视频实现了约 100 FPS 的速度，它通过避免跨平台比特精确的神经网络执行，绕过了对完全标准化定点算术的需求。

reddit · r/MachineLearning · /u/tanelai · 7月30日 19:40

**背景**: 传统视频编解码器如 H.264、H.265 和 AV1 依赖于手工设计的算法，并拥有广泛的硬件加速，因此计算成本低。学习型视频编解码器使用神经网络在压缩效率上超越传统编解码器，但由于熵模型推理中的数值差异，在计算需求高和跨平台可重现性方面存在困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.28027">MLVC: A Multi-platform Learned Video Codec for Real-World...</a></li>
<li><a href="https://www.forasoft.com/learn/video-encoding/articles/key-scientific-breakthroughs-codecs">Key Scientific Breakthroughs Behind Video Codecs : Information Theory</a></li>

</ul>
</details>

**标签**: `#video codec`, `#machine learning`, `#AI`, `#compression`, `#deployment`

---

<a id="item-14"></a>
## [英国 CMA 提议允许应用开发者引导用户使用替代支付](https://t.me/zaihuapd/42855) ⭐️ 8.0/10

6 月 30 日，英国竞争与市场管理局提议允许应用开发者将用户引导至苹果和 Google 应用商店之外的支付选项，旨在降低费用并促进竞争。 这可能大大降低开发者和消费者的成本，可能迫使苹果和 Google 调整其佣金结构，并为全球数字市场监管树立先例。 CMA 还提议，如果苹果或 Google 为此类引导行为收费，费用必须公平合理且低于现有佣金，节省的部分应让消费者受益或用于创新。此外，CMA 正考虑要求苹果开放其 NFC 技术，以便在 iOS 应用中提供非接触式支付。

telegram · zaihuapd · 7月30日 02:10

**背景**: 目前，苹果和 Google 要求许多应用开发者使用其应用内支付系统，并收取 15-30%的佣金。英国新的数字市场制度赋予 CMA 监管具有战略市场地位的公司的权力。近场通信（NFC）是一种实现非接触式支付的技术；苹果一直限制 iPhone 上 NFC 芯片的访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Contactless_payment">Contactless payment - Wikipedia</a></li>
<li><a href="https://www.android.com/intl/en_uk/articles/how-to-turn-on-nfc/">How to Turn On NFC Settings for Contactless Payments | Android</a></li>

</ul>
</details>

**标签**: `#regulation`, `#Apple`, `#Google`, `#app store`, `#antitrust`

---

<a id="item-15"></a>
## [欧盟启动 AI 超级工厂招标，拟撬动 300 亿欧元](https://www.wsj.com/world/europe/eu-opens-call-for-creation-of-local-ai-gigafactories-c286213d) ⭐️ 8.0/10

欧盟委员会周四启动最多七座 AI 超级工厂的招标程序，目标是撬动约 300 亿欧元投资，其中 100 亿欧元来自欧盟和成员国共同出资。 此举标志着欧盟战略性地建设本土 AI 基础设施，以在全球范围内与美国和中国竞争，可能加速欧洲的 AI 研究和应用部署。 投标截止日期为 11 月 12 日，中标结果预计 2027 年 7 月公布，项目须在签约后 18 个月内投入运营。招标涵盖新建选址和现有设施扩建两个阶段。

telegram · zaihuapd · 7月30日 11:50

**背景**: AI 工厂是为 AI 开发者提供高性能计算（HPC）、数据和技能一站式访问的生态系统。欧盟一直在投资超算基础设施，本次招标是升级 12 座科学超算中心为 AI 工厂的更广泛计划的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sango-automation.com/news/europe-s-huge-investment-in-building-ai-super-84958381.html">Europe 's Huge Investment in Building AI Super Factories Will Face...</a></li>
<li><a href="https://csc.fi/en/media-release/new-pan-european-supercomputer-and-eu-ai-factory-in-finland/">A new pan- European supercomputer and a European Union AI ... - CSC</a></li>

</ul>
</details>

**标签**: `#AI`, `#EU Policy`, `#Supercomputing`, `#Investment`

---