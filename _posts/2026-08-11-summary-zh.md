---
layout: default
title: "Horizon Summary: 2026-08-11 (ZH)"
date: 2026-08-11
lang: zh
---

> 从 37 条内容中筛选出 11 条重要资讯。

---

1. [vLLM v0.27.0 发布：新增 Kimi K3、多模型与 PyTorch 2.13 支持](#item-1) ⭐️ 9.0/10
2. [Mojo 1.0 发布：Modular 面向 AI 的系统语言迎来重大里程碑](#item-2) ⭐️ 8.0/10
3. [研究人员从专有 LLM API 中提取隐藏的推理痕迹](#item-3) ⭐️ 8.0/10
4. [AI 吞噬网络，互联网的集体记忆正在消失](#item-4) ⭐️ 8.0/10
5. [英伟达的 AI 算力豪赌：CUDA 护城河遭遇需求风险](#item-5) ⭐️ 8.0/10
6. [H3-metal：为 Apple Silicon 带来 MiniMax-H3 原生视频推理](#item-6) ⭐️ 8.0/10
7. [谷歌称 Go 的简洁性使其成为 AI 辅助编程的理想选择](#item-7) ⭐️ 8.0/10
8. [Chicken Scheme 6.0 发布，带来完整的 Unicode 支持](#item-8) ⭐️ 8.0/10
9. [Meta 发布 Muse Glimmer，一个采用 Apache 2.0 许可的 30B 智能体模型](#item-9) ⭐️ 8.0/10
10. [Anthropic 推出 Claude Opus 5：价格减半，性能逼近旗舰](#item-10) ⭐️ 8.0/10
11. [石墨烯软镜片问世，有望小型化自动对焦相机与 VR 设备](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.27.0 发布：新增 Kimi K3、多模型与 PyTorch 2.13 支持](https://github.com/vllm-project/vllm/releases/tag/v0.27.0) ⭐️ 9.0/10

vLLM v0.27.0 正式发布，包含来自 242 位贡献者的 561 次提交，新增 Kimi K3 的全栈支持（含 AttnRes 内核与 DeepGEMM），以及 Qwen3.5、K-EXAONE-2.0-750B-A37B 等新模型，并将 PyTorch 升级至 2.13.0。该版本还深化了 FlashAttention 4 在 NVIDIA SM100 上的集成，支持 FP8 KV cache 和 headdim-256，并为 DeepSeek-V4 带来大量性能优化。 这是最广泛使用的开源 LLM 推理引擎之一的重要更新，将直接影响所有在生产环境中服务大模型的用户。新增 Kimi K3 等前沿模型支持，并结合内核级性能优化，使 vLLM 更强大、更快速，能应对严苛的 AI 工作负载。 该版本升级到 PyTorch 2.13.0，属于破坏性环境变更，并新增对 NVIDIA Rubin 的 sm_107 和 ROCm gfx1250 等下一代硬件的早期支持。Model Runner V2 扩展到嵌入、分类等非生成式工作负载，并引入适用于大规模 DP+EP 部署的简化容错框架。

github · khluu · 8月10日 21:18

**背景**: vLLM 是一个面向大语言模型的高吞吐、内存高效的推理与服务引擎，采用 PagedAttention、continuous batching 等技术。FlashAttention 是一系列 IO 感知的注意力算法，可加速 GPU 上的 Transformer 训练与推理，FlashAttention 4 针对英伟达下一代数据中心架构。DeepGEMM 是 DeepSeek 开源的简洁高效的 GPU BLAS 内核库；DSpark 是 DeepSeek 的投机解码草稿模型方法。AttnRes（注意力残差）指将注意力与残差连接及归一化融合的内核技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/DeepGEMM: DeepGEMM: clean and efficient ...</a></li>
<li><a href="https://github.com/catswe/Flash-Attention-Residuals">GitHub - catswe/flash-attention-residuals: Triton kernels and PyTorch...</a></li>
<li><a href="https://github.com/ARahim3/mlx-dspark">GitHub - ARahim3/mlx-dspark: Up to 3× faster LLM decoding on ...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#PyTorch`, `#AI/ML systems`

---

<a id="item-2"></a>
## [Mojo 1.0 发布：Modular 面向 AI 的系统语言迎来重大里程碑](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 8.0/10

Modular 宣布 Mojo 1.0 正式到来，这是面向高性能 AI 工作负载、受 Python 启发的系统编程语言的一个重大版本。2026 年 5 月，Mojo 1.0 首个测试版发布，语言官网 mojolang.org 也同步上线。 Mojo 1.0 对这门高关注度的语言来说是一个重要里程碑，它旨在将 Python 的易用性与系统级性能以及对 GPU、TPU、ASIC 等加速器的支持结合起来。该版本的发布可能影响 AI 基础设施的构建方式，但闭源编译器和“Python 超集”立场的转变仍存在争议。 Mojo 基于 MLIR 编译器框架构建，除了 CPU 之外，它还可以面向 GPU、TPU、ASIC 等加速器生成代码，并利用仅靠 LLVM 无法实现的高级编译器优化。Mojo 标准库已在 GitHub 上完全开源，但编译器仍未开源；Modular 计划于 2026 年秋季将编译器开源。

hackernews · dayanruben · 8月11日 16:56 · [社区讨论](https://news.ycombinator.com/item?id=49261128)

**背景**: Mojo 是 Modular 公司开发的系统编程语言，采用受 Rust 启发的静态类型和借用检查器，但语法设计得让人联想到 Python。它最初旨在成为 Python 的超集，但到 2026 年 3 月，这一目标已被放弃或无限期推迟。Mojo 的路线图现在指出，它可能或不会演变为 Python 的完整超集，即使不成为超集也没关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo - Modular</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人援引路线图中的模糊措辞，质疑 Mojo 是否仍在追求成为 Python 超集；也有人表示官网缺少能简明扼要说明语言用途的一页概览。还有评论批评闭源编译器，并认为该项目实际上可能已被“收购式聘用”（acquihire），但也有人对 Mojo 的潜力保持乐观。

**标签**: `#Mojo`, `#programming-language`, `#AI`, `#systems-programming`, `#Modular`

---

<a id="item-3"></a>
## [研究人员从专有 LLM API 中提取隐藏的推理痕迹](https://stolen-thoughts.com/) ⭐️ 8.0/10

该报告展示了从专有 LLM API 中提取隐藏思维链推理的技术。通过将前沿模型的轨迹重放到较弱的兄弟模型并对其进行越狱，或者禁用思考并提供'deep_think'工具，攻击者可以恢复提供商试图隐藏的推理内容。 这很重要，因为它打破了'专有 LLM API 能对推理轨迹保密'的假设，引发安全与透明度方面的担忧。它还加剧了一个持续争论：使用其他模型的输出进行训练究竟是盗窃还是合理使用。 该技术在 AIME 题目上得到验证：Opus 4.8 有时会先给出答案再推导，但 API 摘要可能不会保留这种区别，使推理看起来更干净。作者承认，由于生成的随机性，无法保证提取出的思考与模型的私有推理完全一致。

hackernews · quantumgarbage · 8月11日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49257876)

**背景**: LLM 推理轨迹是中间计算的显式逐步序列，记录了模型内部的决策过程。思维链提示能够激发这种逐步推理，显著提升 LLM 在复杂任务上的表现。专有 API 提供商通常会隐藏这些轨迹以防止蒸馏、API 滥用或竞争性复制，只提供摘要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs - arXiv.org</a></li>
<li><a href="https://www.emergentmind.com/topics/reason-traces-for-llms">LLM Reasoning Traces - emergentmind.com</a></li>

</ul>
</details>

**社区讨论**: 评论者争论'窃取'一词是否恰当；有人认为用户已经为 token 付费，理应访问输出，所以'恢复'更合适。还有人指出类似使用'deep_think'工具的方法，并注意到模型似乎对基准题目训练过度，这使得提取的推理的真实性受到质疑。

**标签**: `#LLM`, `#AI security`, `#reasoning traces`, `#API exploitation`, `#model transparency`

---

<a id="item-4"></a>
## [AI 吞噬网络，互联网的集体记忆正在消失](https://thewalrus.ca/google-search-is-dying/) ⭐️ 8.0/10

文章认为，AI 生成的内容和基于聊天机器人的搜索正在侵蚀互联网的集体记忆，并降低信息检索的可靠性。文章还主张，长期作为网络知识入口的 Google 搜索实际上正在走向消亡。 这之所以重要，是因为搜索和开放网络仍是新闻、公共记录和历史知识的关键基础设施。如果 AI 生成的内容充斥网络，而聊天机器人成为主要入口，一些难以查找的信息类别可能变得无法获取，人们对在线信息的信任也将持续下降。 具体后果已经显现：使用 AI 辅助的开发者常常重复造轮子，构建已有工具；即便是记者等资深用户也仍要依赖 Google，因为聊天机器人无法检索到扫描版政府 PDF 等冷门内容。一个相关的技术风险是'模型崩溃'（model collapse），即 AI 模型在 AI 生成的数据上训练，质量会随时间推移而退化。

hackernews · awnird · 8月10日 22:36 · [社区讨论](https://news.ycombinator.com/item?id=49250836)

**背景**: 传统网页搜索通过爬取和索引页面来工作，用户因此能定位到特定的文档——包括聊天机器人可能永远无法展示的冷门公共记录。互联网的'集体记忆'，指的是搜索引擎几十年来让人们能够发现的人类创作内容的积累。随着 AI 生成的文本充斥网络，这一共同记录面临被污染或丢失的风险。模型崩溃（model collapse）是指机器学习模型在未经筛选的合成数据或其他模型的输出上训练时发生的性能退化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_collapse">Model collapse</a></li>
<li><a href="https://www.ibm.com/think/topics/model-collapse">What Is Model Collapse? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者大体认同文章观点，并分享了现实中的例子：有人提到使用 AI 辅助开发的开发者会在不知情的情况下重复造轮子，复制已有的免费工具；还有人指出，身为记者的姐姐仍在使用 Google，因为聊天机器人无法检索到冷门的扫描版政府表格。一位评论者称自己三年前就预见了这些危害，并对 Google 亲手毁掉其普及信息的遗产感到惋惜。另一位评论者纠正了互联网档案馆诉讼的事实：法院判定该机构构成未经授权的复制，而不仅仅是受到指控。

**标签**: `#AI`, `#search`, `#internet`, `#information quality`, `#collective memory`

---

<a id="item-5"></a>
## [英伟达的 AI 算力豪赌：CUDA 护城河遭遇需求风险](https://stratechery.com/2026/nvidias-risky-business/) ⭐️ 8.0/10

2026 年发布的一篇 Stratechery 分析质疑英伟达对 AI 算力需求持续增长的依赖，并认为其软硬件护城河并非坚不可摧。评论者也提出了新的视角，指出 CUDA 的开发者体验不佳，以及英伟达可能转向机器人等未来市场。 英伟达的估值乃至整个 AI 热潮，都建立在算力需求将按当前速度持续增长的假设之上。如果这些关于增长的第二层假设被夸大，可能引发英伟达的估值调整，并减缓整个行业对以 GPU 为核心的 AI 基础设施的投资。 讨论中的关键细节包括：CUDA 虽然在机器学习研究中根深蒂固，但其开发者体验被认为很差，既有 C++的常见陷阱，又有 CPU 与 GPU 编程模型的根本不同。此外，英伟达已开始布局机器人领域，中国企业正在构建全栈替代方案，而苹果的统一内存可能降低对云端推理的需求，同时中国模型也证明训练不一定需要英伟达最新硬件。

hackernews · jonbaer · 8月11日 10:02 · [社区讨论](https://news.ycombinator.com/item?id=49255710)

**背景**: CUDA（Compute Unified Device Architecture）是英伟达专有的并行计算平台和 API，它让 GPU 能够处理通用计算，是 AI 训练和推理的核心。CUDA 于 2007 年推出，包含编译器、库和开发工具，并已深度嵌入机器学习研究，成为英伟达竞争护城河的重要组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CUDA">CUDA</a></li>
<li><a href="https://developer.nvidia.com/cuda/toolkit">CUDA Toolkit - Free Tools and Training | NVIDIA Developer</a></li>

</ul>
</details>

**社区讨论**: 评论者大体认同风险论点，但也指出了更多细节：YuechenLi 认为 CUDA 的优势来自研究生态的根深蒂固而非开发者体验（后者相当糟糕）；jcfrei 警告投资论点常败在第二层增长假设上；tolugenius 指出英伟达已布局机器人且中国在构建全栈；dzonga 则提到苹果统一内存和中国高效训练模型可能威胁推理需求。

**标签**: `#nvidia`, `#ai`, `#business-strategy`, `#cuda`, `#semiconductors`

---

<a id="item-6"></a>
## [H3-metal：为 Apple Silicon 带来 MiniMax-H3 原生视频推理](https://github.com/antirez/h3.c) ⭐️ 8.0/10

H3-metal（h3.c）是面向 Apple Silicon 的 MiniMax-H3 原生 Metal 推理实现，让 Mac 可以在本地运行这款开放权重视频模型。该项目由 antirez 发布，社区正在积极讨论其跑分和量化方案。 它让 Mac 用户无需依赖云端 GPU 或 CUDA，就能在本地运行一款强大的开放权重多模态视频模型，扩大了本地 AI 视频生成的适用范围。同时也反映出 2026 年 Apple Silicon 推理生态正在日益成熟。 目前的生成速度远未达到实时：在 M5 Pro 上，一段约 9 秒、480x864、20 步的片段需要一个多小时；在 128GB M4 Max 上，一段 15 秒 480p 片段约需 1.5 小时。模型需要较大的统一内存（大致 64GB 或更多），antirez 正在尝试 MiniMax AMA 中提到的可选 --sparse-attention 模式。

hackernews · swyx · 8月11日 01:22 · [社区讨论](https://news.ycombinator.com/item?id=49252179)

**背景**: MiniMax-H3 是一个开放权重的全模态基础模型，可以在单一上下文中结合文本、图片、视频和音频，生成最高 2K 分辨率、24fps、最长 15 秒、并自带立体声音频的视频。Metal 是 Apple 的 GPU 框架，其 Metal Performance Shaders（MPS）API 用于在 Apple Silicon 的统一内存架构上加速机器学习推理。H3-metal（即 h3.c 项目）是一个原生 Metal 实现，可以在 Mac 上本地运行 MiniMax-H3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/ MiniMax - H 3 · Hugging Face</a></li>
<li><a href="https://fal.ai/minimax-h3">MiniMax H 3 - Open-Weights General-Purpose Multimodal Video Model</a></li>
<li><a href="https://developer.apple.com/metal/">Metal Overview - Apple Developer</a></li>

</ul>
</details>

**社区讨论**: 社区整体态度积极，但也认为性能是现实的制约。用户确认 H3-metal 通过 ComfyUI 配合 GGUF 量化（如 Q5_K_M/Q8_0）可以良好运行，但生成速度很慢——在 M5 Pro 上生成 9 秒片段超过一小时，在 M4 Max 上生成 15 秒片段约需 1.5 小时。还有人担心需要 128GB 内存，而 antirez 正在尝试 sparse-attention 模式以加速；一些评论者也指出，对于扩散类任务，CUDA/DGX 仍然更省心。

**标签**: `#apple-silicon`, `#video-generation`, `#metal`, `#inference`, `#machine-learning`

---

<a id="item-7"></a>
## [谷歌称 Go 的简洁性使其成为 AI 辅助编程的理想选择](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/) ⭐️ 8.0/10

谷歌发布了一篇博文，认为 Go 的简洁性、强大的工具链和设计理念使其成为 AI 辅助软件工程的理想语言。这篇文章在 Hacker News 上引发了广泛讨论，既有支持者也有人提出反对意见。 这一观点很重要，因为 AI 辅助开发正在迅速改变代码的编写方式，而语言选择可能影响 AI 工具的性能发挥。如果 Go 的简洁性确实具有优势，可能会进一步推动 Go 在 AI 驱动开发世界的普及。 该博文强调 Go 的可读性、内置格式化和简单的并发模型是 AI 代码生成的关键优势。Hacker News 的讨论中有人提出相反观点，认为 Rust 严格的编译器能在编译期捕获错误，更适合作 LLM 的编程语言；也有人警告说 LLM 可能会生成糟糕的 Go 并发代码。

hackernews · 0xedb · 8月11日 16:57 · [社区讨论](https://news.ycombinator.com/item?id=49261133)

**背景**: AI 辅助软件工程利用大语言模型（LLM）帮助开发者编写、审查和测试代码。Go 是一种静态类型、编译型语言，以简洁和强大的标准库著称；而 Rust 是另一种现代系统语言，强调内存安全和严格的编译期检查。关于哪种语言最适合 AI 的争论，反映了 LLM 如何处理不同语言特性的深层问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/ai_assisted_software_development">AI-assisted software development</a></li>
<li><a href="https://simonwillison.net/2025/Mar/11/using-llms-for-code/">Here’s how I use LLMs to help me write code</a></li>

</ul>
</details>

**社区讨论**: 在 Hacker News 的评论中，Netflix 的 Go 语言公会负责人表示，他们发现 AI 代理用 Go 写出的代码比其他语言更好，而其他用户则持怀疑态度。有人认为 Rust 严格的编译器更适合 LLM，因为它能在编译期暴露错误；还有评论者警告，Go 缺乏抽象能力可能导致 LLM 生成有问题的并发代码。

**标签**: `#Go`, `#AI-assisted development`, `#software engineering`, `#programming languages`, `#LLM coding`

---

<a id="item-8"></a>
## [Chicken Scheme 6.0 发布，带来完整的 Unicode 支持](https://code.call-cc.org/releases/6.0.0/NEWS) ⭐️ 8.0/10

Chicken Scheme 6.0 已发布，带来了完整的 Unicode 支持以及编译器与生态系统的重大改进。 完整的 Unicode 支持解决了长期存在的限制，使 Chicken 更适合现代文本处理应用。这一重大版本也表明项目仍在积极开发中，可能为 Scheme 生态吸引新用户。 Chicken 6.0 将 Scheme 源码编译为可移植的 C，并符合 R7RS 标准。社区评论指出，该版本增加了对 Crunch 的支持（Crunch 是一个针对 R7RS 静态类型子集的编译器），不过 Crunch 本身仍处于 0.993 版本。

hackernews · eatonphil · 8月11日 00:24 · [社区讨论](https://news.ycombinator.com/item?id=49251702)

**背景**: Chicken（风格化为 CHICKEN）是一个免费开源的 Scheme 编程语言编译器与解释器，采用 BSD 许可证发布。它将 Scheme 源码转换为可移植的 C 代码，再交由 C 编译器生成独立可执行文件。Chicken 支持 R5RS 和 R7RS 标准，并提供许多扩展。Scheme 本身是 Lisp 的一个极简方言，以简洁和强大的宏著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chicken_(Scheme_implementation)">Chicken (Scheme implementation) - Wikipedia</a></li>
<li><a href="http://www.call-cc.org/">CHICKEN Scheme</a></li>

</ul>
</details>

**社区讨论**: 社区的反馈总体积极，用户对完整的 Unicode 支持表示兴奋，并向团队表示祝贺。一位用户分享了使用 Chicken 构建包装器的积极实践经验，另一位用户则询问 Chicken 相对于其他 Lisp 的独特优势。还有评论提到 6.0 对 Crunch 编译器的支持。

**标签**: `#Scheme`, `#Lisp`, `#Release`, `#Compiler`, `#Programming Languages`

---

<a id="item-9"></a>
## [Meta 发布 Muse Glimmer，一个采用 Apache 2.0 许可的 30B 智能体模型](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta 发布了 Muse Glimmer，这是一个全新的 30B 参数开放权重模型，采用干净的 Apache 2.0 许可证。该模型针对端到端智能体任务完成、可靠工具使用和多步推理进行了优化，并已通过 LM Studio 提供 18.16 GB 的量化版本。 此次发布标志着 Meta 在开放权重 AI 领域迈出重要一步，其宽松许可证与过去更严格的 Llama 许可证形成鲜明对比。通过聚焦智能体能力和工具使用，Muse Glimmer 迎合了本地模型日益增长的需求，这些模型可支持自主 AI 智能体和复杂工作流。 Muse Glimmer 是一个视觉模型，其描述图像的能力已得到验证，并且可以在 32 GB 或更高内存的机器上流畅运行。它已使用 Simon Willison 的 llm-coding-agent 插件在 Datasette 的全新检出上进行了测试，展示了多工具调用探索代码库的能力。

rss · Simon Willison · 8月10日 23:56

**背景**: 提到的基准测试，包括 DeepSearchQA、MCP-Atlas、τ-Bench 和 SWE-Bench，旨在评估现实场景中的智能体任务完成能力、工具使用和多步推理能力。DeepSearchQA 是一个包含 900 个提示的深度研究基准，MCP-Atlas 使用真实的 MCP 服务器测试工具使用能力，而 τ-Bench 则对工具-智能体-用户交互进行基准测试。Apache 2.0 是一个宽松的开源许可证，允许广泛使用和修改，与更严格的 Llama 社区许可证形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.20975">[2601.20975] DeepSearchQA: Bridging the Comprehensiveness Gap ... DeepSearchQA:Bridgingthe ComprehensivenessGapforDeepResearch ... DeepSearchQA: Bridging the Comprehensiveness Gap for Deep ... DeepSearchQA Leaderboard & Scores — August 2026 | BenchLM.ai DeepSearchQA Leaderboard google/deepsearchqa · Datasets at Hugging Face Evals — Google DeepMind</a></li>
<li><a href="https://static.scale.com/uploads/674f4cc7a74e35bcaae1c29a/MCP_Atlas.pdf">MCP - Atlas : A Large-Scale Benchmark for Tool-Use Competency with...</a></li>
<li><a href="https://taubench.com/">τ- bench — Benchmarking AI Agents on Real-World Tasks</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine-learning`, `#open-source`, `#agents`, `#Meta`

---

<a id="item-10"></a>
## [Anthropic 推出 Claude Opus 5：价格减半，性能逼近旗舰](https://t.me/zaihuapd/43109) ⭐️ 8.0/10

Anthropic 正式发布了 Claude Opus 5，该模型的智能水平接近旗舰产品 Claude Fable 5，而使用成本仅为后者的一半。它即日起成为 Claude Max 的默认模型，同时也是 Claude Pro 上最强的模型，定价与上一代 Opus 4.8 持平。 此次发布表明，接近前沿的 AI 能力不再必须与旗舰级定价捆绑，可能会重塑大语言模型部署的经济性。企业和个人用户现在可以以中档价格获取高端推理与智能体能力，从而加速模型采用并加剧 AI 行业的竞争。 据公告，Claude Opus 5 在 Frontier-Bench、ARC-AGI 3、Zapier AutomationBench 等多项基准测试中表现优异。它即日起作为 Claude Max 的默认模型和 Claude Pro 上的最强模型提供，定价维持与上一代 Opus 4.8 相同的水平。

telegram · zaihuapd · 8月11日 03:39

**背景**: Anthropic 的 Claude 系列是一套专注于有用、无害且诚实的人工智能的大语言模型产品线，与 OpenAI 的 GPT 系列和 Google 的 Gemini 等展开竞争。Frontier-Bench 用于衡量困难的智能体工作任务，ARC-AGI-3 测评在未知环境中的交互式推理能力，而 Zapier 的 AutomationBench 则测试在真实业务流程中的执行能力。通过推出性能接近旗舰但价格更便宜的模型，Anthropic 正在应对通常阻碍企业采用领先语言模型的高推理成本问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.frontierbench.ai/">TERMINAL-BENCH</a></li>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://zapier.com/benchmarks">AutomationBench: AI Agent Benchmarks - Zapier</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#model-release`, `#LLM`, `#Claude`

---

<a id="item-11"></a>
## [石墨烯软镜片问世，有望小型化自动对焦相机与 VR 设备](https://www.qmul.ac.uk/news/latest-news/2026/science-and-engineering/se/new-graphene-powered-soft-lens-could-pave-the-way-for-smarter-glasses-cameras-and-medical-devices.html) ⭐️ 8.0/10

伦敦玛丽女王大学的研究人员开发出一种由还原氧化石墨烯驱动的透明软性镜片，可在小电场作用下改变焦距，模拟人眼的工作原理。该成果发表于《Advanced Functional Materials》，将超薄透明石墨烯电极直接集成到镜片下方的驱动层中。 这一突破有望消除传统镜头系统中笨重的移动部件，从而实现更小、更轻的自动对焦相机、可穿戴显示器、VR/AR 头显以及微型医疗成像设备。它同时解决了传统不透明电极只能置于镜片边缘这一关键设计瓶颈。 该镜片采用喷涂法在介电弹性体薄膜上沉积还原氧化石墨烯（rGO），形成兼具半透明性的可变形电极。目前该原型仍需进一步优化电极的透明度与性能，才能实现商业化应用。

telegram · zaihuapd · 8月11日 12:27

**背景**: 传统变焦和自动对焦系统依赖电磁或静电电机移动刚性玻璃镜片，增加了体积、重量和复杂度。电可调软镜片则通过施加电压使弹性体薄膜变形来改变焦距，是一种紧凑的替代方案。石墨烯是一种单原子厚度的碳材料，导电性优异；还原氧化石墨烯是可通过溶液加工的形式，能够制成透明导电层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.76426">Reduced Graphene Oxide Transparent Electrodes Enabling Compact Soft Tunable Lenses - Sasso - 2026 - Advanced Functional Materials - Wiley Online Library</a></li>
<li><a href="https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.678046/full">Electrically Tunable Lenses: A Review - Frontiers</a></li>
<li><a href="https://www.epfl.ch/labs/lmts/lmts-research/elastomer_actuator/fastlens/">High speed soft tuneable lenses ‒ LMTS ‐ EPFL</a></li>

</ul>
</details>

**标签**: `#graphene`, `#optics`, `#soft lens`, `#research`, `#VR/AR`

---