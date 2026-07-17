---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 32 items, 8 important content pieces were selected

---

1. [First atmosphere detected on rocky exoplanet LHS 1140b in habitable zone](#item-1) ⭐️ 9.0/10
2. [Firefox compiled to WebAssembly runs inside another browser](#item-2) ⭐️ 9.0/10
3. [Huawei Unveils Ascend 950 SuperNode with 6.7x Nvidia Compute](#item-3) ⭐️ 9.0/10
4. [AWS Billing Glitch Shows $1.7 Billion Estimated Bill](#item-4) ⭐️ 8.0/10
5. [Kimi K3 analysis reveals tokenization issues via pelican benchmark](#item-5) ⭐️ 8.0/10
6. [Open Source AI Overtakes Closed Models](#item-6) ⭐️ 8.0/10
7. [Apple Sends Legal Letters to OpenAI Employees Over Poaching](#item-7) ⭐️ 8.0/10
8. [US Lawmakers Seek Ban on Chinese Memory Chips in Allied Supply Chains](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [First atmosphere detected on rocky exoplanet LHS 1140b in habitable zone](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 9.0/10

Astronomers using the James Webb Space Telescope (JWST) have detected an atmosphere on LHS 1140b, a rocky super-Earth located 48 light-years away in the habitable zone of its red dwarf star. This marks the first confirmed atmosphere on a potentially Earth-like planet in a habitable zone. This discovery demonstrates JWST's ability to characterize atmospheres of small, rocky exoplanets, bringing us closer to finding signs of habitability or life beyond our solar system. It also challenges assumptions about red dwarf planets retaining atmospheres despite intense stellar radiation. LHS 1140b has a mass 5.6 times Earth's and orbits its star every 24.7 days at a distance of 0.0946 AU. JWST transmission spectroscopy ruled out a mini-Neptune composition and revealed an atmosphere consistent with a water world or snowball planet scenario.

hackernews · neversaydie · Jul 17, 14:06 · [Discussion](https://news.ycombinator.com/item?id=48947560)

**Background**: Exoplanet atmospheres are studied via transit spectroscopy, where starlight filters through the planet's atmosphere during a transit, revealing absorption fingerprints of gases. JWST's infrared sensitivity and resolution enable such studies for Earth-sized worlds around M-dwarf stars. LHS 1140b was discovered in 2017 and is one of the most promising targets for atmospheric characterization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/science/2026/jul/16/atmosphere-lhs-1140b-exoplanet-could-water-scientists">Earth-like exoplanet found to have an atmosphere | Space | The Guardian</a></li>
<li><a href="https://science.nasa.gov/exoplanet-catalog/lhs-1140-b/">LHS 1140 b - NASA Science</a></li>

</ul>
</details>

**Discussion**: Community reactions include skepticism about red dwarf habitability due to stellar activity, but one commenter noted that JWST emission spectroscopy ruled out a mini-Neptune, confirming the atmosphere. Others discussed future probes and solar lens telescopes, and a duplicate submission was flagged.

**Tags**: `#exoplanets`, `#atmosphere`, `#JWST`, `#astronomy`, `#space exploration`

---

<a id="item-2"></a>
## [Firefox compiled to WebAssembly runs inside another browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the full Firefox browser to WebAssembly, creating a 233MB gecko.wasm file that can run inside another browser like Chrome, with all network traffic proxied through the Wisp protocol. This is a groundbreaking demonstration of browser portability, enabling a full browser to run entirely client-side in another browser, with implications for cloud browsing, cross-platform testing, and isolation. It also highlights the use of AI-assisted programming to achieve such a complex port. The project used $25,000 worth of Claude Opus and Fable tokens but reduced costs via a Claude Max subscription plan. All network traffic is routed through a WebSocket-based Wisp proxy, and the team had to scale servers to handle Hacker News traffic. End-to-end encryption is supported for HTTPS sites.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly is a binary instruction format that allows code from languages like C++ to run in web browsers at near-native speed. Normally, browsers are standalone applications; running one inside another requires porting the entire browser engine (Gecko) to WebAssembly, which is extremely challenging because browsers need to handle networking, rendering, and system calls. This project overcomes the networking limitation by proxying all connections through a server using the Wisp protocol, since WebAssembly code in a browser cannot open arbitrary TCP connections.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wire_protocol">Wire protocol</a></li>

</ul>
</details>

**Tags**: `#WebAssembly`, `#Firefox`, `#browser`, `#web development`, `#portability`

---

<a id="item-3"></a>
## [Huawei Unveils Ascend 950 SuperNode with 6.7x Nvidia Compute](https://www.ithome.com/0/978/019.htm) ⭐️ 9.0/10

At WAIC 2026, Huawei publicly demonstrated the Ascend 950 supernode (Atlas 950 SuperPoD) for the first time, claiming it delivers 1 EFLOPS FP8 and 2 EFLOPS FP4 compute power, which is 6.7 times the total compute of Nvidia's NVL144 system with 144 GPUs. This announcement signals a major leap in AI hardware competition, as Huawei claims to surpass Nvidia's comparable system by a wide margin, potentially reshaping the AI compute landscape and reducing dependency on foreign chips. The supernode scales to 1024 Ascend 950 cards via Huawei's self-developed UnifiedBus interconnect and supernode architecture, featuring 256 TB of globally unified memory. The Ascend 384 supernode has already been commercially deployed in over 750 sets across various industries.

telegram · zaihuapd · Jul 17, 10:27

**Background**: Supernodes are high-density AI compute clusters that integrate dozens or hundreds of accelerators via high-speed interconnects, enabling large model training. Huawei's UnifiedBus is a proprietary interconnect protocol designed to replace PCIe, NVLink, and RDMA, supporting up to 8192 cards without bandwidth loss. FP8 and FP4 are reduced-precision floating-point formats that accelerate AI inference and training while saving memory.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/灵衢/66774401">灵衢 - 百度百科</a></li>
<li><a href="https://cloud.ofweek.com/news/2025-12/ART-178800-8420-30675427.html">从炫技到务实， 超 节 点 的祛魅时刻 - OFweek云计算网</a></li>
<li><a href="https://huggingface.co/Winnougan/Krea-2-Base-Turbo-NVFP4-FP8-INT8">Winnougan/Krea-2-Base-Turbo-NVFP4- FP 8 -INT8 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Huawei`, `#Ascend`, `#supernode`, `#WAIC`

---

<a id="item-4"></a>
## [AWS Billing Glitch Shows $1.7 Billion Estimated Bill](https://news.ycombinator.com/item?id=48945241) ⭐️ 8.0/10

AWS customers reported estimated bills reaching $1.7 billion due to a billing system glitch, identified as a unit error where bytes were charged instead of gigabytes. This glitch caused widespread alarm and distrust, highlighting the critical importance of accurate billing in cloud services, as even minor unit errors can lead to astronomical figures. The error arises from a unit mismatch: the billing system defaults to bytes for storage metering, while the intended unit was gigabytes, resulting in a billion-fold overestimation.

hackernews · nprateem · Jul 17, 09:42

**Background**: AWS billing uses metering data from services to compute estimated charges. A unit error means the numerical value is misinterpreted (e.g., bytes vs. GB), leading to wildly inflated estimates. Such errors are typically corrected by AWS support and do not result in actual charges.

**Discussion**: Community comments show multiple users received similarly inflated billing alerts, with some sharing past experiences. A former AWS engineer confirmed the unit error pattern, and many expressed frustration along with dark humor about the magnitude.

**Tags**: `#AWS`, `#billing`, `#incident`, `#cloud`, `#cost`

---

<a id="item-5"></a>
## [Kimi K3 analysis reveals tokenization issues via pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 8.0/10

Simon Willison's analysis of Kimi K3 using the pelican benchmark exposed tokenization anomalies, including a suspected hidden 85-token system prompt, and highlighted the model's value in probing quality versus cost versus speed. This analysis demonstrates that informal benchmarks like the pelican test can uncover subtle but important model behaviors that standard evaluations miss, affecting how developers choose and deploy LLMs. Kimi K3, a 2.8-trillion-parameter open-source model from Moonshot AI, exhibited unusual token counts—86 tokens for 'hi' and 95 for the pelican prompt—compared to 10 tokens for OpenAI and Anthropic models, suggesting an 85-token hidden system prompt.

hackernews · droidjj · Jul 17, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48947717)

**Background**: The pelican benchmark, created by Simon Willison in late 2024, asks LLMs to 'Generate an SVG of a pelican riding a bicycle' and evaluates their output quality. It has become a popular informal test for comparing model capabilities. Kimi K3 is the largest open-source model to date, released by Moonshot AI in July 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark)</a></li>
<li><a href="https://huggingface.co/spaces/victor/pelican-benchmark">Pelican Benchmark - a Hugging Face Space by victor</a></li>

</ul>
</details>

**Discussion**: Community comments debated whether the pelican prompt is part of training data, with one user noting that personal blog content appears in LLM training. Another commenter provided a cost-speed comparison showing Kimi K3 is 5x cheaper but 2x slower than Opus and Fable models.

**Tags**: `#AI`, `#LLM`, `#benchmarks`, `#tokenization`, `#machine learning`

---

<a id="item-6"></a>
## [Open Source AI Overtakes Closed Models](https://stateofopensource.ai/) ⭐️ 8.0/10

A new report on the state of open source AI reveals that open models now command 63% of token processing on OpenRouter, up from 40% four months ago, with daily token volume increasing nearly 5x from 888B to 4.19T. This rapid shift undermines closed AI leaders like OpenAI and Anthropic, who face high training costs and may lose relevance as hyperscalers and Apple adopt open models without licensing fees. The report is criticized for being AI-generated and lacking coherent analysis, with charts only loosely connected to text. Community members also note that the term 'open' has been diluted, as few models release full training data and methodology.

hackernews · rellem · Jul 17, 14:31 · [Discussion](https://news.ycombinator.com/item?id=48947825)

**Background**: Open source AI models, such as Meta's Llama and Mistral, are released with permissive licenses allowing free use and modification. In contrast, closed models like GPT-4 and Claude are proprietary and require API fees. The debate over openness versus control has intensified as performance gaps narrow.

**Discussion**: Comments are mixed: some predict open models will kill closed players (babblingfish), others cite data showing explosive growth (GodelNumbering). Critics find the report poorly written (hughw, Catloafdev) and worry that the term 'open' is being diluted (semiquaver).

**Tags**: `#open source`, `#AI`, `#machine learning`, `#models`, `#industry analysis`

---

<a id="item-7"></a>
## [Apple Sends Legal Letters to OpenAI Employees Over Poaching](https://www.ft.com/content/1b8c9d52-88a9-426b-ba47-f1811f859166) ⭐️ 8.0/10

Apple has sent legal letters to dozens of OpenAI employees, accusing them of poaching and misappropriating trade secrets. This legal escalation highlights the intense competition for AI talent and could set precedents for how trade secrets are protected when employees move between rival firms. The letters are document retention letters, a standard practice, but their timing suggests Apple is preparing for potential litigation. Some commentators believe Apple likely has strong evidence to support its claims.

hackernews · merksittich · Jul 17, 12:02 · [Discussion](https://news.ycombinator.com/item?id=48946303)

**Background**: Talent poaching is common in the tech industry, especially in AI. Apple and OpenAI are increasingly competing in AI, with Apple developing its own AI capabilities and OpenAI leading in generative AI. Trade secrets like proprietary algorithms and hardware designs are highly valuable.

**Discussion**: Commenters noted that document retention letters are standard industry practice, with some arguing Apple is late to issue them. Others speculated that Apple likely has strong evidence, while one commenter drew parallels to OpenAI's own history of using third-party content.

**Tags**: `#Apple`, `#OpenAI`, `#legal`, `#talent poaching`, `#tech industry`

---

<a id="item-8"></a>
## [US Lawmakers Seek Ban on Chinese Memory Chips in Allied Supply Chains](https://www.tomshardware.com/pc-components/dram/lawmakers-want-us-government-to-ban-memory-chips-from-china-even-in-allied-supply-chains-citing-unacceptable-risk-to-national-economic-and-supply-chain-security) ⭐️ 8.0/10

US House China Committee Chair John Moolenaar and Representative George Whitesides sent a letter to Commerce Secretary Howard Lutnick urging a ban on US companies purchasing Chinese memory chips, including pushing to add CXMT to the entity list and imposing further restrictions on YMTC. This move could severely impact global memory supply chains and AI infrastructure, as Chinese memory manufacturers like CXMT and YMTC are key players in DRAM and NAND markets, and a ban could force US allies to choose between security concerns and supply continuity. Lawmakers cite national economic and supply chain security risks, alleging that Chinese memory chip purchases directly fund the PLA's dual-use technology development; they also call for coordination with Japan, South Korea, and the EU to prevent Chinese manufacturers from establishing footholds in allied supply chains.

telegram · zaihuapd · Jul 17, 14:00

**Background**: ChangXin Memory Technologies (CXMT) is a Chinese DRAM manufacturer, while Yangtze Memory Technologies Co. (YMTC) focuses on NAND flash memory. Both companies have been accused of close ties to the Chinese military and have faced prior US trade restrictions. The US has increasingly sought to limit China's access to advanced semiconductor technology and prevent its integration into global supply chains, especially for AI-related components.

<details><summary>References</summary>
<ul>
<li><a href="https://m.chinapp.com/pinpai/355427.html">长 鑫 存 储 CXMT 品牌 存 储 器怎么样- 长 鑫 存 储 CXMT ...</a></li>
<li><a href="http://chip.com.cn/ymtc.html">长 江 存 储 ( YMTC ) - Glochip.com</a></li>
<li><a href="https://developer.aliyun.com/article/1100149">长 江 存 储 YMTC Xtacking技术演进与芯片级解密-开发者社区-阿里云</a></li>

</ul>
</details>

**Tags**: `#芯片`, `#地缘政治`, `#供应链安全`, `#存储芯片`, `#AI基础设施`

---