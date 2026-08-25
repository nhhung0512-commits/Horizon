---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 36 items, 9 important content pieces were selected

---

1. [Apple unveils M6 and M5 Ultra chips with major AI compute gains](#item-1) ⭐️ 9.0/10
2. [OpenAI's Jalapeño Chip Claims to Beat Nvidia Blackwell in Efficiency](#item-2) ⭐️ 9.0/10
3. [Apple Unveils Mac Studio with M5 Max and M5 Ultra for AI](#item-3) ⭐️ 8.0/10
4. [Nitter Project Receives Cease and Desist; All Instances Down](#item-4) ⭐️ 8.0/10
5. [Continual Learning on Open-Weight Models Paves Path to SovereignAI](#item-5) ⭐️ 8.0/10
6. [SpaceX Plans to Launch Nvidia Vera Rubin NVL72 into Orbit in 2027](#item-6) ⭐️ 8.0/10
7. [NVIDIA Vera Rubin NVL72 Benchmarks: 30x Throughput, 35x Lower Cost](#item-7) ⭐️ 8.0/10
8. [NVIDIA Jetson Orin Nano 2 Doubles Edge AI Inference, Cuts Power 40%](#item-8) ⭐️ 8.0/10
9. [Anthropic Q2 Revenue Surges 14x to Over $11.5 Billion](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Apple unveils M6 and M5 Ultra chips with major AI compute gains](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 9.0/10

Apple announced the M6 and M5 Ultra chips on August 25, 2026, debuting the M6 in the new Mac mini and the M5 Ultra in the Mac Studio. The M6 is Apple's first 2-nanometer chip, featuring a 12-core CPU, 12-core GPU, dual 16-core Neural Engine, and up to 170GB/s unified memory bandwidth. This release marks a major leap in Apple Silicon performance and AI compute, reinforcing Apple's push toward on-device AI and high-end workstation capabilities. It also broadens the Mac lineup dramatically, with the M6 targeting mainstream devices and the M5 Ultra aiming at professionals, potentially reshaping pricing and performance expectations across the industry. The M5 Ultra uses a quad-chip architecture, a first for the M series, offering up to 36-core CPU and 80-core GPU with support for up to 512GB of memory and 1.2TB/s unified memory bandwidth, which is 50% higher than the M3 Ultra. The M6 Mac mini starts at ¥6,999, while the M5 Pro Mac mini starts at ¥12,999; the Mac Studio with M5 Max starts at ¥19,999.

hackernews · interpol_p · Aug 25, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49433292)

**Background**: Apple Silicon is Apple's line of Arm-based system-on-chips, introduced in 2020 to replace Intel processors in Macs. The M6 is Apple's first chip built on a 2-nanometer process, while the M5 Ultra employs a quad-die design to scale performance and memory. These chips use a unified memory architecture shared by the CPU, GPU, and Neural Engine, which is particularly important for AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/">Apple</a></li>
<li><a href="https://en.m.wikipedia.org/wiki/Apple_Inc.">Apple Inc. - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed a mix of admiration and skepticism: some praised the performance leap and noted that inflation-adjusted prices are comparable to older Macs, while others criticized the astronomical cost of fully maxed-out configurations, with one user calculating a $24,699 fully loaded Mac Studio. There was also nostalgia from one user who compared the situation to the 1990s, and another who argued that the $450 M4 Mac mini remains the best value in computing.

**Tags**: `#Apple Silicon`, `#M6`, `#M5 Ultra`, `#AI Compute`, `#Hardware`

---

<a id="item-2"></a>
## [OpenAI's Jalapeño Chip Claims to Beat Nvidia Blackwell in Efficiency](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI published its first test results for its self-designed inference ASIC, code-named Jalapeño, and claims it outperforms Nvidia's Blackwell-based GB300 in throughput per megawatt and latency. The chip is reportedly co-developed with Broadcom and is slated for deployment in OpenAI's own data centers before the end of this year. If confirmed, this marks a major challenge to Nvidia's near-monopoly in AI accelerators, showing that custom ASICs tailored to specific workloads can beat general-purpose GPUs on cost and efficiency. It could accelerate the broader industry trend among hyperscalers toward in-house silicon, pressuring Nvidia's pricing power and reshaping the AI hardware supply chain. On models including GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T, Jalapeño reportedly delivers 1.5–1.9x better work per unit of power, 1.7–3.6x lower end-to-end latency, and 2.1–4.1x higher performance in interactive scenarios. The chip has a rated power of 700W with sustained power not exceeding 550W, and benchmarks were compared against Nvidia GB300, not the newer Vera Rubin, and the chip is not intended for model training.

hackernews · Semianalysis · Aug 25, 14:06 · [Discussion](https://news.ycombinator.com/item?id=49434378)

**Background**: Jalapeño is an application-specific integrated circuit (ASIC), a fixed-function chip designed for a narrow task — in this case, AI inference — rather than a general-purpose GPU like Nvidia's Blackwell family. Nvidia's Blackwell architecture, which powers chips like the GB200 and GB300, has been the dominant platform for AI training and inference, but custom ASICs can offer lower power consumption and better cost efficiency when optimized for specific model workloads. OpenAI's move follows a pattern among large AI companies like Google and Amazon, which have also developed their own accelerators to reduce dependence on Nvidia.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/">The Engine Behind AI Factories | NVIDIA Blackwell Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Application-specific_integrated_circuit">Application-specific integrated circuit - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters generally welcomed the news, with some noting that continued hardware improvements make token price drops inevitable. One commenter speculated that OpenAI and Anthropic could eventually bake static LLM weights into chips for massive speed and cost gains, while another joked that analysis of a trillion-dollar industry is being led by ex-Reddit and 4chan mods at SemiAnalysis. A few also pointed out that human speech is still 22x more energy-efficient than this chip, and that OpenAI may seek an IPO to raise capital for further hardware buildout.

**Tags**: `#OpenAI`, `#AI Hardware`, `#ASIC`, `#Nvidia`, `#Semiconductors`

---

<a id="item-3"></a>
## [Apple Unveils Mac Studio with M5 Max and M5 Ultra for AI](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) ⭐️ 8.0/10

Apple announced a new Mac Studio powered by the M5 Max and the new M5 Ultra chip, with a strong emphasis on local AI performance and high memory bandwidth. The launch positions the Mac Studio as Apple's most powerful Mac for on-device AI workloads. This is significant because it signals Apple's continued push into on-device AI, giving professionals a high-memory-bandwidth machine for running large language models locally. It could influence how AI developers choose between cloud and local inference and strengthen Apple's ecosystem for AI/ML workloads. The M5 Max supports up to 128GB of unified memory with 614GB/s bandwidth, while the high-end M5 Ultra configuration is reported to offer 256GB or more memory and up to 1.2TB/s internal memory bandwidth. The new Mac Studio also debuts PCIe Gen 6 storage, delivering up to twice the storage performance of the previous generation.

hackernews · interpol_p · Aug 25, 13:03 · [Discussion](https://news.ycombinator.com/item?id=49433316)

**Background**: The Mac Studio is Apple's high-performance desktop aimed at professionals such as video editors, 3D artists, and researchers. The M5 series, introduced in late 2025, integrates CPU, GPU, NPU, and unified memory in a single chip, with the M5 Ultra being the highest-end variant. Unified memory allows the CPU and GPU to share the same memory pool, which is especially useful for running large AI models that require fast access to data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://www.notebookcheck.net/Apple-M5-Max-Processor-Benchmarks-and-Specs.1244918.0.html">Apple M5 Max Processor - Benchmarks and Specs - Notebookcheck Tech</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was lively, with users debating pricing and practicality for large-scale AI. Some noted the high cost (e.g., $10,000 for 256GB memory) and questioned future-proofing for models over 1 trillion parameters, while others welcomed Apple's emphasis on local AI and the first PCIe Gen 6 storage in a personal computer.

**Tags**: `#Apple`, `#Mac Studio`, `#M5`, `#hardware`, `#AI`

---

<a id="item-4"></a>
## [Nitter Project Receives Cease and Desist; All Instances Down](https://github.com/zedeus/nitter/issues/1442) ⭐️ 8.0/10

The Nitter project announced in GitHub issue #1442 that it has received cease and desist letters. All public Nitter instances are expected to remain down for the foreseeable future while the maintainers seek legal advice. This marks a significant escalation in legal pressure on open-source tools that provide privacy-preserving access to Twitter/X. It could deter similar projects, reduce user privacy options, and affect people who rely on Nitter to browse X without tracking or an account. Nitter is a free and open-source alternative frontend that only supports browsing; users cannot sign in or interact with posts. The maintainers provided no further details beyond the cease and desist letters, and all instances are now down for the foreseeable future.

hackernews · Banditoz · Aug 25, 17:08 · [Discussion](https://news.ycombinator.com/item?id=49437283)

**Background**: Nitter is a free and open-source alternative frontend for Twitter/X focused on privacy and performance, letting users view profiles, tweets, replies, and media without ads, tracking, or an account. It is commonly accessed through public instances, which have long struggled with rate limits and anti-bot measures. Legal action from X adds a new and potentially decisive threat to the project's sustainability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter</a></li>
<li><a href="https://nitter.tiekoetter.com/about">nitter .tiekoetter.com</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with X's restrictions, noting that users now need an account to lurk and that non-algorithmic feeds cannot be easily configured. Some praised community-friendly platforms, citing Hacker News's dang for supporting an unofficial clone rather than sending legal threats. Overall sentiment was sympathetic to Nitter and critical of X's growing platform control.

**Tags**: `#nitter`, `#privacy`, `#open-source`, `#legal`, `#twitter`

---

<a id="item-5"></a>
## [Continual Learning on Open-Weight Models Paves Path to SovereignAI](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 8.0/10

A new technical report and open-weights model, Thomson, argue that continual learning from open-weight models can close the gap to frontier performance. The team demonstrates competitive results across domains such as safety, legal, tax, multilingualism, and agentic tasks with far lower compute and personnel budgets. This matters because it challenges the assumption that only a few heavily funded labs can build frontier models. It offers a concrete, short-term route for governments, mid-size companies, and public institutions to achieve SovereignAI—independent ownership of the model, infrastructure, values, and data privacy. Thomson is a general-purpose frontier model trained with an emphasis on high-stakes professional work. The report claims a distinctive 'π-shaped' evaluation pattern: wide capability improvements including untargeted domains, while almost eliminating catastrophic forgetting, via minimal high-impact parameter interventions.

reddit · r/MachineLearning · /u/Forsaken_Scientist · Aug 25, 10:30

**Background**: Continual learning, also called lifelong learning, trains a model sequentially on new tasks while preserving previously learned knowledge. Open-weight models publicly release trained parameters, so anyone can download, run, study, and modify them. SovereignAI refers to an organization's ability to independently build, deploy, and govern AI use, a goal often discussed but rarely given practical guidance.

<details><summary>References</summary>
<ul>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open - Weight Model ? - Stanford HAI</a></li>
<li><a href="https://www.linkedin.com/pulse/continual-learning-llms-why-ai-models-need-sleep-nagesh-nama-nbtee">Continual Learning in LLMs: Why AI Models Need Sleep</a></li>

</ul>
</details>

**Tags**: `#continual learning`, `#open-weight models`, `#sovereign AI`, `#frontier models`, `#AI policy`

---

<a id="item-6"></a>
## [SpaceX Plans to Launch Nvidia Vera Rubin NVL72 into Orbit in 2027](https://www.theregister.com/off-prem/2026/08/25/spacex-claims-it-will-put-a-vera-rubin-nvl72-rack-scale-system-into-orbit-next-year/5292067) ⭐️ 8.0/10

SpaceX announced plans to launch an Nvidia Vera Rubin NVL72 rack-scale AI system into orbit in 2027 to validate space-based data center technologies. The announcement marks a concrete step toward operating advanced AI hardware in space. This is significant because it could pioneer the development of orbital AI data centers, enabling low-latency, space-based computing for defense, communications, and Earth observation. It also pushes the boundaries of where high-performance AI infrastructure can be deployed. The NVL72 system pairs 72 Rubin GPUs with 36 Vera CPUs and consumes over 100 kilowatts, requiring elaborate liquid cooling and power supply systems. SpaceX has not yet disclosed the launch timeline, orbital altitude, or the power and cooling solutions to be used in space.

telegram · zaihuapd · Aug 25, 08:03

**Background**: Vera Rubin NVL72 is Nvidia's next-generation rack-scale AI supercomputing platform, built on the third-generation MGX NVL72 rack design and offering AI training with one-fourth the GPUs and inference at one-tenth the cost per million tokens versus Blackwell. Space-based data centers are a proposed concept to place AI data centers in orbit, using space-based solar power and edge computing to bypass ground latency, with historical roots in military architectures like the Brilliant Pebbles program.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL72</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space-based_data_center">Space-based data center</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Nvidia`, `#AI computing`, `#Space data center`

---

<a id="item-7"></a>
## [NVIDIA Vera Rubin NVL72 Benchmarks: 30x Throughput, 35x Lower Cost](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 8.0/10

NVIDIA published first on-silicon benchmark results for its next-generation Vera Rubin NVL72 rack, showing up to 30x higher throughput per megawatt and up to 35x lower cost per million tokens versus GB300 when running DeepSeek-V4-Pro on agentic coding tasks. The company also announced production ramp of the Groq 3 LPX inference accelerator and the Vera CPU for agentic AI. This is significant because inference performance and cost are the key bottlenecks for deploying large language models at scale, and NVL72 shows rack-scale co-design can deliver order-of-magnitude gains. It strengthens NVIDIA's position in the AI data center market and signals a shift toward dedicated inference architectures like Groq LPX and agentic workloads. The Vera Rubin NVL72 integrates 72 Rubin GPUs and 36 Vera CPUs in one rack, with NVLink-Fusion and Spectrum-X Ethernet. The Groq 3 LPX, benchmarked at 3,400 output tokens per second when running Gemma 4 31B, supports up to 256 LP30 accelerators in a rack-scale deployment.

telegram · zaihuapd · Aug 25, 14:48

**Background**: NVIDIA's rack-scale systems like GB200 and the new Vera Rubin NVL72 combine GPUs, CPUs, and high-bandwidth networking into a single supercomputer to handle generative AI and agentic AI workloads. Agentic coding refers to AI agents that autonomously plan and execute multi-step software development tasks, which are compute-intensive and sensitive to latency. The benchmarks were run on DeepSeek-V4-Pro, a large language model used for such coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference">Vera Rubin NVL72 vs GB200 NVL72? Inference TCO & Architecture Analysis</a></li>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-lpx-spectrum-x-nvlink-fusion/">NVIDIA Advances Vera Rubin Inference With New LPX ... | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Vera Rubin`, `#AI hardware`, `#DeepSeek`, `#inference`

---

<a id="item-8"></a>
## [NVIDIA Jetson Orin Nano 2 Doubles Edge AI Inference, Cuts Power 40%](https://www.therobotreport.com/jetson-orin-nano-2-doubles-inference-performance-robotics-edge-says-nvidia/) ⭐️ 8.0/10

NVIDIA announced the Jetson Orin Nano 2, an entry-level edge AI module, on August 25, 2025. It delivers 78 TOPS of compute with 8 GB of memory, doubling the inference performance of the previous Orin Nano Super while reducing power consumption by 40% at the same performance level. This launch significantly strengthens NVIDIA's edge AI and robotics ecosystem, enabling real-time on-device inference for large models like Cosmos and Qwen 3. With over 3 million developers using NVIDIA's robotics stack, the module could accelerate deployment of cost-effective, power-efficient edge AI in drones, robots, and embedded devices. The module and developer kit are scheduled to ship in the first half of 2027. NVIDIA stated that companies such as Wing and Matic are evaluating or adopting the product, which is designed to runCosmos world foundation models and Qwen 3 LLMs directly at the edge.

telegram · zaihuapd · Aug 25, 16:54

**Background**: TOPS (trillions of operations per second) is a key metric for measuring the peak inference performance of AI accelerators, calculated from the number of operations per clock cycle, clock frequency, and processing units. NVIDIA's Jetson lineup targets edge computing and robotics, where localized inference reduces latency and improves privacy. Cosmos is NVIDIA's platform of generative world foundation models for physical AI, while Qwen 3 is Alibaba's family of large language models covering dense and mixture-of-experts architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lenovo.com/us/en/glossary/tops-in-computing/">What is TOPS in computing and How it Affects AI Performance | Lenovo US</a></li>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Edge Computing`, `#AI Hardware`, `#Robotics`, `#Jetson`

---

<a id="item-9"></a>
## [Anthropic Q2 Revenue Surges 14x to Over $11.5 Billion](https://t.me/zaihuapd/43403) ⭐️ 8.0/10

According to Bloomberg citing documents, Anthropic's preliminary second-quarter revenue exceeded $11.5 billion, up more than 14 times year over year. The company also posted a positive adjusted operating profit for the quarter. This milestone underscores Anthropic's rapid commercial growth in the competitive AI market and could boost investor confidence. A possible IPO this fall would be a major event for the AI sector, offering public market investors a rare opportunity to own a leading AI lab. The figures are preliminary and may be revised. Revenue compares with $787 million in the same quarter a year earlier and $4.73 billion in the first quarter of 2026, according to the reported documents.

telegram · zaihuapd · Aug 25, 17:32

**Background**: Anthropic is an AI safety and research company founded by former OpenAI researchers, best known for its Claude family of large language models. The company competes with OpenAI, Google, and Meta in the generative AI market, where demand for enterprise AI services has driven rapid revenue growth. A successful IPO would provide Anthropic with new capital to fund model development and expand its commercial business.

**Tags**: `#Anthropic`, `#AI Business`, `#Revenue`, `#IPO`

---