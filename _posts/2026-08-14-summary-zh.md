---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 33 条内容中筛选出 12 条重要资讯。

---

1. [GLM-5.3 模型展示涌现式网络能力，实现自主安全研究](#item-1) ⭐️ 9.0/10
2. [将《毁灭战士》渲染器编译为 21B 参数 Transformer，无需训练](#item-2) ⭐️ 9.0/10
3. [Qwen3.8-27B 开放权重模型在笔记本电脑上表现出色](#item-3) ⭐️ 8.0/10
4. [Opus 5 的省略式风格为何用起来更难受？](#item-4) ⭐️ 8.0/10
5. [法国最高法院阻止禁止 15 岁以下青少年使用社交媒体](#item-5) ⭐️ 8.0/10
6. [PyTorch 静态检查工具 torch-preflight：提前发现训练错误并估算显存](#item-6) ⭐️ 8.0/10
7. [Vivodyne AI 机器人实验室年测 300 万人体组织样本](#item-7) ⭐️ 8.0/10
8. [小红书开源 280B MoE 模型，仅 16B 激活参数](#item-8) ⭐️ 8.0/10
9. [法官责令谷歌一周内取消第三方应用商店安装障碍](#item-9) ⭐️ 8.0/10
10. [苹果官宣换帅：库克卸任 CEO，特努斯接任](#item-10) ⭐️ 8.0/10
11. [PostgreSQL 修复 to_char 高危漏洞，可致远程代码执行](#item-11) ⭐️ 8.0/10
12. [苹果与阿里联手自研中国专属 AI 模型，或成首个获批外企](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM-5.3 模型展示涌现式网络能力，实现自主安全研究](https://z.ai/blog/glm-5.3) ⭐️ 9.0/10

Z.ai 发布了最新旗舰模型 GLM-5.3，在带来前沿编程能力的同时，还展现出涌现式网络能力，支持自主安全研究和大规模漏洞发现。该模型与 GLM-5.2 共享同一基础模型，所有改进均来自后训练阶段。 社区报告显示，GLM-5.3 能自主发现零日漏洞并适配内核漏洞利用，标志着 AI 模型在攻防两端网络安全应用上的重大转变。这一突破也引发了关于漏洞披露伦理和 AI 驱动安全研究可操作性的紧迫问题。 根据 Z.ai 官方文档，GLM-5.3 在复杂软件工程基准测试上较 GLM-5.2 提升 50%，采用相同基础模型并依靠后训练增强。该模型面向长时程编码和智能体任务设计，Z.ai 还建立了协调漏洞披露站点，列出了众多流行软件的 CVE，其中许多仍在保密期内。

hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

**背景**: AI 的涌现能力是指大型模型随着规模、算力和训练数据增长而突然出现的能力，例如 GLM-5.3 所展示的网络安全技能。后训练指在基础模型训练完成后应用的微调和对齐流程，可显著增强编程和智能体工作流等专门能力。自主漏洞发现利用 AI 智能体通过静态分析、模糊测试和符号执行来识别和验证安全弱点，GLM-5.3 据称推动了这一领域的发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM - 5 . 3 - Overview - Z. AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://models.dev/models/zhipuai/glm-5.3/">GLM - 5 . 3 pricing, providers, and specs | Models .dev</a></li>
<li><a href="https://www.practical-devsecops.com/glossary/emergent-capabilities/">Emergent Capabilities in AI: Unexpected Abilities in Large Models</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体正面但有所保留：用户报告 GLM-5.3 能自主处理红队场景并披露零日漏洞，同时也有评论指出它仍略逊于 Sol 和 Fable 等竞品，且 Mythos 5 在某些利用链任务上领先。多位评论者还表达了对大规模开源软件漏洞扫描的伦理与成本的担忧，并赞赏 Z.ai 博文的学术化写作风格。

**标签**: `#AI`, `#LLM`, `#cybersecurity`, `#coding`, `#GLM`

---

<a id="item-2"></a>
## [将《毁灭战士》渲染器编译为 21B 参数 Transformer，无需训练](https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/) ⭐️ 9.0/10

一个名为 Torchwright 的编译器将《毁灭战士》的渲染算法转换为计算图，再转换为标准 21B 参数 Transformer 检查点的权重。该模型通过生成简单的像素绘制指令来渲染游戏画面，完全无需训练。 这项工作表明，Transformer 权重可以通过解析方式构造来执行任意命令式算法，为可解释性和神经执行开辟了新途径。它还凸显了鲜明的性能对比：原始《毁灭战士》在 486 上以 35 FPS 运行，而这个 21B 模型在 B200 上大约每天只能渲染 35 帧。 每渲染一帧需要 3,614 个 token 的提示词加上 53,747 个生成 token，在 B200 上耗时略超 40 分钟。生成的检查点是标准的 Hugging Face 检查点，无需 trust_remote_code 即可加载，而用于加载、生成和解析输出的宿主程序仅有 43 行 Python 代码。

reddit · r/MachineLearning · /u/notforrob · 8月14日 15:50

**背景**: Transformer 通常在大规模数据集上训练以学习模式，但这个项目而是通过计算图解析地构造权重。Torchwright 是一个编译器，能将普通 Python 定义的计算图转换为 Transformer 权重，实现有时被称为“神经执行”的无梯度下降执行。《毁灭战士》的渲染器由 id Software 于 1993 年创建，是使用射线投射和 BSP 树绘制 3D 场景的经典软件渲染器，在历史上具有重要意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/physicsrob/torchwright/tree/main">GitHub - physicsrob/torchwright: A compiler that transforms ...</a></li>
<li><a href="https://towardsdatascience.com/i-built-a-tiny-computer-inside-a-transformer/">I Built a Tiny Computer Inside a Transformer | Towards Data ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Doom_engine">Doom engine - Wikipedia</a></li>

</ul>
</details>

**标签**: `#transformer`, `#compiler`, `#Doom`, `#rendering`, `#neural execution`

---

<a id="item-3"></a>
## [Qwen3.8-27B 开放权重模型在笔记本电脑上表现出色](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

Qwen 于 2026 年 8 月 14 日发布了开放权重大语言模型 Qwen3.8-27B。这个 27B 参数的模型能在消费级笔记本电脑上运行，并取得了强劲的基准测试成绩，包括在 SWE-bench Pro 上达到 61.7。 此次发布表明，开放权重模型在本地运行的同时也能与专有系统抗衡，拓宽了开发者的使用途径，并降低了对昂贵云 API 的依赖。这可能加速设备端 AI 的普及，并改变模型提供商的竞争格局。 该模型可在 Hugging Face 上以 FP8 和 GGUF 量化格式获取，Unsloth 也提供了社区构建的版本。在社区基准测试中，它在 DeepSWE 上以 42.2 比 40.0 超过了 Claude Opus；不过许多用户仍在期待 Qwen 推出 MoE（混合专家）版本。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**背景**: 开放权重模型是指将训练得到的核心参数公开发布，任何人都可以下载并在本地运行。参数数量（例如 27B）大致体现模型的规模和能力，同时也决定了所需的硬件配置。Qwen3.8-27B 是继 Qwen3.8-Max 之后发布的开放权重模型，其基准成绩表明它能在中等配置硬件上完成复杂的编码任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026">Qwen 3.8 27B: Specs, Hardware Requirements, and How to Run It (2026)</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，有用户称赞该模型在笔记本电脑上的出色表现，称它是“在笔记本上跑过的最好的鹈鹕”。还有人将其与 Claude Opus 在编程基准上对比并认为表现更好，同时也有用户希望未来能推出 MoE 变体。讨论中还出现了大量实际基准测试数据和量化下载链接。

**标签**: `#AI`, `#LLM`, `#Qwen`, `#open-source`, `#machine-learning`

---

<a id="item-4"></a>
## [Opus 5 的省略式风格为何用起来更难受？](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) ⭐️ 8.0/10

这篇文章认为，尽管 Claude Opus 5 能力更强，但因其省略式写作风格和过多的元评论，使用体验反而更差。该文章在 Hacker News 引发广泛讨论，获得 604 分和 568 条评论。 作为 Anthropic 的前沿模型之一，Opus 5 被广泛用于编程和知识工作，因此它的沟通风格直接影响开发者的效率和用户满意度。广泛的批评表明，单纯的能力提升还不够，交互方式和表达风格正成为大模型竞争的关键战场。 文章指出，Opus 5 相比 Opus 4.8 有显著提升，在深度推理和智能体任务上表现更好，但批评其句子总是绕圈子并像揭示悬念一样抛出观点。有用户称已转向 OpenAI Sol 等替代品，也有人认为 Opus 5 质量下降，可能是一个更小或更经济的模型。

hackernews · numeri · 8月14日 10:12 · [社区讨论](https://news.ycombinator.com/item?id=49296740)

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，自 Claude 3 起每一代通常按三种规模发布：Haiku、Sonnet 和 Opus，其中 Opus 最强。Claude Opus 5 于 2026 年 7 月 24 日发布，被描述为一个深思熟虑、主动的模型，以一半的价格接近 Claude Fable 5 的前沿智能水平。这篇文章的批评侧重与模型互动的主观体验，而这一维度常被基准分数所掩盖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus">Claude Opus</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5">What's new in Claude Opus 5 - Claude Platform Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认同文章的观点，称 Opus 5 的写作风格省略、令人疲惫，且充满不必要的“坦白”和元评论。有人表示已转向 OpenAI Sol 或退回 Opus 4.8，也有人进行更深的哲学讨论，认为模型的沟通方式本身就是训练体系下的一种产物。少数用户质疑模型质量确实下降，并猜测 Anthropic 是否存在经济方面的动机。

**标签**: `#AI`, `#LLM`, `#Claude`, `#UX`, `#Communication`

---

<a id="item-5"></a>
## [法国最高法院阻止禁止 15 岁以下青少年使用社交媒体](https://www.reuters.com/world/frances-top-court-rules-social-media-ban-curtails-freedom-expression-2026-08-14/) ⭐️ 8.0/10

法国最高法院驳回了一项禁止 15 岁以下青少年使用社交媒体的提案，裁定其过度侵犯言论自由和隐私权。据路透社报道，该裁决于 2026 年 8 月 14 日作出。 这一裁决为法国及欧洲的互联网监管确立了重要法律先例，确认年龄验证要求必须尊重基本权利。它可能影响其他国家在未来制定儿童网络安全法律和隐私保护政策的方式。 法院认为，禁止 15 岁以下青少年使用社交媒体属于过度的限制，而且年龄验证系统实际上会变成身份验证工具，威胁所有用户的隐私。法院还指出，设备层面的家长控制等限制较少的替代方案也能达到类似目的。

hackernews · BlueBerry2001 · 8月14日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=49300671)

**背景**: 近年来，法国和其他国家纷纷提出要求社交媒体进行年龄验证的法律，以保护未成年人免受有害内容和网络风险的影响。但隐私倡导者认为，这些措施往往导致大规模监控并削弱匿名表达的空间。法国法院的这一裁决反映了儿童安全与公民自由之间的紧张关系。

**社区讨论**: 评论者大体上支持法院的裁决，有人认为年龄验证系统不可避免会变成身份验证系统。还有人提出了设备级锁定或单独的成人专属互联网等技术替代方案，少数人则对法律被直接驳回而不是被修正表示担忧。

**标签**: `#legal`, `#privacy`, `#regulation`, `#social media`, `#age verification`

---

<a id="item-6"></a>
## [PyTorch 静态检查工具 torch-preflight：提前发现训练错误并估算显存](https://www.reddit.com/r/MachineLearning/comments/1vo8vv0/a_linter_for_pytorch_torchpreflight_p/) ⭐️ 8.0/10

作者发布了 torch-preflight，这是一个 PyTorch 静态检查工具，能在不导入或执行代码的情况下发现常见训练错误（如保留 autograd 计算图、缺少 zero_grad() 调用、DDP 未使用 DistributedSampler 等），并估算显存需求。目前包含 13 条规则，可通过 pip install torch-preflight 安装。 该工具针对的是会浪费大量 GPU 机时的常见 PyTorch 错误，这是机器学习开发中的一大痛点。由于它是静态分析且不需要 GPU 或安装 torch，可以轻松集成到 CI 流程中，帮助开发者在花费昂贵的计算资源之前发现问题。 该检查工具目前有 13 条规则，主要在 PyTorch 源码树上测试；显存估算在单个 T4 上用四个模型验证，误差在实测峰值的 4% 以内。作者指出误报是潜在问题，欢迎贡献代码，并计划很快添加“good first issues”。

reddit · r/MachineLearning · /u/LeJanbandhu · 8月14日 14:30

**背景**: PyTorch 的 autograd 在前向传播中会构建计算图；如果在迭代中保留计算图（例如通过 losses.append(loss)），显存会不断增长直至 OOM。梯度累积需要将 loss 除以累积步数，DDP 训练则需要 DistributedSampler 来确保每个 rank 看到不同的数据分区。静态分析可以在不运行代码的情况下发现这些模式，从而提前暴露错误和内存需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/beginner/ddp_series_theory.html">What is Distributed Data Parallel (DDP) — PyTorch Tutorials...</a></li>
<li><a href="https://discuss.pytorch.org/t/accumulating-gradients/30020">Accumulating Gradients - PyTorch Forums</a></li>
<li><a href="https://discuss.pytorch.org/t/use-of-retain-graph-true/179658">Use of retain_graph = True - autograd - PyTorch Forums</a></li>

</ul>
</details>

**标签**: `#PyTorch`, `#linter`, `#debugging`, `#GPU`, `#machine learning`

---

<a id="item-7"></a>
## [Vivodyne AI 机器人实验室年测 300 万人体组织样本](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 8.0/10

Vivodyne 推出了号称全球最大的人体生物数据中心，由 12 个机器人 HIVE 实验室组成，每年可进行 310 万次活体人体组织实验。该 AI 操作系统自主设计并执行实验，规模约为美国全部临床试验总和的两倍。 这可能使药物研发中的动物测试变得过时，因为目前约有 90%的临床试验在通过动物测试后仍以失败告终。通过大规模使用仿真人体组织，Vivodyne 旨在提高药物疗效和安全性预测的准确性，有望变革药物发现并减少对动物模型的依赖。 每个 HIVE 实验室都是位于旧金山南部的壁橱大小的机器人设施，整个系统每年可对人体器官组织进行 300 多万次受控实验。尽管技术能力显著，但该方法尚未被证明能替代动物测试或提高临床试验成功率。

telegram · zaihuapd · 8月14日 01:48

**背景**: Vivodyne 源自宾夕法尼亚大学的生物工程研究，旨在通过以 AI 规模生成人类数据，让生物学变得可计算。传统上，候选药物先在动物身上测试，但动物生物学往往无法预测人类反应，导致后期失败率很高。在体外培养并测试仿真人体组织的自主实验室提供了一种潜在的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>
<li><a href="https://biobuzz.io/news/penn-born-vivodyne-launches-what-it-calls-the-worlds-largest-human-biological-datacenter/">Penn-Born Vivodyne Launches What It Calls the World's Largest ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#biotech`, `#drug discovery`, `#animal testing`, `#lab automation`

---

<a id="item-8"></a>
## [小红书开源 280B MoE 模型，仅 16B 激活参数](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小红书 dots 实验室发布了开源权重模型 dots3-note preview，这是一个总参数量 280B、每次仅激活 16B 参数的混合专家（MoE）模型，支持 512K 上下文。该模型还引入了 TEMPO 强化学习方法，并同步发布了 VibeSearchBench 和 VibeLifeBench 两个智能体基准，权重已在 Hugging Face 上开源。 这一发布具有重要意义：一家中国大型互联网公司开源了激活参数很少的超大规模 MoE 模型，使研究人员和应用开发者更容易使用高容量 LLM。新的强化学习方法和基准面向长程智能体任务，推动 LLM 智能体的评估从短时单轮交互走向更长周期的真实场景。 该模型支持文字、图片、视频和音频输入，可处理 512K token 的上下文窗口。其 TEMPO 方法据称通过自批判和测试时价值估计来训练长程智能体；同时发布的基准包含 200 个主动搜索任务和 200 个覆盖日常生活的多周生活世界任务。

telegram · zaihuapd · 8月14日 08:27

**背景**: 混合专家（MoE）模型通过每个 token 只激活部分参数，在扩大总参数量的同时控制推理成本。长上下文和多模态能力越来越常见于前沿 LLM，但总参数 280B、激活参数 16B 的开源模型仍然很少。VibeSearchBench 通过知识图谱匹配评估智能体在模糊多轮主动搜索中的表现，VibeLifeBench 则在模拟世界中用脚本化事件和模拟服务构建多周生活场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vibebench.github.io/VibeSearchBench.github.io/">VibeSearchBench — Benchmarking Long-horizon Proactive Search...</a></li>
<li><a href="https://arxiv.org/html/2605.27882">VibeSearchBench : Benchmarking Long-horizon Proactive Search in...</a></li>
<li><a href="https://arxiv.org/abs/2608.10875v1">[2608.10875v1] VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?</a></li>

</ul>
</details>

**标签**: `#MoE`, `#open-source`, `#reinforcement-learning`, `#multimodal`, `#LLM`

---

<a id="item-9"></a>
## [法官责令谷歌一周内取消第三方应用商店安装障碍](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 8.0/10

美国地区法官 James Donato 下令谷歌在一周内简化第三方安卓应用商店的安装流程，删除 Play Store 中多余的警告步骤，使安装第三方商店与安装普通应用一样直接。该命令源自 Epic 诉谷歌反垄断案。 这项裁决是重要的反垄断进展，可能重塑安卓应用分发格局，让 Epic Games Store 等竞争对手更容易与 Google Play 竞争，并可能降低开发者的成本。它也为法院如何审视平台守门人行为树立了先例。 法院认定，谷歌的多步流程——例如先显示警告并要求用户点击数次后才出现“安装”按钮——是刻意设计的“反竞争摩擦”，旨在吓退普通用户。谷歌须在一周内完成修改，目前仅适用于美国市场。

telegram · zaihuapd · 8月14日 09:55

**背景**: 在安卓上，侧载（sideloading）是指不通过 Google Play 商店安装应用，通常使用 APK 文件或第三方应用商店。谷歌历来会在侧载过程中显示警告弹窗，提醒用户潜在安全风险。Donato 法官的指令针对这些摩擦点，认为它们超出了正当安全警告的范畴，构成反竞争行为。该裁决是在涉及谷歌对安卓应用分发控制权的 Epic 诉谷歌案中作出的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidcentral.com/what-sideloading">What is sideloading ? [ Android A to Z] | Android Central</a></li>
<li><a href="https://developer.android.com/reference/android/content/pm/PackageInstaller">PackageInstaller | API reference | Android Developers</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#android`, `#google play`, `#app stores`, `#legal`

---

<a id="item-10"></a>
## [苹果官宣换帅：库克卸任 CEO，特努斯接任](https://t.me/zaihuapd/43191) ⭐️ 8.0/10

苹果宣布管理层交接，现任 CEO 蒂姆·库克将卸任，硬件工程高级副总裁约翰·特努斯将于 2026 年 9 月 1 日起担任新任 CEO。库克将出任董事会执行董事长。 这是苹果十多年来首次重大 CEO 更替，将决定公司未来多年的产品战略方向。特努斯曾负责 iPhone、Mac、iPad 和 AirPods 等核心产品，他的上任既延续了硬件领导力，也标志着这家全球最具价值科技公司进入新时代。 董事会一致批准了这项安排，库克将在整个夏天继续担任 CEO 以完成过渡。现任董事长 Arthur Levinson 将于 9 月 1 日转任首席独立董事，特努斯同日进入董事会。

telegram · zaihuapd · 8月14日 11:00

**背景**: 蒂姆·库克自 2011 年起担任苹果 CEO，接替史蒂夫·乔布斯，带领公司达到创纪录估值，拓展服务业务，并推出了 Apple Watch 和 Vision Pro 等产品。约翰·特努斯于 2001 年加入苹果，2013 年升任硬件工程副总裁，2021 年进入高管团队，在苹果核心硬件产品开发中发挥了关键作用。这次换帅是苹果这家以严谨设计驱动文化著称的公司罕见的领导层更替。

**标签**: `#Apple`, `#CEO transition`, `#tech industry`, `#leadership`

---

<a id="item-11"></a>
## [PostgreSQL 修复 to_char 高危漏洞，可致远程代码执行](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 披露了 CVE-2026-14669：to_char(timestamptz) 在处理超长 POSIX 时区缩写时存在堆缓冲区溢出，允许已认证的低权限数据库用户以 PostgreSQL 服务进程的操作系统权限执行任意代码。该漏洞已在 18.6、17.11、16.15、15.19 和 14.24 版本中修复。 这个高危（CVSS 8.8）远程代码执行漏洞影响了全球使用最广泛的开源关系型数据库之一，数据库管理员应优先修补其部署环境。该漏洞也提醒我们，格式化函数和时区解析仍是数据库引擎中危险的攻击面。 受影响版本包括 18.5、17.11、16.15、15.19 和 14.24 之前的所有 PostgreSQL 版本；由于 18.5 因回归问题未正式发布，18 系列用户应直接升级到 18.6。此次小版本更新无需转储数据库或运行 pg_upgrade，只需替换程序文件并重启服务即可。

telegram · zaihuapd · 8月14日 14:35

**背景**: to_char 是 PostgreSQL 的数据类型格式化函数，用于将时间戳、时间间隔和数字转换为字符串。POSIX 时区规范是类似“EST5EDT”的字符串，用于定义标准时间和夏令时偏移量，当设置会话时区时 PostgreSQL 会解析这些字符串。堆缓冲区溢出是指程序写入超出动态分配内存块边界之外的数据，攻击者常可利用它覆盖函数指针并执行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/functions-formatting.html">PostgreSQL : Documentation: 18: 9.8. Data Type Formatting Functions</a></li>
<li><a href="https://www.postgresql.org/docs/current/datetime-posix-timezone-specs.html">PostgreSQL: Documentation: 18: B.5. POSIX Time Zone Specifications</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heap_overflow">Heap overflow - Wikipedia</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#security`, `#CVE`, `#RCE`, `#vulnerability`

---

<a id="item-12"></a>
## [苹果与阿里联手自研中国专属 AI 模型，或成首个获批外企](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 8.0/10

苹果已在阿里巴巴支持下专门为中国市场训练了一款大语言模型，改变此前依赖第三方模型的策略。Apple Intelligence 预计在未来数月随 iOS 更新在华上线。 若获批，苹果将成为首家获北京批准在华提供自有 AI 模型的外国公司，开创监管先例。这可能重塑中国 AI 服务竞争格局，并影响其他全球科技公司进入该市场的策略。 这款中国专属模型由苹果自研，以更好地掌控中国市场的 AI 体验。中国网信办已于上月对其生成式 AI 服务进行备案，这是在华提供此类服务的必要前提。

telegram · zaihuapd · 8月14日 14:47

**背景**: Apple Intelligence 是苹果于 2024 年 6 月在 WWDC 发布的个人智能系统，将生成式模型与个人情境相结合，覆盖 iPhone、iPad 和 Mac。在中国，生成式 AI 服务提供方必须在推出前向中国网信办完成备案，因此苹果在阿里巴巴支持下开发本地化模型，而非沿用常规做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence - Wikipedia</a></li>
<li><a href="https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/">Introducing Apple Intelligence for iPhone, iPad, and Mac - Apple</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#Regulation`

---