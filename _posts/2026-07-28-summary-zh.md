---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 34 条内容中筛选出 12 条重要资讯。

---

1. [PNAS 研究：到 2025 年过半学术论文受 LLM 影响](#item-1) ⭐️ 9.0/10
2. [月之暗面寻求更多英伟达 Blackwell 芯片用于下一代模型](#item-2) ⭐️ 9.0/10
3. [Sebastian Raschka 详解 Kimi K3 的 NoPE 架构](#item-3) ⭐️ 8.0/10
4. [HIV 疫苗“课程”方法在临床前研究中取得成功](#item-4) ⭐️ 8.0/10
5. [Kimi Linear：新注意力架构超越全注意力](#item-5) ⭐️ 8.0/10
6. [Moonshot 发布 2.8 万亿参数 Kimi K3 开放权重模型](#item-6) ⭐️ 8.0/10
7. [NeurIPS 审稿人指出 AI 生成的回复](#item-7) ⭐️ 8.0/10
8. [NeurIPS 2026 AI 生成评审引发伦理争议](#item-8) ⭐️ 8.0/10
9. [NeurIPS 提示注入引发伦理担忧](#item-9) ⭐️ 8.0/10
10. [中国兴起 AI 人脸租赁市场 一季度超 95% 微短剧使用 AI](#item-10) ⭐️ 8.0/10
11. [深圳推出全国首创无人车地铁配送模式](#item-11) ⭐️ 8.0/10
12. [交易所要求券商统一改用广域网行情线路](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PNAS 研究：到 2025 年过半学术论文受 LLM 影响](https://www.reddit.com/r/MachineLearning/comments/1v93q78/pnas_over_half_of_all_academic_articles_now_show/) ⭐️ 9.0/10

一项发表在 PNAS 上的研究分析了 730 万篇学术论文，发现到 2025 年，超过 50%的文章显示出 LLM 影响的证据，这是对学术出版中 AI 渗透程度最大规模的实证量化。 该研究提供了首个权威的量化指标，显示 LLM 如何彻底重塑了科学写作，并对低声望和非英语机构在采纳中的不平等现象具有重要的政策意义。 LLM 的采用偏向于低声望和非英语机构，这突显了学术出版中 LLM 使用不平等的新政策维度。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 7月28日 16:38

**背景**: 大型语言模型（LLM）如 GPT-4 已被广泛用于生成和润色文本，包括学术写作。这项研究是迄今为止最大规模的实证调查，分析了 730 万篇论文，以量化已发表研究中 LLM 影响的程度。

**社区讨论**: Reddit 社区表现出浓厚兴趣，最热评论指出不平等角度（采用偏向低声望和非英语机构）是一个新的政策维度。提供的评论中没有详细的辩论。

**标签**: `#LLM`, `#academic publishing`, `#AI impact`, `#empirical study`, `#inequality`

---

<a id="item-2"></a>
## [月之暗面寻求更多英伟达 Blackwell 芯片用于下一代模型](https://www.theinformation.com/articles/chinese-ai-startup-moonshot-seeks-nvidia-blackwell-chips-next-model) ⭐️ 9.0/10

据报道，中国 AI 初创公司月之暗面（Moonshot）正为其下一代模型寻求更多英伟达 Blackwell 系列芯片。此前白宫指控该公司通过泰国获取 GB300 服务器训练 Kimi K3 模型，违反了美国出口管制。 这一事态凸显了中美在先进 AI 芯片上的技术紧张局势加剧，可能影响中国 AI 模型的开发，并促使出口管制更严格执行。其结果可能影响全球 AI 供应链和竞争格局。 GB300 属于 NVIDIA Blackwell Ultra 系列，是一个机架级液冷系统，包含 72 个 Blackwell Ultra GPU 和 36 个 Grace CPU。月之暗面的 Kimi K3 模型据称已使用非法获取的 GB300 服务器进行训练，而该公司现正为下一代模型寻求更多芯片。

telegram · zaihuapd · 7月28日 13:52

**背景**: NVIDIA 的 Blackwell 架构于 2024 年发布，2025 年升级为 Blackwell Ultra，专为大规模 AI 工作负载设计，并受美国贸易规则严格限制对华出口。月之暗面是一家知名的中国 AI 初创公司，开发大型语言模型，并因涉嫌规避出口管制而成为焦点。美国政府加强了对 AI 芯片流向中国的审查，针对疑似规避限制的公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">NVIDIA GB300 NVL72</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/nvidia-blackwell-architecture-deep-dive-a-closer-look-at-the-upgrades-coming-with-rtx-50-series-gpus">Nvidia Blackwell architecture deep dive: A closer... | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#AI`, `#semiconductors`, `#export controls`, `#Moonshot`, `#NVIDIA Blackwell`

---

<a id="item-3"></a>
## [Sebastian Raschka 详解 Kimi K3 的 NoPE 架构](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html) ⭐️ 8.0/10

Sebastian Raschka 发布了对 Kimi K3 架构的详细解析，指出该模型完全移除了所有 RoPE（旋转位置嵌入）层，并全面采用 NoPE（无位置嵌入）。 这一架构选择挑战了长期以来认为显式位置编码对 Transformer 模型必不可少的假设，表明注意力机制可以隐式学习位置信息。在拥有 100 万上下文的最先进模型中成功采用 NoPE 可能影响未来大语言模型的设计。 Kimi K3 采用了混合注意力机制，将 Kimi Delta Attention（KDA）层与门控多头潜在注意力（MLA）相结合。与传统的通过添加正弦位置信号的 RoPE 不同，NoPE 被应用于每一层，完全依靠注意力输出来编码 token 位置。

hackernews · ModelForge · 7月28日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49085698)

**背景**: 像 RoPE 这样的位置嵌入是现代大语言模型中的标准组件，用于帮助模型理解 token 顺序。NoPE（无位置嵌入）是一种替代方案，它移除显式的位置信息，迫使注意力机制从数据中推断序列顺序。最近的研究，例如 SmolLM3 中每四层丢弃一次 RoPE 的混合方法，表明 NoPE 可以在降低复杂度的同时有效进行长上下文建模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2501.18795v1">Rope to Nope and Back Again: A New Hybrid Attention Strategy</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/nope/">No Positional Embeddings (NoPE) | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**社区讨论**: 评论者对完全移除位置嵌入居然能有效工作感到惊讶，有人询问没有位置归纳偏置是否会导致模型变成“token 汤”。其他人则称赞了 Sebastian Raschka 的分析，并将这一架构选择与 Kimi K3 在编码和多模态任务中的强大实际表现联系起来。

**标签**: `#LLM`, `#architecture`, `#Kimi`, `#NoPE`, `#technical analysis`

---

<a id="item-4"></a>
## [HIV 疫苗“课程”方法在临床前研究中取得成功](https://www.lji.org/news-events/news/post/new-hiv-vaccine-shows-unprecedented-success-in-preclinical-study/) ⭐️ 8.0/10

一种通过一系列注射逐步训练免疫系统产生广谱中和抗体的新型 HIV 疫苗，在猴子临床前研究中显示出前所未有的成功。 这标志着向有效 HIV 疫苗迈出了重要一步，由于病毒快速变异，这一目标几十年来一直难以实现。如果人体试验证实了结果，它可以补充现有的预防工具（如 PrEP），并有助于减少全球 HIV 传播。 该疫苗采用种系靶向策略，每次注射呈现略有不同的免疫原以引导 B 细胞成熟，详情见 Nature 论文（DOI: 10.1038/s41586-026-10837-5）。I 期人体试验已在进行中，但过去的经验表明许多 HIV 疫苗在这一阶段失败。

hackernews · codebyaditya · 7月28日 13:12 · [社区讨论](https://news.ycombinator.com/item?id=49083314)

**背景**: HIV 是一种高度突变的病毒，能逃避免疫系统，使得疫苗开发困难。广谱中和抗体（bnAbs）可以靶向 HIV 的保守区域，但诱导它们需要精确地引导 B 细胞通过多个发育阶段，这一概念称为种系靶向和序贯免疫。这种方法模拟了一种自然的“课程”，逐步训练免疫系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41590-024-01852-7">Germline-targeting immunogens guide bnAb development - Nature</a></li>
<li><a href="https://www.cell.com/immunity/fulltext/S1074-7613(26)00123-8">Germline-targeting HIV immunogen induces cross-neutralizing ...</a></li>
<li><a href="https://www.science.org/doi/10.1126/sciimmunol.adk9550">Germline-targeting HIV vaccination induces neutralizing ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对“课程”概念感到着迷，但也表达了谨慎，指出许多 HIV 疫苗在人体试验中失败。一位用户认为现有的 PrEP 能有效预防传播，主张更广泛地分发 PrEP 而不是依赖未来的疫苗。另一位用户提供了原始论文和独立分析的链接，敦促读者不要盲目相信新闻稿。

**标签**: `#HIV`, `#vaccine`, `#immunology`, `#biotechnology`, `#preclinical`

---

<a id="item-5"></a>
## [Kimi Linear：新注意力架构超越全注意力](https://arxiv.org/abs/2510.26692) ⭐️ 8.0/10

Moonshot AI 推出了 Kimi Linear，一种混合线性注意力架构，在短上下文、长上下文和强化学习缩放场景中均优于全注意力，并开源了其 KDA 内核和 vLLM 实现以及模型检查点。 这项创新表明线性注意力在表达力和效率上可以超越全注意力，有可能在保持或提升性能的同时降低大型语言模型的计算成本。它已在 2.8 万亿参数的 Kimi K3 模型中得到规模化应用，显示出实际影响力。 Kimi Linear 采用 3:1 的 Kimi Delta Attention (KDA) 层与全多头潜在注意力 (MLA) 层交错，在成本和表达力之间取得最佳平衡。开源版本包括 KDA 内核、vLLM 支持以及预训练和指令微调检查点。

hackernews · ronfriedhaber · 7月28日 10:52 · [社区讨论](https://news.ycombinator.com/item?id=49082022)

**背景**: 传统 Transformer 依赖全自注意力机制，其复杂度随序列长度呈二次增长，导致长上下文处理成本高昂。线性注意力旨在降低复杂度同时保持表达力。Kimi Linear 是一种混合架构，结合了线性注意力层和全注意力层，在多种基准测试上表现强劲。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://arxiv.org/pdf/2510.26692">KIMI LINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**社区讨论**: 社区参与度很高，专家们将 Kimi Linear 与 Gated Deltanet 2 等其他架构进行比较，并给予好评，同时注意到其开源发布和被集成到 Kimi K3。一些人讨论了规模带来的智能涌现，另一些人则对开源贡献促进进一步研究表示兴奋。

**标签**: `#attention architecture`, `#deep learning`, `#open-source`, `#transformer`, `#LLM`

---

<a id="item-6"></a>
## [Moonshot 发布 2.8 万亿参数 Kimi K3 开放权重模型](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 8.0/10

Moonshot AI 已在 Hugging Face 上发布了其 2.8 万亿参数的 Kimi K3 模型权重，采用修改后的许可证。该模型大小为 1.56TB，可立即下载和推理。 此次发布标志着有史以来公开可用的最大开放权重模型之一，为 AI 社区提供了巨大的能力。随附的许可证变更要求大型 Model-as-a-Service 企业另行签订协议，为开放权重模型的商业使用树立了令人瞩目的先例。 该许可证不再称为“修改后的 MIT”，而是要求任何年收入超过 2000 万美元且运营 Model-as-a-Service 业务的企业另签协议。OpenRouter 已通过七家提供商提供 Kimi K3，定价与 Moonshot 自身一致，即输入每百万 token 3 美元、输出每百万 token 15 美元。

rss · Simon Willison · 7月27日 23:39

**背景**: Kimi K3 是 Moonshot AI（一家中国人工智能公司）开发的大型语言模型。它延续了之前的 K2 模型，该模型也使用了修改后的开放许可证。术语“开放权重”指的是模型训练后的神经网络权重被公开发布，但通常不包含训练数据、代码和方法论。这使其与完全开源模型有所区别。

**标签**: `#AI`, `#large language model`, `#open source`, `#Hugging Face`

---

<a id="item-7"></a>
## [NeurIPS 审稿人指出 AI 生成的回复](https://www.reddit.com/r/MachineLearning/comments/1v90r9r/neurips_2026_reviewer_aigenerated_rebuttals_and/) ⭐️ 8.0/10

一位 NeurIPS 2026 审稿人报告称，一篇提交的论文及其回复完全由大型语言模型生成，并特别识别出类似 Claude 的写作风格。 这一事件凸显了人们对 AI 生成内容破坏学术同行评审诚信的日益担忧，可能削弱对会议出版物和评审过程的信任。 审稿人指出，作者在检查表中承认使用了 LLM 辅助，但认为 AI 生成的风格难以解读且表明努力不足。该帖既是吐槽，也是寻求处理此类情况的建议。

reddit · r/MachineLearning · /u/gateofptolemy · 7月28日 14:52

**背景**: 大型语言模型如 Claude 和 GPT 能生成连贯文本，导致学术出版中出现“AI 垃圾”——语言通顺但缺乏原创研究的论文。同行评审是自愿无偿的工作，本已面临容量问题，AI 生成内容进一步加重了审稿人的负担。像 NeurIPS 这样的会议虽有伦理指南，但执行仍具挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiblewmymind.substack.com/p/claude-skills-ai-write-like-you">The Claude Skills That Finally Made AI Write Like Me (And How to Build Yours)</a></li>
<li><a href="https://alitu.com/creator/content-creation/ai-writing-claude-styles/">Make Your AI Writing Sound More Like You, with Claude Writing Styles</a></li>
<li><a href="https://easternherald.com/2026/05/17/arxiv-ai-slop-ban-researchers-policy-2026/">arXiv Bans AI Slop Papers with One-Year Penalty Rule</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#peer review`, `#NeurIPS`, `#LLM`, `#academic publishing`

---

<a id="item-8"></a>
## [NeurIPS 2026 AI 生成评审引发伦理争议](https://www.reddit.com/r/MachineLearning/comments/1v8vuae/neurips_2026_aigenerated_reviews_d/) ⭐️ 8.0/10

一个 Reddit 讨论揭示了 NeurIPS 2026 会议上 AI 生成同行评审的担忧，作者注意到提示注入被用于测试 LLM 滥用，许多评审看起来是直接从语言模型复制而来，缺乏人工审查。 这破坏了顶级机器学习会议同行评审过程的诚信，可能导致不公平的评价，并侵蚀对学术评审的信任。 作者提到，审稿人和元审稿人可能都依赖 LLM，提示注入被用作一项研究来检测这种滥用，但关于审稿人应承担何种后果仍存在疑问。

reddit · r/MachineLearning · /u/bricklerex · 7月28日 11:34

**背景**: 提示注入是一种网络安全攻击，通过恶意输入覆盖模型的指令以引发非预期行为，常用于绕过安全过滤器。在同行评审中，审稿人可能使用 LLM 生成评审，提示注入可用来检测评审是否由 AI 生成，例如嵌入人类不会注意到但 LLM 会遵循的隐藏指令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#peer review`, `#NeurIPS`, `#LLM misuse`, `#academic integrity`

---

<a id="item-9"></a>
## [NeurIPS 提示注入引发伦理担忧](https://www.reddit.com/r/MachineLearning/comments/1v955f6/neuripsside_prompt_injection_triggering_ethics/) ⭐️ 8.0/10

NeurIPS 会议组织者秘密使用提示注入技术来检测 LLM 生成的同行评审，但伦理评审员未被告知此次操纵，导致伦理问题被标记。 这一事件削弱了顶级 AI 会议同行评审过程的信任，凸显了在不透明或未征得评审员同意的情况下使用隐蔽技术措施的伦理风险。 提示注入被嵌入会议端以捕捉自动生成的评审，但本应监督伦理实践的伦理评审员却被蒙在鼓里，导致混乱和潜在的利益冲突。

reddit · r/MachineLearning · /u/dontknowwhattoplay · 7月28日 17:28

**背景**: 提示注入是一种安全利用手段，通过恶意或意外输入使 LLM 行为偏离设计意图。在此案例中，NeurIPS 组织者将其用作检测 LLM 生成评审的工具，引发了关于学术同行评审中知情同意和伦理监督的质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>

</ul>
</details>

**标签**: `#NeurIPS`, `#prompt injection`, `#ethics`, `#AI conference`, `#peer review`

---

<a id="item-10"></a>
## [中国兴起 AI 人脸租赁市场 一季度超 95% 微短剧使用 AI](https://restofworld.org/2026/china-ai-microdramas-face-licensing/) ⭐️ 8.0/10

中国 AI 人脸授权市场快速增长，超过 95%的微短剧使用 AI，相关法律纠纷激增。

telegram · zaihuapd · 7月28日 03:03

**标签**: `#AI`, `#face licensing`, `#microdramas`, `#China`, `#regulation`

---

<a id="item-11"></a>
## [深圳推出全国首创无人车地铁配送模式](https://www.sohu.com/a/1055801763_121613636) ⭐️ 8.0/10

这一创新显著降低了同城物流成本并提升效率，为城市物流树立了新标杆。它展示了自动驾驶车辆与公共交通基础设施的实用整合，为可扩展的智慧城市物流解决方案铺平了道路。 2026 年 4 月，深圳向功能型无人车开放了夜间跨区路权。京东物流已投放近百台无人车，覆盖 22 个网点，开通 121 条夜间配送线路。这些车辆依据当地法规被归类为“功能型无人车”（低速无人车）。

telegram · zaihuapd · 7月28日 10:46

**背景**: 功能型无人车是一种低速自动驾驶车辆，专为物流、环卫和巡检等场景设计，通常在非机动车道或专用道路上运行。在中国，它们需要地方政府发放特殊许可和路权。“无人车+地铁”模式利用地铁快速跨区运输，克服了地面无人车的续航和速度限制，实现了低成本的长距离同城配送。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tmtpost.com/6296729.html">tmtpost.com/6296729.html</a></li>
<li><a href="https://finance.sina.com.cn/roll/2026-05-23/doc-inhyuwef7546990.shtml">广东深圳无人车获批“夜间路权” 物流运输降本增效</a></li>
<li><a href="https://www.dutenews.com/n/article/10126082">行业迎爆发前夜！ 深圳 无 人 车 单月狂送90...</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#last-mile delivery`, `#logistics`, `#smart city`

---

<a id="item-12"></a>
## [交易所要求券商统一改用广域网行情线路](https://mp.weixin.qq.com/s/ba7Rx5VCnYnzJzWMHyLoaQ) ⭐️ 8.0/10

交易所要求所有券商将行情接入方式从局域网（LAN）统一变更为广域网（WAN），原有局域网线路将于本月底关闭。新要求规定广域网线路双向时延不得高于 2 毫秒。 这一变更对交易基础设施影响重大，迫使券商升级网络连接，可能影响对延迟敏感的交易策略。同时，行情数据分发集中化，可能改变高频交易者及依赖局域网托管的小型机构的竞争格局。 交易所的托管机房此前提供局域网连接以实现超低延迟，现改为广域网线路，且必须满足严格的 2 毫秒往返时延要求。该要求适用于存量和新增广域网线路，局域网关闭时间定于本月底。

telegram · zaihuapd · 7月28日 11:31

**背景**: 在金融交易中，网络延迟至关重要，尤其是高频交易公司通过托管获得速度优势。交易所机房内的局域网连接提供最低延迟，而广域网线路由于距离更长通常延迟更高。交易所决定统一使用广域网，简化了基础设施，但可能增加此前使用局域网机构的延迟，不过 2 毫秒的上限旨在将延迟控制在可接受范围内。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/s/NiceNews345/27543">Nice News Channel – Telegram</a></li>
<li><a href="https://www.yicai.com/brief/103295227.html">券商接到“广域网交易行情线路技术要求”通知</a></li>

</ul>
</details>

**标签**: `#financial trading`, `#brokerages`, `#exchange`, `#network infrastructure`

---