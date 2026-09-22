---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 39 条内容中筛选出 10 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Sol 与 Luna 前沿模型](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5.5，token 价格下调](#item-2) ⭐️ 9.0/10
3. [五角大楼：过度依赖人工智能导致伊朗学校遭袭](#item-3) ⭐️ 9.0/10
4. [vLLM v0.30.0 发布：762 次提交，引入 Fast Start GPU 权重缓存](#item-4) ⭐️ 8.0/10
5. [黑客声称通过 Oracle PeopleSoft 零日漏洞窃取 FBI 全体员工数据](#item-5) ⭐️ 8.0/10
6. [Claude Opus 5.5 在最高推理档位下的基准测试分析](#item-6) ⭐️ 8.0/10
7. [TypeSafe AI 发布 Jev：输出类型化概率决策的新型「决策模型」](#item-7) ⭐️ 8.0/10
8. [小米发布 MiMo-V2.6 全模态模型，公开披露 350 万美元强化学习训练成本](#item-8) ⭐️ 8.0/10
9. [25 位菲尔兹奖得主警告 AI 或与数学研究目标严重错位](#item-9) ⭐️ 8.0/10
10. [DeepSeek 与清华发布 DSec 沙箱平台技术报告](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna 前沿模型](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 发布了 GPT-6 Sol 和 Luna 两款新前沿模型，在能力与成本之间提供了不同的平衡，其中 Luna 的价格仅为上一代 GPT-5.6 Luna 的一半。此次发布距离 GPT-5.6 推出还不到三个月，并延续了 GPT-6 Astra 的技术进展，同时在多项关键基准上宣称有大幅准确率提升和显著的成本下降。 作为 OpenAI 的重磅前沿模型发布，此举将重塑构建 AI 智能体的开发者的竞争格局，因为定价与容量直接决定了智能体的经济性。大幅降价（尤其是 Luna 仅为前代一半的成本）可能让大规模智能体工作负载变得实惠得多，并促使 Anthropic 的 Claude Code 等竞争对手在成本和用量限制两方面作出回应。 这两款模型已在 API、Codex 和 ChatGPT 中上线，OpenAI 将其定位为把 GPT-6 Astra 的诸多优势带入更快、更实惠的形态。此次发布在多项关键基准上与 Anthropic 的 Claude 进行了对比，这一不寻常的举动表明智能体工具市场的性价比竞争已十分激烈。

hackernews · OfficialTurkey · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: OpenAI 是领先的 AI 实验室，会定期发布前沿大语言模型，每一代通常都会提升推理、编程和智能体能力，同时改变性价比曲线。GPT-6 Astra 是此前的高端模型，而 GPT-6 Sol 和 Luna 被定位为将其大部分能力带入更便宜、更快速档位的派生版本，其中“Luna”似为低成本档，“Sol”为更高能力档。这些模型对运行自主智能体的开发者尤为重要，因为 token 成本和速率限制会迅速累积并直接决定方案的可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://www.zdnet.com/innovation/openai-gpt-6-sol-luna-release/">OpenAI’s GPT-6 Sol doubles its accuracy rate – for half the cost</a></li>
<li><a href="https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna-in-the-api-codex-and-chatgpt/1399925">Announcing GPT-6 Sol and GPT-6 Luna in the API, Codex and ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论聚焦于成本与使用体验：Simon Willison 强调 GPT-6 Luna 价格仅为 GPT-5.6 Luna 的一半是件大事；jeffnash 则从用量限制角度比较了 Codex Pro 20x 与 Claude Code 20x，认为目前 Codex 更胜一筹。m_fayer 等人表达了对前代模型“性格”和工程直觉的依恋，leokennis 则称赞 ChatGPT Plus 对普通用户而言几乎无限且稳定可靠。

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#model-release`, `#pricing`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5，token 价格下调](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了新一代前沿模型 Claude Opus 5.5，官方称其沟通表达比 Opus 5 更自然、行文更清晰易懂，产出内容“更容易跟进和检查”。同时该版本全面下调了每百万 token 的价格：缓存读取从 0.50 美元降至 0.20 美元，输入 token 从 5 美元降至 4 美元，输出 token 从 25 美元降至 20 美元，缓存写入从 6.25 美元降至 5 美元。 这是 Anthropic 在公开呼吁“为前沿发展设定节奏（pacing the frontier）”之后的首个模型发布，许多评论者立刻指出了这一表态与发布行为之间的张力；而全面降价则直接影响了开发者的成本结构——Opus 5 据称是 OpenRouter 上支出最高的模型。前沿模型 token 变便宜会降低开发者的使用成本，并对包括 DeepSeek 等低价替代方案在内的竞争对手形成压力。 据路透社报道，Anthropic 称 Opus 5.5 的性能可与其顶级的 Fable 5.1 相媲美，而运行成本比上一代降低 40%。其定价按每百万 token 计算，输入、输出、缓存读取与缓存写入分别计价；Anthropic 的文档也建议现有 Opus 5 用户考虑迁移到 5.5 以获得更好的性能。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: 前沿模型（frontier model）指最先进的通用型 AI 模型，具备推理、多模态生成和智能体（agentic）工作流能力，通常依赖海量数据和巨大算力训练而成。这类模型一般按 token 计费——一个 token 大约是四个字符的文本——输入（提示词）和输出（模型回复）分别按每百万 token 定价，缓存上下文则享受折扣价。Claude Opus 是 Anthropic 的旗舰模型系列，而 OpenRouter 是一个将请求路由到众多模型的第三方平台，并公布各模型的支出排行，评论者正是借此判断真实使用情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/anthropic-unveils-claude-opus-55-2026-09-22/">Anthropic unveils Claude Opus 5.5 - Reuters</a></li>
<li><a href="https://platform.claude.com/docs/en/models/opus-5-5/overview">Claude Opus 5.5 - Claude Platform Docs</a></li>
<li><a href="https://www.solvimon.com/glossary/ai-token-pricing">What is AI Token Pricing ? | Solvimon Glossary</a></li>

</ul>
</details>

**社区讨论**: 评论区集中讨论 Anthropic 近期“为前沿设定节奏”的呼吁与此次发布之间的反差，有用户称这条发布“用非常具体的数字证明他们根本没有在放慢节奏”。降价总体受到欢迎，用户逐项对比了新旧价格表；也有人表示会继续使用 DeepSeek v4.1 等更便宜的替代方案。开发者 Simon Willison 则照例贴出了在 low、medium、high、xhigh 各思考档位下的“鹈鹕测试”结果。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Model Release`

---

<a id="item-3"></a>
## [五角大楼：过度依赖人工智能导致伊朗学校遭袭](https://www.bloomberg.com/graphics/2026-iran-school-attack/) ⭐️ 9.0/10

五角大楼一份报告认定，美国"未能尽到一切可行努力去核实"伊朗米纳布的一所学校属于军事目标，且这一失职"超出了单纯的疏忽"。报告将过度依赖 AI 辅助目标筛选系统 Maven 列为此次造成平民伤亡的导弹袭击的促成因素之一。 这是首批由官方政府报告直接将 AI 辅助目标筛选与平民伤亡联系起来的案例之一，可能成为军事 AI 政策、Palantir 的 Maven 等系统采购以及算法战争问责国际辩论的转折点。它也加大了压力，要求明确当算法参与导致非战斗人员死亡时，究竟由谁承担法律责任。 据报道，米纳布这一地点因数据过时而被标注为伊斯兰革命卫队设施，随后与其他候选目标一起被输入 Maven，并最终作为推荐结果输出；官员称部分使用者原本以为 Maven 会标记出情报中的过时记录或矛盾之处，但目前并不清楚他们为何会这样认为。事件还引发了相互推责，五角大楼实际上将责任归于软件，而 Palantir 则把结果归咎于输入数据质量差。

hackernews · devonnull · 9月22日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49806430)

**背景**: Maven（最初名为 Project Maven）是美国国防部的一项计划，如今与 Palantir 的软件紧密相关，其核心是用机器学习分析侦察图像与情报，为人类操作员标出潜在目标。这类系统通常以"人在回路中"（human in the loop）作为保障，即由人类复核机器的每一项推荐，但批评者认为这一机制往往退化为形式上的盖章批准。相关讨论的核心概念是"自动化偏差"（automation bias），即人类倾向于采信自动化系统的建议、忽视与之矛盾的证据，此外还涉及联合国一直在讨论是否应予禁止的致命性自主武器系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.defensenews.com/opinion/2026/03/26/the-militarys-fabled-human-in-the-loop-for-ai-is-dangerously-misleading/">The military’s fabled ‘human in the loop’ for AI is dangerously misleading</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automation_bias">Automation bias</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lethal_autonomous_weapons_systems">Lethal autonomous weapons systems</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者大多不接受"AI 本身是元凶"的说法，认为根本原因在于人类决定把大量致命决策权交给机器，而算法无法受审，因此每一次行动都必须有可负责的人类。也有人指出五角大楼与 Palantir 之间存在问责真空，批评那些并不理解 AI 局限却全盘拥抱它的官员，并强调该系统本就并非为发现过时或矛盾数据而设计。

**标签**: `#AI ethics`, `#military AI`, `#accountability`, `#AI safety`, `#civilian casualties`

---

<a id="item-4"></a>
## [vLLM v0.30.0 发布：762 次提交，引入 Fast Start GPU 权重缓存](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 发布 v0.30.0，这是一个包含 762 次提交、来自 315 位贡献者（其中 104 位是新贡献者）的重要版本更新。该版本新增支持大量前沿模型，包括 DeepSeek-V4.1-Flash、DeepSeek-V4-Flash-Vision-Exp、GLM-5.3-Flash、K2-Horizon、Cohere Compass、Bailing V3 VL 和 Nanbeige4.2，同时引入常驻式每 GPU 权重缓存守护进程 "Fast Start"、Gumbel-max 水印、HiSparse 主机端 KV 分层，以及扩展的量化与 CPU 后端内核。 vLLM 是应用最广泛的开源大模型推理与服务引擎之一，因此这次发布直接影响所有在生产环境中部署模型的人。Fast Start 权重缓存与新增模型支持降低了冷启动延迟，缩短了模型发布到在高吞吐服务栈中可用之间的时间差，而 CPU 后端与量化方面的工作则拓宽了 vLLM 能以较低成本运行的硬件范围。 Fast Start 将量化后、按张量并行切分的权重常驻在 GPU 显存中，使引擎重启时可通过 `--load-format ipc_cache` 经 CUDA IPC 直接映射，而无需从磁盘重新加载，目前还覆盖了 FP4 检查点和多节点张量并行。其他值得注意的细节包括：在 SM100 上通过 FlashMLA V4.1 记录为 DeepSeek-V4.1-Flash 提供 MXFP8 的 KV 存储、为 DeepSeek-V4 提供 AVX512/AMX 稀疏 MLA 的 CPU 后端、Model Runner V2 的改动使 CUDA graph 捕获从 12 秒降到 2 秒、H200 上引擎初始化从 28.9 秒降到 8.2 秒，以及通过 `--return-sampling-mask` 修复了约 2 倍的 RL 单步耗时回退。

github · khluu · 9月22日 05:20

**背景**: vLLM 是一个面向大语言模型的高吞吐服务引擎，其核心创新 PagedAttention 将 KV 缓存（即让模型在 token 之间复用上下文的键/值张量缓存）按页式块管理，而非使用一整块连续缓冲区，从而实现大量并发请求的高效批处理。FlashMLA 是 DeepSeek 的优化 Multi-head Latent Attention（MLA，多头潜在注意力）内核库，MLA 是 DeepSeek 模型用来压缩 KV 缓存体积的注意力变体。Engram 是 DeepSeek 的一种条件记忆技术，通过对大型嵌入表进行确定性哈希查找，使系统能够在 GPU 计算其他层时从主机 DRAM 预取记忆条目。MXFP8 是一种带共享块缩放的低精度 8 位浮点格式，后训练量化研究显示它在许多模型和任务上接近无损。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/FlashMLA: FlashMLA: Efficient Multi-head Latent Attention Kernels · GitHub</a></li>
<li><a href="https://generativeai.pub/deepseeks-engram-the-lookup-table-that-eats-transformer-layers-90b5f6a99a90">DeepSeek’s Engram : The Lookup Table That Eats... | Generative AI</a></li>
<li><a href="https://www.alphaxiv.org/abs/2601.09555">Benchmarking Post-Training Quantization of Large... | alphaXiv</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#model-serving`, `#deepseek`, `#release`

---

<a id="item-5"></a>
## [黑客声称通过 Oracle PeopleSoft 零日漏洞窃取 FBI 全体员工数据](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 8.0/10

据 404 Media 报道，一群自称“我们黑进了 FBI”的黑客声称已窃取覆盖 FBI 全体雇员的数据。攻击者据称是通过一个 Oracle PeopleSoft 零日漏洞获得访问权限的，这引发了关于泄露数据和底层漏洞的广泛讨论。 如果得到证实，涉及整个联邦机构雇员名册的数据泄露将是一起重大的国家安全事件，使相关人员面临被锁定、身份盗用和社工攻击的风险。由于 PeopleSoft 在政府和企业中被广泛部署，其中存在的零日漏洞可能意味着许多运行同一软件的其他机构同样面临风险。 该事件被归因于一个 Oracle PeopleSoft 零日漏洞，即厂商在漏洞被利用之前没有任何时间准备补丁的先前未知缺陷。网络安全社区中流传的报道将此类缺陷描述为 PeopleSoft 中一个可远程利用的严重漏洞，不过 FBI 数据泄露这一说法本身尚未得到独立方的证实。

hackernews · spenvo · 9月22日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=49805278)

**背景**: Oracle PeopleSoft 是一套企业软件套件，最初由 PeopleSoft 公司开发、后被 Oracle 收购，用于为大型组织和政府机构集中管理人力资源、薪资、财务和学生记录。零日漏洞是指此前从未被知晓或报告的缺陷，使开发者没有时间在攻击者利用之前打补丁。此事件被拿来与 2015 年美国人事管理局（OPM）数据泄露事件相提并论，当时约有 2210 万条美国政府雇员记录被泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mindmajix.com/what-is-peoplesoft">What is PeopleSoft | PeopleSoft Tutorial</a></li>
<li><a href="https://www.kaspersky.com/resource-center/definitions/zero-day-exploit">Zero - Day Exploits & Zero - Day Attacks</a></li>
<li><a href="https://medium.com/@Inforsecpro/oracle-peoplesoft-zero-day-rce-vulnerability-exposes-enterprise-systems-to-remote-compromise-a2baf6986401">Oracle PeopleSoft Zero Day RCE Vulnerability Exposes... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对数据库安全感到悲观，有人指出似乎没有任何组织能保护好大型数据集，并以 OPM 泄露事件作为先例。其他人强调，牵涉 Oracle PeopleSoft 零日漏洞很可能意味着还有更多存在漏洞的系统，也有若干人称赞 404 Media 报道领先于主流媒体，并批评相关机构重削减成本而轻视安全专业能力。

**标签**: `#cybersecurity`, `#data-breach`, `#fbi`, `#zero-day`, `#oracle-peoplesoft`

---

<a id="item-6"></a>
## [Claude Opus 5.5 在最高推理档位下的基准测试分析](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10

Artificial Analysis 发布了 Claude Opus 5.5 在“max”（最高）推理档位下的智能水平、性能与价格分析，并为其配套提供了“xhigh”和“medium”（默认）档位的独立页面。该分析在 Hacker News 上获得了 202 分和 55 条评论，讨论主要围绕推理预算、单任务成本和模型可靠性展开。 对实际使用模型的团队而言，推理预算档位和单任务成本正变得比单纯的基准分数更具决定性。有评论指出，在相同努力档位下，Opus 5.5 的单任务成本相比 Opus 5 降低了约一半，这可能比智能分数的提升更快地把真实生产负载推向新模型。 “max”档位可能在给出答案之前就耗尽全部 128,000 token 的推理预算——一位评论者称，在一个简单的 SVG 生成任务上连续两次因此失败。多位评论者认为“high”档位才是实用上的最佳平衡点，因为许多基准分数在超过该档位后开始进入平台期，而成本仍在持续上升。

hackernews · theanonymousone · 9月22日 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

**背景**: Artificial Analysis 进行与模型无关的评测，并发布一个聚合的智能指数（Intelligence Index），综合推理、知识、数学和编程数据集，使不同模型能在统一标准下比较。推理模型可以在推理阶段通过生成较长的思维链来投入更多算力，厂商则将其暴露为可调的档位，例如 medium、high、xhigh 和 max。由于更高的档位意味着每次请求生成更多 token，延迟与成本都会随之上升，因此推理预算、质量与单任务价格之间的权衡，已成为模型选型的核心话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/methodology/intelligence-benchmarking">Artificial Analysis Intelligence Benchmarking Methodology</a></li>
<li><a href="https://arxiv.org/html/2507.02076v1">Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs</a></li>
<li><a href="https://orq.ai/blog/model-vs-data-drift">Understanding Model Drift and Data Drift in LLMs (2026 Guide)</a></li>

</ul>
</details>

**社区讨论**: 评论整体持积极态度，但在细节上颇为怀疑：simonw 记录了一个具体失败案例，即 max 档位在推理过程中耗尽了 128k token 预算；breckenedge 则担心厂商发布时的基准成绩在数周后重跑时未必站得住脚，并警告存在用户迁移后厂商“撤梯子”的风险。积极方面，hglaser 强调单任务成本相比 Opus 5 降低了约一半，mchusma 推荐“high”档位是基准表现与成本之间的最佳平衡，而 linuxrebe1 表示自己已退回到 Opus 4.8，因为 Opus 5 在遵循指令和保持任务连贯性上不够稳定。

**标签**: `#LLM`, `#AI benchmarks`, `#Claude`, `#model pricing`, `#reasoning models`

---

<a id="item-7"></a>
## [TypeSafe AI 发布 Jev：输出类型化概率决策的新型「决策模型」](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI 发布了 Jev，这是其所谓「System One 模型」（也有人更愿意称之为「决策模型」）的第一个实例：它接受文本或半结构化的「state」输入，但返回的不是文本，而是浮点数。针对每个问题，它可以返回 yes/no（「Noul」）命题的 0 到 1 置信度、一组候选项上的概率分布，或是在给定区间内的一个数值评分。 它把 LLM 的输出重新定义为类型化的概率决策而非自由文本，使得垃圾信息检测、标签推荐、优先级排序和搜索重排序这类分类任务变得更便宜、更易搭建。Jev 的输入价格仅为每百万 token 0.042 美元且输出免费，甚至低于 OpenAI 的 GPT-5 Nano（每百万 0.05 美元），这可能推动行业在通用聊天模型之外发展专门的决策模型。 该 API 接受一份文档以及尽可能多地塞进上下文窗口的问题，问题会被并行评估，因此问很多问题与只问一个问题的耗时大致相当。TypeSafe 针对 Jev 1.13 的「jaggedness」文档指出，该模型目前在数字、日期和对抗性内容上表现不佳；Simon Willison 还指出一个更深层的隐忧：Jev 完全不提供文字解释，只给出一个浮点数。

rss · Simon Willison · 9月21日 23:09

**背景**: 「System One」这个名字源自 Daniel Kahneman 在《思考，快与慢》中提出的区分：System 1 是快速、自动、直觉式的思维，System 2 则是缓慢、费力的推理。「Noul」这类问题取自 Bernoulli（伯努利）的缩写，意味着模型返回的是伯努利分布的概率参数——即一个介于 0 和 1 之间、表示某命题为真的可能性的数值。传统 LLM 按输入和输出 token 分别计费且输出价格更高，而 Jev 只对输入收费，因为它的输出只是几个数字而非生成的文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow">Thinking , Fast and Slow - Wikipedia</a></li>
<li><a href="https://thedecisionlab.com/reference-guide/philosophy/system-1-and-system-2-thinking">System 1 and System 2 Thinking - The Decision Lab</a></li>

</ul>
</details>

**标签**: `#LLM`, `#decision models`, `#AI models`, `#probabilistic reasoning`, `#TypeSafe AI`

---

<a id="item-8"></a>
## [小米发布 MiMo-V2.6 全模态模型，公开披露 350 万美元强化学习训练成本](https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/) ⭐️ 8.0/10

小米正式发布并开源了 MiMo-V2.6 系列，包含 MiMo-V2.6-Pro 和 MiMo-V2.6-Flash 两个原生全模态模型，并公开披露其强化学习训练总成本仅为 350 万美元。此次发布还附带一个实时“benchmaxxing”看板，直接展示训练器日志中的强化学习训练指标。 一家消费硬件公司以公开披露的 350 万美元强化学习成本推出前沿级多模态模型，说明前沿多模态后训练的成本正在大幅下降，这可能降低非传统大厂团队参与前沿竞争的门槛。开源模型权重并配套实时训练看板，也在推动更透明的模型能力声明与验证规范。 MiMo-V2.6-Pro 被称为小米迄今最强的模型，而 MiMo-V2.6-Flash 主打智能、效率与成本之间的最佳平衡，强化学习训练日志发布在 mimo.xiaomi.com/rl/ 上。官方措辞直接借用了“benchmaxxing”（即为刷排行榜而优化）这一说法，因此 350 万美元这一数字应理解为仅覆盖强化学习阶段而非完整预训练流程，且该看板属于官方自报数据，并非第三方独立审计。

reddit · r/MachineLearning · /u/we_are_mammals · 9月22日 07:56

**背景**: MiMo 是小米自研的大语言模型系列，“全模态”（omnimodal）指单一模型原生处理文本、图像与音频，而非在文本模型上外挂多个独立编码器。基于可验证任务的强化学习后训练，是目前各大实验室提升推理与智能体能力的主要手段，但通常成本高昂且极少公开。小米称此次发布是迈向 RSI（递归自我改进）的一步，并采取“公开构建”的方式，即随着进展同步开放权重、训练指标与成本信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo-V2.6 | Xiaomi</a></li>
<li><a href="https://mimo.mi.com/docs/en-US/news/latest/v2-6">Xiaomi MiMo-V2.6 Series: 3 New Models Officially Released</a></li>
<li><a href="https://mimo.xiaomi.com/rl/">mimo-v2.6 RL - mimo.xiaomi.com</a></li>
<li><a href="https://ctaio.dev/en/labs/benchmaxxing/">What Is Benchmaxxing? The AI Benchmark Gaming Problem ...</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#LLM`, `#Multimodal`, `#Model Release`, `#Reinforcement Learning`

---

<a id="item-9"></a>
## [25 位菲尔兹奖得主警告 AI 或与数学研究目标严重错位](https://t.me/zaihuapd/43973) ⭐️ 8.0/10

包括陶哲轩在内的 25 位菲尔兹奖得主发表联合声明，警告将 AI 快速用于解决数学问题可能导致 AI 发展目标与数学研究目标出现“严重错位”。声明认为，尽管大型语言模型近年来解决重大数学问题的能力大幅提升，但把数学解题当作衡量 AI 能力的基准，可能损害数学研究与整体学术生态。 这份声明出自数学界最具权威性的一批学者，因此很可能影响 AI 实验室、资助机构和期刊如何定义与评估 AI 系统的“数学能力”。它也表明，学界日益担忧 AI 生成的内容可能扭曲科研激励、基准测试优先级和学术贡献认定机制，其影响远不止于数学领域。 声明强调，数学研究的核心在于形成概念性理解和新的洞见，而不是单纯得到答案；并警告 AI 批量生成成果可能压缩用于验证、交流与引用前人工作的时间，同时引发署名和抄袭等问题。声明也承认 AI 有望提升研究效率，最终影响取决于人们如何使用这项技术。

telegram · zaihuapd · 9月22日 03:00

**背景**: 菲尔兹奖被普遍视为数学领域的最高荣誉，每四年颁发一次，通常授予不超过四位、年龄一般在 40 岁以下的数学家；签署人之一的陶哲轩于 2006 年获奖。近年来，大型语言模型在数学基准测试和竞赛类题目上进步迅速，引发了对这些成绩是否真正代表数学推理能力的讨论。这份声明是学术界围绕科研伦理、署名规范以及 AI 在学术出版中应用的更广泛讨论的一部分。

**标签**: `#AI`, `#Mathematics`, `#Research Ethics`, `#Large Language Models`, `#Academic Publishing`

---

<a id="item-10"></a>
## [DeepSeek 与清华发布 DSec 沙箱平台技术报告](https://arxiv.org/abs/2609.22978) ⭐️ 8.0/10

DeepSeek-AI 与清华大学联合发布技术报告《DeepSeek Elastic Compute（DSec）》，公开了支撑大规模智能体训练与评测的沙箱基础设施：每天服务约 300 万个沙箱实例，峰值并发超过 38 万，创建速度超过每秒 5000 个。单个生产单元约 160 个节点，单节点可高密度承载 3200 个容器或 800 个 microVM，并通过统一 SDK 提供 FnCall、容器、Firecracker microVM 和完整 VM 四种后端。 沙箱的创建速度与部署密度，是当前基于强化学习的智能体训练常见的瓶颈，因此公开真实生产指标与架构选型，为整个 AI 系统社区提供了可参考的规模化智能体环境设计范式。这也说明智能体训练如今已高度依赖系统层基础设施，而不仅仅是模型或算法层面的工作。 DSec 基于 3FS 分布式文件系统按需加载 EROFS 镜像，相比传统 Docker 全量拉取，任务完成时间快 1.7 倍、磁盘写入减少 57%，并通过内存共享与回收机制使峰值内存占用下降约 40%。在架构上，它把有状态的 rollout 执行与可抢占的 GPU 训练解耦，使强化学习框架能够与沙箱层深度协同。

telegram · zaihuapd · 9月22日 04:45

**背景**: 智能体训练通常需要在隔离环境中执行代码运行、软件工程任务、电脑操作等不可信且带状态的工作负载，这正是沙箱平台所提供的功能。DSec 建立在 Firecracker 之上——这是 AWS 开源、基于 KVM 的轻量级虚拟化技术，能提供启动快、内存开销低的 microVM 隔离；同时结合 EROFS 这一为高性能只读镜像设计的轻量级 Linux 文件系统，以及 DeepSeek 自研、面向 AI 负载的 3FS 分布式文件系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://firecracker-microvm.github.io/">Firecracker</a></li>
<li><a href="https://en.wikipedia.org/wiki/EROFS">EROFS - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/nidhinkumar06_opensourceweek-3fs-distributedfilesystem-activity-7301297675969118212-UaxW">Introducing 3 FS : A High-Performance File System for AI | LinkedIn</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Agent Training`, `#Sandbox Infrastructure`, `#Firecracker`, `#AI Systems`

---