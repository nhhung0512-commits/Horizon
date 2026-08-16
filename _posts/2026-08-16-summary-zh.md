---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 26 条内容中筛选出 3 条重要资讯。

---

1. [Anthropic 公开发布 Claude 系统提示词，提升开发者透明度](#item-1) ⭐️ 8.0/10
2. [重新审视 ECA-Net：对通道注意力设计的概念性批评](#item-2) ⭐️ 8.0/10
3. [Anthropic 第二季营收暴涨 14 倍，突破 115 亿美元](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 公开发布 Claude 系统提示词，提升开发者透明度](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 已在其平台文档中公开发布 Claude 模型使用的系统提示词，使开发者能够查看和分析影响模型行为的具体指令。这标志着 Anthropic 在模型引导方式上迈出了罕见的透明度一步。 这让开发者和研究人员能够直接了解 Claude 的安全边界和优先事项，从而更深入地分析模型行为和发展路线。同时，在一个这类细节通常被保密的行业中，这也为 AI 透明度树立了先例。 已发布的系统提示词包括 Claude 如何处理图像、危机情况和任务完成的指令。社区成员 Simon Willison 建立了 Git 提交历史来追踪模型版本之间的变化，例如加入了 Claude Fable 5 和 Claude Mythos 5 的相关引用。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 系统提示词是在用户输入之前给大型语言模型的基础指令，用来定义语气、规则和行为。传统上，主要 AI 实验室都对这些提示词保密，因此 Anthropic 的公开提供了对 Claude 塑造方式的一次难得内部视角。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@david.p.lemon79/system-prompts-explained-how-ai-models-actually-work-behind-the-scenes-2265f14e3eba">System Prompts Explained: How AI Models Actually ... - Medium</a></li>
<li><a href="https://tetrate.io/learn/ai/system-prompts-guide">System Prompts: Design Patterns and Best Practices</a></li>
<li><a href="https://aiwiki.ai/wiki/system_prompt">System prompt - AI Wiki</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体积极，Simon Willison 分享了一个用于追踪提示词变更的 Git 历史工具。一些评论者指出，系统提示词只是塑造模型行为的层层体系中的一部分，另一些人则对涉及 AI 负面报道的审核问题表达了担忧。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#system prompts`, `#transparency`

---

<a id="item-2"></a>
## [重新审视 ECA-Net：对通道注意力设计的概念性批评](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 8.0/10

一篇 Reddit 分析重新审视了 2019 年发表的 ECA-Net 论文（被引 12,000 次），指出其核心假设——通过一维卷积实现跨通道交互——在概念上与卷积的拓扑假设不一致，尽管 ECA 在实验上确实有效。作者在国际象棋残局库上测试，发现 k=1 的 ECA（无跨通道交互）表现与 k=3 几乎相当。 这一分析挑战了一篇高被引论文中被广泛接受的设计依据，说明实验成功未必能验证论文提出的机制。它可能影响研究者如何解读和设计通道注意力模块，尤其是在将这类模块应用于非空间数据时。 ECA 模块不在通道均值上做降维，而是使用自适应卷积核大小 k 的一维卷积。作者使用六子国际象棋残局库作为无偏训练数据，结果显示 ECA(k=3) 的准确率为 96.68%，优于 SE 的 96.17%，但 ECA(k=1) 也达到了 96.61%，这让“跨通道交互是关键”的说法受到质疑。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**背景**: ECA-Net（高效通道注意力）是 CVPR 2020 论文，针对 Squeeze-and-Excitation（SE）模块的改进：避免降维，改用一维卷积实现跨通道交互。通道注意力机制通过对每个通道加权来重新校准特征图。作者认为，在通道维度上做一维卷积相当于把通道当作有顺序的空间或表格数据，违背了卷积的局部性和平移不变性假设；但神经网络仍能适应并取得不错的效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep Convolutional Neural Networks</a></li>
<li><a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Wang_ECA-Net_Efficient_Channel_Attention_for_Deep_Convolutional_Neural_Networks_CVPR_2020_paper.pdf">ECA-Net: Efﬁcient Channel Attention for Deep Convolutional Neural Networks</a></li>

</ul>
</details>

**标签**: `#Computer Vision`, `#Attention Mechanisms`, `#Deep Learning`, `#Research Analysis`, `#Model Design`

---

<a id="item-3"></a>
## [Anthropic 第二季营收暴涨 14 倍，突破 115 亿美元](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

2026 年第二季度，Anthropic 初步营收超过 115 亿美元，同比增长超 14 倍，高于去年同期的 7.87 亿美元和 2026 年第一季度的 47.3 亿美元。公司调整后营业利润转正，并正在筹备可能在今秋启动的 IPO。 这一里程碑凸显了 AI 商业化的快速推进，以及 Anthropic 作为主要参与者的崛起。营收激增和计划中的 IPO 可能重塑投资者对 AI 公司的预期，并加剧该行业的竞争。 这些数字为初步数据，可能调整。Anthropic 营收从 2025 年第二季度的 7.87 亿美元跃升至 2026 年第二季度的超过 115 亿美元，调整后营业利润转正，但公司尚未发布完整的审计财务报表。

telegram · zaihuapd · 8月16日 07:26

**背景**: Anthropic 是一家人工智能研究与安全公司，由前 OpenAI 研究人员于 2021 年创立，以开发 Claude 系列大语言模型而闻名。其营收快速增长反映了企业对生成式 AI 的强劲需求。IPO 将为公司带来公开市场投资和扩张资金，并伴随与 OpenAI 等其他 AI 实验室的激烈竞争。

**标签**: `#Anthropic`, `#AI`, `#Revenue`, `#IPO`, `#Business`

---