---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 35 条内容中筛选出 6 条重要资讯。

---

1. [Calif 声称利用 AI 打造微信零点击蠕虫并实现 RCE 利用](#item-1) ⭐️ 9.0/10
2. [研究者质疑：OpenAI 是否值得托付未发表的数学成果？](#item-2) ⭐️ 8.0/10
3. [Shopify 将移动应用从 React Native 迁回原生 iOS/Android](#item-3) ⭐️ 8.0/10
4. [微软将 Rust 列为一级（Tier-1）语言](#item-4) ⭐️ 8.0/10
5. [DeepSeek 发布 V4.1 Flash：552B 多模态模型，激活参数 8B/16B](#item-5) ⭐️ 8.0/10
6. [DeepSeek 发布 MIT 许可 Harness 并开放 V4-Pro-0813 权重](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Calif 声称利用 AI 打造微信零点击蠕虫并实现 RCE 利用](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，称其是首个可通过微信通话在 iOS 与 Android 上传播的零点击蠕虫，无需受害者任何交互即可劫持其账号。该团队表示，借助 AI 他们在大约两天内找到了底层漏洞并写出首个远程代码执行（RCE）利用程序，随后又用约一周时间完成了整个蠕虫的构建。 若该成果被证实，这标志着 AI 赋能攻击性安全的转折点：过去需要更大团队耗时数月才能完成的蠕虫，据称如今由小团队在一周左右即可做出，从而降低了针对拥有十亿级用户平台的大规模移动端攻击门槛。这也向微信母公司腾讯、移动操作系统厂商以及防御方提出紧迫问题：AI 辅助的漏洞发现与武器化速度究竟有多快。 受害者无需接听电话，甚至完全不需要碰手机；即便接听，也听不到任何声音，而漏洞利用依然成功；研究人员在三部测试手机上演示了蠕虫的传播。该结论基于 2026 年 9 月 8 日前后发布的公开演示和研究条目，因此无论漏洞本身还是 AI 的实际贡献，都仍待独立验证。

rss · Simon Willison · 9月10日 00:56

**背景**: 零点击漏洞利用指无需用户任何操作即可攻陷设备，因此比依赖受害者点击链接或打开文件的攻击危险得多。远程代码执行（RCE）意味着攻击者可在目标设备上运行自己的代码，通常是部署后续恶意软件或窃取数据的前置步骤，Log4Shell 等事件即属此类。蠕虫则是无需人工干预即可在受害者之间自我传播的恶意软件，而把它与消息应用通话功能上的零点击 RCE 结合，正是这一声明引人注目的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">"Zero-click" WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls</a></li>
<li><a href="https://www.cloudflare.com/learning/security/what-is-remote-code-execution/">What is remote code execution?</a></li>

</ul>
</details>

**标签**: `#AI security`, `#zero-click exploit`, `#WeChat`, `#remote code execution`, `#AI-assisted hacking`

---

<a id="item-2"></a>
## [研究者质疑：OpenAI 是否值得托付未发表的数学成果？](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

在数学爱好者聚集的 Mathstodon 实例上，用户 @andreasthom 发起的一条讨论帖被 Hacker News 放大传播：在有人指控 OpenAI 未经署名便将这些交流用于自身已发表的成果之后，研究者是否还能放心地把未发表的数学想法交给 OpenAI 的模型，成了公开疑问。 如果研究者无法判断自己的私人数学思路是否会出现在厂商后续的成果或训练中，支撑学术界与 AI 厂商合作的那层非正式信任就会被侵蚀，这可能减少前沿模型接触真正困难的新问题，并重塑整个 AI 行业关于署名与数据使用的规范。 有评论指出，据称 OpenAI 表示“不可能”让 Buckmaster 博士近两个月的 Codex 提示词以任何方式影响该系统，包括训练；但批评者反驳称，基于可验证奖励的强化学习（RL）与对用户对话的预训练是两条不同的影响路径，影响仍可能发生；另一位评论者还提到，从一个仍在训练中的模型里生成 3000 亿输出 token 的做法相当可疑。

hackernews · pred_ · 9月10日 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: Mathstodon.xyz 是一个面向数学爱好者的 Mastodon（联邦宇宙）实例，支持 LaTeX 渲染，因此自然成为数学家讨论科研伦理的场所。技术层面的争议集中在“训练数据归因”（training data attribution）——即追溯究竟是哪些训练样本影响了模型输出的研究方向——以及“把用户对话预训练进模型权重”与“在可验证数学题上做强化学习”这两者的区别：在后一条路径中，模型可能自行发现从未出现在任何用户消息里的技巧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mathstodon.xyz/">About - Mathstodon</a></li>
<li><a href="https://medium.com/people-ai-research/scaling-training-data-attribution-f7d1eddd85da">Scaling Training Data Attribution | People + AI Research Blog</a></li>
<li><a href="https://www.choice360.org/libtech-insight/chatting-isnt-training-demystifying-memory-in-llms/">Chatting Isn't Training: Demystifying Memory in LLMs - Choice 360</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧明显：一些评论认为应当用同一标准衡量 OpenAI——如果换作人类合作者拿走了自愿参与者提供的想法却不署名发表，那显然是不道德的；另一些人则坚称这场风波是“毫无实质依据的歇斯底里”；还有一派认为两件事可以同时成立，因为对对话的预训练可以提升模型的直觉，而可验证数学上的强化学习则独立地发现了超越人类的技巧。质疑还集中在 OpenAI 的动机上，包括为约十万名研究者提供免费访问的说法，以及从一个仍在训练中的模型大量生成 token 的行为。

**标签**: `#OpenAI`, `#AI ethics`, `#mathematics`, `#research integrity`, `#pretraining data`

---

<a id="item-3"></a>
## [Shopify 将移动应用从 React Native 迁回原生 iOS/Android](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 工程团队发布文章，解释为何将其旗舰移动应用从 React Native 迁回完全原生的 iOS 与 Android 代码库。该文章在 Hacker News 上获得 633 个赞和 426 条评论，再次点燃了原生开发与跨平台开发之争。 Shopify 是与 Meta、微软并列的 React Native 最知名使用方之一，这样一家高调采用者的公开“回头”，对判断该框架在大型产品中的适用边界具有很强的信号意义。此事在当前尤为值得关注，因为社区成员认为 AI 代码生成正在降低编写和迁移原生代码的成本，从而可能削弱跨平台框架最核心的经济性论据。 React Native 是 Meta 推出的开源框架，开发者只需编写一次 React/JavaScript 代码即可在 iOS 和 Android 上运行，Facebook、微软和 Shopify 等公司都曾使用它。在讨论中，开发者 atonse 表示，AI 编程代理（Codex）逐个清点了现有 React Native 代码库中的每个界面，约在一夜之间将一款 15 至 20 个页面的应用迁移到 Android 和 iOS 并达到约 90% 的完成度，随后又花几天时间打磨，并用 Maestro 做测试。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta Platforms（原 Facebook）开发的开源 UI 框架，它把 React 编程模型引入移动端开发，让团队可以用一套 JavaScript 代码同时覆盖 iOS 和 Android，而不必维护两个独立原生应用。这类跨平台方案——历史上包括 Apache Cordova/PhoneGap，桌面端则是 Electron——以共享代码、降低人力需求为代价，换来的体验往往像是各平台功能的“最小公约数”。相比之下，原生开发使用各平台自有的语言和工具（iOS 上的 Swift/Objective-C，Android 上的 Kotlin/Java），可以做出更深入的优化，但需要各自独立的专业团队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://reactnative.dev/">React Native</a></li>
<li><a href="https://cloud.google.com/use-cases/ai-code-generation">AI Code Generation: Definition, Uses and Tools | Google Cloud</a></li>

</ul>
</details>

**社区讨论**: 社区情绪并非一边倒地支持原生：Waterluvian 认为这本质上只是受资源约束的工程决策，不同公司情况各异；pkaler 则指出，二十年来团队不断采用跨平台框架，期待节省人力，但这一预期很少兑现，最终得到的却是各平台功能“最小公约数”式的应用。最引人注目的是 AI 视角，tonic_note 和 atonse 认为，既然代码越来越多由 AI 生成，React Native 最大的吸引力——让 Web 开发者兼职做移动端——正在失效，因此不如一开始就用原生开发。

**标签**: `#React Native`, `#mobile development`, `#native apps`, `#cross-platform`, `#AI code generation`

---

<a id="item-4"></a>
## [微软将 Rust 列为一级（Tier-1）语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

微软已将 Rust 提升为内部开发的“一级（Tier-1）语言”，与 C++、C# 和 TypeScript 并列，成为公司支持力度最大的语言之一。这一消息以客座文章的形式发布在 Rust 基金会博客上，把此前微软内部逐步推进的 Rust 采用正式化、公开化。 这一举措对 Rust 而言是一次重要的行业背书，表明一家顶级的操作系统与工具链厂商已将其视为系统编程和内存安全开发的一流选择。由于微软既扮演 C/C++ 工具链供应商、又是平台方，其语言选择会影响企业和开源项目在启动新项目时的技术决策，因此对整个生态都有重要意义。 文章指出 Rust 已与 C++、C# 和 TypeScript 并列，成为微软支持力度最大的语言之一；社区讨论则把该公告与微软提出的目标联系起来——到 2030 年借助自动化工具将 10 亿行代码转换为 Rust，效率目标为“1 名工程师、1 个月、100 万行代码”。社区还将其视为对长期流传的“Rust 将集成进 MSVC 工具链”传闻的公开印证。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**背景**: Rust 是由 Graydon Hoare 于 2006 年在 Mozilla 时期创造的通用系统编程语言，2015 年 5 月发布首个稳定版 Rust 1.0，目前由 Rust 基金会负责管理。它通过编译期的“借用检查器（borrow checker）”追踪对象生命周期，在无需垃圾回收器的情况下保证内存安全，从而在构建阶段就防止内存错误和数据竞争。微软公开表示，内存安全问题——据 Azure 首席技术官 Mark Russinovich 称约占其产品 CVE 的 70%——是采用内存安全语言的重要动因。“一级（Tier-1）”是微软内部的一种工程地位，代表该语言在工具链、文档和人员投入上都能得到完整的一流支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier - 1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language)</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对这一消息表示欢迎，认为这证明 Rust 已成熟为 C++ 和 C# 的有力竞争者，而不再是像 Zig、Odin 那样仍在快速演进、棱角尚多的新语言。不少人把该公告与微软“10 亿行代码转换”目标以及 DARPA 组织的多团队 C 转 Rust 自动化尝试联系起来；也有人强调，鉴于微软长期受内存相关 CVE 困扰，内存安全具有重要的战略价值。

**标签**: `#Rust`, `#Microsoft`, `#systems-programming`, `#memory-safety`, `#programming-languages`

---

<a id="item-5"></a>
## [DeepSeek 发布 V4.1 Flash：552B 多模态模型，激活参数 8B/16B](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek 正式发布 V4.1 Flash，官方称这是其全新模型结构系列中尺寸最小的模型，采用 552B 参数的 Causal-Encoder-Decoder 结构，输入与输出激活参数分别为 8B 和 16B，并原生支持多模态视觉理解。该模型已在 DeepSeek API 上线，模型名为 deepseek-flash，新价格于 2026 年 9 月 10 日 12:00 生效；自 2026 年 9 月 14 日 12:00 起，deepseek-v4-pro 的请求将被路由至 V4.1 Flash，并按 V4.1 Flash 的价格计费。 通过将高达 552B 的总参数与仅 8B/16B 的激活参数相结合，V4.1 Flash 追求的是更快、更廉价的推理表现，这有望大幅降低开发者通过 API 使用前沿级多模态能力的成本。而 deepseek-v4-pro 的流量被自动路由至 V4.1 Flash，意味着现有用户实际上会被迁移到新模型，表明 DeepSeek 正围绕这一新架构整合其产品线，而非继续维持并行的模型代际。 最关键的技术点在于总参数与激活参数的分离：552B 的总参数量决定托管模型所需的内存占用，而 8B 输入、16B 输出的激活量决定单 token 的计算量，因而在很大程度上决定了延迟与服务成本。值得注意的是，该公告并未给出基准测试分数、上下文窗口大小、延迟数据，也没有说明 Causal-Encoder-Decoder 注意力机制的具体实现方式；此外，价格与流量路由的变更都绑定在特定的未来生效日期，而非立即生效。

telegram · zaihuapd · 9月10日 05:54

**背景**: 像混合专家（MoE）这类稀疏架构，刻意把稠密模型混为一谈的两个数字拆开：总参数量决定装载模型所需的内存，激活参数量决定每个 token 消耗的算力，因此一个很大的模型也能以接近小模型的速度运行。DeepSeek 所说的“Causal-Encoder-Decoder”指的是一种混合注意力设计，把因果（从左到右）解码与编码器式组件结合起来，这与大多数大语言模型采用的纯因果解码器结构不同；这类混合设计通常是为了更好地利用完整的双向上下文，而这在多模态场景下对图像输入尤其重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts (MoE) explained for local LLMs · localmodel.run</a></li>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>
<li><a href="https://www.unite.ai/decoder-based-large-language-models-a-complete-guide/">Decoder -Based Large Language Models: A Complete Guide – Unite.AI</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#Multimodal`, `#Model Release`, `#AI API`

---

<a id="item-6"></a>
## [DeepSeek 发布 MIT 许可 Harness 并开放 V4-Pro-0813 权重](https://t.me/zaihuapd/43738) ⭐️ 8.0/10

DeepSeek 发布了以 MIT 协议开源的智能体框架 DeepSeek Harness，把模型、工具、技能、会话、沙箱、存储、调度和 UI 等能力全部实现为可替换插件，并提供标准、PTC、极简和创造四种运行模式。与此同时，DeepSeek-V4-Pro-0813 的模型权重已在 Hugging Face 开放，代码同步发布在 GitHub 与 npm 上。 这为智能体开发者提供了一个完全开源、MIT 许可的替代方案，可以对抗 Claude Code 等闭源编码智能体框架；插件化设计意味着模型厂商、工具供应商和企业可以自由重组整条技术栈，而不必被锁定在某一家厂商的运行时里。开放 V4-Pro-0813 权重则把又一个具备 100 万 token 上下文的前沿级模型放进了可下载的开源权重池，对需要私有化或自托管推理的团队意义重大。 据文档说明，PTC 模式保留标准模式的完整工具集，但通过自动生成的 SDK 和预留的 run_code 传输通道来调用工具：嵌套调用会重新进入带保护的工具流水线，安全调用可以并行重叠，而独占调用则充当排序屏障，且副作用不会回滚，因此 token 节省幅度取决于具体工作负载。DeepSeek-V4-Pro-0813 被描述为采用高效 MoE 架构、面向编码任务可扩展到 100 万 token 上下文窗口的模型，第三方榜单显示的 API 价格约为每百万输入 token 0.435 美元、每百万输出 token 0.87 美元。

telegram · zaihuapd · 9月10日 07:28

**背景**: 所谓“智能体框架（agent harness）”是位于语言模型与外部世界之间的运行时层：它提供工具（文件编辑、shell、网页搜索），管理会话与上下文，并通过沙箱等机制施加安全防护。DeepSeek Harness 把这些能力统统做成插件，使框架可以由可互换的部件组装而成，而不是一个铁板一块的成品。“开放权重”指模型的参数被公开发布，任何人都可以下载并在本地运行，这与只能远程调用的纯 API 模型形成对比；MoE（混合专家）则是一种每个 token 只激活部分网络的架构，能够在规模较大时降低推理成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness: Everything is a Plugin. · GitHub</a></li>
<li><a href="https://agentspulse.github.io/tutorials/deepseek-harness-ptc-mode/">DeepSeek Harness PTC Mode: How run_code Works | AgentsPulse</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#open-source`, `#llm`, `#model-release`, `#ai-agents`

---