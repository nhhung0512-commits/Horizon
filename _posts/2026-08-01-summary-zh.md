---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> 从 37 条内容中筛选出 7 条重要资讯。

---

1. [OpenAI Astra 模型解决十项长期未解数学难题](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Flash 0731：304B 参数智能体模型性价比领先](#item-2) ⭐️ 8.0/10
3. [无状态 MCP 2.0 重燃兴趣，催生 mcp-explorer 与 datasette-mcp](#item-3) ⭐️ 8.0/10
4. [KataGo 研究探秘超人围棋网络内部对称性](#item-4) ⭐️ 8.0/10
5. [谷歌确认 Android 侧载应用将实行两档开发者验证](#item-5) ⭐️ 8.0/10
6. [EA 以 550 亿美元被沙特财团收购](#item-6) ⭐️ 8.0/10
7. [微软确认今年推出 Copilot 超级应用](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Astra 模型解决十项长期未解数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 9.0/10

OpenAI 宣布其下一代主要模型 Astra 的一个内部版本解决了十个至少十年未有进展的数学问题。公司声称每个问题的 token 成本（按 GPT-5.6 Sol 价格计算）低于 2,000 美元，并发布了 Lean 4 形式化证明、论文以及模型生成的推理回顾。 这标志着 AI 驱动数学研究的一个重要里程碑，表明前沿模型能够以极低成本产出原创且可验证的成果。紧随 Anthropic 的 Claude Mythos 密码学发现之后，这一进展预示着向 Terence Tao 所称的“大数学”（人类与机器大规模协作）加速转变。 这十个问题涵盖群论、高维几何、编码理论、量子复杂性、格密码与极值组合学。OpenAI 未披露有多少其他问题尝试后未能解决，也未公开模型使用的具体提示词。

rss · Simon Willison · 8月1日 20:34

**背景**: Astra 是 OpenAI 的下一代模型系列，旨在让多个智能体协作数小时甚至数天来解决复杂问题。这些证明用 Lean 4 形式化——Lean 4 是一种证明助手，可让数学论证被机器自动检查。此举延续了 AI 系统用于探索数学猜想的趋势，也与数学家陶哲轩对“大数学”的愿景相符：AI 承担大量技术性工作，人类负责创造性部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bitsminds.com/news/openai-astra-ten-open-math-problems-lean-proofs-2026">OpenAI Names Its Next Model Family Astra — and Says It Solved ...</a></li>
<li><a href="https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/">OpenAI announces its "next major model" Astra by dropping ten ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 和数学界人士的讨论既兴奋又怀疑。评论者称赞其惊人的成本效率，但也指出未公开的失败案例和缺失的实际提示词是重要的保留点。

**标签**: `#AI research`, `#mathematics`, `#OpenAI`, `#LLMs`, `#theoretical computer science`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731：304B 参数智能体模型性价比领先](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek-V4-Flash-0731，这是一个 304B 参数（Hugging Face 上 167GB）的模型，宣称“显著增强的智能体能力”，输入价格每百万 token $0.14，输出价格每百万 token $0.27。Artificial Analysis 将其排在 MiniMax M3（428B 参数）之前，并认为它可能是当前性价比最高的模型。 此次发布巩固了 DeepSeek 在高性价比大模型领域的地位，表明较小规模的模型在智能体任务上可以媲美甚至超越更大的模型。其极具竞争力的定价可能给其他厂商带来压力，并让高频智能体应用更容易用上先进 AI。 该模型在 Artificial Analysis Intelligence Index（v4.1）及其“每任务成本”图表上表现强劲，独自落在最具吸引力象限，每任务成本约$0.028，智能得分约 50。输出质量取决于推理强度：通过 OpenRouter 使用默认推理级别生成的鹈鹕图像有缺陷，而设置`reasoning_effort high`后结果明显更好。

rss · Simon Willison · 7月31日 23:59

**背景**: Artificial Analysis 是一个独立的模型评测平台，其 Intelligence Index 综合多项评测指标对 LLM 打分，并发布“每任务成本”对比。DeepSeek-V4-Flash 属于 DeepSeek V4 系列；DeepSeek API 文档指出其推理能力接近 V4-Pro，但参数更小、响应更快且 API 定价极具竞争力；OpenRouter 观察称 V4 发布一个月内，Flash 就占据了 DeepSeek 智能体 token 流量的 70%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence , Performance, and Price</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424/">DeepSeek V 4 Preview Release | DeepSeek API Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#artificial intelligence`

---

<a id="item-3"></a>
## [无状态 MCP 2.0 重燃兴趣，催生 mcp-explorer 与 datasette-mcp](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison 表示，2026-07-28 版 Model Context Protocol（MCP）2.0 规范引入了无状态核心，将原先两次往返的会话流程简化为单个 HTTP 请求。他本周构建了三个 MCP 实现，其中包括 mcp-explorer 与 datasette-mcp。 这是 MCP 协议发布以来最重大的变化，让 MCP 工具比给 Agent 一个带 curl 的 shell 环境更易于审计和控制，也让能在笔记本电脑上运行的较小模型更容易驱动。在兴趣转向 Anthropic 的 Skills 之后，这有望重燃 MCP 的采用。 无状态方案不再需要 Mcp-Session-Id 和单独的 initialize 请求，而是改用 MCP-Protocol-Version、Mcp-Method 等 HTTP 头。这简化了客户端与服务器的实现，也无需维护服务器端会话状态，更适合构建可扩展的 Web 应用。

rss · Simon Willison · 7月31日 23:13

**背景**: MCP 是 Anthropic 于 2024 年 11 月推出的开放标准，定义了 AI 系统与外部工具、数据源集成的通用方式。2025 年该协议被各大 AI 厂商广泛采用，但随着 Anthropic 的另一项发明 Skills 的出现，人们发现拥有终端与 curl 的 Agent 能更灵活地完成许多任务，MCP 的关注度有所下降。新的无状态规范大幅降低了实现复杂度，从而重新吸引了开发者兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/">The 2026-07-28 MCP Specification Release Candidate</a></li>

</ul>
</details>

**标签**: `#Model Context Protocol`, `#AI Agents`, `#Protocols`, `#Open Source`

---

<a id="item-4"></a>
## [KataGo 研究探秘超人围棋网络内部对称性](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

KataGo 维护者 David Wu 发布了一项研究，分析围棋神经网络在内部如何对称地表示棋盘，尽管网络架构并未强制 8 重旋转/镜像对称。该研究报告主要由 AI 辅助撰写但有人类指导，报告中有一个意外发现，并附有相关代码链接。 这是少数针对超人级别围棋网络的解释性研究之一，可以揭示神经网络是自动习得与方向无关的概念，还是分别记忆不同方向。研究结果可能影响在训练强化学习智能体时如何使用对称先验和数据增强。 KataGo 采用标准 CNN 架构，主体由残差块构成，并带有策略头和价值头；训练时使用随机 8 重数据增强，每批次都会随机旋转/翻转棋盘方向。尽管围棋规则在旋转和镜像下完全对称，但模型并未硬编码对称性，因此内部表示在多大程度上与方向无关是一个经验问题。

reddit · r/MachineLearning · /u/icosaplex · 8月1日 16:18

**背景**: 围棋是一种经典棋盘游戏，规则简单但策略极深；KataGo 等现代围棋引擎通过自我对弈和强化学习达到超人水平。随机 8 重方向变换这类数据增强在深度学习中常被用来让模型对方向变化不敏感，但这项研究追问的是：训练后的网络是否真的在内部利用了这种不变性。KataGo 的模型架构被记录为卷积神经网络，包含残差主体、策略头和价值头，并通过大规模分布式自我对弈训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/lightvector/KataGo/7.2-model-architecture">Model Architecture | lightvector/ KataGo | DeepWiki</a></li>
<li><a href="https://katagotraining.org/">KataGo Distributed Training</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#interpretability`, `#go`, `#symmetry`, `#neural-networks`

---

<a id="item-5"></a>
## [谷歌确认 Android 侧载应用将实行两档开发者验证](https://t.me/zaihuapd/42911) ⭐️ 8.0/10

Google 确认将在 Android 16 中推出面向侧载应用的两档开发者验证系统，要求开发者注册包名和签名密钥。付费档费用为 25 美元，免费档仅需邮箱注册，但有安装次数限制。 该政策对 Android 侧载生态和 F-Droid 等开源应用商店影响重大，可能限制 Google Play 之外的應用分发。同时，Google 虽不公开开发者名单，但仍会收集开发者个人信息，引发隐私和审查担忧。 该系统通过云端验证应用，安装时可能需要网络连接。免费档有安装次数限制，付费档费用为 25 美元（与 Google Play 注册费相同），可能对独立和开源开发者造成负担，并且该要求可能影响 F-Droid 等仓库的自动化构建。

telegram · zaihuapd · 8月1日 03:08

**背景**: 侧载是指在官方应用商店（如 Google Play）之外安装 Android 应用的做法。Android 应用签名使用加密密钥来验证应用的真实性和完整性，每个应用的签名密钥在其生命周期内保持不变。F-Droid 是一个流行的免费开源 Android 应用仓库，依赖自动化构建和社区贡献。Android 16 是谷歌下一代移动操作系统版本，这一新的开发者验证系统预计将在其中推出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid - Wikipedia</a></li>
<li><a href="https://f-droid.org/">F-Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://developer.android.com/studio/publish/app-signing">Sign your app | Android Studio | Android Developers</a></li>

</ul>
</details>

**标签**: `#Android`, `#Google`, `#developer verification`, `#sideloading`, `#privacy`

---

<a id="item-6"></a>
## [EA 以 550 亿美元被沙特财团收购](https://www.gamersky.com/news/202607/2180618.shtml) ⭐️ 8.0/10

EA 宣布，出售给沙特公共投资基金（PIF）牵头的财团的交易已获得全部监管批准，预计将于 2026 年 8 月 4 日正式完成。交易完成后，EA 将成为一家私营公司，财务数据将不再对外公开。 这是游戏史上第二大收购案，仅次于 2023 年微软以 754 亿美元收购动视暴雪。这笔交易将西方最大的游戏发行商之一置于沙特资本之下，可能加速主权财富对游戏行业的投资。 收购方由 PIF、银湖资本（Silver Lake）和 Affinity Partners 组成。PIF 此前已全资收购了 Scopely 和 Niantic，而交易完成后 EA 将退市私有化，其财务信息将不再对外披露。

telegram · zaihuapd · 8月1日 09:10

**背景**: EA 是全球最大的游戏发行商之一，旗下拥有 EA Sports FC（FIFA）、Madden、Battlefield、The Sims 等知名 IP。沙特 PIF 近年来持续扩张游戏投资版图，这与其国家 2030 愿景经济多元化战略密切相关。此次收购延续了游戏行业的整合浪潮，此前最大的案例是 2023 年微软收购动视暴雪。

**标签**: `#Electronic Arts`, `#Gaming Industry`, `#M&A`, `#Saudi PIF`, `#Business News`

---

<a id="item-7"></a>
## [微软确认今年推出 Copilot 超级应用](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

微软 CEO 纳德拉在财报电话会议上确认，微软今年将推出一款 AI「超级应用」，把 Copilot 的聊天、编程和智能体能力整合起来，同时覆盖消费者和企业用户。该应用将把 Copilot、GitHub Copilot、Copilot Cowork 和 Autopilot 系统合并为一种体验。 这是微软将分散的 AI 产品统一为单一平台的重大战略举措，可能重塑用户与 AI 助手及自主智能体的交互方式。这也加剧了与 OpenAI 的 ChatGPT Work 以及 Anthropic 的 Claude Cowork 生态系统的竞争。 这款超级应用将整合聊天、编程功能、Copilot Cowork 和 Autopilot 系统，代码功能将在本季度加入。微软上季度营收增至 900 亿美元，主要由 AI 和云业务推动。

telegram · zaihuapd · 8月1日 13:18

**背景**: 超级应用是指在一个移动或网页应用中整合多种服务（如消息、支付、生产力工具）的平台。微软的 Copilot 是嵌入其产品中的 AI 助手，而 Copilot Cowork 可自动化跨多步骤的工作流，Autopilot 系统则能处理目标驱动的任务。智能体 AI（agentic AI）指能够自主推理并主动发起任务、而非仅响应指令的软件。此前微软已将 Anthropic 的 Claude Cowork 技术整合到 Microsoft 365 Copilot 中，OpenAI 也推出了结合 ChatGPT 与 Codex 的 ChatGPT Work 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/microsoft-365-copilot/cowork">Copilot Cowork: Automate Tasks and Workflows | Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Super_app">Super app - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents? | IBM</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Copilot`, `#AI`, `#Super App`, `#Agents`

---