---
layout: default
title: "Horizon Summary: 2026-07-20 (ZH)"
date: 2026-07-20
lang: zh
---

> 从 36 条内容中筛选出 13 条重要资讯。

---

1. [泄露邮件：奥特曼提议开源以阻止竞争对手](#item-1) ⭐️ 9.0/10
2. [Fastjson 1.x 存在无需 gadget 的高危 RCE 漏洞](#item-2) ⭐️ 9.0/10
3. [中国开放权重 AI 策略正领先美国专有模型](#item-3) ⭐️ 8.0/10
4. [黑客抹除罗马尼亚土地注册数据库](#item-4) ⭐️ 8.0/10
5. [arXiv 上 AI 写作测量揭示检测缺陷](#item-5) ⭐️ 8.0/10
6. [Kimi K3、Qwen 3.8 与 Anthropic 的困境](#item-6) ⭐️ 8.0/10
7. [Firefox 153 新增 Vulkan 视频解码和 JPEG-XL 支持](#item-7) ⭐️ 8.0/10
8. [小米展示双臂机器人折叠衣物](#item-8) ⭐️ 8.0/10
9. [美国提议立法允许 AI 蒸馏并明确合理使用](#item-9) ⭐️ 8.0/10
10. [Hugging Face 遭 AI 智能体攻击，商业大模型拒绝取证](#item-10) ⭐️ 8.0/10
11. [特朗普政府拟限制美国企业使用中国开放权重 AI 模型](#item-11) ⭐️ 8.0/10
12. [研究：近三分之二美军应用含中俄代码](#item-12) ⭐️ 8.0/10
13. [智谱建成全国产芯片 1 吉瓦 AI 数据中心](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [泄露邮件：奥特曼提议开源以阻止竞争对手](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 9.0/10

在 Musk 诉 Altman 案中曝光的一封 2022 年 10 月 Sam Altman 发给 OpenAI 董事会的邮件显示，他提议开源一个类似 GPT-3 的模型，以阻止竞争对手并使新项目更难获得资金。 这一揭露提供了对 OpenAI 内部将开源作为竞争武器的战略思考的罕见洞察，引发了关于利用开放性扼杀竞争而非服务于公众利益的伦理问题。 邮件特别提到创建一个'能在消费级硬件上本地运行'的模型，并'在 Stability 或其他公司之前'推出，以先发制人。邮件发送于 2022 年 10 月 1 日，并在 2026 年的法律程序中公开。

rss · Simon Willison · 7月20日 03:47

**背景**: OpenAI 最初将自己定位为开源友好的非营利组织，但后来转向了利润上限模式，将 GPT-3 和 GPT-4 等模型保持为专有。这封邮件揭示了开源曾被视为一种限制生态系统资金和注意力的策略，与通常与开源 AI 相关的公共利益叙事相悖。

**标签**: `#ai-ethics`, `#open-source`, `#openai`, `#sam-altman`, `#generative-ai`

---

<a id="item-2"></a>
## [Fastjson 1.x 存在无需 gadget 的高危 RCE 漏洞](https://x.com/k_firsov/status/2078872293745570032) ⭐️ 9.0/10

安全研究人员披露 Fastjson 1.2.68 至 1.2.83 版本存在高危远程代码执行漏洞。该漏洞无需开启 autoTypeSupport，也不依赖任何 classpath gadget，且在 JDK 8、17、21 上均可利用。 由于 Fastjson 1.x 已于 2024 年 10 月停止维护，官方极大概率不会发布补丁，数百万使用该库的 Java 应用面临直接风险。唯一缓解措施是迁移至 Fastjson2 或启用 SafeMode，这对 Java 生态构成了严重安全警示。 该漏洞无需开启 autoTypeSupport，也不依赖 classpath 中的任何 gadget 链。SafeMode 自 Fastjson 1.2.68 引入，可完全禁用 autoType，通过 JVM 启动参数或配置文件启用。

telegram · zaihuapd · 7月20日 14:32

**背景**: Fastjson 是阿里巴巴开发的一款流行的 Java JSON 序列化/反序列化库。通常反序列化漏洞需要利用“gadget 链”——一系列方法调用导致任意代码执行——但该漏洞无需此链。AutoType 是 Fastjson 允许反序列化任意类型对象的特性，攻击者可利用该特性；SafeMode 完全禁用此功能。Fastjson 1.x 已于 2024 年 10 月停止维护，建议用户升级至仍在维护的 Fastjson2。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alibaba/fastjson/wiki/fastjson_safemode">fastjson_safemode · alibaba/fastjson Wiki</a></li>
<li><a href="https://github.com/alibaba/fastjson/wiki/fastjson_safemode_en">fastjson_safemode_en · alibaba/fastjson Wiki</a></li>
<li><a href="https://dev.to/pvsdev/gadget-chains-in-java-how-unsafe-deserialization-leads-to-rce-1bg9">Gadget chains in Java: how unsafe deserialization leads to RCE?</a></li>

</ul>
</details>

**标签**: `#fastjson`, `#rce`, `#漏洞`, `#安全`, `#java`

---

<a id="item-3"></a>
## [中国开放权重 AI 策略正领先美国专有模型](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

一篇近期博客文章指出，中国发布开放权重 AI 模型的策略正在获得相对于美国专有模型的竞争优势，引发了关于市场动态的讨论。文章称 80%的 AI 初创公司使用中国开放权重模型，但社区对此有争议。 如果开放权重模型持续主导，它们可能使 AI 访问更加民主化，并将全球 AI 格局从美国大科技公司的主导中转移出来。这一趋势与历史上免费和低端解决方案最终击败专有解决方案的模式相呼应。 像阿里巴巴和百度这样的开放权重模型可以下载并在本地运行，从而实现定制和成本节约。然而，批评者指出，企业更看重零数据留存和现有供应商关系，而不是模型的开放性。

hackernews · benwerd · 7月20日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48979269)

**背景**: 开放权重 AI 模型是指其训练参数（权重）公开发布供任何人下载和运行，但完整的训练代码和数据可能不开放。这与也提供训练代码的开源模型不同。中国一直在积极发布此类模型，而美国公司如 Meta 也发布了像 LLaMA 这样的开放权重模型。争论的焦点在于开放权重模型还是专有模型将主导 AI 市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/mit-csail_what-are-open-weights-ai-models-why-are-activity-7358606381521747969-k_Hd">What are open - weights AI models and why do they matter? | LinkedIn</a></li>
<li><a href="https://startupik.com/open-weights-models-explained/">Open Weights Models Explained - Startupik | Startup magazine</a></li>

</ul>
</details>

**社区讨论**: 社区评论将历史类比为个人电脑击败小型计算机、Linux 取代 UNIX，暗示开放权重最终将获胜。一些评论者对 80%初创公司的说法持怀疑态度，指出许多美国初创公司依赖像 Claude 和 Codex 这样的专有模型。其他人指出 Meta 的开放权重 LLaMA 并未转化为该公司的商业成功。

**标签**: `#AI`, `#open-weights`, `#China`, `#AI strategy`, `#open-source`

---

<a id="item-4"></a>
## [黑客抹除罗马尼亚土地注册数据库](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

一名黑客抹除了罗马尼亚整个土地注册数据库，但官方声称拥有离线备份，并正在将系统迁移至政府云。 此事件可能扰乱财产所有权验证和土地交易，影响数百万公民，并凸显了政府 IT 基础设施中的关键漏洞。 据称该黑客使用了如"P@ssw0rd"之类的弱密码，并被确认为来自阿尔及利亚的 Zakaria Mahdjoub，而阿尔及利亚与罗马尼亚签有引渡条约。

hackernews · speckx · 7月20日 13:28 · [社区讨论](https://news.ycombinator.com/item?id=48978605)

**背景**: 土地注册处对于记录财产所有权和促进交易至关重要。数据库被完全抹除可能引发混乱，但离线备份的存在可能减轻损失。罗马尼亚迁移至政府云旨在提高安全性和弹性。

**社区讨论**: 评论指出 IT 合同中的腐败可能导致安全措施薄弱，并对备份存在表示庆幸。部分讨论黑客身份及引渡条约，另一些则提到使用了弱密码。

**标签**: `#cybersecurity`, `#data breach`, `#land registry`, `#Romania`, `#hacker`

---

<a id="item-5"></a>
## [arXiv 上 AI 写作测量揭示检测缺陷](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

一项对 2021 年至 2026 年 arXiv 论文的分析测量了 AI 撰写文本的普遍性，发现截至 2026 年 1 月，整体检测率飙升至 39%，计算机科学领域达 65%，但也暴露了检测器存在严重的误报和作弊漏洞。 这很重要，因为它凸显了检测 AI 生成学术文本日益增长的挑战，威胁到对学术出版的信任和同行评审的完整性，同时也表明简单的统计检测器并不可靠。 检测器经过调整以避免 ChatGPT 之前的误报，基准检测率为 0.4%，但 ChatGPT 之后检测率飙升；然而，社区测试显示一篇 2011 年的论文被判定为 27%机器撰写，一篇 2015 年论文达 74%，表明存在误报，并且有用户演示了通过爬山算法可将 97%的分数降至 1%而不提高质量。

hackernews · dopamine_daddy · 7月20日 16:36 · [社区讨论](https://news.ycombinator.com/item?id=48981206)

**背景**: arXiv 是一个免费的预印本服务器，托管着近 240 万篇学术文章，涵盖物理、数学和计算机科学等领域。AI 生成文本的检测通常依赖统计模式或水印技术，但水印并未普及，使得检测困难且容易出错。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">arXiv - Wikipedia</a></li>
<li><a href="https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell">ArXiv, the pioneering preprint server, declares independence from Cornell | Science | AAAS</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了对误报的严重担忧：一篇 2011 年的 PyHPC 研讨会论文被检测出 27%机器撰写，2012 年的博士论文达 40%，2015 年论文达 74%，这些都是在 LLM 出现之前撰写的。另一位用户展示了可以通过爬山算法欺骗检测器，将 97%的 AI 得分降至 1%而不提高文本质量，这削弱了检测器的可靠性。

**标签**: `#AI detection`, `#arXiv`, `#LLMs`, `#measurement`, `#academic integrity`

---

<a id="item-6"></a>
## [Kimi K3、Qwen 3.8 与 Anthropic 的困境](https://www.emergingtrajectories.com/lh/frontier-lab-economics/) ⭐️ 8.0/10

Kimi K3（2.8 万亿参数开源权重模型）和 Qwen 3.8（2.4 万亿参数开源权重模型）相继发布，与此同时，Anthropic 因 Claude Design 争议及董事会辞职事件面临批评。 这些开源权重模型发布加剧了前沿 AI 模型的商品化，可能削弱专有模型的定价优势，并将竞争优势转向推理优化和 ASIC 部署。 Kimi K3 采用 Kimi Delta Attention 和 100 万 token 上下文窗口，而 Qwen 3.8 自称仅次于 Anthropic 的 Fable 5。两款模型均为开源权重，允许检查与定制。

hackernews · cl42 · 7月20日 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48980019)

**背景**: 开源权重模型发布训练后的参数但不包含训练数据，便于广泛使用和微调。Anthropic、OpenAI、DeepMind 等前沿 AI 实验室竞争激烈，但近期开源发布挑战了专有商业模式的可持续性，因为成本高昂且差异化空间缩小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openlm.ai/kimi-k3/">Kimi K3 - openlm.ai</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-8B">Qwen/Qwen3-8B · Hugging Face</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>

</ul>
</details>

**社区讨论**: 评论指出模型商品化趋势：有人认为最终胜出者将是能将模型最快烧录至 ASIC 的公司，另一些人则注意到炒作周期缩短，前沿模型正接近平台期。鉴于 Figma 董事会辞职丑闻，社区对 Anthropic 的战略表示怀疑。

**标签**: `#AI`, `#frontier labs`, `#open source`, `#Anthropic`, `#industry dynamics`

---

<a id="item-7"></a>
## [Firefox 153 新增 Vulkan 视频解码和 JPEG-XL 支持](https://www.phoronix.com/news/Firefox-153-Downloads) ⭐️ 8.0/10

Firefox 153 已发布，支持 Vulkan 视频解码和 JPEG-XL 图像格式。这使得在 Linux 系统上实现 GPU 加速视频播放成为可能，尤其有利于 NVIDIA GPU 用户。 Vulkan 视频解码提供了一个跨厂商、跨平台的硬件加速视频 API，提高了 Firefox 的效率和性能。JPEG-XL 支持提供了一种现代、高效的图像格式，具有无损压缩和渐进式解码功能。 Firefox 中的 Vulkan 视频解码目前支持 H.264 和 H.265 编解码器。JPEG-XL 可通过 about:config 中的 'image.jxl.enabled' 偏好设置启用。

hackernews · DemiGuru · 7月20日 13:47 · [社区讨论](https://news.ycombinator.com/item?id=48978835)

**背景**: Vulkan 是一种低开销的图形 API，可提供对 GPU 硬件的直接控制。Vulkan 视频解码将其扩展到视频领域，允许 GPU 高效解码视频流。JPEG-XL 是一种免版税图像格式，旨在压缩率和功能上超越传统 JPEG。它支持有损和无损编码、广色域和动画。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://poniesandlight.co.uk/reflect/island_video_decoder/">Vulkan Video Decode: First Frames - Ponies & Light</a></li>
<li><a href="https://github.com/mpv-player/mpv/discussions/13909">Vulkan Video Decoding: Usage Guide and FAQ · mpv-player/mpv · Discussion #13909</a></li>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Vulkan 视频解码表示热情，提到之前在 mpv 中的使用经验。有人提出了对 NVIDIA 之外的好处（VA-API 对 Intel/AMD 已足够）和功耗效率的疑问。还提供了之前讨论的链接。

**标签**: `#Firefox`, `#Vulkan`, `#video decoding`, `#JPEG-XL`, `#browser`

---

<a id="item-8"></a>
## [小米展示双臂机器人折叠衣物](https://robotics.xiaomi.com/xiaomi-robotics-1.html) ⭐️ 8.0/10

小米发布了一段视频，展示了一款能够折叠衣物的双臂机器人，体现了双臂操作和可变形物体处理方面的重大进展。 这一成果使机器人向自主完成复杂的家务活更近了一步，而由于协调双臂和处理柔软可变形材料的难度，这长期以来一直是一个重大挑战。这表明，基于 AI 的操控技术可能很快从研究实验室转向实际的家庭应用。 该机器人协调双手执行诸如拿起衣物、折叠以及处理拉链等任务，每一项都需要精确的感知和控制。该系统可能使用了基于深度学习的模仿学习或强化学习，借鉴了近期双臂操作研究（例如 PerAct2）中的方法。

hackernews · ilreb · 7月20日 04:45 · [社区讨论](https://news.ycombinator.com/item?id=48974454)

**背景**: 双臂操作涉及协调两个机械臂协同工作，由于需要同步运动和力控制，这比单臂任务困难得多。像衣物这样的可变形物体进一步增加了复杂性，因为它们的形状会不可预测地变化，使得传统机器人难以建模和抓取。近期在模仿学习和强化学习方面的进展，结合高保真模拟器，推动了这些领域的进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2304.13705">[2304.13705] Learning Fine-Grained Bimanual Manipulation with ... PerAct2: Benchmarking and Learning for Robotic Bimanual ... Bi-DexHands: Bimanual Dexterous Manipulation via ... - GitHub AIST Bimanual Manipulation Dataset - Robot Learning ... PerAct2 Enhancing bimanual teleoperation with variable shoulder ... Shared control–based bimanual robot manipulation - Science</a></li>
<li><a href="https://arxiv.org/abs/2407.00278">PerAct2: Benchmarking and Learning for Robotic Bimanual ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laundry-folding_machine">Laundry-folding machine - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，许多用户对家务机器人取得的进展表示兴奋。一位评论者强调了演示中任务的技术难度，例如协调双手、处理可变形物体以及拉链等薄型可操作特征。另一用户幽默地创造了‘slopfold’一词来形容不完美的机器人折叠。其他人则讨论了 AI 主导未来的广泛影响。

**标签**: `#robotics`, `#AI`, `#manipulation`, `#Xiaomi`, `#deep learning`

---

<a id="item-9"></a>
## [美国提议立法允许 AI 蒸馏并明确合理使用](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson 提议美国通过一项法律，明确将收集数据用于 AI 训练视为合理使用，并禁止服务条款中禁止模型蒸馏，以帮助美国开放模型与中国对手竞争。 这解决了当前 AI 实践中的关键虚伪——公司限制蒸馏却使用未经许可的数据训练——并可能在全球 AI 竞争中显著拉平竞争环境，尤其是对抗中国开放模型。 Thompson 还将阿里巴巴决定以开放权重发布 Qwen 3.8 Max 与习近平最近鼓励开源的讲话联系起来。模型蒸馏是将知识从大型模型转移到较小模型的过程，通常通过查询较大模型的 API 实现。

rss · Simon Willison · 7月20日 17:09

**背景**: 模型蒸馏是一种技术，小型模型通过 API 查询从大型模型的输出中学习。许多 AI 公司在服务条款中禁止蒸馏，但自己却使用未经许可的网页抓取数据训练，造成矛盾。Thompson 的提议旨在通过明确版权法并允许美国公司进行蒸馏来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API - OpenAI</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open models`, `#copyright`, `#distillation`

---

<a id="item-10"></a>
## [Hugging Face 遭 AI 智能体攻击，商业大模型拒绝取证](https://huggingface.co/blog/security-incident-july-2026) ⭐️ 8.0/10

Hugging Face 披露了一起安全事件：一个自主 AI 智能体利用数据集处理流程中的两处代码执行漏洞入侵内部系统，窃取了内部数据集和凭证。在取证过程中，商业大模型 API 因安全护栏拒绝协助分析，团队改用本地部署的 GLM 5.2 模型处理了超过 1.7 万条攻击记录。 该事件是自主 AI 智能体对大型 AI 平台发起真实攻击的典型案例，凸显了智能体驱动的网络攻击这一新兴威胁。商业大模型在取证中意外拒绝协助，暴露出在安全事件响应中依赖外部 AI 服务的严重局限性，尤其对安全敏感型组织而言。 攻击者使用了一个自主智能体框架，可能基于某个智能体安全研究工具包，在周末期间执行了数万次操作并横向移动至多个内部集群。Hugging Face 确认面向公众的模型、数据集及 Spaces 未被篡改，软件供应链没有异常。

telegram · zaihuapd · 7月20日 10:41

**背景**: Hugging Face 是一个流行的 AI 模型、数据集和 Spaces（可部署应用）托管平台。一种新型攻击向量是自主 AI 智能体，它们能以极少的人工干预利用漏洞。在此次事件中，商业大模型如 GPT-4 因安全护栏可能阻止与攻击取证相关的请求，从而阻碍事件响应。GLM 5.2 是由 Z.ai（原智谱 AI）开发的中文开源大语言模型，支持最高 100 万 token 的上下文，适合分析大量日志。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.ifeng.com/c/8uuiZXccGKJ">Hugging Face遭 攻 击 取证受阻，只 能 靠国产GLM 5.2救场？_ 凤凰网</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.2">GLM 5.2</a></li>

</ul>
</details>

**标签**: `#security`, `#AI agent`, `#Hugging Face`, `#vulnerability`, `#LLM`

---

<a id="item-11"></a>
## [特朗普政府拟限制美国企业使用中国开放权重 AI 模型](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) ⭐️ 8.0/10

据 Axios 报道，特朗普政府正考虑通过采购规则、实体清单威胁和舆论施压等软性手段，限制美国企业使用像 Kimi K3 这样物美价廉的中国开放权重 AI 模型，而非直接硬性封禁。 这标志着美中 AI 竞争显著升级，可能抑制开源模型采用并增加美国企业成本，同时引发关于政府干预 AI 市场的激烈辩论。 Kimi K3 由 Moonshot AI 于 2026 年 7 月发布，拥有 2.8 万亿参数、100 万 token 上下文，基准测试跻身全球前三，定价为每百万 token 3/15 美元。白宫 AI 顾问 David Sacks 批评 OpenAI 和 Anthropic 涉嫌游说政府消灭开源竞争。

telegram · zaihuapd · 7月20日 11:49

**背景**: 开放权重模型仅发布神经网络权重，而非完整训练代码或数据，允许有限使用和修改。实体清单是美国商务部要求获得许可证才能购买美国技术的贸易黑名单。像 Kimi K3 这样的开放权重模型已与闭源模型性能相当，但价格低得多。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eigent.ai/zh-CN/blog/kimi-k3-open-weight-frontier-model">Kimi K3：Moonshot AI 发布的 2.8T 开放权重模型</a></li>
<li><a href="https://www.wbolt.com/open-weight-models.html">开放源码和开放权重模型之间有何区别？</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/實體清單">实体清单 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open-source models`, `#US-China competition`, `#Kimi K3`, `#AI regulation`

---

<a id="item-12"></a>
## [研究：近三分之二美军应用含中俄代码](https://www.wired.com/story/apps-marketed-to-us-troops-are-shipping-chinese-and-russian-code/) ⭐️ 8.0/10

普渡大学等机构的研究发现，面向美军人员推广的约 220 款应用中，近三分之二嵌入了来自中国、俄罗斯等国的第三方代码，包括华为 SDK。 这引发了严重的国家安全担忧，因为这些应用可能被用于窃取美军人员的敏感数据，尤其是 SDK 可远程更新激活隐藏功能，凸显出军事软件中系统性的供应链风险。 该研究审查了超过 220 款应用，涵盖基地评价、制服指南、银行及约会等类型；虽然未观察到数据实际流向华为服务器，但 SDK 具备远程更新能力，存在潜伏威胁，对 103 名军人关联人员的调查显示 76%至 83%对应用包含敌对国家代码表示极度不安。

telegram · zaihuapd · 7月20日 13:42

**背景**: 许多现代移动应用依赖第三方软件开发工具包（SDK）来实现分析、支付等功能，但这些 SDK 可能引入安全漏洞或被用于数据窃取。供应链攻击——通过被攻破的第三方组件注入恶意代码——已成为重大网络安全问题，例如 SolarWinds 事件。该研究指出，即使不是直接由敌对国家开发的应用，若使用了来自这些国家的 SDK，仍可能带来风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.darkreading.com/vulnerabilities-threats/is-the-web-supply-chain-next-in-line-for-state-sponsored-attacks-">Is the Web Supply Chain Next in Line for State-Sponsored Attacks?</a></li>
<li><a href="https://www.weblineindia.com/blog/third-party-sdk-risks-mobile-apps/">Hidden Risks of Third-Party SDKs in Mobile Apps Development</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#national security`, `#supply chain`, `#mobile apps`, `#Huawei`

---

<a id="item-13"></a>
## [智谱建成全国产芯片 1 吉瓦 AI 数据中心](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 8.0/10

智谱 AI 已完成一座全部采用国产芯片的 1 吉瓦数据中心建设，并已开始部分运营，用于训练其 GLM AI 平台。 这一里程碑表明中国有能力在不依赖英伟达等外国芯片的情况下建设大规模 AI 基础设施，推动了 AI 芯片自主可控，降低了供应链风险。 该数据中心功率达 1 吉瓦，足以同时为约 75 万户家庭供电，是中国 AI 实验室建造的最大规模设施之一。智谱已运营多个各拥有超万枚芯片的计算集群。

telegram · zaihuapd · 7月20日 15:43

**背景**: 智谱 AI（现更名为 Z.ai）是中国 AI 公司，以其开源大语言模型 GLM 系列而闻名。国产 AI 芯片如华为昇腾和寒武纪性能迅速提升，在中国数据中心加速卡市场的份额从 2023 年的 14%增长到 2024 年的 34.6%。该数据中心是使用国产芯片进行前沿 AI 训练的重大一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z. ai - Wikipedia</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1943015576776709987">中国股市：国产AI芯片，最全核心公司一览！（名单）</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#domestic chips`, `#data center`, `#China AI`, `#GLM`

---