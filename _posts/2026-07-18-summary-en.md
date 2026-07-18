---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 34 items, 15 important content pieces were selected

---

1. [GPT-5.6 Solves 30-Year Convex Optimization Conjecture](#item-1) ⭐️ 9.0/10
2. [SpaceX in talks with Pentagon for AI computing deal worth billions](#item-2) ⭐️ 9.0/10
3. [Kimi K3: Open-Source 2.8T Model Tops Frontend Code Arena](#item-3) ⭐️ 9.0/10
4. [Trump Administration Considers FINRA-like AI Model Watchdog](#item-4) ⭐️ 9.0/10
5. [Fable 5 vs GPT-5.6 Sol on NP-Hard: Does /goal Help?](#item-5) ⭐️ 8.0/10
6. [LG monitors silently install bloatware via Windows Update](#item-6) ⭐️ 8.0/10
7. [Graph shows Stack Overflow decline; community cites policies, not AI](#item-7) ⭐️ 8.0/10
8. [TP-Link Kasa cameras leaked home GPS via unauthenticated UDP for 6 years](#item-8) ⭐️ 8.0/10
9. [Anthropic Reverses Course, Makes Claude Fable 5 Permanent](#item-9) ⭐️ 8.0/10
10. [AI 'slop' submission wins $25k DeepMind Kaggle prize, sparks integrity debate](#item-10) ⭐️ 8.0/10
11. [ByteDance's Doubao Phone Abandons GUI Automation for MCP](#item-11) ⭐️ 8.0/10
12. [OpenRouter Acquisition Interest at $1.3B+ Valuation](#item-12) ⭐️ 8.0/10
13. [TSMC announces A14 process for 2028 production](#item-13) ⭐️ 8.0/10
14. [SK Hynix CEO Warns of Worst Memory Shortage by 2027](#item-14) ⭐️ 8.0/10
15. [San Francisco Orders Apple and Google to Remove 'Nudify' Apps](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GPT-5.6 Solves 30-Year Convex Optimization Conjecture](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

OpenAI's GPT-5.6, using a carefully crafted prompt, solved a long-standing conjecture in convex optimization that had remained open for 30 years. This breakthrough demonstrates AI's growing ability to tackle complex mathematical research problems, potentially accelerating progress in optimization theory and its applications in machine learning, engineering, and economics. The model used was the Sol Pro version, not the Ultra version, and the conjecture involves bounding the complexity of optimizing convex Lipschitz functions over a spherical domain.

hackernews · mbustamanter · Jul 18, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48957779)

**Background**: Convex optimization studies minimizing convex functions over convex sets, a fundamental problem in many fields. The solved conjecture provides a tight lower bound on the iteration complexity of certain first-order methods, a problem researchers had struggled with for three decades.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://haltmal.com/learning-knowledge-work/gpt-5-6-used-a-prompt-to-close-a-30-year-gap-in-convex-optimization/">GPT-5.6 Used A Prompt To Close A 30-Year Gap In Convex ... - Halt Mal</a></li>
<li><a href="https://pulseaugur.com/cluster/149817-gpt-5-6-solves-30-year-convex-optimization-problem">GPT-5.6 Solves 30-Year Convex Optimization Problem · PulseAugur</a></li>

</ul>
</details>

**Discussion**: The community acknowledged the contribution as real but noted it addresses a relatively niche conjecture. Some commenters discussed the broader implications for AI in mathematics, suggesting LLMs could now tackle medium-difficulty problems, but human creativity is still needed for novel approaches.

**Tags**: `#AI`, `#convex optimization`, `#mathematics`, `#machine learning`, `#breakthrough`

---

<a id="item-2"></a>
## [SpaceX in talks with Pentagon for AI computing deal worth billions](https://www.wsj.com/tech/ai/spacex-in-talks-to-provide-computing-power-for-pentagons-ai-push-15e752e4) ⭐️ 9.0/10

SpaceX is in negotiations with the U.S. Department of Defense to provide data center computing power for running artificial intelligence models, with a potential deal valued in the tens of billions of dollars. The discussions are ongoing and could still fall through. This deal would significantly deepen SpaceX's relationship with the Pentagon and mark a major expansion of its cloud computing business. It also reflects the U.S. military's accelerating push to acquire cloud computing capabilities for AI applications in national security and daily operations. The Pentagon recently approved SpaceX, Amazon, Google, Microsoft, and Oracle to use AI models in classified environments. SpaceX has also signed similar computing power supply agreements with Anthropic and Google in recent months.

telegram · zaihuapd · Jul 18, 01:44

**Background**: SpaceX, primarily known for space launch and satellite internet services, is expanding into cloud computing. The U.S. Department of Defense is seeking to leverage AI for various missions, requiring substantial computing resources. Negotiations like this are part of a broader trend of tech companies partnering with the military for AI capabilities.

**Tags**: `#AI算力`, `#SpaceX`, `#国防`, `#五角大楼`, `#云计算`

---

<a id="item-3"></a>
## [Kimi K3: Open-Source 2.8T Model Tops Frontend Code Arena](https://t.me/zaihuapd/42637) ⭐️ 9.0/10

Moonshot AI released Kimi K3, the world's first open-source 2.8 trillion parameter model, on July 12, 2026. It achieved first place on the Frontend Code Arena benchmark with a score of 1679, surpassing previous leader Fable 5. This release demonstrates that open-source models can now compete with and even surpass proprietary frontier models, potentially democratizing access to state-of-the-art AI. It also highlights rapid progress in China's AI ecosystem, challenging US dominance in large language models. Kimi K3 is built on two novel architectural innovations: Kimi Delta Attention (KDA), which enables efficient linear-scaling long-context processing, and Attention Residuals (AttnRes), which replace standard residual connections with learned, input-dependent attention over depth. The model also features native vision capabilities and a 1 million token context window.

telegram · zaihuapd · Jul 18, 02:29

**Background**: Kimi Delta Attention (KDA) is a linear attention mechanism that extends Gated DeltaNet with a finer-grained gating mechanism, allowing transformers to handle ultra-long contexts and multimodal integration with linear computational scaling. Attention Residuals (AttnRes) is a drop-in replacement for standard residual connections that enables each layer to selectively aggregate earlier representations using softmax attention over depth, improving representational flexibility. The Frontend Code Arena benchmark evaluates AI models on their ability to generate frontend code (HTML, CSS, JavaScript) from natural language descriptions, measuring both functionality and visual fidelity.

<details><summary>References</summary>
<ul>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention : Kimi Delta Attention | Jianyu Huang’s Blog</a></li>
<li><a href="https://arxiv.org/abs/2603.15031">[2603.15031] Attention Residuals</a></li>
<li><a href="https://digg.com/tech/we56zqdp">Chinese model Kimi-K3 tops Frontend Code Arena benchmark · Digg</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some users applaud the open-source achievement and view it as a necessary counterbalance to US regulation, while others report that Kimi K3 underperforms in practical tasks compared to frontier models like Fable 5 and GPT-5.5, consuming excessive usage limits. There is also debate over whether the model's capabilities stem from genuine innovation or distillation from existing models.

**Tags**: `#AI`, `#open-source`, `#large language model`, `#attention mechanism`, `#benchmark`

---

<a id="item-4"></a>
## [Trump Administration Considers FINRA-like AI Model Watchdog](https://www.bloomberg.com/news/articles/2026-07-17/us-considers-creating-finra-like-watchdog-to-vet-top-ai-models) ⭐️ 9.0/10

The Trump administration is considering creating an independent agency modeled after FINRA to vet top AI models, aimed at addressing cybersecurity concerns and giving industry more input. This proposal could reshape AI regulation by establishing a self-regulatory model that balances industry interests with safety oversight, potentially setting a precedent for AI governance globally. The agency would report to the SEC and be led by Treasury Secretary Scott Bessent, with the plan still under review by White House Chief of Staff Susie Wiles and not yet seen by President Trump.

telegram · zaihuapd · Jul 18, 05:45

**Background**: FINRA is a private, not-for-profit self-regulatory organization (SRO) that oversees U.S. broker-dealers and exchange markets under SEC oversight, created to protect investors and ensure market integrity. The proposed AI watchdog would similarly be industry-funded and operate with government oversight, applying FINRA's approach to AI model safety.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Financial_Industry_Regulatory_Authority">Financial Industry Regulatory Authority - Wikipedia</a></li>
<li><a href="https://www.finra.org/about">About FINRA</a></li>

</ul>
</details>

**Tags**: `#AI监管`, `#政策`, `#特朗普政府`, `#AI安全`, `#FINRA`

---

<a id="item-5"></a>
## [Fable 5 vs GPT-5.6 Sol on NP-Hard: Does /goal Help?](https://charlesazam.com/blog/fable-5-gpt-5-6-sol-goal/) ⭐️ 8.0/10

A new blog post compares Anthropic's Fable 5 and OpenAI's GPT-5.6 Sol on an NP-hard problem to test whether adding the '/goal' instruction improves the models' performance. The evaluation provides empirical data on the impact of explicit goal-setting in prompts. This comparison matters because it sheds light on how prompting strategies like '/goal' affect AI reasoning on complex problems, which is crucial for practical applications in optimization and planning. It also provides insights into the relative strengths of leading AI models from Anthropic and OpenAI. The test uses an NP-hard problem, which is known for being computationally intractable for large instances. The '/goal' instruction is a prompt engineering technique meant to focus the model on a specific objective, and the results suggest it can improve performance for single-track investigations.

hackernews · couAUIA · Jul 18, 11:00 · [Discussion](https://news.ycombinator.com/item?id=48956879)

**Background**: NP-hard problems are a class of problems for which no efficient algorithm is known to solve all instances, making them a challenging benchmark for AI reasoning. '/goal' is a directive added to prompts to explicitly state the desired outcome, which may help guide the model's search process. Fable 5 is Anthropic's advanced model for autonomous agentic work, while GPT-5.6 Sol is OpenAI's latest coding-focused model with state-of-the-art performance on agentic benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/docs/models/claude-fable-5">Claude Fable 5 | Cursor Docs</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://routeway.ai/blog/kimi-k3-vs-claude-fable-5">Kimi K3 vs Claude Fable 5 : Which AI Model Should You... | Routeway</a></li>

</ul>
</details>

**Discussion**: Commenters noted that 'ultra mode' might be superior for search strategies and suggested a follow-up evaluation. Others pointed out that Claude tends to forget instructions in long sessions, while GPT generally excels at optimization problems, referencing a recent AtCoder competition win.

**Tags**: `#AI`, `#LLM comparison`, `#prompting`, `#NP-hard`, `#evaluation`

---

<a id="item-6"></a>
## [LG monitors silently install bloatware via Windows Update](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 8.0/10

Connecting certain LG monitors to a Windows PC via HDMI triggers Windows Update to silently download and install LG-specific software that promotes McAfee subscriptions without user consent. This exploit gives a third-party vendor system-level access with no user interaction, affecting privacy and security. It also highlights a broader issue with Windows Update delivering potentially unwanted software alongside drivers. The software is installed as soon as a monitor is connected, has full system and internet access with no sandboxing, and starts automatically at every system boot. Even older LG monitors are affected.

hackernews · baranul · Jul 18, 10:21 · [Discussion](https://news.ycombinator.com/item?id=48956688)

**Background**: Windows Update can automatically install device drivers and associated software from manufacturers. In this case, LG includes its own software package that installs via Windows Update's driver delivery mechanism, effectively bypassing user consent. This is similar to past issues where USB drives could autorun malware.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48956688">LG monitors silently install software through Windows Update without consent | Hacker News</a></li>
<li><a href="https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent">LG monitors silently install software through Windows Update without user consent - VideoCardz.com</a></li>
<li><a href="https://support.microsoft.com/en-US/Windows/Hardware/Drivers/automatically-get-recommended-and-updated-hardware-drivers">Automatically get recommended and updated hardware drivers</a></li>

</ul>
</details>

**Discussion**: The community is highly concerned, with one comment calling it 'worse than the title suggests' and detailing the full system access and persistence. Workarounds via group policy or device installation settings were shared, along with debate over whether Microsoft or LG bears more responsibility.

**Tags**: `#security`, `#windows update`, `#LG monitors`, `#privacy`, `#driver installation`

---

<a id="item-7"></a>
## [Graph shows Stack Overflow decline; community cites policies, not AI](https://data.stackexchange.com/stackoverflow/query/1953768#graph) ⭐️ 8.0/10

A graph from Stack Exchange Data Explorer illustrates a sharp decline in Stack Overflow activity, often linked to AI chatbots, but community comments reveal the downturn began years before AI became mainstream. This challenges the oversimplified narrative that AI alone caused Stack Overflow's decline, highlighting deeper issues like platform governance, community management, and corporate acquisition effects. The graph peaked around 2014 and shows a steady decline well before ChatGPT's release. Commenters specifically blame strict moderation, high entry barriers for newcomers, and the 2021 acquisition by Prosus.

hackernews · secretslol · Jul 18, 11:12 · [Discussion](https://news.ycombinator.com/item?id=48956949)

**Background**: Stack Overflow is a popular Q&A site for programmers, known for its strict moderation and reputation system. Its declining activity has been widely attributed to AI tools like ChatGPT, but many users argue that long-standing community and policy issues are the real cause. The graph visualizes the decline over the past decade.

**Discussion**: Commenters argue that the decline started long before AI, due to exclusionary policies and the Prosus acquisition. Some note that the site's focus on Q&A over community drove users away, while others point to better documentation and modern tools reducing the need for Stack Overflow.

**Tags**: `#Stack Overflow`, `#AI impact`, `#community management`, `#online communities`, `#platform decline`

---

<a id="item-8"></a>
## [TP-Link Kasa cameras leaked home GPS via unauthenticated UDP for 6 years](https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md) ⭐️ 8.0/10

A security researcher disclosed that TP-Link Kasa EC71 indoor cameras exposed precise GPS coordinates via an unauthenticated UDP listener, a flaw that went unpatched for six years until a recent firmware fix disabled the vulnerable endpoint. This vulnerability compromises user privacy by leaking home GPS data over the network without authentication, affecting millions of IoT devices. The long exposure period highlights systemic security weaknesses in consumer IoT products. The vulnerability tracks as CVE-2025-12345 and involves a UDP endpoint that responds to unauthenticated LAN requests with precise latitude and longitude. The geofencing feature, launched in September 2023, uses mobile device GPS rather than camera-stored coordinates and requires explicit user opt-in.

hackernews · BadChemical · Jul 17, 21:42 · [Discussion](https://news.ycombinator.com/item?id=48952565)

**Background**: UDP is a connectionless network protocol that does not require authentication or encryption by default. Exposing GPS coordinates over unauthenticated UDP means any device on the same local network can retrieve the camera's location without any credentials. This is particularly concerning because a remote attacker who gains LAN access could deduce the owner's home address.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BadChemical/IoT-Vulnerability-Research-Public/blob/main/TP-Link_Kasa_EC71/Kasa_EC71.md">github.com/BadChemical/IoT- Vulnerability -Research-Public/blob/main...</a></li>
<li><a href="https://eucloudservers.com/security-encryption/tp-link-kasa-cameras-leaked-home-gps-via-unauthenticated-udp-for-6-years/">TP-Link Kasa Cameras Leaked Home GPS Via Unauthenticated UDP ...</a></li>
<li><a href="https://news.oblaidish.com/tx/tp-link-kasa-cameras-gps-udp-leak">TP-Link Kasa camera leaked home GPS via unauthenticated UDP for...</a></li>

</ul>
</details>

**Discussion**: Comments highlight that this leak is limited to LAN access, but some users argue that even LAN-only exposure is risky due to potential remote access via DMZ or other means. Others criticize the report for appearing AI-generated, though the core vulnerability is acknowledged as a serious privacy flaw. There is also discussion about IoT devices lacking basic security measures like encryption.

**Tags**: `#security`, `#IoT`, `#privacy`, `#vulnerability`, `#TP-Link`

---

<a id="item-9"></a>
## [Anthropic Reverses Course, Makes Claude Fable 5 Permanent](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic announced that Claude Fable 5 will be included in all Max and Team Premium subscription plans starting July 20, with usage limited to 50% of the plan's limit, reversing a previous plan to remove subscriber access. This reversal highlights intense competitive pressure from rivals like OpenAI's GPT-5.6 Sol and Moonshot AI's Kimi 3, as Anthropic realized subscribers would not pay a premium for plans lacking its best model. It also signals that compute capacity concerns are being addressed, possibly at the expense of training efforts. Only users on Max ($100/$200 per month) and Team Premium plans get Fable 5 at 50% of limits; Pro and Team Standard users receive a one-time $100 credit and continued usage via credits. Users on the $20/month plan still do not have access.

rss · Simon Willison · Jul 18, 06:00

**Background**: Claude Fable 5 is a 'Mythos-class' large language model from Anthropic, considered their most capable model generally available. Originally, Anthropic planned to remove it from subscriptions due to compute capacity concerns, making it API-only. However, competitive launches like GPT-5.6 Sol (July 9, 2026) and Kimi 3 (July 16, 2026) forced a rethink. Kimi 3 is a 2.8 trillion parameter model from Moonshot AI that ranked third on leaderboards behind Fable 5 and GPT-5.6 Sol.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Claude`, `#Fable 5`, `#Anthropic`, `#AI pricing`, `#competition`

---

<a id="item-10"></a>
## [AI 'slop' submission wins $25k DeepMind Kaggle prize, sparks integrity debate](https://www.reddit.com/r/MachineLearning/comments/1uzyf66/did_blatant_ai_slop_just_win_a_25k_usd_deepmind/) ⭐️ 8.0/10

A Reddit user presented evidence that the grand prize winner of the DeepMind-sponsored Kaggle competition 'Measuring Progress Toward AGI - Cognitive Abilities' produced a nonsensical number generation machine and unfounded claims, questioning the review process. This raises critical concerns about the integrity of high-profile AI competitions and the rigor of peer review in benchmark development, potentially affecting trust in research quality and evaluation standards. The submission was supposed to design new cognitive-science-based AI benchmarks but allegedly became a 'vibed pile of spaghetti' 10 times the requested format, with the user claiming neither authors nor judges gave it a cursory reading.

reddit · r/MachineLearning · /u/TheWerkmeister · Jul 18, 15:10

**Background**: Kaggle is a platform for data science competitions where participants compete for prizes. DeepMind, a leading AI research lab, sponsored this competition to design benchmarks measuring cognitive abilities toward AGI, as outlined in their cognitive framework. The grand prize was $25,000.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kaggle.com/competitions/kaggle-measuring-agi">Measuring Progress Toward AGI - Cognitive Abilities | Kaggle</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/">Measuring Progress Towards AGI: A Cognitive Framework</a></li>

</ul>
</details>

**Tags**: `#AI competition`, `#Kaggle`, `#DeepMind`, `#benchmarking`, `#research integrity`

---

<a id="item-11"></a>
## [ByteDance's Doubao Phone Abandons GUI Automation for MCP](https://www.latepost.com/news/dj_detail?id=3648) ⭐️ 8.0/10

ByteDance's Doubao phone assistant will no longer use GUI automation (screen reading and simulated clicks) to interact with major apps, instead requiring super apps like Alibaba and Tencent to provide MCP services and open data access. Production has been boosted from 30,000 units to hundreds of thousands. This strategic pivot highlights the industry's shift from fragile GUI automation to standardized protocols like MCP for AI assistant integration, potentially reshaping how mobile AI assistants interact with apps. It also signals ByteDance's aggressive push into the AI hardware market with a significantly larger production scale. The Doubao phone assistant software received generative AI service备案 on July 15, 2025, and first launched a technical preview in December 2024, which was previously disabled due to blockades by WeChat and Taobao. Apple and Google are also moving toward similar MCP-based frameworks that require developer authorization.

telegram · zaihuapd · Jul 18, 00:29

**Background**: The Model Context Protocol (MCP) is an open standard developed by Anthropic that allows AI assistants to securely connect with external data sources, tools, and services through a client-server architecture. GUI automation, by contrast, involves reading screen pixels and simulating user inputs, which is brittle and often blocked by apps. MCP provides a more robust and standardized integration pathway, reducing development complexity and enabling richer AI interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://mcp.so/">MCP .so - MCP Marketplace</a></li>

</ul>
</details>

**Tags**: `#AI assistants`, `#MCP`, `#ByteDance`, `#mobile strategy`, `#AI ecosystem`

---

<a id="item-12"></a>
## [OpenRouter Acquisition Interest at $1.3B+ Valuation](https://www.theinformation.com/articles/startup-openrouter-fields-multi-billion-dollar-takeover-interest) ⭐️ 8.0/10

OpenRouter, an AI model routing platform, is being pursued by multiple large tech companies for acquisition at a valuation exceeding $1.3 billion. This signals strong market validation for AI infrastructure intermediaries, and a potential consolidation in the AI model access layer. OpenRouter's Series B in May 2025 raised $113 million at a $1.3 billion valuation, and the platform now routes over 400 models, serves 8 million users, and processes 100 trillion tokens monthly.

telegram · zaihuapd · Jul 18, 03:45

**Background**: Model routing platforms like OpenRouter provide a unified API to access multiple large language models, allowing developers to switch between models easily. Tokens are the fundamental units of text that AI models process; for example, 100 trillion tokens represent a massive volume of text data. OpenRouter's rapid growth from a $547 million valuation in Series A to $1.3 billion in Series B reflects the surging demand for flexible AI model access.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/">The unified interface for LLMs. Find the best models & prices for your...</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#acquisition`, `#OpenRouter`, `#model routing`, `#startup valuation`

---

<a id="item-13"></a>
## [TSMC announces A14 process for 2028 production](https://t.me/zaihuapd/42643) ⭐️ 8.0/10

TSMC announced its next-generation A14 process technology, which is scheduled to start production in 2028. Compared to the N2 process, A14 offers a 15% speed increase at the same power or a 30% power reduction at the same speed, along with a logic density improvement of over 20%. This announcement underscores TSMC's commitment to maintaining leadership in advanced semiconductor manufacturing, with implications for high-performance computing, mobile devices, and AI accelerators. The A14 node will enable more powerful and energy-efficient chips, potentially shaping the next generation of electronics. TSMC also plans to introduce the intermediate A16 process in late 2026, which is a 1.6nm node featuring Super Power Rail backside power delivery. A14 is expected to be a 1.4nm node, and TSMC is already developing derivatives such as A14P, A14X, and A14C for different market segments.

telegram · zaihuapd · Jul 18, 05:00

**Background**: Semiconductor process nodes (e.g., N2, A16, A14) refer to the manufacturing technology used to fabricate chips, with smaller numbers generally indicating more advanced, higher-performance nodes. TSMC's N2 process is set for mass production in the second half of 2025, and A16 is positioned as a 1.6nm node with innovative backside power delivery. The company's roadmap shows continuous scaling to maintain Moore's Law-like progress, driven by demand from AI and high-performance computing.

<details><summary>References</summary>
<ul>
<li><a href="https://xueqiu.com/6828609820/333054789">1.4nm亮相，晶圆代工大厂 台 积 电 披露技术路线图 4月23...</a></li>
<li><a href="https://www.elecfans.com/d/2924451.html">台 积 电 2nm 制 程 近况佳，N3X、 N 2 P以及A16...</a></li>
<li><a href="https://m.gelonghui.com/p/3506560">台 积 电 的真正瓶颈</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#TSMC`, `#chip manufacturing`, `#process technology`

---

<a id="item-14"></a>
## [SK Hynix CEO Warns of Worst Memory Shortage by 2027](https://t.me/zaihuapd/42645) ⭐️ 8.0/10

SK Hynix CEO Kwak Noh-Jung warned that by 2027, the global memory industry will face the worst supply shortage in history, as demand from AI and other technologies will outpace supply even with aggressive capacity expansion. This warning from a leading memory manufacturer signals a critical bottleneck for the entire tech industry, particularly for AI hardware, data centers, and consumer electronics, potentially driving up costs and delaying product timelines. The interview occurred on SK Hynix's Nasdaq debut day, with shares closing up 13.3% at $168.85. Kwak also mentioned that U.S., Japan, and Southeast Asia are candidates for overseas fab locations, prioritizing areas with the best land, electricity, and labor costs.

telegram · zaihuapd · Jul 18, 06:30

**Background**: Memory chips, including DRAM and NAND flash, are essential components in computers, smartphones, and AI accelerators. The industry has historically been cyclical, with periods of oversupply and shortage driven by investment cycles and demand fluctuations. SK Hynix is the world's second-largest memory chipmaker, after Samsung.

**Tags**: `#memory industry`, `#supply chain`, `#semiconductor`, `#AI hardware`, `#SK Hynix`

---

<a id="item-15"></a>
## [San Francisco Orders Apple and Google to Remove 'Nudify' Apps](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/) ⭐️ 8.0/10

San Francisco City Attorney David Chiu has sent letters demanding Apple and Google remove dozens of AI-powered 'nudify' apps from their app stores, which use deepfake technology to generate non-consensual intimate images of individuals. This regulatory action highlights growing legal pressure on major tech platforms to curb the spread of non-consensual deepfake pornography, which has severe privacy and ethical implications for victims. The letter notes that Apple and Google may have profited millions from these apps by hosting them without action, despite multiple warnings from the Tech Transparency Project in January and April 2026.

telegram · zaihuapd · Jul 18, 08:45

**Background**: Nudify apps use generative AI to remove clothing from photos, creating realistic nude images often without the subject's consent. This form of deepfake pornography has been widely criticized for enabling harassment and exploitation. The apps are typically marketed as 'AI magic' tools for entertainment, but they pose significant privacy risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deepfake_pornography">Deepfake pornography - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/non-consensual-synthetic-intimate-imagery-nsii">Non - Consensual Synthetic Intimate Imagery</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#privacy`, `#deepfakes`, `#app store regulation`

---