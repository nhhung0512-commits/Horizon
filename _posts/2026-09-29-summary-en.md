---
layout: default
title: "Horizon Summary: 2026-09-29 (EN)"
date: 2026-09-29
lang: en
---

> From 36 items, 3 important content pieces were selected

---

1. [AMD to acquire Fei-Fei Li's World Labs for $8.2 billion](#item-1) ⭐️ 9.0/10
2. [OpenAI DevDay 2026: Dots agents, GPT-6.1 models and 20+ updates](#item-2) ⭐️ 9.0/10
3. [Privacy Analysis Exposes Tracking in Web and Mobile AI Chat Agents](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AMD to acquire Fei-Fei Li's World Labs for $8.2 billion](https://ir.amd.com/news-events/press-releases/detail/1299/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute) ⭐️ 9.0/10

AMD announced it will acquire World Labs, the world-model startup founded by Fei-Fei Li, for $8.2 billion, with the deal expected to close by the end of the year pending regulatory approval. Li will join AMD as Executive Vice President and Chief Scientist, and World Labs' model research will be combined with AMD's chips and compute platforms. This is one of the largest AI acquisitions of the year and a direct escalation of AMD's rivalry with Nvidia, whose Isaac Sim and Omniverse tools dominate robotics simulation and physical AI. Bringing a foundational AI researcher of Li's stature in-house signals that AMD intends to compete not just on raw accelerators but on the models and software stack that drive robotics, autonomous systems, and interactive world generation. World Labs builds world models that perceive, generate, reason about and interact with virtual and physical environments, and its technology can also generate the simulated environments used to train robots. The $8.2 billion price tag and the fact that the transaction still requires regulatory approval mean the deal could take months to complete and could face antitrust scrutiny given the current AI consolidation wave.

telegram · zaihuapd · Sep 29, 03:59

**Background**: A world model is a machine learning system that builds an internal representation of an environment and predicts how that environment changes in response to actions, letting agents plan and reason instead of learning only through costly real-world trial and error. Unlike large language models, which predict text, world models capture physics, object interactions and causality, and early ideas date back to the 1990s. Modern versions power robots, autonomous driving and interactive video generation, and World Labs has published work such as Atlas, a world model aimed at spatial intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/09/amd-acquires-world-labs-ai-pioneer-fei-fei-lis-world-models-startup/">AMD acquires World Labs AI startup, upping the ante against ...</a></li>
<li><a href="https://www.worldlabs.ai/blog/atlas">Atlas: A World Model for Spatial Intelligence - World Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#AMD`, `#Acquisition`, `#World Models`, `#Robotics`

---

<a id="item-2"></a>
## [OpenAI DevDay 2026: Dots agents, GPT-6.1 models and 20+ updates](https://openai.com/zh-Hant/index/devday-2026-recap/) ⭐️ 9.0/10

At its DevDay 2026 event, OpenAI announced more than 20 updates, led by Dots — an always-on companion agent that runs around the clock, learns a user's habits, and proactively takes over long-running complex work by communicating through Slack and Teams. The company also introduced GPT-6.1 Sol, which specializes in coding and computer control at roughly one-fifth the price of comparable Astra-level intelligence, plus an Astra Ultrafast tier that is up to 8x faster (6x in the API), along with an Agents API, a Decisions API, "Sign in with ChatGPT", and a new Pro 500 plan. The release signals that OpenAI is pushing from single-turn chat models toward persistent, always-on agents that live inside a user's workflow, a direction that directly challenges Meta's Muse and reframes how developers build on top of frontier models. If always-on agents become the default interface, switching costs rise sharply for users and enterprises because work history, integrations and permissions all accumulate inside one vendor's platform. OpenAI says Ultrafast delivers up to 8x faster token generation in Codex and up to 6x in the API, with the Pro 500 tier offering 25x the compute allowance of Plus and exclusive access to Astra Ultrafast. The Decisions API is a lightweight, real-time decision interface built on the Luna model for classification, routing and agent action selection over a preset set of limited options from text or image input, while the Agents API natively exposes computer control and AWS Bedrock hosting.

telegram · zaihuapd · Sep 29, 17:52

**Background**: OpenAI's DevDay is its annual developer conference, where it typically launches new models, APIs and platform features in a single batch. "Always-on agent" refers to an AI that does not wait for a prompt but keeps running in the background, holding long-term memory and taking multi-step actions across tools — a step beyond chat assistants and short-lived coding agents like Codex. Astra is OpenAI's frontier model family, so "Ultrafast" is a premium service tier that trades higher cost for much lower latency rather than a new model capability.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-dots/">Introducing dots | OpenAI</a></li>
<li><a href="https://www.reuters.com/business/openai-takes-meta-with-always-on-dots-agent-enterprise-ai-push-2026-09-29/">OpenAI takes on Meta with dots agent in enterprise AI push | Reuters</a></li>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed | OpenAI</a></li>

</ul>
</details>

**Discussion**: Commenters were largely skeptical: several criticized the name "dots" as an unfortunate metaphor for missing content or loading spinners, joking it should have been called "motes". Others worried that always-on agents deepen platform lock-in — since work history and integrations make them effectively "your computer on the cloud" — and that OpenAI, having won users with generous Codex limits, is now pushing unnecessary products and tightening those limits, a pattern they say Anthropic followed too. A few noted the blurring overlap between Codex, ChatGPT Work and Dots, and argued Meta's Muse is the stronger consumer bet because ad subsidies can fund it indefinitely.

**Tags**: `#OpenAI`, `#AI Agents`, `#GPT-6.1`, `#Developer Conference`, `#API`

---

<a id="item-3"></a>
## [Privacy Analysis Exposes Tracking in Web and Mobile AI Chat Agents](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf) ⭐️ 8.0/10

A paper titled "Prompt like a butterfly, sting like a tracker" presents a privacy analysis of web and mobile conversational AI agents, documenting tracking practices and data leakage, including a report that ChatGPT sends unfinished prompts to its servers before the user presses send. The work, shared as a PDF and discussed on Hacker News (404 points, 128 comments), focuses on how prompt data and usage signals are transmitted by widely used AI chat services. Conversational AI agents are now used by hundreds of millions of people for everything from casual questions to sensitive work, so evidence that prompts, drafts and behavioural patterns leak to vendors or advertisers raises serious questions about consent and confidentiality. The findings strengthen the argument for local or open-weight models and for users, engineers and regulators to treat AI chat interfaces as tracking surfaces rather than private notebooks. Commenters point to concrete mechanisms: ChatGPT periodically posts partial drafts to a `conversation/prepare` endpoint, likely to pre-warm a cache, which could also reveal writing cadence, correction style and evolving ideas; and services such as Perplexity appear to treat a UUID in the URL as sufficient privacy protection, so anyone with the link can read the full conversation. Users are also advised to check the cookie and "marketing privacy" toggles in ChatGPT settings, though it is unclear whether these disable the observed behaviour.

hackernews · damaru2 · Sep 29, 09:03 · [Discussion](https://news.ycombinator.com/item?id=49890226)

**Background**: Conversational AI agents are chat-based services — ChatGPT, Perplexity and similar tools on the web and in mobile apps — that users rely on for questions, drafting and coding help. Their interfaces typically stream user input to remote servers, and like ordinary websites they can embed cookies, analytics and advertising trackers that record behaviour. This paper examines those interfaces from a privacy-engineering perspective, asking what data leaves the user's device and when, rather than only what the model does with it after it is submitted.

**Discussion**: The Hacker News discussion is broadly critical: commenters share firsthand reports of unfinished prompts being transmitted, compare the situation to OpenAI's earlier admission that de-identified product data may have improved its models, and conclude that private prompts and results keep leaking whether through training data or ad trackers. Several argue this vindicates local and open-weight models, while others note that toggling off marketing cookies may not fix the underlying behaviour, and one commenter mocks the habit of treating a URL UUID as a privacy guarantee.

**Tags**: `#privacy`, `#conversational AI`, `#web tracking`, `#mobile security`, `#AI agents`

---