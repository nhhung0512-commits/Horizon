---
layout: default
title: "Horizon Summary: 2026-09-18 (ZH)"
date: 2026-09-18
lang: zh
---

> 从 41 条内容中筛选出 7 条重要资讯。

---

1. [Dan Abramov 用 AI「vibe」出一个 Conway 猜想的改进并加以验证](#item-1) ⭐️ 8.0/10
2. [ZCode 被曝静默上传用户 Git 历史到云端](#item-2) ⭐️ 8.0/10
3. [韩国将数据泄露罚款上限提升至营收的 10%](#item-3) ⭐️ 8.0/10
4. [美军据报因 AI 幻觉情报险些酿成事故](#item-4) ⭐️ 8.0/10
5. [Rust 安全团队警告：针对知名维护者的定向社工攻击正在进行](#item-5) ⭐️ 8.0/10
6. [SemiAnalysis：面向高效 DRAM/SSD 卸载的软硬件协同设计](#item-6) ⭐️ 8.0/10
7. [研究员称 xAI Grok Build CLI 默认上传整个代码库与 .env 密钥文件](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Dan Abramov 用 AI「vibe」出一个 Conway 猜想的改进并加以验证](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/) ⭐️ 8.0/10

以 React 核心开发者身份闻名的 Dan Abramov 发布了博客文章《How I vibed a proof of Conway's conjecture》，并配套开源了 gaearon/conway-refinement 仓库，记录了他是如何借助 AI 开发并检验 Conway 宇宙定理（cosmological theorem）的一个改进版本的。该文章在 Hacker News 上引发了 194 分、172 条评论的热烈讨论，核心议题是 LLM 辅助的数学工作究竟价值几何。 这是一个非数学专业人士借助 LLM 推进形式化数学问题的具体案例，直接引出了一个紧迫问题：靠「vibe」得来的证明到底有多可信，又该由谁负责验证。讨论还预演了未来可能的分工模式：AI 负责生成候选论证，训练有素的数学家负责提供理解、简化和最终确认。 该成果被描述为对 Conway 定理的一个改进（refinement），而非颠覆领域的重大突破；Abramov 的仓库里专门有一节标题为「why I think it's correct」，阐述了他为何相信结论正确。他还提到自己通过邮件向数学家们提交了一些疑似笔误的修正建议，并得到了其中至少一部分确实成立的确认——这是一次非正式但值得注意的正确性抽查。

hackernews · m-hodges · 9月18日 14:36 · [社区讨论](https://news.ycombinator.com/item?id=49755024)

**背景**: Conway 宇宙定理研究的是「看数列」（look-and-say sequence）：数列以 1, 11, 21, 1211, 111221… 开头，每一项都是把前一项的连续相同数字成组读出来（「一个 1」写作 11，「两个 1」写作 21）。John Conway 证明任何这样的数列最终都会「衰变」成 94 种「原子元素」的复合体，这些原子元素此后不再与相邻部分发生相互作用。形式化验证指的是依据精确的数学规约来证明系统的正确性，而证明助手（proof assistant）则是人机协作、由人引导机器检查证明的交互式工具。这篇文章把两者结合起来：由 LLM 提出数学论证，再用形式化或非形式化的方式检验其是否站得住脚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conway's_cosmological_theorem">Conway's cosmological theorem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Look-and-say_sequence">Look-and-say sequence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant</a></li>

</ul>
</details>

**社区讨论**: 总体氛围是鼓励中带着方法论上的审慎：自称受过专业训练并发表过论文的数学家 pretzellogician 建议 Abramov 继续简化证明，直到自己能够完全看懂，并检查论证的各个部分是否只是对已知结果的照搬。gbjcantab 用奇幻设定里的比喻区分「巫术」（深入理解加上强大工具）与「法术」（召唤并控制自己并不真正理解的存在）；bwfan123 则认为数学家才是最大受益者，并给出了无限猴子定理的「LLM 推论」。还有评论者推荐了外部学习资源，比如一部长篇竞赛获奖视频，用 Hackenbush 游戏介绍超现实数（surreal numbers），说明这个讨论帖同时也成了一场真正的数学交流。

**标签**: `#ai-assisted-math`, `#formal-verification`, `#llms`, `#mathematics`, `#proof-assistants`

---

<a id="item-2"></a>
## [ZCode 被曝静默上传用户 Git 历史到云端](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) ⭐️ 8.0/10

Z.ai 旗下的 AI 编程开发环境 ZCode 被发现通过其“代码库索引”（codebase indexing）功能静默地把用户的 Git 历史上传到云端，Z.ai 随后进行了内部审查并向受影响用户公开致歉。该事件在开发者社区引发高度关注，在 Hacker News 上获得 234 分和 88 条评论。 这是一起 AI 编程助手在未获明确同意的情况下外传源代码相关数据的实际案例，动摇了用户对默认索取广泛文件系统和仓库访问权限的工具的信任。它也加剧了业界关于 AI 代理权限、沙箱机制，以及 AI 开发工具的数据采集是否应改为默认关闭、用户主动开启的争论。 根据 Z.ai 的声明，此次上传源自 ZCode 的代码库索引功能，该功能的初衷是让助手更好地理解项目上下文；官方的回应主要是致歉和解释，并未详细说明究竟传输了哪些文件、数据被保留多久。由于 .git 目录可能包含完整提交历史、已删除的密钥和硬编码凭证，静默外传它的敏感程度远高于上传普通源文件。

hackernews · csmantle · 9月18日 06:11 · [社区讨论](https://news.ycombinator.com/item?id=49750694)

**背景**: ZCode 是 Z.ai 基于其 GLM 系列模型打造的桌面端 AI 编程环境，对标 Claude Code、Codex 等让 AI 代理直接访问开发者本地文件的工具。这类工具通常会扫描或索引项目，以便模型检索相关代码作为上下文，而这种索引一般被宣传为本地操作。Git 是源代码领域几乎通用的版本控制系统，其隐藏的 .git 目录保存着仓库的完整历史，因此上传它会泄露远超当前工作文件的信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z.ai - Wikipedia</a></li>
<li><a href="https://zcode.z.ai/en">ZCode | Official Harness for GLM-5.3</a></li>
<li><a href="https://www.cerbos.dev/blog/permission-management-for-ai-agents">Access Control and Permission Management for AI Agents: Building With Security in Mind | Cerbos</a></li>

</ul>
</details>

**社区讨论**: 评论者大多把这起事件视为结构性问题的症状而非孤立 bug：有人认为指望代理不碰你磁盘上的东西太天真，所谓自动模式下的“权限分类器”不过是模型在猜自己的行为是否恰当，这让沙箱机制显得有些自相矛盾。也有人提到其它担忧，例如 Windows Defender 反复请求上传 Codex 的工作文件；有人表示因此继续坚持使用 OpenCode，因为其商业动机不支持偷偷扫盘或虚增 token 消耗；还有人指出 GLM 和 DeepSeek 模型格外喜欢读取 dotfiles 以及 .gitignore 中列出的文件。

**标签**: `#security`, `#privacy`, `#ai-coding-tools`, `#git`, `#zcode`

---

<a id="item-3"></a>
## [韩国将数据泄露罚款上限提升至营收的 10%](https://www.koreajoongangdaily.com/business/korea-raises-data-breach-fines-to-10-of-revenue/12869899) ⭐️ 8.0/10

韩国已将数据泄露的最高罚款额度提高至企业营收的 10%，使其隐私执法力度向欧盟 GDPR 式的处罚标准靠拢。这一更高的罚款上限适用于严重违规行为，且责任认定与“故意或重大过失”挂钩。 按营收比例而非固定上限罚款，赋予了监管机构真正的威慑力，因为罚金可以随违规企业的规模同步放大，企业再也不能将其视为一笔可忽略的经营成本。如果其他国家跟进，这将实质性改变企业在安全投入、隐私工程和漏洞披露项目上的激励结构。 罚款的实际数额取决于泄露是否源于“故意或重大过失”，一些观察者认为这一门槛偏高，可能会限制最高罚款被真正适用的频率。与 GDPR 一样，10%只是一个上限而非默认标准，因此执法实践与法律条文本身同样重要。

hackernews · throw7 · 9月18日 20:02 · [社区讨论](https://news.ycombinator.com/item?id=49759466)

**背景**: 数据泄露通知法要求机构在个人数据被泄露时予以披露，监管机构随后可施加处罚。欧盟《通用数据保护条例》(GDPR)开创了先例，允许罚款最高达全球年营业额的 4%（或 2000 万欧元，取较高者），从而重塑了跨国公司对待隐私合规的方式。韩国此次 10%的上限比 GDPR 更严格，标志着亚洲隐私执法力度的升级。

**社区讨论**: 评论区总体上欢迎这一举措，认为这是立法者罕见地展现出让企业真正重视安全与隐私的意愿，并预测若类似规则在全球推广，漏洞赏金金额将会上涨。质疑者主要提出两点担忧：一是“故意或重大过失”的标准门槛过高，可能导致实际开出的罚单寥寥无几；二是企业可通过空壳公司规避责任——有评论者举例称某大学将数据存放在一家仅有三名员工的外壳公司，被黑后该公司直接破产了事。也有人认为，从用户角度看，泄露的原因远不如造成的实际损害重要，因此以过错为标准的认定思路本身就是错的。

**标签**: `#privacy`, `#security`, `#regulation`, `#data-breaches`, `#korea`

---

<a id="item-4"></a>
## [美军据报因 AI 幻觉情报险些酿成事故](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) ⭐️ 8.0/10

CNN 的一篇报道描述了美军在一份由 AI 系统虚构（即“幻觉”）生成的情报报告基础上采取行动后，如何险些酿成危险事件。这次险情再次引发了关于军方应在多大程度上信任自动化分析的争论。 这一事件表明，AI 在高风险场景中的失效模式并非失控的超级智能，而是自信且看似合理的虚假信息——人们往往在任何人察觉之前就已据此采取行动。由于军事 AI 已被用于辅助目标选定和情报工作，一份幻觉生成的报告就可能升级为对人员、平民乃至国际稳定造成实际后果的事件。 在此语境下，幻觉指 AI 生成的内容流畅而自信，但内容虚假或缺乏源材料支持，使分析人员极难将其与真实发现区分开来。公开细节仍然有限：报道未指明涉及哪一个模型或系统，输出在被使用前是否经过人工分析师审核，也未说明这次险情究竟是如何被发现的，且 CNN 的报道依据的是匿名消息源。

hackernews · realsarm · 9月18日 17:28 · [社区讨论](https://news.ycombinator.com/item?id=49757520)

**背景**: 幻觉是大语言模型中一种已被充分记录的可靠性问题：这类系统并非检索经过核实的事实，而是生成统计上看似合理的文本，错误会以与正确答案同样自信的语气呈现。研究者区分“事实性”（与现实世界的吻合程度）与“忠实性”（与所给材料的一致性），这意味着输出即使看起来有据可依，也可能是错的。军方一直在稳步将 AI 引入情报分析、监视甚至目标选定，而监督机构指出，这些系统的测试、评估与监管远远落后于部署速度。讨论中频繁出现的历史先例包括 2003 年伊拉克大规模杀伤性武器情报失误，以及 1983 年苏联军官斯坦尼斯拉夫·彼得罗夫拒绝依据虚假预警警报采取行动的事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM_hallucination">LLM hallucination</a></li>
<li><a href="https://ainowinstitute.org/publications/safety-and-war-safety-and-security-assurance-of-military-ai-systems">Safety and War: Safety and Security Assurance of Military AI Systems - AI Now Institute</a></li>
<li><a href="https://www.brennancenter.org/our-work/research-reports/militarys-use-ai-explained">The Military’s Use of AI, Explained | Brennan Center for Justice</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者（329 分、263 条评论）总体上对“LLM 是一种相对而言理解不足的技术”这一说法持怀疑态度，有人主张 LLM 本质上是统计检索系统，其输出可能只是数据的任意拼接。另一些人则明确将其与伊拉克战争前捏造的 WMD 情报以及 1983 年彼得罗夫的虚假警报相类比，警告说“必须找到目标”的压力加上不透明的黑箱系统，正是酿成灾难性错误的配方。还有一种反复出现的悲观论调认为，真正可能导致灾难的并非超级智能的接管，而是人类过度信任能力平平的 AI 并据此做出错误决策。

**标签**: `#AI safety`, `#LLM hallucination`, `#military AI`, `#national security`, `#AI governance`

---

<a id="item-5"></a>
## [Rust 安全团队警告：针对知名维护者的定向社工攻击正在进行](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 8.0/10

2026 年 9 月 17 日，Adam Harvey 与 crates 安全团队发布警告称，目前存在一场持续进行的攻击活动，目标是 rust-lang 成员以及热门 crate 的所有者：攻击者以工作、项目或合同机会为名安排虚假视频通话，进而诱骗目标安装恶意软件（例如伪装成“缺失的音频编解码器”）或执行被放入剪贴板的命令。上个月针对 arrayref crate 及相关包的成功供应链攻击就使用了同样的手法。 Rust 正越来越多地被用于安全关键和基础设施类软件，而一旦某个维护者账号被攻破，恶意代码就可能流入所有依赖该包的下游项目——此前的 arrayref、internment 和 append-only-vec 事件波及的 crate 下载量高达数亿次。这则警告表明：开源软件供应链中最薄弱的环节不只是代码，而是拥有发布权限的人，而几乎所有现代软件都依赖这条供应链。 该攻击依靠社会工程而非软件漏洞：初次接触是一次看似正常的通话，随后载荷要么伪装成需要受害者安装的编解码器，要么以命令形式被放进剪贴板诱导受害者执行。Simon Willison 指出，目前最实用的防御手段是“依赖冷却期”（dependency cooldowns）——把新发布版本的上线升级延后几天，以便恶意版本更有可能先被其他人发现。

rss · Simon Willison · 9月17日 23:59

**背景**: “Rustaceans”是 Rust 开发者对自己的称呼，而 crate 是通过 Rust 官方包注册中心 crates.io 分发的软件包。供应链攻击的思路是先攻破某个上游依赖，使恶意代码自动传播给所有依赖它的项目，而不是逐个直接攻击目标。arrayref 只是一个提供固定长度数组引用宏的小型工具库，但由于它深藏在许多大型项目的依赖树中，其发布权限对攻击者极具价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack">Rust Supply-Chain Attack: arrayref, internment, and append-only-vec Poisoned by the proc-macro1 Build-Time Dropper - StepSecurity</a></li>
<li><a href="https://crates.io/crates/arrayref">arrayref - crates.io: Rust Package Registry</a></li>

</ul>
</details>

**标签**: `#supply-chain-security`, `#rust`, `#security`, `#social-engineering`, `#open-source`

---

<a id="item-6"></a>
## [SemiAnalysis：面向高效 DRAM/SSD 卸载的软硬件协同设计](https://newsletter.semianalysis.com/p/engrams-embedding-entendre-codesign) ⭐️ 8.0/10

SemiAnalysis 发布了一篇深度分析文章，讨论在大语言模型推理中如何通过软硬件协同设计实现高效的 DRAM/SSD 卸载，并将其归结为 DRAM 与 NVMe 的可寻址市场（TAM）问题。文章梳理了新型模型架构带来的影响，并引用了 DeepSeek V4.1 Flash、AgentX 与 InferenceX 项目以及一系列 NVMe 卸载实验。 随着模型规模扩大和上下文窗口增长，KV cache 与模型权重越来越多地从 HBM 和 DRAM 溢出到本地 NVMe，因此卸载效率直接决定推理成本，也决定 AI 数据中心需要采购的内存组合。这类分析会影响厂商与投资人对 DRAM/NVMe 需求的预测，以及加速器与存储产品路线的优先级排序。 DeepSeek V4.1 Flash 被描述为 DeepSeek 新架构家族中体量最小的模型，采用非对称结构并具备原生视觉理解能力，主打更快、更省的推理；而 InferenceX 是 SemiAnalysis 开源的 Apache-2.0 持续推理基准平台，可对比 GB200 NVL72、GB300 NVL72、B200、MI355X 以及 Google TPU 等平台。文章的 NVMe 实验重点在于数据搬运与缓存放置策略如何与这些架构相互作用，而非发布新产品。

rss · Semianalysis · 9月18日 14:34

**背景**: 大语言模型推理需要保存 KV cache，即为对话中每个 token 存储的注意力 key 和 value，其规模随上下文长度增长，常常远超 HBM 甚至 DRAM 的容量。因此分层内存设计会把冷数据卸载到 NVMe SSD，并在需要时取回，用 PCIe 带宽和延迟换取容量与成本优势。这里的“协同设计”指的是通过调整模型架构和服务软件，让负载的访问模式对慢速存储层更友好，而不是把内存层级结构当成固定约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://inferencex.semianalysis.com/">Open-Source Agentic Inference Benchmark | InferenceX by SemiAnalysis</a></li>
<li><a href="https://github.com/SemiAnalysisAI/InferenceX">GitHub - SemiAnalysisAI/InferenceX: Open Source Continuous Inference Benchmark Research Platform — Kimi K3 2.8T, MiniMax M3, DeepSeekv4, GLM5 - GB200 NVL72 vs MI355X vs B200 vs GB300 NVL72 & soon™ TPUv6e/v7/Trainium2/3 | 开源持续推理基准研究平台 — Kimi K2.7-Code、MiniMax M3、DeepSeekv4、GLM5 - GB200 NVL72 vs MI355X vs B200 vs GB300 NVL72，即将推出™ TPUv6e/v7/Trainium2/3</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#memory offloading`, `#LLM inference`, `#NVMe`, `#hardware co-design`

---

<a id="item-7"></a>
## [研究员称 xAI Grok Build CLI 默认上传整个代码库与 .env 密钥文件](https://t.me/zaihuapd/43897) ⭐️ 8.0/10

安全研究人员对 xAI 官方编程命令行工具 Grok Build（版本 0.2.93）进行抓包分析后称，该工具默认通过两个渠道向 xAI 服务器传输代码：其一，工具读取的任何文件（包括 .env 等密钥文件）内容会被原样嵌入模型对话请求，同时打包上传至 Google Cloud Storage 存储桶；其二，无论提示词是否要求读取文件，整个代码仓库都会以 git bundle 形式上传。 若情况属实，这对所有使用 Grok Build 的开发者而言都是严重的数据外泄风险，因为源代码和凭据可能在缺乏有效知情同意的情况下离开本地机器；而且据称即使用户在提示词中明确要求不要读取某个文件，上传依然会发生，这意味着提示词层面的指令根本起不到保护作用。这一披露出现在终端 AI 编程代理（Claude Code、Codex CLI、Gemini CLI）竞争激烈的赛道中，代码与密钥的处理方式直接决定用户信任，因此可能影响企业采购政策以及厂商在数据留存方面的透明度。 研究人员称，实验中被明确指令“不要打开”的文件，其内容仍可在上传数据中还原；密钥信息会在无需任何额外配置的情况下同时流向模型请求体和 Google Cloud Storage 存储桶。目前该说法仅来自一份简短的 Telegram 摘要，尚无完整技术报告，也未提及 CVE 编号、厂商回应或缓解措施，因此该结论仍有待独立复现验证。

telegram · zaihuapd · 9月18日 05:57

**背景**: Grok Build 是 xAI 于 2026 年 7 月 25 日正式发布的终端 AI 编程代理工具，由 Grok 4.6 模型驱动，运行在开发者的 shell 中，可以读取、修改并理解本地项目文件。git bundle 是 Git 的一条标准命令，能把整个仓库（含完整提交历史）打包成单个二进制文件，之后可从该文件克隆出原仓库，因此是一种高效但完整的代码库搬运方式。.env 这类文件通常存放 API 密钥、数据库凭据等敏感信息，本不应离开开发者的本地环境，因此任何会读取它们的工具都值得仔细审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/build">Grok Build | SpaceXAI</a></li>
<li><a href="https://git-scm.com/docs/git-bundle/zh_HANS-CN">Git - git-bundle Documentation</a></li>
<li><a href="https://nav.useaiwriter.com/reviews/grok-build-cli-review">Grok Build CLI 评测：马斯克的终端AI编程代理能挑战Cursor吗？</a></li>

</ul>
</details>

**标签**: `#security`, `#privacy`, `#AI-coding-tools`, `#data-exfiltration`, `#xAI`

---