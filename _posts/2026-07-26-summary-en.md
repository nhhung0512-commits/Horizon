---
layout: default
title: "Horizon Summary: 2026-07-26 (EN)"
date: 2026-07-26
lang: en
---

> From 32 items, 10 important content pieces were selected

---

1. [Science Investigates Fatal Unauthorized Gene Therapy at Shanghai Hospital](#item-1) ⭐️ 9.0/10
2. [GrapheneOS Protections Against Data Extraction from Locked Devices](#item-2) ⭐️ 8.0/10
3. [Investigation Uncovers LLM Token Resale Market via API Proxies](#item-3) ⭐️ 8.0/10
4. [Ruff v0.16.0 Default Rules Surge from 59 to 413](#item-4) ⭐️ 8.0/10
5. [YOLO26n Inference from Scratch Using ARM64 Assembly](#item-5) ⭐️ 8.0/10
6. [4B Open-Weight Models Approach o3 in Swedish Medical QA](#item-6) ⭐️ 8.0/10
7. [LLMs Compared on IMO 2026: Frontier Models Excel, Harness Helps](#item-7) ⭐️ 8.0/10
8. [CXMT to Debut on Shanghai Stock Exchange, May Become Largest A-Share Company](#item-8) ⭐️ 8.0/10
9. [Claude Shared Links Leak User Data via Search Engine Indexing](#item-9) ⭐️ 8.0/10
10. [SpaceX Stops Falcon 9 Orders Beyond 2028, Pivots to Starship](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Science Investigates Fatal Unauthorized Gene Therapy at Shanghai Hospital](https://t.me/zaihuapd/42777) ⭐️ 9.0/10

Science magazine published an investigation on July 23, 2026, revealing that a 6-year-old girl died at Shanghai Xinhua Hospital in March 2025 after receiving experimental base editing gene therapy without regulatory approval, and the hospital concealed the incident. This case raises grave ethical and safety concerns about unregulated gene editing in humans, potentially undermining public trust in gene therapy and prompting stricter oversight worldwide. The girl suffered from a rare monogenic disease; the research team injected trillions of AAV viral vectors into her spinal fluid to target brain neurons. She died from a severe immune reaction within 7 days, and her parents paid over $800,000 out of pocket.

telegram · zaihuapd · Jul 26, 06:01

**Background**: Base editing is a gene editing technique that enables precise single-base conversions without cutting both DNA strands, reducing the risk of unintended insertions or deletions. AAV (adeno-associated virus) vectors are commonly used to deliver therapeutic genes to cells, including in the central nervous system. ClinicalTrials.gov is a publicly accessible registry of clinical trials maintained by the U.S. National Library of Medicine. In China, experimental therapies require approval from the National Medical Products Administration and ethics committees, which appears to have been bypassed in this case.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41573-020-0084-6">Base editing: advances and therapeutic opportunities | Nature Reviews Drug Discovery</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adeno-associated_virus">Adeno-associated virus - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ClinicalTrials.gov">ClinicalTrials . gov - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#gene editing`, `#bioethics`, `#clinical trial`, `#Science investigation`, `#China`

---

<a id="item-2"></a>
## [GrapheneOS Protections Against Data Extraction from Locked Devices](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices) ⭐️ 8.0/10

A community discussion highlights GrapheneOS's advanced protections, including an auto-reboot feature that returns the device to Before First Unlock (BFU) mode, preventing key extraction from locked devices. This matters because GrapheneOS provides a higher level of security for journalists and privacy-conscious users, even without a duress PIN, potentially thwarting forensic data extraction and border searches. The auto-reboot feature can be configured to automatically restart the device after a period of inactivity, reverting from After First Unlock (AFU) to BFU state, wiping encryption keys from RAM. The discussion also notes that pattern locks offer only ~18.57 bits of entropy, equivalent to less than three random characters.

hackernews · Cider9986 · Jul 26, 05:57 · [Discussion](https://news.ycombinator.com/item?id=49055169)

**Background**: GrapheneOS is a security-focused open-source mobile OS based on Android, available for Google Pixel devices. It implements extensive hardening to protect user data. The auto-reboot feature forces a transition from the unlocked AFU state back to the locked BFU state, where full disk encryption keys are unavailable. This makes brute-force attacks more difficult by enforcing throttling through the secure element.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS - Wikipedia</a></li>
<li><a href="https://grapheneos.org/features">Features overview | GrapheneOS</a></li>

</ul>
</details>

**Discussion**: The community overwhelmingly supports the auto-reboot feature, with users noting its use in helping journalists protect sources. Some commenters call for a complete backup/restore solution to allow safe wiping before border crossings. Others compare GrapheneOS favorably to Apple's lockdown mode, and one user criticizes the low entropy of pattern locks.

**Tags**: `#security`, `#grapheneos`, `#android`, `#privacy`, `#password-entropy`

---

<a id="item-3"></a>
## [Investigation Uncovers LLM Token Resale Market via API Proxies](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 8.0/10

A detailed investigation by Matt Lenhard reveals a thriving black market where resellers pool LLM API keys from free trials, stolen cards, and unprotected endpoints to offer discounted tokens through open-source proxy software like one-api and new-api. This market exposes systemic fraud vulnerabilities in LLM API infrastructure, costing providers significant revenue and posing security risks for developers who may inadvertently fund abuse. It also underscores the urgent need for strict API caps and better fraud detection. The resale market is predominantly China-based, using open-source API proxy projects one-api and its fork new-api to load-balance across pooled credentials. Buyers include those seeking cheap tokens, bypassing geo-restrictions, or collecting data for model distillation.

rss · Simon Willison · Jul 26, 19:30

**Background**: API relay proxies act as intermediaries between users and LLM providers, enabling multi-key pooling and load balancing to manage rate limits and costs. While legitimate uses exist, fraudsters exploit these tools by aggregating credentials obtained through trial abuse, chargebacks, or stolen credit cards. Open-source tools like one-api and new-api are designed for legitimate multi-key management but can be repurposed for fraudulent token resale.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.4sapi.com/blog/api-relay-proxies-llm-cost-optimization">Cut LLM API Costs with Relay Proxies - 4sAPI Blog</a></li>
<li><a href="https://www.getmaxim.ai/articles/top-5-tools-to-tackle-rate-limiting-for-llm-apps/">Top 5 Tools to Tackle Rate Limiting for LLM Apps</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#fraud`, `#API`, `#LLM`

---

<a id="item-4"></a>
## [Ruff v0.16.0 Default Rules Surge from 59 to 413](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0, released on July 23rd, expands its default rule set from 59 to 413 rules, potentially breaking existing CI pipelines with unpinned dependencies. This dramatic increase means many Python projects will discover numerous new issues in their codebases, improving code quality but requiring immediate attention from developers and automated CI fixes. The total number of rules in Ruff has grown from 708 to 968 since v0.1.0, and the new defaults catch syntax errors and runtime errors that were previously skipped without explicit configuration.

rss · Simon Willison · Jul 25, 22:44

**Background**: Ruff is an extremely fast Python linter and code formatter written in Rust, combining the functionality of tools like Flake8, Black, and isort into a single binary. It is developed by Astral, which was recently acquired by OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://docs.astral.sh/ruff/">Ruff - Astral Docs</a></li>

</ul>
</details>

**Tags**: `#Python`, `#linting`, `#Ruff`, `#CI`, `#release`

---

<a id="item-5"></a>
## [YOLO26n Inference from Scratch Using ARM64 Assembly](https://www.reddit.com/r/MachineLearning/comments/1v6w394/i_implemented_the_yolo26n_model_inference_from/) ⭐️ 8.0/10

A developer implemented YOLO26n object detection inference entirely from scratch using ARM64 assembly language and C, without any existing deep learning frameworks. The implementation incorporates multiple low-level optimizations including ARM NEON SIMD, Winograd convolution, cache-aware tiling, and operator fusion, and runs on a Raspberry Pi 4. This project demonstrates how deep learning inference can be optimized at the bare-metal level for edge devices, offering both educational value and potential for high-efficiency deployment. It highlights the feasibility of achieving decent performance without heavyweight libraries, which is critical for resource-constrained environments like IoT and robotics. The implementation includes custom ARM64 micro-kernels, a redesigned memory layout in a custom binary format, and specific YOLO26n modules such as Conv, C3K2, SPPF, C2PSA, PSA, BottleNeck, and Detect. Despite successful detection results, the author noted that the performance improvement was lower than expected, indicating room for further optimization.

reddit · r/MachineLearning · /u/Forward_Confusion902 · Jul 26, 06:43

**Background**: YOLO (You Only Look Once) is a popular family of real-time object detection models. YOLO26n is a variant optimized for edge devices. Running inference efficiently on ARM CPUs like the Raspberry Pi's requires careful low-level optimization due to limited compute and memory. Techniques like Winograd convolution reduce the number of multiplications in convolutional layers, while SIMD (Single Instruction Multiple Data) instructions like ARM NEON allow parallel processing of multiple data points. Cache-aware tiling and operator fusion further minimize memory bandwidth bottlenecks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/winograd-convolution">Winograd Convolution in CNNs</a></li>
<li><a href="https://arxiv.org/html/2410.17725v1">YOLOv11: An Overview of the Key Architectural Enhancements</a></li>
<li><a href="https://docs.ultralytics.com/reference/nn/modules/block">nn.modules.block API Reference | Ultralytics Docs</a></li>

</ul>
</details>

**Discussion**: The Reddit post likely receives positive feedback for its technical depth and educational value, with suggestions for further optimization from the community. Users may discuss alternative approaches or point out potential improvements in memory layout or SIMD usage.

**Tags**: `#YOLO`, `#ARM64`, `#Assembly`, `#Edge AI`, `#Optimization`

---

<a id="item-6"></a>
## [4B Open-Weight Models Approach o3 in Swedish Medical QA](https://www.reddit.com/r/MachineLearning/comments/1v71wds/openweight_4b_models_approach_o3level_medical/) ⭐️ 8.0/10

Open-weight 4B models Gemma4-E4B and Qwen3.5-4B achieve up to 87% accuracy on the Swedish medical licensing exam dataset MedQA-SWE, approaching the performance of GPT-4 (84%) and o3 (88%). This demonstrates that small open-weight models can rival much larger proprietary systems in specialized domains, potentially democratizing access to high-quality medical question answering in low-resource languages like Swedish. Qwen3.5-4B achieves 87% accuracy with reasoning enabled, but its reasoning traces are in English despite Swedish prompts; an early exit intervention from the S-GRPO paper helps prevent infinite loops.

reddit · r/MachineLearning · /u/AccomplishedCat4770 · Jul 26, 11:58

**Background**: MedQA-SWE is a Swedish clinical question-answering dataset built from medical licensing exams. Small open-weight models (4B parameters) are significantly cheaper and more accessible than large proprietary models like GPT-4 or o3. The S-GRPO paper proposes a reinforcement learning method to enable early exit in chain-of-thought reasoning, reducing unnecessary computation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.07686">S - GRPO : Early Exit via Reinforcement Learning in Reasoning Models</a></li>
<li><a href="https://huggingface.co/datasets/nicher92/medqa-swe">nicher92/ medqa - swe · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#open-weight models`, `#medical question answering`, `#reasoning`, `#LLM fine-tuning`, `#Swedish`

---

<a id="item-7"></a>
## [LLMs Compared on IMO 2026: Frontier Models Excel, Harness Helps](https://www.reddit.com/r/MachineLearning/comments/1v6wskz/we_compared_different_llms_on_imo_2026_r/) ⭐️ 8.0/10

A Reddit post compares various LLMs on the novel IMO 2026 problems, showing frontier models achieve near-perfect scores while other models improve dramatically with a custom multi-agent harness called AutoFyn. This benchmark tests genuine reasoning and multi-step problem-solving, demonstrating that harness engineering can bridge the gap for weaker models but cannot substitute for core capability, highlighting the importance of both model quality and system design. Frontier models (sol, fable) scored perfectly regardless of harness; Sonnet and Opus improved from poor webapp performance to higher scores when using Claude Code and AutoFyn; the hardest problem (P3) remained unsolved by all non-frontier models due to a missing key reduction.

reddit · r/MachineLearning · /u/pequalnp92 · Jul 26, 07:21

**Background**: The International Mathematical Olympiad (IMO) features novel, multi-step math problems not included in training data, making it a strong proxy for general intelligence. Harness engineering involves building structured systems—such as agent loops, retrieval, and verification—around LLMs to improve reliability. AutoFyn is an open-source multi-agent harness developed by the authors, designed to run long-duration tasks with clean state per round.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/SignalPilot-Labs/AutoFyn">GitHub - SignalPilot-Labs/AutoFyn: Run Claude in self ...</a></li>
<li><a href="https://github.com/RyanAlberts/best-of-Agent-Harnesses">GitHub - RyanAlberts/best-of-Agent-Harnesses: Curated ...</a></li>
<li><a href="https://www.decodingai.com/p/agentic-harness-engineering">Agentic Harness Engineering : LLMs as the New OS</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmark`, `#mathematical reasoning`, `#IMO`, `#multi-agent`

---

<a id="item-8"></a>
## [CXMT to Debut on Shanghai Stock Exchange, May Become Largest A-Share Company](https://www.bloomberg.com/news/articles/2026-07-26/memory-frenzy-primes-china-champion-cxmt-for-historic-debut?srnd=phx-technology) ⭐️ 8.0/10

ChangXin Memory Technologies (CXMT), China's leading DRAM manufacturer, will debut on the Shanghai Stock Exchange on July 27, 2026, after completing a 66.6 billion yuan IPO—the largest A-share IPO since 2010. This listing marks a major milestone for China's semiconductor self-sufficiency efforts, as CXMT is the country's most advanced DRAM IDM. If the stock price rises as analysts predict, it could surpass Industrial and Commercial Bank of China to become the highest market cap on the A-share market. The IPO price was set at 8.66 yuan per share, giving an initial market cap of about 580 billion yuan. Retail investor subscriptions were oversubscribed 212 times, with 9.4 million orders freezing approximately 7.07 trillion yuan in funds.

telegram · zaihuapd · Jul 26, 07:31

**Background**: DRAM (Dynamic Random Access Memory) is a type of semiconductor memory used for main system memory in computers and servers. An IDM (Integrated Device Manufacturer) designs and manufactures its own chips, unlike fabless companies that outsource production. CXMT is a DRAM IDM, meaning it controls both design and fabrication.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_random-access_memory">Dynamic random-access memory - Wikipedia</a></li>
<li><a href="https://www.techtarget.com/searchstorage/definition/DRAM">What is DRAM (Dynamic Random Access Memory)? How Does it Work?</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#IPO`, `#semiconductor`, `#China`, `#finance`

---

<a id="item-9"></a>
## [Claude Shared Links Leak User Data via Search Engine Indexing](https://search.brave.com/search?q=site%3Aclaude.ai%2Fshare&amp;source=android) ⭐️ 8.0/10

Claude's shared conversation links lack noindex tags, causing sensitive user data to be indexed by search engines like Brave and Bing, exposing API keys, financial info, and more. This privacy vulnerability exposes highly sensitive personal and business data to anyone using a search engine, with evidence of active exploitation. It undermines user trust in AI services that promise privacy and requires urgent action from Anthropic. Google has blocked the indexed pages, but Brave and Bing continue to show results. Anthropic has not yet fixed the issue, and users are advised to manually delete sensitive shared conversations.

telegram · zaihuapd · Jul 26, 11:16

**Background**: A noindex tag is an HTML meta tag or HTTP header that instructs search engines not to include a page in their search results. Without such a tag, publicly accessible web pages are automatically crawled and indexed by search engines like Google, Brave, and Bing. This means any content on a URL without noindex can be discovered via search queries, even if the page is intended only for sharing with specific individuals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noindex">noindex - Wikipedia</a></li>
<li><a href="https://developers.google.com/search/docs/crawling-indexing/block-indexing">Block Search Indexing with noindex | Google Search Central | Documentation | Google for Developers</a></li>
<li><a href="https://www.lumar.io/blog/best-practice/noindex-disallow-nofollow/">Noindex, Nofollow & Disallow: How to Use SEO Indexing & Crawling Directives</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#security`, `#Claude`, `#vulnerability`, `#AI`

---

<a id="item-10"></a>
## [SpaceX Stops Falcon 9 Orders Beyond 2028, Pivots to Starship](https://www.bloomberg.com/news/articles/2026-07-23/spacex-is-turning-away-falcon-customers-in-major-bet-on-starship) ⭐️ 8.0/10

SpaceX has stopped accepting new Falcon 9 launch orders for missions scheduled after 2028 and has scaled back production of non-reusable Falcon components, accelerating its transition to the Starship system. This strategic pivot signals SpaceX's commitment to Starship as its primary launch vehicle, but risks leaving satellite operators without viable launch options if Starship fails to achieve commercial readiness by late 2028. SpaceX may still support Falcon 9 missions for the U.S. Department of Defense and NASA, but the company's stock has declined about 25% since its June 2026 IPO amid Starship test delays.

telegram · zaihuapd · Jul 26, 12:42

**Background**: Falcon 9 is a partially reusable medium-lift rocket that has dominated the commercial launch market through high cadence and low-cost rideshare programs. Starship, a fully reusable super-heavy lift vehicle under development, is intended to lower costs further and enable deep space missions, but as of July 2026 it has flown 13 times with 8 successes and 5 failures and is not yet operational.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9">Falcon 9 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://www.spacex.com/rideshare">SpaceX - Rideshare</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#Falcon 9`, `#commercial spaceflight`, `#launch services`

---