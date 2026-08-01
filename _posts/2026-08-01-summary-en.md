---
layout: default
title: "Horizon Summary: 2026-08-01 (EN)"
date: 2026-08-01
lang: en
---

> From 37 items, 7 important content pieces were selected

---

1. [OpenAI's Astra Model Solves Ten Long-Standing Math Problems](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Flash 0731: 304B Agentic Model Offers Top Value](#item-2) ⭐️ 8.0/10
3. [Stateless MCP 2.0 revives interest; inspires mcp-explorer and datasette-mcp](#item-3) ⭐️ 8.0/10
4. [KataGo Study Probes Internal Symmetry of Superhuman Go Networks](#item-4) ⭐️ 8.0/10
5. [Google Confirms Two-Tier Verification for Android Sideloaded Apps](#item-5) ⭐️ 8.0/10
6. [EA Acquired by Saudi-Led Consortium for $55 Billion](#item-6) ⭐️ 8.0/10
7. [Microsoft confirms Copilot 'super app' launching this year](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI's Astra Model Solves Ten Long-Standing Math Problems](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 9.0/10

OpenAI announced that an internal version of its next major model, Astra, solved ten mathematical problems that had seen no progress for at least a decade. The company spent less than $2,000 per problem at GPT-5.6 Sol token prices, and released Lean 4 formalizations, a paper, and an LLM-generated reasoning walkthrough. This marks a major milestone in AI-driven mathematical research, showing that frontier models can produce original, verifiable results at remarkably low cost. Coming right after Anthropic's Claude Mythos cryptographic discovery, it signals an accelerating shift toward what Terence Tao calls 'big mathematics' — large-scale human-machine collaboration. The ten problems span group theory, high-dimensional geometry, coding theory, quantum complexity, lattice cryptography, and extremal combinatorics. OpenAI has not disclosed how many additional problems were attempted without success, and the exact prompts used by the model have not been published.

rss · Simon Willison · Aug 1, 20:34

**Background**: Astra is OpenAI's next model family, designed to let multiple agents collaboratively tackle complex problems over hours or days. The proofs were formalized in Lean 4, a proof assistant that allows mathematical arguments to be checked mechanically. This follows a broader trend of AI systems being used to explore mathematical conjectures, and aligns with mathematician Terence Tao's vision of 'big mathematics,' where AI handles technical grunt work while humans claim the creative parts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bitsminds.com/news/openai-astra-ten-open-math-problems-lean-proofs-2026">OpenAI Names Its Next Model Family Astra — and Says It Solved ...</a></li>
<li><a href="https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/">OpenAI announces its "next major model" Astra by dropping ten ...</a></li>

</ul>
</details>

**Discussion**: Discussion on Hacker News and among mathematicians online has been a mix of excitement and skepticism. Commenters highlighted the remarkable cost efficiency, but also flagged the lack of published failures and the absence of the actual prompts as important caveats.

**Tags**: `#AI research`, `#mathematics`, `#OpenAI`, `#LLMs`, `#theoretical computer science`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731: 304B Agentic Model Offers Top Value](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek released DeepSeek-V4-Flash-0731, a 304B-parameter model (167GB on Hugging Face) with substantially enhanced agentic capabilities, priced at $0.14 per million input tokens and $0.27 per million output tokens. Artificial Analysis ranks it ahead of MiniMax M3 (428B parameters) and calls it possibly the best value-per-intelligence model available. This release strengthens DeepSeek's position in the cost-efficient LLM segment, showing that a smaller model can rival or beat much larger ones on agentic workloads. Its aggressive pricing could pressure other providers and make advanced AI more accessible for high-volume agentic applications. The model shows strong results on the Artificial Analysis Intelligence Index (v4.1) and its cost-per-task chart, where it sits alone in the most attractive quadrant at roughly $0.028 per task with an intelligence score around 50. Output quality depends on reasoning effort: using the default reasoning level via OpenRouter produced a flawed pelican image, while setting `reasoning_effort high` yielded a much better result.

rss · Simon Willison · Jul 31, 23:59

**Background**: Artificial Analysis is an independent platform that benchmarks LLMs using an Intelligence Index that aggregates multiple evaluation metrics, and it publishes cost-per-task comparisons. DeepSeek-V4-Flash is part of DeepSeek's V4 family; DeepSeek's API docs note its reasoning capabilities closely approach V4-Pro while being smaller, faster, and cheaper, and OpenRouter observed that within a month of V4's release, Flash captured 70% of DeepSeek's agentic token flow.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence , Performance, and Price</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424/">DeepSeek V 4 Preview Release | DeepSeek API Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#artificial intelligence`

---

<a id="item-3"></a>
## [Stateless MCP 2.0 revives interest; inspires mcp-explorer and datasette-mcp](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison reports that the Model Context Protocol 2.0 specification (dated 2026-07-28) introduces a stateless core, collapsing the two-round-trip session flow into a single HTTP request. He built three MCP implementations this week, including mcp-explorer and datasette-mcp. This is the most significant MCP change since the protocol launched, making MCP tools easier to audit and control than giving agents a shell with curl, and simple enough for smaller laptop-running models to drive. It could reignite MCP adoption after interest shifted toward Anthropic's Skills. The stateless approach eliminates the Mcp-Session-Id and the separate initialize request, using headers such as MCP-Protocol-Version and Mcp-Method instead. This simplifies clients and servers and removes the need to maintain server-side session state, which is a better fit for scalable web applications.

rss · Simon Willison · Jul 31, 23:13

**Background**: MCP is an open standard introduced by Anthropic in November 2024 that defines a common way for AI systems to expose and integrate external tools and data. It was widely adopted by major AI providers in 2025, but later drew less attention as Skills—another Anthropic idea—showed that a harness with terminal and curl could handle many tasks more flexibly. The new stateless specification reduces implementation complexity, renewing developer interest.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/">The 2026-07-28 MCP Specification Release Candidate</a></li>

</ul>
</details>

**Tags**: `#Model Context Protocol`, `#AI Agents`, `#Protocols`, `#Open Source`

---

<a id="item-4"></a>
## [KataGo Study Probes Internal Symmetry of Superhuman Go Networks](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

KataGo maintainer David Wu published a study analyzing how symmetrically the Go-playing neural network represents the board internally, despite no architectural enforcement of 8-fold rotational/reflectional symmetry. The writeup, driven largely by AI but human-directed, reports an unexpected finding and is accompanied by linked code. This is one of the few interpretability studies on a superhuman-level game-playing network, and it can reveal whether neural nets automatically learn orientation-invariant concepts or memorize them separately. The results could inform how symmetry priors and data augmentation are used in training strong reinforcement-learning agents. KataGo uses a standard CNN architecture with a trunk of residual blocks plus policy and value heads, and is trained with stochastic 8-fold data augmentation that randomizes board orientation per batch. Although Go rules are fully symmetric under rotation and reflection, no symmetry is hard-coded, so the degree to which internal representations become orientation-independent is an empirical question.

reddit · r/MachineLearning · /u/icosaplex · Aug 1, 16:18

**Background**: Go is a classic board game with a grid board and simple rules, yet it is extremely deep strategically, and modern engines such as KataGo learn by self-play and reinforcement learning at superhuman strength. Data augmentation such as random 8-fold orientation changes is commonly used in deep learning to build invariance, but here the study asks whether the trained network actually recruits that invariance internally. The project's model architecture is documented as a convolutional neural network with residual trunk, policy head, and value head, trained through large-scale distributed self-play.

<details><summary>References</summary>
<ul>
<li><a href="https://deepwiki.com/lightvector/KataGo/7.2-model-architecture">Model Architecture | lightvector/ KataGo | DeepWiki</a></li>
<li><a href="https://katagotraining.org/">KataGo Distributed Training</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#interpretability`, `#go`, `#symmetry`, `#neural-networks`

---

<a id="item-5"></a>
## [Google Confirms Two-Tier Verification for Android Sideloaded Apps](https://t.me/zaihuapd/42911) ⭐️ 8.0/10

Google confirmed it will introduce a two-tier developer verification system for sideloaded apps in Android 16, requiring developers to register their package name and signing key. The paid tier costs $25 and the free tier requires only an email but limits installation counts. This policy significantly affects Android sideloading and open-source app stores such as F-Droid, potentially restricting app distribution outside Google Play. It also raises privacy and censorship concerns because Google will collect developer personal information even while not making the developer list public. The system verifies apps through the cloud, which may require a network connection during installation. The free tier's installation limits and the $25 fee matching Google Play's registration fee could burden indie and open-source developers, and the requirement may disrupt automated builds from repositories like F-Droid.

telegram · zaihuapd · Aug 1, 03:08

**Background**: Sideloading is the practice of installing Android apps from outside official app stores like Google Play. Android app signing uses cryptographic keys to verify that an app is genuine and untampered, and each app's signing key never changes. F-Droid is a popular repository for free and open-source Android apps, relying on automated builds and community contributions. Android 16 is the upcoming release of Google's mobile operating system, where this new developer verification system is expected to appear.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F-Droid - Wikipedia</a></li>
<li><a href="https://f-droid.org/">F-Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://developer.android.com/studio/publish/app-signing">Sign your app | Android Studio | Android Developers</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Google`, `#developer verification`, `#sideloading`, `#privacy`

---

<a id="item-6"></a>
## [EA Acquired by Saudi-Led Consortium for $55 Billion](https://www.gamersky.com/news/202607/2180618.shtml) ⭐️ 8.0/10

EA has announced that its $55 billion sale to a consortium led by Saudi Arabia's Public Investment Fund (PIF) has received all regulatory approvals, with the deal set to close on August 4, 2026. Upon completion, EA will become a private company and will no longer publish its financial results. This is the second-largest acquisition in gaming history, behind only Microsoft's $75.4 billion purchase of Activision Blizzard in 2023. The deal hands one of the West's biggest publishers to Saudi ownership, a milestone that could accelerate sovereign wealth investment in the gaming industry. The buying consortium is made up of PIF, Silver Lake, and Affinity Partners. PIF has previously taken full ownership of Scopely and Niantic, and the deal means EA's financial disclosures will cease once it goes private.

telegram · zaihuapd · Aug 1, 09:10

**Background**: EA is one of the world's largest game publishers, known for franchises such as EA Sports FC (FIFA), Madden, Battlefield, and The Sims. The Saudi PIF has been aggressively buying gaming assets as part of the kingdom's Vision 2030 economic diversification plan. The deal follows a wave of consolidation in the industry, with Microsoft's acquisition of Activision Blizzard in 2023 serving as the largest benchmark.

**Tags**: `#Electronic Arts`, `#Gaming Industry`, `#M&A`, `#Saudi PIF`, `#Business News`

---

<a id="item-7"></a>
## [Microsoft confirms Copilot 'super app' launching this year](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

Microsoft CEO Satya Nadella confirmed on the company's earnings call that Microsoft will release an AI 'super app' this year, integrating Copilot's chat, coding, and agentic capabilities for both consumer and business users. The app will merge Copilot, GitHub Copilot, Copilot Cowork, and Autopilot systems into a single experience. This is a major strategic move to unify Microsoft's fragmented AI products into a single platform, which could reshape how users interact with AI assistants and autonomous agents. It also intensifies competition with OpenAI's ChatGPT Work and Anthropic's Claude Cowork ecosystem. The super app will combine chat, coding features, Copilot Cowork, and Autopilot systems, with code functionality included this quarter. Microsoft's latest quarterly revenue grew to $90 billion, driven primarily by AI and cloud businesses.

telegram · zaihuapd · Aug 1, 13:18

**Background**: A super app is a single mobile or web application that offers multiple services, such as messaging, payments, and productivity tools. Microsoft's Copilot is an AI assistant embedded across its products, while Copilot Cowork automates multi-step workflows and Autopilot systems handle goal-driven tasks. Agentic AI refers to software that can autonomously reason and initiate tasks rather than just respond to prompts. This announcement follows Microsoft integrating technology behind Anthropic's Claude Cowork into Microsoft 365 Copilot, and OpenAI launching its own combined ChatGPT Work app.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/microsoft-365-copilot/cowork">Copilot Cowork: Automate Tasks and Workflows | Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Super_app">Super app - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents? | IBM</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#Copilot`, `#AI`, `#Super App`, `#Agents`

---