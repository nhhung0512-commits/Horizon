---
layout: default
title: "Horizon Summary: 2026-09-25 (ZH)"
date: 2026-09-25
lang: zh
---

> 从 27 条内容中筛选出 4 条重要资讯。

---

1. [美国上诉法院维持五角大楼对 Anthropic 的供应链风险认定](#item-1) ⭐️ 9.0/10
2. [Go 官方博客发布实验性平台无关 SIMD 包](#item-2) ⭐️ 8.0/10
3. [SemiAnalysis 发布中国数据中心模型，覆盖 1000+ 设施](#item-3) ⭐️ 8.0/10
4. [F-Droid 发布 2.0，开源安卓应用商店迎来十年来最大更新](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [美国上诉法院维持五角大楼对 Anthropic 的供应链风险认定](https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html) ⭐️ 9.0/10

2026 年 9 月 25 日，华盛顿特区一家联邦上诉法院维持了五角大楼将 Anthropic 列为“供应链风险”的决定，驳回了该公司针对特朗普政府提起诉讼、试图撤销这一黑名单措施的请求。该认定最初于 2026 年 3 月作出，如今在 Anthropic 不再上诉的情况下将正式生效。 这是一个标志性先例：美国法院确认，国家安全的供应链权力可以被用来对付一家本土领先的 AI 公司，这可能会重塑联邦机构采购 AI 的方式，以及供应商对其模型使用方式的话语权。它还引发担忧：该机制可能被政治性地用于打击其他承包商，从而在整个国防工业基础中抑制 AI 安全护栏的设立。 根据法律分析，国防部（Department of War）依据两项法律授权——10 U.S.C. § 3252 与 2018 年《联邦采购供应链安全法》（FASCSA）——而旧金山和华盛顿特区两地法院各自只就其中一项作出裁决，因此两条法律路径出现了结果分歧；据报道，2026 年 8 月一名美国法官裁定五角大楼对 Anthropic 的针对行为违法，而此次华盛顿特区的上诉裁决结果则相反。

hackernews · cramer4next · 9月25日 15:29 · [社区讨论](https://news.ycombinator.com/item?id=49845977)

**背景**: 2018 年《联邦采购供应链安全法》（FASCSA）设立了联邦采购安全委员会，允许政府对被认定构成供应链安全风险的供应商建议发出移除或排除令——这一工具最初是针对华为等外国对手设计的。自 2026 年 1 月起，Anthropic 与国防部就军方如何使用其模型发生冲突，原因是 Anthropic 的使用政策限制监控、自主武器等应用；谈判破裂后，五角大楼并未简单地终止合同，而是正式将该公司列为供应链风险。公司 CEO Dario Amodei 曾在 2026 年 2 月就 AI 的国家安全用途公开发表声明回应这一争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html">U.S. appeals court upholds Pentagon designation of Anthropic as...</a></li>
<li><a href="https://www.mayerbrown.com/en/insights/publications/2026/03/anthropic-supply-chain-risk-designation-takes-effect--latest-developments-and-next-steps-for-government-contractors">Anthropic Supply Chain Risk Designation Takes Effect — Latest Developments and Next Steps for Government Contractors | Insights | Mayer Brown</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic–United_States_Department_of_Defense_dispute">Anthropic–United States Department of Defense dispute - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见严重分裂。有人认为这一认定在法律上是教科书式的操作——Anthropic 给军事用途附加了条件，军方拒绝并干脆不采购它的产品；另一些人则认为这是政治滥用甚至腐败，警告一项本为应对外国对手而设计的工具如今被用于本国企业，未来政府可能反过来用它打击 Palantir 之类的公司。还有一个反复出现的困惑：考虑到五角大楼拒绝使用其模型某种程度上正是 Anthropic 想要的，该公司究竟损失了什么。

**标签**: `#AI regulation`, `#national security`, `#Anthropic`, `#supply chain risk`, `#AI policy`

---

<a id="item-2"></a>
## [Go 官方博客发布实验性平台无关 SIMD 包](https://go.dev/blog/simd-experiment) ⭐️ 8.0/10

Go 官方博客发布了一项实验：为 Go 引入平台无关的 SIMD 包，提供可移植的向量化能力，既能统一支持 x86 AVX、Arm NEON 等固定宽度指令集，也能支持 Arm SVE、RISC-V RVV 这类向量长度可伸缩的指令集。该文章明确定位为实验性探索，而非已经随标准库正式发布的特性。 Go 长期以来缺乏表达数据并行操作的便携方式，开发者只能手写特定架构的汇编，或退回到标量代码；若能在标准库中提供 SIMD API，就能让图像、音频、加密和机器学习等负载在不重写多架构版本的前提下获得显著加速。由于这是官方 Go 项目，它还代表了语言未来性能演进的方向，而不只是一个第三方库。 最关键的设计选择是支持向量长度无关（VLA）：不同于多数早期假定了固定宽度寄存器的可移植 SIMD 方案，该设计能够适配 SVE、RVV 这类可伸缩指令集。早期社区基准测试显示，可移植 SIMD 比架构专用 SIMD 慢约 11%，但比非 SIMD 的标量代码快约 5 倍；该特性仍处于实验阶段，尚无正式发布的时间表。

hackernews · yurivish · 9月25日 11:47 · [社区讨论](https://news.ycombinator.com/item?id=49843269)

**背景**: SIMD（单指令多数据）是一种并行计算模型，一条指令可以同时对多个数据元素进行运算，因此在图像调色、音频音量缩放和矩阵计算等任务上非常高效。现代 CPU 通过指令集架构提供 SIMD 能力：x86 的 SSE/AVX 和 Arm 的 NEON 等较老设计使用固定向量宽度，而较新的 Arm 可伸缩向量扩展（SVE）和 RISC-V 向量扩展（RVV）的向量长度由具体实现决定。编写最优 SIMD 代码通常需要针对每种指令集分别适配，因此语言层面的可移植抽象非常有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SIMD">SIMD</a></li>
<li><a href="https://arxiv.org/html/2605.12445v2">Scalable Packed Layouts for Vector-Length-Agnostic ML Code Generation</a></li>

</ul>
</details>

**社区讨论**: 评论区反响热烈：一位用户分享了基于浏览器 WASM 的调色板替换基准测试，结果显示可移植 SIMD 比架构专用 SIMD 慢约 11%，但比非 SIMD 快约 5 倍；另一位指出，这是他所见首个让 SVE、RVV 这类非固定宽度向量更易支持的可移植方案。还有人将其与 C++ 即将到来的 std::simd 作比较，并称赞 Go 把 SIMD 放进标准库；一位开发者则提到在无需 CGO 的 Go 语音识别与语音合成模型中获得了可感知的性能提升。

**标签**: `#Go`, `#SIMD`, `#performance`, `#compilers`, `#programming-languages`

---

<a id="item-3"></a>
## [SemiAnalysis 发布中国数据中心模型，覆盖 1000+ 设施](https://newsletter.semianalysis.com/p/the-chinese-ai-infrastructure-boom) ⭐️ 8.0/10

SemiAnalysis 推出了一个全面的中国数据中心模型，覆盖了超过 1000 个设施和 60 多家运营商。分析显示，中国数据中心最初以零售为主建设，但已被转向支持 AI，其中最大的超大规模租户租赁了全国五分之一的容量，并在 12 个月内增加了 100MW。 该模型为中国 AI 基础设施的规模和结构提供了前所未有的可见性，这对于该国在美国出口管制下积极扩展计算能力至关重要。它有助于投资者、分析师和政策制定者了解中国数据中心格局如何演变以支持 AI 工作负载，突出了超大规模企业的主导地位以及从零售向 AI 驱动需求的转变。 该模型追踪了 60 多家运营商的 1000 多个设施，显示许多数据中心最初是为零售托管而建，但正在被改造用于 AI。它还与“东数西算”计划相关联，该计划旨在利用中国西部的可再生能源和凉爽气候，尽管一些报告质疑其有效性。最大的超大规模租户租赁了全国五分之一的容量，并在 12 个月内增加了 100MW，表明高度集中和快速增长。

rss · Semianalysis · 9月25日 15:58

**背景**: SemiAnalysis 是一家专注于半导体和 AI 基础设施的知名研究公司。“东数西算”计划于 2022 年 2 月启动，是一项国家超级工程，旨在将数据处理从发达的东部地区转移到拥有丰富可再生能源和较低温度的西部地区。超大规模企业是指像阿里巴巴、腾讯和华为这样运营大型数据中心的大型云服务提供商。该模型有助于在这些更广泛的趋势中理解中国 AI 基础设施的繁荣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://icds.ee/en/more-than-meets-the-ai-chinas-data-centre-strategy/?trk=article-ssr-frontend-pulse_little-text-block">More Than Meets the AI: China’s Data Centre Strategy - International...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/china-invested-dollar61-billion-in-a-state-data-center-project-in-two-years-the-eastern-data-western-computing-project-aims-to-utilize-the-countrys-undeveloped-land">China invested $6.1 billion in a state data center... | Tom's Hardware</a></li>
<li><a href="https://www.chinatalk.media/p/eastern-data-western-compute-is-fake">“ Eastern Data , Western Compute ” is Fake</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#China`, `#datacenters`, `#hyperscalers`, `#SemiAnalysis`

---

<a id="item-4"></a>
## [F-Droid 发布 2.0，开源安卓应用商店迎来十年来最大更新](https://f-droid.org/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html) ⭐️ 8.0/10

2026 年 9 月 24 日，F-Droid 发布了 2.0 版本，官方称这是该应用十年来最大的一次更新：界面与底层代码均被重写，整体简化为“发现、搜索、我的应用”三大区域。该版本此前经历了 14 次测试发布，并将在未来数周内向用户逐步推送。 F-Droid 是 Google Play 之外最主要的自由开源应用分发渠道，因此这次从底层到界面的重做以及发现能力的提升，直接影响依赖它来寻找无账号、无追踪应用的隐私关注用户和 FOSS 用户。搜索与目录浏览的改进，正好回应了该项目长期存在的短板——仓库不断膨胀却难以浏览。 新版搜索支持检索应用描述、分类以及翻译后的元数据，并特别加强了对中文、日文、韩文内容的搜索能力；同时引入了更顺畅的安装更新流程和后台检查更新。不过，F-Droid Privileged Extension 在 2.0 中暂不支持，Android 6（Marshmallow）也被放弃支持。

telegram · zaihuapd · 9月24日 23:58

**背景**: F-Droid 是面向 Android 的自由开源（FOSS）应用商店与软件仓库，相当于 Google Play 的替代方案，只收录自由开源应用，用户无需注册账号即可浏览、下载和安装。它还会在应用说明中标注广告、用户追踪或依赖非自由软件等“反特性”，并公开其服务端软件，允许任何人搭建自己的仓库。F-Droid Privileged Extension 则是一个可选的系统级 priv-app，能让 F-Droid 在不开启“未知来源”或无需用户每次点击“安装”的情况下安装、更新和卸载应用，通常需要 root 权限或 Shizuku 框架支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid</a></li>
<li><a href="https://f-droid.org/packages/org.fdroid.fdroid.privileged/">F - Droid Privileged Extension | F - Droid - Free and Open Source...</a></li>
<li><a href="https://github.com/f-droid/privileged-extension">GitHub - f - droid / privileged - extension : mirror of https...</a></li>

</ul>
</details>

**标签**: `#F-Droid`, `#Android`, `#Open Source`, `#App Store`, `#Privacy`

---