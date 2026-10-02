---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02
lang: zh
---

> 从 32 条内容中筛选出 5 条重要资讯。

---

1. [2025 年诺贝尔生理学或医学奖授予外周免疫耐受发现者](#item-1) ⭐️ 9.0/10
2. [新型 AI 击败史上最强 Stratego 棋手，训练用量比 DeepNash 少 34 倍](#item-2) ⭐️ 8.0/10
3. [Zig v0.17.0 发布：扩展目标平台支持与全新构建集成](#item-3) ⭐️ 8.0/10
4. [Greg Kroah-Hartman：LLM 漏洞报告大多经不起推敲](#item-4) ⭐️ 8.0/10
5. [arXiv 对未核查的 LLM 生成内容实施 1 年禁投处罚](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [2025 年诺贝尔生理学或医学奖授予外周免疫耐受发现者](https://t.me/zaihuapd/44174) ⭐️ 9.0/10

2025 年诺贝尔生理学或医学奖授予 Mary E. Brunkow、Fred Ramsdell 和 Shimon Sakaguchi 三位科学家，以表彰他们在外周免疫耐受领域的开创性发现。他们的研究阐明了免疫系统为何不会误伤自身器官的关键机制，该消息目前仅以简短摘要形式公布，尚未附带详细解读。 这些发现奠定了现代调节性 T 细胞（Treg）生物学的基础，是理解自身免疫病、过敏与移植耐受的核心。它们直接影响了从自身免疫病治疗到肿瘤免疫治疗的研发思路，因此这次颁奖标志着整个生物医学界已把该方向视为公认的范式。 Sakaguchi 发现了表达 CD25、能抑制其他免疫细胞的 T 细胞亚群，Brunkow 和 Ramsdell 则通过 scurfy 小鼠与人类 IPEX 综合征追踪到关键基因 FOXP3。需要注意，外周耐受只是免疫防护的一层：胸腺中的中枢耐受清除自身反应性 T 细胞的效率仅约 60%–70%，剩余部分必须依靠外周机制来管控。

telegram · zaihuapd · 10月2日 14:15

**背景**: 免疫系统必须区分机体自身组织（"自我"）与外来威胁，这种能力被称为免疫耐受。T 细胞和 B 细胞在胸腺和骨髓中成熟，中枢耐受会清除大量自身反应性细胞，但仍有部分细胞逃逸到淋巴结和外周组织。外周免疫耐受随后通过克隆删除、失能（anergy，功能性沉默）以及调节性 T 细胞的抑制作用来控制这些漏网细胞，而 FOXP3 转录因子是调节性 T 细胞的主控开关。一旦这一控制失效，就会引发自身免疫病；FOXP3 缺陷的患者会出现严重的多器官自身免疫。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Peripheral_immune_tolerance">Peripheral immune tolerance</a></li>

</ul>
</details>

**标签**: `#Nobel Prize`, `#Immunology`, `#Peripheral Immune Tolerance`, `#Scientific Research`, `#Biomedical Breakthrough`

---

<a id="item-2"></a>
## [新型 AI 击败史上最强 Stratego 棋手，训练用量比 DeepNash 少 34 倍](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 8.0/10

一套新发表的 AI 系统（成果见于一篇 Nature 论文及配套的 arXiv 预印本 2511.07312）击败了史上最强的 Stratego 棋手。据报道，它是在相对有限的算力预算下做到的：训练所用对局数量比 DeepMind 的 DeepNash 少约 34 倍，最终棋力却明显更强。 Stratego 属于隐藏信息博弈，一步棋的好坏取决于玩家无法观测的信息，因此当年征服国际象棋和围棋的搜索与学习方法在此大打折扣。此次展示出一种样本效率极高的方法并能战胜最强人类棋手，意味着类似思路或可迁移到安全、谈判等同样存在隐藏信息的现实战略问题中。 核心难点在于隐藏信息使常规的前瞻搜索失效——你无法推演“我这样走、他就那样应对”，因为你根本不知道对手那个棋子是什么——算法只能改为对概率分布进行推理。社区讨论还提到，该 AI 发现了不寻常的策略，例如把军旗藏在角落、只用两颗炸弹掩护，而这种布局人类棋手极少采用。

hackernews · PaulHoule · 10月2日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**背景**: 在国际象棋、围棋这类完全信息博弈中，双方都能看到整个棋盘，因此 AI 可以向前搜索，并通过大量自我对弈超越人类。Stratego 则不同：每方的棋子对对手都是隐藏的，它与扑克以及现实世界中大量决策问题同属非完全信息博弈。DeepMind 在 2022 年提出的 DeepNash 是此前 Stratego 研究的里程碑，该公司还探索过 Player of Games 这类通用的非完全信息智能体。样本效率——即学习算法达到某一水平所需经验量——是强化学习的核心难题之一，而此次成果的价值主要体现在它相比以往 Stratego 工作的大幅改进上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://analyticsindiamag.com/ai-features/deepmind-comes-out-with-player-of-games-masters-both-perfect-and-imperfect-information-games">How does DeepMind's Player of Games master diverse games ? | AIM</a></li>
<li><a href="https://arxiv.org/abs/1807.01675">[1807.01675] Sample - Efficient Reinforcement Learning with...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者大多带着怀旧情绪分享儿时玩 Stratego 的经历：有人坦言曾发现朋友的棋子被偷偷做了标记，也有人表示自己当年在当地无人能敌，却从未想到这款游戏还有严肃的竞技选手。最具技术含量的观点来自 janalsncm，他认为“对局数减少 34 倍”才是真正的关键成果，因为隐藏信息使通常意义上的前瞻搜索无法进行。其他人则调侃自己原本打算做出第一个能赢的 Stratego 机器人，rcyeh 还讨论了尝试 AI 那种“军旗藏角落、两颗炸弹掩护”的布局，以消耗对手预期的步数。

**标签**: `#AI`, `#game-playing`, `#hidden-information`, `#reinforcement-learning`, `#Stratego`

---

<a id="item-3"></a>
## [Zig v0.17.0 发布：扩展目标平台支持与全新构建集成](https://ziglang.org/download/0.17.0/release-notes.html) ⭐️ 8.0/10

Zig 项目在 ziglang.org 上发布了 Zig v0.17.0 的官方发行说明，公布了这门系统编程语言的最新版本。社区讨论很快聚焦于该版本广泛的目标平台支持和新的构建系统集成，同时也就项目的 AI/LLM 政策以及尚未完成的异步 I/O 工作提出了疑问。 Zig 异常广泛的交叉编译目标支持，使其成为少数能在嵌入式和底层开发中真正与 C 竞争的新兴语言，因此每次版本更新都在扩大它的适用场景。构建集成的改进也会向外辐射到依赖 Zig 构建系统的工具链与打包生态。 评论者指出，本次版本中仍有两大特性停留在路线图上而尚未落地：全新的无栈协程（stackless coroutine）I/O 实现和一等公民的模糊测试（fuzzer）工具。此外，v0.17.0 中事件驱动 I/O 与 io_uring 的支持状况也被列为待解问题，而 Zig 目前已经提供了 std.testing.fuzz、std.testing.Smith 等有限的模糊测试基础能力。

hackernews · ErenayDev · 10月2日 20:56 · [社区讨论](https://news.ycombinator.com/item?id=49938521)

**背景**: Zig 是由 Andrew Kelley 创建并于 2016 年首次公布的通用系统编程语言与工具链，定位为对 C 语言的全面改进。它不使用宏和预处理器指令，而是提供带反射的编译期泛型、手动内存管理、紧凑结构体（packed struct）、任意宽度整数以及多种指针类型。项目由 Zig 软件基金会（ZSF）通过企业赞助和个人捐赠提供资金，并以 MIT 许可证开源发布。由于 Zig 仍处于 0.x 阶段，版本迭代频繁且常包含破坏性变更，因此每份发行说明都受到用户密切关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home Zig Programming Language</a></li>
<li><a href="https://andrewkelley.me/post/zig-new-async-io-text-version.html">Zig's New Async I/O (Text Version) - Andrew Kelley</a></li>

</ul>
</details>

**社区讨论**: 在 Hacker News 的 91 条评论中，主流态度是对 Zig 目标平台支持的赞叹，有评论者认为它可能是唯一能在这方面与 C 抗衡的语言，同时也对新的构建集成能为工具链带来什么充满期待。多位参与者反复询问该项目强硬的 AI/LLM 立场是否已经改变，有人指出 Andrew Kelley 受 SQLite 相关成果启发，开始接受用 LLM 来发现 bug，并将其视为通向"无 bug 软件"的一条路径。此外还有人追问事件驱动 I/O 与 io_uring 的现状，并把全新的无栈协程 I/O 实现和一等公民模糊测试工具列为最期待的特性。

**标签**: `#zig`, `#programming-languages`, `#systems-programming`, `#compilers`, `#release-notes`

---

<a id="item-4"></a>
## [Greg Kroah-Hartman：LLM 漏洞报告大多经不起推敲](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

在 Kernel Recipes 2026 的一场演讲中，资深 Linux 内核维护者 Greg Kroah-Hartman 剖析了 Anthropic 旗下 Mythos 的漏洞披露：在号称发现的 79 个漏洞中，有 24 个完全没有任何细节，14 个根本不是 bug，3 个是凭空捏造的数据，15 个已在最新版本中修复，真正需要修复的只剩约 20 个。他总结说，这整场营销故事最终折算下来大约只相当于一小时的内核开发工作量。 这是一次罕见且信息量极高的“打假”，来自对全球部署最广的内核拥有权威的维护者，提醒企业、媒体和公众不要把 AI 报出的 CVE 数量当成真实的安全价值。它也加剧了围绕前沿 AI 实验室的公信力争论：一边宣称模型危险到不能公开发布，一边其宣传式的数据却连基本核查都过不了。 在真正值得修复的约 20 个漏洞中，有 7 个建立在“恶意文件系统镜像”的假设之上，另有 2 个假设攻击者能控制输入，因此许多并非现实世界中可实际利用的威胁。Kroah-Hartman 还指出，Mythos 本质上是对过去几十年内核补丁做模式匹配，再把同样机制套用到别处去检查是否漏修，却没有对最初修复这些问题的内核开发者给予任何署名。

hackernews · usernomdeguerre · 10月2日 02:51 · [社区讨论](https://news.ycombinator.com/item?id=49929391)

**背景**: Linux 内核的缺陷与修复通过 CVE 编号和稳定版回移植来跟踪，而这类工作由 Greg Kroah-Hartman 等维护者公开协调，因此相关说法任何人都能核实。Anthropic 的 Claude Mythos 是一个受限访问的模型系列，官方以“能够发现软件漏洞”为由未向公众开放，而是仅授予部分机构用于安全扫描。与此同时，安全业界一直在担忧 LLM 生成的 CVE 描述和补丁建议会拉低漏洞数据的质量与可信度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Mythos">Anthropic Mythos</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>
<li><a href="https://vuldb.com/article/llm-generated-cve-descriptions-undermine-security-data-quality-and-trust">LLM Generated CVE Descriptions Undermine Security Data Quality...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大多赞赏 Kroah-Hartman 的坦率，有人直接引用幻灯片中的分类数据，凸显 79 个 CVE 的说法经核查后所剩无几。也有人指出实验室“模型危险到不能发布”与粗糙营销话术之间的强烈矛盾，批评 Anthropic 未给被其模式匹配的内核补丁原作者署名，同时认为未来基于内核专门训练的模型仍可能让缺陷发现更快、更准确。

**标签**: `#linux-kernel`, `#security`, `#LLM`, `#AI-hype`, `#vulnerability-research`

---

<a id="item-5"></a>
## [arXiv 对未核查的 LLM 生成内容实施 1 年禁投处罚](https://t.me/zaihuapd/44166) ⭐️ 8.0/10

arXiv 明确了针对稿件的处罚规则：如果稿件中出现足以证明作者未核查 LLM 生成结果的内容，作者将被禁止投稿 1 年。禁投期满后，其后续投稿还必须先被可信的同行评审 venue 接收，才能提交到 arXiv。 这是大型预印本平台首次针对未经核查使用 LLM 写作公布具体的惩罚措施，意味着学术平台正从模糊的 AI 使用指南转向可执行的制裁手段。这将直接影响研究者（尤其是 AI/ML 及相关领域）在撰写论文时使用 LLM 的方式，并可能为其他预印本平台和出版商树立先例。 处罚适用于诸如幻觉引用、正文中残留的 LLM 元注释，以及“表格数据仅为示例、请替换为真实实验数据”这类内容。arXiv 的行为准则要求，作者署名即代表对论文全部内容负责，不论这些内容是用何种方式生成的。

telegram · zaihuapd · 10月2日 06:21

**背景**: arXiv 是一个免费开放获取的预印本平台，收录了物理、数学、计算机科学等领域约 240 万篇论文，投稿仅经过审核（moderation）而非同行评审。大语言模型可能产生“幻觉”，即表达流畅、语气肯定但实际虚假的内容，其中就包括看似合理实则不存在的伪造引用。由于 arXiv 历来依赖作者自负其责而非正式同行评审，未核查的 LLM 生成内容混入预印本已成为明显问题，这促使平台出台这一明确的执行政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">arXiv - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.promptlayer.com/glossary/citation-hallucination/">What is Citation hallucination ?</a></li>

</ul>
</details>

**标签**: `#arXiv`, `#LLM`, `#academic-publishing`, `#research-integrity`, `#AI-policy`

---