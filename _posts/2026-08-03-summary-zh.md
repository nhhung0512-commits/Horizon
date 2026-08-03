---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 37 条内容中筛选出 13 条重要资讯。

---

1. [OpenAI 强调 AI 在数学研究中的日益重要作用](#item-1) ⭐️ 9.0/10
2. [开发工具必须是开源的](#item-2) ⭐️ 8.0/10
3. [MiniMax H3 获 ComfyUI 首日支持：开放权重、原生音频与 2K 视频](#item-3) ⭐️ 8.0/10
4. [Andy Pavlo 加入 ClickHouse，创立 ClickHouse Labs](#item-4) ⭐️ 8.0/10
5. [别当“肉代理”：批判盲目转发 AI 回复的做法](#item-5) ⭐️ 8.0/10
6. [Rust 项目目标：提出不可移动类型与受保证析构函数](#item-6) ⭐️ 8.0/10
7. [Qwen3.8-Max：代码生成与 AI 协作的新标杆](#item-7) ⭐️ 8.0/10
8. [Kimi K3 架构深度解析：压缩记忆与跨深度注意力](#item-8) ⭐️ 8.0/10
9. [机器学习审稿人：无复现代码的论文应直接拒稿](#item-9) ⭐️ 8.0/10
10. [美国 DNA 分析设备漏洞致 30 年法医证据面临篡改风险](#item-10) ⭐️ 8.0/10
11. [美媒调查：至少 50 名美国警员滥用摄像头窥探前任](#item-11) ⭐️ 8.0/10
12. [英伟达 170HX 矿卡被破解：解锁 80GB 显存，二手价暴涨](#item-12) ⭐️ 8.0/10
13. [英国再次要求苹果为云备份开后门，限制为仅英国用户数据](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 强调 AI 在数学研究中的日益重要作用](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 9.0/10

OpenAI 发布了一篇题为《数学与理论计算机科学的十项进展》的博客文章，展示了人工智能模型促成重大突破的十项最新成果，包括高维球填充和多色拉姆齐数。 这表明 AI 正成为数学领域真正的科研伙伴，而不仅仅是计算工具，这可能会重塑数学发现的方式，并加速理论领域的发展。 该列表似乎重点介绍了高维球填充和多色拉姆齐数等问题，其中一些结果被描述为出人意料地直观。更广泛的背景是 OpenAI 努力将 AI 定位为严谨研究的积极贡献者。

hackernews · milkshakes · 8月3日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49157930)

**背景**: 这篇文章反映了一个日益增长的趋势：大型语言模型和其他 AI 系统被用来生成猜想、验证证明以及解决对人类来说难以处理的组合问题。OpenAI 一直致力于将 AI 与形式化数学工具相结合。这篇博客总结了最近的成就，旨在回应关于 AI 与纯数学相关性的质疑。

**社区讨论**: 评论者观点不一：有人对 AI 成果的指数级速度印象深刻，认为否认已无意义；也有人担心文章语言可能为了营销而夸大。少数评论者甚至为具体问题提供了直观解释的链接，显示出既热情又审慎的态度。

**标签**: `#AI`, `#mathematics`, `#theoretical-computer-science`, `#OpenAI`, `#research`

---

<a id="item-2"></a>
## [开发工具必须是开源的](https://blog.exe.dev/devtools-must-be-open-source) ⭐️ 8.0/10

一篇题为《开发工具必须是开源的》的博文认为开发工具应该开源，并提出 LLM 使得修改它们更加可行。该文章在 Hacker News 上引发了 146 条评论的讨论，涉及可配置性、AI 生成的修改以及维护分支的现实情况。 这一点很重要，因为开发工具是程序员的日常工作核心，这场辩论直接影响到个人和公司如何投资、定制和贡献他们的工具链。LLM 的视角增加了新的维度：AI 可能降低修改源代码的门槛，使开源更具可行性，并重塑一线开发工作流。 该博文似乎反对配置文件、选项和插件系统，而是建议当用户想要更改（如编辑器的字体大小）时，应让 LLM 下载代码、修改硬编码值并重新构建。讨论中的批评者指出这种方法效率低下且浪费资源，并质疑在每晚定时任务中基于上游更新变基 AI 生成的本地更改是否可行。

hackernews · bryanmikaelian · 8月3日 14:15 · [社区讨论](https://news.ycombinator.com/item?id=49156111)

**背景**: 大型语言模型（LLM）是一种人工智能模型，通常是深度神经网络，在大量文本上训练，能够理解和生成类似人类的语言。传统上，开源的核心论据是检查和修改代码的自由，但实践中大多数开发者无法为定期使用的工具抽出时间去阅读和修改其源码。LLM 可能通过自动化代码理解和修改来改变这一点，使长期以来的开源梦想更易实现。然而，讨论中也揭示了关于能耗、AI 可靠性和不断变基自定义更改所带来的维护负担等实际问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What are large language models (LLMs)? - IBM</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论既展现了热情，也表现出怀疑。Simon Willison 认为 LLM 使最初的开源梦想对大多数人来说更加可行，而 kelnos 和 theamk 等人则强烈反对用 AI 重建工作流取代配置系统，称其低效、浪费且不可靠。一个可轻松 fork 的开发工具维护者表示，他们能理解这种想法的吸引力，但很可惜对其实用性持怀疑态度。

**标签**: `#open-source`, `#devtools`, `#LLM`, `#software-engineering`

---

<a id="item-3"></a>
## [MiniMax H3 获 ComfyUI 首日支持：开放权重、原生音频与 2K 视频](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 8.0/10

MiniMax H3 是一款开放权重的全模态模型，现已在 ComfyUI 中获得首日支持，可本地生成最高 2K 分辨率、带原生立体声音频的视频。官方称通过剪枝和动态显存卸载，内存占用降低了 66%。 这很重要，因为它在本地 GPU 上实现了带原生音频的最先进视频生成，降低了对独立创作者和开发者的门槛。ComfyUI 的首日支持让用户能更轻松地将其融入自定义工作流和现有的 AI 艺术流程。 该模型的调制权重（约占总参数的 40%）可被剪枝为查找表，且不损失质量，总面积内存从全精度的 123.6 GB 降至最小变体的 42.5 GB。结合动态显存卸载，可在 RTX 3060 等 GPU 上运行 2K 视频生成，但生成时间仍较长（例如在 16 GB RTX 4070 Ti Super 上生成 10 秒 480p 片段约需 10 分钟）。

hackernews · vblanco · 8月3日 13:34 · [社区讨论](https://news.ycombinator.com/item?id=49155629)

**背景**: MiniMax H3 是一个通用全模态生成模型，可联合理解文本、图像、视频和音频，并以最高 2K 分辨率、时长 15 秒生成带原生立体声音频的视频。ComfyUI 是一个开源、基于节点的界面，用于构建扩散模型的模块化工作流，广泛用于 AI 图像和视频生成。开放权重模型允许用户访问训练得到的参数，实现本地部署、微调和透明度，这与仅提供 API 的封闭模型形成鲜明对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open - Weights Model ? | AI 21</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者对其输出质量印象深刻，有人称在 4070 Ti Super 上“结果非常出色”，还有人称赞鼠标渲染是相对于当前 SOTA 模型的“一大飞跃”。其他用户则询问 RTX 3060 上的推理速度、这种剪枝技术是否适用于 LLM，以及是否能在 Mac 设备上运行。对于“输出质量无损”的剪枝说法，也有人表示怀疑，认为“简单得几乎不像真的”。总体评价积极，但仍有一些技术问题被提出。

**标签**: `#AI`, `#video-generation`, `#ComfyUI`, `#open-weights`, `#MiniMax`

---

<a id="item-4"></a>
## [Andy Pavlo 加入 ClickHouse，创立 ClickHouse Labs](https://clickhouse.com/blog/andy-pavlo-joins-clickhouse) ⭐️ 8.0/10

知名数据库研究者 Andy Pavlo 加入 ClickHouse，负责建立并领导名为 ClickHouse Labs 的新项目，聚焦数据库架构与研究。 此举表明 ClickHouse 正加大对数据库研究与创新的投入，并可能影响 OLAP 技术及存算分离架构的未来发展方向。 公告引发的讨论聚焦于存算分离架构（如使用 S3 作为存储层）、数据摄入与索引，以及 Iceberg V3、Paimon 等现代表格式。此外，社区成员也希望 Pavlo 能推动 ClickHouse 资助学术界的数据库研究。

hackernews · nikolay_sivko · 8月3日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49156011)

**背景**: ClickHouse 是一款开源的列式数据库管理系统，专为在线分析处理（OLAP）设计，支持使用 SQL 查询实时生成分析报告。OLAP 是一种快速回答多维分析查询的方法，通常处理大规模历史数据。Andy Pavlo 是卡内基梅隆大学（CMU）的知名数据库研究者，其数据库系统系列讲座在社区中广受欢迎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ClickHouse">ClickHouse - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Online_analytical_processing">Online analytical processing - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，多位评论者向 Pavlo 和 ClickHouse 表示祝贺。讨论焦点包括快速 OLAP 产品与 Trino 的融合趋势、存算分离架构的影响，以及希望 ClickHouse 资助学术界数据库研究的呼吁。评论者还对 Pavlo 在 CMU 的系列讲座表示赞赏，认为其影响了他们的学习与职业发展。

**标签**: `#ClickHouse`, `#Andy Pavlo`, `#OLAP`, `#databases`, `#industry-news`

---

<a id="item-5"></a>
## [别当“肉代理”：批判盲目转发 AI 回复的做法](https://gruhn.me/blog/2026-08-03/) ⭐️ 8.0/10

文章创造了“肉代理”一词，指那些不加理解就转发 AI 生成回复的人，并批评了技术职场中的这种做法。该文在 Hacker News 上引发讨论，获得 664 条评论。 随着 AI 生成文本在技术交流中越来越普遍，不加核实就转发的做法会把认知成本转嫁给他人，并削弱责任感。这场讨论凸显了人们对“人在回路”中 AI 使用方式的担忧，以及知识工作中真实理解被侵蚀的问题。 文章创造了一个令人印象深刻的术语并引起社区强烈共鸣，不过有评论者指出“meat puppet”一词早已存在。评论中提出的实用对策包括：让模型生成简化技术英语（ASD-STE100）的要点，使 AI 文本更易核对和改写。

hackernews · ngruhn · 8月3日 06:28 · [社区讨论](https://news.ycombinator.com/item?id=49151933)

**背景**: “肉代理”（meat proxy）是文章新造的词，指充当 AI 被动中间人、在不理解或不核实的情况下转达 AI 输出的人。随着基于大语言模型的工具在软件工程等领域的普及，这种行为日益常见。Hacker News 上的讨论收获了 1,622 点积分和 664 条评论，反映出该话题的强烈关注度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49151933">Don't be a meat proxy | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论者大体认同这一批评，并分享职场轶事，认为这种行为令人疲惫和厌烦。有人建议使用简化技术英语让 AI 输出更容易核对，也有人指出“meat puppet”是更好的既有词语，或分享了一些幽默的重新表述。还有人表示自己曾用直接对抗的方式让同事不再粘贴 AI 回复。

**标签**: `#AI`, `#software engineering`, `#LLM`, `#workplace`, `#commentary`

---

<a id="item-6"></a>
## [Rust 项目目标：提出不可移动类型与受保证析构函数](https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md) ⭐️ 8.0/10

新发布的 Rust 项目目标文档（2026 周期，move-trait.md）提议为语言增加不可移动类型和受保证的析构函数。该提议引入显式的 Move 和 Forget trait，使类型可以选择不允许被移动或遗忘。 不可移动类型弥补了一个长期存在的缺陷：自引用类型（在异步 Future 中很常见）无法安全移动，而目前的 Pin 机制被普遍认为是一种权宜之计。受保证析构函数可以支持安全的作用域 spawn 等模式，即句柄的析构函数即使在 mem::forget 下也能保证运行。 该提议只是一个项目目标，而非已接受的语言变更，因此设计可能会大幅调整甚至被放弃。它还涉及 !Destruct / 线性（『必须移动』）类型等相关概念，但重点是让 Move 和 Forget 成为显式的能力。

hackernews · paavohtl · 8月3日 06:42 · [社区讨论](https://news.ycombinator.com/item?id=49152023)

**背景**: 在 Rust 中，值在所有权转移时默认会被移动，而任何没有实现 Drop（析构）的类型都可以通过 std::mem::forget 被遗忘。然而自引用类型（值内部包含指向自身的指针）一旦移动就会失效，因此异步 Future 目前依赖 Pin/Unpin 机制来解决这个问题。受保证析构函数之所以重要，是因为安全代码目前无法依赖析构函数必定运行（mem::forget 是安全的），这阻碍了某些 RAII 风格的保证。该提议让类型可以选择退出移动和遗忘能力，从而为编译器提供执行这些保证所需的信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md">rust -project-goals/src/2026/move-trait.md at main...</a></li>
<li><a href="https://rust-lang.github.io/rust-project-goals/2026/move-trait.html">Immobile types and guaranteed destructors - Rust Project Goals Rust Project Goals: Immobile Types And Guaranteed Destructors Destructors - The Rust Reference rust-project-goals/src/2026/move-trait.md at main - GitHub Destructors - The Rustonomicon - Learn Rust Immobile types and guaranteed destructors · Issue #635 · rust ... Destructors - The Rust Reference</a></li>
<li><a href="https://doc.rust-lang.org/std/pin/">std::pin - Rust</a></li>

</ul>
</details>

**社区讨论**: 评论者大多欢迎该提议，指出不可移动类型自 2016 年左右就是众所周知的缺失部分，而 Pin 只是权宜之计。有评论者澄清这只是项目目标而非最终确定的语言变更；还有人询问这是否取代了 withoutboats 的替代方案『pinned places』。讨论中还涉及相关的线性类型（!Destruct）概念，也有评论者认为这是把更多代数效应硬套到 Rust 上。

**标签**: `#rust`, `#language-design`, `#type-systems`, `#destructors`, `#immovable-types`

---

<a id="item-7"></a>
## [Qwen3.8-Max：代码生成与 AI 协作的新标杆](https://qwen.ai/blog?id=qwen3.8) ⭐️ 8.0/10

阿里巴巴云的 Qwen 团队发布了 Qwen3.8-Max，这是编码和 AI 协作模型的重大进步，并计划于下周发布开放权重版本 Qwen3.8-27B。该模型在视觉网页开发与感知基准测试中表现出色。 此次发布加剧了 AI 编程助手市场的竞争，为专有前沿模型提供了开放权重替代方案。随着 LLM 能够处理传统上外包给人类开发者的任务，这可能会颠覆程序员的自由职业外包工作。 开放权重版本 Qwen3.8-27B 预计下周发布，接替广受好评的本地模型 Qwen3.6-27B。基准测试突出其强大的图像转 HTML 能力，用户测试显示在复杂设计转 SPA 任务上与 Opus 5 竞争激烈。

hackernews · ai2027 · 8月3日 02:16 · [社区讨论](https://news.ycombinator.com/item?id=49150470)

**背景**: Qwen（通义千问）是阿里云开发的大型语言模型家族。开放权重模型公开发布训练后的参数（权重和偏差），允许任何人下载和运行，但再分发权取决于许可证。这一背景解释了为什么 Qwen3.8 的开放权重变体对本地部署和模型切换灵活性很重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了复杂情绪：一位自由职业者担心在 Upwork 等外包平台上与前沿模型直接竞争，另一位则赞赏即将发布的开放权重 27B 版本。有用户质疑 AI 公司是否真的有护城河，因为用户很容易切换 LLM；还有人分享了并排的图像转 HTML 测试，显示 Qwen3.8-Max 与 Opus 5 表现相当。

**标签**: `#AI/ML`, `#LLM`, `#Qwen`, `#Coding Assistant`, `#Tech Industry`

---

<a id="item-8"></a>
## [Kimi K3 架构深度解析：压缩记忆与跨深度注意力](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis 发布了一份技术深度分析，详细解读了 Kimi K3 的架构，包括压缩记忆、跨深度注意力、潜空间专家路由和推理性能。该模型被视为 Moonshot AI 的下一代旗舰，规模约 2.8 万亿参数的混合专家模型，支持 100 万 token 上下文。 这件事很重要，因为 Kimi K3 的架构突破了传统的注意力累加模式，可能带来更高效的扩展方式和长上下文推理能力。它展示了前沿 AI 的一种设计选择，可能影响未来大型模型的构建方式，尤其是注重效率的部署场景。 Kimi K3 采用 Kimi Delta Attention（KDA）来高效扩展注意力，并利用 Attention Residuals（AttnRes）在深度维度上选择性地检索表示，而不是统一累加。模型还原生支持视觉能力，可处理仓库级编码和前端界面调试等任务。

rss · Semianalysis · 8月3日 19:42

**背景**: 混合专家（MoE）模型每次只激活部分参数，从而在较低算力下拥有大容量。压缩记忆技术旨在缩小注意力缓存，而潜空间专家路由则将 token 映射到语义潜空间以改进专家选择。Kimi K3 通过 KDA 和 AttnRes 进一步延展了这些思路，使模型能跨层访问信息，而不是仅仅逐层累加表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://kie.ai/blog/what-is-kimi-k3">What Is Kimi K 3 ? Moonshot's 2.8T, 1M-Context Flagship</a></li>
<li><a href="https://lmstudio.ai/models/kimi-k3">Kimi K 3</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Model Architecture`, `#Deep Learning`

---

<a id="item-9"></a>
## [机器学习审稿人：无复现代码的论文应直接拒稿](https://www.reddit.com/r/MachineLearning/comments/1vei12v/its_time_to_desk_reject_papers_that_dont_include/) ⭐️ 8.0/10

一位机器学习审稿人报告称，今年在三大顶级会议上评审的 12 篇论文中，只有 1 篇提供了完整可运行的代码。他呼吁对未提供可复现结果代码的论文直接在编辑阶段拒稿（desk reject）。 这一提议直指机器学习研究中的可复现性危机——目前隐藏代码几乎没有代价，而公开代码反而增加被审稿人发现错误的风险。若被采纳，将改变研究激励，推动透明性与可验证性，影响作者、审稿人及会议政策。 审稿人发现，12 篇论文中有 7 篇完全没有代码，4 篇只有部分代码，而 5 篇提供了一些代码的论文中有 3 篇含有明显错误，导致结果无效。只有 1 篇论文提供了从输入数据集到最终 AUROC 输出的完整代码。

reddit · r/MachineLearning · /u/Flaky-Ambition5900 · 8月3日 16:17

**背景**: AUROC（受试者工作特征曲线下面积）是评估二分类模型性能的常用指标，衡量模型区分正负类的能力。在学术出版中，desk reject（桌面拒稿）指编辑不经过外部同行评审就直接退回稿件。机器学习领域正面临可复现性危机，许多研究未提供复现结果所需的代码或数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc">Classification: ROC and AUC | Machine Learning | Google for ... AUROC and AUPRC. In evaluating classification models… | by ... What Is AUROC: Area Under the ROC Curve, Explained A Closer Look at AUROC and AUPRC under Class Imbalance AUROC in Machine Learning: Bridging Statistical Separability ...</a></li>
<li><a href="https://peerreviewai.org/guides/desk-rejection-prevention">How to Avoid Desk Rejection | PeerReviewAI</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/ai-reproducibility-crisis">Is AI Driving a Scientific Reproducibility Crisis ?</a></li>

</ul>
</details>

**标签**: `#reproducibility`, `#machine learning`, `#research practices`, `#code availability`, `#peer review`

---

<a id="item-10"></a>
## [美国 DNA 分析设备漏洞致 30 年法医证据面临篡改风险](https://www.wsj.com/tech/cybersecurity/security-flaw-placed-30-years-of-dna-evidence-at-risk-of-hacking-1932775a) ⭐️ 8.0/10

研究人员发现，美国多数犯罪实验室使用的赛默飞世尔 Applied Biosystems 人类识别软件存在漏洞，可让 1995 年以来的 DNA 数据文件被不留痕迹地篡改。该公司已发布高危安全公告并推出加入数字签名的软件更新，目前尚无实际利用案例。 意义重大，因为 DNA 证据支撑着数十年的刑事定罪；若被利用，案件文件可在不被察觉的情况下被篡改，动摇司法体系的公信力。此事也暴露了全美 200 多家法医实验室网络安全监管薄弱，并给已审或未审案件带来不确定性。 测试中，研究人员借助 Anthropic 的 Claude AI 生成的代码，约 45 分钟即完成文件篡改且未触发常用分析软件警报。赛默飞世尔 7 月已私下承认该问题，并表示正与 CISA 合作；研究人员称尚无法检测此前是否发生过篡改。

telegram · zaihuapd · 8月3日 05:15

**背景**: 法医实验室使用基因分析仪（如赛默飞世尔的 Applied Biosystems 设备）处理 DNA 证据，生成的数据文件随后会被载入分析软件。该漏洞使文件能在分析软件加载前被修改，而这些文件缺少物证纸袋那样的防篡改标记。补丁中加入的数字签名可帮助实验室验证数据文件未被改动。这一发现凸显了随着证据日益数字化，法医科学领域对网络安全的迫切需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html">Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable</a></li>
<li><a href="https://www.hindustantimes.com/technology/security-flaw-placed-30-tears-of-dna-evidence-at-risk-of-hacking-101785681888060.html">Security flaw placed 30 tears of DNA evidence at risk of hacking | Technology News (HT Tech)</a></li>
<li><a href="https://www.techradar.com/pro/security/weve-been-behind-the-ball-for-so-long-experts-say-dna-samples-from-crime-scene-forensics-can-be-modified-and-even-switched-using-an-ai-tool">Researchers used AI-assisted code to undetectably tamper with data from computerized scans of physical DNA evidence produced by widely used crime-lab machines — vulnerable DNA files ‘lack the same level of tamper-evident markings that we require for a paper bag’</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#DNA analysis`, `#forensic science`, `#vulnerability`, `#AI security`

---

<a id="item-11"></a>
## [美媒调查：至少 50 名美国警员滥用摄像头窥探前任](https://www.washingtonpost.com/technology/2026/08/02/how-police-officers-used-vast-network-cameras-spy-their-exes/) ⭐️ 8.0/10

《华盛顿邮报》调查发现，美国至少 50 名执法人员被指控或起诉滥用 Flock 等车牌识别系统，其中 26 起案件涉及窥探妻子、女友、前任或心仪女性。佐治亚州警察局长 Michael Steffman 涉嫌约 600 次搜索前女友的车牌，并于今年 4 月开庭前自杀身亡。 这项调查揭示了快速扩张的监控基础设施被系统性滥用的问题，表明车牌识别摄像头可能被执法者本人用作个人跟踪的工具。随着 ALPR 网络覆盖更多社区，这凸显了加强审计、培训和问责机制的迫切性。 Flock 称其超过 12 万台摄像头覆盖 6000 多个社区，每月记录约 200 亿次车牌扫描；公司 CEO 承认滥用难以完全避免，并推出了可选的「审计辅助」功能。目前美国仅 13 个州要求对这些系统进行审计，至少 8 个州已将滥用行为定为犯罪。

telegram · zaihuapd · 8月3日 09:03

**背景**: 自动车牌识别系统（ALPR/ANPR）通过摄像头和光学字符识别技术自动读取并存储车牌号码，以及相应的时间、地点信息。Flock 摄像头就是这类 ALPR 设备，通常安装在路杆或高架桥上，持续记录所有过往车辆，而不仅仅是涉嫌违规的车辆。由于这些系统会为每一辆普通汽车生成位置数据，警员滥用时实际上就等同于大规模跟踪或监控。这项调查表明，相关监管远远落后于该技术的部署速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number-plate recognition - Wikipedia</a></li>
<li><a href="https://www.dhs.gov/science-and-technology/saver/automatic-license-plate-readers">Automatic License Plate Readers - Homeland Security</a></li>
<li><a href="https://mashable.com/tech/flock-cameras-explained-surveillance">What are Flock cameras? How they work and why they’re... | Mashable</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#law enforcement`, `#license plate cameras`, `#ethics`

---

<a id="item-12"></a>
## [英伟达 170HX 矿卡被破解：解锁 80GB 显存，二手价暴涨](https://finance.sina.com.cn/tech/roll/2026-08-03/doc-inikzqsf4659769.shtml) ⭐️ 8.0/10

亚利桑那州立大学研究人员公开了英伟达 CMP 170HX 矿卡的破解方案。通过 GPU Falcon 安全协处理器的栈溢出漏洞，绕过物理熔丝锁定，将显存最高解锁到 80GB，FP32 算力从 0.39 TFLOPS 提升至 94 TFLOPS。 这一破解将廉价且被严重限制的矿卡变成高显存 AI 推理加速器，大幅降低 AI 工作负载的成本门槛。同时表明英伟达的硬件锁可通过固件安全漏洞被逆转，并已引发二手价格飙升等直接市场影响。 据报道，破解后的显卡可在 Windows 和 Linux 下直接运行 AI 图像生成及大语言模型推理。但长期稳定性和不同批次的解锁上限仍存风险；该破解利用 Falcon 安全协处理器的 DMA 无界溢出改写寄存器实现解锁。

telegram · zaihuapd · 8月3日 11:29

**背景**: CMP 170HX 是英伟达 2021 年推出的专用以太坊矿卡，采用与 A100 数据中心 GPU 相同的 GA100 核心。英伟达通过 OTP 熔丝锁定了算力、显存和 PCIe 等能力，此前被认为不可逆转；此次破解正是利用英伟达 GPU 上负责安全固件的 Falcon 微控制器漏洞，推翻了这一假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.topcpu.net/en/gpu-c/cmp-170hx-vs-geforce-gtx-1070">NVIDIA CMP 170 HX vs NVIDIA GeForce GTX 1070 - GPU Comparison</a></li>
<li><a href="https://docs.kernel.org/gpu/nova/core/falcon.html">Falcon (FAst Logic Controller) — The Linux Kernel documentation</a></li>

</ul>
</details>

**标签**: `#GPU`, `#hardware security`, `#AI inference`, `#vulnerability`, `#Nvidia`

---

<a id="item-13"></a>
## [英国再次要求苹果为云备份开后门，限制为仅英国用户数据](https://t.me/zaihuapd/42953) ⭐️ 8.0/10

9 月初，英国内政部向苹果发出新的技术能力通知，要求其为加密云备份创建后门，但这次仅针对英国公民数据。此前 1 月的通知要求访问全球用户数据，引发英美外交紧张，苹果随后于 2 月从英国撤回了 iCloud 高级数据保护功能。 这一事态加剧了政府监控要求与科技公司端到端加密之间的持续冲突。如果苹果遵从要求，可能会削弱对所有用户的安全保障，并为其他政府提出类似后门要求开创先例。 新通知的范围仅限英国公民数据，比之前要求全球数据访问的范围更窄。隐私活动人士警告，任何迫使苹果破坏系统安全的尝试都可能危及全球用户的私人数据；特朗普政府此前曾施压英国撤回要求，而英国坚持将采取一切必要行动保护本国公民。

telegram · zaihuapd · 8月3日 15:40

**背景**: 技术能力通知是根据英国 2016 年《调查权力法》发出的命令，要求相关运营商构建或维持技术能力，以便配合合法的拦截请求。苹果的 iCloud 高级数据保护功能采用端到端加密，这意味着苹果本身不持有解密密钥，因此创建后门将从根本上削弱这一安全模型。英国内政部 1 月发出的通知曾要求访问全球用户数据，促使苹果在 2 月将该功能撤出英国市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.legislation.gov.uk/ukdsi/2018/9780111163610">The Investigatory Powers (Technical Capability) Regulations 2018</a></li>
<li><a href="https://www.gov.uk/government/publications/investigatory-powers-amendment-bill-factsheets/investigatory-powers-amendment-bill-overview-of-the-notices-regime">Investigatory Powers (Amendment) Bill: Overview of the Notices Regime - GOV.UK</a></li>
<li><a href="https://support.apple.com/guide/security/advanced-data-protection-for-icloud-sec973254c5f/web">Advanced Data Protection for iCloud - Apple Support</a></li>

</ul>
</details>

**标签**: `#privacy`, `#encryption`, `#government surveillance`, `#Apple`, `#security`

---