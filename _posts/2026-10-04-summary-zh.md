---
layout: default
title: "Horizon Summary: 2026-10-04 (ZH)"
date: 2026-10-04
lang: zh
---

> 从 25 条内容中筛选出 4 条重要资讯。

---

1. [Strata 声称可在单张 RTX 4090 上运行 125B 的 Qwen3.8-Flash-Next](#item-1) ⭐️ 8.0/10
2. [ARC-AGI-3 的 Kaggle 最高分在 30 天内从 7% 升至 56%](#item-2) ⭐️ 8.0/10
3. [SK 电信就大规模信息泄露致歉，为全体用户免费更换 USIM 卡](#item-3) ⭐️ 8.0/10
4. [Google 发布 VeriHarness 长程任务验证框架](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata 声称可在单张 RTX 4090 上运行 125B 的 Qwen3.8-Flash-Next](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

一个名为 Strata（Niko1221/Strata）的 GitHub 项目发布了 Windows 和 Linux 的一键安装包，让用户能在消费级硬件上运行 125B 参数的 Qwen3.8-Flash-Next 模型，并在本地提供兼容 OpenAI/Anthropic 的 API 接口。在 Hacker News 讨论中，用户 snehesht 报告在配备 128GB DDR5 和 Ryzen 7950X3D 的 RTX 4090 上达到了 124 tokens/秒，与项目宣称的约 100 tokens/s 相符。 如果这些性能声称属实，这将把 125B 级别的开源多模态模型带到准专业硬件上以可用的吞吐量运行，对 llama.cpp 等成熟推理栈构成挑战，并让大型模型的使用不再局限于数据中心级 GPU。然而，围绕极低位宽量化质量的争论意味着社区现在真正审视的是实际可用性，而不仅仅是原始速度。 Qwen3.8-Flash-Next 是一个 125B 参数的混合专家（MoE）模型，额外带有 51B 的 N-gram 嵌入，每个 token 仅激活约 6B 参数，这种配置使得即便模型总体量巨大，也能实现高吞吐量。关键警告来自评论者 Jackson__：他用 50 张图像的视觉基准测试发现，Strata 的误差距离中位数为 154.8 像素，而在 llama.cpp 上运行完全相同的 GGUF 和视觉适配器权重时中位数仅为 46.5 像素——这一巨大质量差距暗示了低于 4-bit 量化带来的取舍。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: 像 Qwen3.8-Flash-Next 这样的混合专家（MoE）模型包含大量参数，但每个 token 只激活其中一小部分，这正是 125B 模型能在有限硬件上快速运行的原因。量化通过降低权重数值精度（例如降到 4-bit 或更低）让大型模型能够塞进有限的显存，用一定的精度换取内存节省和速度提升。Strata 的方案结合 GPU 与系统内存来承载模型，而整个讨论反映出模型运行速度与强力压缩所导致的质量损失之间长期存在的矛盾。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Niko1221/Strata/releases">Releases · Niko1221/ Strata · GitHub</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/qwenlm/qwen3.8-flash-next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪出现分歧：一些用户报告了出色结果（snehesht 的 124 tok/s，AntiRush 在 RTX 6000 Pro 上解码达 255 tok/s），而另一些人则对低于 4-bit 的量化持怀疑态度。最有力的反驳是 Jackson__ 的独立视觉基准测试，显示在相同权重下 Strata 的误差约为 llama.cpp 的三倍；a11r 也指出 4-bit 量化对困难但范围明确的编码任务已经“足够好”，暗示低于 4-bit 可能不值得牺牲质量。

**标签**: `#local-llm`, `#inference-optimization`, `#quantization`, `#gpu`, `#llm-serving`

---

<a id="item-2"></a>
## [ARC-AGI-3 的 Kaggle 最高分在 30 天内从 7% 升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

据 r/MachineLearning 上的一篇帖子，过去 30 天内 Kaggle 上 ARC-AGI-3 的最高分从 7% 上升到 56%。据称，体积较小的本地模型在搭配评估 harness（测试框架）后，已经在得分上超过了普通人类的水平。 ARC-AGI 明确遵循“对人类容易、对 AI 困难”的设计原则，用来衡量通用智能的进展，而不依赖模型规模或记忆训练数据，因此得分迅速逼近并超越普通人类水平，是推理能力进步的一个有意义信号。这些提升来自小模型加上 harness 框架，而非前沿规模算力，说明智能体设计与评测工程的重要性可能不亚于模型本身的能力。 发帖人说明所附的排行榜图片已略微过时，并指出 Kaggle 比赛规则限制参赛者只能使用体量较小的本地模型，因此这一进步在很大程度上应归功于 harness/智能体框架，而非超大模型。ARC-AGI-3 被定位为面向智能体能力的基准，任务需要与环境持续交互，而不只是解答单道静态谜题。

reddit · r/MachineLearning · /u/we_are_mammals · 10月4日 10:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**背景**: ARC-AGI（抽象与推理语料库）由 François Chollet 提出，现由非营利组织 ARC Prize Foundation 运营；每道题只给出少量网格输入输出示例，解题者必须推断出背后的变换规则，而题目被刻意设计成无法直接从训练数据中记忆出规律。ARC-AGI-3 则把这一思路拓展到可交互的智能体环境。所谓“eval harness”（评测框架）是驱动模型跑基准测试的外围脚手架，负责提示构造、采样、工具调用与打分，因此同一个底层模型在不同 harness 下得分可能相差很大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>
<li><a href="https://arcprize.org/">ARC Prize Foundation is a nonprofit advancing open-source AGI ...</a></li>
<li><a href="https://github.com/EleutherAI/lm-evaluation-harness">GitHub - EleutherAI/lm-evaluation-harness: A framework for ...</a></li>

</ul>
</details>

**标签**: `#ARC-AGI`, `#Kaggle`, `#benchmark`, `#AI reasoning`, `#local models`

---

<a id="item-3"></a>
## [SK 电信就大规模信息泄露致歉，为全体用户免费更换 USIM 卡](https://t.me/zaihuapd/44206) ⭐️ 8.0/10

韩国最大电信运营商 SK 电信（SKT）确认其内部系统遭到黑客攻击，核心 HSS 服务器被攻破，泄露的敏感数据包括 IMEI、SN、ICCID、PIN2/PUK2、eID、加密 K 值和私钥等，受影响用户超过 2500 万人。SKT CEO 已公开致歉，并宣布为所有希望更换的 SKT 用户（含其网络下的 MVNO 用户，部分设备除外）免费更换 USIM 卡，同时为近期已付费更换的用户报销费用。 这是迄今披露的规模最大的电信数据泄露事件之一，而 SIM 认证密钥和私钥的外泄直击移动身份信任链的根基，理论上可能被用于大规模 SIM 卡克隆、账号接管和通信拦截攻击。此次事件影响约韩国一半人口，也将促使全球运营商加固核心网系统，并重新审视用户密钥的存储方式。 被攻破的 HSS 是 4G/5G 核心网中负责认证与业务配置的主用户数据库，而泄露的 ICCID 是按 ITU-T E.118 标准为每张 SIM 卡分配的全球唯一 19–20 位序列号。SKT 正加速推进 USIM 卡更换以强制启用新的认证凭证，但换卡无法追回已被窃取的数据，且部分设备（尤其某些 eSIM 或嵌入式模块）不在免费更换范围内。

telegram · zaihuapd · 10月4日 09:02

**背景**: 每个移动用户都依靠存储在 SIM 卡和运营商 HSS 中的同一把密钥（即 K 值）完成认证，SIM 卡与网络通过质询—应答握手来验证身份，密钥本身并不在网络上传输。ICCID 是印在卡片上的 SIM 卡唯一序列号，PIN2/PUK2 分别是二级 PIN 码与解锁码，eID 则是嵌入式身份标识。一旦攻击者拿到 K 值和相关标识符，理论上就能克隆 SIM 卡或冒充用户，因此运营商历来把 HSS 数据视为最高敏感级别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.p1sec.com/blog/home-subscriber-server-hss">Home Subscriber Server (HSS): The Backbone of Modern Telecom ...</a></li>
<li><a href="https://telnyx.com/resources/iccid-number">ICCID number: how to find, decode, and use it - Telnyx ICCID/SIM Card Number Checker/Decoder - phone.fyicenter.com ICCID decoder online — validate and break down any SIM number Free Sim Card Decoder - Decode ICCID & IMSI Online ICCID Lookup. Decode Any SIM Card Serial Number | Irreva ICCID Checker - IMEI.info How to Find Your SIM Card Number (ICCID) on Any Device</a></li>
<li><a href="https://en.wikipedia.org/wiki/SIM_card">SIM card - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#telecom`, `#privacy`, `#SK Telecom`

---

<a id="item-4"></a>
## [Google 发布 VeriHarness 长程任务验证框架](https://arxiv.org/abs/2610.00972v1) ⭐️ 8.0/10

Google 研究团队发布 VeriHarness，这是一个无需训练、即插即用的智能体验证框架，其核心思路是用生成候选结果的同一模型来执行验证：对存在分歧的主张核查环境证据，对已达成共识的主张主动发起挑战，然后据此选择、修订或重建最终结果。该框架在 5 个长程任务基准、2 个模型上取得最高选择分，经证据驱动修订后相较单次生成平均提升 Gemini 3.5 Flash 6.2 分、Claude Opus 4.8 6.4 分，并公开了约 2.6 万条 rollout 数据。 验证能力被普遍视为长程智能体的瓶颈——只要一步出错就可能让整条轨迹偏离，因此一个无需微调即可提升结果选择与修订的框架，可以直接套用到现有的前沿模型上。公开约 2.6 万条 rollout 也为社区提供了研究乃至训练验证器的数据资源，可能加速智能体推理与评测方向的进展。 一个值得注意的设计是用同一模型进行验证，即验证器不依赖更强的外部裁判模型，这让方法更廉价、更自洽。该框架无需训练且在不同基准和模型之间即插即用，其两种验证模式把主张分为有分歧的主张（对照环境证据核查）和已达成共识的主张（主动对抗性挑战）；报告中的增益是在选择结果与修订后的最终输出上测得的，而非原始单次生成。

telegram · zaihuapd · 10月4日 13:32

**背景**: 长程任务指需要智能体在较长轨迹上连续做出大量决策的多步骤任务，例如跨站点的网页操作流程或办公套件任务；而针对短流程、单站点任务的现有基准，前沿模型的表现已接近饱和。提升智能体输出的一种常见做法是 best-of-N 采样，即生成多个候选尝试（称为 rollout），再由验证器或裁判挑选最佳者。VeriHarness 正是瞄准这一选择环节，并额外加入修订能力，使较弱的候选结果可以被修复而不只是被丢弃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00972">VeriHarness : Scaling Agentic Verification for Long - Horizon Tasks</a></li>
<li><a href="https://github.com/google-research/veriharness">GitHub - google -research/ veriharness · GitHub</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#LLM verification`, `#long-horizon tasks`, `#agentic reasoning`, `#Google Research`

---