---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 40 条内容中筛选出 9 条重要资讯。

---

1. [Keyv 及相关 npm 包在 Shai-Hulud 供应链攻击中遭入侵](#item-1) ⭐️ 9.0/10
2. [简单算法与色彩空间生成多样肤色](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 token/秒](#item-3) ⭐️ 8.0/10
4. [苹果扩大诉讼，称更多前员工可能向 OpenAI 泄露机密数据](#item-4) ⭐️ 8.0/10
5. [面向自我改进 AI 智能体的 Harness 工程化](#item-5) ⭐️ 8.0/10
6. [Cloudflare 弃用第三方安全工具，用 58 美元/月 AI 处理漏洞赏金](#item-6) ⭐️ 8.0/10
7. [谷歌为 Anthropic 搭起 2000 亿美元 AI 芯片融资机器](#item-7) ⭐️ 8.0/10
8. [我国首部 L3/L4 自动驾驶强制性国标报批，2027 年实施](#item-8) ⭐️ 8.0/10
9. [英伟达 CEO 黄仁勋支持使用中国开源 AI 模型](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Keyv 及相关 npm 包在 Shai-Hulud 供应链攻击中遭入侵](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 9.0/10

一起新的 Shai-Hulud 供应链攻击通过恶意的 pre-install 钩子入侵了流行的 npm 包 Keyv 以及 cacheable 等相关包。JFrog 研究人员发现该蠕虫会窃取凭据、将自身发布到所有可写的 npm 包中，并在 GitHub 仓库中植入执行钩子。 Keyv 是一个被广泛使用、拥有数千个依赖项目的键值存储库，因此这次零日攻击可能在 npm 生态系统中传播，导致凭据泄露和下游连锁入侵。这凸显了采取更严格的注册表治理和更强防御措施以抵御恶意安装脚本的紧迫性。 该恶意软件利用了包安装时自动运行的 pre-install 钩子，最初是在新发布的 Keyv 版本中被发现。据 JFrog 称，该活动已影响超过 400 个包，npm 正在努力移除被报告的包。

hackernews · cimi_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: 供应链攻击通过入侵受信任的上游依赖来实现，开发者在安装包时恶意代码就会执行。pre-install 和 post-install 钩子是 npm 自动运行的脚本，因此成为此类攻击的主要载体。Shai-Hulud 是一个已知的恶意软件活动，通过入侵 npm 包来传播。Keyv 是一个简单的键值存储库，支持多种后端，因此有大量项目依赖它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.jfrog.com/post/shai-hulud-is-back-august/">Major Shai Hulud campaign strikes npm again, affecting keyv and 400+ packages - JFrog Security Research</a></li>
<li><a href="https://www.npmjs.com/package/keyv">keyv - npm</a></li>

</ul>
</details>

**社区讨论**: 评论者敦促 npm 限制或弃用 pre-install 钩子，有人建议暂停审批新的钩子，还有人推荐在 .npmrc 中设置 'min-release-age=5'。也有人质疑商业安全工具能否主动检测此类攻击，同时有用户分享了关于 npm 供应链攻击技术的最新文档。

**标签**: `#security`, `#npm`, `#supply-chain`, `#javascript`, `#malware`

---

<a id="item-2"></a>
## [简单算法与色彩空间生成多样肤色](https://toneyalexander.github.io/inclusive-color-space/) ⭐️ 8.0/10

开发者创建了一个新的色彩空间和程序化生成算法，用于生成多样化且合理的肤色，并提供了交互式 JavaScript 取色器和 Python 示例。该项目在 toneyalexander.github.io/inclusive-color-space/上进行了详细说明。 这很重要，因为它为数字艺术和游戏开发中一个长期存在的难题提供了实用、算法驱动的解决方案：选择多样化且逼真的肤色。它可以让游戏、插画和虚拟世界中的角色和头像更具包容性，更好地代表人类真实的多样性。 这个色彩空间是通过对手动拟合的经验肤色数据进行函数拟合而构建的，而不是使用 PCA 等方法，页面还包含了大量方程和交互式演示。作者承认方法论“有点不稳固”，并列出了相关局限性，包括未显式模拟光照条件，以及一个“未来工作”章节。

hackernews · automatoney · 8月4日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49170165)

**背景**: 程序化生成是一种通过算法创建数据的方法，通常结合随机性，广泛应用于游戏和数字艺术。人类肤色并非简单的物理量，它有很大差异，并受光照、感知和生物因素影响。这个项目试图定义一种简化但广泛的肤色色彩空间，使多样化角色的程序化生成更加容易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://toneyalexander.github.io/inclusive-color-space/">What Colors Are We? Constructing A Color Space For Skin Tones</a></li>
<li><a href="https://en.wikipedia.org/wiki/Procedural_generation">Procedural generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human_skin_color">Human skin color - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上很热情，称赞了交互式演示和巧妙的手动拟合函数。建设性的批评指出，局限性部分没有包含光照因素；还有人建议参考如 Pantone 肤色卡等资源，或探索 Oklab 颜色空间，后者曾被用来绘制真实粉底色号数据。

**标签**: `#color science`, `#computer graphics`, `#procedural generation`, `#digital art`, `#skin tone`

---

<a id="item-3"></a>
## [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 token/秒](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

一个 GitHub 项目展示了 DeepSeek V4 Flash 在单块 AMD MI300X 上以每秒超过 150 个 token 的速度运行，使用完整模型权重，仅将上下文窗口从 100 万 token 缩减至 256k。 这使得前沿类 MoE 模型在单块加速器上即可实际运行，相比多 GPU 方案大幅降低了运行 DeepSeek V4 Flash 的硬件成本和复杂度。同时也凸显了 MI300X 大容量 HBM 在单卡大模型推理上的实际优势。 代价是上下文长度：原模型支持 100 万 token，而该方案只提供 256k。MI300X 拥有 192GB HBM3 和 5.3 TB/s 带宽，得益于原生 MXFP4 量化以及仅激活 13B 参数的 MoE 架构，足以容纳 284B 参数的模型。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是面向效率优化的混合专家（MoE）模型，总参数 284B，激活参数 13B，支持 100 万 token 的上下文窗口。AMD MI300X 是基于 CDNA 3 架构的加速器，配备 192GB HBM3 显存，专为大规模 AI 推理设计。要在单张 GPU 上运行如此大的模型，既需要足够的内存存放权重，也需要精心控制上下文窗口以适应硬件限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html">AMD Instinct™ MI300X Accelerators</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V4 Flash 0423 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认可这一实用取舍，认为在保留完整权重和 150+ tok/s 速度的情况下，即使缩减上下文也很不错。多人补充了硬件细节：MI300X 是 OAM 模块，通常以 8 卡整机形式销售；基于 PCIe 的 MI350P 只有 144GB，但由于原生 MXFP4 量化也可能运行；另外 README 中未完全引用 DwarfStar 或 2xMI300X 的先前工作。

**标签**: `#AI/ML`, `#Inference`, `#AMD MI300X`, `#DeepSeek`, `#Hardware`

---

<a id="item-4"></a>
## [苹果扩大诉讼，称更多前员工可能向 OpenAI 泄露机密数据](https://techcrunch.com/2026/08/04/apple-says-more-ex-employees-may-have-taken-confidential-data-to-openai/) ⭐️ 8.0/10

苹果已扩大对 OpenAI 的诉讼，指控更多前员工可能将机密数据带到了这家人工智能初创公司。更新后的起诉文件据称包含对文档截图和苹果系统残留访问权限的指控。 此案可能为 AI 行业的人才流动和知识产权保护树立先例。它还可能削弱 OpenAI 的硬件计划，有些人认为这只是首席执行官萨姆·奥尔特曼的虚荣项目。 这些指控不仅限于员工的记忆——据称还包括对机密文件的截图。苹果也没有坦承，前员工对苹果系统的'残留访问权限'是源于苹果自身糟糕的安全程序，而这一点正是 OpenAI 所强调的。

hackernews · thewebguyd · 8月4日 15:37 · [社区讨论](https://news.ycombinator.com/item?id=49170479)

**背景**: 苹果此前已就员工跳槽至 OpenAI 并涉嫌窃取商业机密（尤其是与硬件工作相关的机密）而对 OpenAI 提起了诉讼。OpenAI 否认了这些指控，并批评苹果的安全做法，指出前员工对苹果系统留有'残留访问权限'。该案反映出更广泛行业紧张局势：AI 公司正积极从老牌科技巨头挖人，引发关于商业机密、竞业限制条款和创新的讨论。OpenAI 自己的硬件项目（旨在开发消费设备）也招致质疑，有人将其比作已失败的 Humane AI Pin。

**社区讨论**: 评论者意见不一：苹果前高管托尼·法德尔称此诉讼是典型的恐吓员工手段；另一些人则批评 OpenAI 的硬件雄心，称之为'虚荣项目'，可能成为'Humane Pin 2.0'。同时，也有人认为这些指控性质严重，因为涉及文档截图而非仅凭记忆，并以此嘲讽 OpenAI 对苹果安全性的批评。

**标签**: `#Apple`, `#OpenAI`, `#Legal`, `#Confidential Data`, `#AI Hardware`

---

<a id="item-5"></a>
## [面向自我改进 AI 智能体的 Harness 工程化](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

Lilian Weng 发布了一篇题为《Harness Engineering for Self-Improvement》的技术文章，探讨如何通过工程化 AI 智能体的 harness（外部支架）来实现自我改进。文章讨论了 Self-Harness 等框架，这类框架利用执行轨迹在迭代、自主的循环中改进智能体的脚手架、工具和提示词。 这件事很重要，因为它开辟了一个新的优化前沿：改进 harness 而不是仅仅改进模型权重，尤其是当一些人认为预训练的收益正在趋于平缓时。它影响着构建 agentic 系统的开发者，也影响着用于衡量和改进智能体在真实部署中行为所需的工具与评估方法。 文章及相关讨论指出，智能体可以通过在生产轨迹上进行自动研究来发现并修复真实问题，甚至能编写自己的工具，例如将上下文加载从 15 次工具调用、约 2 万 token 缩减为一次 session_context 调用、约 800 token。关键的注意事项包括：需要可靠的 fitness function（适应度函数）、evals 以及验证/测试集划分来防止奖励作弊（reward hacking），同时安全和防护层应当置于该循环之外。

hackernews · tosh · 8月4日 06:17 · [社区讨论](https://news.ycombinator.com/item?id=49164896)

**背景**: AI 智能体的 harness（外部支架）通常包含模型、系统提示词、工具、技能以及将它们连接起来的编排代码。Self-harness 类方法让智能体通过挖掘执行轨迹来迭代更新这套脚手架，类似于自我对弈或进化算法——由 fitness function 来引导改进。与此同时，Genetic-Pareto (GEPA) 等框架会采样智能体轨迹、用自然语言进行反思、提出提示词修订，并通过迭代反馈循环来演化整个系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lilianweng.github.io/posts/2026-07-04-harness/">Harness Engineering for Self-Improvement | Lil'Log</a></li>
<li><a href="https://bdtechtalks.com/2026/07/13/ai-agents-self-improving-harness/">How self-improving harnesses are rewriting the agent engineering playbook - TechTalks</a></li>
<li><a href="https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining">Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining</a></li>

</ul>
</details>

**社区讨论**: 评论者总体持乐观态度，并分享了具体经验：一位评论者表示，让智能体读取生产轨迹并允许其编写自己的工具后，harness 上的自动研究“出奇地强大”，同时强调需要用 evals 和训练/测试集划分来防止奖励作弊。另一位网友提问：harness 何时能生成自己的 RLHF/DPO 训练集，并对自身运行的模型做 LoRA 微调；还有一位评论者认为，优化提示词和代码可能比训练权重更具样本效率，尽管这里没有梯度下降。

**标签**: `#AI agents`, `#harness engineering`, `#LLM self-improvement`, `#agentic systems`, `#evals`

---

<a id="item-6"></a>
## [Cloudflare 弃用第三方安全工具，用 58 美元/月 AI 处理漏洞赏金](https://www.theregister.com/security/2026/08/04/cloudflare-has-mostly-ditched-third-party-security-tools-suggests-not-trying-that-at-home/5282600) ⭐️ 8.0/10

Cloudflare 首席安全官 Grant Bourzikas 表示，公司已用 200 多个自研自主代理取代几乎全部第三方安全工具，并使用 Anthropic 的 Claude Sonnet 每月仅花约 58 美元来处理漏洞赏金报告。他同时提醒其他企业不要盲目效仿。 这是一个 AI 驱动安全自动化并附带具体成本数据的真实案例，凸显了与专用安全模型（Mythos 约 20 万美元/月）之间的巨大成本差异。这可能改变企业对安全工具、AI 代理以及厂商合作模式的认知。 Bourzikas 透露，同样的漏洞分诊工作若改用安全专用模型 Mythos，每月成本约 20 万美元。Cloudflare 还将裁员 1100 人归因于 AI 自动化；首席战略官 Stephanie Cohen 表示，公司计划充当 AI 公司与出版商之间的中介，通过微支付让 AI 公司为内容付费。

telegram · zaihuapd · 8月4日 09:24

**背景**: Claude 是 Anthropic 旗下的大语言模型系列，Sonnet 是其中间档型号（另有 Haiku 和 Opus）。Mythos 是 Anthropic 推出的受限访问自主网络安全模型（Mythos Preview），英国 AISI 评测显示它能够自主执行多阶段攻击并发现漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet \ Anthropic</a></li>
<li><a href="https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities">Our evaluation of Claude Mythos Preview’s cyber capabilities | AISI Work</a></li>
<li><a href="https://www.contrastsecurity.com/glossary/mythos-ai">What Is Mythos AI? Autonomous Exploits and AppSec Defense | Contrast Security</a></li>

</ul>
</details>

**社区讨论**: 未提供评论，因此暂无社区讨论内容。

**标签**: `#security`, `#AI`, `#Cloudflare`, `#automation`, `#bug bounty`

---

<a id="item-7"></a>
## [谷歌为 Anthropic 搭起 2000 亿美元 AI 芯片融资机器](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c) ⭐️ 8.0/10

据《金融时报》8 月 4 日调查，谷歌已悄然搭建史上最大规模的基础设施融资架构之一，总额约 2000 亿美元，以向 Anthropic 交付超 1500 亿美元的 AI 芯片。该架构涉及博通、阿波罗、黑石、摩根士丹利及多家加密矿企，采用厂商融资模式在多方之间分摊风险。 这一前所未有的融资结构表明，AI 基础设施正从直接购买硬件转向高杠杆的厂商融资模式，对 AI 经济性和竞争格局意义重大。这也显示谷歌等超大规模云厂商正通过金融工程为关键合作伙伴锁定 AI 算力，而无需让自家资产负债表承受巨额负担。 今年 6 月，名为 Compute SPV 的特殊目的载体完成首批交易，购入约 350 亿美元硬件，约合 1 吉瓦算力和 100 万颗 TPU。该结构借鉴波音和通用电气推销飞机与发动机时的厂商融资玩法：谷歌为数据中心提供担保，博通购买并协助融资芯片，阿波罗和黑石购买硬件后回租给 Anthropic。

telegram · zaihuapd · 8月4日 10:52

**背景**: 厂商融资是一种由供应商（或其关联融资实体）提供贷款或租赁来帮助客户购买自家产品的模式，波音和通用电气在飞机与发动机销售中常用。在 AI 基础设施领域，这种方式正日益流行，因为超大规模云厂商和 Anthropic 等 AI 实验室需要海量算力，却无法将数千亿美元硬件成本全部压在资产负债上。特殊目的载体（SPV）是为隔离金融风险而设立的子公司，如今越来越多地被用来汇聚投资者资本以支持 AI 算力交易。谷歌的张量处理单元（TPU）是为神经网络机器学习设计的专用集成电路（ASIC），正是本次交易的核心硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/s/spv.asp">investopedia.com/terms/s/ spv .asp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/what-circular-ai-deals-reveal-current-strategy-harsha-srivatsa-htvcc">What Circular AI Deals Reveal about current AI Strategy</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Anthropic`, `#Google`, `#financing`, `#TPU`

---

<a id="item-8"></a>
## [我国首部 L3/L4 自动驾驶强制性国标报批，2027 年实施](https://t.me/zaihuapd/42972) ⭐️ 8.0/10

工信部已完成首部针对 L3/L4 级自动驾驶的强制性国家标准《智能网联汽车自动驾驶系统安全要求》报批稿，自 6 月 17 日起公示，建议 2027 年 7 月 1 日实施。 这一里程碑将中国自动驾驶监管从非强制性的指导转向可强制执行的硬约束，要求车企以严谨的证据论证安全性，而非依靠宣传话术。这将重塑全球最大汽车市场上 L3/L4 车型的开发周期与市场竞争格局。 标准引入了 Safety Case（安全档案）机制，要求企业以『声明—论据—证据』的结构系统性论证安全性，并分别对 L3 级的人机交接和 L4 级的系统自主风险处置提出要求。

telegram · zaihuapd · 8月4日 13:06

**背景**: 自动驾驶按照 SAE J3016 和中国 GB/T 40429-2021 等标准划分为 L0 至 L5 共六个等级。L3 为『有条件自动化』，驾驶员需随时准备接管；L4 为『高度自动化』，系统可在无需人工介入的情况下自主处置风险。此前中国的自动驾驶监管多为自愿性要求，而这项强制性国标要求车企以结构化的 Safety Case（安全档案）作为安全性证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/L01347E80547KOTE.html">163.com/dy/article/L01347E80547KOTE.html</a></li>
<li><a href="https://auto-time.36kr.com/p/1373076185888129">自 动 驾 驶 不等于零事故，但也不该被“妖魔化”_36氪</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#regulation`, `#safety`, `#China`, `#automotive`

---

<a id="item-9"></a>
## [英伟达 CEO 黄仁勋支持使用中国开源 AI 模型](https://t.me/zaihuapd/42977) ⭐️ 8.0/10

英伟达 CEO 黄仁勋在采访中表示，中国开源 AI 模型“非常优秀”，美国企业“绝对”应该获准使用。他还反对以国家安全为由全面限制开源模型，认为免费或更便宜的 AI 会扩大用户规模，增加对芯片和数据中心的需求。 作为行业领军人物，黄仁勋的言论可能影响关于 AI 监管和国家安全的政策辩论。这凸显了创新与安全之间的张力，并可能影响美国企业采用全球开源 AI 模型的方式以及芯片需求的走向。 黄仁勋提出，企业下载的中国模型可以在安全沙箱中受控使用，开放代码也便于研究人员发现漏洞、加强防御。他还主张针对具体的隐私或合同违规行为处理知识产权争议，而不是全面限制相关模型类别。

telegram · zaihuapd · 8月4日 15:22

**背景**: 开源 AI 模型是指代码公开可访问的模型，允许广泛使用和修改。沙箱是一种安全实践，通过隔离软件来限制潜在危害，而 OWASP 等组织则提供针对大型语言模型安全评估的框架。近期，DeepSeek R1 等中国开源模型引发全球关注，也带来了关于其安全性和使用的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aisafetyhub.au/ai-sandbox">The AI Sandbox — AI Safety Hub</a></li>
<li><a href="https://owasp.org/www-project-top-10-for-large-language-model-applications/">OWASP Top 10 for Large Language Model ... | OWASP Foundation</a></li>
<li><a href="https://opentools.ai/news/deepseek-r1-the-open-source-ai-model-making-waves-for-all-the-wrong-reasons">DeepSeek R1: The Open - Source AI Model Making... | OpenTools</a></li>

</ul>
</details>

**标签**: `#AI`, `#开源模型`, `#AI政策`, `#黄仁勋`, `#英伟达`

---