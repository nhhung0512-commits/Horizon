---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 29 条内容中筛选出 9 条重要资讯。

---

1. [DRAM 寻址漏洞实现 Ring-0 特权提升](#item-1) ⭐️ 9.0/10
2. [谷歌发布 Gemini 3.7 Flash：最智能的实用型模型](#item-2) ⭐️ 8.0/10
3. [Cerebras 与 OpenAI 推出 GPT-5.6 Sol Ultrafast，宣称 HLE 推理速度提升 7 倍](#item-3) ⭐️ 8.0/10
4. [DeepSeek 发布开源 Agent Harness 开发者预览版](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4 Pro 0813 通过 OpenRouter 发布，开源权重或将上线](#item-5) ⭐️ 8.0/10
6. [苹果拟为 Siri AI 授权新闻内容，预算或达九位数](#item-6) ⭐️ 8.0/10
7. [DeepMind 发布手语转文字模型 SL2T，首次登陆 Pixel 11](#item-7) ⭐️ 8.0/10
8. [OpenAI 升级 ChatGPT 至 GPT-5.6 系列并扩展免费权限](#item-8) ⭐️ 8.0/10
9. [谷歌发布 Gemini 3.6 Flash，确认 Gemini 4 已启动预训练](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DRAM 寻址漏洞实现 Ring-0 特权提升](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

安全研究员 Christopher Domas 发布了名为 'skitter-creek-bath-salts' 的新型攻击技术与工具，通过利用 DRAM 控制器的地址转换寄存器，在 AMD Family 16h CPU 上实现从 ring-0 内核权限向更深层特权 CPU 模式的权限提升。该研究连同开源概念验证代码已在 Black Hat 上展示。 这一研究意义重大，因为它展示了一个绕过传统软件安全边界的硬件级攻击面，使拥有 ring-0 权限的攻击者能够进入通常承载固件和虚拟机监视器的 SMM 或其他隐藏模式。该技术可能影响多款 AMD 处理器，并对未公开的 DRAM 控制器功能的安全性提出新的质疑。 根据项目 README，该漏洞利用是在 AMD Family 16h（Jaguar）CPU 上开发和测试的，这是最后一代数据手册中记录了 DRAM 控制器转换寄存器且表明它们无法被锁定的处理器。研究人员指出，较新的 Zen 3 处理器对内存控制器寄存器使用了不同的基地址，因此该技术可能无法直接适用。

hackernews · matt_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: DRAM 寻址指的是内存控制器如何将物理内存地址映射到 DRAM 芯片内的行、列、Bank 和通道位置，这种映射常常由未公开的翻译寄存器完成。CPU 特权级别（ring）将操作系统内核（ring 0）与用户进程隔离，但像系统管理模式（SMM）这样的更深层模式拥有更高权限，且通常处于隐藏状态。此前 DRAMA 等研究已经表明 DRAM 寻址可被逆向工程并用于侧信道攻击；而这项新工作进一步通过篡改这些寄存器，打破了 ring 0 与更高特权执行环境之间的隔离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49286341">Spaghettifying DRAM | Hacker News</a></li>
<li><a href="https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_pessl.pdf">PDF DRAMA: Exploiting DRAM Addressing for Cross-CPU Attacks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Protection_ring">Protection ring - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论大多对 Christopher Domas 的工作表示兴奋和赞赏，用户们热切期待 Black Hat 演讲。一些评论者感叹 DRAM 已成为巨大的攻击面，另一些则询问该漏洞利用对较新 CPU 的适用性以及其他处理器系列是否受影响。还有少数人猜测，Xbox 和 PlayStation 等游戏机厂商可能会对这种硬件级漏洞感到担忧。

**标签**: `#security`, `#DRAM`, `#exploit`, `#ring-0`, `#hardware`

---

<a id="item-2"></a>
## [谷歌发布 Gemini 3.7 Flash：最智能的实用型模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.7 Flash，这是面向编码和智能体任务的新型 AI 模型，距离 Gemini 3.6 Flash 发布仅三周。它在 Legal Agent Bench 的 all-pass 指标上比此前 Flash 模型提升了 2.6 个百分点。 作为 Google 高性价比 Flash 系列的最新成员，此次发布对需要在较低价格下获得强大编码与视觉能力的开发者很重要。社区反应表明它正被直接拿来与 GPT-5.6 Luna、Opus 5 等竞品对比，体现出其在快速演进的 AI 模型竞赛中的地位。 该模型的限时优惠价格计划于 2026 年 12 月 31 日翻倍，一些评论者觉得这很不寻常。早期实测显示其在图像转 HTML 和 SVG 渲染方面能力突出，同时对比表明 Opus 5 和 Luna 等竞品在部分基准上仍占优。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**背景**: Gemini 是 Google DeepMind 开发的多模态大语言模型家族，继承自 LaMDA 与 PaLM 2，并为 Gemini 聊天机器人提供支持。Flash 系列被定位为低成本、高吞吐的“主力”模型，常用于摘要、解析、格式化和编码智能体任务，在能力之外强调效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash - Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_2.5_Flash_Image">Gemini 2.5 Flash Image</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户称赞 Gemini 3.7 Flash 在价格上的视觉和编码表现，另一些则对其定价时间表存疑，并指出 GPT-5.6 Luna 和 Opus 5 在部分基准上仍领先。还有用户要求与 Luna 和 Terra 直接对比，并有人称 Luna 更便宜的价格削弱了 Flash 的存在必要。

**标签**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#model release`

---

<a id="item-3"></a>
## [Cerebras 与 OpenAI 推出 GPT-5.6 Sol Ultrafast，宣称 HLE 推理速度提升 7 倍](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras 与 OpenAI 宣布推出由 Cerebras 硬件支持的 GPT-5.6 Sol Ultrafast 模式，每秒可输出高达 750 个 token，处理速度最高提升 14 倍。在评估中，它用 11 小时 11 分钟回答了 HLE 的全部 2500 道题，比 Claude Fable 5 快约 7 倍，且准确率相当。 这一里程碑表明，专用 AI 硬件可以大幅加速前沿级语言模型，可能重塑推理成本和延迟的预期。它有利于对时间敏感和关键任务的应用，并可能加剧 AI 基础设施提供商之间的竞争。 OpenAI 的预览说明称，Ultrafast 模式可将 GPT-5.6 Sol 的速度提升至 14 倍，每秒输出高达 750 个 token，Cerebras 则声称不会牺牲质量。然而，目前尚未公布任何定价信息，部分评论者指出，两家公司并未明确说明 Ultrafast 模式与标准 Sol 模型的性能完全一致。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**背景**: Cerebras Systems 开发晶圆级引擎（WSE）和 CS-3 超级计算机，并提供 AI 推理与训练云 API，用户无需购买硬件即可使用。Humanity's Last Exam（HLE）是一个包含 2500 道专家审核题目的基准测试，涵盖数学、科学和人文领域，旨在测试 AI 的能力极限。Ultrafast 是 OpenAI 新推出的 API 服务层级，最初仅向精选客户开放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Humanity's_Last_Exam">Humanity's Last Exam - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对更快的推理速度感到兴奋，但对性能等同的说法持怀疑态度，指出官方未明确确认 Ultrafast 在所有基准测试中都与标准 Sol 模型的准确率一致。有人指出缺乏定价信息，怀疑这是否会是高价服务或仅仅是在试探市场需求。还有人认为速度提升有利于大规模代码库和测试工作负载，也有人认为这给其他硬件厂商带来了竞争压力。

**标签**: `#AI`, `#OpenAI`, `#hardware`, `#performance`, `#GPT`

---

<a id="item-4"></a>
## [DeepSeek 发布开源 Agent Harness 开发者预览版](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek 发布了其 DeepSeek Harness 智能体框架（agent harness）的开源开发者预览版，采用 MIT 许可证。该版本提供通过只追加（append-only）会话日志实现的完整运行可追溯性、轨迹检查视图以及可热重载的插件架构。 像 DeepSeek 这样重要的 AI 实验室将这类工具开源，会推动智能体工具链走向“每次运行都可审计、可回放、可恢复”的标准，这对自主智能体的调试和信任至关重要。该发布也凸显了可追溯性正成为快速发展的 LLM 智能体生态中的关键差异化优势。 该框架基于 Cordis v4，可在不重启进程的情况下热加载和卸载插件，并且能清理副作用及依赖模块。恢复（resume）、分支（fork）、搜索和回放等主要操作都基于同一条只追加事件流；项目仍处于早期预览阶段，预计会有破坏兼容性的变更。

hackernews · bjin · 8月13日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**背景**: Agent harness（智能体框架）是连接 LLM 与工具、记忆和执行逻辑的结构层，让模型能够“做事”而不只是生成文本。会话回放（session replay）是一种调试技术，通过记录用户或系统的交互，让开发者能准确看到问题发生前发生了什么。可热重载的插件架构允许在运行时应用代码更改而无需重启进程，从而加快开发速度，并支持动态启用或停用组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/vinit-tomar_harness-harness-contextinjection-activity-7450227892724334592-TdxO">Agent Harness : The Structural Layer for LLM Execution | LinkedIn</a></li>
<li><a href="https://sentry-io.nproxy.org/product/session-replay/">Session Replay : See What Users See, Fix What Broke | Sentry</a></li>
<li><a href="https://github.com/veemex/open-reload">GitHub - veemex/open-reload: Hot-reload MCP meta-plugin for OpenCode — watches plugin files and dynamically reloads tools at runtime</a></li>

</ul>
</details>

**社区讨论**: 评论者大多热情很高，称只追加的轨迹记录功能是“杀手级特性”，并拿来与一些美国专有模型中加密或混淆的轨迹进行对比。一位作者确认这仅是 MIT 许可的早期预览版并欢迎反馈，其他人指出它基于 Cordis v4，也有人对“万物皆插件”的设计表示“插件疲劳”。

**标签**: `#agent-harness`, `#deepseek`, `#LLM-agents`, `#traceability`, `#open-source`

---

<a id="item-5"></a>
## [DeepSeek V4 Pro 0813 通过 OpenRouter 发布，开源权重或将上线](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek V4 Pro 0813 现已通过 OpenRouter 提供 API 调用，其权重也已在 Hugging Face 上开放。该模型在低、中、高三种推理级别下会生成截然不同的输出，Simon Willison 表示他未在其他模型上见过这种差异。 作为中国头部 AI 实验室的又一可能开源权重版本，该发布巩固了 DeepSeek 在开源 AI 生态中的地位，也为开发者提供了更多选择。不同推理级别导致输出差异的现象，也引发了关于这些设置如何在实际应用中改变模型行为的思考。 该模型最初仅通过 OpenRouter 的 API 提供，DeepSeek 没有发布官方公告页面。基准测试数据从 DeepSeek 官方微信群流出，在 Reddit 上被以“低质量”删除，随后被转贴到 Hacker News；Hugging Face 权重页面还曾短暂返回 404，随后恢复。

rss · Simon Willison · 8月12日 23:59

**背景**: OpenRouter 是一个统一的 API 网关，允许开发人员通过单个端点访问数百个 LLM，并自动处理回退与价格选择。开源权重模型会公开发布训练后的神经网络参数，任何人都可以下载并运行，但不一定包含完整训练数据。现代 LLM 中的推理级别控制模型在回答前进行思维链计算的深度，可能影响输出的质量和风格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/docs/quickstart">OpenRouter Quickstart Guide</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.ibm.com/think/topics/reasoning-model">What Is a Reasoning Model? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区讨论较为分散：包含基准数据的 Reddit 帖因“低质量”被版主删除，而 Hacker News 以 ASCII 表格形式发布了相关结果。Telegram 用户指出 Hugging Face 权重页面曾短暂 404 后恢复，一度引发关于开源权重是否真的可用的疑虑。

**标签**: `#deepseek`, `#ai`, `#model-release`, `#openrouter`, `#machine-learning`

---

<a id="item-6"></a>
## [苹果拟为 Siri AI 授权新闻内容，预算或达九位数](https://9to5mac.com/2026/08/12/report-apple-seeks-publisher-deals-to-give-siri-ai-better-access-to-current-events/) ⭐️ 8.0/10

据 2026 年 8 月 12 日的报道，苹果正与出版商洽谈为 Siri AI 授权新闻内容，可能按使用量支付费用并签订多年协议。据报道预算可能达九位数，但苹果尚未宣布任何合作。 这标志着 AI 数据授权经济的重要转变，因为苹果似乎倾向于按使用量付费，而非其他 AI 公司常见的固定预付授权费。如果消息属实，此举可能改变出版商与 AI 开发者的谈判方式，并影响更广泛的 AI 训练数据市场。 洽谈中的协议是多年期内容授权，旨在让 Siri AI 获取当前新闻和信息。该报道尚未得到证实，苹果拒绝置评；Siri AI 预计于 2026 年晚些时候推出。

telegram · zaihuapd · 8月13日 04:40

**背景**: Siri 是苹果的语音助手，可以处理命令、搜索互联网并与 iOS 应用交互。2026 年 6 月，苹果推出了 Siri AI，这是由下一代 Apple Intelligence 驱动的全新版本，支持自然的来回对话并提供更强大的协助。AI 公司通常通过授权受版权保护的内容（如新闻文章）来训练模型或提供实时答案，通常采用固定预付费用模式——而苹果据报道采用的按使用量付费方式将与这一模式不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Siri">Siri - Wikipedia</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri</a></li>
<li><a href="https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/">Apple introduces Siri AI, a profoundly more capable and ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Siri AI`, `#News Licensing`, `#AI`

---

<a id="item-7"></a>
## [DeepMind 发布手语转文字模型 SL2T，首次登陆 Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

谷歌 DeepMind 发布了大规模多语言手语转文字模型 SL2T，并将其部署到 Pixel 11 设备的 Gboard 和 Live Transcribe 中。该功能最初支持美国手语（ASL）转英语，这是手语 AI 首次进入消费级产品。 这是无障碍领域的一个重要里程碑：实时手语转文字技术由此进入日常智能手机，而不再停留在研究实验室。其端侧、保护隐私的设计和出色的零样本表现，可能为包容性 AI 树立新标准，并推动行业覆盖更多语言。 SL2T 使用超过 10 万小时、覆盖 50 多种手语的视频数据训练，在 FLEURS-ASL 基准上，零样本 ASL 转英语翻译取得了 70 BLEURT 分。为保护隐私，模型仅处理视频中的手部与身体姿态关键点，而不读取原始像素画面。

telegram · zaihuapd · 8月13日 08:55

**背景**: FLEURS-ASL 是 FLORES/FLEURS 多语平行语料库向美国手语的扩展，为衡量手语转文字质量提供了标准数据集。BLEURT 是一种基于神经网络的自然语言生成评估指标，通过比较候选译文与参考译文来模拟人类评价。关键点处理是指模型只看到表示手部、面部和身体的地标点，这为 Gboard、Live Transcribe 等产品实现端侧计算并保护用户隐私提供了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datanorth.ai/news/google-deepmind-releases-sl2t">Google DeepMind releases SL 2 T sign language AI - DataNorth</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/google-sign-language-model-body-landmarks">Google's new model turns sign language into text for web searches</a></li>
<li><a href="https://arxiv.org/html/2408.13585">FLEURS - ASL : Including American Sign Language in Massively...</a></li>

</ul>
</details>

**标签**: `#DeepMind`, `#Sign Language AI`, `#Accessibility`, `#Machine Translation`, `#Pixel`

---

<a id="item-8"></a>
## [OpenAI 升级 ChatGPT 至 GPT-5.6 系列并扩展免费权限](https://t.me/zaihuapd/43176) ⭐️ 8.0/10

OpenAI 宣布更新 ChatGPT，推出 GPT-5.6 系列模型。付费的 Plus 和 Pro 用户将获得回复更可靠、更聚焦的 GPT-5.6 Sol；免费用户本周起默认升级为 GPT-5.6 Luna，下周起可享无限文本对话。 此次更新扩大了先进 AI 推理功能的可用范围，免费用户也能使用更新模型和 Think 按钮应对复杂问题。这表明 OpenAI 在提升付费用户体验的同时，也致力于让更高质量的 AI 助手触达更广泛的用户。 GPT-5.6 系列包含 Luna、Terra 和 Sol 三个版本。付费用户新增滑块可调节模型思考深度，免费用户则获得 Think 按钮；官方内部评估显示，Luna 在财经、医疗和法律等领域的事实错误更少。

telegram · zaihuapd · 8月13日 17:04

**背景**: GPT-5.6 是 OpenAI 于 2026 年 7 月 9 日发布的大语言模型系列，按能力从低到高分为 Luna、Terra 和 Sol 三个版本。ChatGPT 是 OpenAI 的对话式 AI 助手。此次更新延续了提升回复可靠性和用户对推理层级控制力的趋势。Think 按钮和思考滑块让用户可以在快速问答与针对复杂问题的深度推理之间灵活选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/">Improving GPT‑5.6 Sol in ChatGPT—and expanding ... - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://findskill.ai/blog/chatgpt-think-button-what-it-does/">ChatGPT's New 'Think' Button: What It Does, When to Use It</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#GPT-5.6`, `#AI`, `#Model Update`

---

<a id="item-9"></a>
## [谷歌发布 Gemini 3.6 Flash，确认 Gemini 4 已启动预训练](https://t.me/zaihuapd/43177) ⭐️ 8.0/10

谷歌于 2026 年 7 月 21 日发布 Gemini 3.6 Flash，相比 3.5 Flash 输出 token 减少 17%，并在代码生成、知识工作和计算机操作方面有所提升，知识截止日期更新至 2026 年 3 月。谷歌同时确认 Gemini 4 已启动预训练，并表示这是其“迄今为止最宏大的预训练项目”。 该发布增强了谷歌 Flash 系列在高效智能体工作流中的竞争力，且定价具有竞争力；Gemini 4 预训练启动也表明谷歌持续推进前沿 AI 研发。依赖低成本、高吞吐大语言模型的开发者和企业将直接受到影响。 Gemini 3.6 Flash 的 API 定价为每百万输入 token 1.5 美元、每百万输出 token 7.5 美元，并且能用更少的推理步骤和工具调用完成多步任务。谷歌还同时推出了 Gemini 3.5 Flash-Lite 和 3.5 Flash Cyber 等模型。

telegram · zaihuapd · 8月13日 17:32

**背景**: Gemini 是 Google DeepMind 开发的多模态大语言模型系列，是 LaMDA 和 PaLM 2 的继任者。Flash 系列旨在兼顾效率与质量，用于扩展智能体工作流。预训练是模型训练中资源消耗最大的初始阶段，模型在此阶段从大规模数据集中学习，之后再进行微调和部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/">3 . 6 Flash , 3.5 Flash -Lite, and 3.5 Flash Cyber</a></li>
<li><a href="https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/">Google launches Gemini 3 . 6 Flash and teases Gemini 4</a></li>
<li><a href="https://felloai.com/all-we-know-about-google-gemini-4/">Gemini 4: Release Date, Pre-Training News & Rumors</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#AI model release`, `#LLM`, `#Machine Learning`

---