---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 36 items, 15 important content pieces were selected

---

1. [Stacked Pull Requests Launch on GitHub](#item-1) ⭐️ 9.0/10
2. [UEFA and 55 National Associations Boycott FIFA Competitions](#item-2) ⭐️ 9.0/10
3. [Kimi K3: Novel Attention, Load Balancing, and RL Infrastructure](#item-3) ⭐️ 9.0/10
4. [Russia Charges Telegram Founder Durov with Aiding Terrorism](#item-4) ⭐️ 9.0/10
5. [Anthropic AI Finds Critical Flaw in NIST Candidate HAWK](#item-5) ⭐️ 9.0/10
6. [DeepMind disbands Nobel-winning AlphaFold team, members join Anthropic](#item-6) ⭐️ 9.0/10
7. [Beware of Malware in Cheap TV Streaming Sticks](#item-7) ⭐️ 8.0/10
8. [Gemini Robotics 2 brings whole body intelligence to robots](#item-8) ⭐️ 8.0/10
9. [OpenAI Cuts GPT-5.6 Luna Cost by 80%](#item-9) ⭐️ 8.0/10
10. [Refactoring Economic Benefits in the Age of AI](#item-10) ⭐️ 8.0/10
11. [GCC adopts human-oversight policy for AI contributions](#item-11) ⭐️ 8.0/10
12. [Professor loses PhD students over review process](#item-12) ⭐️ 8.0/10
13. [MLVC: A Multi-Platform Learned Video Codec Nearing Real-World Deployment](#item-13) ⭐️ 8.0/10
14. [UK CMA Proposes Allowing App Developers to Direct Users to Alternative Payments](#item-14) ⭐️ 8.0/10
15. [EU launches AI super factory tender to mobilize €30B](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stacked Pull Requests Launch on GitHub](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) ⭐️ 9.0/10

GitHub has launched stacked pull requests in public preview, allowing developers to create and manage a stack of dependent changes that can be reviewed and merged independently. This feature is one of the largest changes to GitHub in years, covering services from Actions to the web UI. Stacked PRs enable a more efficient workflow where complex features are broken into small, reviewable pieces, potentially improving code review quality and developer productivity. As this workflow becomes available on the world's largest code hosting platform, it could influence how millions of developers approach software development. The feature is in public preview and may contain issues, such as merging an entire stack being broken in some cases and requiring re-approval for squash-and-merge with reviews. GitHub has provided a CLI tool and documentation to help developers get started.

hackernews · tomzorz · Jul 30, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49112232)

**Background**: Stacked pull requests (also called stacked diffs) are a workflow where a series of small, dependent changes are stacked on top of each other, each represented as a separate pull request. This contrasts with the traditional approach of creating one large PR for an entire feature, which can be difficult to review. The workflow is popular in some open-source communities and has been supported by third-party tools like Graphite, but this is the first native implementation on GitHub.

<details><summary>References</summary>
<ul>
<li><a href="https://www.git-tower.com/blog/stacked-prs">Understanding the Stacked Pull Requests Workflow | Tower Blog</a></li>
<li><a href="https://www.graphite.com/guides/stacked-diffs">Stacked diffs</a></li>
<li><a href="https://www.michaelagreiler.com/stacked-pull-requests/">Stacked pull requests : make code reviews... - Dr. Michaela Greiler</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive, with many developers excited about this long-requested feature. However, there are concerns about stability and usability, such as issues with merging entire stacks and the need for re-approvals. Some commenters also question the benefits over well-structured commit-based reviews, especially in the context of AI-generated code.

**Tags**: `#GitHub`, `#pull requests`, `#software engineering`, `#developer workflow`

---

<a id="item-2"></a>
## [UEFA and 55 National Associations Boycott FIFA Competitions](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/) ⭐️ 9.0/10

UEFA and its 55 national associations have announced they will not participate in FIFA competitions, citing corruption and governance issues. This boycott could reshape international football governance, as UEFA represents the most powerful football region. It signals a potential split from FIFA, threatening the unity of the global game. The announcement came from UEFA and all its 55 member associations, indicating unanimous support. Specific FIFA competitions affected were not detailed, but it likely includes future World Cups.

hackernews · dickfickling · Jul 30, 18:40 · [Discussion](https://news.ycombinator.com/item?id=49113929)

**Background**: FIFA is the global governing body for football, while UEFA oversees European football. Frequent corruption scandals have plagued FIFA, leading to criticism from member associations. This boycott is unprecedented in scale.

**Discussion**: Comments largely support UEFA's stance, with users calling FIFA corrupt and suggesting UEFA should organize its own World Cup. Some note it's overdue and compare it to a religious schism in sports.

**Tags**: `#football`, `#FIFA`, `#UEFA`, `#sports governance`, `#boycott`

---

<a id="item-3"></a>
## [Kimi K3: Novel Attention, Load Balancing, and RL Infrastructure](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 9.0/10

Moonshot AI released the technical report and open-source code for Kimi K3, a 2.8-trillion-parameter mixture-of-experts model that introduces Kimi Delta Attention, Quantile Balancing, and the AgentENV reinforcement learning runtime. Kimi K3 achieves frontier performance as an open-weight model, ranking fourth out of 580 models on Artificial Analysis, behind only Claude Opus 5, Fable 5, and GPT-5.6 Sol, demonstrating that open-weight models can compete with proprietary systems. Kimi Delta Attention replaces the KV cache in 69 of 93 layers with a 128x128 matrix per head, reducing memory for a 1M-token context from 104.6 GiB to 27.2 GiB. Quantile Balancing computes bias from router score margins to evenly load 896 experts per layer without hyperparameters.

reddit · r/MachineLearning · /u/noninertialframe96 · Jul 30, 16:37

**Background**: Traditional transformer attention has quadratic complexity O(T²) with sequence length T, making long contexts expensive. Mixture-of-experts models face load balancing issues where some experts are overused. Agentic reinforcement learning requires isolated sandboxes for training agents to interact with environments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/kimi-delta-attention">Kimi Delta Attention : Delta ‐Rule Linear Mechanism</a></li>
<li><a href="https://openathena.ai/blog/quantile-balancing/">Mixture of Experts Quantile Balancing: Validated at 32B-A5B (1e22 FLOPs) Scale | Open Athena</a></li>
<li><a href="https://www.marktechpost.com/2026/07/27/kimi-ai-and-kvcache-ai-open-sources-agentenv/">Kimi AI and kvcache-ai Open Sources ' AgentENV ... - MarkTechPost</a></li>

</ul>
</details>

**Tags**: `#Kimi K3`, `#attention`, `#mixture of experts`, `#open-weight models`, `#RL training infrastructure`

---

<a id="item-4"></a>
## [Russia Charges Telegram Founder Durov with Aiding Terrorism](https://t.me/zaihuapd/42859) ⭐️ 9.0/10

On July 29, Russia's Federal Security Service (FSB) announced that it has filed criminal charges against Telegram founder Pavel Durov under Article 205.1, Part 1.1 of the Russian Criminal Code (aiding terrorism) and placed him on an international wanted list. This unprecedented legal action against a prominent tech founder could set a dangerous precedent for platform liability and end-to-end encryption, threatening the privacy and security of hundreds of millions of Telegram users worldwide. The FSB alleges that Telegram management refused to delete channels, groups, and bots used by Ukrainian intelligence and terrorist organizations to coordinate sabotage, terror attacks, mass killings, and fraud, resulting in numerous casualties and billions of rubles in damages.

telegram · zaihuapd · Jul 30, 03:45

**Background**: Telegram is an encrypted messaging app founded by Pavel Durov, who left Russia in 2014 after refusing to comply with government demands to block opposition groups. Article 205.1 of the Russian Criminal Code criminalizes aiding terrorist activities, including financing or organizing. The charges carry severe penalties, including potential imprisonment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unodc.org/cld/en/legislation/rus/the_criminal_code_of_the_russian_federation_russianenglish/chapter_24/article_205.1_-_205.3/article_205.1_-_205.3.html">Article 205.1 - 205.3</a></li>
<li><a href="https://www.rightsinrussia.org/law-of-the-week-37/">Law of the Week: Article 205.5 of the Russian Criminal Code (Organisation of and participation in the activities of a terrorist organisation) - Rights in Russia</a></li>

</ul>
</details>

**Tags**: `#Pavel Durov`, `#Telegram`, `#FSB`, `#terrorism charges`, `#international wanted list`

---

<a id="item-5"></a>
## [Anthropic AI Finds Critical Flaw in NIST Candidate HAWK](https://startupfortune.com/claude-mythos-broke-hawk-and-the-nist-post-quantum-timeline-may-not-survive-it/) ⭐️ 9.0/10

Anthropic's Claude Mythos Preview AI discovered a severe weakness in the NIST post-quantum algorithm HAWK within 60 hours, reducing its effective key strength from 2^64 to 2^38, a flaw that human cryptanalysts had missed for two years. This milestone shows AI can dramatically accelerate cryptanalysis, directly impacting post-quantum cryptography standardization timelines and forcing the community to reconsider algorithm evaluation processes. The attack cost approximately $100,000 in API fees and does not run in polynomial time, meaning larger key sizes remain secure; HAWK has not been publicly withdrawn by NIST.

telegram · zaihuapd · Jul 30, 05:47

**Background**: Post-quantum cryptography aims to develop algorithms resistant to future quantum computers. NIST has been running a public competition since 2016 to select standards, with HAWK being a third-round candidate. The U.S. executive order mandates federal migration to quantum-resistant cryptography by 2030-2031.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/">Mythos attack on 3rd-round PQC algorithm candidate... - Ars Technica</a></li>
<li><a href="https://www.techzine.eu/news/applications/143290/mythos-knocks-hawk-out-of-the-race-for-a-post-quantum-standard/">Mythos knocks HAWK out of the race for a post - quantum standard</a></li>
<li><a href="https://korben.info/en/claude-breaks-post-quantum-algorithm-60-hours.html">Claude breaks a post - quantum algorithm in 60 hours - Korben</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cryptanalysis`, `#post-quantum cryptography`, `#NIST`, `#Anthropic`

---

<a id="item-6"></a>
## [DeepMind disbands Nobel-winning AlphaFold team, members join Anthropic](https://www.ft.com/content/61b2953d-ee0d-45de-af6e-a9c1cf524b33?syn-25a6b1a6=1) ⭐️ 9.0/10

Google DeepMind has disbanded its Nobel Prize-winning AlphaFold team, reassigning many researchers to other projects, while three core members have left to join competitor Anthropic. This strategic shift away from protein folding research towards generative AI and other areas could reshape the competitive landscape of AI research and potentially slow progress in computational biology. Nearly a quarter of the original AlphaFold paper authors have left DeepMind, including key researchers John Jumper, Jonas Adler, and Alexander Pritzel, who joined Anthropic. Remaining team members moved to projects like Gemini, enzyme design, nuclear fusion, or Isomorphic Labs.

telegram · zaihuapd · Jul 30, 07:45

**Background**: AlphaFold is an AI system developed by DeepMind that accurately predicts protein structures, winning the 2024 Nobel Prize in Chemistry. DeepMind is Alphabet's AI research lab, and Isomorphic Labs is a spin-off focused on AI-driven drug discovery.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold - Wikipedia</a></li>
<li><a href="https://deepmind.google/science/alphafold/">AlphaFold — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isomorphic_Labs">Isomorphic Labs</a></li>

</ul>
</details>

**Tags**: `#AlphaFold`, `#DeepMind`, `#Anthropic`, `#AI research`, `#protein folding`

---

<a id="item-7"></a>
## [Beware of Malware in Cheap TV Streaming Sticks](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/) ⭐️ 8.0/10

A Krebs on Security article reveals that cheap TV streaming sticks, such as the H96 model, come pre-infected with malware that enables residential proxy and ad fraud schemes, turning the devices into bots for clicking on ads. Millions of users may unknowingly buy compromised devices from major e-commerce platforms, putting their home networks at risk and contributing to ad fraud that drains advertiser budgets. The malware uses Blockly modules to control the sticks for tasks like browsing websites and clicking ads, employing vision and reasoning systems to mimic human behavior, according to a Bitsight report.

hackernews · speckx · Jul 30, 17:04 · [Discussion](https://news.ycombinator.com/item?id=49112744)

**Background**: TV streaming sticks are inexpensive devices that plug into a TV's HDMI port to stream content. Cheap 'no-name' brands often run modified Android systems with no security updates, making them easy targets for malware. Attackers can use these devices to commit ad fraud by simulating web traffic, which generates revenue for them.

<details><summary>References</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/">Read This Before You Buy That TV Streaming Stick – Krebs on Security</a></li>
<li><a href="https://www.malwarebytes.com/blog/news/2025/11/illegal-streaming-is-costing-people-real-money-research-finds">The hidden costs of illegal streaming and modded Amazon Fire TV Sticks | Malwarebytes</a></li>

</ul>
</details>

**Discussion**: Commenters express frustration that e-commerce platforms like Amazon sell these harmful products without accountability. Some users share personal experiences with ad-ridden devices, while others recommend isolating IoT devices on separate VLANs for protection.

**Tags**: `#security`, `#streaming`, `#privacy`, `#malware`, `#IoT`

---

<a id="item-8"></a>
## [Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

Google DeepMind released Gemini Robotics 2 on July 30, 2026, a vision-language-action model that enables whole-body control of full humanoid robots, from feet to fingertips. This breakthrough advances robot adaptability and dexterity, enabling fluid movements, fine motor skills, and multi-robot collaboration, potentially transforming industries like manufacturing, healthcare, and home assistance. Gemini Robotics 2 is a vision-language-action model (VLA) that controls the Apptronik Apollo 2 humanoid robot, and it includes a separate model, Gemini Robotics ER 2, for embodied reasoning and complex multi-step planning.

hackernews · ai2027 · Jul 30, 15:15 · [Discussion](https://news.ycombinator.com/item?id=49111237)

**Background**: Traditional robotics AI often relies on task-specific programming and lacks the flexibility to handle unstructured environments. Vision-language-action models (VLAs) like Gemini Robotics 2 combine visual perception, language understanding, and motor control into a single system, allowing robots to understand and execute natural language commands in real-world settings. Whole-body intelligence means the robot coordinates its entire body—not just arms or legs—to perform tasks dynamically.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body... — Google DeepMind</a></li>
<li><a href="https://www.humanoidsdaily.com/news/google-deepmind-unveils-gemini-robotics-2-bringing-whole-body-intelligence-and-multi-robot-teams-to-physical-ai">Google DeepMind Unveils Gemini Robotics 2, Bringing Whole - Body ...</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: a DeepMind researcher praised the lab's breadth of work, while others noted the robots appear slow and highlighted ongoing actuator limitations in humanoid robotics. Some commenters expressed optimism that progress could mirror LLM-like rapid improvements, while others remain skeptical about hardware constraints.

**Tags**: `#robotics`, `#AI`, `#DeepMind`, `#Gemini`, `#machine learning`

---

<a id="item-9"></a>
## [OpenAI Cuts GPT-5.6 Luna Cost by 80%](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) ⭐️ 8.0/10

OpenAI announced GPT-5.6 Luna, a cost-efficient model that is 80% cheaper and faster than previous versions, available starting today. This dramatic price reduction marks a turning point in AI model economics, enabling high-volume inference at a fraction of previous costs and spurring competition among AI providers to lower prices further. Pricing is set at $0.10 per million input tokens and $0.60 per million output tokens, with a context window of 1,050,000 tokens and maximum output of 128,000 tokens; the company also introduced higher-tier models Sol and Terra in the GPT-5.6 family.

hackernews · tedsanders · Jul 30, 17:15 · [Discussion](https://news.ycombinator.com/item?id=49112867)

**Background**: Inference cost—the compute expense for generating model outputs—has been a major barrier to widespread AI adoption. Recent optimizations have driven costs down rapidly, with GPT-3.5-level inference costs dropping over 280-fold from late 2022 to late 2024. OpenAI's latest move continues this trend, making frontier AI more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.6-luna">GPT-5.6 Luna Model | OpenAI API</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-luna">GPT-5.6 Luna - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the 80% price cut, with some comparing it to the dial-up-to-broadband transition and noting the potential for running 5× more parallel agents. Others debated whether the cost reductions truly add up to billions in savings and highlighted the challenge of separating trivial from non-trivial tasks when choosing a model.

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI pricing`, `#language models`, `#inference cost`

---

<a id="item-10"></a>
## [Refactoring Economic Benefits in the Age of AI](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html) ⭐️ 8.0/10

Martin Fowler analyzes the economic benefits of refactoring in the context of generative AI, asserting that best practices for human developers apply equally to AI assistants. This analysis provides a specific, grounded, and quantitative perspective on how AI tools impact software engineering economics, countering vague AI commentary. The article ties refactoring to reduced token consumption and improved reasoning ability in AI models, arguing that cleaner code enables more intelligent AI behavior.

hackernews · javaeeeee · Jul 30, 15:10 · [Discussion](https://news.ycombinator.com/item?id=49111176)

**Background**: Refactoring is the process of restructuring existing code without changing its external behavior, aimed at improving readability, maintainability, and reducing complexity. In the context of AI, refactoring can optimize the context window for large language models, leading to better performance and lower costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/top-content/technology/software-engineering-principles/when-software-refactoring-is-not-worthwhile/">When Software Refactoring Is Not Worthwhile</a></li>
<li><a href="https://wasrek.medium.com/bad-smell-and-refactoring-software-engineering-5bb07809b86d">Bad Smell and Refactoring | Software Engineering | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters highlight that best practices for human programmers are being rediscovered for AI, praising the article's grounded approach but questioning whether AI can truly understand the big picture of a project. Some note that refactoring benefits extend beyond token costs to enhance model reasoning.

**Tags**: `#refactoring`, `#generative AI`, `#software engineering`, `#best practices`, `#economics`

---

<a id="item-11"></a>
## [GCC adopts human-oversight policy for AI contributions](https://lwn.net/Articles/1086041/) ⭐️ 8.0/10

The GCC steering committee has announced a new policy that requires human oversight for all AI-generated contributions, ensuring a human is accountable before code is merged. This policy sets a precedent for open-source projects grappling with AI-generated code, emphasizing human accountability and addressing concerns about low-quality automated contributions. The policy material is hosted on sourceware.org and mirrors LLVM's existing AI tool policy, which also requires a human in the loop for LLM-generated code or text.

hackernews · arto · Jul 30, 11:45 · [Discussion](https://news.ycombinator.com/item?id=49108685)

**Background**: GCC (GNU Compiler Collection) is a key open-source compiler suite. As large language models (LLMs) become popular, projects like GCC face an influx of AI-generated patches, prompting the need for clear contribution guidelines to maintain quality and accountability.

**Discussion**: Commenters generally welcomed the policy, noting it aligns with LLVM's approach. Some highlighted the issue of low-effort AI-generated PRs, while others praised GNU's inclusive tone in guiding new contributors.

**Tags**: `#GCC`, `#AI policy`, `#open source`, `#contribution guidelines`, `#LLM`

---

<a id="item-12"></a>
## [Professor loses PhD students over review process](https://www.reddit.com/r/MachineLearning/comments/1vawwb8/i_have_lost_three_and_a_half_potential_phd/) ⭐️ 8.0/10

An early-career professor reports losing three and a half potential PhD students because the students were demoralized by the conference peer review process, despite producing high-quality papers with positive reviews. This highlights a systemic issue in machine learning research where the peer review process—especially at top conferences—can deter talented young researchers from pursuing a PhD, threatening the future pipeline of researchers. The papers received very positive reviews (e.g., four unanimous weak accepts) but were still rejected, leading to endless resubmission cycles where addressing previous concerns only introduced new random criticisms. The professor has over 10 years of experience at top conferences and judged the work well above the acceptance bar.

reddit · r/MachineLearning · /u/AffectionateLife5693 · Jul 30, 15:30

**Background**: In machine learning research, top conferences (like NeurIPS, ICML, ICLR) are the primary venues for publishing, and acceptance is highly competitive. The peer review process is often criticized for its randomness, inconsistency, and high rejection rates, leading to multiple resubmissions. This pressure can demotivate early-career researchers and students considering a PhD in the field.

**Tags**: `#ML research`, `#peer review`, `#PhD education`, `#academic culture`

---

<a id="item-13"></a>
## [MLVC: A Multi-Platform Learned Video Codec Nearing Real-World Deployment](https://www.reddit.com/r/MachineLearning/comments/1vb3xwd/mlvc_multiplatform_learned_video_codec_for/) ⭐️ 8.0/10

MLVC is a learned video codec that solves cross-platform incompatibility by explicitly transmitting entropy-model scale parameters through the hyperprior, enabling bit-exact decoding across different NPUs without requiring identical hardware. This addresses a key barrier preventing learned video codecs from replacing traditional codecs like H.264/AV1 in real-world applications, potentially enabling efficient AI-based video compression on diverse hardware. MLVC achieves ~100 FPS for 360p/540p video on consumer NPUs, and it circumvents the need for fully standardized fixed-point arithmetic by avoiding bit-exact neural network execution across platforms.

reddit · r/MachineLearning · /u/tanelai · Jul 30, 19:40

**Background**: Traditional video codecs like H.264, H.265, and AV1 rely on hand-engineered algorithms and have widespread hardware acceleration, making them computationally cheap. Learned video codecs use neural networks to outperform traditional codecs in compression efficiency, but have struggled with high compute requirements and cross-platform reproducibility due to numerical differences in entropy model inference.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.28027">MLVC: A Multi-platform Learned Video Codec for Real-World...</a></li>
<li><a href="https://www.forasoft.com/learn/video-encoding/articles/key-scientific-breakthroughs-codecs">Key Scientific Breakthroughs Behind Video Codecs : Information Theory</a></li>

</ul>
</details>

**Tags**: `#video codec`, `#machine learning`, `#AI`, `#compression`, `#deployment`

---

<a id="item-14"></a>
## [UK CMA Proposes Allowing App Developers to Direct Users to Alternative Payments](https://t.me/zaihuapd/42855) ⭐️ 8.0/10

On June 30, the UK's Competition and Markets Authority proposed allowing app developers to direct users to payment options outside Apple and Google's app stores, aiming to reduce fees and boost competition. This could significantly lower costs for developers and consumers, potentially forcing Apple and Google to revise their commission structures, and set a precedent for digital market regulation globally. The CMA also proposed that if Apple or Google charge fees for directing users, those fees must be fair and lower than current commissions, with savings passed to consumers or used for innovation. Additionally, the CMA is considering requiring Apple to open its NFC technology for contactless payments in iOS apps.

telegram · zaihuapd · Jul 30, 02:10

**Background**: Currently, Apple and Google require many app developers to use their in-app payment systems, which charge commissions of 15-30%. The UK's new digital markets regime gives the CMA power to regulate firms with strategic market status. Near-field communication (NFC) is a technology enabling contactless payments; Apple has restricted access to its NFC chip in iPhones.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Contactless_payment">Contactless payment - Wikipedia</a></li>
<li><a href="https://www.android.com/intl/en_uk/articles/how-to-turn-on-nfc/">How to Turn On NFC Settings for Contactless Payments | Android</a></li>

</ul>
</details>

**Tags**: `#regulation`, `#Apple`, `#Google`, `#app store`, `#antitrust`

---

<a id="item-15"></a>
## [EU launches AI super factory tender to mobilize €30B](https://www.wsj.com/world/europe/eu-opens-call-for-creation-of-local-ai-gigafactories-c286213d) ⭐️ 8.0/10

The European Commission opened a tender for up to seven AI 'super factories' on Thursday, aiming to mobilize approximately €30 billion in investment, with €10 billion coming from EU and member state funds. This initiative signals the EU's strategic push to build domestic AI infrastructure and compete globally with the US and China, potentially accelerating AI research and deployment across Europe. Bids must be submitted by November 12, with winners announced by July 2027, and projects must become operational within 18 months of signing. The tender covers site selection and expansion of existing facilities.

telegram · zaihuapd · Jul 30, 11:50

**Background**: AI factories are ecosystems that provide one-stop access to high-performance computing (HPC), data, and skills for AI developers. The EU has been investing in supercomputing infrastructure, and this tender is part of a broader plan to upgrade 12 scientific supercomputing centers into AI factories.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sango-automation.com/news/europe-s-huge-investment-in-building-ai-super-84958381.html">Europe 's Huge Investment in Building AI Super Factories Will Face...</a></li>
<li><a href="https://csc.fi/en/media-release/new-pan-european-supercomputer-and-eu-ai-factory-in-finland/">A new pan- European supercomputer and a European Union AI ... - CSC</a></li>

</ul>
</details>

**Tags**: `#AI`, `#EU Policy`, `#Supercomputing`, `#Investment`

---