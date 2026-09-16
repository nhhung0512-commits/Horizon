---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 33 条内容中筛选出 2 条重要资讯。

---

1. [4B 参数模型生成的查询计划据称比 Postgres 快 81%](#item-1) ⭐️ 8.0/10
2. [Flock Safety 摄像头被曝满是漏洞和硬编码凭据](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [4B 参数模型生成的查询计划据称比 Postgres 快 81%](https://rohanbansal.com/qorl) ⭐️ 8.0/10

一位工程师在 rohanbansal.com 上发表技术文章，讲述自己如何训练一个 40 亿参数（4B）的模型来为 Postgres 生成 SQL 查询计划，并声称这些计划在内存基准测试中比 Postgres 默认计划快 81%。该文章在 Hacker News 上获得 298 个赞和 55 条评论，既有对其通俗讲解 LLM 原理的称赞，也有对基准测试设置的尖锐质疑。 查询计划生成是数据库系统中最困难的组合优化问题之一，传统上依赖人工编写的代价模型和启发式规则；如果一个小型 LLM 能胜过 Postgres 的规划器，就意味着学习型方法可能最终改变优化器的构建方式。这也体现了当前的一个趋势：把前沿大模型的能力蒸馏进可本地部署的小模型，而不是依赖庞大的托管模型。 该基准测试运行在一个可完全放入内存的 8 GB 数据集上，shared_buffers 被限制为其中一小部分，测量前还预热了缓存，并且只测试只读 SELECT 查询；批评者认为这些条件让“快 81%”这一结论很难推广到真实的 OLTP 工作负载。作者还提到，该模型是通过蒸馏一个名为 Astra 的更大前沿模型所产生的轨迹训练出来的。

hackernews · polyphilz · 9月16日 18:50 · [社区讨论](https://news.ycombinator.com/item?id=49731285)

**背景**: 数据库查询规划器负责决定一条 SQL 语句的物理执行方式——扫描哪些表、以什么顺序做连接、使用哪些索引——它通常依赖基于统计信息的代价模型和人工调优的启发式规则。学术界已经探索过 Neo 这类“学习型查询优化器”，用神经网络来构建执行计划，而不只是依赖代价模型。像 TPC-H 这样的基准测试是评估这类方案的标准手段，而 shared_buffers 是 Postgres 中控制数据库用于缓存数据页的内存大小的参数。文章中的结果依赖于类似 profile-guided optimization（基于执行反馈的优化）的方式，也就是说模型是通过实际执行反馈训练出来的，而非纯粹的静态推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vldb.org/pvldb/vol12/p1705-marcus.pdf">Neo: A Learned Query Optimizer</a></li>
<li><a href="https://www.tpc.org/tpch/">TPC-H Homepage</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍对“快 81%”的说法持怀疑态度，指出 8 GB 全内存数据集、受限的 shared_buffers、预热过的缓存以及只读 SELECT 使该基准缺乏代表性，容易过拟合到狭窄的工作负载。也有不少读者称赞文章把 LLM 的内部机制讲得让非 AI 方向的工程师也能理解；另一些人则认为对于这种数学密集的问题，LLM 只是“钝器”，AlphaGo 式的学习型启发式规则或即时索引（just-in-time index）可能是更好的方向；还有人担心生产环境中的失败模式，以及公开承认蒸馏闭源前沿模型可能招来麻烦。

**标签**: `#databases`, `#query-optimization`, `#llm`, `#postgresql`, `#machine-learning`

---

<a id="item-2"></a>
## [Flock Safety 摄像头被曝满是漏洞和硬编码凭据](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

黑客与安全研究员 Micah Lee 披露，Flock Safety 的警方监控摄像头存在严重安全漏洞，包括硬编码凭据以及糟糕的安全启动（secure boot）与密钥管理实践，相关技术分析由 Wired 和 micahflee.com 发布。Distributed Denial of Secrets 还公开了受影响 ALPR 摄像头的分区镜像。 这些缺陷意味着任何能物理接触到公共空间摄像头的人都可能提取数据或凭据，从而动摇人们对这套本就因大规模车牌识别追踪和警方滥用记录而备受争议的监控系统的信任。这也加剧了关于 AI 监控厂商如何处理安全与漏洞披露的争论。 这些摄像头似乎依赖现成的硬件和软件栈，被提取的数据据报道也没有经过适当的加密，因此未授权者只要走到设备旁就可能直接拿走；Flock 的漏洞披露政策也被批评为徒有其表，其中还包含一项例外条款，把需要“与设备交互”或下载数据的情形排除在外。

hackernews · driverdan · 9月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: Flock Safety 生产的太阳能摄像头安装在街道和公路旁的立杆上，利用自动车牌识别（ALPR）和 AI 帮助执法部门识别车辆，并已与全美众多警察部门合作。硬编码凭据是一种众所周知的弱点（编号 CWE-798），指密码、API 密钥或加密密钥被直接写死进源代码、配置文件或固件中，而非安全地存储。当设备部署在无防护的公共空间时，攻击者的威胁模型实际上就包含本地物理接触，这使得这类内嵌密钥尤其危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/home/security/when-flock-comes-to-town-how-these-ai-cameras-work-and-what-to-do-about-them/">When Flock Comes to Town: How These AI Cameras Work... - CNET</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/798.html">CWE - CWE-798: Use of Hard - coded Credentials (4.20)</a></li>
<li><a href="https://www.securityscientist.net/blog/12-questions-and-answers-about-hardcoded-credentials-in-code/">12 Questions and Answers About hardcoded credentials in code</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者普遍持批评态度：有人称 Flock 的漏洞披露政策只是做样子，表面欢迎报告，但一旦需要与设备交互就不算数；有人把这些缺陷归因于“偷懒”和压缩上市时间，忽视了包含物理接触的威胁模型；还有人认为这正体现了“快速行动、打破常规”的风险投资式监控的必然结果，并指出该报道是与 404 Media 合作的。

**标签**: `#security`, `#privacy`, `#surveillance`, `#vulnerability-disclosure`, `#iot`

---