---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 26 items, 7 important content pieces were selected

---

1. [vLLM v0.25.0 Released: MRv2 Default, PagedAttention Removed](#item-1) ⭐️ 9.0/10
2. [Humanoid robot performs world's first live pig gallbladder surgery remotely](#item-2) ⭐️ 9.0/10
3. [VultronRetriever Models Achieve #1 on MTEB with Edge Efficiency](#item-3) ⭐️ 8.0/10
4. [SK Hynix CEO warns of worst memory shortage by 2027](#item-4) ⭐️ 8.0/10
5. [Apple Sues OpenAI for Systematic Trade Secret Theft](#item-5) ⭐️ 8.0/10
6. [U-Boot bootloader flaws allow code execution before OS boot](#item-6) ⭐️ 8.0/10
7. [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna Tiers](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0 Released: MRv2 Default, PagedAttention Removed](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 makes Model Runner V2 (MRv2) the default execution path for all dense models and removes the legacy PagedAttention implementation. The release also adds new models like LLaVA-OneVision-2 and GLM-5, a Streaming Parser Engine, and support for dynamic speculative decoding. This release marks a significant architectural shift for vLLM, improving performance and modularity, which will benefit the many developers and organizations relying on vLLM for LLM inference. The removal of PagedAttention and the maturity of MRv2 signal a cleaner, faster codebase. Model Runner V2 now handles all dense models, and the Transformers modeling backend has become as fast as native vLLM. New features include universal speculative decoding for heterogeneous vocabularies and a Rust frontend with HTTPS/mTLS support.

github · khluu · Jul 11, 20:06

**Background**: PagedAttention is a memory-efficient attention algorithm used by vLLM since its inception, while Model Runner V2 is a redesigned execution core that separates CPU scheduling from GPU execution using GPU-native Triton kernels. The v0.25.0 release transitions fully to MRv2, removing the older PagedAttention backend.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/v0.22.1/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM | vLLM Blog</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#LLM inference`, `#release`, `#performance`, `#open source`

---

<a id="item-2"></a>
## [Humanoid robot performs world's first live pig gallbladder surgery remotely](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

Surgeons remotely controlled a Unitree G1 humanoid robot to perform two minimally invasive gallbladder removals on live pigs, a world first published in Nature. This milestone demonstrates the potential of affordable general-purpose humanoid robots for surgery, which could drastically reduce costs and expand access to remote, rural, or battlefield settings. The Unitree G1 costs about $67,000 with dexterous hands, far less than dedicated surgical robots like da Vinci ($500,000+). However, the system required multiple recalibrations and had latency issues that slowed procedures.

telegram · zaihuapd · Jul 11, 02:29

**Background**: Humanoid robots are designed to mimic human form and movement, making them potentially adaptable to various tasks. Teleoperated surgery allows a surgeon to control a robot from a distance, but most surgical robots are expensive and specialized. This study tested whether a low-cost, general-purpose humanoid could perform delicate operations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10796-x">In vivo feasibility study of humanoid robots in surgery | Nature</a></li>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G 1 _ Humanoid Robot ... | Unitree Robotics</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI in healthcare`

---

<a id="item-3"></a>
## [VultronRetriever Models Achieve #1 on MTEB with Edge Efficiency](https://www.reddit.com/r/MachineLearning/comments/1utmxq8/vultronretriever_family_of_models_released_on/) ⭐️ 8.0/10

The VultronRetriever family of retrieval models has been released on HuggingFace, achieving the number-one ranking on the MTEB leaderboard in each model class, with the 8B Prime model as global #1. These models offer up to 16x smaller index storage and 12x higher throughput compared to previous leaders, enabling state-of-the-art retrieval on edge devices like iPhones fully offline, which could democratize high-precision document retrieval for mobile and low-resource environments. The smallest model, Flash (0.8B), outperforms models up to 5x its size and indexes up to 60 images per minute offline. All models were trained with 0% cross-dataset duplication and 0% eval contamination, and show no overfitting on private MTEB evals.

reddit · r/MachineLearning · /u/madkimchi · Jul 11, 15:22

**Background**: MTEB (Massive Text Embedding Benchmark) is a standard public leaderboard for evaluating embedding models across retrieval, classification, clustering, reranking, and other tasks. The VultronRetriever models are built on the Hydra architecture, which unifies late-interaction retrieval and autoregressive generation in a single vision-language model, allowing efficient offline operation on edge devices.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.vultr.com/vultronretriever">VultronRetriever : Open Visual Document Retrieval Models Built for...</a></li>
<li><a href="https://huggingface.co/spaces/mteb/leaderboard">MTEB Leaderboard - a Hugging Face Space by mteb</a></li>

</ul>
</details>

**Tags**: `#retrieval`, `#embedding`, `#transformers`, `#huggingface`, `#MTEB`

---

<a id="item-4"></a>
## [SK Hynix CEO warns of worst memory shortage by 2027](https://www.reuters.com/world/asia-pacific/sk-hynix-ceo-sees-worst-ever-memory-supply-shortage-2027-says-demand-outstrip-2026-07-10/) ⭐️ 8.0/10

SK Hynix CEO Kwak Noh-jung warned that the global memory industry will face its worst supply shortage in 2027, with demand outstripping supply even after 2030. This prediction signals a prolonged period of tight memory supply, which could drive up prices for DRAM and NAND flash, affecting consumer electronics, data centers, and AI infrastructure. The warning came on the day of SK Hynix's Nasdaq debut, with shares closing up 13.3% at $168.85; the company posted a record operating profit of 47 trillion won in 2025.

telegram · zaihuapd · Jul 11, 00:45

**Background**: SK Hynix is a major global memory manufacturer, producing DRAM and NAND flash widely used in computers, smartphones, and servers. The memory industry is cyclical, with periods of oversupply and shortage driven by demand from PCs, mobile devices, and more recently AI accelerators.

**Tags**: `#半导体`, `#内存`, `#供应链`, `#行业预测`

---

<a id="item-5"></a>
## [Apple Sues OpenAI for Systematic Trade Secret Theft](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) ⭐️ 8.0/10

Apple filed a lawsuit on July 10, 2026, in the U.S. District Court for the Northern District of California against OpenAI, two former employees, and io Products, alleging systematic theft of trade secrets related to hardware design, manufacturing, and supply chain. This lawsuit targets the intersection of AI and hardware, potentially reshaping talent mobility and intellectual property protection in the tech industry. It highlights the escalating competition between Apple and OpenAI as both companies expand into consumer hardware. Apple claims former employee Chang Liu accessed internal networks after departure and downloaded dozens of hardware files, while OpenAI hardware chief Tang Yew Tan allegedly sent supplier data to his personal email and asked job applicants to bring Apple components to interviews.

telegram · zaihuapd · Jul 11, 03:14

**Background**: Trade secrets are confidential business information that provides a competitive edge, such as product designs and manufacturing processes. Apple has long guarded its hardware secrets, while OpenAI, known for AI software, is now pursuing consumer hardware, creating friction.

**Tags**: `#苹果`, `#OpenAI`, `#诉讼`, `#商业机密`, `#硬件`

---

<a id="item-6"></a>
## [U-Boot bootloader flaws allow code execution before OS boot](https://www.bleepingcomputer.com/news/security/new-u-boot-flaws-could-enable-stealthy-firmware-attacks/) ⭐️ 8.0/10

Six vulnerabilities have been discovered in U-Boot's FIT image signature verification, two of which allow arbitrary code execution before the operating system boots, affecting over 50 stable versions since 2013.07. These vulnerabilities enable attackers to bypass secure boot and execute malicious code at the firmware level, potentially compromising devices permanently. Since U-Boot is widely used in embedded systems, servers, and IoT devices, the impact is extensive and remediation depends on vendor firmware updates. The flaws reside in the FIT image parser and affect both verified and unverified boot modes. Patches have been accepted by U-Boot maintainers, but deployment requires integration by hardware vendors; devices no longer supported may never receive fixes.

telegram · zaihuapd · Jul 11, 08:32

**Background**: U-Boot is a widely used open-source bootloader for embedded systems, responsible for initializing hardware and loading the operating system. The Flattened Image Tree (FIT) format packages boot images with hashes and signatures to ensure integrity and authenticity. Baseboard Management Controllers (BMCs) enable remote firmware updates, making remote exploitation possible without physical access.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.u-boot.org/en/latest/usage/fit/index.html">Flat Image Tree (FIT) — Das U-Boot unknown version documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface">Intelligent Platform Management Interface - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#bootloader`, `#vulnerability`, `#firmware`, `#U-Boot`

---

<a id="item-7"></a>
## [OpenAI Launches GPT-5.6 Series with Sol, Terra, Luna Tiers](https://t.me/zaihuapd/42497) ⭐️ 8.0/10

OpenAI has officially released the GPT-5.6 series, introducing three tiers: Sol for top performance, Terra for balanced cost and performance, and Luna for high-concurrency low-cost scenarios. The series features significant improvements in code generation, reasoning, design, research, and cybersecurity, along with new capabilities such as max/ultra reasoning, multi-agent collaboration, and programmatic tool calling. This release represents a major advancement in AI model capabilities, offering developers and enterprises more flexible options optimized for different use cases and budgets. The introduction of multi-agent collaboration and programmatic tool calling could significantly reduce complexity and cost for building AI-powered applications. The GPT-5.6 series includes three tiers: Sol (flagship high-performance), Terra (balanced), and Luna (cost-effective for high throughput), with GPT-5.6 defaulting to Sol. New features include max/ultra reasoning effort levels, multi-agent collaboration, and programmatic tool calling that allows the model to orchestrate tools via code instead of API round-trips.

telegram · zaihuapd · Jul 11, 13:34

**Background**: GPT-5.6 is the latest iteration of OpenAI's large language model series, following GPT-4 and GPT-4o. The tiered approach mirrors strategies seen in other AI labs, aiming to serve diverse needs from resource-intensive tasks to lightweight, high-concurrency applications. Multi-agent collaboration enables multiple specialized AI agents to work together on complex tasks, while programmatic tool calling allows models to execute tool uses through code for greater efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling">Programmatic tool calling - Claude Platform Docs</a></li>
<li><a href="https://www.toolcolumn.com/learn/gpt-5-6-max-vs-ultra">GPT-5.6 Max vs Ultra: What Actually Changes? | ToolColumn</a></li>
<li><a href="https://www.ibm.com/think/topics/multi-agent-collaboration">What is Multi-Agent Collaboration? | IBM</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#language models`, `#performance`

---