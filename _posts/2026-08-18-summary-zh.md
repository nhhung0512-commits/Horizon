---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 29 条内容中筛选出 5 条重要资讯。

---

1. [Qwen 3.8 27B 在智能指数上追平 GPT-5.6 Luna](#item-1) ⭐️ 9.0/10
2. [亚马逊税：广告霸占搜索结果，消费者信任流失](#item-2) ⭐️ 8.0/10
3. [用 20 美元工具和弹簧针修复变砖的 Framework 笔记本 BIOS](#item-3) ⭐️ 8.0/10
4. [谷歌在拍卖中收购破产精神航空的客户数据](#item-4) ⭐️ 8.0/10
5. [中国要求部分政府机构提前卸载定制版 Windows 10](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen 3.8 27B 在智能指数上追平 GPT-5.6 Luna](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 9.0/10

Qwen 3.8 27B 在 Artificial Analysis 智能指数上取得 52 分，追平了 GPT-5.6 Luna（最大值），并且仅比 GLM-5.2（最大值）和 DeepSeek V4 Pro 0813（最大值）低 1 分。对于一个 270 亿参数的模型来说，这是一个非常高的分数。 一个 27B 的开源权重模型在智能水平上追平了体积大得多的闭源模型，标志着效率上的重大突破。这可能降低硬件门槛并改变部署强大 AI 的经济性，进而影响开源和商业模型的开发方向。 Artificial Analysis 智能指数是一个由九项评估组成的综合指标，涵盖推理、编程、科学推理和多步任务。Qwen 3.8 是一个原生视觉-语言模型，支持灵活思考控制；27B 级模型在 BF16 下大约需要 56GB 显存，FP8 下约 28GB，4-bit 量化下约 14–16GB（不含 KV cache）。

rss · Simon Willison · 8月17日 23:58

**背景**: Artificial Analysis 智能指数是一个综合基准，用于衡量模型在推理、编程、知识、指令跟随、科学推理和多步任务等方面的能力。以往，要获得顶尖分数通常需要数千亿甚至万亿参数的模型，例如 GLM-5.2（753B）和 DeepSeek V4 Pro（1.7T）。Qwen 3.8 27B 是 Qwen 团队推出的开源权重模型，其接近顶尖的分数表明高效的较小模型正在缩小与前沿规模系统的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B-FP8">Qwen/Qwen3.8-27B-FP8 · Hugging Face</a></li>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026">Qwen 3.8 27B: Specs, Hardware Requirements, and How to Run It (2026) | Yotta Labs</a></li>

</ul>
</details>

**标签**: `#ai`, `#generative-ai`, `#llms`, `#qwen`, `#benchmark`

---

<a id="item-2"></a>
## [亚马逊税：广告霸占搜索结果，消费者信任流失](https://seths.blog/2026/08/the-amazon-tax/) ⭐️ 8.0/10

Seth Godin 在 2026 年 8 月的博客文章《The Amazon tax》中指出，亚马逊广告泛滥的搜索结果相当于向消费者征收“税”，利用用户对平台的信任来牟利。这篇文章引发了对广告位与平台激励机制的广泛讨论。 这凸显了电商搜索从“帮用户找商品”转向“赚取广告收入”的变化，而这种趋势在大型平台中已普遍存在。一旦信任流失，消费者可能转向本地商店或 Etsy 等替代渠道，进而威胁亚马逊的核心零售业务。 有评论者称，亚马逊搜索结果中约四分之三是赞助广告，即使明确查找某件商品也如同穿越广告雷区。Godin 认为，这些广告的成本就是用户暗中支付的“税”——包括注意力、更高的价格以及日益下降的推荐质量；另有评论指出，仅搜索广告收入就足以给每位员工发放 3.5 万美元现金奖金后仍有剩余。

hackernews · herbertl · 8月18日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49345263)

**背景**: 亚马逊的 A9 搜索算法本应将用户查询与最相关的商品 listing 进行匹配，但如今自然结果中混入了大量 Sponsored Products 广告。卖家通过实时广告竞价购买搜索结果的显眼位置，而这类广告成本最终往往被计入商品价格。这种“相关性+广告”的混合模式，正是用户如今几乎每次搜索都会看到推广产品的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sell.amazon.com/advertising/sponsored-products">Sponsored Products | Sell on Amazon</a></li>
<li><a href="https://sellermetrics.app/amazon-a9-algorithm/">Amazon A 9 Algorithm : How it Works & How to Master it</a></li>
<li><a href="https://eleverze.com/blog/amazon-ppc-complete-guide-2026-how-the-ad-auction-system-works-and-how-to-set-up-winning-campaigns/">Amazon PPC Guide 2026: How the Ad Auction System Works...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍批评亚马逊的搜索体验，有人说该平台“在搜索方面几乎完全不可用”，也有人因质量明显下滑而考虑注销使用了 15 年的账户。也有反驳意见认为这就是广告的运作方式，广告商品、亚马逊的便捷和退货服务仍有价值，用户可以选择去别处购买。

**标签**: `#Amazon`, `#E-commerce`, `#Advertising`, `#Search`, `#Platform economics`

---

<a id="item-3"></a>
## [用 20 美元工具和弹簧针修复变砖的 Framework 笔记本 BIOS](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) ⭐️ 8.0/10

2026 年 8 月，quantum5.ca 上的一篇详细指南展示了如何用约 20 美元的现成工具（包括 SPI 编程器和弹簧针）重写 BIOS 闪存芯片，从而修复变砖的 AMD 7040 系列 Framework 13 笔记本。由于 Framework 没有提供简便的恢复途径，作者选择直接接触芯片而非焊接。 这件事很重要，因为 BIOS 更新失败仍然很常见，在厂商缺乏内置恢复机制时，一台原本完好的笔记本可能会因此变成电子垃圾。该指南为可维修性主张提供了有力案例，也引发了对固件更新缺陷法律责任问题的讨论。 维修过程中没有焊接，而是用弹簧针接触 BIOS 芯片，因为 Framework 选择不焊接调试排针；有评论指出官方 FrameworkDebugger 的 JSPI 接口其实存在，但出于成本原因未贴片。文章还对比了戴尔和惠普的恢复功能，例如 USB 恢复和 HP Sure Start。

hackernews · jp_sc · 8月18日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49345220)

**背景**: BIOS（基本输入输出系统）是操作系统加载前初始化计算机硬件的固件；如果 BIOS 更新中断或损坏，闪存芯片可能无法引导，也就是常说的“变砖”。维修人员通常使用带测试夹或弹簧针的 SPI 编程器直接重写固件芯片。Framework Laptop 13 是一款模块化、可维修的笔记本，但这次案例表明它的 BIOS 恢复选项比某些其他 PC 厂商更有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/">Fixing a bricked AMD 7040 series Framework 13” laptop with $20 tools</a></li>
<li><a href="https://community.frame.work/t/bios-guide/4178">BIOS guide - Framework Laptop 13 - Framework Community</a></li>
<li><a href="https://www.accio.com/plp/bios-programmer-for-laptop">Bios Programmer for Laptop : Fast & Reliable</a></li>

</ul>
</details>

**社区讨论**: 评论区的讨论热烈且不乏批评：有人主张此类案例应诉诸小额索赔法庭，因为 Framework 有缺陷的固件导致设备变砖；还有人讲述了 ThinkPad Nano 类似变砖经历，认为厂商普遍不重视。另一些评论指出官方 JSPI 调试接口确实存在但未贴片，认为安装官方更新应延长保修，也有用户表示现在有些后悔购买 Framework 笔记本。整体情绪介于技术支持与对整个行业做法的不满之间。

**标签**: `#hardware`, `#BIOS`, `#Framework-laptop`, `#repair`, `#embedded`

---

<a id="item-4"></a>
## [谷歌在拍卖中收购破产精神航空的客户数据](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962) ⭐️ 8.0/10

谷歌在拍卖会上收购了已倒闭的美国精神航空公司的客户和运营数据，据称用于人工智能目的。该收购包括约 1 亿封电子邮件和 5 亿条微软 Teams 消息，以及其他记录。 此次收购引发了严重的隐私担忧，因为数百万旅客的个人数据在未经明确同意的情况下被重新用于人工智能训练。这也凸显了破产企业的数字资产已成为科技巨头眼中的宝贵商品。 该数据集包括超过 3000 万条客服通话录音、1500 万条客服聊天记录、1700 万个 OneDrive 文件和 2050 万个 SharePoint 项目。合同要求由“去标识化代理”在数据送达谷歌前移除个人身份信息，但评论者质疑这一过程能否彻底完成。

hackernews · pseudolus · 8月18日 10:13 · [社区讨论](https://news.ycombinator.com/item?id=49343559)

**背景**: 精神航空是一家美国航空公司，后来申请破产并最终停止运营。当一家公司倒闭时，其剩余资产（包括数字记录）可以通过拍卖出售以偿还债权人。如今，这类数据对人工智能开发者越来越有吸引力，用于训练模型，尽管这种做法引发了尚未解决的法律和伦理问题。

**社区讨论**: 评论者对去标识化过程表示怀疑，有人说他们怀疑这些数据是否真的都被去除了个人身份信息。其他人对这种规模庞大的个人信息竟然被视为可出售资产感到不安，还有人质疑所获数据的详细分解是否过于异常。

**标签**: `#AI`, `#data privacy`, `#data acquisition`, `#Google`, `#airline`

---

<a id="item-5"></a>
## [中国要求部分政府机构提前卸载定制版 Windows 10](https://www.bloomberg.com/news/articles/2026-08-18/china-axing-microsoft-windows-from-state-agencies-ahead-of-plan) ⭐️ 8.0/10

中国国家安全部已要求部分政府相关机构卸载定制版 Windows 10 系统，将原定 2027 年 2 月的停用计划提前了数月。微软表示，未发现影响该产品的安全事件，该产品仍在定期获得安全更新。 此举加速了中国政府推动减少对微软软件依赖的进程，反映出日益增强的数据安全担忧。这可能对微软在中国公共部门的市场地位以及更广泛的政府 IT 采购政策产生深远影响。 该指令据称源于数据安全担忧，但未披露具体漏洞。该定制版 Windows 10 由微软中国与神州网信联合开发，专供中国政府机构使用。

telegram · zaihuapd · 8月18日 06:22

**背景**: 定制版 Windows 10 通常被称为“政府版”，由微软中国与神州网信联合开发，以满足中国政府在安全和监管方面的要求。中国政府此前计划在 2027 年 2 月前逐步停用该系统，而新指令将部分时间表提前。这体现了中国在敏感领域推广国产软件、减少对外国技术依赖的更大趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/times001/820430">电报时报 – Telegram</a></li>

</ul>
</details>

**标签**: `#policy`, `#Microsoft`, `#Windows 10`, `#cybersecurity`, `#government IT`

---