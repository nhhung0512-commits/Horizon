---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 29 条内容中筛选出 8 条重要资讯。

---

1. [Kimi K3：开源 2.8T 模型登顶前端编程竞技场](#item-1) ⭐️ 9.0/10
2. [Fastjson 1.x 高危无 gadget RCE 漏洞](#item-2) ⭐️ 9.0/10
3. [vLLM v0.26.0：支持 Inkling 模型，大幅提升 DeepSeek-V4 性能](#item-3) ⭐️ 8.0/10
4. [Libsm64 将超级马里奥 64 转化为可复用的游戏引擎库](#item-4) ⭐️ 8.0/10
5. [Bun 的 Rust 重写已集成到 Claude Code，发布推迟](#item-5) ⭐️ 8.0/10
6. [谷歌宣布 Gemini 4 为最雄心勃勃的预训练项目](#item-6) ⭐️ 8.0/10
7. [中方驳美方拟制裁 AI 蒸馏，警告将反制](#item-7) ⭐️ 8.0/10
8. [中芯国际测试中国首台国产 DUV 光刻机](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3：开源 2.8T 模型登顶前端编程竞技场](https://t.me/zaihuapd/42793) ⭐️ 9.0/10

月之暗面发布了 Kimi K3，这是全球首个开源 2.8 万亿参数模型。它在 Frontend Code Arena 基准测试中以 1679 分排名第一，超越了 Fable 5。 此次发布通过提供具有新颖架构的大型开源模型，在编程任务上超越领先的专有模型，从而推动了开源 AI 的前沿。它为研究和企业定制提供了广泛使用最先进能力的机会。 K3 采用 Kimi Delta Attention 和 Attention Residuals 架构，支持原生视觉和 100 万 token 的上下文窗口。它在 7 个评测领域中 6 项居首，仅在游戏领域落后。

telegram · zaihuapd · 7月27日 06:27

**背景**: Kimi K3 基于混合线性注意力架构构建，结合了 Kimi Delta Attention（KDA）——一种富有表现力的线性注意力机制，以及 Attention Residuals（AttnRes）——用基于学习的、输入相关的深度注意力取代标准残差连接。这些创新旨在提高效率和性能，尤其是在长上下文场景中。该模型采用专家混合（MoE）方法训练，参数量为 2.8 万亿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.15031">[2603.15031] Attention Residuals - arXiv.org GitHub - MoonshotAI/Attention-Residuals Attention Residuals - arXiv.org Images Attention Residuals Explained: Rethinking Transformer Depth Attention Residuals by Kimi AI: A Clear Explanation Standard Transformer Attention vs. Attention-Residuals: A ... Attention Residuals: How Kimi Is Rethinking Transformer Depth</a></li>
<li><a href="https://arxiv.org/pdf/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://aitoolhunt.co/blog/kimi-k3-benchmarks-frontend-code-arena-2026">Kimi K3 Benchmarks : Frontend Leap and Review... | AIToolHunt</a></li>

</ul>
</details>

**社区讨论**: 社区评论对开放权重用于微调和知识产权主权表示兴奋，但也有人指出托管成本高昂（估计约 1.5TB VRAM），以及商业许可限制：年营收超过 2000 万美元需单独与月之暗面签订协议。初始提供商的定价显示输入每百万 token 3 美元，输出每百万 token 15 美元。

**标签**: `#AI`, `#open-source`, `#large language model`, `#benchmark`, `#architecture`

---

<a id="item-2"></a>
## [Fastjson 1.x 高危无 gadget RCE 漏洞](https://t.me/zaihuapd/42797) ⭐️ 9.0/10

安全研究人员 Kirill Firsov 披露，Fastjson 1.x 版本 1.2.68 至 1.2.83 存在高危远程代码执行漏洞，该漏洞无需开启 autoType 或依赖 classpath gadget，可在 JDK 8、17 和 21 上利用。 这是广泛使用的 JSON 库的一个严重安全问题，由于 Fastjson 1.x 已停止维护且不会发布补丁，唯一缓解措施是升级到 Fastjson2。 该漏洞影响 Fastjson 1.x 从 1.2.68 到 1.2.83 的所有版本，无需 autoType 支持等特定条件，可在包括 JDK 8、17 和 21 在内的多个 JDK 版本上利用。

telegram · zaihuapd · 7月27日 10:31

**背景**: Fastjson 是阿里巴巴最初开发的流行 JSON 处理库，广泛应用于 Java 应用程序。AutoType 是一个允许多态反序列化的特性，一直是反序列化漏洞的常见攻击向量。该 RCE 无需 autoType 或 gadgets 即可利用，使其尤其危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Fastjson">Fastjson</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#RCE`, `#Fastjson`, `#Java`

---

<a id="item-3"></a>
## [vLLM v0.26.0：支持 Inkling 模型，大幅提升 DeepSeek-V4 性能](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0（包含 411 次提交，212 位贡献者）新增对 Thinking Machines Lab Inkling 模型家族（1 万亿参数多模态 MoE）的完整支持，通过专用内核为 DeepSeek-V4 带来显著性能提升（单次生成 token 时间最高提升 2.94%），引入用于生成模型的 fp32 lm_head，并支持按 KV 缓存组灵活选择注意力后端。 此版本通过为一个重要的开源模型家族（Inkling）提供首发支持，显著扩大了 vLLM 的模型覆盖范围。针对 NVIDIA、AMD 和 Intel 硬件的 DeepSeek-V4 优化降低了这一最热门 MoE 架构的推理成本，而 fp32 lm_head 等功能则提升了许多模型的生成精度。 Inkling 模型支持包括基础建模、分段 CUDA 图、Hopper FlashAttention-4 相对注意力、MTP=1 推测解码、LoRA 和 ModelOpt NVFP4 量化。对于 DeepSeek-V4，专用路由内核使端到端单次生成 token 时间提升 2.94%，fused_topk_bias 将内核速度提升 1.5-2 倍。新增的 head_dtype 选项允许使用 fp32 lm_head 提高精度，并且现在可以按 KV 缓存组选择注意力后端。

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个开源的高吞吐量大语言模型推理引擎，广泛用于部署大语言模型。Thinking Machines Lab 的 Inkling 模型是一个 1 万亿参数的多模态混合专家（MoE）Transformer，支持文本、图像和音频输入，上下文长度可达 100 万 tokens。FlashAttention-4 是一种针对 Hopper GPU 优化的新型注意力算法，而推测解码是一种使用小型草稿模型加速大型目标模型推理且不损失质量的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://recipes.vllm.ai/thinkingmachines/Inkling">thinkingmachines/Inkling | vLLM Recipes</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance | vLLM Blog</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#performance optimization`, `#model support`

---

<a id="item-4"></a>
## [Libsm64 将超级马里奥 64 转化为可复用的游戏引擎库](https://github.com/libsm64/libsm64) ⭐️ 8.0/10

Libsm64 是一个软件库，从逆向工程的超级马里奥 64 反编译中提取移动和渲染代码，提供干净的 API，可集成到如 Half-Life 2 等外部游戏引擎中。 这实现了前所未有的跨游戏互操作性，使马里奥角色能够在其他游戏中自然出现和行为，展示了逆向工程在创意混搭中的潜力，无需区块链或元宇宙炒作。 该库基于超级马里奥 64 的完全反编译（日版、美版、欧版、Shindou、iQue 版本），编译时需要原始游戏 ROM。它已被用于如 Half-Life 2 中的马里奥和独立 SDL2 演示等项目。

hackernews · klaussilveira · 7月27日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49067352)

**背景**: 超级马里奥 64 于 2019 年由 sm64 反编译项目完全反编译，从原始 N64 二进制文件中生成了可读的 C 代码。该反编译虽然仅合法分发代码（不包含资源），但允许开发者理解和修改游戏逻辑。Libsm64 在此基础上，将关键子系统打包成带有稳定 API 的可复用库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/libsm64/libsm64">GitHub - libsm 64 / libsm 64 : Mario 64 as a library for use in external...</a></li>
<li><a href="https://github.com/n64decomp/sm64">GitHub - n64decomp/sm64: A Super Mario 64 decompilation, brought to you by a bunch of clever folks. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区非常热情，评论者称其“不可思议”，并指出它实现了元宇宙的承诺，没有炒作。示例包括 Half-Life 2 中的马里奥，以及非工程师用户设置难易度的问题。也有人开玩笑说可以将其作为服务销售。

**标签**: `#reverse-engineering`, `#game development`, `#interoperability`, `#C++`

---

<a id="item-5"></a>
## [Bun 的 Rust 重写已集成到 Claude Code，发布推迟](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) ⭐️ 8.0/10

Bun 的创建者 Jarred 宣布，Bun 的 Rust 重写已在一个月前集成到 Claude Code 中，而 Bun 1.4 的发布将推迟，直到达到承诺的新增通过 Node.js 测试数量。 这次从 Zig 到 Rust 的重写是 Bun（一个流行的 JavaScript 运行时）的重大架构变化，可能影响性能和兼容性。延迟发布表明了对 Node.js 兼容性的坚定承诺，这对采用至关重要。 Rust 重写是通过使用 LLM 转换代码库实现的，发布因待合并的改进 Node.js 测试通过数的拉取请求而受阻。目标数字在之前的视频中提到过，但尚未达到。

hackernews · tomlockwood · 7月27日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=49067854)

**背景**: Bun 是一个集 JavaScript 运行时、打包器、测试运行器和包管理器于一体的工具，旨在作为 Node.js 的快速替代品。它最初用 Zig 编写，但团队决定用 Rust 重写以获得更好的生态系统支持和性能。Claude Code 是 Anthropic 开发的一款 AI 驱动的编程助手，能够理解和编辑代码库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>

</ul>
</details>

**社区讨论**: Jarred 的评论提供了关于延迟和测试数量承诺的透明度。一些评论者质疑使用 LLM 进行转换，而另一个人则指出 Bun 的一个 Zig 分支声称通过坚持最佳实践实现了亚秒级构建时间，暗示重写可能并非绝对必要。

**标签**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#rewrite`, `#community update`

---

<a id="item-6"></a>
## [谷歌宣布 Gemini 4 为最雄心勃勃的预训练项目](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 8.0/10

谷歌 CEO 桑达尔·皮查伊在 Alphabet 2026 年第二季度财报会上透露，下一代大模型 Gemini 4 已投入训练，称其为公司迄今最具雄心的预训练项目，计划于 2026 年底发布。 这表明谷歌持续大力投资前沿 AI 和通用人工智能（AGI），以保持对 OpenAI 等竞争对手的优势。Gemini 4 的发布可能会推动推理、编程和多模态理解等能力的进步。 皮查伊强调，计算资源将优先用于前沿 AGI 研发，模型预计在 2026 年 11 月或 12 月发布。同时，Gemini 3.x Flash 系列将继续每月更新，重点提升编码能力。

telegram · zaihuapd · 7月27日 04:06

**背景**: 预训练是指在大型通用数据集上训练机器学习模型，使其学习通用模式，然后再针对特定任务进行微调。通用人工智能（AGI）是一种假设性的 AI 系统，能够在广泛的任务中匹配或超越人类认知能力。谷歌与多家科技公司一样，公开将 AGI 作为长期目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre-trained transformer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini 4`, `#AI`, `#Large Language Model`, `#AGI`

---

<a id="item-7"></a>
## [中方驳美方拟制裁 AI 蒸馏，警告将反制](https://www.mofcom.gov.cn/syxwfb/art/2026/art_7f1622463a7c48ef9fad600ce0ef702f.html) ⭐️ 8.0/10

中国商务部公开驳斥美国指控中国 AI 企业进行非法模型蒸馏，指出美国企业同样在训练中使用中国模型，并警告若美方制裁损害中方利益将采取必要反制措施。 这加剧了美中科技紧张局势，可能影响全球 AI 合作，因为模型蒸馏是广泛使用的技术。争端可能导致 AI 生态系统分裂，并增加 AI 开发的监管障碍。 中方声明提到近 200 家美国初创企业已呼吁政府不要限制访问中国开源模型，并指出模型蒸馏是行业常见做法，本身并不违法。

telegram · zaihuapd · 7月27日 11:01

**背景**: 模型蒸馏是一种机器学习技术，通过让较小的学生模型从较大的教师模型中学习，以较低的计算成本实现相似的性能。美国当局近期调查中国 AI 企业涉嫌蒸馏 OpenAI 等公司的前沿模型，引发知识产权担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intellectyx.com/model-distillation-ai-starter-guide-techniques-benefits-and-applications/">AI Model Distillation Guide: Techniques , Benefits & Applications</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#model distillation`, `#geopolitics`, `#China`, `#US sanctions`

---

<a id="item-8"></a>
## [中芯国际测试中国首台国产 DUV 光刻机](https://t.me/zaihuapd/42800) ⭐️ 8.0/10

中芯国际正在试运行中国首台由上海初创公司宇量昇研发的国产深紫外（DUV）光刻机，用于生产 28 纳米芯片，并尝试通过多重图形化工艺实现 7 纳米甚至 5 纳米节点。 这标志着在美国出口管制阻止中国获得 ASML 先进 EUV 光刻系统的背景下，中国在半导体自给自足方面迈出了重要一步。如果成功，可能减少中国在成熟和先进节点上对外国设备的依赖。 该设备大部分零部件已实现国产化，但仍有部分依赖进口。中芯国际利用该机生产 28 纳米芯片，并尝试通过多重图形化实现 7 纳米，但良率目前较低；业内人士预计实现量产和稳定良率至少需要一至两年，量产目标定在 2027 年。

telegram · zaihuapd · 7月27日 14:10

**背景**: DUV 光刻使用紫外线（例如 193 纳米波长）来图案化芯片，其先进程度低于 EUV（13.5 纳米），后者是 7 纳米以下尖端节点所必需的。ASML 在 DUV 和 EUV 市场均占主导地位，但美国出口管制阻止 ASML 向中国出售 EUV 机器。多重图形化技术，如双重或四重图形化，允许 DUV 系统通过多次曝光在晶圆上创建更小的特征，但成本更高、良率较低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multiple_patterning">Multiple patterning - Wikipedia</a></li>
<li><a href="https://www.asml.com/en/products/duv-lithography-systems">See ASML's DUV lithography systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Extreme_ultraviolet_lithography">Extreme ultraviolet lithography</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#lithography`, `#SMIC`, `#DUV`, `#China tech`

---