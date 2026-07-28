---
layout: default
title: "Horizon Summary: 2026-07-28 (EN)"
date: 2026-07-28
lang: en
---

> From 34 items, 12 important content pieces were selected

---

1. [PNAS Study: Over Half of Academic Papers Show LLM Influence by 2025](#item-1) ⭐️ 9.0/10
2. [Moonshot seeks more NVIDIA Blackwell chips for next AI model](#item-2) ⭐️ 9.0/10
3. [Sebastian Raschka Breaks Down Kimi K3's NoPE Architecture](#item-3) ⭐️ 8.0/10
4. [HIV vaccine 'curriculum' approach succeeds in preclinical study](#item-4) ⭐️ 8.0/10
5. [Kimi Linear: New Attention Architecture Outperforms Full Attention](#item-5) ⭐️ 8.0/10
6. [Moonshot Releases 2.8T Parameter Kimi K3 Open-Weight Model](#item-6) ⭐️ 8.0/10
7. [NeurIPS Reviewer Flags AI-Generated Rebuttals](#item-7) ⭐️ 8.0/10
8. [NeurIPS 2026 AI-Generated Reviews Spark Ethics Debate](#item-8) ⭐️ 8.0/10
9. [NeurIPS Prompt Injection Triggers Ethics Concerns](#item-9) ⭐️ 8.0/10
10. [中国兴起 AI 人脸租赁市场 一季度超 95% 微短剧使用 AI](#item-10) ⭐️ 8.0/10
11. [Shenzhen launches China's first unmanned vehicle-subway delivery](#item-11) ⭐️ 8.0/10
12. [Exchange mandates WAN for market data, cuts LAN lines](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PNAS Study: Over Half of Academic Papers Show LLM Influence by 2025](https://www.reddit.com/r/MachineLearning/comments/1v93q78/pnas_over_half_of_all_academic_articles_now_show/) ⭐️ 9.0/10

A PNAS study analyzing 7.3 million academic papers found that over 50% of articles published by 2025 show evidence of LLM influence, marking the largest empirical quantification of AI penetration in academic publishing. This study provides the first authoritative quantitative marker of how thoroughly LLMs have reshaped scientific writing, with significant policy implications regarding inequality in adoption across lower-prestige and non-English institutions. The adoption skews toward lower-prestige and non-English institutions, highlighting a fresh policy dimension about inequality in LLM usage in academic publishing.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jul 28, 16:38

**Background**: Large language models (LLMs) like GPT-4 have become widely used for generating and polishing text, including in academic writing. This study is the largest empirical investigation to date, analyzing 7.3 million papers to quantify the extent of LLM influence in published research.

**Discussion**: The Reddit community expressed strong interest, with the top comment noting that the inequality angle (adoption skews lower-prestige and non-English institutions) is a fresh policy dimension. There was no detailed debate in the provided comments.

**Tags**: `#LLM`, `#academic publishing`, `#AI impact`, `#empirical study`, `#inequality`

---

<a id="item-2"></a>
## [Moonshot seeks more NVIDIA Blackwell chips for next AI model](https://www.theinformation.com/articles/chinese-ai-startup-moonshot-seeks-nvidia-blackwell-chips-next-model) ⭐️ 9.0/10

Chinese AI startup Moonshot is reportedly seeking additional NVIDIA Blackwell series chips for its next-generation model, following accusations by the White House that the company violated US export controls by acquiring GB300 servers through Thailand to train its Kimi K3 model. This escalation highlights the intensifying US-China tech tensions over advanced AI chips, potentially impacting the development of Chinese AI models and prompting stricter enforcement of export controls. The outcome could affect global AI supply chains and competitive dynamics. The GB300 is part of NVIDIA's Blackwell Ultra series, a rack-scale liquid-cooled system with 72 Blackwell Ultra GPUs and 36 Grace CPUs. Moonshot's Kimi K3 model had already been trained using allegedly illegally obtained GB300 servers, and the company now seeks more chips for its next iteration.

telegram · zaihuapd · Jul 28, 13:52

**Background**: NVIDIA's Blackwell architecture, announced in 2024 and updated to Blackwell Ultra in 2025, is designed for massive AI workloads and is heavily restricted from export to China under US trade rules. Moonshot, a prominent Chinese AI startup, develops large language models and has been at the center of accusations regarding circumvention of these controls. The US government has increased scrutiny of AI chip flows to China, targeting companies suspected of evading restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">NVIDIA GB300 NVL72</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/nvidia-blackwell-architecture-deep-dive-a-closer-look-at-the-upgrades-coming-with-rtx-50-series-gpus">Nvidia Blackwell architecture deep dive: A closer... | Tom's Hardware</a></li>

</ul>
</details>

**Tags**: `#AI`, `#semiconductors`, `#export controls`, `#Moonshot`, `#NVIDIA Blackwell`

---

<a id="item-3"></a>
## [Sebastian Raschka Breaks Down Kimi K3's NoPE Architecture](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html) ⭐️ 8.0/10

Sebastian Raschka published a detailed architecture breakdown of Kimi K3, highlighting the complete removal of all RoPE (Rotary Position Embeddings) layers in favor of NoPE (No Positional Embeddings) across the entire model. This architectural choice challenges the long-standing assumption that explicit positional encoding is necessary for transformer models, showing that attention mechanisms can implicitly learn positional information. The successful adoption of NoPE in a state-of-the-art 1M-context model could influence future LLM design. Kimi K3 employs a hybrid attention mechanism combining Kimi Delta Attention (KDA) layers with Gated Multi-Head Latent Attention (MLA). NoPE is applied in every layer, relying entirely on attention outputs to encode token position, as opposed to traditional RoPE which adds sinusoidal positional signals.

hackernews · ModelForge · Jul 28, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49085698)

**Background**: Positional embeddings like RoPE are standard in most modern LLMs to help the model understand token order. NoPE (No Positional Embeddings) is an alternative that removes explicit positional information, forcing attention to infer sequence order from the data. Recent research, such as the hybrid approach in SmolLM3 that drops RoPE every 4th layer, suggests NoPE can be effective for long-context modeling while reducing complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2501.18795v1">Rope to Nope and Back Again: A New Hybrid Attention Strategy</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/nope/">No Positional Embeddings (NoPE) | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that removing all positional embeddings works at all, with one asking whether the model becomes a 'token soup' without positional inductive bias. Others praised Sebastian Raschka's analysis and linked the architectural choices to Kimi K3's strong real-world performance in coding and multimodal tasks.

**Tags**: `#LLM`, `#architecture`, `#Kimi`, `#NoPE`, `#technical analysis`

---

<a id="item-4"></a>
## [HIV vaccine 'curriculum' approach succeeds in preclinical study](https://www.lji.org/news-events/news/post/new-hiv-vaccine-shows-unprecedented-success-in-preclinical-study/) ⭐️ 8.0/10

A new HIV vaccine that uses a series of shots to sequentially train the immune system to produce broadly neutralizing antibodies has shown unprecedented success in preclinical studies in monkeys. This marks a major step toward an effective HIV vaccine, a goal that has remained elusive for decades due to the virus's rapid mutation. If human trials confirm the results, it could complement existing prevention tools like PrEP and help reduce HIV transmission globally. The vaccine employs a germline-targeting strategy, where each shot presents slightly different immunogens to guide B cell maturation, as detailed in the Nature paper (DOI: 10.1038/s41586-026-10837-5). Phase I human trials are already underway, but past experience suggests many HIV vaccines fail at this stage.

hackernews · codebyaditya · Jul 28, 13:12 · [Discussion](https://news.ycombinator.com/item?id=49083314)

**Background**: HIV is a highly mutable virus that evades the immune system, making vaccine development difficult. Broadly neutralizing antibodies (bnAbs) can target conserved regions of HIV, but inducing them requires precisely guiding B cell development through multiple stages, a concept known as germline-targeting and sequential immunization. This approach mimics a natural 'curriculum' to train the immune system step by step.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41590-024-01852-7">Germline-targeting immunogens guide bnAb development - Nature</a></li>
<li><a href="https://www.cell.com/immunity/fulltext/S1074-7613(26)00123-8">Germline-targeting HIV immunogen induces cross-neutralizing ...</a></li>
<li><a href="https://www.science.org/doi/10.1126/sciimmunol.adk9550">Germline-targeting HIV vaccination induces neutralizing ...</a></li>

</ul>
</details>

**Discussion**: Commenters were fascinated by the 'curriculum' concept but expressed caution, noting that many HIV vaccines have failed in human trials. One user argued that existing PrEP effectively prevents transmission and advocated for broader PrEP distribution instead of relying on a future vaccine. Another provided links to the original paper and an independent analysis, urging readers not to trust press releases blindly.

**Tags**: `#HIV`, `#vaccine`, `#immunology`, `#biotechnology`, `#preclinical`

---

<a id="item-5"></a>
## [Kimi Linear: New Attention Architecture Outperforms Full Attention](https://arxiv.org/abs/2510.26692) ⭐️ 8.0/10

Moonshot AI introduced Kimi Linear, a hybrid linear attention architecture that outperforms full attention across short-context, long-context, and reinforcement learning scaling scenarios, and open-sourced its KDA kernel and vLLM implementations along with model checkpoints. This innovation demonstrates that linear attention can surpass full attention in expressiveness and efficiency, potentially reducing the computational cost of large language models while maintaining or improving performance. It has already been scaled up in the 2.8-trillion-parameter Kimi K3 model, showing practical impact. Kimi Linear uses a 3:1 interleave of Kimi Delta Attention (KDA) layers with full Multi-Head Latent Attention (MLA) layers, offering the best trade-off between cost and expressivity. The open-source release includes the KDA kernel, vLLM support, and pre-trained/instruct-tuned checkpoints.

hackernews · ronfriedhaber · Jul 28, 10:52 · [Discussion](https://news.ycombinator.com/item?id=49082022)

**Background**: Traditional Transformers rely on full self-attention, which has quadratic complexity with sequence length, making long-context processing expensive. Linear attention aims to reduce this complexity while preserving expressiveness. Kimi Linear is a hybrid architecture that combines linear attention layers with full attention layers, achieving strong performance across various benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://arxiv.org/pdf/2510.26692">KIMI LINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**Discussion**: The community is highly engaged, with experts comparing Kimi Linear favorably to other architectures like Gated Deltanet 2 and noting its open-source release and integration into Kimi K3. Some discuss the emergence of intelligence with scale, while others express excitement about open-source contributions enabling further research.

**Tags**: `#attention architecture`, `#deep learning`, `#open-source`, `#transformer`, `#LLM`

---

<a id="item-6"></a>
## [Moonshot Releases 2.8T Parameter Kimi K3 Open-Weight Model](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 8.0/10

Moonshot AI has released the weights of their 2.8 trillion parameter Kimi K3 model on Hugging Face under a modified license. The model is 1.56TB in size and is available immediately for download and inference. This release marks a significant milestone as one of the largest open-weight models ever made publicly available, offering immense capability to the AI community. The accompanying license change, requiring separate agreements for large Model-as-a-Service businesses, sets a notable precedent for commercial use of open-weight models. The license is no longer called 'modified MIT' but now requires a separate agreement for any entity with over $20M annual revenue operating a Model-as-a-Service business. OpenRouter is already offering Kimi K3 from seven providers at pricing matching Moonshot's own $3/M input and $15/M output tokens.

rss · Simon Willison · Jul 27, 23:39

**Background**: Kimi K3 is a large language model developed by Moonshot AI, a Chinese AI company. It follows their earlier K2 model, which also used a modified open license. The term 'open-weight' refers to models where the trained neural network weights are publicly released, but the training data, code, and methodology are typically not included. This distinguishes them from fully open-source models.

**Tags**: `#AI`, `#large language model`, `#open source`, `#Hugging Face`

---

<a id="item-7"></a>
## [NeurIPS Reviewer Flags AI-Generated Rebuttals](https://www.reddit.com/r/MachineLearning/comments/1v90r9r/neurips_2026_reviewer_aigenerated_rebuttals_and/) ⭐️ 8.0/10

A NeurIPS 2026 reviewer reported that a submitted paper and its rebuttals appear entirely generated by a large language model (LLM), specifically identifying Claude-like writing patterns. This incident highlights growing concerns about AI-generated content undermining the integrity of academic peer review, potentially eroding trust in conference publications and the review process. The reviewer noted that the authors acknowledged LLM assistance in the checklist, but found the AI-generated style difficult to parse and indicative of low effort. The post serves as both a rant and a request for guidance on handling such cases.

reddit · r/MachineLearning · /u/gateofptolemy · Jul 28, 14:52

**Background**: Large language models like Claude and GPT can generate coherent text, leading to 'AI slop' in academic publishing—papers that are linguistically plausible but lack original research. Peer review is a voluntary, unpaid process that already faces capacity issues, and AI-generated content exacerbates the burden on reviewers. Conferences like NeurIPS have ethical guidelines, but enforcement remains challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://aiblewmymind.substack.com/p/claude-skills-ai-write-like-you">The Claude Skills That Finally Made AI Write Like Me (And How to Build Yours)</a></li>
<li><a href="https://alitu.com/creator/content-creation/ai-writing-claude-styles/">Make Your AI Writing Sound More Like You, with Claude Writing Styles</a></li>
<li><a href="https://easternherald.com/2026/05/17/arxiv-ai-slop-ban-researchers-policy-2026/">arXiv Bans AI Slop Papers with One-Year Penalty Rule</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#peer review`, `#NeurIPS`, `#LLM`, `#academic publishing`

---

<a id="item-8"></a>
## [NeurIPS 2026 AI-Generated Reviews Spark Ethics Debate](https://www.reddit.com/r/MachineLearning/comments/1v8vuae/neurips_2026_aigenerated_reviews_d/) ⭐️ 8.0/10

A Reddit discussion highlights concerns about AI-generated peer reviews at NeurIPS 2026, with authors noting that prompt injection was used to test for LLM misuse and many reviews appear to be copied from language models without proper oversight. This undermines the integrity of the peer review process at a top machine learning conference, potentially leading to unfair evaluations and eroding trust in academic review. The author mentions that both reviewers and meta-reviewers might have relied on LLMs, and that prompt injection was deployed as a study to detect such misuse, raising questions about consequences for reviewers.

reddit · r/MachineLearning · /u/bricklerex · Jul 28, 11:34

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs override a model's instructions to cause unintended behavior, often used to bypass safety filters. In peer review, reviewers may use LLMs to generate reviews, and prompt injection could be used to test if a review was AI-generated by embedding hidden instructions that an LLM would follow but a human would not.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#peer review`, `#NeurIPS`, `#LLM misuse`, `#academic integrity`

---

<a id="item-9"></a>
## [NeurIPS Prompt Injection Triggers Ethics Concerns](https://www.reddit.com/r/MachineLearning/comments/1v955f6/neuripsside_prompt_injection_triggering_ethics/) ⭐️ 8.0/10

NeurIPS conference organizers secretly used prompt injection to detect LLM-generated peer reviews, but ethics reviewers were not informed about this manipulation, leading to ethical flags being raised. This incident undermines trust in the peer review process at a top AI conference, highlighting ethical risks of using covert technical measures without transparency or consent from reviewers. The prompt injection was embedded on the conference side to catch automated reviews, but ethics reviewers—who are supposed to oversee ethical practices—were kept in the dark, causing confusion and potential conflict of interest.

reddit · r/MachineLearning · /u/dontknowwhattoplay · Jul 28, 17:28

**Background**: Prompt injection is a security exploit where malicious or unintended inputs cause an LLM to behave contrary to its design. In this case, NeurIPS organizers used it as a detection tool against LLM-generated reviews, raising questions about consent and ethical oversight in academic peer review.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>

</ul>
</details>

**Tags**: `#NeurIPS`, `#prompt injection`, `#ethics`, `#AI conference`, `#peer review`

---

<a id="item-10"></a>
## [中国兴起 AI 人脸租赁市场 一季度超 95% 微短剧使用 AI](https://restofworld.org/2026/china-ai-microdramas-face-licensing/) ⭐️ 8.0/10

China's AI face licensing market is growing rapidly, with over 95% of microdramas using AI and a surge in related legal disputes.

telegram · zaihuapd · Jul 28, 03:03

**Tags**: `#AI`, `#face licensing`, `#microdramas`, `#China`, `#regulation`

---

<a id="item-11"></a>
## [Shenzhen launches China's first unmanned vehicle-subway delivery](https://www.sohu.com/a/1055801763_121613636) ⭐️ 8.0/10

Shenzhen has implemented China's first 'unmanned vehicle + subway' same-city delivery model, where parcels are transported by autonomous vehicles from a grid warehouse to a subway station, then transferred across districts via subway, and finally picked up by another unmanned vehicle for last-mile delivery. The model reduces transportation costs by approximately 60% and improves vehicle capacity utilization by 10%. This innovation significantly cuts logistics costs and improves efficiency for intra-city delivery, setting a new benchmark for urban logistics. It demonstrates the practical integration of autonomous vehicles with public transit infrastructure, paving the way for scalable smart city logistics solutions. In April 2026, Shenzhen granted nighttime cross-district road access to functional unmanned vehicles. JD Logistics has deployed nearly 100 such vehicles across 22 service points, operating 121 nighttime delivery routes. The vehicles are classified as 'functional unmanned vehicles' (低速无人车) under local regulations.

telegram · zaihuapd · Jul 28, 10:46

**Background**: Functional unmanned vehicles are low-speed autonomous vehicles designed for logistics, sanitation, and inspection, typically operating on sidewalks or dedicated lanes. In China, they require special permits and road rights from local authorities. The 'unmanned vehicle + subway' model leverages the subway's fast cross-district transit to overcome range and speed limitations of ground-level autonomous vehicles, enabling longer-distance same-city delivery with reduced cost.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tmtpost.com/6296729.html">tmtpost.com/6296729.html</a></li>
<li><a href="https://finance.sina.com.cn/roll/2026-05-23/doc-inhyuwef7546990.shtml">广东深圳无人车获批“夜间路权” 物流运输降本增效</a></li>
<li><a href="https://www.dutenews.com/n/article/10126082">行业迎爆发前夜！ 深圳 无 人 车 单月狂送90...</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#last-mile delivery`, `#logistics`, `#smart city`

---

<a id="item-12"></a>
## [Exchange mandates WAN for market data, cuts LAN lines](https://mp.weixin.qq.com/s/ba7Rx5VCnYnzJzWMHyLoaQ) ⭐️ 8.0/10

The exchange has mandated that all brokers switch from local area network (LAN) to wide area network (WAN) connections for market data feeds, with existing LAN lines set to be shut down by the end of July. A new requirement mandates that WAN lines must have a bidirectional latency no higher than 2 milliseconds. This change significantly impacts trading infrastructure, forcing brokers to upgrade their network connectivity and potentially affecting latency-sensitive trading strategies. It also centralizes market data delivery, which could alter the competitive landscape for high-frequency traders and smaller firms that relied on LAN co-location. The exchange's colocation datacenter used to offer LAN connections for ultra-low latency, but now those are being replaced with WAN lines that must meet a strict 2ms round-trip latency requirement. This applies to both existing and new WAN circuits, and the LAN shutdown is scheduled for the end of July.

telegram · zaihuapd · Jul 28, 11:31

**Background**: In financial trading, network latency is critical, especially for high-frequency trading firms that use co-location to gain speed advantages. LAN connections inside exchange data centers offered the lowest possible latency, while WAN lines involve longer distances and typically higher latency. The exchange's decision to standardize on WAN simplifies infrastructure but may increase latency for those previously using LAN, though the 2ms cap aims to keep it manageable.

<details><summary>References</summary>
<ul>
<li><a href="https://t.me/s/NiceNews345/27543">Nice News Channel – Telegram</a></li>
<li><a href="https://www.yicai.com/brief/103295227.html">券商接到“广域网交易行情线路技术要求”通知</a></li>

</ul>
</details>

**Tags**: `#financial trading`, `#brokerages`, `#exchange`, `#network infrastructure`

---