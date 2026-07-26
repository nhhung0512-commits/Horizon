---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 32 条内容中筛选出 10 条重要资讯。

---

1. [Science 调查上海医院未经授权致命基因治疗](#item-1) ⭐️ 9.0/10
2. [GrapheneOS 针对锁定设备数据提取的保护措施](#item-2) ⭐️ 8.0/10
3. [调查揭露通过 API 代理转售 LLM 代币的灰色市场](#item-3) ⭐️ 8.0/10
4. [Ruff v0.16.0 默认规则从 59 条激增至 413 条](#item-4) ⭐️ 8.0/10
5. [从头用 ARM64 汇编实现 YOLO26n 推理](#item-5) ⭐️ 8.0/10
6. [4B 开源模型在瑞典医学问答中接近 o3 水平](#item-6) ⭐️ 8.0/10
7. [IMO 2026 上对比 LLM：前沿模型表现优异，工程框架有助提升](#item-7) ⭐️ 8.0/10
8. [长鑫科技登陆上交所，有望成 A 股最大市值公司](#item-8) ⭐️ 8.0/10
9. [Claude 共享链接漏洞致用户数据泄露](#item-9) ⭐️ 8.0/10
10. [SpaceX 停止接受 2028 年后 Falcon 9 订单，全力转向 Starship](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Science 调查上海医院未经授权致命基因治疗](https://t.me/zaihuapd/42777) ⭐️ 9.0/10

《科学》杂志于 2026 年 7 月 23 日发布调查，披露一名 6 岁女童于 2025 年 3 月在上海新华医院接受未经批准的实验性碱基编辑基因治疗后死亡，院方隐瞒了该事件。 此案引发了关于人类基因编辑未经监管的严重伦理和安全担忧，可能削弱公众对基因治疗的信任，并促使全球加强监管。 该女童患有一种罕见的单碱基突变遗传病；研究团队通过脊髓液注射数万亿 AAV 病毒载体靶向脑部神经元。她在 7 天内因严重免疫反应死亡，其父母自费超过 80 万美元。

telegram · zaihuapd · 7月26日 06:01

**背景**: 碱基编辑是一种基因编辑技术，能够在不断裂双链 DNA 的情况下实现精确的单碱基转换，从而降低意外插入或缺失的风险。AAV（腺相关病毒）载体通常用于将治疗基因递送至细胞，包括中枢神经系统。ClinicalTrials.gov 是由美国国家医学图书馆维护的公开临床试验注册库。在中国，实验性疗法需经国家药品监督管理局和伦理委员会批准，而此案似乎绕过了这些程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41573-020-0084-6">Base editing: advances and therapeutic opportunities | Nature Reviews Drug Discovery</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adeno-associated_virus">Adeno-associated virus - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ClinicalTrials.gov">ClinicalTrials . gov - Wikipedia</a></li>

</ul>
</details>

**标签**: `#gene editing`, `#bioethics`, `#clinical trial`, `#Science investigation`, `#China`

---

<a id="item-2"></a>
## [GrapheneOS 针对锁定设备数据提取的保护措施](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices) ⭐️ 8.0/10

一次社区讨论强调 GrapheneOS 的先进保护措施，包括自动重启功能，使设备恢复到首次解锁前（BFU）状态，防止从锁定设备中提取密钥。 这很重要，因为 GrapheneOS 为记者和注重隐私的用户提供了更高等级的安全性，即使没有胁迫密码，也能阻止法医数据提取和边境搜查。 自动重启功能可配置为在闲置一段时间后自动重启设备，从首次解锁后（AFU）状态恢复到 BFU 状态，清除 RAM 中的加密密钥。讨论还指出图案锁仅提供约 18.57 位熵，相当于不到三个随机字符。

hackernews · Cider9986 · 7月26日 05:57 · [社区讨论](https://news.ycombinator.com/item?id=49055169)

**背景**: GrapheneOS 是一款基于 Android、注重安全性的开源移动操作系统，适用于 Google Pixel 设备。它通过大量加固措施保护用户数据。自动重启功能强制从解锁后的 AFU 状态回到锁定的 BFU 状态，此时全盘加密密钥不可用。这通过安全元件强制执行节流，使暴力破解攻击更加困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS - Wikipedia</a></li>
<li><a href="https://grapheneos.org/features">Features overview | GrapheneOS</a></li>

</ul>
</details>

**社区讨论**: 社区普遍支持自动重启功能，用户指出该功能帮助记者保护消息来源。一些评论者呼吁提供完整的备份/恢复解决方案，以便在过境前安全擦除。其他人将 GrapheneOS 与苹果的锁定模式进行有利比较，还有一位用户批评图案锁的低熵问题。

**标签**: `#security`, `#grapheneos`, `#android`, `#privacy`, `#password-entropy`

---

<a id="item-3"></a>
## [调查揭露通过 API 代理转售 LLM 代币的灰色市场](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 8.0/10

Matt Lenhard 的一项详细调查揭示了一个蓬勃发展的黑市，转售商通过 one-api 和 new-api 等开源代理软件，汇集来自免费试用、被盗信用卡和未受保护端点的 LLM API 密钥，以提供打折代币。 这个市场暴露了 LLM API 基础设施中的系统性欺诈漏洞，给提供商造成重大收入损失，并给开发者带来安全风险——他们可能无意中为滥用行为买单。这也凸显了制定严格 API 配额和加强欺诈检测的紧迫性。 这个转售市场主要基于中国，使用开源 API 代理项目 one-api 及其分支 new-api 来跨汇集凭证进行负载均衡。买家包括寻求廉价代币、绕过地理限制或收集数据用于模型蒸馏的人。

rss · Simon Willison · 7月26日 19:30

**背景**: API 中继代理充当用户和 LLM 提供商之间的中间人，支持多密钥池化和负载均衡以管理速率限制和成本。虽然存在合法用途，但欺诈者通过聚合通过滥用试用、拒付或被盗信用卡获取的凭证来利用这些工具。one-api 和 new-api 等开源工具本用于合法的多密钥管理，但可能被重新用于欺诈性代币转售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.4sapi.com/blog/api-relay-proxies-llm-cost-optimization">Cut LLM API Costs with Relay Proxies - 4sAPI Blog</a></li>
<li><a href="https://www.getmaxim.ai/articles/top-5-tools-to-tackle-rate-limiting-for-llm-apps/">Top 5 Tools to Tackle Rate Limiting for LLM Apps</a></li>

</ul>
</details>

**标签**: `#security`, `#AI`, `#fraud`, `#API`, `#LLM`

---

<a id="item-4"></a>
## [Ruff v0.16.0 默认规则从 59 条激增至 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0 于 7 月 23 日发布，将其默认规则集从 59 条扩展至 413 条，可能破坏未固定依赖的现有 CI 流水线。 这一大幅增加意味着许多 Python 项目将发现代码库中众多新问题，在提升代码质量的同时，也需要开发者立即关注并自动修复 CI。 自 v0.1.0 以来，Ruff 总规则数从 708 条增加到 968 条；新默认规则会捕获之前因缺少显式配置而遗漏的语法错误和运行时错误。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的极速 Python 代码检查器和格式化工具，将 Flake8、Black、isort 等工具的功能合并到单个二进制文件中。它由 Astral 开发，后者近期被 OpenAI 收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://docs.astral.sh/ruff/">Ruff - Astral Docs</a></li>

</ul>
</details>

**标签**: `#Python`, `#linting`, `#Ruff`, `#CI`, `#release`

---

<a id="item-5"></a>
## [从头用 ARM64 汇编实现 YOLO26n 推理](https://www.reddit.com/r/MachineLearning/comments/1v6w394/i_implemented_the_yolo26n_model_inference_from/) ⭐️ 8.0/10

一位开发者完全从零开始使用 ARM64 汇编语言和 C 语言实现了 YOLO26n 目标检测推理，不依赖任何现有深度学习框架。该实现采用了多种底层优化技术，包括 ARM NEON SIMD、Winograd 卷积、缓存感知分块和算子融合，并在 Raspberry Pi 4 上运行。 该项目展示了如何在没有重量级库的情况下，在边缘设备上对深度学习推理进行底层优化，具有重要的教育价值和高效部署潜力。这对于物联网和机器人等资源受限环境至关重要。 该实现包括自定义 ARM64 微内核、以自定义二进制格式重新设计的内存布局，以及 YOLO26n 的具体模块如 Conv、C3K2、SPPF、C2PSA、PSA、BottleNeck 和 Detect。尽管成功完成了检测，但作者指出性能提升低于预期，仍有进一步优化的空间。

reddit · r/MachineLearning · /u/Forward_Confusion902 · 7月26日 06:43

**背景**: YOLO（You Only Look Once）是流行的实时目标检测模型系列，YOLO26n 是针对边缘设备优化的变体。在 Raspberry Pi 等 ARM CPU 上高效运行推理需要精心的底层优化，因为计算和内存有限。Winograd 卷积等技术减少卷积层的乘法次数，而 ARM NEON 等 SIMD（单指令多数据）指令允许并行处理多个数据点。缓存感知分块和算子融合进一步减少内存带宽瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/winograd-convolution">Winograd Convolution in CNNs</a></li>
<li><a href="https://arxiv.org/html/2410.17725v1">YOLOv11: An Overview of the Key Architectural Enhancements</a></li>
<li><a href="https://docs.ultralytics.com/reference/nn/modules/block">nn.modules.block API Reference | Ultralytics Docs</a></li>

</ul>
</details>

**社区讨论**: Reddit 帖子因其技术深度和教育价值可能获得积极反馈，社区可能会提出进一步优化的建议。用户可能讨论替代方法或在内存布局或 SIMD 使用方面的潜在改进。

**标签**: `#YOLO`, `#ARM64`, `#Assembly`, `#Edge AI`, `#Optimization`

---

<a id="item-6"></a>
## [4B 开源模型在瑞典医学问答中接近 o3 水平](https://www.reddit.com/r/MachineLearning/comments/1v71wds/openweight_4b_models_approach_o3level_medical/) ⭐️ 8.0/10

开源 4B 模型 Gemma4-E4B 和 Qwen3.5-4B 在瑞典医学执业考试数据集 MedQA-SWE 上取得了高达 87%的准确率，接近 GPT-4（84%）和 o3（88%）的水平。 这表明小型开源模型在专业领域可以媲美更大规模的专有系统，可能使瑞典语等低资源语言的高质量医学问答变得更加普及。 Qwen3.5-4B 在启用推理后达到 87%的准确率，但其推理轨迹为英文，尽管提示是瑞典语；来自 S-GRPO 论文的早期退出干预有助于防止无限循环。

reddit · r/MachineLearning · /u/AccomplishedCat4770 · 7月26日 11:58

**背景**: MedQA-SWE 是一个基于医学执业考试构建的瑞典语临床问答数据集。小型开源模型（4B 参数）比 GPT-4 或 o3 等大型专有模型成本更低、更易获取。S-GRPO 论文提出了一种强化学习方法，使思维链推理能够提前退出，减少不必要的计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.07686">S - GRPO : Early Exit via Reinforcement Learning in Reasoning Models</a></li>
<li><a href="https://huggingface.co/datasets/nicher92/medqa-swe">nicher92/ medqa - swe · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#medical question answering`, `#reasoning`, `#LLM fine-tuning`, `#Swedish`

---

<a id="item-7"></a>
## [IMO 2026 上对比 LLM：前沿模型表现优异，工程框架有助提升](https://www.reddit.com/r/MachineLearning/comments/1v6wskz/we_compared_different_llms_on_imo_2026_r/) ⭐️ 8.0/10

一篇 Reddit 帖子在全新的 IMO 2026 题目上对比了多种大语言模型，结果表明前沿模型获得了近乎满分的成绩，而其他模型借助名为 AutoFyn 的自定义多智能体工程框架后表现显著提升。 该基准测试考察了真正的推理和多步骤问题解决能力，说明工程框架可以缩小较弱模型与前沿模型之间的差距，但无法替代核心能力，凸显了模型质量与系统设计的重要性。 前沿模型（sol、fable）无论是否使用工程框架均获得满分；Sonnet 和 Opus 在使用 Claude Code 和 AutoFyn 后从较差的 Web 应用表现提升至更高分数；最难的题目（P3）因缺少关键归约步骤，所有非前沿模型均未能解决。

reddit · r/MachineLearning · /u/pequalnp92 · 7月26日 07:21

**背景**: 国际数学奥林匹克竞赛（IMO）的题目均为全新、多步骤的数学问题，不包含在训练数据中，因此成为衡量通用智能的有力指标。工程框架是指围绕大语言模型构建结构化系统（如智能体循环、检索和验证）以提高可靠性的方法。AutoFyn 是作者开发的开源多智能体工程框架，设计为每轮以干净状态运行，能够执行长时间任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/SignalPilot-Labs/AutoFyn">GitHub - SignalPilot-Labs/AutoFyn: Run Claude in self ...</a></li>
<li><a href="https://github.com/RyanAlberts/best-of-Agent-Harnesses">GitHub - RyanAlberts/best-of-Agent-Harnesses: Curated ...</a></li>
<li><a href="https://www.decodingai.com/p/agentic-harness-engineering">Agentic Harness Engineering : LLMs as the New OS</a></li>

</ul>
</details>

**标签**: `#LLM`, `#benchmark`, `#mathematical reasoning`, `#IMO`, `#multi-agent`

---

<a id="item-8"></a>
## [长鑫科技登陆上交所，有望成 A 股最大市值公司](https://www.bloomberg.com/news/articles/2026-07-26/memory-frenzy-primes-china-champion-cxmt-for-historic-debut?srnd=phx-technology) ⭐️ 8.0/10

长鑫科技（CXMT），中国领先的 DRAM 制造商，将于 2026 年 7 月 27 日在上海证券交易所上市，此前完成了 666 亿元人民币的 IPO，这是自 2010 年以来 A 股最大的 IPO。 此次上市标志着中国半导体自主化努力的重要里程碑，因为长鑫科技是国内最先进的 DRAM IDM 公司。如果股价如分析师预期上涨，它可能超越工商银行，成为 A 股市值最高的公司。 IPO 发行价为每股 8.66 元，初始市值约 5800 亿元。散户认购部分超额 212 倍，940 万个订单共冻结约 7.07 万亿元资金。

telegram · zaihuapd · 7月26日 07:31

**背景**: DRAM（动态随机存取存储器）是一种用于计算机和服务器主存储器的半导体存储器。IDM（整合器件制造商）自行设计和制造芯片，而 fabless 公司则将生产外包。长鑫科技是一家 DRAM IDM，意味着它同时掌控设计和制造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_random-access_memory">Dynamic random-access memory - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchstorage/definition/DRAM">What is DRAM (Dynamic Random Access Memory)? How Does it Work?</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#IPO`, `#semiconductor`, `#China`, `#finance`

---

<a id="item-9"></a>
## [Claude 共享链接漏洞致用户数据泄露](https://search.brave.com/search?q=site%3Aclaude.ai%2Fshare&amp;source=android) ⭐️ 8.0/10

Claude 的共享对话链接未设置 noindex 标签，导致 Brave 和 Bing 等搜索引擎索引了敏感用户数据，暴露了 API 密钥、财务信息等。 这一隐私漏洞使任何使用搜索引擎的人都能获取高度敏感的个人和商业数据，且已有证据表明漏洞正被利用。它破坏了用户对承诺隐私的 AI 服务的信任，需要 Anthropic 紧急应对。 谷歌已屏蔽被索引的页面，但 Brave 和 Bing 仍显示结果。Anthropic 尚未修复该问题，建议用户手动删除涉及隐私的共享对话。

telegram · zaihuapd · 7月26日 11:16

**背景**: Noindex 标签是一种 HTML 元标签或 HTTP 头部，它指示搜索引擎不要将页面纳入搜索结果。如果没有这种标签，公开可访问的网页会被 Google、Brave 和 Bing 等搜索引擎自动抓取和索引。这意味着，即使页面仅供特定人员分享，任何没有 noindex 标签的 URL 上的内容都可能通过搜索查询被发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noindex">noindex - Wikipedia</a></li>
<li><a href="https://developers.google.com/search/docs/crawling-indexing/block-indexing">Block Search Indexing with noindex | Google Search Central | Documentation | Google for Developers</a></li>
<li><a href="https://www.lumar.io/blog/best-practice/noindex-disallow-nofollow/">Noindex, Nofollow & Disallow: How to Use SEO Indexing & Crawling Directives</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#Claude`, `#vulnerability`, `#AI`

---

<a id="item-10"></a>
## [SpaceX 停止接受 2028 年后 Falcon 9 订单，全力转向 Starship](https://www.bloomberg.com/news/articles/2026-07-23/spacex-is-turning-away-falcon-customers-in-major-bet-on-starship) ⭐️ 8.0/10

SpaceX 已停止接受 2028 年之后发射的 Falcon 9 新订单，并缩减了 Falcon 系列部分非重复使用部件的生产，加速向 Starship 系统过渡。 这一战略转变表明 SpaceX 决心将 Starship 作为主力运载火箭，但如果 Starship 无法在 2028 年底前投入商业运营，将使卫星运营商面临发射能力缺口。 SpaceX 可能仍会为美国国防部和 NASA 保留 Falcon 9 任务，但自 2026 年 6 月 IPO 以来，由于 Starship 测试屡遭延误，公司股价已下跌约 25%。

telegram · zaihuapd · 7月26日 12:42

**背景**: Falcon 9 是一种部分可重复使用的中型运载火箭，凭借高发射频率和低成本的拼单项目主导了商业发射市场。Starship 是正在研发的全可重复使用超重型运载器，旨在进一步降低成本并实现深空任务，但截至 2026 年 7 月，它已发射 13 次，其中 8 次成功、5 次失败，尚未投入运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9">Falcon 9 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://www.spacex.com/rideshare">SpaceX - Rideshare</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#Falcon 9`, `#commercial spaceflight`, `#launch services`

---