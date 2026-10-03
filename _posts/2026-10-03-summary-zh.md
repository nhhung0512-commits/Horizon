---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 23 条内容中筛选出 1 条重要资讯。

---

1. [Aleph Alpha 发布主权开放权重模型 Kolibri](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Aleph Alpha 发布主权开放权重模型 Kolibri](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) ⭐️ 8.0/10

Aleph Alpha 发布了 Kolibri——一个面向主权场景的开放权重英德双语混合专家（MoE）模型，总参数量 78B、激活参数 3B，上下文窗口最高支持 100 万 token，权重以 Apache 2.0 许可开放。此次发布还附带了极为详尽的技术报告，并在训练中引入了“拒绝作答”（abstention）数据和公司自研的 Merlin-Arthur 协议，使模型在上下文中找不到答案时学会回答“我不知道”。 这次发布的意义更多在于透明度而非跑分领先：技术报告详实到被从业者称为“如何构建现代智能体 LLM 的教程”，甚至披露了数据集的构建方式。它同时也是欧洲“主权 AI”路线的一次落地，为企业提供了可在本地或气隙环境中部署的 Apache 2.0 模型，而不必依赖封闭的美国供应商。 Kolibri 是英德双语 MoE 模型，总参数 78B、激活参数 3B，上下文最长 100 万 token；其拒绝作答训练的目标是“限制幻觉”而非单纯提高回答率。社区成员也指出了一个评测上的问题：对比基准似乎只包含较旧或较弱的模型，这使得其宣称的成绩更难解读。

hackernews · bastitx · 10月3日 09:36 · [社区讨论](https://news.ycombinator.com/item?id=49942706)

**背景**: 开放权重模型会公开训练好的参数，供他人下载运行，但这并不等同于完全开源：训练数据、代码和许可条款仍可能不同，而这一区别关系到可审计性和部署权利。Aleph Alpha 是一家德国 AI 公司，将自家模型定位为“主权”用途，即政府或受监管企业等客户能把模型与数据掌控在自有基础设施中。幻觉——模型自信地编造答案——是 LLM 的核心缺陷之一，因此训练模型在上下文不足时拒绝作答是一种被广泛研究的缓解手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/">Kolibri Has Landed: A Sovereign Open-Weight Model</a></li>
<li><a href="https://neysa.ai/blog/open-weights-open-source/">Open Weights vs Open Source: What’s the Real Difference?</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models? - Analytics Vidhya</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体偏正面：有人称这是自己第一次见到如此程度的开放，也有训练团队成员表示 Kolibri 在编程和智能体任务上表现良好，并强调这是团队成立不到一年内的首个发布、迭代速度很快。还有人关注到让模型学会说“我不知道”的拒绝作答训练，并有人免费提供 Kolibri-1 的托管试用，无需 GPU 即可体验；主要批评则集中在基准对比只使用了过时或表现较弱的模型。

**标签**: `#open-weight models`, `#LLM`, `#Aleph Alpha`, `#AI transparency`, `#hallucination mitigation`

---