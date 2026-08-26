---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> 从 34 条内容中筛选出 11 条重要资讯。

---

1. [Qwen3.8-Flash-Next：N-gram 嵌入 MoE 模型，激活 6B 参数](#item-1) ⭐️ 9.0/10
2. [DeepSeek-V4-Pro 正式上线，API 实行峰谷定价](#item-2) ⭐️ 9.0/10
3. [vLLM v0.28.0 发布，大幅优化 Kimi-K3 与 DeepSeek V4 性能](#item-3) ⭐️ 8.0/10
4. [Tailcat：基于 Tailscale 数据平面的类 Netcat 工具](#item-4) ⭐️ 8.0/10
5. [GLM-5.3-Flash：以五分之一成本实现接近旗舰级的 AI 性能](#item-5) ⭐️ 8.0/10
6. [AWS 收购 DuckLabs，DuckDB 开源项目仍归基金会所有](#item-6) ⭐️ 8.0/10
7. [恢复 57.5 万裁剪标签：人工点击胜过更大模型](#item-7) ⭐️ 8.0/10
8. [ImageBench：开放文本到图像基准，含 52 个模型和 9 千张图片](#item-8) ⭐️ 8.0/10
9. [X 向开源项目 Nitter 发停止函，主站下线并暂停开发](#item-9) ⭐️ 8.0/10
10. [智谱确认 Ox Alpha 为 GLM 新迭代，使用量超 DeepSeek 两倍](#item-10) ⭐️ 8.0/10
11. [腾讯开源多模态嵌入模型 WeMM-Embedding，多项基准领先](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen3.8-Flash-Next：N-gram 嵌入 MoE 模型，激活 6B 参数](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 9.0/10

阿里巴巴通义千问发布了 Qwen3.8-Flash-Next，这是基于全新 Qwen4 架构的大语言模型。该模型拥有 125B 参数的混合专家（MoE）结构，并额外包含 51B 的 N-gram 嵌入，每个 token 只激活 6B 参数。 此次发布引入了新颖的 N-gram 嵌入架构，以内存换取算力，训练成本仅为 Qwen3.7-Plus 的 1/9，但综合性能全面超越。这可能会为更高效的大模型设计铺平道路，并让先进的模型更易于在本地运行。 该模型的有效参数量约为 176B，这引发了对量化的疑问：4-bit 量化可能超过 100GB，可能无法放入 128GB 统一内存。根据 BenchLM，它在 226 个模型中排名第 25，综合得分 67.54/100，在 SWE Multilingual 方面表现强劲。

hackernews · tosh · 8月26日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=49448210)

**背景**: N-gram 嵌入是一种通过 token 序列（n-gram）来表示词的技术，使模型能够在不过多增加激活参数的情况下捕捉更多上下文。在混合专家（MoE）模型中，每个 token 只激活一部分参数，因此可以拥有更大的总参数量，同时保持推理效率。Qwen3.8-Flash-Next 是首个基于 Qwen4 架构的开源模型，设计为可在 128GB 工作站或 Mac 上以 4-bit 量化运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atomic.chat/blog/guides/how-to-run-qwen-3-8-flash-next-locally">How to Run Qwen 3 . 8 Flash Next Locally: GGUF... - Atomic Chat</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://benchlm.ai/models/qwen3-8-flash-next">Qwen 3 . 8 - Flash - Next Benchmarks & Context (August 2026)</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极但看法不一。Simon Willison 在不同推理级别上进行了测试，对他没有获得像 Qwen 3.8 27B 那样满意的结果感到惊讶，而 rohansood15 则指出它明显胜过 3.8 27B。一些评论者（andy99、schopra909）讨论了 N-gram 架构的有效大小、量化可行性及其背后的直觉，并提到 DeepSeek 早前的论文。tosh 强调新架构预示着 Qwen4，并指出其训练成本仅为 Qwen3.7-Plus 的 1/9。

**标签**: `#AI`, `#Qwen`, `#Large Language Models`, `#Architecture`, `#Machine Learning`

---

<a id="item-2"></a>
## [DeepSeek-V4-Pro 正式上线，API 实行峰谷定价](https://t.me/zaihuapd/43417) ⭐️ 9.0/10

DeepSeek-V4-Pro 正式版同步上线 APP、网页端和 API，模型名为 deepseek-v4-pro，调用方式不变。该版本增强 Agent 能力，原生支持 Responses API 格式，并为 V4-Pro 和 V4-Flash 新增 low、high、max 三档思考模式。 这是广泛使用的 AI 模型 DeepSeek 的一次重大版本发布，提升了其智能体（Agent）能力以及与 Codex 等工具的互操作性。新的 API 峰谷定价（闲时价格为高峰时段一半）可能显著影响开发者的成本和使用模式，对 AI/ML 社区影响深远。 API 调用方式不变，模型名设为 deepseek-v4-pro。新的峰谷定价自 2026 年 8 月 17 日 0 时生效，闲时价格降为高峰时段的一半；V4-Pro 和 V4-Flash 的思考模式新增 low、high、max 三档。

telegram · zaihuapd · 8月26日 08:02

**背景**: DeepSeek 是中国一家以发布大语言模型著称的 AI 公司，其 API 可让开发者将 AI 能力集成到各类应用中。Responses API 是一种较新的接口格式，它将聊天补全和助手功能整合为统一的有状态多轮交互体验。峰谷定价常见于电力等公用事业，通过降低闲时价格鼓励用户错峰使用。Agent（智能体）能力指的是模型进行推理、规划并自主行动的能力，通常涉及调用外部工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses">Use the Azure OpenAI Responses API - Microsoft Foundry | Microsoft Learn</a></li>
<li><a href="https://aws.amazon.com/what-is/api/">What is an API ? - Application Programming Interfaces Explained -...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI`, `#LLM`, `#API`, `#Release`

---

<a id="item-3"></a>
## [vLLM v0.28.0 发布，大幅优化 Kimi-K3 与 DeepSeek V4 性能](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) ⭐️ 8.0/10

vLLM v0.28.0 正式发布，包含来自 270 位贡献者的 584 次提交，重点为 Kimi-K3 进行了大规模性能优化（如 Decode Context Parallel 和融合 FlashKDA 内核），并为 DeepSeek V4 提供了端到端稀疏 MLA 支持，同时支持 ROCm 和分层 KV 缓存卸载。新默认值包括将 max_num_batched_tokens 提升至 16384，以及为 Mamba 模型默认启用前缀缓存。 vLLM 是目前应用最广泛的 LLM 推理引擎之一，因此这些优化直接提升了 Kimi-K3、DeepSeek V4 等前沿模型的推理速度和内存效率。用户将受益于更低的延迟、更高的吞吐量以及更低的 GPU 内存开销，尤其是在投机解码和 MoE 工作负载方面。 值得注意的改进包括：自适应投机 token 预算使 DSpark TTFT 提升约 60%，合并 all-gather 带来 1.5–3 倍的内核级加速，以及可选的共享专家分片每 GPU 节省约 17 GiB 内存。破坏性变更包括 bitsandbytes 迁移到插件机制，以及 Transformers 版本升级至 5.15.0。

github · khluu · 8月26日 09:46

**背景**: vLLM 是一个开源的高吞吐 LLM 推理引擎，通过 PagedAttention 优化显存管理，并支持连续批处理。Kimi-K3 和 DeepSeek V4 是采用混合专家（MoE）架构的大语言模型，token 会被路由到专门的专家模块；MegaMoE 就是针对这类模型的高性能架构。DeepSeek V4 还使用了稀疏 MLA（多潜变量注意力）和 DSpark——一个开源的投机解码框架，通过让草稿模型并行提出候选 token 再由目标模型验证，从而加速推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark : Confidence-Scheduled Speculative Decoding...</a></li>
<li><a href="https://codersera.com/blog/deepseek-dspark-explained-2026/">DeepSeek DSpark : 51–400% Faster V4 Inference (2026)</a></li>
<li><a href="https://deepwiki.com/deepseek-ai/DeepGEMM/3.3-mega-moe-architecture">Mega MoE Architecture | deepseek-ai/DeepGEMM | DeepWiki</a></li>

</ul>
</details>

**标签**: `#vllm`, `#LLM inference`, `#performance optimization`, `#DeepSeek`, `#release`

---

<a id="item-4"></a>
## [Tailcat：基于 Tailscale 数据平面的类 Netcat 工具](https://github.com/tailscale/tailcat) ⭐️ 8.0/10

Tailscale 发布了 tailcat，这是一个类似 netcat 的命令行工具，利用 Tailscale 的数据平面（magicsock）在机器之间建立点对点 TCP/UDP 连接。它提供 WireGuard 加密的安全隧道，而无需依赖 Tailscale 的控制平面来转发流量。 Tailcat 简化了点对点网络工具和服务的构建，降低了开发者使用 Tailscale 的 NAT 穿透和安全隧道基础设施的门槛。它带来了诸多实际用例，如远程访问、自定义协议，甚至 Minecraft 模组，也反映了点对点连接日趋简便的行业趋势。 Tailcat 使用 Tailscale 的 magicsock 数据平面创建点对点的 WireGuard 加密隧道，DERP 作为 NAT 打洞的辅助通道和 NAT 穿透失败时的最后中继。它不需要 Tailscale 的控制平面即可工作，并且该项目提供了 Nix 安装/开发环境。

hackernews · nderjung · 8月26日 17:42 · [社区讨论](https://news.ycombinator.com/item?id=49452990)

**背景**: Tailscale 是一种软件定义网状 VPN，可将设备连接成一个 'tailnet'。其控制平面负责协调和策略，而数据平面则运行在每个设备上，以网状结构在机器之间直接传输加密流量。Netcat 是经典的 Unix 网络工具，用于通过 TCP/UDP 读写数据，常用于测试和脚本；tailcat 将类似的接口带到了现代点对点网络中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tailscale/tailcat">GitHub - tailscale/tailcat: like netcat, but over Tailscale's data plane, without Tailscale's control plane · GitHub</a></li>
<li><a href="https://tailscale.com/docs/concepts/control-data-planes">Control and data planes · Tailscale Docs</a></li>
<li><a href="https://tailscale.com/blog/how-tailscale-works">Tailscale: How it works</a></li>

</ul>
</details>

**社区讨论**: 社区对 tailcat 的反响积极而热烈。Brad Fitzpatrick 展示了一个基于 tailcat 的 Minecraft 模组，用户将其与 Iroh 进行比较，还有开发者表示它启发自己重新思考 SSH 连回家的方案。也有人指出，如果 IPv6 普及（避免 CGNAT），这类工具的必要性会降低；还有用户询问 Tailscale 是否将 Nix 作为标准开发环境。

**标签**: `#networking`, `#tailscale`, `#p2p`, `#developer-tools`, `#golang`

---

<a id="item-5"></a>
## [GLM-5.3-Flash：以五分之一成本实现接近旗舰级的 AI 性能](https://z.ai/blog/glm-5.3-flash) ⭐️ 8.0/10

Z.ai 发布了 GLM-5.3-Flash，这是一款高性价比多模态模型，以极低的成本提供接近 GLM5.3 的性能，权重已在 Hugging Face 上开放。该模型采用 320B 参数 MoE 架构，其中 18B 参数为活跃参数。 此次发布标志着行业正向“以极低成本实现接近前沿模型推理”的趋势发展，可能使先进 AI 对小型开发者更可用，并支持本地或半本地部署。同时，它也加剧了 AI 实验室之间的竞争压力，尤其是像 Z.ai 这样的中国实验室正以颠覆性的价格推动开放权重模型。 GLM-5.3-Flash 是 GLM-5 系列中首个原生多模态模型，在 Artificial Analysis 智能指数中得分 57，在 Z.ai 的 API 上输出速度达每秒 48.7 tokens。据报道，其参数量约为 GLM5.3 的一半，服务成本约为 GLM5.3 的五分之一，并且可在国产芯片上运行。

hackernews · Philpax · 8月26日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49449507)

**背景**: GLM 是由中国 AI 公司 Z.ai（智谱）开发的一系列开放权重大语言模型，以 ChatGLM 而闻名。MoE（混合专家）架构如本例所示，每次 token 只激活部分参数，从而降低计算量和成本，同时保持较高容量。来自中国实验室的开放权重模型在性价比上越来越有竞争力，推动了 AI 生态系统的快速迭代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/vlm/glm-5.3-flash">GLM-5.3-Flash - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://artificialanalysis.ai/models/glm-5-3-flash">GLM-5.3-Flash - Intelligence, Performance & Price Analysis | Artificial Analysis</a></li>
<li><a href="https://unsloth.ai/docs/models/glm-5.3">GLM-5.3-Flash | Unsloth Documentation</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者普遍对这一快速的进步速度和性价比印象深刻，有人指出它“比几个竞争对手更聪明且更便宜”。其他人讨论了本地硬件对重度用户的经济可行性，同时有人提醒注意 Z.ai 的服务条款，并警告不要过度依赖厂商的基准测试。

**标签**: `#AI`, `#machine learning`, `#LLM`, `#model release`, `#benchmarks`

---

<a id="item-6"></a>
## [AWS 收购 DuckLabs，DuckDB 开源项目仍归基金会所有](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐️ 8.0/10

AWS 已收购 DuckLabs，即 DuckDB 背后的商业公司。开源 DuckDB 项目仍归非营利组织 DuckDB 基金会所有。 此次收购是数据库领域的一件大事，因为 DuckDB 已成为广泛使用的嵌入式分析型 SQL 引擎。由于基金会仍持有开源知识产权，核心项目的治理可能保持独立，但 AWS 对商业生态系统的影响力可能很大。 DuckLabs 是从 CWI（荷兰数学与计算机科学研究中心）分拆出来的，当时成立了 DuckDB 基金会来持有开源项目的全部知识产权。此次收购不转移 DuckDB 源代码的所有权，但 DuckLabs 商业服务和功能的未来尚待观察。

hackernews · onderkalaci · 8月26日 12:59 · [社区讨论](https://news.ycombinator.com/item?id=49448321)

**背景**: DuckDB 是一款开源的嵌入式列式分析型 SQL 数据库，旨在无需独立服务器即可对大型数据集进行快速查询。它因在 Python、R 等环境中的嵌入式分析功能而广受欢迎，与 Apache DataFusion 以及大型云数据仓库等形成竞争。当 DuckLabs 从 CWI 分拆时，成立了 DuckDB 基金会以保护该项目的开源性质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DuckDB">DuckDB - Wikipedia</a></li>
<li><a href="https://duckdb.org/">DuckDB – An in- process SQL OLAP database management system</a></li>

</ul>
</details>

**社区讨论**: 评论者的看法在祝贺与担忧之间分歧明显。有人担心 AWS 对开源项目的维护记录不佳，可能不会悉心培育 DuckDB；也有人指出基金会拥有知识产权，会限制 AWS 的控制力。还有评论者推荐用 Apache DataFusion 作为替代方案，另有人提到 AWS 内部混乱和人才流失问题。

**标签**: `#AWS`, `#DuckDB`, `#acquisition`, `#database`, `#open-source`

---

<a id="item-7"></a>
## [恢复 57.5 万裁剪标签：人工点击胜过更大模型](https://www.reddit.com/r/MachineLearning/comments/1vz2ojw/we_recovered_575k_crop_labels_from_a_decade_of/) ⭐️ 8.0/10

作者通过 SIFT+MAGSAC 注册，从十年间在 1,765 本乌尔都语图书上的手工 Photoshop 工作中恢复了 575,729 个裁剪标签，并用它们训练书籍数字化模型。扩大训练数据、改用 ResNet-50、提高分辨率都无效，而每本书仅 10 个操作员修正的裁剪就把 pass@80 从 0.71 提升到 0.83。 这对机器学习社区是一个有价值的反面结果：它表明当主要误差是每卷特有的、不在像素中体现的人工偏好时，增加数据或模型容量无法修复。这种人在回路中的校准方法为要求完美的档案数字化和文档处理提供了实用模板。 恢复几何使用 SIFT+MAGSAC 并在保守的接受阈值下完成；逐卷误差分析显示，失败源于操作员边距内缩的近似恒定偏移。在修图任务中，作者仅用 U-Net 做检测，经典 OpenCV 重建图像，并采用 REMOVE/KEEP/IGNORE 标签方案和变音符号否决规则，使标记 IoU 从 0.56 提升到 0.60，同时将符号误报降至零。

reddit · r/MachineLearning · /u/laamaleph · 8月26日 16:53

**背景**: 书籍数字化通常需要拍摄书页并手动裁剪到内容区域；对于罕见的乌尔都语石印本和词典，这一过程极其耗费人力。巴基斯坦的 Ibteda 数字图书馆花了十年时间在 Photoshop 中手工完成页面，不知不觉中记录了隐含的裁剪决策。作者将完成页注册回原始照片以生成监督信号，并使用 pass@k 作为指标、MAGSAC 作为稳健几何估计方法。这些负面结果表明，一种隐藏的人工偏好——操作员偏好的边距内缩——从根本上不存在于新书的像素中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1912.05909">MAGSAC ++, a fast, reliable and accurate robust estimator</a></li>
<li><a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Barath_MAGSAC_a_Fast_Reliable_and_Accurate_Robust_Estimator_CVPR_2020_paper.pdf">MAGSAC ++, a Fast, Reliable and Accurate Robust Estimator</a></li>

</ul>
</details>

**标签**: `#Machine Learning`, `#Computer Vision`, `#Book Digitization`, `#Negative Results`, `#Dataset`

---

<a id="item-8"></a>
## [ImageBench：开放文本到图像基准，含 52 个模型和 9 千张图片](https://www.reddit.com/r/MachineLearning/comments/1vz9x9c/a_dataset_with_52_text_to_image_model_evaluation_p/) ⭐️ 8.0/10

作者发布了 ImageBench V1，这是一个包含 192 个精心设计的困难提示词、并覆盖 52 个模型结果的文生图基准。该数据集包含超过 9,000 张生成并分析过的图像，同时在 Hugging Face 和 GitHub 上公开了完整方法、提示词和评分代码。 该基准通过公开实际生成的图像而不仅仅是汇总分数，填补了文生图评估中的一个关键空白。它为在文本渲染、空间推理和否定指令等困难场景下比较模型性能，提供了一个可复用且透明的资源。 该基准使用固定的 192 个提示词，旨在从文本渲染、空间推理、人物真实感、否定指令等类别对文生图模型进行压力测试。由视觉语言模型（VLM）根据带真值的二值问题对每个输出进行评判，但作者也指出 VLM 评判并非完美。

reddit · r/MachineLearning · /u/dh7net · 8月26日 21:10

**背景**: 文生图基准通常使用汇总指标或人工偏好分数对模型排序，但许多公开排行榜并不发布评估过程中实际生成的图像。公开图像可以让研究人员检查失败模式并验证评分行为。VLM 越来越多地被用作自动化评判器以扩展评估规模，但其判断可能存在噪声或偏差。该基准旨在将可复现性与透明的输出共享结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://imagebench.ai/">ImageBench — AI image model benchmark</a></li>
<li><a href="https://imagebench.ai/methodology-v1">Benchmark V1 Methodology</a></li>
<li><a href="https://huggingface.co/spaces/ArtificialAnalysis/Text-to-Image-Leaderboard">Image Arena Leaderboard - a Hugging Face Space by ArtificialAnalysis</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#text-to-image`, `#evaluation`, `#dataset`, `#machine-learning`

---

<a id="item-9"></a>
## [X 向开源项目 Nitter 发停止函，主站下线并暂停开发](https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/) ⭐️ 8.0/10

2026 年 8 月 24 日，X 公司向开源项目 Nitter 及其多个实例发出停止函，指控其非法抓取数据、绕过 API 并违反美国法律。Nitter 主站已下线，作者 Zedeus 暂停开发并寻求法律意见。 这一法律行动针对的是一个被广泛使用的隐私工具，可能为打击客户端抓取和开源前端树立先例。它影响了众多依赖 Nitter 无广告、免登录浏览 X 内容的用户，也引发了对类似开源项目未来的担忧。 X 要求 Nitter 所有实例永久关闭并在 8 月 25 日 17 时前删除代码库。Nitter 此前利用内部 API 提供无 JavaScript、无广告的轻量前端，且在 2024 年曾因 API 限制被 X 封杀。

telegram · zaihuapd · 8月26日 06:30

**背景**: Nitter 是一个免费开源、注重隐私和性能的 Twitter（现为 X）替代前端。它充当代理，在服务器端请求数据，并以无跟踪、无广告、无需登录的形式提供页面。停止函是一种正式要求停止涉嫌非法活动的法律文书，通常可能预示着后续诉讼。抓取网页和未经授权使用 API 在平台政策变化后常常处于法律灰色地带。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://github.com/zedeus/nitter">GitHub - zedeus/nitter: Alternative Twitter front-end · GitHub</a></li>
<li><a href="https://nlnet.nl/project/Nitter/">NLnet; Nitter</a></li>

</ul>
</details>

**标签**: `#open source`, `#legal`, `#web scraping`, `#privacy`, `#twitter`

---

<a id="item-10"></a>
## [智谱确认 Ox Alpha 为 GLM 新迭代，使用量超 DeepSeek 两倍](https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek?srnd=phx-technology) ⭐️ 8.0/10

中国 AI 公司智谱（Z.ai）确认，近日神秘上线的 Ox Alpha 模型是其 GLM 系列的最新迭代。该模型已登上 OpenRouter 使用量榜首，使用量是 DeepSeek 的两倍以上。 这标志着中国主要 AI 实验室之一对同为中国的 DeepSeek 发起了有力的竞争，后者模型已在全球广泛采用。也表明智谱正在开放模型路由平台上积极推出新的 GLM 版本。 Ox Alpha 目前处于免费预览阶段，预计持续约一周，具体定价尚未公布。它是智谱开发的 GLM 系列开放权重大型语言模型的最新迭代。

telegram · zaihuapd · 8月26日 09:33

**背景**: GLM（General Language Model）是由中国软件公司智谱（Z.ai）开发的一系列开放权重大型语言模型。首个 GLM 模型于 2021 年发布，后于 2023 年 3 月以 ChatGLM 聊天机器人的形式推出。OpenRouter 是一个提供统一 API 访问 400 多个模型的平台，涵盖 OpenAI、Anthropic 等供应商的模型以及这些中国模型。DeepSeek 是另一家知名的中国 AI 实验室，其模型与智谱的产品直接竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://z.ai/blog/glm-4.5">GLM-4.5: Reasoning, Coding, and Agentic Abililties</a></li>

</ul>
</details>

**标签**: `#AI`, `#GLM`, `#Zhipu`, `#DeepSeek`, `#LLM`

---

<a id="item-11"></a>
## [腾讯开源多模态嵌入模型 WeMM-Embedding，多项基准领先](https://github.com/Tencent/WeMM-Embedding) ⭐️ 8.0/10

腾讯微信视觉团队开源了 WeMM-Embedding 多模态嵌入模型系列，提供 2B、4B、9B 三种规格，统一支持文本、图像、视频、视觉文档及混合多模态输入。模型在多项基准上达到 SOTA 水平，并采用 Apache 2.0 协议发布，但不支持音频输入。 此次发布为开发者与研究人员提供了一个采用宽松许可证的开源多模态嵌入模型系列，可用于跨文本、图像、视频和类似 PDF 文档的检索增强生成、多模态搜索及文档理解。它增强了多模态模型的开源生态，并为专有嵌入 API 提供了有竞争力的替代方案。 该模型系列基于原生多模态的 Qwen3.5 骨干构建，统一支持文本、图像、视频、视觉文档及混合输入的表示与检索。2B、4B、9B 三种规格为不同部署场景提供了可扩展性，项目采用 Apache 2.0 协议开源。

telegram · zaihuapd · 8月26日 13:15

**背景**: 多模态学习是一种整合并处理文本、图像、音频、视频等多种数据类型（模态）的深度学习方法。嵌入模型将数据转换为稠密向量表示，从而实现相似度搜索与检索。视觉文档检索是搜索相关图像型文档（如 PDF）的特定任务，对多模态检索增强生成（RAG）系统很重要。WeMM-Embedding 将这些模态统一到一个嵌入空间中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent/WeMM-Embedding">GitHub - Tencent/ WeMM - Embedding : WeMM - Embedding is a family...</a></li>
<li><a href="https://arxiv.org/html/2608.24053v1">WeMM - Embedding : WeChat Multi-Modal Embedding Technical Report</a></li>
<li><a href="https://huggingface.co/tasks/visual-document-retrieval">What is Visual Document Retrieval? - Hugging Face</a></li>

</ul>
</details>

**标签**: `#multimodal-embedding`, `#open-source`, `#tencent`, `#retrieval`, `#AI`

---