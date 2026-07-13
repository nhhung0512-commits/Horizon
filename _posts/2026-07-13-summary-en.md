---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 17 items, 4 important content pieces were selected

---

1. [Climate.gov Destroyed, Open Data Rescues It](#item-1) ⭐️ 8.0/10
2. [LAPD ends Flock contract over privacy concerns, but data access persists](#item-2) ⭐️ 8.0/10
3. [CoT is a scaling trap; latent reasoning next wave, but interpretability remains](#item-3) ⭐️ 8.0/10
4. [GPUHedge Cuts Serverless GPU Cold Start Latency from 117s to 30s](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Climate.gov Destroyed, Open Data Rescues It](https://werd.io/climate-gov-was-destroyed-open-data-saved-it/) ⭐️ 8.0/10

A blog post reports that climate.gov was destroyed, but open data initiatives and community efforts successfully preserved the underlying climate data. This incident underscores the critical role of open data in safeguarding publicly funded scientific information, especially when government systems fail or are disrupted. The preservation effort relied on donations and independent archiving, raising concerns about the long-term sustainability of relying on ad-hoc community efforts for essential data.

hackernews · benwerd · Jul 13, 19:57 · [Discussion](https://news.ycombinator.com/item?id=48897945)

**Background**: Open data refers to data that is freely accessible, reusable, and shareable by anyone for any purpose. Data preservation involves activities like backup, migration, and archiving to maintain data authenticity and availability over time. Climate.gov is a U.S. government website providing climate data and resources.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_data">Open data - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_preservation">Data preservation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether government data should be maintained by taxpayer-funded institutions rather than relying on donations. Some expressed distrust in government oversight and argued for independent data collection and analysis.

**Tags**: `#open data`, `#climate science`, `#government transparency`, `#data preservation`

---

<a id="item-2"></a>
## [LAPD ends Flock contract over privacy concerns, but data access persists](https://techcrunch.com/2026/07/13/lapd-lets-contract-with-surveillance-giant-flock-expire-citing-serious-concerns-over-civil-liberties-and-privacy/) ⭐️ 8.0/10

The Los Angeles Police Department has allowed its contract with surveillance company Flock Safety to expire, citing serious concerns over civil liberties and privacy. However, Flock continues to operate its cameras and may sell data to other agencies. This decision highlights growing tensions between law enforcement surveillance and civil rights, but the persistence of data sharing through Flock's network undermines the impact of such contract terminations. It raises critical questions about the effectiveness of local oversight when data can be accessed regionally or nationally. Flock owns the cameras and poles, so even after contract expiration, the cameras continue recording and Flock can sell the data to other agencies like CHP, LASD, FBI, or Palantir. The LAPD can still access the data through mutual aid agreements or by simply calling other departments.

hackernews · forks · Jul 13, 15:11 · [Discussion](https://news.ycombinator.com/item?id=48893947)

**Background**: Flock Safety is a surveillance technology company that provides automated license plate readers and camera systems to law enforcement and private entities. Their cameras are often installed on poles owned by Flock, and they offer network sharing features that allow agencies to share data across jurisdictions. Critics argue this creates a surveillance infrastructure that is difficult to dismantle or opt out of.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aclu.org/news/privacy-technology/flock-roundup">Flock’s Aggressive Expansions Go Far Beyond Simple Driver Surveillance | American Civil Liberties Union</a></li>
<li><a href="https://www.flocksafety.com/blog/statement-network-sharing-use-cases-federal-cooperation">Setting the Record Straight: Statement on Flock Network Sharing, Use Cases, and Federal Cooperation</a></li>
<li><a href="https://data.aclum.org/2025/10/07/flock-gives-law-enforcement-all-over-the-country-access-to-your-location/">Flock Gives Law Enforcement All Over the Country Access to Your Location – The Data for Justice Project | ACLU of Massachusetts</a></li>

</ul>
</details>

**Discussion**: Community comments express concern that Flock's business model is engineered to be resilient to political pressure, as the cameras continue operating and data persists. Users point out the irony of LAPD citing civil liberties in light of its history of civil rights violations. Some question the effectiveness of surveillance when repeat offenders are not prosecuted.

**Tags**: `#surveillance`, `#privacy`, `#civil liberties`, `#LAPD`, `#Flock`

---

<a id="item-3"></a>
## [CoT is a scaling trap; latent reasoning next wave, but interpretability remains](https://www.reddit.com/r/MachineLearning/comments/1uviru5/chain_of_thought_is_a_scaling_trap_the_next_wave/) ⭐️ 8.0/10

A Reddit post argues that Chain of Thought (CoT) reasoning is a scaling trap due to faithfulness and cost issues, and proposes that the next wave is latent reasoning approaches like Coconut, Hierarchical Reasoning Model (HRM), and RecursiveMAS. The post then raises the 'black box wall' problem, questioning how to maintain interpretability when reasoning moves into latent space. This analysis highlights a critical trade-off in LLM reasoning: language-based computation is interpretable but costly and potentially unfaithful, while latent-space computation is efficient but opaque. The discussion is highly relevant for researchers and practitioners designing next-generation reasoning systems, especially for high-stakes domains where auditability is mandatory. Coconut (Chain of Continuous Thought) feeds the last hidden state back as the next input embedding without decoding to tokens; HRM separates slow planning from fast execution; RecursiveMAS treats the multi-agent system as a unified latent-space recursive computation. BDH (Dragon Hatchling) achieves 97.4% accuracy on Sudoku Extreme without CoT or backtracking, and aims to combine latent iteration with stateful memory over time.

reddit · r/MachineLearning · /u/meowsterpieces · Jul 13, 17:50

**Background**: Chain of Thought (CoT) prompting improves LLM performance by having the model output intermediate reasoning steps in natural language. However, these steps may not faithfully reflect the model's actual computation, and they increase latency and cost because reasoning is serialized into tokens. Latent reasoning methods perform computation in the model's hidden state space, avoiding token serialization, but sacrifice the interpretability that CoT provides. The post discusses approaches like Coconut, HRM, and RecursiveMAS that move reasoning into latent space, and considers how to ensure auditability through outer-loop verification or native model analysis hooks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in a Continuous Latent Space</a></li>
<li><a href="https://arxiv.org/abs/2506.21734">[2506.21734] Hierarchical Reasoning Model</a></li>
<li><a href="https://arxiv.org/abs/2604.25917">[2604.25917] Recursive Multi - Agent Systems</a></li>

</ul>
</details>

**Tags**: `#LLM reasoning`, `#Chain of Thought`, `#latent reasoning`, `#scaling`, `#interpretability`

---

<a id="item-4"></a>
## [GPUHedge Cuts Serverless GPU Cold Start Latency from 117s to 30s](https://www.reddit.com/r/MachineLearning/comments/1uvlb6h/gpuhedge_hedging_serverless_gpu_providers/) ⭐️ 8.0/10

GPUHedge is a new open-source tool that uses speculative execution across multiple serverless GPU providers to hedge requests, reducing the p95 cold start latency from 116.6 seconds to 29.4 seconds in benchmark tests. Cold start latency is a major pain point for serverless GPU inference, often causing delays of over a minute. GPUHedge's approach offers a practical, provider-agnostic solution that can significantly improve user experience and reduce costs. GPUHedge starts a request on a primary provider, monitors the job's lifecycle, and conditionally launches a backup request on a secondary provider after a configurable delay; the first successful result is used and the losing job is cancelled via the provider's native API.

reddit · r/MachineLearning · /u/Putrid_Construction3 · Jul 13, 19:20

**Background**: Serverless GPU providers allow users to run AI models without managing infrastructure, but they suffer from cold start latency when the GPU must be initialized and the model loaded. Speculative execution, or hedging, is a technique where multiple redundant requests are sent to different providers, and the fastest response is used. This approach helps mitigate long-tail latency issues common in distributed systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_execution">Speculative execution - Wikipedia</a></li>
<li><a href="https://www.beam.cloud/blog/top-serverless-gpu-providers">The Top Serverless GPU Providers in 2025, Ranked by Cold Start</a></li>
<li><a href="https://www.spheron.network/blog/gpu-cold-start-llm-inference-2026/">GPU Cold Start on Serverless LLM Inference: 4 Fixes That Actually Work ...</a></li>

</ul>
</details>

**Tags**: `#serverless`, `#GPU`, `#cold start`, `#hedging`, `#speculative execution`

---