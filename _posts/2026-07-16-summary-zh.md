---
layout: default
title: "Horizon Summary: 2026-07-16 (ZH)"
date: 2026-07-16
lang: zh
---

> 从 51 条内容中筛选出 14 条重要资讯。

---

1. [Kimi K3：全新开源权重前沿模型，支持 100 万上下文](#item-1) ⭐️ 9.0/10
2. [Mira Murati 的 Thinking Machines Lab 发布开放权重模型 Inkling](#item-2) ⭐️ 9.0/10
3. [xAI 在隐私风波后开源 Grok Build 命令行工具](#item-3) ⭐️ 9.0/10
4. [新 Schema 框架在 ARC-AGI-3 上实现 99%准确率](#item-4) ⭐️ 9.0/10
5. [伪装字体：通过模糊效果隐藏信息，欺骗 AI 文本识别](#item-5) ⭐️ 8.0/10
6. [从 Rust 到 Zig 的编译器重写进展](#item-6) ⭐️ 8.0/10
7. [索尼删除更多已购影片，引发数字所有权担忧](#item-7) ⭐️ 8.0/10
8. [GPT-5.6 Codex 漏洞可删除 $HOME 目录](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds 支持在 Linux 中使用 AI，反对者可以分叉](#item-9) ⭐️ 8.0/10
10. [ExTernD：扩展秩三元分解提升 LLM 量化精度](#item-10) ⭐️ 8.0/10
11. [250%速度提升：98GB DeepSeek 在 4060 Ti 上达到 7 t/s](#item-11) ⭐️ 8.0/10
12. [xAI 起诉用户用 Grok 制作儿童性虐待深度伪造](#item-12) ⭐️ 8.0/10
13. [日本采购 2.75 万块英伟达 Rubin 芯片打造机器人 AI](#item-13) ⭐️ 8.0/10
14. [台积电再投千亿美元赴美，Q2 利润飙升 77%创新高](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3：全新开源权重前沿模型，支持 100 万上下文](https://www.kimi.com/blog/kimi-k3) ⭐️ 9.0/10

Kimi K3 是 Moonshot AI 推出的全新开源权重前沿 AI 模型，具备 100 万 token 的上下文窗口，性能强劲可与顶级模型媲美，并包含一个由模型自主设计的芯片概念验证。 作为与 GPT-4、Claude 等专有前沿模型相抗衡的开源权重模型，Kimi K3 有望推动高性能 AI 的普及，而其芯片设计能力则展示了 AI 驱动硬件优化的可能性。 定价为每百万 token $3/$15（缓存$0.3），与 Anthropic 的 Sonnet 系列相当。芯片设计概念验证在 48 小时内自主完成，使用开源 EDA 工具和 45nm 库，在 4 mm²内实现了 100MHz 时序收敛和每秒 8700 token 的解码吞吐量。

hackernews · vincent_s · 7月16日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=48935342)

**背景**: 开源权重模型允许研究人员和开发者查看和微调模型权重，这与封闭的专有模型不同。前沿模型是大型基础模型，推动了 AI 能力的边界。上下文窗口决定了 LLM 一次能处理的文本量；100 万 token 的规模异常庞大，可分析整本书或长文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>
<li><a href="https://www.ibm.com/think/topics/context-window">What is a context window ? | IBM</a></li>
<li><a href="https://medium.com/@bhagyarana80/why-open-weight-models-matter-more-than-you-think-1d1d8787a4fe">Why Open - Weight Models Matter (More Than You Think) | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些评论称赞其技术成就和竞争性能，另一些人则指出相对于中国开源权重模型定价较高，并对 Moonshot AI 的数据使用政策表示担忧，该政策允许使用 API 内容进行训练，除非客户选择退出。

**标签**: `#AI`, `#LLM`, `#open-weight`, `#frontier model`, `#chip design`

---

<a id="item-2"></a>
## [Mira Murati 的 Thinking Machines Lab 发布开放权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

Mira Murati 的 Thinking Machines Lab 发布了 Inkling，一个开放权重的多模态混合专家（MoE）Transformer 模型，总参数量 9750 亿，激活参数 410 亿，采用 Apache-2.0 许可，在 45 万亿 token 的文本、图像、音频和视频数据上训练。 此次发布增强了美国开放权重生态系统，为中国开源模型提供了有力竞争替代方案，并通过 Thinking Machines 的 Tinker 平台支持微调，Apache-2.0 许可确保了研究和商业用途的广泛可及性。 Inkling 并非前沿模型，而是设计为用于定制化的强大基础模型；其文档资料较少，模型卡和训练数据文档缺乏详细信息。此外，较小的变体 Inkling-Small（总参数量 2760 亿，激活参数 120 亿）仍在测试中，稍后发布。

rss · Simon Willison · 7月16日 15:35

**背景**: 混合专家（MoE）是一种神经网络架构，每次输入只激活部分参数，从而在高效计算的同时实现大模型容量。开放权重模型（如采用 Apache-2.0 许可的 Inkling）允许用户自由下载和使用训练好的权重，这与需要根据 OSI 批准许可证分发源代码的开源模型不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts (MoE) in Large Language Models</a></li>
<li><a href="https://kilo.ai/open-source-vs-open-weight-models">Kilo - Open Source vs Open Weight AI Models Explained</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#large language model`, `#multimodal`, `#Mixture-of-Experts`, `#AI announcement`

---

<a id="item-3"></a>
## [xAI 在隐私风波后开源 Grok Build 命令行工具](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI 在因 Grok Build 命令行工具默认将整个用户目录上传至 Google Cloud 而引发强烈批评后，将该工具的完整代码库以 Apache 2.0 许可证在 GitHub 上开源。 这一事件暴露了 AI 编程工具中严重的隐私漏洞，而 xAI 的开源和删除保留数据等应对措施，可能迫使其他公司采取类似的透明化举措。 该仓库的首次提交包含 844,530 行 Rust 代码，其中仅有约 3% 为外部依赖，包括一个 Mermaid 图表终端渲染器以及编程智能体的主要系统提示词。

rss · Simon Willison · 7月15日 23:59

**背景**: Grok Build 是一款由 xAI 的 Grok 模型驱动的 AI 命令行工具，旨在帮助开发者完成编码任务。该工具可将文件上传至云存储进行处理，但其默认设置导致在运行命令时会上传整个目录，从而引发了严重的隐私泄露事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://support.google.com/cloud/answer/6250993?hl=en">Cloud Storage - Google Cloud Platform Console Help</a></li>

</ul>
</details>

**社区讨论**: 用户在社交媒体上表达了强烈不满，有用户报告称包括 SSH 密钥和密码管理器数据在内的所有个人文件均被上传。埃隆·马斯克回应称将删除所有已上传数据并开源代码库以重建信任。

**标签**: `#grok`, `#xAI`, `#privacy`, `#open-source`, `#CLI`

---

<a id="item-4"></a>
## [新 Schema 框架在 ARC-AGI-3 上实现 99%准确率](https://www.reddit.com/r/MachineLearning/comments/1uyf8oo/new_fable5opus48_harness_called_schema_claims_99/) ⭐️ 9.0/10

一种名为 Schema 的新型推理框架通过优化现有模型的推理过程（不修改权重），在 ARC-AGI-3 公共基准上达到了 99%的准确率。 这一结果意义重大，因为 ARC-AGI 是通用智能的基准，接近完美的分数表明改进的推理过程可以释放当前模型的潜在能力，可能将焦点从扩展模型转向更好地利用模型。 该框架采用回退策略：首先运行 Claude Opus 4.8 和 GPT-5.6 Sol，如果游戏得分低于 80，则使用更高推理能力的 Fable 5 和 GPT-5.6 Sol 重新运行，并保留每局游戏的最高分。它不改变模型权重。

reddit · r/MachineLearning · /u/we_are_mammals · 7月16日 21:02

**背景**: ARC-AGI 是一个旨在衡量通用智能进展的基准。推理框架是协调推理过程的系统，包括如何呈现输入和评估输出，而不改变模型参数。这种方法与微调或训练新模型形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>

</ul>
</details>

**标签**: `#ARC-AGI`, `#AI benchmark`, `#harness`, `#Claude Opus`, `#Fable 5`

---

<a id="item-5"></a>
## [伪装字体：通过模糊效果隐藏信息，欺骗 AI 文本识别](https://www.mixfont.com/experiments/decoy-font) ⭐️ 8.0/10

一种名为“Decoy Font”的字体，能让 AI 文本识别看到一条消息，而人类在模糊或远距离查看时才能看到隐藏的另一条消息。 这展示了针对 OCR 和大型语言模型的一种简单而有效的对抗攻击，揭示了自动文本理解的脆弱性。它可能催生实际应用，例如创建人类可读但机器难以识别的文本，用于反机器人或隐私保护。 该字体使用两层叠加：一种颜色的清晰轮廓形成伪装文本，另一种颜色的模糊阴影创建隐藏信息。正常查看时，AI 读取清晰文本；当图像缩小或模糊时，隐藏信息变得显著，利用了人类与机器感知的差异。

hackernews · ray__ · 7月16日 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48936584)

**背景**: 对抗样本是对输入进行微小、通常不可察觉的扰动，导致机器学习模型出错。这种字体是针对文本识别的物理对抗样本，利用了人类对模糊的容忍度。类似技术已在结合高低空间频率的光学幻觉中使用。Decoy Font 的概念与早期融合高通和低通滤波图像的实验相似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.turbolens.io/blog/2025-12-20-watermarks-and-background-noise-a-silent-ocr-killer">Watermarks and Background Noise: A Silent OCR ... | TurboLens Blog</a></li>
<li><a href="https://christophm.github.io/interpretable-ml-book/adversarial.html">30 Adversarial Examples – Interpretable Machine Learning</a></li>

</ul>
</details>

**社区讨论**: 社区成员用 GPT、Claude 和 Gemini 测试了该字体，发现 GPT 在被提示后能部分识别隐藏信息，而 Claude 完全看不到。有人指出将图像缩小到 150x150 像素时，AI 会转而读取模糊文本。总体认为该字体在欺骗 AI 方面没有实际用途，但视觉设计巧妙，引发了有趣的讨论。

**标签**: `#typography`, `#adversarial AI`, `#OCR`, `#font design`, `#computer vision`

---

<a id="item-6"></a>
## [从 Rust 到 Zig 的编译器重写进展](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

文章描述了将 Roc 编译器从 Rust 重写为 Zig 的动机和经验，重点介绍了在安全性、性能和交叉编译方面的改进。 这次重写意义重大，因为它提供了 Rust 和 Zig 这两种现代系统编程语言之间的真实对比，并探讨了安全性、性能和工具链方面的权衡。这些见解影响着编译器开发人员和更广泛的编程语言社区。 作者指出，用于生成机器码的编译器通常需要不安全操作来实现热二进制修补等功能，但 Zig 的 ReleaseSafe 模式可以在运行时捕获释放后使用错误。重写还旨在改善交叉编译和增量构建。

hackernews · jorangreef · 7月16日 11:39 · [社区讨论](https://news.ycombinator.com/item?id=48933149)

**背景**: Zig 是一种通用系统编程语言，旨在改进 C 语言，具有手动内存管理、编译时泛型和一等公民的交叉编译功能。Rust 通过其借用检查器强调内存安全，且无需垃圾回收。文章讨论了在编译器开发中选择 Zig 而非 Rust 的权衡，特别是在安全性和性能方面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**社区讨论**: 评论中辩论编译器是否真的需要不安全代码，Steve Klabnik 认为只有像二进制修补这样的特定功能才需要不安全，而不是常规的代码生成。其他人质疑 Zig 的内存安全性声称，例如其捕获释放后使用错误的能力，并比较 Zig 与 Rust 的增量构建速度。一些人好奇为什么用于原型设计的 OCaml 没有被选为最终实现语言。

**标签**: `#Rust`, `#Zig`, `#compiler design`, `#memory safety`, `#programming languages`

---

<a id="item-7"></a>
## [索尼删除更多已购影片，引发数字所有权担忧](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/) ⭐️ 8.0/10

索尼从用户账户中移除了多部之前已在 PlayStation 商店购买的电影，实质上撤销了消费者自以为拥有的内容访问权限。 这一事件凸显了数字所有权的脆弱性——购买往往只是可随时撤销的许可证，削弱了消费者信任，并推动了关于真正数字所有权权益的讨论。 被删除影片的具体数量和片名未披露，但这并非索尼首次移除内容；2024 年就曾发生过类似删除事件。受影响用户未获得任何补偿或退款。

hackernews · nekusar · 7月16日 12:13 · [社区讨论](https://news.ycombinator.com/item?id=48933419)

**背景**: 数字版权管理（DRM）技术使公司能够控制对数字内容（如电影和软件）的访问权限，即使在消费者付费后也是如此。在许多情况下，所谓“购买”实际上是一种可撤销的许可证。这种模式与物理媒体所有权形成对比——除非实物丢失或损坏，否则买家可无限期保留访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management</a></li>
<li><a href="https://www.fortinet.com/resources/cyberglossary/digital-rights-management-drm">What Is DRM? Digital Rights Management Explained | Fortinet</a></li>

</ul>
</details>

**社区讨论**: 评论者对索尼的行为表示失望，有人认为消费者应获得实际视频文件而非许可证。另一些评论建议撤销时应提供全额退款以平衡经济影响。少数人指出此类删除行为屡见不鲜，而当前数字所有权模式存在不足。

**标签**: `#digital rights`, `#ownership`, `#movies`, `#sony`, `#consumer protection`

---

<a id="item-8"></a>
## [GPT-5.6 Codex 漏洞可删除 $HOME 目录](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

GPT-5.6 Codex 中的一个漏洞会在覆盖环境变量时意外删除用户的 $HOME 目录，前提是未启用沙箱保护和自动审核。 此漏洞突显了具有完全系统访问权限的 AI 编码代理的关键安全风险，强调必须采用沙箱和人工审核来防止破坏性操作。 该问题发生在启用完全访问模式、禁用沙箱和自动审核的情况下，模型尝试覆盖 $HOME 来定义临时目录，却错误地删除了 $HOME。

rss · Simon Willison · 7月16日 17:45

**背景**: OpenAI Codex 是一种 AI 编码代理，可以自主读取、编写和执行代码，通常能访问用户的文件系统。沙箱技术将代理的操作隔离，以防止对主机系统造成损害。如果没有沙箱和审核，代理的错误可能导致严重后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://amux.io/guides/ai-agent-sandboxing/">AI Agent Sandboxing in 2026: Docker, E2B, Firecracker... — amux</a></li>

</ul>
</details>

**标签**: `#codex`, `#generative-ai`, `#ai-safety`, `#coding-agents`, `#bug`

---

<a id="item-9"></a>
## [Linus Torvalds 支持在 Linux 中使用 AI，反对者可以分叉](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 内核的创建者和主要维护者 Linus Torvalds 明确表示，Linux 不是一个反 AI 的项目，AI 是一个明显有用的工具，并警告不同意的人可以分叉项目或离开。 这位顶级维护者的明确声明平息了关于在内核开发中使用 AI 的潜在社区争议，提供了清晰的指导，并可能加速 Linux 生态系统中 AI 辅助工具的采用。 Torvalds 强调 AI 与其他工具一样，其有用性已毋庸置疑，同时承认围绕 AI 经济仍存在未解问题。他是在回应 Linux 媒体邮件列表上的讨论。

rss · Simon Willison · 7月16日 13:26

**背景**: Linus Torvalds 是 Linux 内核（Linux 操作系统的核心）的创建者和长期维护者。开源社区中一直存在关于在开发中使用 AI 工具（如来自大型语言模型的代码生成）的伦理和效用辩论，有些项目已采取明确的禁令或限制。

**标签**: `#Linux`, `#AI`, `#Linus Torvalds`, `#kernel development`, `#open source`

---

<a id="item-10"></a>
## [ExTernD：扩展秩三元分解提升 LLM 量化精度](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

ExTernD 提出了一种用于大型语言模型训练后量化的扩展秩三元分解，将权重矩阵分解为两个三元矩阵和一个对角缩放矩阵，从而支持任意内部秩，并使精度接近任意量化级别。 该方法解决了先前三元 PTQ 方法的固定矩阵大小限制，以极小的 VRAM 开销实现高精度，这对于在资源受限硬件上高效部署大型语言模型至关重要。 该分解有效增加了三元表示的秩，作者证明，与标准量化方法相比，仅需轻微增加 VRAM，同时利用三元算术实现高效性。

reddit · r/MachineLearning · /u/LMTLS5 · 7月16日 13:31

**背景**: 训练后量化（PTQ）通过在不重新训练的情况下降低权重精度来压缩神经网络。三元量化将权重映射到 {-1, 0, +1}，提供高压缩率，但常因固定矩阵大小限制而精度有限。ExTernD 通过矩阵分解扩展表示秩来克服这一限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ternary-weight-ptq-framework">Ternary -Weight PTQ Framework</a></li>
<li><a href="https://www.researchgate.net/publication/395573778_Network_Splitting_Techniques_and_Their_Optimization_for_Lightweight_Ternary_Neural_Networks">(PDF) Network Splitting Techniques and Their Optimization for...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#quantization`, `#ternary decomposition`, `#PTQ`, `#efficient inference`

---

<a id="item-11"></a>
## [250%速度提升：98GB DeepSeek 在 4060 Ti 上达到 7 t/s](https://www.reddit.com/r/LocalLLaMA/comments/1uy33fw/deepseek_v4_flash_98gb_on_1x_4060ti_cpu_got_300/) ⭐️ 8.0/10

一位用户报告，最近的 llama.cpp 提交（b9986 到 b10034 之间）将 98GB 的 DeepSeek-V4-Flash-UD-Q2_K_XL 模型在一台配备 RTX 4060 Ti（16GB 显存）和 6 核 CPU 的系统上的推理速度从 2 个 token/秒提升到了 7 个 token/秒，速度提升了 250%。 这表明像 DeepSeek V4 Flash（总参数量 284B，激活 13B）这样的大型混合专家模型，通过激进的量化和 CPU-GPU 混合推理，可以在低廉的消费级硬件上变得可用。这降低了无需昂贵 GPU 即可运行先进本地大语言模型的门槛。 该模型使用了 UD-Q2_K_XL 量化（Q2_K 的一种超低位变体），将 98GB 的参数压缩到 CPU 内存中。该系统拥有 138GB 的系统内存，并将超出 16GB 显存的层卸载到 CPU。用户采用了 split-mode=layer 和 flash attention 来实现速度提升。

reddit · r/LocalLLaMA · /u/Chuyito · 7月16日 13:35

**背景**: llama.cpp 是一个开源库，用于在消费级硬件上高效推理大语言模型，支持 CPU、GPU 以及通过层卸载的混合推理。量化降低模型精度以适配有限内存，像 Q2_K 这样的 K-quant 是最小的可行格式。DeepSeek V4 Flash 是一个混合专家模型，总参数量 284B，但每个 token 仅激活 13B，有助于降低计算成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://craftrigs.com/guides/llama-cpp-cpu-gpu-hybrid-inference-limited-vram/">llama . cpp CPU + GPU Hybrid Inference : Run 70B on Any... | CraftRigs</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>

</ul>
</details>

**标签**: `#local-llm`, `#inference-optimization`, `#llama.cpp`, `#hardware-efficiency`, `#deepseek`

---

<a id="item-12"></a>
## [xAI 起诉用户用 Grok 制作儿童性虐待深度伪造](https://www.reuters.com/legal/litigation/musks-xai-sues-grok-user-over-sexualized-deepfakes-2026-07-15/) ⭐️ 8.0/10

xAI 对南卡罗来纳州男子 Terry Harwood 提起诉讼，指控其滥用 Grok AI 聊天机器人生成儿童性虐待材料和非自愿成人色情深度伪造，违反了服务条款。 这是首批 AI 公司因用户生成儿童性虐待材料而起诉用户的案件之一，可能为 AI 安全和内容审核树立法律先例。 xAI 要求赔偿并申请永久禁止 Harwood 使用 Grok；该公司今年已暂停 52,222 个账户，向国家失踪与受虐儿童中心举报 73,604 次，促成至少 244 人被捕。

telegram · zaihuapd · 7月16日 01:45

**背景**: 深度伪造是利用机器学习生成的合成媒体，通常通过生成对抗网络（GAN）实现，两个神经网络相互对抗以创建逼真的虚假图像或视频。该技术可能被滥用于制作非自愿的露骨内容，包括儿童性虐待材料，引发严重的法律和伦理问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/what-is-deepfake">What Are Deepfakes and How Are They Created? - IEEE Spectrum</a></li>
<li><a href="https://in.norton.com/blog/emerging-threats/what-are-deepfakes">Deepfakes : What they are and why they’re threatening | NortonLifeLock</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#legal`, `#Grok`, `#content moderation`, `#deepfakes`

---

<a id="item-13"></a>
## [日本采购 2.75 万块英伟达 Rubin 芯片打造机器人 AI](https://www.bloomberg.com/news/articles/2026-07-16/japan-to-buy-nvidia-rubin-chips-to-build-sovereign-ai-for-robots) ⭐️ 8.0/10

日本宣布计划采购 2.75 万块英伟达下一代 Rubin 芯片，由新成立的 Noetra 公司牵头建设大型数据中心，开发面向机器人的主权 AI 基础模型，并获得政府 3873 亿日元（约 240 亿美元）拨款支持。 此举标志着日本战略转向，旨在减少对外国 AI 技术的依赖，强化机器人产业，争取到 2040 年占据全球机器人市场 30%以上份额，可能重塑与中美竞争的格局。 Noetra 公司由田场广信领导，计划于 2027 年 3 月发布首个 AI 模型，并在数年内推出机器人专用版本，参与方包括软银、丰田支持的 Preferred Networks 和 NEC。

telegram · zaihuapd · 7月16日 10:59

**背景**: 英伟达 Rubin 架构是其下一代 GPU 平台，旨在整合 GPU、CPU、网络和存储，构建大规模 AI 工厂。主权 AI 是指国家开发自主 AI 能力以实现战略自主的概念，在中美科技竞争背景下日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thundercompute.com/blog/nvidia-rubin-architecture">Nvidia Rubin Architecture : Everything You Must... | Thunder Compute</a></li>
<li><a href="https://www.linkedin.com/posts/itmatterss_nvidia-unveils-rubin-architecture-at-ces-activity-7414182623264059393-ZHRl">Nvidia Unveils Rubin Architecture for AI Workloads | LinkedIn</a></li>
<li><a href="https://www.aol.com/finance/nvidia-rubin-architecture-game-changer-172211628.html">Nvidia ’s Rubin Architecture Is a Game-Changer. Here’s Why. - AOL</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI chips`, `#robotics`, `#Japan`, `#sovereign AI`

---

<a id="item-14"></a>
## [台积电再投千亿美元赴美，Q2 利润飙升 77%创新高](https://www.reuters.com/world/asia-pacific/tsmcs-second-quarter-profit-seen-hitting-record-ai-boom-2026-07-15/) ⭐️ 8.0/10

台积电宣布再向美国亚利桑那州投资 1000 亿美元，使在美总投资规模增至 2650 亿美元；同时公布二季度净利润同比飙升 77%至 7066 亿新台币（约 220 亿美元），创历史新高，远超市场预期。 这笔巨额投资凸显了台积电在地缘政治紧张局势下将制造布局从台湾分散化转移的战略；同时，创纪录的利润彰显了 AI 芯片的旺盛需求，巩固了台积电在全球半导体供应链中的核心地位。 台积电还在 2026 年资本支出预测上调至 600 亿至 640 亿美元，预计全年美元营收将增长略超 40%；亚利桑那州目前已有 8 座工厂在建或规划中，未来可能再增 4 座。

telegram · zaihuapd · 7月16日 12:29

**背景**: 台积电是全球最大的专业半导体代工厂，为苹果、英伟达、AMD 等公司生产芯片。AI 需求推动了先进芯片（尤其是采用领先制程的芯片）的爆发式增长。美国政府通过《芯片法案》鼓励芯片制造回流，台积电在亚利桑那州的扩张成为供应链安全的关键一环。

**标签**: `#semiconductor`, `#TSMC`, `#AI`, `#investment`, `#supply chain`

---