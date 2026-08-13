---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 29 items, 9 important content pieces were selected

---

1. [Spaghettifying DRAM: Exploiting DRAM Addressing for Ring-0 Privilege Escalation](#item-1) ⭐️ 9.0/10
2. [Introducing Gemini 3.7 Flash: Google's Most Intelligent Workhorse Model](#item-2) ⭐️ 8.0/10
3. [Cerebras and OpenAI launch GPT-5.6 Sol Ultrafast, claiming 7x faster HLE inference](#item-3) ⭐️ 8.0/10
4. [DeepSeek Releases Open-Source Agent Harness Developer Preview](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4 Pro 0813 Launches via OpenRouter, Open Weights Likely](#item-5) ⭐️ 8.0/10
6. [Apple Reportedly in Talks to License News for Siri AI, Budget in Nine Figures](#item-6) ⭐️ 8.0/10
7. [DeepMind's SL2T Brings Sign-Language-to-Text AI to Pixel 11](#item-7) ⭐️ 8.0/10
8. [OpenAI Upgrades ChatGPT to GPT-5.6 Series, Expands Free Access](#item-8) ⭐️ 8.0/10
9. [Google launches Gemini 3.6 Flash, confirms Gemini 4 pretraining has begun](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Spaghettifying DRAM: Exploiting DRAM Addressing for Ring-0 Privilege Escalation](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

Security researcher Christopher Domas has released a new attack technique and tool, 'skitter-creek-bath-salts,' that exploits the DRAM controller's address translation registers to escalate from ring-0 kernel access to deeper, more privileged CPU modes on AMD Family 16h CPUs. The research is being presented at Black Hat alongside the open-source proof-of-concept. This is significant because it demonstrates a hardware-level attack surface that bypasses traditional software security boundaries, allowing ring-0 attackers to reach SMM or other hidden modes that typically host firmware and hypervisors. The technique could affect a wide range of AMD processors and raises new questions about the security of undocumented DRAM controller features. According to the project README, the exploit was developed and tested on AMD Family 16h (Jaguar) CPUs, the last generation whose datasheets document the DRAM controller's translation registers and show that they cannot be locked. The researcher notes that newer Zen 3 processors use a different base address for the memory controller registers, so the technique may not directly apply to them.

hackernews · matt_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**Background**: DRAM addressing refers to how the memory controller maps physical memory addresses to the row, column, bank, and channel locations inside DRAM chips; this mapping is often performed by undocumented translation registers. CPU privilege levels, or 'rings,' protect the OS kernel (ring 0) from user processes, but deeper modes like System Management Mode run at an even higher privilege and are normally hidden. Previous research, such as the DRAMA project, already showed that DRAM addressing can be reverse-engineered and exploited for side-channel attacks. This new work goes further by manipulating those registers to break the isolation between ring 0 and more privileged execution environments.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49286341">Spaghettifying DRAM | Hacker News</a></li>
<li><a href="https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_pessl.pdf">PDF DRAMA: Exploiting DRAM Addressing for Cross-CPU Attacks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Protection_ring">Protection ring - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Comments on Hacker News mostly expressed excitement and admiration for Christopher Domas' work, with users eagerly anticipating the Black Hat talk. Some commenters reflected on how DRAM has become a giant attack surface, while others asked about the exploit's applicability to newer CPUs and whether other processor families are affected. A few speculated that console manufacturers like Xbox and PlayStation could be concerned about this kind of hardware-level escape.

**Tags**: `#security`, `#DRAM`, `#exploit`, `#ring-0`, `#hardware`

---

<a id="item-2"></a>
## [Introducing Gemini 3.7 Flash: Google's Most Intelligent Workhorse Model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

Google announced Gemini 3.7 Flash, a new AI model for coding and agentic tasks, released just three weeks after Gemini 3.6 Flash. It delivers substantial improvements over prior Flash models, including a 2.6-point gain on the Legal Agent Bench all-pass metric. As the latest in Google's cost-efficient Flash line, this release matters for developers who need strong coding and vision performance at a lower price point. Community reactions show it is being compared directly against competitors like GPT-5.6 Luna and Opus 5, signaling its role in the fast-moving AI model race. The model's introductory pricing is scheduled to double on December 31, 2026, which some commenters find unusual. Early hands-on tests highlight strong image-to-HTML and SVG-rendering capabilities, while comparisons note that rivals like Opus 5 and Luna still lead in certain benchmarks.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**Background**: Gemini is a family of multimodal large language models developed by Google DeepMind, which succeeded LaMDA and PaLM 2 and powers the Gemini chatbot. The Flash series is designed as low-cost, high-volume 'workhorse' models commonly used for summarization, parsing, formatting, and coding agent tasks, prioritizing efficiency alongside capability.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash - Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_2.5_Flash_Image">Gemini 2.5 Flash Image</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some users praise Gemini 3.7 Flash's vision and coding performance relative to its price, while others are skeptical about the pricing schedule and note that GPT-5.6 Luna and Opus 5 still outrank it on certain benchmarks. There are also calls for direct comparisons against Luna and Terra, with one commenter arguing Luna's cheaper pricing undercuts the need for Flash.

**Tags**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#model release`

---

<a id="item-3"></a>
## [Cerebras and OpenAI launch GPT-5.6 Sol Ultrafast, claiming 7x faster HLE inference](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras and OpenAI announced Ultrafast mode for GPT-5.6 Sol, powered by Cerebras hardware, delivering up to 750 output tokens per second and up to 14x faster processing. In evaluations, it answered all 2,500 HLE questions in 11 hours and 11 minutes, about 7x faster than Claude Fable 5, with comparable accuracy. This milestone demonstrates that specialized AI hardware can dramatically accelerate frontier-scale language models, potentially reshaping inference cost and latency expectations. It could benefit time-sensitive and mission-critical applications, and intensify competition among AI infrastructure providers. OpenAI's preview states Ultrafast runs GPT-5.6 Sol up to 14x faster with up to 750 output tokens per second, and Cerebras claims no quality compromise. However, no pricing information has been released, and some commenters note the companies have not explicitly stated that Ultrafast performs identically to the regular Sol model.

hackernews · pr337h4m · Aug 13, 18:10 · [Discussion](https://news.ycombinator.com/item?id=49289844)

**Background**: Cerebras Systems develops wafer-scale engines (WSE) and CS-3 supercomputers, along with AI inference and training cloud APIs that allow access without purchasing hardware. Humanity's Last Exam (HLE) is a benchmark of 2,500 expert-vetted questions spanning mathematics, sciences, and humanities, designed to push the limits of AI evaluation. Ultrafast is a new OpenAI API service tier initially available to a select group of customers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Humanity's_Last_Exam">Humanity's Last Exam - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are generally excited about faster inference but skeptical of the performance parity claim, noting the absence of explicit confirmation that Ultrafast matches the standard Sol model's accuracy on all benchmarks. Some point out the lack of pricing information, wondering if it will be premium or simply a market test. A few also note that speed improvements could benefit large-scale codebases and testing workloads, while others see this as competitive pressure on other hardware vendors.

**Tags**: `#AI`, `#OpenAI`, `#hardware`, `#performance`, `#GPT`

---

<a id="item-4"></a>
## [DeepSeek Releases Open-Source Agent Harness Developer Preview](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek has released an open-source developer preview of its DeepSeek Harness agent harness, licensed under MIT. It includes full run traceability via append-only session logs, a trajectory inspection view, and hot-reloadable plugin architecture. For a major AI lab like DeepSeek to open-source this, it pushes agent tooling toward standards where every run can be audited, replayed, and resumed, which is critical for debugging and trust in autonomous agents. The release also highlights how traceability is becoming a key differentiator in the rapidly evolving LLM agent ecosystem. The harness is built on Cordis v4, which enables hot-loading and unloading plugins without restarting a process, including cleanup of side effects and dependent modules. All major operations — resume, fork, search, and replay — operate on the same append-only event stream, and the project is still at an early preview stage with compatibility-breaking changes expected.

hackernews · bjin · Aug 13, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**Background**: An agent harness is the structural layer that connects an LLM to tools, memory, and execution logic, letting models do things rather than just generate text. Session replay is a debugging technique that records user or system interactions so developers can see exactly what led to an issue. Hot-reloadable plugin architectures allow code changes to be applied at runtime without restarting the process, speeding up development and enabling dynamic enable/disable of components.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/vinit-tomar_harness-harness-contextinjection-activity-7450227892724334592-TdxO">Agent Harness : The Structural Layer for LLM Execution | LinkedIn</a></li>
<li><a href="https://sentry-io.nproxy.org/product/session-replay/">Session Replay : See What Users See, Fix What Broke | Sentry</a></li>
<li><a href="https://github.com/veemex/open-reload">GitHub - veemex/open-reload: Hot-reload MCP meta-plugin for OpenCode — watches plugin files and dynamically reloads tools at runtime</a></li>

</ul>
</details>

**Discussion**: Commenters were largely enthusiastic, calling the append-only traceability a 'killer feature' compared with encrypted or obfuscated traces in some proprietary US models. One author confirmed it is an early MIT-licensed preview and welcomed feedback, while others noted it leverages Cordis v4, and some expressed 'plugin fatigue' over the everything-is-a-plugin design.

**Tags**: `#agent-harness`, `#deepseek`, `#LLM-agents`, `#traceability`, `#open-source`

---

<a id="item-5"></a>
## [DeepSeek V4 Pro 0813 Launches via OpenRouter, Open Weights Likely](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek V4 Pro 0813 is now available via API on OpenRouter, with open weights also appearing on Hugging Face. The model produces markedly different outputs across low, medium, and high reasoning levels, a behavior Simon Willison says he has not observed in other models. As a likely open-weight release from a major Chinese AI lab, this strengthens DeepSeek's position in the open AI ecosystem and expands options for developers. The observed reasoning-level output differences also raise interesting questions about how these settings change model behavior in production use. The model was initially available only via API on OpenRouter, and DeepSeek has not published an official announcement page. Benchmarks were shared from the official DeepSeek WeChat group, deleted from Reddit as low-effort, and then reposted to Hacker News; the Hugging Face weights page also briefly returned a 404 before being restored.

rss · Simon Willison · Aug 12, 23:59

**Background**: OpenRouter is a unified API gateway that lets developers access hundreds of LLMs through a single endpoint, handling fallbacks and pricing. Open-weight models publicly release the trained neural network parameters, allowing anyone to download and run them, though they may not include the full training data. Reasoning levels in modern LLMs control how much chain-of-thought computation the model performs before answering, which can affect output quality and style.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/docs/quickstart">OpenRouter Quickstart Guide</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.ibm.com/think/topics/reasoning-model">What Is a Reasoning Model? | IBM</a></li>

</ul>
</details>

**Discussion**: Community discussion was fragmented: the Reddit post containing benchmark data was removed by moderators for being low-effort, while Hacker News hosted the results in an ASCII-art table. On Telegram, users noted the Hugging Face weight page briefly went 404 before being restored, causing a moment of uncertainty about whether the open weights were actually available.

**Tags**: `#deepseek`, `#ai`, `#model-release`, `#openrouter`, `#machine-learning`

---

<a id="item-6"></a>
## [Apple Reportedly in Talks to License News for Siri AI, Budget in Nine Figures](https://9to5mac.com/2026/08/12/report-apple-seeks-publisher-deals-to-give-siri-ai-better-access-to-current-events/) ⭐️ 8.0/10

According to a report published on August 12, 2026, Apple is in discussions with publishers to license news content for Siri AI, potentially paying usage-based fees under multi-year deals. The reported budget could reach nine figures, though Apple has not announced any partnerships. This marks a significant shift in AI data licensing economics, as Apple appears to favor usage-based payments over the fixed upfront fees typical of other AI companies. If confirmed, the move could reshape how publishers negotiate with AI developers and affect the broader AI training-data market. The agreements under discussion are multi-year content licenses specifically aimed at giving Siri AI access to current news and information. The report remains unconfirmed—Apple declined to comment—and Siri AI is expected to launch later in 2026.

telegram · zaihuapd · Aug 13, 04:40

**Background**: Siri is Apple's voice assistant that handles commands, searches the internet, and interacts with iOS apps. In June 2026, Apple introduced Siri AI, a completely reimagined version powered by the next generation of Apple Intelligence, offering natural back-and-forth conversation and more capable assistance. AI companies often license copyrighted content, such as news articles, to train models or power real-time answers, typically through fixed upfront payments—a model Apple's reported usage-based approach would break from.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Siri">Siri - Wikipedia</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri</a></li>
<li><a href="https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/">Apple introduces Siri AI, a profoundly more capable and ...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Siri AI`, `#News Licensing`, `#AI`

---

<a id="item-7"></a>
## [DeepMind's SL2T Brings Sign-Language-to-Text AI to Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

Google DeepMind released SL2T, a massively multilingual sign-language-to-text model, and is rolling it out to Pixel 11 devices in Gboard and Live Transcribe. It initially supports American Sign Language (ASL) to English translation, marking the first time sign language AI ships in a consumer product. This is a significant accessibility milestone, bringing real-time sign-to-text dictation to everyday smartphones rather than leaving it in research labs. The on-device, privacy-preserving design and strong zero-shot performance could set a new bar for inclusive AI and spur broader language coverage across the industry. SL2T was trained on more than 100,000 hours of sign language video across over 50 sign languages, and scores 70 BLEURT on the FLEURS-ASL benchmark in zero-shot ASL-to-English translation. To protect privacy, the model processes only hand and body keypoints from the video rather than the raw pixels.

telegram · zaihuapd · Aug 13, 08:55

**Background**: FLEURS-ASL is a benchmark dataset that extends the FLORES/FLEURS parallel corpora to American Sign Language, providing a standard way to measure sign-to-text translation quality. BLEURT is a neural text-generation metric that compares a candidate translation with a reference to approximate human judgment. Keypoint-based processing means the model sees landmarks representing the hands, face, and body, which is essential for keeping computation on-device and respecting user privacy in products like Gboard and Live Transcribe.

<details><summary>References</summary>
<ul>
<li><a href="https://datanorth.ai/news/google-deepmind-releases-sl2t">Google DeepMind releases SL 2 T sign language AI - DataNorth</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/google-sign-language-model-body-landmarks">Google's new model turns sign language into text for web searches</a></li>
<li><a href="https://arxiv.org/html/2408.13585">FLEURS - ASL : Including American Sign Language in Massively...</a></li>

</ul>
</details>

**Tags**: `#DeepMind`, `#Sign Language AI`, `#Accessibility`, `#Machine Translation`, `#Pixel`

---

<a id="item-8"></a>
## [OpenAI Upgrades ChatGPT to GPT-5.6 Series, Expands Free Access](https://t.me/zaihuapd/43176) ⭐️ 8.0/10

OpenAI announced an update to ChatGPT with the GPT-5.6 model series. Paid Plus and Pro users receive GPT-5.6 Sol with more reliable factual answers and focused replies, while free users get GPT-5.6 Luna as default and unlimited text chats starting next week. This update broadens access to advanced AI reasoning, letting free users use a newer model and a Think button for harder questions. It signals OpenAI's push to make higher-quality AI assistance more accessible while deepening capabilities for paying users. The GPT-5.6 family includes three tiers: Luna, Terra, and Sol. Paid users get a new slider to control thinking depth, while free users get a Think button; internal evaluations show Luna has fewer factual errors on finance, medical, and legal questions.

telegram · zaihuapd · Aug 13, 17:04

**Background**: GPT-5.6 is a family of large language models from OpenAI, released on July 9, 2026, with variants ranked by capability: Luna, Terra, and Sol. ChatGPT is OpenAI's conversational AI assistant. The update follows a pattern of improving response reliability and giving users more control over reasoning effort. The Think button and thinking slider let users choose between quick answers and deeper, more deliberate reasoning for complex problems.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/">Improving GPT‑5.6 Sol in ChatGPT—and expanding ... - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://findskill.ai/blog/chatgpt-think-button-what-it-does/">ChatGPT's New 'Think' Button: What It Does, When to Use It</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#GPT-5.6`, `#AI`, `#Model Update`

---

<a id="item-9"></a>
## [Google launches Gemini 3.6 Flash, confirms Gemini 4 pretraining has begun](https://t.me/zaihuapd/43177) ⭐️ 8.0/10

Google released Gemini 3.6 Flash on July 21, 2026, with 17% fewer output tokens than Gemini 3.5 Flash, improved code generation, knowledge work, and computer use, plus a knowledge cutoff of March 2026. Google also confirmed that pretraining for Gemini 4 has begun, calling it its 'most ambitious pre-training run yet.' The release strengthens Google's Flash lineup for efficient agentic workflows at a competitive price, while the Gemini 4 pretraining announcement signals Google's continued push in frontier AI. Developers and enterprises relying on cost-effective, high-throughput LLMs will be directly affected. Gemini 3.6 Flash is priced at $1.5 per million input tokens and $7.5 per million output tokens, and completes multi-step tasks with fewer reasoning steps and tool calls. Google also introduced Gemini 3.5 Flash-Lite and 3.5 Flash Cyber alongside the new model.

telegram · zaihuapd · Aug 13, 17:32

**Background**: Gemini is a family of multimodal large language models developed by Google DeepMind, succeeding LaMDA and PaLM 2. The Flash series is designed to balance efficiency and quality for scaling agentic workflows. Pretraining is the initial resource-intensive phase in which a model learns from large datasets before fine-tuning and deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/">3 . 6 Flash , 3.5 Flash -Lite, and 3.5 Flash Cyber</a></li>
<li><a href="https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/">Google launches Gemini 3 . 6 Flash and teases Gemini 4</a></li>
<li><a href="https://felloai.com/all-we-know-about-google-gemini-4/">Gemini 4: Release Date, Pre-Training News & Rumors</a></li>

</ul>
</details>

**Tags**: `#Google`, `#Gemini`, `#AI model release`, `#LLM`, `#Machine Learning`

---