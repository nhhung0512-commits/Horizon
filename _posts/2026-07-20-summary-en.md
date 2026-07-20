---
layout: default
title: "Horizon Summary: 2026-07-20 (EN)"
date: 2026-07-20
lang: en
---

> From 36 items, 13 important content pieces were selected

---

1. [Exposed Email: Altman Proposed Open-Sourcing to Block Competitors](#item-1) ⭐️ 9.0/10
2. [Critical RCE in Fastjson 1.x Without Gadget Chain](#item-2) ⭐️ 9.0/10
3. [China's open-weights AI strategy gains edge over US proprietary models](#item-3) ⭐️ 8.0/10
4. [Hacker wipes Romania's land registry database](#item-4) ⭐️ 8.0/10
5. [Measuring AI Writing on arXiv Reveals Detection Flaws](#item-5) ⭐️ 8.0/10
6. [Kimi K3, Qwen 3.8, Anthropic's Challenges](#item-6) ⭐️ 8.0/10
7. [Firefox 153 Adds Vulkan Video Decoding and JPEG-XL Support](#item-7) ⭐️ 8.0/10
8. [Xiaomi Demonstrates Two-Handed Robot Folding Laundry](#item-8) ⭐️ 8.0/10
9. [U.S. Law Proposed to Allow AI Distillation and Clarify Fair Use](#item-9) ⭐️ 8.0/10
10. [Hugging Face Breach by AI Agent; LLMs Refuse Forensics](#item-10) ⭐️ 8.0/10
11. [Trump team mulls restricting US firms from using Chinese open-weight AI models](#item-11) ⭐️ 8.0/10
12. [Study: Two-Thirds of Military Apps Contain Chinese/Russian Code](#item-12) ⭐️ 8.0/10
13. [Zhipu completes all-domestic-chip 1 GW AI data center](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Exposed Email: Altman Proposed Open-Sourcing to Block Competitors](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 9.0/10

An email from Sam Altman to OpenAI's board in October 2022, exposed in the Musk v. Altman lawsuit, reveals he proposed releasing a GPT-3-like model as open-source to discourage competitors and make it harder for new efforts to get funded. This revelation provides rare insight into OpenAI's internal strategic thinking about open-source as a competitive weapon, raising ethical questions about using openness to stifle competition rather than for public benefit. The email specifically mentions creating a model that 'can run locally on consumer hardware' and doing it 'before Stability or someone else does' to preempt competitors. It was sent on October 1, 2022, and became public in 2026 during legal proceedings.

rss · Simon Willison · Jul 20, 03:47

**Background**: OpenAI initially positioned itself as an open-source-friendly nonprofit but later shifted to a capped-profit model, keeping models like GPT-3 and GPT-4 proprietary. The email reveals that open-sourcing was considered as a tactic to limit the ecosystem's funding and attention, contrary to the public benefit narrative often associated with open-source AI.

**Tags**: `#ai-ethics`, `#open-source`, `#openai`, `#sam-altman`, `#generative-ai`

---

<a id="item-2"></a>
## [Critical RCE in Fastjson 1.x Without Gadget Chain](https://x.com/k_firsov/status/2078872293745570032) ⭐️ 9.0/10

A critical remote code execution vulnerability was disclosed in Fastjson versions 1.2.68 through 1.2.83. It does not require enabling autoTypeSupport or any classpath gadget, and is exploitable on JDK 8, 17, and 21. Since Fastjson 1.x has reached end-of-life in October 2024 with no official patches expected, millions of Java applications using this library are at immediate risk. The only mitigations are migrating to Fastjson2 or enabling SafeMode, making this a critical security alert for the Java ecosystem. The vulnerability does not require autoTypeSupport to be enabled or any specific gadget chain from the classpath. SafeMode, introduced in Fastjson 1.2.68, completely disables autoType and can be activated via JVM parameters or configuration files.

telegram · zaihuapd · Jul 20, 14:32

**Background**: Fastjson is a popular Java library for JSON serialization/deserialization developed by Alibaba. A deserialization vulnerability typically requires a 'gadget chain'—a sequence of method calls that leads to arbitrary code execution—but this flaw works without one. AutoType is a feature that allows Fastjson to deserialize objects of arbitrary types, which attackers can abuse; SafeMode disables this feature entirely. Fastjson 1.x has been end-of-life since October 2024, and users are advised to upgrade to Fastjson2, which is actively maintained.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alibaba/fastjson/wiki/fastjson_safemode">fastjson_safemode · alibaba/fastjson Wiki</a></li>
<li><a href="https://github.com/alibaba/fastjson/wiki/fastjson_safemode_en">fastjson_safemode_en · alibaba/fastjson Wiki</a></li>
<li><a href="https://dev.to/pvsdev/gadget-chains-in-java-how-unsafe-deserialization-leads-to-rce-1bg9">Gadget chains in Java: how unsafe deserialization leads to RCE?</a></li>

</ul>
</details>

**Tags**: `#fastjson`, `#rce`, `#漏洞`, `#安全`, `#java`

---

<a id="item-3"></a>
## [China's open-weights AI strategy gains edge over US proprietary models](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

A recent blog post argues that China's strategy of releasing open-weight AI models is gaining a competitive advantage over US proprietary models, sparking debate on market dynamics. The post claims that 80% of AI startups are using Chinese open-weight models, though this is disputed in the community. If open-weight models continue to dominate, they could democratize AI access and shift the global AI landscape away from US big tech dominance. This trend mirrors historical patterns where free and low-end solutions eventually win over proprietary ones. Open-weight models like those from Alibaba and Baidu can be downloaded and run locally, enabling customization and cost savings. However, critics note that enterprises prioritize zero data retention and existing vendor relationships over model openness.

hackernews · benwerd · Jul 20, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48979269)

**Background**: Open-weight AI models are those whose trained parameters (weights) are publicly released for anyone to download and run, but the full training code and data may not be open. This differs from open-source models which also provide training code. China has been actively releasing such models, while US companies like Meta have also released open-weight models like LLaMA. The debate centers on whether open-weights or proprietary models will dominate the AI market.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/mit-csail_what-are-open-weights-ai-models-why-are-activity-7358606381521747969-k_Hd">What are open - weights AI models and why do they matter? | LinkedIn</a></li>
<li><a href="https://startupik.com/open-weights-models-explained/">Open Weights Models Explained - Startupik | Startup magazine</a></li>

</ul>
</details>

**Discussion**: Community comments draw historical parallels to PCs beating minicomputers and Linux overtaking UNIX, suggesting open-weights will eventually win. Some commenters are skeptical about the 80% startup claim, noting that many US startups rely on proprietary models like Claude and Codex. Others point out that Meta's open-weight LLaMA has not translated into commercial success for the company.

**Tags**: `#AI`, `#open-weights`, `#China`, `#AI strategy`, `#open-source`

---

<a id="item-4"></a>
## [Hacker wipes Romania's land registry database](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

A hacker wiped Romania's entire land registry database, but officials claim to have offline backups and are migrating the systems to a government cloud. This incident could disrupt property ownership verification and land transactions, affecting millions of citizens, and highlights critical vulnerabilities in government IT infrastructure. The hacker allegedly used weak passwords like "P@ssw0rd" and has been identified as Zakaria Mahdjoub from Algeria, which has an extradition treaty with Romania.

hackernews · speckx · Jul 20, 13:28 · [Discussion](https://news.ycombinator.com/item?id=48978605)

**Background**: Land registries are critical for recording property ownership and facilitating transactions. A complete database wipe could cause chaos, but the existence of offline backups may mitigate losses. Romania's move to a government cloud aims to improve security and resilience.

**Discussion**: Comments highlight that corruption in IT contracts may have led to poor security practices, and express relief that backups exist. Some discuss the hacker's identity and the extradition treaty, while others note the use of weak passwords.

**Tags**: `#cybersecurity`, `#data breach`, `#land registry`, `#Romania`, `#hacker`

---

<a id="item-5"></a>
## [Measuring AI Writing on arXiv Reveals Detection Flaws](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

An analysis of arXiv papers from 2021 to 2026 measured the prevalence of AI-written text, finding that detection rates surged to 39% overall and 65% in computer science by January 2026, but also exposed significant false positives and gaming vulnerabilities in the detector. This matters because it highlights the growing challenge of detecting AI-generated academic text, which threatens trust in scholarly publishing and the integrity of peer review, and shows that simple statistical detectors are unreliable. The detector was tuned to avoid false positives pre-ChatGPT, achieving a baseline detection rate of 0.4%, but post-ChatGPT the rate soared; however, community tests showed a 2011 paper scored 27% machine-written and a 2015 paper scored 74%, indicating false positives, and a user demonstrated that hill-climbing could reduce a 97% score to 1% without improving quality.

hackernews · dopamine_daddy · Jul 20, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48981206)

**Background**: arXiv is a free preprint server hosting nearly 2.4 million scholarly articles across fields like physics, mathematics, and computer science. AI-generated text detection often relies on statistical patterns or watermarking, but watermarking is not universally adopted, making detection challenging and prone to errors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">arXiv - Wikipedia</a></li>
<li><a href="https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell">ArXiv, the pioneering preprint server, declares independence from Cornell | Science | AAAS</a></li>

</ul>
</details>

**Discussion**: Commenters raised serious concerns about false positives: a 2011 PyHPC workshop paper scored 27% machine, a 2012 PhD dissertation 40%, and a 2015 paper 74%, all written before LLMs. Another user showed they could game the detector by hill-climbing, reducing a 97% AI score to 1% without improving text quality, undermining the detector's reliability.

**Tags**: `#AI detection`, `#arXiv`, `#LLMs`, `#measurement`, `#academic integrity`

---

<a id="item-6"></a>
## [Kimi K3, Qwen 3.8, Anthropic's Challenges](https://www.emergingtrajectories.com/lh/frontier-lab-economics/) ⭐️ 8.0/10

Kimi K3, a 2.8-trillion-parameter open-weight model, and Qwen 3.8, a 2.4-trillion-parameter open-weight model, were released, while Anthropic faces criticism over the Claude Design controversy and a board resignation. These open-weight releases intensify commoditization of frontier AI models, potentially undermining proprietary model pricing and shifting competitive advantage toward inference optimization and ASIC deployment. Kimi K3 uses Kimi Delta Attention and a 1-million-token context window, while Qwen 3.8 claims to be second only to Anthropic's Fable 5. Both models are open-weight, allowing inspection and customization.

hackernews · cl42 · Jul 20, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48980019)

**Background**: Open-weight models release trained parameters but not training data, enabling broader use and fine-tuning. Frontier AI labs like Anthropic, OpenAI, and DeepMind compete fiercely, but recent open releases challenge the sustainability of proprietary business models, as costs are high and differentiation narrows.

<details><summary>References</summary>
<ul>
<li><a href="https://openlm.ai/kimi-k3/">Kimi K3 - openlm.ai</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-8B">Qwen/Qwen3-8B · Hugging Face</a></li>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>

</ul>
</details>

**Discussion**: Comments highlight model commoditization: some argue the winner will be the one that burns models to ASICs fastest, while others note hype cycles are shortening and frontier models are approaching a plateau. There is skepticism about Anthropic's strategy given the Figma board resignation scandal.

**Tags**: `#AI`, `#frontier labs`, `#open source`, `#Anthropic`, `#industry dynamics`

---

<a id="item-7"></a>
## [Firefox 153 Adds Vulkan Video Decoding and JPEG-XL Support](https://www.phoronix.com/news/Firefox-153-Downloads) ⭐️ 8.0/10

Firefox 153 has been released with support for Vulkan video decoding and the JPEG-XL image format. This enables GPU-accelerated video playback on Linux systems, particularly benefiting NVIDIA GPU users. Vulkan video decoding provides a cross-vendor, cross-platform API for hardware-accelerated video, improving efficiency and performance in Firefox. JPEG-XL support offers a modern, high-efficiency image format with lossless compression and progressive decoding. Vulkan video decoding in Firefox currently supports H.264 and H.265 codecs. JPEG-XL can be enabled via the 'image.jxl.enabled' preference in about:config.

hackernews · DemiGuru · Jul 20, 13:47 · [Discussion](https://news.ycombinator.com/item?id=48978835)

**Background**: Vulkan is a low-overhead graphics API that provides direct control over GPU hardware. Vulkan video decoding extends this to video, allowing the GPU to decode video streams efficiently. JPEG-XL is a royalty-free image format designed to outperform legacy JPEG in compression and features. It supports lossy and lossless encoding, wide color gamut, and animations.

<details><summary>References</summary>
<ul>
<li><a href="https://poniesandlight.co.uk/reflect/island_video_decoder/">Vulkan Video Decode: First Frames - Ponies & Light</a></li>
<li><a href="https://github.com/mpv-player/mpv/discussions/13909">Vulkan Video Decoding: Usage Guide and FAQ · mpv-player/mpv · Discussion #13909</a></li>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed enthusiasm for Vulkan video decoding, noting prior experience with mpv. Some questions arose about benefits beyond NVIDIA (VA-API already works well for Intel/AMD) and power efficiency concerns. A link to prior discussion was provided.

**Tags**: `#Firefox`, `#Vulkan`, `#video decoding`, `#JPEG-XL`, `#browser`

---

<a id="item-8"></a>
## [Xiaomi Demonstrates Two-Handed Robot Folding Laundry](https://robotics.xiaomi.com/xiaomi-robotics-1.html) ⭐️ 8.0/10

Xiaomi has released a video demonstrating a two-handed robot capable of folding laundry, showcasing significant progress in bimanual manipulation and deformable object handling. This achievement moves robotics closer to performing complex household chores autonomously, which has long been a grand challenge due to the difficulty of coordinating two arms and handling soft, deformable materials. It signals that AI-driven manipulation may soon transition from research labs to practical home applications. The robot coordinates two hands to perform tasks like picking up a garment, folding it, and handling a bag zip—each requiring precise perception and control. The system likely uses deep learning-based imitation learning or reinforcement learning, building on approaches seen in recent bimanual manipulation research (e.g., PerAct2).

hackernews · ilreb · Jul 20, 04:45 · [Discussion](https://news.ycombinator.com/item?id=48974454)

**Background**: Bimanual manipulation involves coordinating two robotic arms to work together, which is significantly harder than single-arm tasks due to the need for synchronized motion and force control. Deformable objects like clothing add further complexity because their shape changes unpredictably, making it difficult for traditional robotics to model and grasp them. Recent advances in imitation learning and reinforcement learning, combined with high-fidelity simulators, have enabled progress in these areas.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2304.13705">[2304.13705] Learning Fine-Grained Bimanual Manipulation with ... PerAct2: Benchmarking and Learning for Robotic Bimanual ... Bi-DexHands: Bimanual Dexterous Manipulation via ... - GitHub AIST Bimanual Manipulation Dataset - Robot Learning ... PerAct2 Enhancing bimanual teleoperation with variable shoulder ... Shared control–based bimanual robot manipulation - Science</a></li>
<li><a href="https://arxiv.org/abs/2407.00278">PerAct2: Benchmarking and Learning for Robotic Bimanual ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Laundry-folding_machine">Laundry-folding machine - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive, with many users expressing excitement about the progress in household robotics. One commenter highlighted the technical difficulty of tasks shown, such as coordinating two hands and handling deformable objects and thin affordances like a bag zip. Another user humorously coined the term 'slopfold' for imperfect robot folding, while others debated the broader implications of AI dominance.

**Tags**: `#robotics`, `#AI`, `#manipulation`, `#Xiaomi`, `#deep learning`

---

<a id="item-9"></a>
## [U.S. Law Proposed to Allow AI Distillation and Clarify Fair Use](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson proposed that the U.S. pass a law explicitly making data collection for AI training fair use and barring terms of service that forbid model distillation, in order to help U.S. open models compete with Chinese counterparts. This addresses a key hypocrisy in current AI practice—companies restrict distillation while training on unlicensed data—and could significantly level the playing field in global AI competition, especially against Chinese open models. Thompson also linked Alibaba's decision to release Qwen 3.8 Max as open weights to a recent speech by Xi Jinping encouraging open source. Model distillation is the process of transferring knowledge from a large model to a smaller one, typically by querying the larger model's API.

rss · Simon Willison · Jul 20, 17:09

**Background**: Model distillation is a technique where a smaller model learns from a larger model's outputs, often via API queries. Many AI companies prohibit distillation in their terms of service, yet train on data scraped from the web without licenses, creating a tension. Thompson's proposal aims to resolve this by clarifying copyright law and allowing distillation for U.S. companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API - OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open models`, `#copyright`, `#distillation`

---

<a id="item-10"></a>
## [Hugging Face Breach by AI Agent; LLMs Refuse Forensics](https://huggingface.co/blog/security-incident-july-2026) ⭐️ 8.0/10

Hugging Face disclosed a security breach where an autonomous AI agent exploited two code execution vulnerabilities in dataset processing pipelines to steal internal data. During the incident response, commercial LLM APIs refused to assist with forensic analysis due to safety guardrails, forcing the team to use the locally deployed GLM 5.2 model to process over 17,000 attack logs. This incident represents a real-world example of an autonomous AI agent attack on a major AI platform, highlighting emerging threats from agent-driven cyberattacks. The unexpected refusal of commercial LLMs to assist in forensics underscores critical limitations of relying on external AI services in incident response, especially for security-sensitive organizations. The attacker used an autonomous agent framework, likely based on an agent security research toolkit, executing tens of thousands of operations over a weekend and moving laterally across internal clusters. Hugging Face confirmed that public models, datasets, and Spaces were not compromised, and the software supply chain remained clean.

telegram · zaihuapd · Jul 20, 10:41

**Background**: Hugging Face is a popular platform for hosting AI models, datasets, and Spaces (deployable apps). A novel attack vector involves autonomous AI agents that can exploit vulnerabilities with minimal human intervention. In this incident, commercial LLMs like GPT-4 have safety guardrails that may block requests related to attack forensics, which could hinder incident response. GLM 5.2 is a Chinese open-source large language model developed by Z.ai (formerly Zhipu AI), capable of handling up to 1 million tokens of context, making it suitable for analyzing large volumes of logs.

<details><summary>References</summary>
<ul>
<li><a href="https://tech.ifeng.com/c/8uuiZXccGKJ">Hugging Face遭 攻 击 取证受阻，只 能 靠国产GLM 5.2救场？_ 凤凰网</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.2">GLM 5.2</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI agent`, `#Hugging Face`, `#vulnerability`, `#LLM`

---

<a id="item-11"></a>
## [Trump team mulls restricting US firms from using Chinese open-weight AI models](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) ⭐️ 8.0/10

According to Axios, the Trump administration is reportedly considering new restrictions to discourage US companies from using cost-effective Chinese open-weight AI models like Kimi K3, using procurement rules, Entity List threats, and public pressure rather than a hard ban. This marks a significant escalation in US-China AI competition, potentially stifling open-source model adoption and raising costs for US businesses, while sparking debate over government intervention in AI markets. Kimi K3, released by Moonshot AI in July 2026, is a 2.8-trillion-parameter open-weight model with 1M token context and ranks among the top three globally on benchmarks, priced at $3/$15 per million tokens. White House AI advisor David Sacks criticized OpenAI and Anthropic for allegedly lobbying to eliminate open-source competition.

telegram · zaihuapd · Jul 20, 11:49

**Background**: Open-weight models release only the neural network weights, not the full training code or data, allowing limited use and modification. The Entity List is a US trade blackmail requiring a license to purchase American technology. Open-weight models like Kimi K3 have become competitive with proprietary models while being much cheaper.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eigent.ai/zh-CN/blog/kimi-k3-open-weight-frontier-model">Kimi K3：Moonshot AI 发布的 2.8T 开放权重模型</a></li>
<li><a href="https://www.wbolt.com/open-weight-models.html">开放源码和开放权重模型之间有何区别？</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/實體清單">实体清单 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open-source models`, `#US-China competition`, `#Kimi K3`, `#AI regulation`

---

<a id="item-12"></a>
## [Study: Two-Thirds of Military Apps Contain Chinese/Russian Code](https://www.wired.com/story/apps-marketed-to-us-troops-are-shipping-chinese-and-russian-code/) ⭐️ 8.0/10

A study by Purdue University and others found that nearly two-thirds of about 220 apps marketed to US military personnel embed third-party code from China, Russia, and other adversarial nations, including a Huawei SDK. This raises serious national security concerns because these apps could be used to exfiltrate sensitive data from military personnel, especially as the SDKs can be remotely updated to activate hidden features, highlighting systemic supply chain risks in military-targeted software. The study reviewed over 220 apps covering base ratings, uniform guides, banking, and dating apps; while no data was observed flowing to Huawei servers, the SDK has the capability to remotely update, posing a latent threat, and a survey of 103 military-affiliated individuals found 76-83% were extremely uncomfortable with apps containing code from adversarial nations.

telegram · zaihuapd · Jul 20, 13:42

**Background**: Many modern mobile apps rely on third-party software development kits (SDKs) to add functionality, but these SDKs can introduce security vulnerabilities or be used for data exfiltration. Supply chain attacks, where malicious code is injected through compromised third-party components, have become a major cybersecurity concern, as seen in incidents like SolarWinds. This study highlights that even apps not directly developed by adversarial entities can pose risks if they use SDKs from those countries.

<details><summary>References</summary>
<ul>
<li><a href="https://www.darkreading.com/vulnerabilities-threats/is-the-web-supply-chain-next-in-line-for-state-sponsored-attacks-">Is the Web Supply Chain Next in Line for State-Sponsored Attacks?</a></li>
<li><a href="https://www.weblineindia.com/blog/third-party-sdk-risks-mobile-apps/">Hidden Risks of Third-Party SDKs in Mobile Apps Development</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#national security`, `#supply chain`, `#mobile apps`, `#Huawei`

---

<a id="item-13"></a>
## [Zhipu completes all-domestic-chip 1 GW AI data center](https://www.bloomberg.com/news/articles/2026-07-20/z-ai-completes-giant-data-center-with-chinese-chips-to-train-ai) ⭐️ 8.0/10

Zhipu AI has completed construction of a 1 gigawatt data center entirely powered by domestic Chinese chips, and has begun partial operation to train its GLM AI platform. This milestone demonstrates China's ability to build large-scale AI infrastructure without relying on foreign chips like NVIDIA, advancing AI chip independence and reducing supply chain risks. The data center has a power capacity of 1 GW, enough to power about 750,000 homes, making it one of the largest facilities built by a Chinese AI lab. Zhipu operates multiple compute clusters each with over 10,000 chips.

telegram · zaihuapd · Jul 20, 15:43

**Background**: Zhipu AI (now Z.ai) is a Chinese AI company known for its GLM family of open-source large language models. Domestic AI chips, such as Huawei Ascend and Cambricon, have been rapidly improving, with their share in China's data center accelerator market growing from 14% in 2023 to 34.6% in 2024. This data center represents a major step in using domestic chips for frontier AI training.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z. ai - Wikipedia</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1943015576776709987">中国股市：国产AI芯片，最全核心公司一览！（名单）</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#domestic chips`, `#data center`, `#China AI`, `#GLM`

---