---
layout: default
title: "Horizon Summary: 2026-09-07 (EN)"
date: 2026-09-07
lang: en
---

> From 31 items, 6 important content pieces were selected

---

1. [OpenAI Reveals RSI Progress and Coding Agents' Rising Role in Research](#item-1) ⭐️ 9.0/10
2. [LG Smart TVs Caught Logging Audio and Scanning Network While Off](#item-2) ⭐️ 8.0/10
3. [Google's InferenceX Externalization Accelerates TPU Adoption, Pressures CUDA Moat](#item-3) ⭐️ 8.0/10
4. [LLM-guided program evolution improves 10 Packomania circle-packing solutions](#item-4) ⭐️ 8.0/10
5. [Measuring LLM performance drift via 31,352 repeated benchmark runs](#item-5) ⭐️ 8.0/10
6. [Huawei Debuts Kirin 9050 Pro, a New High-Performance Chip After Six Years](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Reveals RSI Progress and Coding Agents' Rising Role in Research](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 9.0/10

OpenAI shared a new report, 'Research acceleration: The view inside OpenAI,' detailing how recursive self-improvement (RSI) is progressing and how coding agents have transformed internal research workflows. The report includes a chart showing median daily AI spend per researcher jumping from roughly $150 to about $600 between late July and August 2026. This matters because RSI has long been a theoretical milestone on the path to AGI, and OpenAI now presents it as a concrete internal focus. It also demonstrates that coding agents have become indispensable in high-level AI research, signaling a broader shift toward agentic engineering across the industry. OpenAI did not expand the RSI acronym in the post, suggesting it now treats the concept as familiar internal vocabulary. The author speculates the steep spend increase in late July may coincide with internal access to the model later released as GPT-6 Astra.

rss · Simon Willison · Sep 6, 23:57

**Background**: Recursive self-improvement (RSI) describes an AI system that can improve its own capabilities in a compounding cycle, potentially leading to an intelligence explosion beyond human-level performance. Coding agents are AI assistants that help engineers write, review, and debug code by handling well-defined tasks. Agentic engineering, a term coined by OpenAI cofounder Andrej Karpathy, refers to developing software with substantial assistance from these coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is Agentic Engineering? | IBM</a></li>
<li><a href="https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/">What is agentic engineering? - Agentic Engineering Patterns - Simon Willison's Weblog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#OpenAI`, `#RSI`, `#coding agents`, `#research`

---

<a id="item-2"></a>
## [LG Smart TVs Caught Logging Audio and Scanning Network While Off](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

A report and video titled "216M Spy TVs – The LG Smart TV Problem" show that LG Smart TVs log audio and probe local network devices even while the screen is off. The investigation highlights the TVs' background data collection as a privacy and security concern. With potentially hundreds of millions of LG smart TVs in homes, this covert behavior could turn living-room hardware into a surveillance device that maps private networks and captures private conversations. It also raises serious legal questions about wiretapping and consent, since visitors in a home are unlikely to have agreed to LG's terms. According to the report, the TV performed audio logging while in standby with the screen off, and used UPnP-style discovery messages to enumerate devices on the local network. LG's terms of service reportedly place the burden on the owner to notify household members and guests that their voices may be captured and processed.

hackernews · treve · Sep 7, 00:22 · [Discussion](https://news.ycombinator.com/item?id=49592375)

**Background**: Two technologies help explain the findings. Automatic Content Recognition (ACR) is used in smart TVs to generate signatures of on-screen content, supporting viewership tracking and targeted advertising; it can also process audio. UPnP (Universal Plug and Play) is a networking standard that lets devices on a local network discover each other automatically by sending search and advertisement messages, so a TV probing UPnP can learn which PCs, phones, and smart-home devices are present.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_content_recognition">Automatic content recognition - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_Plug_and_Play">Universal Plug and Play - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community reaction was largely angry and vindicated. Commenters noted that LG's contract terms require owners to tell guests their voices may be captured, and one pointed to possible all-party wiretap law violations; others said they had deliberately disabled network functions on their LG TVs or even unplugged internal Wi-Fi/BT chips, questioning why LG keeps pushing such behavior.

**Tags**: `#privacy`, `#security`, `#smart-tv`, `#surveillance`, `#consumer-tech`

---

<a id="item-3"></a>
## [Google's InferenceX Externalization Accelerates TPU Adoption, Pressures CUDA Moat](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

SemiAnalysis reports that Google's InferenceX initiative is rapidly externalizing its TPU stack, claiming up to 50% better performance per dollar and a growing customer base. The report highlights Ironwood and TPUv8i as key hardware in this push to make TPUs a stronger option for external AI inference. Google's aggressive externalization of its TPU inference stack threatens NVIDIA's CUDA ecosystem dominance by offering comparable or better economics for inference workloads. This could reshape the AI hardware market, giving cloud customers a credible alternative beyond CUDA-based GPUs. The report specifically mentions up to 50% better performance per dollar, with Ironwood and TPUv8i as key hardware. SemiAnalysis also operates an open-source benchmark called InferenceX that measures agentic and fixed-sequence inference across accelerators and serving stacks.

rss · Semianalysis · Sep 7, 20:00

**Background**: TPUs are Google's custom ASICs designed for neural network workloads, and the TPUv8i is a cost-efficient inference chip split from the TPUv8t training chip. The "CUDA moat" refers to NVIDIA's deep software ecosystem and accumulated developer expertise, which make it difficult for customers to switch to alternative hardware. By externalizing its TPU software stack, Google aims to reduce this lock-in and demonstrate that TPUs can serve external inference workloads, not just internal products.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.servethehome.com/googles-tpuv8s-for-training-and-inference-at-hot-chips-2026/">Google's TPUv8s for Training and Inference at Hot Chips 2026 - ServeTheHome</a></li>
<li><a href="https://wccftech.com/google-splits-tpuv8-strategy-two-chips-broadcom-training-mediatek-inference-duties/">Google Splits TPUv8 Strategy Into Two Chips, Handing Broadcom Training and MediaTek Inference Duties</a></li>

</ul>
</details>

**Tags**: `#TPU`, `#AI inference`, `#Google Cloud`, `#CUDA moat`, `#hardware`

---

<a id="item-4"></a>
## [LLM-guided program evolution improves 10 Packomania circle-packing solutions](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

An independent researcher used an LLM to iteratively evolve an optimization program for the Packomania csqv benchmark. In 15 iterations it improved the best-known sum-of-radii for 10 values of N between 101 and 114 by 2.4% to 5.4%, at a total LLM cost of $27.72. It demonstrates that LLM-guided program evolution can surpass longstanding human and expert records on a difficult mathematical benchmark at negligible cost. This points to a scalable, low-cost strategy for automated algorithm discovery in optimization and related fields. The system starts from a simple seed solver and proposes algorithmic changes guided by a scoreboard of results and a history of prior attempts; every candidate is checked by an independent verifier so only real improvements are kept. Paper: arxiv.org/abs/2609.05093, code: github.com/ucsandman/discovery-loop, and Packomania independently accepted the improved results.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Circle packing asks how to place N circles inside a container—here the unit square—without overlaps, while maximizing an objective such as the sum of radii, which is the Packomania csqv variant. These problems are nonconvex, have many local optima, and quickly become extremely difficult as N grows. LLM-guided program evolution treats the solver program itself as the subject of optimization: an LLM proposes source-code mutations, each candidate is executed and scored, and successful mutations accumulate. This approach is similar in spirit to earlier systems such as AlphaEvolve.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.05093">LLM - Guided Program Evolution for Circle Packing:Breaking 10...</a></li>
<li><a href="https://packomania.com/csqv/csqv.html">The best known packings of unequal circles in a square</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program evolution`, `#optimization`, `#circle packing`, `#AI-guided search`

---

<a id="item-5"></a>
## [Measuring LLM performance drift via 31,352 repeated benchmark runs](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/) ⭐️ 8.0/10

The author quantifies LLM performance drift using 31,352 repeated score observations across 49 models, finding within-day standard deviation of 2.80 points versus 8.43 points between daily medians. They propose treating benchmarking as a longitudinal measurement problem and released a public methodology paper that withholds the exact live task bank to limit contamination. This addresses a significant and often ignored issue: API-served models can change behavior without public version transitions, making single-point leaderboard scores misleading. Longitudinal measurement and drift detection could help practitioners make more informed model choices and distinguish genuine capability changes from infrastructure or availability effects. The analysis reported a roughly 3:1 ratio between between-day and within-day variation, but the author cautions that confounders such as task composition, sampling, missingness, and provider behavior could explain it. Their methodology uses versioned benchmark configurations, execution-based evaluation, availability-failure separation, and change-point detection on time series.

reddit · r/MachineLearning · /u/ionutvi · Sep 7, 07:44

**Background**: LLM model drift is the gradual, often unnoticed degradation or shift in model performance as data, user behavior, or context changes, and with API-served models the underlying system can change even without a new version announcement. Longitudinal research studies subjects repeatedly over time to suppress noise and reveal systematic differences, which is more appropriate than one-time snapshot benchmarks for detecting drift. Repeated-run variability in LLM evaluation is also an active research area because models can produce different answers on identical inputs, so reliability assessments must account for run-to-run variance.

<details><summary>References</summary>
<ul>
<li><a href="https://byaiteam.com/blog/2025/12/30/llm-model-drift-detect-prevent-and-mitigate-failures/">LLM Model Drift: Detect, Prevent, and Mitigate Failures – By ...</a></li>
<li><a href="https://arxiv.org/html/2509.24086v1">Do Repetitions Matter? Strengthening Reliability in LLM ...</a></li>
<li><a href="https://www.fiddler.ai/blog/how-to-monitor-llmops-performance-with-drift">How to Monitor LLMOps Performance with Drift Monitoring</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmarking`, `#performance drift`, `#evaluation`, `#ML`

---

<a id="item-6"></a>
## [Huawei Debuts Kirin 9050 Pro, a New High-Performance Chip After Six Years](https://www.news.cn/20260907/adf46c5c003240d28cc3cf6de54f9b5f/c.html) ⭐️ 8.0/10

On September 7, 2026, Huawei unveiled the Mate XT 2 tri-fold smartphone in Guangzhou, powered by the Kirin 9050 Pro chip. This is Huawei's first new flagship chip in six years since the Mate 40 global launch, and the first high-performance chip to adopt logic folding technology. The release signals that Huawei is again advancing its smartphone processor roadmap after a long gap, underscoring its in-house chip design capability. Logic folding also offers a different technical route from conventional 3D stacking and traditional transistor scaling, making it relevant beyond Huawei's own products. The Kirin 9050 Pro is designed by HiSilicon and reportedly fabricated by SMIC using its N+3P process, making it the world's first consumer chip to implement the Tau (τ) law. Inside the chip, logic cells are arranged in vertical layers, with vertical interconnect channels described as 'elevators' that shorten signal paths and reduce latency.

telegram · zaihuapd · Sep 7, 08:20

**Background**: For decades, chip performance gains relied primarily on shrinking transistor geometry under Moore's Law. As that scaling slows, the industry has increasingly turned to 3D stacking, which stacks multiple complete chips vertically. In May 2026, Huawei presented logic folding and the Tau (τ) law at ISCAS 2026 as an approach within 3D IC and advanced packaging, aiming to achieve improvements through 'time minification' rather than purely geometric shrinkage. Logic folding is described as a distinct concept from conventional 3D stacking.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/逻辑折叠技术/67870423">逻辑折叠技术 - 百度百科</a></li>
<li><a href="https://www.eet-china.com/news/202609076952.html">华为时隔六年旗舰发布会详解麒麟芯片，麒麟9050 Pro首发“韬定律”技术</a></li>
<li><a href="https://xueqiu.com/7227104507/408385272">华为麒麟9050 Pro芯片技术解析：架构、能效与竞品对比 本文基于公开评...</a></li>

</ul>
</details>

**Tags**: `#华为`, `#芯片`, `#半导体`, `#麒麟`, `#智能手机`

---