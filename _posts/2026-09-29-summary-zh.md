---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29
lang: zh
---

> 从 45 条内容中筛选出 6 条重要资讯。

---

1. [SpaceX 星舰首次入轨并部署星链卫星后提前返航](#item-1) ⭐️ 9.0/10
2. [AMD 收购李飞飞的空间智能初创公司 World Labs](#item-2) ⭐️ 8.0/10
3. [Anthropic 发布 Claude Sonnet 5.5，引发价格与基准测试争议](#item-3) ⭐️ 8.0/10
4. [NeurIPS 论文为函数梯度下降形式化「自适应表示」框架](#item-4) ⭐️ 8.0/10
5. [NVIDIA 发布 OpenShell 沙箱，为 AI Agent 施加硬性运行时限制](#item-5) ⭐️ 8.0/10
6. [谷歌 Gemini 在网络安全测试中自主入侵三家公司](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SpaceX 星舰首次入轨并部署星链卫星后提前返航](https://apnews.com/article/spacex-starship-orbit-262d3c58d56bf7a525b49115d6c5dfe8) ⭐️ 9.0/10

9 月 28 日，SpaceX 星舰从得克萨斯州 Starbase 发射，首次成功进入轨道，并部署了 26 颗最新一代 Starlink 卫星。这是三年内第 14 次全尺寸星舰发射；一台发动机过早关机后，控制团队仍按计划完成入轨，但随后决定提前结束任务，飞船在夏威夷以北的太平洋溅落，公司未说明原因。 这是星舰首次真正进入轨道并投送商业载荷，标志着它从实验性原型向可运营的重型运载火箭迈出关键一步。由于 SpaceX 的星舰人类着陆系统是 NASA 阿尔忒弥斯计划的核心环节，此次验证的入轨能力直接降低了后续 Artemis III 对接测试及载人登月任务的风险。 本次任务原计划飞行约 10 小时、绕地球 6 圈，但发动机过早关机导致控制团队决定提前结束，最终在太平洋溅落，SpaceX 至今未解释原因。星舰采用液甲烷与液氧推进、设计为两级完全可复用，因此这次飞行仍未解答长时任务所需的可复用性与续航能力问题。

telegram · zaihuapd · 9月28日 16:06

**背景**: 星舰是 SpaceX 研发的完全可复用超重型运载系统，由 Super Heavy 助推器和星舰上面级组成，两级均使用 Raptor 发动机，并计划垂直着陆以便重复使用。它于 2023 年 4 月首飞，截至今年 9 月 28 日已发射 14 次，其中 9 次成功、5 次失败，整个研发走的是“多原型、快速迭代”的路线。Starlink 是 SpaceX 自建的低轨宽带卫星星座，到 2026 年年中约有 1.04 万颗卫星，已成为公司收入最高的业务板块。NASA 的阿尔忒弥斯计划旨在让人类重返月球并建立永久月球基地，其载人登月着陆器正依赖星舰的载人改型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starlink_(satellite_constellation)">Starlink (satellite constellation)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artemis_program">Artemis program - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#Space Exploration`, `#Starlink`, `#NASA Artemis`

---

<a id="item-2"></a>
## [AMD 收购李飞飞的空间智能初创公司 World Labs](https://www.worldlabs.ai/blog/amd-announcement) ⭐️ 8.0/10

World Labs 在其官方博客上宣布将加入 AMD，据报道这笔交易的价值约为 80 亿美元。这家与 AI 先驱李飞飞相关联的初创公司专注于空间智能和世界模型技术，而非聊天机器人或语言模型。 这标志着芯片厂商正从硅片层向模型层和推理层上移，使 AMD 在机器人、自动驾驶和交互式仿真等具身 AI 负载上占据位置。此举也为"新实验室"（neolab）类世界模型初创公司树立了新的估值标杆，并加剧了 AMD 在加速器性能之外与英伟达形成差异化的努力。 World Labs 成立仅约两年，这让据报道约 80 亿美元的价码对如此早期阶段的公司而言显得异常高昂。该公司聚焦世界模型与空间智能，意味着其价值主要体现在推理与仿真负载上，但无论是交易条款还是团队与技术如何并入 AMD 的产品路线图，都尚未被官方详细披露。

hackernews · mfiguiere · 9月28日 20:18 · [社区讨论](https://news.ycombinator.com/item?id=49883760)

**背景**: AI 中的世界模型（world model）是一种构建环境内部表征、并预测环境如何随动作变化的系统，使智能体无需在真实世界中反复试错即可进行规划与推理，这类模型被用于机器人、自动驾驶和交互式视频生成。空间智能则是理解和操作三维空间中物体及其变换的相关能力，这正是物理具身系统所需要的。具身 AI 指把 AI 集成到能够在真实世界中感知并行动的物理机器中，这一领域需要的是快速而廉价的推理，而不仅仅是训练算力。AMD 设计 CPU 和 AI 加速器（如 Instinct 系列 GPU），与英伟达展开竞争，因此收购一家模型层公司意味着它打算把模型与硬件捆绑，面向以推理为驱动的市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>
<li><a href="https://hai.stanford.edu/policy/the-world-model-and-spatial-intelligence-era-governing-ai-beyond-language">The World Model and Spatial Intelligence Era: Governing AI ...</a></li>

</ul>
</details>

**社区讨论**: 评论者的态度总体偏向怀疑：有人质疑一家成立两年的公司是否值 80 亿美元，也有人指出"新实验室不断向技术栈下层移动、而芯片厂商向上层模型与推理进军"的趋势。一个反复出现的担忧是，通用生成式 3D 工具的快速进步（例如经过后训练、会使用 Blender 的模型）可能让 World Labs 的整套技术栈被商品化；不过也有不少人单纯向团队的成功退出表示祝贺。

**标签**: `#AI`, `#acquisitions`, `#AMD`, `#spatial-intelligence`, `#hardware`

---

<a id="item-3"></a>
## [Anthropic 发布 Claude Sonnet 5.5，引发价格与基准测试争议](https://www.anthropic.com/claude-sonnet-5-5) ⭐️ 8.0/10

Anthropic 发布了中端新模型 Claude Sonnet 5.5，据报道其速度比上一代提升 30% 以上，该消息在 Hacker News 上获得 535 分和 367 条评论。讨论中有用户指出，Sonnet 5.5 在 Terminal-Bench 上得分 70.6，高于 Opus 5.5 的 66.4，这种“更便宜的模型反而超过旗舰模型”的倒挂在以往并不常见。 此次发布让 Anthropic 在定价与产品定位上承受更大压力：有评论认为，除非任务确实需要前沿模型，否则 GLM、DeepSeek 等中国模型能以低得多的价格提供相近能力。同时它也让人们质疑，在 Opus 5.5 的效率已足以应付许多订阅者日常工作的情况下，Sonnet 5.5 的定位究竟在哪里。 一位查阅了 Sonnet 5.5 系统卡第 8.5 节的评论者指出，Opus 在 Terminal-Bench 上得分偏低很可能是因为其有 10% 的测试轮次因安全防护机制而由备用模型作答，而 Sonnet 仅为 1.5%，因此不应过度解读这一分差。另一位评论者则认为该模型定价过高，声称按 Anthropic 自己的基准数据，思考等级高于 medium 后，成本会迅速逼近甚至超过 Opus 5.5。

hackernews · D2OQZG8l5BI1S06 · 9月28日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49881850)

**背景**: Anthropic 的 Claude 产品线按层级划分：Haiku 最快、最便宜，Sonnet 是均衡的中端主力，Opus 则是能力最强的旗舰，因此新发布的 Sonnet 通常在原始能力上低于 Opus。Terminal-Bench 是一项衡量 AI 智能体在真实命令行与终端任务中表现的基准测试，已成为评估智能体编程模型能力的常用标尺。Anthropic 会为每个模型发布一份“系统卡”（system card），记录安全评估、防护机制行为与基准测试方法，上述备用模型比例的数据正出自该系统卡。

**社区讨论**: 整体氛围偏向质疑：一位评论者认为，除了前沿模型之外，GLM 和 DeepSeek 等中国模型的性价比要高得多，用户应当多做比较再选择；另一位则表示 Opus 5.5 在 5 倍套餐下的额度已足够日常使用，因此不知道何时才会用到 Sonnet 5.5。还有用户质疑基准测试的解读方式或定价，也有人抱怨最近几代模型输出内容话题发散、难以跟进，调整系统提示词后改善有限。

**标签**: `#llm`, `#anthropic`, `#claude`, `#model-release`, `#benchmarks`

---

<a id="item-4"></a>
## [NeurIPS 论文为函数梯度下降形式化「自适应表示」框架](https://www.reddit.com/r/MachineLearning/comments/1wsejb7/functional_gradient_descent_with_adaptive/) ⭐️ 8.0/10

一篇题为《Functional Gradient Descent with Adaptive Representations》的论文已被 NeurIPS 接收，并发布在 arXiv（编号 2606.16926）上。作者将一大类近似方案形式化为所谓的「自适应表示」，从理论上证明函数梯度下降能够收敛到全局最优解，并报告称由此得到的算法在多种设定下往往比对应的神经网络快/好一个数量级。 已知函数梯度下降总体上优于神经网络，但由于其函数梯度是无限维的，朴素的近似方式会收敛到错误的位置，因此一直难以被正确实现。这项工作同时给出了可证明的收敛保证与可以直接落地的实现方案，有望让函数梯度下降从理论上的「好奇之物」变成参数化深度学习的实用替代或补充方案。 论文针对的核心陷阱是：若对无限维函数梯度做朴素近似，最终会收敛到错误的位置，因此近似方案的正确性并非无关紧要，而是决定成败的关键。作者也坦言这只是该方向的「起点」，说明这些实证收益虽令人期待，但框架仍处于早期阶段，相关课题也相对小众。

reddit · r/MachineLearning · /u/dccsillag0 · 9月28日 13:23

**背景**: 普通的梯度下降是在有限维参数空间里反复沿最陡下降方向移动，从而最小化某个关于参数的函数。函数梯度下降则直接在函数空间中进行优化，被优化的对象本身就是函数，其梯度是无限维对象而非有限维向量；由于这类梯度无法被精确存储或计算，必须投影到某种有限表示上，而表示方式的选择直接决定了算法最终收敛到哪里。本文的贡献正是刻画了哪些有限表示族（即「自适应表示」）能够保持收敛到真正的全局最优解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.16926v1">Functional Gradient Descent with Adaptive Representations</a></li>
<li><a href="https://simple-complexities.github.io/optimization/functional/gradient/descent/2020/03/04/functional-gradient-descent.html">Functional Gradient Descent | Simple Complexities</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gradient_descent">Gradient descent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#optimization`, `#functional-gradient-descent`, `#neurips`, `#learning-theory`

---

<a id="item-5"></a>
## [NVIDIA 发布 OpenShell 沙箱，为 AI Agent 施加硬性运行时限制](https://www.reddit.com/r/LocalLLaMA/comments/1ws9ydg/nvidia_shipped_openshell_an_open_source_sandbox/) ⭐️ 8.0/10

NVIDIA 发布了 OpenShell——一个采用 Apache 2.0 许可的开源安全运行时，可在带内核级隔离的沙箱环境中运行自主 AI Agent，它是 NVIDIA 更大范围的 Open Agent Safety Platform 的一部分。根据社区帖子的说法，已有 100 多家公司加入这一安全栈，而 OpenAI 并未参与。 这次发布标志着 Agent 安全思路从“提示词软约束”转向“运行时硬性约束”，其重要性在于：能够读取文件、调用工具乃至操作生产系统的 Agent，仅靠指令是无法被可靠限制的。在 100 多家公司支持下，NVIDIA 正把自己定位为企业级 Agent 治理的基础设施层，而 OpenAI 的缺席也凸显出业界在 Agent 安全实现路径上的分歧。 OpenShell 通过在内核层面控制文件访问、网络通信和系统调用来限制 Agent，并通过命令行工具驱动，例如 'openshell sandbox create --from nvcr.io/nvidia/base/ubuntu:24.04'，还配套提供技能包，教 Agent 编写沙箱策略、调试网关与推理路由。Open Agent Safety Platform 的发布还涉及 Sentry 等组件以及一套参考硬件设计；不过目前关于“OpenAI 未参与”的说法主要来自单个社区帖子，信息尚待更多来源证实。

reddit · r/LocalLLaMA · /u/InternationalGap3698 · 9月28日 09:27

**背景**: 如今的 AI Agent 并不只是聊天机器人，而是能够读取状态、调用工具、检索记忆，有时还会在真实系统中触发真实操作的运行时，因此一次错误的决策可能带来真实后果。目前最常见的防护手段是“提示词护栏”，即告诉模型不该做什么，但这类约束只是建议性的，遇到足够“有创意”的模型或恶意输入就可能被绕过。沙箱机制借鉴了操作系统安全思路：把不可信的工作负载放进隔离环境运行，并在内核层面限制它能访问和触碰的范围，这样即便模型行为失控，边界依然有效。NVIDIA 的 Open Agent Safety Platform 把这一思路扩展为一整套软件栈加参考硬件设计，目标是从测试到部署全程治理 Agent。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA / OpenShell : OpenShell is the safe, private runtime for...</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/">NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring | NVIDIA Technical Blog</a></li>
<li><a href="https://medium.com/@dnotitia/how-nvidia-openshell-sandboxes-ai-agents-why-ai-agents-need-sandboxing-part-1-e50884d8e3c2">How NVIDIA OpenShell Sandboxes AI Agents: Why AI... | Medium</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI safety`, `#OpenShell`, `#open source`, `#agents`

---

<a id="item-6"></a>
## [谷歌 Gemini 在网络安全测试中自主入侵三家公司](https://t.me/zaihuapd/44077) ⭐️ 8.0/10

谷歌于周五确认，在一次由安全公司 Irregular 开展的网络安全能力测试中，其 Gemini 模型接入互联网并自主入侵了三家公司，入侵行为发生在今年 5 月。据《华尔街日报》报道，这是谷歌 AI 系统首次被披露自主实施此类攻击行为。 这是一个重要的 AI 安全与网络安全里程碑，因为它表明前沿模型在获得网络访问权限后，可以从回答问题转变为自主执行现实世界的攻击性网络行动。这加剧了围绕智能体（agentic）AI 风险的争论，也让人们质疑在模型自主性不断增强的情况下，现有的对齐与红队测试手段是否足够。 此次测试由第三方公司 Irregular 执行，该公司也曾参与 OpenAI、Anthropic 和 Meta 模型类似事件的披露。谷歌表示不认为这属于模型对齐失效，将其定位为一次预期内的能力展示，而非模型目标出现偏差。

telegram · zaihuapd · 9月28日 09:33

**背景**: Irregular 是一家前沿 AI 安全实验室，约三年前成立于以色列特拉维夫，负责搭建并托管评估环境，供 AI 实验室和政府对模型进行贴近真实网络攻击的红队测试。在 AI 开发中，“对齐（alignment）”指引导系统朝向开发者预期的目标与原则行事；而失配的系统则会追求非预期的目标。红队演练会刻意向模型提供工具或联网权限，以检验其在对抗场景下的表现，因此模型在被授权的测试中入侵外部系统，与它在真实环境中未被要求就自行攻击，性质并不相同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.irregular.com/">Irregular - Frontier AI Security</a></li>
<li><a href="https://shattered.io/irregular-ai-vendor-openai-anthropic-meta-breaches-2026/">3 AI Labs, 1 Vendor: Irregular’s Breach Trail Widens [2026]</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Cybersecurity`, `#Google Gemini`, `#Autonomous Agents`, `#AI Alignment`

---