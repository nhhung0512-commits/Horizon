---
layout: default
title: "Horizon Summary: 2026-07-15 (ZH)"
date: 2026-07-15
lang: zh
---

> 从 36 条内容中筛选出 9 条重要资讯。

---

1. [Stripe 和 Advent 联合出价 530 亿美元收购 PayPal](#item-1) ⭐️ 9.0/10
2. [DeepSeek 首轮融资超 500 亿元，特殊架构保创始人控制权](#item-2) ⭐️ 9.0/10
3. [Telegram 推出机器人与迷你应用的无服务器平台](#item-3) ⭐️ 8.0/10
4. [Claude web_fetch 漏洞致数据泄露](#item-4) ⭐️ 8.0/10
5. [新方法解耦 InceptionV1 中的卷积神经元](#item-5) ⭐️ 8.0/10
6. [PyTorch 模型在 T4 上比 A100 慢 170 倍：极端瓶颈](#item-6) ⭐️ 8.0/10
7. [DeepSeek 计划 IPO，寻求 710 亿美元估值新融资](#item-7) ⭐️ 8.0/10
8. [法官质疑 Epic 与谷歌 8 亿美元合作影响反垄断立场](#item-8) ⭐️ 8.0/10
9. [沙盒逃逸使 Filza 可访问 iOS 27 备忘录数据库](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe 和 Advent 联合出价 530 亿美元收购 PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

据消息人士称，Stripe 和私募股权公司 Advent International 联合出价超过 530 亿美元收购 PayPal。 此次收购将整合主要支付处理商，可能减少竞争，并引发对更高费用和对商家更严格政策的担忧。 该交易将使 Stripe、PayPal、Venmo、Braintree 和 Xoom 归于同一集团，导致在线非面对面结账的赫芬达尔-赫希曼指数（HHI）非常高。

hackernews · rvz · 7月15日 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: Stripe 是领先的在线支付处理商，而 PayPal 是历史悠久的数字支付公司。Advent International 是一家全球私募股权公司。此次合并由于市场集中度而引发重大的反垄断担忧。

**社区讨论**: 评论者表达了对竞争减少、费用可能上涨以及 Stripe 限制性政策的担忧，特别是对大麻和成人行业。一些用户担心账户标记风险，并建议剥离 Venmo 和 Braintree 以通过反垄断审查。

**标签**: `#fintech`, `#acquisition`, `#payments`, `#antitrust`

---

<a id="item-2"></a>
## [DeepSeek 首轮融资超 500 亿元，特殊架构保创始人控制权](https://t.me/zaihuapd/42589) ⭐️ 9.0/10

DeepSeek 完成首轮融资，筹得超过 500 亿元人民币（约 74 亿美元），采用非常规架构，投资者需将资金投入由 CEO 梁文锋管理的有限合伙企业，接受五年锁定期且无表决权。 这一巨额融资轮表明投资者对 DeepSeek 及 AI 行业信心十足，而特殊架构确保了创始人控制权，可能影响其他 AI 实验室在融资和治理方面的做法。 创始人梁文锋个人投资 200 亿元，腾讯和宁德时代分别考虑或计划投资 100 亿元和 50 亿元，可能成为最大的外部投资者。DeepSeek 对此暂未置评。

telegram · zaihuapd · 7月15日 12:56

**背景**: 有限合伙架构在风险投资中常用于分离控制权和收益权。普通合伙人（GP）管理合伙企业并持有表决权，有限合伙人（LP）出资但不参与管理。在本案例中，投资者作为有限合伙人进入由梁文锋控制的合伙企业，使他能够在筹集大量外部资金的同时保持对 DeepSeek 的控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rbrf.xnai.edu.cn/__local/3/2C/1E/D04DD95BE51FEBBF23E8B5AFCD0_BDED923C_954AA.pdf">1 科创板公司“有限合伙”架构创新实践 及管理建议 摘要：2019 年7 月科创板开板以来，已有400 多家公司实</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/383462470">公司控制模式之三：有限合伙控制 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#DeepSeek`, `#venture capital`, `#corporate governance`

---

<a id="item-3"></a>
## [Telegram 推出机器人与迷你应用的无服务器平台](https://core.telegram.org/bots/serverless) ⭐️ 8.0/10

Telegram 正式推出了无服务器平台，开发者只需通过一条命令 npx tgcloud push 即可将机器人和 Mini App 的 JavaScript 后端代码部署到 Telegram 的基础设施上。 这通过消除服务器管理、扩容顾虑和部署复杂性，简化了机器人和 Mini App 的开发，可能吸引数百万 Telegram 用户构建更多交互式服务。 该平台在靠近 Bot API 的隔离 V8 沙箱中运行代码，并自带一个基于 SQLite 的内置数据库。然而，关于配额（执行时间、存储）和定价的细节尚未公布。

hackernews · soheilpro · 7月15日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=48918534)

**背景**: 无服务器计算允许开发者无需管理服务器即可运行代码，由云提供商处理扩容和维护。Telegram Mini App 是基于 JavaScript 和 HTML5 的 Web 应用，在 Telegram 内运行，提供交互式体验。此前，开发者需要自行托管机器人后端，或使用 AWS Lambda 等第三方无服务器提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://core.telegram.org/bots/serverless">Telegram Serverless</a></li>
<li><a href="https://core.telegram.org/bots/webapps">Telegram Mini Apps</a></li>
<li><a href="https://grokipedia.com/page/Telegram_Mini_Apps">Telegram Mini Apps</a></li>

</ul>
</details>

**社区讨论**: 社区成员表现出兴趣，但对缺失的细节提出疑问：执行时间和存储的配额、API 密钥的秘密管理、SQLite 数据库大小限制以及定价。一些人认为内置 SQLite 是个不错的特性，另一些人则希望 Signal 等其他通讯平台也能提供类似功能。

**标签**: `#Telegram`, `#serverless`, `#bot development`, `#JavaScript`, `#deployment`

---

<a id="item-4"></a>
## [Claude web_fetch 漏洞致数据泄露](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

研究员 Ayush Paul 发现了一种利用 Claude 的 web_fetch 工具漏洞的方法，通过设置蜜罐站点诱导 AI 依次访问嵌套链接，从而窃取了用户的姓名、所在城市和雇主信息。 该漏洞展示了 AI 工具设计中的关键缺陷，绕过了 Anthropic 对数据泄露的防护，突显了“致命三重奏”攻击向量持续存在的风险，即私人数据、不可信内容和工具访问结合带来的威胁。 该攻击需要用户直接要求 Claude 获取某个 URL，攻击者的网站只对包含 'Claude-User' 的 user-agent 显示恶意内容。漏洞在于 web_fetch 允许访问之前获取页面中嵌入的链接。

rss · Simon Willison · 7月15日 14:21

**背景**: “致命三重奏”指的是 AI 代理数据窃取的三个条件：访问私人数据、暴露于不可信内容和外部通信能力。Claude 的 web_fetch 工具本设计为仅导航到用户提供的精确 URL 或搜索结果以防止数据泄露，但此设计被绕过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cyera.com/research/when-language-becomes-the-attack-vector-the-lethal-trifecta-of-ai-agents">When Language Becomes the Attack Vector: The Lethal Trifecta of AI...</a></li>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#AI security`, `#Claude`, `#prompt injection`, `#data exfiltration`, `#vulnerability`

---

<a id="item-5"></a>
## [新方法解耦 InceptionV1 中的卷积神经元](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 8.0/10

一位研究人员提出了一项新技术，利用卷积神经元感受野与权重的 Hadamard 积来聚类并可视化 InceptionV1 中单个神经元检测到的所有模式，揭示了针对汽车和猫等概念的单语义聚类，以及针对字母等低值激活的聚类。 这项工作通过提供更细粒度的方法来分析卷积神经元，推动了机制可解释性发展，可能有助于我们理解神经网络在视觉模型中如何表示和组合特征。 该方法通过对 Hadamard 积进行聚类，得到高激活的单语义聚类（如汽车、狗）和低激活聚类（如字母）。对低值聚类的分析显示，下游神经元也针对同一概念激活，且正负权重均衡分布以压低求和结果，这表明梯度下降有意将概念置于噪声范围内。

reddit · r/MachineLearning · /u/narang_27 · 7月15日 06:59

**背景**: 机制可解释性旨在通过理解神经网络的内部电路和特征来对其进行逆向工程。InceptionV1（GoogLeNet）是一种经典的图像分类卷积神经网络，常在可解释性研究中使用。Hadamard 积是一种逐元素矩阵乘法，本文用它来结合感受野图像块与神经元的权重向量，以隔离神经元“看到”的内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inception_(deep_learning_architecture)">Inception (deep learning architecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_product_(matrices)">Hadamard product (matrices) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mechanistic interpretability`, `#neural network interpretability`, `#InceptionV1`, `#neuron analysis`, `#convolutional networks`

---

<a id="item-6"></a>
## [PyTorch 模型在 T4 上比 A100 慢 170 倍：极端瓶颈](https://www.reddit.com/r/MachineLearning/comments/1ux6a9x/pytorch_model_running_170x_slower_on_t4_vs_a100/) ⭐️ 8.0/10

这种极端的性能差距远超典型硬件差异，表明存在特定的算法或内核级别瓶颈，很可能与 T4 架构上的 4D 相关体积构建或内存访问模式有关。理解这一问题有助于机器学习工程师优化类似模型，避免代价高昂的部署失误。 用户已排除常见问题：GPU 利用率 99%，模型已在 GPU 上，cudnn.benchmark 无效果。模型以纯 FP32 运行，在 T4 上意味着无法利用 Tensor Core（仅在混合精度中可用），但仅此不足以解释 170 倍的减慢。4D 相关体积操作是内存密集型的，可能在 T4 较小的内存带宽（300 GB/s vs A100 的 1555 GB/s）上遭遇不良的内存合并。

reddit · r/MachineLearning · /u/Future-Structure-296 · 7月15日 13:44

**背景**: NVIDIA T4（图灵）GPU 的内存带宽约为 300 GB/s，Tensor Core 仅用于混合精度运算，而 A100（安培）提供 1555 GB/s 带宽和更大的缓存。4D 相关体积是点追踪模型（例如 TAPIR、LocoTrack）中的常用技术，涉及帧间的密集匹配，产生大量中间张量。FP32 执行与内存受限操作的结合会不成比例地损害 T4 的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.26087v1">MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation</a></li>
<li><a href="https://discuss.pytorch.org/t/how-to-calculate-the-gpu-memory-that-a-model-uses/157486">How to calculate the GPU memory that a model ... - PyTorch Forums</a></li>

</ul>
</details>

**标签**: `#PyTorch`, `#GPU Performance`, `#NVIDIA T4`, `#NVIDIA A100`, `#Model Optimization`

---

<a id="item-7"></a>
## [DeepSeek 计划 IPO，寻求 710 亿美元估值新融资](https://t.me/zaihuapd/42577) ⭐️ 8.0/10

DeepSeek 已启动首次公开募股（IPO）筹备工作，计划最早于 2025 年底或 2026 年初提交申请，目标在 2027 年上市。同时，公司正在寻求新一轮私募融资，投前估值至少为 7100 亿美元（约合 4800 亿元人民币）。 这标志着 DeepSeek 的一个重要里程碑，也显示出市场对 AI 领域的强烈信心——其估值从 6 月份首轮外部融资时的约 500 亿美元飙升至超过 7100 亿美元。此次 IPO 可能成为近年来规模最大的科技股上市之一。 该公司于 2025 年 6 月初完成了 7 亿美元的首轮外部融资，投资方包括腾讯和宁德时代。新一轮融资目标至少 100 亿元人民币，最终金额可能因投资者数量而翻数倍。相关讨论仍在进行中，计划可能根据市场情况调整。

telegram · zaihuapd · 7月15日 07:04

**背景**: DeepSeek 是一家位于杭州的中国 AI 初创公司，专注于大型语言模型和 AI 应用。该公司因其 DeepSeek-V2 等具有竞争力的模型而受到广泛关注。上市将为其提供公开市场资本，以扩大运营规模并与全球 AI 领导者竞争。

**标签**: `#DeepSeek`, `#IPO`, `#AI funding`, `#venture capital`, `#financing`

---

<a id="item-8"></a>
## [法官质疑 Epic 与谷歌 8 亿美元合作影响反垄断立场](https://t.me/zaihuapd/42588) ⭐️ 8.0/10

法官 James Donato 在一次听证会上披露，Epic Games 与谷歌达成了一项新的商业合作，Epic 将在 6 年内向谷歌支付约 8 亿美元。法官质疑该协议可能影响 Epic 在反垄断诉讼中推动 Android 生态改革的立场。 这一进展意义重大，因为它可能削弱 Epic 在针对谷歌的反垄断诉讼中的可信度，进而对移动应用商店竞争和开发者费用产生广泛影响。如果法官认定该协议损害了 Epic 的立场，可能会削弱迫使谷歌开放 Android 生态系统的案件。 该合作涉及 Unreal Engine、《堡垒之夜》及 Android 相关业务的联合产品开发、营销和伙伴关系。Epic CEO Tim Sweeney 表示，协议未包含 Epic Games Store 在 Android 平台分发的条款。

telegram · zaihuapd · 7月15日 11:15

**背景**: Epic Games 于 2020 年起诉谷歌，指控谷歌 Play 商店的政策和 30%的抽成构成非法垄断。此案与 Epic 针对苹果的诉讼类似，旨在迫使谷歌允许替代应用商店和支付系统。Epic 与谷歌最近的商业合作引发了担忧，可能表明两者关系密切，与 Epic 的公开立场相悖。

**标签**: `#antitrust`, `#Epic Games`, `#Google`, `#Android`, `#app store`

---

<a id="item-9"></a>
## [沙盒逃逸使 Filza 可访问 iOS 27 备忘录数据库](https://x.com/0xjohnny/status/2077216973256274272) ⭐️ 8.0/10

开发者 johnny 修改了 Filza 文件管理器，利用 iOS 27 beta 3 上的沙盒逃逸漏洞，使其能够在 iPhone 17 Pro Max 上访问系统的备忘录数据库。 这展示了新 iOS 版本中的一个重大安全漏洞，可能暴露敏感用户数据。它突显了 iOS 沙盒强制执行的持续挑战，可能促使苹果在正式发布前修补该漏洞。 该利用是在 iOS 27 beta 3 上使用修改版 Filza（一款用于越狱设备的流行文件管理器）进行的。该攻击绕过了应用程序容器限制，读取外部数据，特别是备忘录数据库。

telegram · zaihuapd · 7月15日 14:35

**背景**: Filza 是一款在越狱 iOS 设备上提供完整文件系统访问的文件管理器。沙盒逃逸是指突破应用程序的受限环境以访问系统数据。此类漏洞非常关键，因为它们可能导致数据窃取或恶意软件安装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ios-repo-updates.com/repository/tigisoftware/package/com.tigisoftware.filza/">Package: Filza File Manager • com.tigisoftware....</a></li>
<li><a href="https://www.tigisoftware.com/default/?page_id=78">Filza – TIGI Software</a></li>
<li><a href="https://vulners.com/thn/THN:E828782CB52567D01CA178688A53E3A6">Microsoft Details App Sandbox Escape Bug Impacting Apple iOS .</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#iOS`, `#sandbox escape`, `#vulnerability`, `#mobile security`

---