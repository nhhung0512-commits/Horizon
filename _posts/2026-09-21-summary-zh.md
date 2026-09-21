---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
---

> 从 35 条内容中筛选出 5 条重要资讯。

---

1. [苹果发布 2 纳米 M6 与四芯粒架构 M5 Ultra 芯片](#item-1) ⭐️ 9.0/10
2. [NASA 火星采样返回任务实际上已被取消](#item-2) ⭐️ 8.0/10
3. [Bryan Cantrill 复盘 Sun Microsystems 的战略失误](#item-3) ⭐️ 8.0/10
4. [Cloudflare Python Workers 结束两年预览，正式全面可用](#item-4) ⭐️ 8.0/10
5. [SemiAnalysis 解析 MoE 推理中的计算与数据流动](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [苹果发布 2 纳米 M6 与四芯粒架构 M5 Ultra 芯片](https://t.me/zaihuapd/43965) ⭐️ 9.0/10

苹果发布了两款全新 Apple Silicon 芯片：首款采用 2 纳米制程的 M6，首发于新款 Mac mini，配备 12 核 CPU、12 核 GPU、双 16 核神经网络引擎，统一内存带宽最高 170GB/s；以及首发于新款 Mac Studio 的 M5 Ultra，这是 M 系列首个四芯粒（four-die）架构芯片，最高 36 核 CPU、80 核 GPU、512GB 内存，统一内存带宽达 1.2TB/s。 M6 让苹果成为首批将 2 纳米制程用于消费级芯片的厂商之一，这意味着整个 Mac 产品线有望获得显著更高的每瓦性能与更充裕的晶体管预算；而四芯粒的 M5 Ultra 则把 Apple Silicon 推向工作站级别，其内存容量与带宽以往只出现在高端 GPU 和服务器芯片上，明显是冲着本地 AI 与重型创意工作负载而来。 据报道，M5 Ultra 的四颗芯粒通过超低延迟互连通信，芯粒间总带宽超过 4.4TB/s，并对外表现为一颗统一处理器；其 1.2TB/s 的内存带宽比 M3 Ultra 高出 50%。此外，与所有现代制程命名一样，“2 纳米”只是营销标签，并不对应任何实际物理特征尺寸。

telegram · zaihuapd · 9月21日 16:32

**背景**: Apple Silicon 的 M 系列芯片属于系统级芯片（SoC）设计，将 CPU、GPU 与统一内存集成在同一封装内；神经网络引擎是苹果自研的 AI 加速单元，最早随 2017 年的 A11 Bionic 亮相，如今已是 iPhone 与 Mac 芯片的标准模块。3 纳米、2 纳米等制程节点代表半导体制造的连续世代，节点越小通常意味着晶体管密度更高、开关速度更快、功耗更低。苹果产品线中的 “Ultra” 芯片由两颗 Max 芯粒拼接而成，四芯粒设计相当于在此基础上再翻一倍，依赖先进封装——这与 AMD、英特尔用 chiplet 方案突破单块硅片光罩极限的思路一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcmag.com/news/apple-m5-ultra-and-m6-silicon-explained">Forget Foldables: Apple's 2nm M6 and Quad-Die Monster Just Reset the AI Race | PCMag</a></li>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_Engine">Neural Engine - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#M6`, `#M5 Ultra`, `#2nm`, `#Apple Silicon`

---

<a id="item-2"></a>
## [NASA 火星采样返回任务实际上已被取消](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) ⭐️ 8.0/10

据《Science》报道，由 NASA 与欧洲空间局（ESA）联合推进的“火星采样返回”（MSR）计划实际上已被取消，该计划原本要把“毅力号”火星车在火星上采集并封存的样本带回地球。项目成本已膨胀到约 110 亿美元、样本返回时间推迟到 2040 年，如今已不是延期而是彻底终止。 MSR 一直被行星科学界视为未来十年的最高优先级目标，它的取消意味着人类首次从另一颗行星表面取回样本的往返任务被搁置，也给了中国的天问三号采样返回任务一个战略空档。同时，这也让外界对喷气推进实验室（JPL）的前途以及 NASA 能否在预算内完成旗舰级机器人任务产生疑问。 2022 年获批的 NASA–ESA 方案包含三个部分：作为采样器的“毅力号”、搭载火星上升器的样本取回着陆器，以及地球返回轨道器，最初目标是在 2033 年前后把样本带回，后来推迟到 2040 年代。社区中的批评者认为，JPL 是围绕 Ariane 64 等老旧运载火箭来设计架构的，而没有采用 Starship 或 New Glenn 这类更便宜、运力更强的商业方案。

hackernews · Muhammad523 · 9月21日 19:14 · [社区讨论](https://news.ycombinator.com/item?id=49791939)

**背景**: 火星采样返回任务的目标是把火星岩石和尘土带回地球，让地面实验室能用远超任何火星车搭载仪器的精度进行分析，核心是判断火星是否曾经存在生命。NASA 的“毅力号”火星车自 2021 年起就在杰泽罗陨石坑钻取并密封铅笔大小的钛合金样本管，把它们留在火星表面等待未来任务取回。从火星取回样本需要一条前所未有的步骤链——着陆、从另一颗行星上发射火箭、在火星轨道交会对接——正是这些环节导致成本与工期不断膨胀。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NASA-ESA_Mars_Sample_Return">NASA-ESA Mars Sample Return - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mars_sample-return_mission">Mars sample-return mission - Wikipedia</a></li>
<li><a href="https://www.globaltimes.cn/page/202609/1369763.shtml">Tianwen - 3 mission enters prototype phase, prioritizing... - Global Times</a></li>

</ul>
</details>

**社区讨论**: 评论者大多把矛头指向 JPL 的领导层，提到成本飙升至 110 亿美元、返回时间推迟到 2040 年，并将计划取回的 1.1 磅火星样本与阿波罗从月球带回的 842 磅岩石作对比，认为或许等待载人任务更为划算。一位曾参与 ExoMars“罗莎琳德·富兰克林”号火星车工作的评论者指出该任务已多次延期；其他人则强调中国计划于 2028 年发射的天问三号采样返回任务，并质疑为何要让“毅力号”为一项目标尚不明确的后续任务提前封存样本。

**标签**: `#space-exploration`, `#NASA`, `#Mars`, `#JPL`, `#space-policy`

---

<a id="item-3"></a>
## [Bryan Cantrill 复盘 Sun Microsystems 的战略失误](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

曾任职于 Sun Microsystems、以 DTrace 共同创造者身份闻名的系统工程师 Bryan Cantrill，在其 dtrace.org 博客上发表题为《What Sun got wrong》的文章，剖析导致 Sun 衰落的一系列战略与技术决策。该文在 Hacker News 上获得 469 分和约 260 条实质性评论，读者纷纷补充关于 Sun 销售文化、2002 年取消 Solaris on x86 以及错失 Google 交易的第一手经历。 Sun 的崩塌重塑了整个计算产业——它为 x86 与 Linux 主导服务器市场扫清了道路，终结了最后一批垂直整合的 Unix 硬件厂商之一，并为 2010 年 Oracle 收购 Solaris 与 SPARC 埋下伏笔。Cantrill 的分析被广泛引用为「仅有技术卓越不足以支撑一家企业」的经典案例，这对如今同样面临「锁定还是开放」抉择的 AI 硬件与基础设施厂商颇具借鉴意义。 讨论中补充了大量具体细节：有评论者指出 Sun 的销售流程强迫客户参加现场会议、反复修改报价，以至于一台 Alpha 服务器的导轨和电源线价格就可能超过一台次日送达的整机 Dell 服务器。还有人提到 Sun 在 2002 年短暂取消 Solaris on x86，损害了那些不愿被锁定在 SPARC 上的客户的信任；以及据称因 Sun 坚持要了解 Google 拥有多少台服务器而使 2002 年的 Google 交易告吹。

hackernews · chmaynard · 9月21日 14:03 · [社区讨论](https://news.ycombinator.com/item?id=49787436)

**背景**: Sun Microsystems 创造了 SPARC（可扩展处理器架构，一种 RISC 指令集架构）以及 Solaris 这一 Unix 操作系统，后者催生了 DTrace、ZFS 等颇具影响力的技术。Sun 于 2005 年将 Solaris 的大部分代码以 OpenSolaris 项目形式开源，但 Oracle 在 2010 年收购该公司后，操作系统被更名为 Oracle Solaris，OpenSolaris 发行版被终止，Oracle 又在 2017 年裁撤了大部分 Solaris 团队；OpenSolaris 则以 Illumos 分支的形式延续下来。Bryan Cantrill 是一位系统工程师，先后任职于 Sun 和 Joyent，以可观测性工具 DTrace 闻名，该工具至今仍广泛应用于类 Unix 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SPARC">SPARC - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Solaris_operating_system">Solaris operating system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Oracle_Solaris">Oracle Solaris - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上认同 Cantrill 的观点，并纷纷贡献自己的亲历故事：coreyh14444 描述了在 Sun 和 DEC 采购时被迫反复修改报价的痛苦体验，与 Dell 次日送达形成鲜明对比；cryptonector 则列举了 Sun 在 21 世纪初的一系列错误，包括 2002 年短暂取消 Solaris on x86 以及搞砸与 Google 的交易。jedberg 对 Cantrill 的论述框架提出反驳，认为 Sun 从来就没兴趣经营企业，只在意打造出色的技术；labrador 则把在 70 美元卖出 Sun 股票（随后跌至 7 美元）与如今特斯拉、SpaceX 和 AI 股票的超高估值相类比，引以为戒。

**标签**: `#Sun Microsystems`, `#Solaris`, `#SPARC`, `#tech history`, `#Bryan Cantrill`

---

<a id="item-4"></a>
## [Cloudflare Python Workers 结束两年预览，正式全面可用](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 8.0/10

Cloudflare 宣布 Python Workers 正式全面可用（GA），经过约两年的预览期后，Python 成为 Cloudflare 开发者平台上的一等公民和完全受支持的语言。其实现方式并非使用原生 CPython 解释器，而是通过 Pyodide 将 Python 编译为 WebAssembly，再运行在基于 V8 的 workerd 运行时中。 在 Cloudflare 平台上，边缘端的无服务器 Python 长期落后于 JavaScript 和 TypeScript，因此 GA 意味着 Python 开发者现在可以在 Workers 上构建生产级负载并获得官方支持。这也体现了 Cloudflare 对 Python 与 Pyodide 生态的更广泛投入——发布公告署名者中有两位是 Pyodide 的核心维护者。 这一基于 WebAssembly 的运行时存在官方记录的局限，最明显的是 multiprocessing 和 threading 在 WebAssembly 虚拟机中均无法工作。本地开发由 pywrangler 工具负责（在 PyPI 上以容易混淆的名字 workers-py 发布），它通过在 123MB 的 workerd 二进制内运行 V8、再于其中执行 WebAssembly 版 Pyodide 来完整模拟整套技术栈，在 macOS 上通常安装于 node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd。

rss · Simon Willison · 9月21日 22:25

**背景**: Cloudflare Workers 是一个在 Cloudflare 边缘网络上运行代码的无服务器平台，其运行时 workerd 是一个 JavaScript/WebAssembly 引擎，于 2022 年开源，Wrangler 也用它来做本地开发。Pyodide 项目将 CPython 以及众多科学计算类 Python 包编译为 WebAssembly，使它们能够在未提供原生 Python 解释器的环境中运行，最初面向浏览器场景。WebAssembly 是一种可移植的二进制指令格式，允许 JavaScript 之外的语言运行在 JavaScript 虚拟机中，这正是上述方案得以成立的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Workerd">Workerd</a></li>
<li><a href="https://flaviocopes.com/workerd/">How workerd , the Cloudflare Workers runtime, is built</a></li>
<li><a href="https://pyodide.org/en/stable/usage/downloading-and-deploying.html">Downloading and deploying Pyodide — Version 314.0.7</a></li>

</ul>
</details>

**标签**: `#Cloudflare Workers`, `#Python`, `#WebAssembly`, `#Pyodide`, `#Serverless`

---

<a id="item-5"></a>
## [SemiAnalysis 解析 MoE 推理中的计算与数据流动](https://newsletter.semianalysis.com/p/computation-and-data-movement-for) ⭐️ 8.0/10

SemiAnalysis 发布了一篇深度技术分析，探讨如何将混合专家（MoE）模型映射到推理硬件上，重点关注模型结构、数据流动以及高效服务。文章的核心观点是：稀疏专家模型的推理主要是一个数据搬运问题，而非单纯的计算问题。 MoE 已成为前沿大语言模型的主流架构，因为它把总参数量与每个 token 实际消耗的算力解耦，因此整个行业的成本、延迟和吞吐量越来越取决于这类模型能否被高效地服务。构建或采购推理技术栈的基础设施工程师与机器学习系统工程师，正需要这种硬件层面的分析来做出合理决策。 MoE 推理通常受限于显存带宽和互连能力，而不是峰值算力，因为专家权重需要在不同设备之间进行聚集与分发，而专家并行（expert parallelism）等技术还涉及大量 all-to-all 通信。实际部署中的难点包括：路由在专家之间的负载不均衡、每个专家分到的批次规模很小导致张量核心利用率不足，以及在把专家常驻高带宽显存与通过较慢链路搬运专家权重之间做权衡。

rss · Semianalysis · 9月21日 18:14

**背景**: 混合专家（MoE）是一种机器学习方法，它把模型拆分成多个“专家”子网络，每个专家专注于输入数据的一个子集，并由路由器为每个 token 只选择少数几个专家。由于任意一次输入只激活一部分参数，MoE 模型可以用少得多的算力完成预训练，并把总参数量扩展到极大的规模，同时让每个 token 的成本大致保持恒定。模型服务（model serving）则是把训练好的模型部署为可大规模、低延迟、高可用推理服务的基础设施实践。这篇文章正处在两者的交汇点上：探讨让 MoE 训练成本低廉的稀疏性，如何在真实推理硬件上转化为特定的计算模式与数据搬运模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://inferenceengineering.tech/learn/ai-inference-hardware/">AI Inference Hardware Guide</a></li>

</ul>
</details>

**标签**: `#Mixture-of-Experts`, `#Inference`, `#AI Hardware`, `#Model Serving`, `#Systems`

---