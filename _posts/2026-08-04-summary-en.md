---
layout: default
title: "Horizon Summary: 2026-08-04 (EN)"
date: 2026-08-04
lang: en
---

> From 40 items, 9 important content pieces were selected

---

1. [Keyv and Friends Compromised in Active Shai-Hulud Supply Chain Attack](#item-1) ⭐️ 9.0/10
2. [Simple Algorithm and Color Space for Diverse Skin Tones](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4 Flash Runs on Single AMD MI300X at 150+ tok/s](#item-3) ⭐️ 8.0/10
4. [Apple Expands Lawsuit, Says More Ex-Employees May Have Leaked Data to OpenAI](#item-4) ⭐️ 8.0/10
5. [Harness Engineering for Self-Improving AI Agents](#item-5) ⭐️ 8.0/10
6. [Cloudflare Ditches Third-Party Security Tools, Uses $58/Month AI for Bug Bounty Triage](#item-6) ⭐️ 8.0/10
7. [Google Assembles $200B Vendor-Financing Machine to Deliver AI Chips to Anthropic](#item-7) ⭐️ 8.0/10
8. [China's First Mandatory L3/L4 Autonomous Driving Safety Standard Heads to Approval](#item-8) ⭐️ 8.0/10
9. [NVIDIA CEO Jensen Huang Backs Use of Chinese Open-Source AI](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Keyv and Friends Compromised in Active Shai-Hulud Supply Chain Attack](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 9.0/10

A new Shai-Hulud supply-chain attack has compromised the popular npm package Keyv and related packages such as cacheable, using malicious pre-install hooks. JFrog researchers identified the worm, which harvests credentials, publishes itself to every writable npm package, and plants execution hooks in GitHub repositories. Keyv is a widely used key-value storage library with thousands of dependents, so this zero-day attack can propagate across the npm ecosystem and cause credential theft and downstream compromises. It underscores the urgent need for stricter registry practices and stronger defenses against malicious install scripts. The malware leverages pre-install hooks that run automatically during package installation, and it was first spotted in a newly published version of Keyv. According to JFrog, the campaign has already affected over 400 packages, and npm has been working to remove the reported packages.

hackernews · cimi_ · Aug 4, 11:01 · [Discussion](https://news.ycombinator.com/item?id=49166874)

**Background**: Supply-chain attacks work by compromising a trusted upstream dependency, so malicious code executes when developers install a package. Pre-install and post-install hooks are scripts that npm runs automatically, making them a prime vector for such attacks. Shai-Hulud is a known malware campaign that spreads by compromising npm packages. Keyv is a simple key-value storage library that supports multiple backends, which explains the large number of dependent projects.

<details><summary>References</summary>
<ul>
<li><a href="https://research.jfrog.com/post/shai-hulud-is-back-august/">Major Shai Hulud campaign strikes npm again, affecting keyv and 400+ packages - JFrog Security Research</a></li>
<li><a href="https://www.npmjs.com/package/keyv">keyv - npm</a></li>

</ul>
</details>

**Discussion**: Commenters are urging npm to restrict or deprecate pre-install hooks, with one suggesting a moratorium on new hooks and another recommending setting 'min-release-age=5' in .npmrc. Others questioned whether commercial security tools can detect such attacks proactively, while a user shared updated documentation on npm supply-chain attack techniques.

**Tags**: `#security`, `#npm`, `#supply-chain`, `#javascript`, `#malware`

---

<a id="item-2"></a>
## [Simple Algorithm and Color Space for Diverse Skin Tones](https://toneyalexander.github.io/inclusive-color-space/) ⭐️ 8.0/10

A developer created a new color space and procedural generation algorithm for producing diverse, plausible skin tones, with an interactive JavaScript color picker and a Python sample. The project is documented at toneyalexander.github.io/inclusive-color-space/. This matters because it offers a practical, algorithm-driven solution to a persistent challenge in digital art and game development: choosing diverse, realistic skin tones. It could make characters and avatars in games, illustrations, and virtual worlds more inclusive and representative of real human diversity. The color space was built by hand-fitting functions to empirical skin-tone data rather than using a method like PCA, and the page includes extensive equations and interactive demos. The author acknowledges the methodology is 'a bit shaky' and lists limitations, including the fact that lighting conditions are not explicitly modeled, along with a Future Work section.

hackernews · automatoney · Aug 4, 15:16 · [Discussion](https://news.ycombinator.com/item?id=49170165)

**Background**: Procedural generation is a method of creating data algorithmically, often using randomness, and is widely used in games and digital art. Human skin color is not a simple physical quantity; it varies widely and is affected by lighting, perception, and biological factors. This project attempts to define a simplified but broad color space for plausible skin tones, making procedural generation of diverse characters easier.

<details><summary>References</summary>
<ul>
<li><a href="https://toneyalexander.github.io/inclusive-color-space/">What Colors Are We? Constructing A Color Space For Skin Tones</a></li>
<li><a href="https://en.wikipedia.org/wiki/Procedural_generation">Procedural generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human_skin_color">Human skin color - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were generally enthusiastic, praising the interactive demos and the clever hand-fitted functions. Constructive critiques noted that lighting is not included in the limitations, and some suggested consulting references like Pantone Skin Tones or exploring Oklab, which had been used to plot real foundation shade data.

**Tags**: `#color science`, `#computer graphics`, `#procedural generation`, `#digital art`, `#skin tone`

---

<a id="item-3"></a>
## [DeepSeek V4 Flash Runs on Single AMD MI300X at 150+ tok/s](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

A GitHub project demonstrates DeepSeek V4 Flash running on a single AMD MI300X GPU at over 150 tokens per second, using the full model weights and only reducing the context window from 1 million to 256k tokens. This makes a frontier-class MoE model practical on one accelerator, cutting the hardware cost and complexity of running DeepSeek V4 Flash compared with multi-GPU setups. It also highlights the MI300X's large HBM capacity as a real advantage for single-GPU large-model inference. The tradeoff is context length: the original model supports 1M tokens, while this setup offers 256k. The MI300X provides 192GB of HBM3 with 5.3 TB/s bandwidth, which is sufficient to hold the 284B-parameter model thanks to its native MXFP4 quantization and MoE architecture with only 13B activated parameters.

hackernews · zhoutong · Aug 4, 10:00 · [Discussion](https://news.ycombinator.com/item?id=49166386)

**Background**: DeepSeek V4 Flash is an efficiency-optimized Mixture-of-Experts (MoE) model with 284B total parameters and 13B activated parameters, supporting a 1M-token context window. AMD's MI300X is a CDNA 3-based accelerator with 192GB of HBM3 memory, designed for large-scale AI inference. Running such a large model on a single GPU requires both enough memory to store the weights and careful management of the context window to fit within hardware limits.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html">AMD Instinct™ MI300X Accelerators</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V4 Flash 0423 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Commenters largely praised the practical tradeoffs, noting that keeping full weights and 150+ tok/s is impressive even with the context cut. Several added hardware clarifications: MI300X is an OAM module typically sold in an 8-GPU box, the PCIe-based MI350P has 144GB but may also work due to native MXFP4 quantization, and prior work on DwarfStar or 2xMI300X was not fully referenced in the README.

**Tags**: `#AI/ML`, `#Inference`, `#AMD MI300X`, `#DeepSeek`, `#Hardware`

---

<a id="item-4"></a>
## [Apple Expands Lawsuit, Says More Ex-Employees May Have Leaked Data to OpenAI](https://techcrunch.com/2026/08/04/apple-says-more-ex-employees-may-have-taken-confidential-data-to-openai/) ⭐️ 8.0/10

Apple has expanded its lawsuit against OpenAI, alleging that additional former employees may have taken confidential data to the AI startup. The update reportedly includes claims involving screenshots of documents and residual access to Apple's systems. This case could set precedents for employee mobility and intellectual property protection in the AI industry. It also threatens to derail OpenAI's hardware efforts, which some see as a vanity project by CEO Sam Altman. The allegations involve more than memory—they reportedly include screenshots of confidential documents. Apple also did not concede that former employees' 'residual access' to its systems stemmed from Apple's own poor security procedures, a point OpenAI has highlighted.

hackernews · thewebguyd · Aug 4, 15:37 · [Discussion](https://news.ycombinator.com/item?id=49170479)

**Background**: Apple has been embroiled in a legal battle with OpenAI over accusations that employees who left for the startup took confidential information, especially related to hardware work. OpenAI has denied the allegations and has criticized Apple's security practices, pointing to the 'residual access' former employees retained to Apple's systems. The case is part of a broader industry tension as AI companies aggressively recruit from established tech giants, raising questions about trade secrets, non-compete clauses, and innovation. OpenAI's own hardware project, which aims to develop consumer devices, has also attracted skepticism, with some comparing it to past failures like the Humane AI Pin.

**Discussion**: Commenters are divided: some, like former Apple executive Tony Fadell, call the lawsuit a typical scare tactic aimed at employees. Others criticize OpenAI's hardware ambitions, with one calling it a 'vanity project' that might be the 'Humane Pin 2.0.' Meanwhile, some defend the seriousness of the allegations, noting they involve document screenshots, not just memory, and mock OpenAI's critiques of Apple's security.

**Tags**: `#Apple`, `#OpenAI`, `#Legal`, `#Confidential Data`, `#AI Hardware`

---

<a id="item-5"></a>
## [Harness Engineering for Self-Improving AI Agents](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

Lilian Weng published a technical post titled 'Harness Engineering for Self-Improvement,' exploring how AI agent harnesses can be engineered to enable self-improvement. The post discusses frameworks such as Self-Harness, which uses execution traces in an iterative, autonomous loop to improve an agent's scaffolding, tools, and prompts. This matters because improving the harness rather than just model weights opens a new optimization frontier for AI agents, especially as pretraining gains are seen by some as plateauing. It affects developers building agentic systems, as well as the tools and evaluators needed to measure and improve agent behavior in real-world deployments. The article and surrounding discussion highlight that agents can use auto-research over production traces to spot and fix real issues, and can even write their own tools, e.g., reducing context loading from 20k tokens across 15 tool calls to 800 tokens in one session_context call. Key caveats include the need for robust fitness functions, evals, and validation/test splits to prevent reward hacking, with security and safety layers kept outside the loop.

hackernews · tosh · Aug 4, 06:17 · [Discussion](https://news.ycombinator.com/item?id=49164896)

**Background**: An AI agent harness typically includes the model, system prompts, tools, skills, and the orchestration code that connects them. Self-harness approaches let an agent mine execution traces and iteratively update this scaffolding, similar to self-play or evolutionary algorithms where a fitness function guides improvement. Meanwhile, frameworks like Genetic-Pareto (GEPA) sample agent trajectories, reflect on them in natural language, propose prompt revisions, and evolve the system through feedback loops.

<details><summary>References</summary>
<ul>
<li><a href="https://lilianweng.github.io/posts/2026-07-04-harness/">Harness Engineering for Self-Improvement | Lil'Log</a></li>
<li><a href="https://bdtechtalks.com/2026/07/13/ai-agents-self-improving-harness/">How self-improving harnesses are rewriting the agent engineering playbook - TechTalks</a></li>
<li><a href="https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining">Self-Evolving Agents - A Cookbook for Autonomous Agent Retraining</a></li>

</ul>
</details>

**Discussion**: Commenters are largely optimistic and share concrete experiences: one reports auto-research on harnesses is 'surprisingly powerful' when combined with reading production traces and letting the agent write its own tools, while emphasizing evals and train/test splits to avoid reward hacking. Another asks when harnesses will generate their own RLHF/DPO training sets and LoRA-finetune the models they run, and a third argues that optimizing prompts and code may be more sample-efficient than training weights, though it lacks gradient descent.

**Tags**: `#AI agents`, `#harness engineering`, `#LLM self-improvement`, `#agentic systems`, `#evals`

---

<a id="item-6"></a>
## [Cloudflare Ditches Third-Party Security Tools, Uses $58/Month AI for Bug Bounty Triage](https://www.theregister.com/security/2026/08/04/cloudflare-has-mostly-ditched-third-party-security-tools-suggests-not-trying-that-at-home/5282600) ⭐️ 8.0/10

Cloudflare CSO Grant Bourzikas said the company replaced nearly all third-party security tools with 200+ self-built autonomous agents, using Anthropic's Claude Sonnet to triage bug bounty reports for about $58 per month. He cautioned other enterprises not to blindly follow suit. This is a notable real-world example of AI-driven security automation with concrete cost data, showing a dramatic price difference versus a specialized security model (Mythos at ~$200k/month). It could reshape how enterprises think about security tooling, AI agents, and vendor relationships. The security-specific model Mythos would cost roughly $200,000 per month for the same triage workload, per Bourzikas. Cloudflare also attributed its 1,100-person layoff to AI automation, and chief strategy officer Stephanie Cohen said the company plans to act as an intermediary between AI companies and publishers using micropayments.

telegram · zaihuapd · Aug 4, 09:24

**Background**: Claude is Anthropic's family of large language models, with Sonnet being the mid-tier size (alongside Haiku and Opus). Mythos is Anthropic's limited-access autonomous cyber security model, announced as Mythos Preview, which according to UK AISI evaluations can autonomously execute multi-stage attacks and discover vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet \ Anthropic</a></li>
<li><a href="https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities">Our evaluation of Claude Mythos Preview’s cyber capabilities | AISI Work</a></li>
<li><a href="https://www.contrastsecurity.com/glossary/mythos-ai">What Is Mythos AI? Autonomous Exploits and AppSec Defense | Contrast Security</a></li>

</ul>
</details>

**Discussion**: No comments were provided, so no community discussion is available.

**Tags**: `#security`, `#AI`, `#Cloudflare`, `#automation`, `#bug bounty`

---

<a id="item-7"></a>
## [Google Assembles $200B Vendor-Financing Machine to Deliver AI Chips to Anthropic](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c) ⭐️ 8.0/10

According to a Financial Times investigation published on August 4, Google has quietly assembled one of the largest infrastructure financing structures in history—totaling roughly $200 billion—to deliver over $150 billion in AI chips to Anthropic. The structure, involving Broadcom, Apollo, Blackstone, Morgan Stanley, and several crypto miners, uses a vendor-financing model where risk is spread across multiple parties. This unprecedented financing structure reveals how AI infrastructure is shifting from outright hardware purchases to highly leveraged, vendor-financed models, with major implications for AI economics and the competitive landscape. It also shows hyperscalers like Google using financial engineering to secure AI compute for key partners without taking huge balance-sheet hits. In June, a special purpose vehicle named Compute SPV completed its first transactions, purchasing about $35 billion in hardware, equivalent to roughly 1 gigawatt of compute and 1 million TPUs. The structure mirrors the vendor-financing playbook used by Boeing and GE: Google guarantees data centers, Broadcom buys and helps finance chips, and Apollo and Blackstone buy hardware and lease it back to Anthropic.

telegram · zaihuapd · Aug 4, 10:52

**Background**: Vendor financing is a model in which a supplier (or a related financing entity) provides loans or leases to help customers buy its products—commonly used by Boeing and GE for aircraft and engines. In AI infrastructure, this approach is gaining traction because hyperscalers and AI labs like Anthropic need enormous compute capacity but cannot absorb hundreds of billions of dollars in hardware costs on their balance sheets. A special purpose vehicle (SPV) is a subsidiary created to isolate financial risk, and it is increasingly used to pool investor capital for AI compute deals. Google's Tensor Processing Units (TPUs) are custom application-specific integrated circuits (ASICs) designed for neural network machine learning, which are central to this deal.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/s/spv.asp">investopedia.com/terms/s/ spv .asp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/what-circular-ai-deals-reveal-current-strategy-harsha-srivatsa-htvcc">What Circular AI Deals Reveal about current AI Strategy</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#Anthropic`, `#Google`, `#financing`, `#TPU`

---

<a id="item-8"></a>
## [China's First Mandatory L3/L4 Autonomous Driving Safety Standard Heads to Approval](https://t.me/zaihuapd/42972) ⭐️ 8.0/10

China's Ministry of Industry and Information Technology has finalized the draft of the first mandatory national standard for L3/L4 autonomous driving, titled 'Safety Requirements for Autonomous Driving Systems of Intelligent Connected Vehicles.' The draft is open for public comment from June 17 and is recommended to take effect on July 1, 2027. This milestone shifts China's AV regulation from non-binding guidance to enforceable safety mandates, requiring automakers to prove safety through rigorous evidence rather than marketing claims. It will reshape development cycles and market competition for L3/L4 vehicles in the world's largest auto market. The standard introduces a Safety Case mechanism, compelling enterprises to argue safety through a 'claim-argument-evidence' structure. It sets separate requirements: human-machine takeover for L3 systems and autonomous risk handling for L4 systems.

telegram · zaihuapd · Aug 4, 13:06

**Background**: Autonomous driving is classified into levels L0-L5 according to standards such as SAE J3016 and China's GB/T 40429-2021. L3 is 'conditional automation,' where the driver must be ready to take over; L4 is 'high automation,' where the system can manage risks without human intervention. Previously, China's AV regulations were largely voluntary, but this new mandatory standard requires automakers to assemble a structured Safety Case as evidence of safety.

<details><summary>References</summary>
<ul>
<li><a href="https://www.163.com/dy/article/L01347E80547KOTE.html">163.com/dy/article/L01347E80547KOTE.html</a></li>
<li><a href="https://auto-time.36kr.com/p/1373076185888129">自 动 驾 驶 不等于零事故，但也不该被“妖魔化”_36氪</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#regulation`, `#safety`, `#China`, `#automotive`

---

<a id="item-9"></a>
## [NVIDIA CEO Jensen Huang Backs Use of Chinese Open-Source AI](https://t.me/zaihuapd/42977) ⭐️ 8.0/10

In an interview, NVIDIA CEO Jensen Huang said Chinese open-source AI models are 'very good' and US companies should 'absolutely' be allowed to use them. He also argued against broad national-security restrictions on open-source models, contending that free or cheaper AI expands the user base and increases demand for chips and data centers. As a leading industry figure, Huang's remarks could shape the ongoing policy debate over AI regulation and national security. This highlights the tension between innovation and security, and may influence how US companies adopt global open-source AI models and how chip demand evolves. Huang proposed that Chinese models downloaded by companies could be controlled within secure sandboxes, and that open code helps researchers identify vulnerabilities and strengthen defenses. He also suggested handling IP disputes based on specific privacy or contract violations rather than banning entire model categories.

telegram · zaihuapd · Aug 4, 15:22

**Background**: Open-source AI models are models with publicly accessible code, allowing broad usage and modification. Sandboxing is a security practice that isolates software to limit potential harm, while organizations like OWASP provide frameworks for assessing large language model security. Recent Chinese open-source models, such as DeepSeek R1, have drawn global attention, prompting debates about their safety and usage.

<details><summary>References</summary>
<ul>
<li><a href="https://aisafetyhub.au/ai-sandbox">The AI Sandbox — AI Safety Hub</a></li>
<li><a href="https://owasp.org/www-project-top-10-for-large-language-model-applications/">OWASP Top 10 for Large Language Model ... | OWASP Foundation</a></li>
<li><a href="https://opentools.ai/news/deepseek-r1-the-open-source-ai-model-making-waves-for-all-the-wrong-reasons">DeepSeek R1: The Open - Source AI Model Making... | OpenTools</a></li>

</ul>
</details>

**Tags**: `#AI`, `#开源模型`, `#AI政策`, `#黄仁勋`, `#英伟达`

---