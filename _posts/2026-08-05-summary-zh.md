---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 32 条内容中筛选出 12 条重要资讯。

---

1. [DeepMind 管理层变动：哈萨比斯转任董事长，杰夫·迪恩离职](#item-1) ⭐️ 9.0/10
2. [ChainDrop 蠕虫攻陷 npm 逾 1300 个包](#item-2) ⭐️ 9.0/10
3. [OpenAI 发布全双工语音模型 GPT-Live，实现实时对话](#item-3) ⭐️ 9.0/10
4. [Discovery Loop 旨在自动化机器学习实验循环](#item-4) ⭐️ 8.0/10
5. [Cloudflare OS：为 AI 代理、应用与工作打造的开源平台](#item-5) ⭐️ 8.0/10
6. [LLM 无法跳跃：推理局限的立场论文](#item-6) ⭐️ 8.0/10
7. [新墨西哥州飞机坠毁引发对军用 GPS 干扰的质疑](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5 根据一条推文一次性生成完整游戏《Raccoon Heist》](#item-8) ⭐️ 8.0/10
9. [LLM 0.32 大更新：推理轨迹、服务端工具与 Responses API](#item-9) ⭐️ 8.0/10
10. [DeepSeek 重启第二轮融资 投前估值 5000 亿元](#item-10) ⭐️ 8.0/10
11. [三星与 SK 海力士据报测试中微设备以对冲美国出口管制](#item-11) ⭐️ 8.0/10
12. [FFmpeg 9.0 发布：支持动画 WebP 与 Claude AI 辅助开发](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepMind 管理层变动：哈萨比斯转任董事长，杰夫·迪恩离职](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/) ⭐️ 9.0/10

Google DeepMind 首席执行官德米斯·哈萨比斯将转任董事长，而传奇工程师杰夫·迪恩和桑贾伊·格玛沃特将离开谷歌，创办一家专注于机器学习、科学和工程的独立公益公司（PBC）。 这标志着在关键时期谷歌 AI 领导层的重大重塑。迪恩和格玛沃特是谷歌最受尊敬的两位技术人物，他们的离开可能意味着机构知识的流失，并引发对 Google DeepMind 人才留任的担忧。 杰夫·迪恩在谷歌工作了 27 年；他与格玛沃特将创办一家新的公益公司（PBC）。据报道，哈萨比斯还将在 Alphabet 范围内承担更广泛的职责，实际上承担类似首席科学家的角色，同时继续作为 Google DeepMind 的董事长。

hackernews · colesantiago · 8月5日 16:05 · [社区讨论](https://news.ycombinator.com/item?id=49184755)

**背景**: Google DeepMind 是谷歌在 2014 年收购 DeepMind 后，后来与 Google Brain 合并而成。德米斯·哈萨比斯是 DeepMind 的联合创始人，并长期担任 CEO；杰夫·迪恩是谷歌高级研究员（Google Senior Fellow），也是谷歌大规模 AI 与基础设施系统的关键设计者。这一公告反映了谷歌和 Alphabet 正在进行的 AI 领导层重组。

**社区讨论**: 社区成员反应震惊和担忧，称此举是'黄金时代的终结'，并指出谷歌人才大量外流，包括 Noam Shazeer、Oriol Vinyals 和 John Jumper 等。有人指出杰夫·迪恩的离职导致股价下跌 5%，并开玩笑道'新的杰夫·迪恩事实'。还有人认为更大的事不是哈萨比斯的职位变动，而是迪恩和格玛沃特的离开。

**标签**: `#Google`, `#DeepMind`, `#AI Leadership`, `#Jeff Dean`, `#Demis Hassabis`

---

<a id="item-2"></a>
## [ChainDrop 蠕虫攻陷 npm 逾 1300 个包](https://www.bleepingcomputer.com/news/security/massive-chaindrop-npm-supply-chain-attack-infects-hundreds-of-packages/) ⭐️ 9.0/10

自我传播的 ChainDrop 蠕虫已攻陷超过 1300 个 npm 包，包括 Keyv 和 Cacheable 等热门缓存工具，这些包合计月下载量达 20 亿次。攻击始于 Keyv 维护者的 GitHub 账号被入侵，并通过正常的 GitHub Actions 工作流发布恶意版本而扩散。 这是一次严重的供应链攻击，会窃取 GitHub、npm、AWS 和 Kubernetes 中的凭证，威胁整个软件生态系统。受影响的系统必须视为已被攻破，需要立即重建环境并轮换令牌。 恶意包中包含 setup.mjs 投放器和 Math_Symbol.js 凭证窃取脚本，它们会在执行 npm install 时自动运行。npm-cache[.]com 域名可作为失陷指标；受害者应重建环境并轮换所有令牌。

telegram · zaihuapd · 8月5日 03:04

**背景**: 供应链攻击通过入侵开发者自动下载的第三方依赖代码来利用信任关系。ChainDrop 这样的自我传播蠕虫更进一步，利用窃取的凭证感染更多包，形成连锁效应。ChainDrop 是 Shai-Hulud 窃密软件家族的一个变种，该家族此前曾多次针对软件仓库发起攻击。这类攻击尤其危险，因为它能在常规的包安装过程中悄无声息地传播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/">ChainDrop supply chain compromise: Anatomy of a self ...</a></li>
<li><a href="https://www.securityweek.com/over-400-npm-packages-infected-in-chaindrop-supply-chain-attack/">Over 400 NPM Packages Infected in ChainDrop ... - SecurityWeek</a></li>
<li><a href="https://www.itpro.com/security/malware/shai-hulud-here-we-go-again-thousands-of-npm-packages-compromised-in-chaindrop-malware-campaign-where-hackers-taunt-victims">‘Shai-Hulud: Here We Go Again’: Thousands of npm packages compromised in ‘Chaindrop’ malware campaign where hackers taunt victims | IT Pro</a></li>

</ul>
</details>

**标签**: `#供应链攻击`, `#npm安全`, `#恶意软件`, `#凭证窃取`, `#安全漏洞`

---

<a id="item-3"></a>
## [OpenAI 发布全双工语音模型 GPT-Live，实现实时对话](https://t.me/zaihuapd/42984) ⭐️ 9.0/10

2026 年 7 月 8 日，OpenAI 发布了新一代语音模型 GPT-Live，采用全双工架构，让用户能够同时听和说。该模型正在向全球 ChatGPT 用户推出，其中 GPT-Live-1 和 GPT-Live-1 mini 分别作为付费和免费用户的默认语音模型。 这一突破让 AI 对话更加自然，允许用户随时打断并实现双向同时说话，减少了以往语音助手的机械式轮流发言。它很可能为语音交互树立新标准，并影响数十亿 ChatGPT 用户与 AI 的互动方式。 GPT-Live 的全双工设计使其能够边说边听，并可在后台调用 GPT-5.5 完成搜索与复杂推理。该模型提供两个版本：GPT-Live-1 面向付费用户，GPT-Live-1 mini 面向免费用户。

telegram · zaihuapd · 8月5日 04:42

**背景**: 传统语音助手采用轮流发言或半双工模式，一次只有一方说话，使对话显得生硬。全双工通信如同电话通话，允许双方同时发送和接收，从而实现更自然的打断和重叠语音。GPT-Live 正是基于这一概念，并在后台利用 GPT-5.5 处理高级任务，同时不打断对话流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT‑Live - OpenAI</a></li>
<li><a href="https://kie.ai/blog/gpt-live-full-duplex-voice-model-deep-dive">GPT-Live Deep Dive: OpenAI's Full-Duplex Voice Model</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/gpt-live-review-openai-voice-model-july-2026">GPT-Live Review: OpenAI's Full-Duplex Voice Model Explained ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-Live`, `#voice model`, `#real-time conversation`, `#AI`

---

<a id="item-4"></a>
## [Discovery Loop 旨在自动化机器学习实验循环](https://www.discoveryloop.com/) ⭐️ 8.0/10

Discovery Loop 是一项新宣布的机构计划，旨在自动化机器学习研究与工程中的实验循环（experimental loop）。该项目力求将科学发现规模化扩展到多个领域，但目前主要以公告/落地页的形式存在。 自动化实验循环有可能大幅加速机器学习研究，减少人工试错工作。此举标志着机构对自动导向实验室（self-driving labs）和自主研究系统的兴趣日益增加，与 Sakana AI 的 AI Scientist 和 Karpathy 的 autoresearch 等项目相呼应。 该计划声称其方法广泛适用于科学与工程领域，但初期将聚焦于机器学习研究。它强调需要同时具备机器学习和大规模系统方面的深厚专业能力，并提到美国国家工程院（NAE）的十四项重大挑战是其潜在应用方向。

hackernews · xtreak29 · 8月5日 16:19 · [社区讨论](https://news.ycombinator.com/item?id=49184960)

**背景**: 机器学习研究中的实验循环通常包括提出假设、设计实验、运行实验和分析结果，这一过程往往依赖人工且耗时。近期一些工作，如 Sakana AI 的 AI Scientist（arXiv:2408.06292）以及基于 LLM 智能体的自主研究循环框架，已经开始将这一生命周期的部分环节自动化。Discovery Loop 似乎是这一思路的更机构化、更大规模的版本，旨在将自动化整合到许多科学领域。对于需要物理实验设备的研究，自动化仍具挑战性，但对机器学习、软件工程等计算领域则相对可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2408.06292">[2408.06292] The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery</a></li>
<li><a href="https://sakana.ai/ai-scientist/">The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery</a></li>
<li><a href="https://dl.acm.org/doi/full/10.1145/3802133.3802134">Autonomous Research Loops: An LLM-Agent Framework for End-to ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该计划类似于 Karpathy 的 autoresearch 的机构化、大规模扩展版本，还有人引用了 Karpathy 提出的“异步大规模多智能体协作（SETI@home 风格）”方向。另一些评论者对自动化物理实验表示怀疑，认为人工智能缺乏在实验室中操作的身体；还有人嘲讽该使命宣言中充斥着晦涩术语。总体而言，社区态度是既有好奇也有谨慎。

**标签**: `#machine-learning`, `#research-automation`, `#scientific-discovery`, `#AI-systems`, `#experimental-loop`

---

<a id="item-5"></a>
## [Cloudflare OS：为 AI 代理、应用与工作打造的开源平台](https://blog.cloudflare.com/cloudflare-os/) ⭐️ 8.0/10

Cloudflare 发布了 Cloudflare OS，这是一个用于在 Workers 边缘平台构建和托管 AI 代理与应用的开放平台。该项目以“代理工作空间”的形式在 GitHub 上开源，可用于创建文档、构建应用，并结合公司上下文和系统运行代理。 这一发布标志着 Cloudflare 向企业 AI 编排核心平台的进军，让企业能够在内置安全和访问控制下运行 AI 代理。如果被广泛采用，它可能重塑内部工具和仪表盘的构建方式，使其迁移到边缘基础设施上。 该平台以开源“代理工作空间”的形式在 GitHub 上发布，底层基于 Cloudflare Workers。它像一个带连接器、可接入内部系统的聊天机器人；Kenton Varda 表示，它在概念上是其早期开源项目 Sandstorm.io 的再造，只是这次构建在 Workers 之上并深度融入了 AI。

hackernews · speckx · 8月5日 13:58 · [社区讨论](https://news.ycombinator.com/item?id=49182996)

**背景**: Cloudflare Workers 是 Cloudflare 的无服务器边缘计算平台，让开发者无需管理服务器即可在全球各地就近运行代码。Cloudflare 还提供 Workers AI，用于在边缘运行 AI 推理。Cloudflare OS 旨在将这些能力整合成一个类似操作系统的层，让员工可以通过聊天机器人驱动的界面与公司数据交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/cloudflare-os/">Cloudflare OS: an open platform for agents, apps, and work</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-os">GitHub - cloudflare/cloudflare-os: Agent workspace built on Cloudflare ...</a></li>
<li><a href="https://www.cloudflare.com/products/workers-ai/">Cloudflare Workers AI - Edge AI Inference Platform</a></li>

</ul>
</details>

**社区讨论**: 早期用户反馈称，在 Workers 上部署大约只需一分钟，并能配合 Cloudflare Access SSO 使用，但提供方配置不太方便。与此同时，一些评论者担心被 Cloudflare 锁定，另一些人则批评该公司把“OS”当营销流行语来用。

**标签**: `#cloudflare`, `#agents`, `#platform`, `#workers`, `#ai`

---

<a id="item-6"></a>
## [LLM 无法跳跃：推理局限的立场论文](https://openreview.net/challenge?redirect=%2Fforum%3Fid%3DklU4737opt) ⭐️ 8.0/10

DeepMind 的 Tom Zahavy 在一篇立场论文中提出，大语言模型无法做出解决分布外问题所需的直觉性“跳跃”，并质疑 LLM 能带来全新科学发现的说法。该论文在 OpenReview 和社交媒体上引发了热烈讨论。 这一观点具有重要意义，因为它反驳了“LLM 能通过在训练数据之外推理来加速科学发现”的乐观叙事。它影响着研究者如何用 LLM 提出假说，也有助于为 AI 推理能力设定现实的预期。 该论文属于立场论文而非实证研究，因此一些评论者批评它缺乏定量证据。讨论中还指出语言是对人类经验的有损编码，暗示仅靠文本训练存在根本性的局限。

hackernews · theanonymousone · 8月5日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49181083)

**背景**: 分布外泛化（OOD generalization）指模型处理与训练分布不同数据的能力，是机器学习的核心挑战之一。系统性泛化又称组合泛化，指人类以新方式重新组合已知概念的能力。立场论文基于推理和现有文献而非新实验来阐述观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2402.06599">[2402.06599] On the Out-Of-Distribution Generalization of ... On the Out-Of-Distribution Generalization of Multimodal Large ... Out-of-Distribution Generalization in Natural Language ... CVPR 2026 Open Access Repository Out-of-Distribution Generalization in Natural Language ... Out-of-Distribution Generalization in Natural Language ... On the Out-Of-Distribution Generalization of Large Multimodal ...</a></li>
<li><a href="https://www.nature.com/articles/s41586-023-06668-3">Human-like systematic generalization through a meta-learning ...</a></li>
<li><a href="https://arxiv.org/html/2209.01610v3">Generalization in neural networks: a broad survey - arXiv.org</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人支持该论文，也有人批评它“只是一个人的观点”、缺乏定量支持。还有人讨论语言的有损本质，并指出关于爱因斯坦的简化历史叙述并不准确，为辩论增添了更多层次。

**标签**: `#LLMs`, `#AI research`, `#reasoning`, `#position paper`, `#DeepMind`

---

<a id="item-7"></a>
## [新墨西哥州飞机坠毁引发对军用 GPS 干扰的质疑](https://www.wired.com/story/a-civilian-plane-crashed-in-new-mexico-was-the-militarys-tech-to-blame/) ⭐️ 8.0/10

美国国家运输安全委员会（NTSB）正在调查新墨西哥州一架民用医疗救援飞机坠毁事件，该事件可能与美军 GPS 干扰演习有关。飞机在撞山前失去了 GPS 信号，机上人员全部遇难。 这起事件凸显了 GPS 干扰对民航日益严重的威胁，以及军事演习与飞行安全之间的潜在冲突。它也引发了关于飞行员对 GPS 依赖程度、以及加强保障和冗余导航系统必要性的讨论。 NTSB 的初步报告显示机组人员做出了错误决策，专家们对 GPS 干扰还是飞行员失误是主要原因存在分歧。GPS 干扰会破坏 ADS-B 和导航功能，但飞机拥有 DME/DME 三角测量等替代系统，一些飞行员可能因此变得自满。

hackernews · dzdt · 8月5日 11:03 · [社区讨论](https://news.ycombinator.com/item?id=49181099)

**背景**: GPS 干扰是一种无线电干扰形式，用强大的信号压倒 GNSS 接收器，使其无法计算位置或时间。在民航领域，它会破坏导航和 ADS-B 传输，FAA 已将 GNSS 干扰视为新出现的威胁。虽然军事演习是干扰的常见来源，但 ICAO 和 IATA 建议各国尽量减少其对民航的影响。飞机和飞行员接受过使用冗余导航系统的训练，但 GPS 的便利性可能掩盖了导航严谨性的下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/us-military-gps-jamming-exercise-suspected-of-contributing-to-civilian-plane-crash-in-new-mexico-medevac-flight-lost-signal-before-flying-into-a-mountain-killing-everyone-onboard">US military GPS jamming exercise suspected of contributing to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPS_jamming">GPS jamming</a></li>
<li><a href="https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afx/afs/afs400/afs410/GNSS/GPS_GNSS_Interference_Resource_Guide.pdf">GPS and GNSS Interference Resource Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意，虽然 GPS 干扰是一个促成因素，但飞行员所做的糟糕决策导致了坠机。一位航线机长指出，在无月夜晚于山区地形进行目视进近非常危险；GPSJAM.org 的 jjwiseman 也表示，NTSB 报告似乎显示机组人员做出了糟糕的选择。还有人认为 GPS 并非必需，飞行员在导航严谨性上变得自满。

**标签**: `#GPS`, `#aviation`, `#safety`, `#interference`, `#NTSB`

---

<a id="item-8"></a>
## [Claude Fable 5 根据一条推文一次性生成完整游戏《Raccoon Heist》](https://simonwillison.net/2026/Aug/5/raccoon-heist/#atom-everything) ⭐️ 8.0/10

Simon Willison 使用 Anthropic 的 Claude Fable 5（通过 Claude Code for web）将 2022 年一条推文中的概念变成了可玩的完整游戏《Raccoon Heist》。该模型根据推文截图和提示词独立构建了整个游戏，结果已上线 GitHub Pages。 这标志着 AI 编程智能体的一个重要里程碑：模型现在可以仅凭简单的提示词和图片，在极少人工干预下生成完整、可玩的电子游戏。它表明 AI 辅助开发正从生成代码片段走向端到端的项目交付，影响开发者与爱好者制作游戏原型的方式。 该流程使用 Claude Code for web 和 GitHub Pages 来解决测试中间产物困难的问题：用户让 Claude 尽早提交一个 index.html，然后在仓库设置中从生成的 branch 部署 Pages。游戏和代码仓库均已公开，并附有视频演示。

rss · Simon Willison · 8月5日 19:42

**背景**: Claude Fable 5 是 Anthropic 于 2026 年 6 月 9 日发布的“Mythos 级”大语言模型，已做安全化处理供公众使用；其受限访问版本 Claude Mythos 5 与它是同一个底层模型，只是部分领域的安全限制被放宽。Claude Code 是 Anthropic 的智能体编程工具，能理解代码库、编辑文件、运行命令并帮助交付项目；Claude Code for web 则允许用户无需打开终端，直接在浏览器或移动应用中启动编码会话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://claude.com/blog/claude-code-on-the-web">Claude Code on the web | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Game Development`, `#Coding Agent`, `#LLM`

---

<a id="item-9"></a>
## [LLM 0.32 大更新：推理轨迹、服务端工具与 Responses API](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32 是 Simon Willison 的 CLI 工具的重大更新，新增了可见的推理轨迹、OpenAI CodeInterpreter 和 WebSearch 等服务端工具、重新设计的内容寻址 SQLite 日志，以及对 OpenAI Responses API 的支持。随附的 llm-anthropic 插件 0.26 增加了 WebSearch、WebFetch、CodeExecution 和 AnthropicMCP 工具。 这是 LLM 自发布以来最重要的一次版本更新，它让推理轨迹可见而不会污染管道输出，并启用了跨提供方使用的服务端工具。该版本让工具与 OpenAI 较新的 Responses API 对齐，降低了把 LLM 当作灵活命令行界面使用的开发者的使用门槛。 默认情况下，推理轨迹会输出到标准错误流；用 -R/--hide-reasoning 参数可关闭。`llm` 提示的默认模型现在是价格较低的 GPT-5.6 Luna，新的 `llm openai endpoint` 命令可对任何兼容 OpenAI 的端点运行一次性提示，且不会记录日志。

rss · Simon Willison · 8月4日 23:58

**背景**: LLM 是 Simon Willison 开发的一款命令行工具，用于与不同提供方的大语言模型交互。推理轨迹是推理模型产生的内部思维链步骤，通常被隐藏，现在 LLM 会将其显示到标准错误流。OpenAI Responses API 是 2025 年 3 月推出的开发者 API，旨在通过统一工具调用来简化智能体应用；服务端工具允许模型在不需要客户端基础设施的情况下执行代码或搜索网页。内容寻址 SQLite 日志按内容的哈希值存储日志记录，便于关联和复现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Responses_API">OpenAI Responses API</a></li>
<li><a href="https://arxiv.org/html/2510.20665v1">The Shape of Reasoning: Topological Analysis of - arXiv.org</a></li>
<li><a href="https://blog.textile.io/the-quest-for-a-content-addressable-sqlite">The Quest for a Content Addressable SQLite</a></li>

</ul>
</details>

**标签**: `#LLM`, `#OpenAI`, `#CLI`, `#release`, `#developer-tools`

---

<a id="item-10"></a>
## [DeepSeek 重启第二轮融资 投前估值 5000 亿元](https://finance.sina.com.cn/wm/2026-08-05/doc-inimfmyv1554159.shtml) ⭐️ 8.0/10

DeepSeek 已重启第二轮融资，投前估值约 5000 亿元人民币，计划募资 500 亿元，预计 8 月下旬完成签约。该轮融资曾于 7 月底暂停，原因是创始人梁文锋对疑似泄露的面向投资者的会议实录表示不满。 本轮融资规模巨大，估值较首轮提升约 43%，体现出市场对 DeepSeek 发展前景的强烈信心。若顺利完成，两轮合计募资将超 1000 亿元，使 DeepSeek 在中国竞争激烈的 AI 领域中占据重要地位。 本轮投前估值约 5000 亿元，较 6 月完成的首轮融资（估值超 3500 亿元）提升约 43%。首轮融资于 4 月开启、6 月交割，金额为 500 亿元；本轮暂停据说源于创始人梁文锋对网上流传的疑似泄露会议实录的不满，部分机构表示重启消息尚未接到，通道仍处暂缓状态。

telegram · zaihuapd · 8月5日 02:46

**背景**: DeepSeek 是一家总部位于杭州的中国人工智能公司，主要开发大型语言模型，以 AI 助手和开源模型著称。该公司近期因其具有竞争力的 AI 能力而受到全球关注，与百度文心一言、字节跳动豆包等中国 AI 产品类似。本轮融资反映出中国 AI 初创企业的快速成长和高资本需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/c5yv5976z9po">What is DeepSeek - and why is everyone talking about it?</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI`, `#funding`, `#valuation`, `#business`

---

<a id="item-11"></a>
## [三星与 SK 海力士据报测试中微设备以对冲美国出口管制](https://www.reuters.com/world/china/samsung-sk-hynix-test-chinese-chip-tools-hedge-against-us-risks-2026-08-05/) ⭐️ 8.0/10

路透社 8 月 5 日援引知情人士称，三星电子和 SK 海力士近两年一直在评估中国半导体设备商中微公司（AMEC）的刻蚀设备，考虑用于其在华工厂，但尚未决定是否大规模部署。三星否认相关测试，SK 海力士拒绝置评。 此举意义重大，因为如果两大存储芯片巨头采用中国设备，将为中国设备商提供有力背书，并可能加速在出口管制背景下向西方供应商之外的多元化转变。这也表明美国限制正促使盟友通过供应链多元化来对冲风险。 美国在 2025 年撤销了两家韩企中国工厂的“经验证最终用户”（VEU）待遇，改为年度许可，韩企担忧未来限制可能影响现有西方设备的维护。中国设备价格通常低 20%至 30%；德意志银行预计，今年中国本土设备商可能占据中国约 280 亿美元晶圆制造设备市场的 25%至 30%。

telegram · zaihuapd · 8月5日 04:32

**背景**: 中微公司（AMEC，全称 Advanced Micro-Fabrication Equipment）是一家部分国有的中国上市公司，也是中国最大的半导体设备制造商之一，生产刻蚀设备等产品。刻蚀是芯片制造中的关键步骤，通过化学方式去除硅片上的材料层以形成电路。VEU 项目是美国出口管制的一种授权机制，允许向经预先审核的实体出口受控物项，但需遵守美国商务部工业与安全局设定的条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Micro-Fabrication_Equipment">Advanced Micro-Fabrication Equipment - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Etching_(microfabrication)">Etching (microfabrication) - Wikipedia</a></li>
<li><a href="https://www.bis.doc.gov/index.php/policy-guidance/deemed-exports/deemed-exports-faqs/faq/24-what-is-the-difference-between-a-validated-end-user-and-an-eligible-destination">Deemed Exports FAQs - What is the difference between a “Validated End-User” and an “Eligible Destination”?</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#export-controls`, `#chip-equipment`, `#China`, `#supply-chain`

---

<a id="item-12"></a>
## [FFmpeg 9.0 发布：支持动画 WebP 与 Claude AI 辅助开发](https://news.ycombinator.com/item?id=49166202) ⭐️ 8.0/10

FFmpeg 9.0 正式发布，新增动画 WebP 解码器与分离器、v360_vulkan 滤镜、Playdate 视频编码器及封装器、HE-AAC 960 解码（DAB+）、transpose_cuda 滤镜、AMF 帧率转换器滤镜和 ONNX Runtime DNN 后端。开发团队还通过 Anthropic 的开源计划获得了六个月免费 Claude Max 使用权，主要利用 AI 查找缺失的向后移植。 作为被广泛使用的多媒体框架，FFmpeg 的这次重大发布扩展了多媒体格式支持，并增加了现代 GPU 加速滤镜。同时，它也凸显了 AI 在开源开发中日益重要的作用，引发了关于 AI 辅助贡献安全审查流程的讨论。 值得注意的新功能包括动画 WebP 解码器、用于 360 度视频转换的 v360_vulkan 滤镜，以及对 .pdv（Playdate 视频）文件的支持。AI 辅助主要用于识别缺失的向后移植，不过一些社区成员对 AI 辅助开发的安全审查流程表达了担忧。

telegram · zaihuapd · 8月5日 10:32

**背景**: FFmpeg 是领先的开源多媒体框架，广泛用于音视频的编码、解码、转码和滤镜处理。动画 WebP 是一种支持动画的图像格式，类似于 GIF，但压缩效率更高。Claude 是 Anthropic 的 AI 助手，Claude for Open Source Program 为开源项目提供免费的 AI 工具使用权。v360_vulkan 滤镜利用 Vulkan API 实现 GPU 加速的 360 度视频投影转换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ffmpeg.org/ffmpeg-filters.html">FFmpeg Filters Documentation</a></li>
<li><a href="https://www.phoronix.com/news/FFmpeg-360-Degree-Vulkan">FFmpeg Introduces Vulkan-Accelerated 360 Degree Video ...</a></li>
<li><a href="https://trac.ffmpeg.org/ticket/10324">#10324 (Add support for .pdv ( Playdate video format )) – FFmpeg</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论既对 FFmpeg 新版本表示热情，也对 AI 辅助开发流程提出质疑。一些评论者担心 AI 生成的代码在被合并到关键开源项目之前，是否经过了足够的安全审查。

**标签**: `#FFmpeg`, `#release`, `#multimedia`, `#AI`, `#open source`

---