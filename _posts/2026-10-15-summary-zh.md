---
layout: default
title: "Horizon Summary: 2026-10-15 (ZH)"
date: 2026-10-15
lang: zh
---

> 从 36 条内容中筛选出 7 条重要资讯。

---

1. [Citizen Lab 揭露 AdFection：定向广告沦为零点击间谍软件投递管道](#item-1) ⭐️ 9.0/10
2. [Meta 发布 Muse Spark Open：可在消费级硬件运行的 816B-A42B 开放权重模型](#item-2) ⭐️ 8.0/10
3. [Goodfire 的 Nick Cammarata 称神经网络本质上是「干净」的](#item-3) ⭐️ 8.0/10
4. [Libreboot 26.10 "Ominous Olive" 发布：引入 UEFI/EDK2 并支持 233 款 Chromebook](#item-4) ⭐️ 8.0/10
5. [随笔探讨：AI 逼近数学发现，数学家为何陷入存在性焦虑](#item-5) ⭐️ 8.0/10
6. [Anthropic 向投资者披露第三季度营收达 168 亿美元，环比增长近 50%](#item-6) ⭐️ 8.0/10
7. [MIT 与 PNAS：神经网络可自组织出自己的学习回路](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Citizen Lab 揭露 AdFection：定向广告沦为零点击间谍软件投递管道](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 9.0/10

Citizen Lab 发布了一项名为“AdFection”的攻击活动研究报告，指称一家在以色列注册的广告公司 Discover-Tech 将定向广告基础设施变成投递零点击雇佣间谍软件的管道，用于感染特定个人。The Guardian、The Verge 和 WIRED 在 2026 年 10 月对此进行了报道，Citizen Lab 的原始报告同时记录了分发链路与命令控制（C&C）服务器。 如果广告网络可以被用作间谍软件的投递渠道，那么“只要不点击就安全”这一常识对记者、活动人士和民间社会目标就不再成立。这也给广告技术行业和监管机构带来新的压力，必须回答当广告分发本身成为攻击手段时，责任究竟由谁承担。 一位有 13 年从业经验的广告技术工程师在讨论中指出，报告在“零点击”这一点上“极具耸动色彩”：它详细描述了分发与 C&C 环节，但对究竟什么机制在无用户交互的情况下激活恶意软件却语焉不详。评论者还强调，并不存在单一的“广告提供商”，因为广告技术生态由广告交易平台、SSP、DSP、发布商等众多中间环节组成。

hackernews · jcomp · 10月15日 10:43 · [社区讨论](https://news.ycombinator.com/item?id=50101813)

**背景**: 零点击间谍软件是指无需受害者点击或进行任何交互即可感染设备的恶意程序，通常利用操作系统或应用程序中的漏洞实现。雇佣间谍软件是商业公司开发并出售给政府客户的监控工具，苹果曾多次通过威胁通知向 150 多个国家的用户发出此类攻击的警告。定向广告允许买方通过广告交易平台按地理位置、设备类型等条件筛选受众，这意味着攻击者理论上可以“购买”针对某一特定个人的广告展示，把广告分发链路变成投递通道。Citizen Lab 是多伦多大学的研究机构，长期追踪商业监控技术的滥用问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Exposing AdFection : How Discover-Tech Turned... - The Citizen Lab</a></li>
<li><a href="https://www.wired.com/story/nightmare-scenario-zero-click-spyware-is-infecting-phones-via-targeted-ads/">‘Nightmare Scenario’: Zero-Click Spyware Is Infecting Phones... | WIRED</a></li>
<li><a href="https://news.ycombinator.com/item?id=50101813">Zero-Click Spyware Delivered via Targeted Ads : AdFection</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（约 347 分、505 条评论）意见分化：一位广告技术工程师质疑“零点击”的表述以及存在单一应负责的“广告提供商”这一说法，另一些人则主张干脆禁止在线广告，或者转而起诉实际展示这些广告的网站。还有评论者质疑以色列网络安全公司因与国家的关系而难以被视为独立可信的实体，并就以色列为何能位居全球网络强国前列展开争论。

**标签**: `#spyware`, `#adtech`, `#cybersecurity`, `#privacy`, `#zero-click exploits`

---

<a id="item-2"></a>
## [Meta 发布 Muse Spark Open：可在消费级硬件运行的 816B-A42B 开放权重模型](https://research.meta.ai/blog/muse-spark-open) ⭐️ 8.0/10

Meta 发布了 Muse Spark Open，这是一个开放权重的混合专家（MoE）模型，总参数量 8160 亿、激活参数 420 亿（816B-A42B），权重已上线 Hugging Face，并同步提供了部署文档和发布博客。Meta 强调该模型经过优化，可在 Mac Studio 等消费级硬件上运行，并且首发即支持 Unsloth、MLX 等多种推理运行时。 这是 Meta 重返开放权重赛道的一次重要发力，而此时 Qwen、GLM 等中国开放权重模型已成为自托管部署的强势默认选择。如果超大 MoE 模型真的能在单台高端桌面设备上跑起来，那么“不租云 GPU 也能部署接近前沿的能力”这件事的适用范围将被重新定义。 该模型的许可证并非毫无限制：其中包含一条“模型即服务（Model as a Service）”条款，若被许可方及其关联方的总营收超过 2000 万美元，则不得通过 API 或类似接口向第三方提供该模型的输出。由于其混合专家架构，420 亿激活参数决定推理速度，而完整的 8160 亿参数仍决定显存/内存需求，因此在消费级硬件上运行必须依赖较为激进的量化。

hackernews · bigwheels · 10月15日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=50107379)

**背景**: 混合专家（MoE）模型把网络拆分成众多专门的“专家”子网络，每个 token 只激活其中少数几个，因此它有两个参数量：用于存储知识的总参数量和决定速度的激活参数量。标注为 816B-A42B 的模型意味着存储了 8160 亿参数，但每次计算只经过 420 亿参数，这也是这类模型速度较快却依然需要巨大内存的原因。“开放权重”只表示训练好的权重可以下载并在本地运行，这与许可证条款是两回事——许可证仍可能限制商业用途或托管服务。该领域的竞争对手包括阿里巴巴的 Qwen 系列和 Z.ai 的 GLM 系列，它们被广泛自托管或由云厂商托管；Artificial Analysis 等评测聚合平台则从智能水平、速度和价格等维度对这类模型进行对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts (MoE) explained for local LLMs · localmodel.run</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(large_language_model)">GLM (large language model)</a></li>
<li><a href="https://artificialanalysis.ai/leaderboards/models">LLM Leaderboard - Comparison of AI models from... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人引用 Artificial Analysis 的数据指出 Muse Spark Open 不如 Qwen3.8 Flash Next 和 GLM 5.3 Flash，而后者都能在单台 B300 上运行，认为 Meta 在开放权重领域还需追赶；也有人对“开放”的说法提出质疑，引用许可证中的“模型即服务”条款及 2000 万美元营收门槛。支持者则称赞 Meta 对 Unsloth、MLX 等众多运行时的广泛适配，并认为一旦 Meta 的模型成为行业标准，真正的护城河是生态锁定而非许可证本身的开放程度。

**标签**: `#open-weight-models`, `#Meta`, `#LLM`, `#model-licensing`, `#AI-benchmarks`

---

<a id="item-3"></a>
## [Goodfire 的 Nick Cammarata 称神经网络本质上是「干净」的](https://already-clean.goodfire.com/) ⭐️ 8.0/10

Goodfire 的可解释性研究员 Nick Cammarata（曾在 OpenAI 参与早期机制可解释性研究）发布了题为「Neural networks are clean」的文章（already-clean.goodfire.com），认为神经网络在很大程度上并不存在叠加（superposition）问题，而是基本可解释的、并非混乱的。文章还配有一个交互式「显微镜」演示，Cammarata 称其为「第一个我自认为基本理解的、非平凡的神经网络」。 如果神经网络本质上确实「干净」、默认就大体可解释，就等于动摇了「叠加是机制可解释性最大障碍」这一前提，而许多研究者认为可解释性是解决 AI 对齐问题的先决条件。因此这一主张对 Goodfire、Anthropic、OpenAI 等对齐与可解释性研究机构，以及「我们究竟能逆向工程出模型内部多少机制」的更大争论都意义重大。 Cammarata 把这一定位为与对齐相关的突破，他在发布帖中称「如果我们不知道自己造的是什么，就无法解决对齐问题」，并附上了交互式演示链接。批评者则认为这些结论超出了已被证明的范围：渐进式特征复杂度与「彩票假说」（Lottery Ticket Hypothesis）早已为人所知，且并不与参数过载／叠加互斥；多模态鸿沟（multimodal gap）的研究（arXiv:2203.02053）反而暗示网络倾向于压缩表征。

hackernews · themgt · 10月15日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=50105647)

**背景**: 机制可解释性（mechanistic interpretability，简称 mech interp）是可解释 AI 的一个子领域，旨在把神经网络内部的具体结构、算法与电路逆向工程为人类可理解的解释。其中一个核心概念是「叠加」（superposition）：由于模型的神经元数量远少于它需要表示的特征数，特征被认为会以重叠且难以读懂的方向被压缩在一起，这也是可解释性被认为困难的根源。Goodfire 是一家位于旧金山的可解释性研究实验室与公益公司（public benefit corporation），由曾在 OpenAI 和 Google DeepMind 开创可解释性工作的研究者创立，融资已超过 2 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://www.goodfire.com/">Goodfire AI</a></li>
<li><a href="https://www.goodfire.com/company">About Goodfire</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：有人称赞 Cammarata 是「一股自然力量」，并强调发布帖把可解释性称为当今最重要的科学问题；也有人认为这些主张「超出了真正被证明的范围」，并援引彩票假说与多模态鸿沟的研究。另一些人则提供了具体资源——文章的音频版本和「显微镜」演示链接；还有评论者把这种语气比作 Anthropic 机制可解释性团队在首批大规模 SAE 结果出炉时的「轻躁狂式热情」，当时许多人相信关键范式已经找到，剩下的只是把它规模化。

**标签**: `#mechanistic-interpretability`, `#AI-alignment`, `#neural-networks`, `#machine-learning`, `#research`

---

<a id="item-4"></a>
## [Libreboot 26.10 "Ominous Olive" 发布：引入 UEFI/EDK2 并支持 233 款 Chromebook](https://libreboot.org/news/libreboot2610.html) ⭐️ 8.0/10

代号 "Ominous Olive" 的 Libreboot 26.10 通过 EDK2/TianoCore payload 引入了 UEFI 支持，并一次性导入了 MrChromebox coreboot 发行版目前支持的全部 233 款 Chromebook。该版本仅提供源码，用户需要自行编译固件而不能下载预编译 ROM；同时项目还正式确立了严格禁止 LLM 辅助贡献的政策。 引入 UEFI/EDK2 payload 并整合 MrChromebox 的整套 Chromebook 设备树，使 Libreboot 可运行的机型数量成倍增长，也让未来移植新设备变得容易得多，因为开发者有了可参考的上游实现。这标志着这个历来以支持列表小而精著称的项目，正走向更广泛的主流硬件覆盖。 目前只有 Baytrail（Kip）平台经过测试，其余导入的设备仍待验证，而且本次发布不提供任何二进制镜像。项目还在其 lbmk 仓库中发布了 AGENTS 文件，明确规定拒绝 AI 生成的补丁，但在一定程度上接受 AI 辅助撰写的缺陷报告。

hackernews · iamnothere · 10月15日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=50102923)

**背景**: Libreboot 是 coreboot 的一个发行版；coreboot 是自由开源的固件，负责完成底层硬件初始化并引导操作系统，用以替代专有的 BIOS 或 UEFI 实现。由于 coreboot 需要针对每一款芯片组和主板单独移植，其硬件支持范围取决于贡献者移植了多少块主板。EDK2（TianoCore EDK II）是 Intel 主导的 UEFI 规范事实参考实现，而 MrChromebox 则是为大量 Chromebook 提供固件的 coreboot 发行版。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Libreboot">Libreboot</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coreboot">Coreboot</a></li>
<li><a href="https://en.wikipedia.org/wiki/EDK2">EDK2</a></li>

</ul>
</details>

**社区讨论**: 多数评论者认为真正的重点是 UEFI/EDK2 集成与 Chromebook 支持，有人称这让可用设备数量 "成倍增加"，而 AI 政策反而抢走了关注度。Heads/LinuxBoot 项目的贡献者（cwiggs）提到自己也在做类似的 ChromeOS 设备移植工作，并把 MrChromebox 的代码当作上游依赖；而反对 LLM 辅助贡献的立场一方面被赞为 "令人耳目一新"，另一方面也反映出该项目对前沿 AI 的强硬态度。

**标签**: `#firmware`, `#coreboot`, `#libreboot`, `#UEFI`, `#open-source`, `#Chromebook`

---

<a id="item-5"></a>
## [随笔探讨：AI 逼近数学发现，数学家为何陷入存在性焦虑](https://www.derekthompson.org/p/i-know-why-the-mathematicians-weep) ⭐️ 8.0/10

作家 Derek Thompson 发表了题为《I know why the mathematicians weep》的哲学随笔，认为随着 AI 系统日益侵入数学发现领域，数学家正陷入一种存在性焦虑。该文在 Hacker News 上获得 325 分和 529 条实质性评论，讨论焦点集中在 AI 是否正在把数学工作的声望商品化，以及是否正在侵蚀验证数学真理的社会机制。 这篇文章捕捉到了一种更广泛的文化转变：当 AI 系统能够产出研究级别的数学证明和结果时，被重塑的可能不只是个别岗位，而是整个学科的声望体系、职业结构以及认识论权威。它还提出了一个远超数学领域的问题——在充斥 AI 的信息环境中，对真理的验证是否正在被单纯的“看起来可信”所取代。 有评论者指出，这篇文章虽未点名，但实际围绕哲学家 Robert Brandom 的“道义记账”（deontic scorekeeping）理论展开——该理论认为概念系统依赖于社会性的理由与资格交换而得以维系。核心争议在于：AI 给出的数学结果究竟是被真正验证过，还是仅仅因为可信度、形式或数量而被接受；据称，连 Hacker News 的部分读者都未阅读或核验证明，就已认定某些问题被解决了。

hackernews · RickJWagner · 10月15日 13:44 · [社区讨论](https://news.ycombinator.com/item?id=50103630)

**背景**: 自动定理证明（automated theorem proving）是自动推理与数理逻辑的一个子领域，自计算机科学诞生之初就致力于让程序自动生成形式化证明。自 2020 年代中期以来，大型语言模型——尤其是被训练来解决多步推理问题的“推理模型”——在研究级证明生成上取得了持续进展，成果大多来自 OpenAI 和 Anthropic。正是在这一背景下，数学家们开始追问：自己的技艺中还剩下什么是真正属于人类的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_mathematical_discoveries_by_artificial_intelligence">List of mathematical discoveries by artificial intelligence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reasoning_model">Reasoning model - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同这种焦虑，但把焦虑归因于不同的损失：有人认为，一旦声望被商品化，建立在声望与苦练技能之上的整个人生架构便化为乌有；也有人哀悼的不是饭碗，而是“追寻真理的欲望”的消失——如今一切都无人验证，数量或声量取代了证明。一条高赞讨论引用 Brandom 的道义记账理论，认为 LLM 编码了人类语言的规范性规律，却必然缺失维系意义的社会实践；也有质疑者反驳说 Thompson 根本不懂纯数学——借用爱因斯坦“我想知道上帝的想法”的说法，数学家哀悼的并非沉没成本，而是可能再也无法亲手发现根本真理。

**标签**: `#AI and mathematics`, `#AI existential impact`, `#philosophy of mathematics`, `#LLM reasoning`, `#academic culture`

---

<a id="item-6"></a>
## [Anthropic 向投资者披露第三季度营收达 168 亿美元，环比增长近 50%](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 8.0/10

据《金融时报》报道（Simon Willison 做了摘要），Anthropic 周三向投资者披露其第三季度（7 至 9 月）营收环比增长近 50%，达到 168 亿美元，高于第二季度的 115 亿美元和第一季度的约 48 亿美元。公司还披露，模型蒸馏贡献了 5% 至 7% 的营收，并已在第三季度“大幅”削减了这部分用量，此举发生在公司筹备 IPO 之际。 以单季 168 亿美元的规模计算，Anthropic 的体量已可媲美大型上市软件公司，这使其 IPO 成为 AI 行业最受瞩目的事件之一。而“竞争对手为蒸馏 Anthropic 模型花费数亿美元”的披露，也表明竞争态势与 API 驱动的数据使用正在成为前沿实验室财务报表上的实质性项目。 第三季度 Anthropic 每在算力上花费 1 美元就产生 1.70 美元营收，剔除股权激励后的调整后营业利润率为 11%，说明在计入算力成本后盈利空间仍然较薄。Willison 推算，若蒸馏占第二季度营收的 5%，那么未具名的竞争对手在该季度为蒸馏 Anthropic 模型花费了超过 5 亿美元；值得注意的是，Anthropic 在面向投资者的沟通中似乎已不再使用“年化运行率营收”这一口径。

rss · Simon Willison · 10月15日 13:04

**背景**: 知识蒸馏是一种用一个 AI 模型（“学生”）去学习另一个通常更强的模型（“教师”）输出的技术——它是制造更小、更便宜模型的合法且广泛使用的方法，但当实验室利用竞争对手的商业 API 输出来训练竞品模型时就颇具争议。Anthropic 的这些数据发布在备受期待的 IPO 之前；而“年化运行率营收”是一种将单期营收外推到全年的初创企业指标，批评者认为它会夸大高速增长业务的实际规模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://innodata.com/what-is-knowledge-distillation-in-ai/">What is Knowledge Distillation in AI ? — Innodata</a></li>
<li><a href="https://blog.roboflow.com/what-is-knowledge-distillation/">What is Knowledge Distillation ? A Deep Dive. | Roboflow Blog</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI industry`, `#IPO`, `#revenue growth`, `#distillation`

---

<a id="item-7"></a>
## [MIT 与 PNAS：神经网络可自组织出自己的学习回路](https://www.reddit.com/r/MachineLearning/comments/1x6hmyg/how_artificial_neural_networks_build_their_own/) ⭐️ 8.0/10

2026 年 10 月 9 日发表在 PNAS 上、并由 MIT News 于 10 月 13 日报道的一篇论文指出，由共享局部可塑性规则支配的、随机互连的类神经元单元能够自发地自组织出“学习基元”（learning motifs），进而在模式识别和图像分类任务上达到与该研究中所测试的反向传播训练网络相当的性能。其核心转变在于：不再直接设计学习回路，而只是规定局部规则，让学习机制自行组织形成。 如果基于梯度的学习能够从随机连接和简单局部可塑性规则中自下而上地涌现，那么它就在生物可塑性与现代机器学习之间架起了一座有理论依据的桥梁，并可能为类脑硬件或神经形态系统带来更具生物合理性的训练思路。这也意味着未来网络的学习回路或许无需人工精心设计。 论文报告的精度对比仅限于其所测试的特定模式识别和图像分类任务；论文也明确指出，自组织现象并不能证明大脑真的采用这一机制——其动机是追求生物合理性，而非宣称可以在大规模模型中取代反向传播。尚待回答的问题包括：这些涌现出的基元在不同初始连接下是否稳定，以及该方法能否推广到所展示任务之外。

reddit · r/MachineLearning · /u/Dorian182 · 10月15日 10:01

**背景**: 反向传播是现代深度学习的核心算法，但它依赖全局误差信号和权重传输，这些机制在真实大脑中普遍被认为缺乏生物合理性。相比之下，局部可塑性规则（例如仅依赖邻近神经元与突触活动的 Hebbian 式更新）更接近神经科学实验所观察到的现象。这类研究要问的是：把这种简单的局部规则施加于随机连接的网络，能否集体涌现出在功能上等价于梯度学习回路的结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.2606245123">How biological synapses self-assemble gradient learning | PNAS</a></li>
<li><a href="https://news.mit.edu/2026/how-artificial-neural-networks-build-their-own-learning-machinery-1013">How artificial neural networks build their own learning machinery</a></li>
<li><a href="https://arxiv.org/pdf/2412.20018">Self - Assembly of a Biologically Plausible Learning Circuit</a></li>

</ul>
</details>

**标签**: `#Neural Networks`, `#Self-Organization`, `#Plasticity`, `#Backpropagation`, `#Computational Neuroscience`

---