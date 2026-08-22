---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> 从 26 条内容中筛选出 5 条重要资讯。

---

1. [SGLang v0.5.18 发布，包含 710 个 PR 并新增多模型支持](#item-1) ⭐️ 8.0/10
2. [Munder Difflin：本地多智能体工具，以确定性方式运行“克隆办公室”模拟](#item-2) ⭐️ 8.0/10
3. [开发者构建亚 2 比特量化 LLM，60MB 模型在 CPU 上每秒处理 400 个 token](#item-3) ⭐️ 8.0/10
4. [特斯拉宣布监督版 FSD 在中国可用](#item-4) ⭐️ 8.0/10
5. [亚马逊被曝购书扫描后销毁用于 AI 训练](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.18 发布，包含 710 个 PR 并新增多模型支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.18) ⭐️ 8.0/10

SGLang v0.5.18 已发布，包含来自 212 位贡献者的 710 个拉取请求。该版本新增了对 Muse Glimmer、Intern-S2-Mobius、SANA-Video、LTX-2.5 等多个模型的支持，并引入了重叠检查点暂存、TP LMHead All-to-All 等性能优化。 SGLang 是广泛采用的 LLM 推理引擎，此次发布将支持范围扩展到扩散模型和多模态模型，而不仅仅是自回归语言模型。例如 Qwen3-32B 在 H100 上启动速度提升 2.38 倍，这些可衡量的性能提升直接惠及生产部署和更广泛的开源推理生态。 该版本将核心依赖升级至 torch 2.13.0、triton 3.7.1、flashinfer 0.6.17 和 sgl-kernel 0.4.6.post1。一个显著的破坏性变更将所有编译内核缓存统一到 SGLANG_CACHE_DIR 下，升级后需要一次性重新编译。

github · Fridge003 · 8月22日 00:09

**背景**: SGLang 是一个开源的推理框架，最初用于高效服务大语言模型，如今也扩展支持扩散模型。该版本的 cookbook 配方为新增支持的模型提供了部署指南，使用户更容易在自有硬件上运行各种生成模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model">Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device | Meta AI Research</a></li>
<li><a href="https://huggingface.co/Efficient-Large-Model/SANA-Video_2B_480p">Efficient-Large-Model/SANA-Video_2B_480p · Hugging Face</a></li>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX's Latest AI Open-Source Foundation Model | LTX</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#SGLang`, `#release`, `#model support`, `#open source`

---

<a id="item-2"></a>
## [Munder Difflin：本地多智能体工具，以确定性方式运行“克隆办公室”模拟](https://munderdiffl.in/) ⭐️ 8.0/10

Munder Difflin 是一个本地多智能体工具，可封装 Claude Code、Codex 等现有编码智能体，以确定性方式运行“克隆办公室”模拟。其作者 Chaitanya 表示上线一周已有超过 2 万用户，且多数用户反映 token 消耗有所下降。 它直击 AI 辅助开发中的两大痛点：多智能体协同与 token 成本。通过让开发者在本地模拟一个由克隆智能体组成的“办公室”，多智能体工作流变得更易用、更可测试。 该工具称可封装“几乎所有”编码智能体，并在用户已有的 Claude Code、Codex 订阅之上运行确定性、不消耗 token 的模拟。早期用户反馈对设计提出质疑，一位评论者认为它更像是流水线和角色，而非真正的智能体。

hackernews · simonpure · 8月22日 09:49 · [社区讨论](https://news.ycombinator.com/item?id=49398152)

**背景**: Agent harness（智能体外壳）是围绕大语言模型的软件基础设施，负责管理工具调用、记忆、状态、执行环境和反馈循环，把语言模型变成能执行任务的智能体。Claude Code、Codex 等编码智能体通过子智能体编排、上下文压缩和 CLI 交互来逐步完成任务。这里的“确定性模拟”指的是可重复、脚本化的工作流，而不是每一步都依赖实时模型推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/concepts/harness">Agent Harness | Microsoft Learn</a></li>
<li><a href="https://israynotarray.com/en/ai/2026/07/14/why-more-ai-agents-lag-your-computer/">AI Runs in the Cloud — So Why Does Opening More Agents Lag Your...</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体热情，且很吃“办公室”主题的梗，作者本人也出现在帖中回答问题并分享了 2 万用户里程碑。一位长篇评论认可其概念，但批评智能体抽象方式，认为这更像是流水线和角色而非独立智能体；另一位网友则把使用体验比作管理 Michael 和 Dwight。

**标签**: `#multi-agent`, `#LLM`, `#coding agents`, `#harness`, `#simulation`

---

<a id="item-3"></a>
## [开发者构建亚 2 比特量化 LLM，60MB 模型在 CPU 上每秒处理 400 个 token](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 8.0/10

一位开发者从零开始用 30B 个 FineWeb token 训练了一个 250M 参数的 LLM，并将其量化到每个权重低于 2 比特，得到一个 60MB 的部署模型，在没有 GPU 的笔记本电脑 CPU 上每秒可处理约 400 个 token。该模型还使用了 512 位固定码词表（131k 个 token 占用 8.4MB，零训练参数），以及一个基于磁盘的长上下文缓存，将较早的 token 压缩到 1 比特。 这表明高度压缩的 LLM 可以在边缘设备和个人使用中以极小的内存和磁盘占用进行训练和部署，推动了高效推理的边界。它还挑战了长上下文处理需要大量 RAM 或专用硬件的假设，因为磁盘缓存支持从多达 1 亿个 token 的历史记录中进行检索。 该模型在保留的教育网页文本上的交叉熵为每 token 3.15 nats（困惑度 23.3，每字节 0.99 比特）。最近的 2048 个 token 以 fp16 正常 KV 缓存形式保留，而较旧的 token 被压缩为 1 比特并写入磁盘，每个 token 约 320 字节；作者指出模型仅被训练为从磁盘缓存中检索和回答，而非进行推理。固定码词表在 WordSim-353 上的 Spearman 相关为 0.619，随机码为 0.029。

reddit · r/MachineLearning · /u/Final-Data-1410 · 8月22日 04:39

**背景**: 量化将模型权重降低到低比特表示（例如 8 位、4 位，或本例中的亚 2 位）以减小内存并加速推理。FineWeb 数据集是 Hugging Face 发布的 15 万亿 token 级网络文本语料库，常用于 LLM 预训练研究。KV 缓存会在自回归生成期间存储中间键和值矩阵以避免重复计算；此处将其部分卸载到磁盘以处理长上下文。该模型使用每个 token 固定 512 位码而非学习得到的嵌入表，从而减少存储并使磁盘缓存能够高效引用 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/AI-Efficiency/Awesome-Model-Quantization">GitHub - AI-Efficiency/Awesome-Model- Quantization : A list of papers...</a></li>
<li><a href="https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1">FineWeb: decanting the web for the finest text data at scale ...</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**标签**: `#LLM`, `#quantization`, `#efficient-inference`, `#on-device`, `#training`

---

<a id="item-4"></a>
## [特斯拉宣布监督版 FSD 在中国可用](https://t.me/zaihuapd/43321) ⭐️ 8.0/10

特斯拉在社交媒体平台 X 上宣布，其监督版全自动驾驶（FSD）系统现在可以在中国使用。这标志着该功能正式进入中国市场。 这对中国自动驾驶领域而言是一个重要的监管和市场里程碑，因为特斯拉的 FSD 进入了全球最大的汽车市场之一。它可能加剧本土自动驾驶开发商的竞争，并影响未来的监管政策。 该公告内容简短，未透露具体价格、适配车型或推出时间表。FSD（监督版）仍然是 L2 级驾驶辅助系统，要求驾驶员始终保持专注。

telegram · zaihuapd · 8月22日 01:56

**背景**: 特斯拉的“全自动驾驶（监督版）”是一种高级驾驶辅助系统，可在驾驶员主动监督下完成路线导航、转向、变道和停车等操作。根据 SAE 标准，它属于 L2 级自动化，意味着驾驶员必须保持参与并随时准备接管车辆。特斯拉已将其品牌定位从“完全自动驾驶”调整为“监督版”，以反映系统的实际能力以及驾驶员监督的必要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tesla.com/fsd">Full Self-Driving (Supervised) - Tesla</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot">Tesla Autopilot - Wikipedia</a></li>
<li><a href="https://opentools.ai/news/teslas-bold-dreams-of-full-autonomy-shift-to-supervised-reality">Tesla 's Bold Dreams of Full Autonomy Shift to Supervised Reality</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#FSD`, `#autonomous-driving`, `#China`, `#regulation`

---

<a id="item-5"></a>
## [亚马逊被曝购书扫描后销毁用于 AI 训练](https://t.me/zaihuapd/43331) ⭐️ 8.0/10

404 Media 的调查显示，亚马逊正大规模购买纸质书、扫描用于 AI 训练，随后销毁实体书。调查人员在书中放入追踪装置，最终定位到拉斯维加斯的亚马逊仓库；据称员工为加快扫描会剪掉装订，书页随后被处理掉。 这一做法引发严重的版权与伦理问题，与之前 Anthropic 被曝出的行为相似，凸显了 AI 公司为获取训练数据愿意采取的程度。这可能促使公众进一步审视科技巨头如何获取和处理受版权保护的材料，对作者、出版商及整个 AI/ML 社区产生深远影响。 据报道，拉斯维加斯仓库的员工会接收大量印刷书籍，剪掉装订以加快扫描速度，随后处理掉书页。调查人员在一本稀有书中暗藏追踪装置，从而确认该书进入了亚马逊仓库。

telegram · zaihuapd · 8月22日 15:40

**背景**: 此前已有报道称 Anthropic 在 AI 训练中使用受版权保护的图书。训练大型语言模型通常需要海量文本数据，一些公司因此通过扫描实体书来获取数字化文本。此次报道中提到的销毁原书行为，给 AI 时代关于合理使用、盗版和知识产权的既有争论增添了新维度。

**标签**: `#AI training`, `#copyright`, `#Amazon`, `#books`, `#ethics`

---