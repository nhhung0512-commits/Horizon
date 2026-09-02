---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
lang: en
---

> From 39 items, 13 important content pieces were selected

---

1. [Google releases Gemini 3.8 Flash and a dedicated cybersecurity variant](#item-1) ⭐️ 9.0/10
2. [xAI Releases Grok 4.6, Boosts Long-Running Agent Tasks and Vision Capabilities](#item-2) ⭐️ 9.0/10
3. [FBI Probes Nexus Dark Web Service Selling 153 Million Driver's License Scans](#item-3) ⭐️ 9.0/10
4. [Investigation: Three Sites Made 215,128 'Best Software' Pages for AI; Perplexity Cites Them](#item-4) ⭐️ 8.0/10
5. [Mistral AI under fire over Team-tier data-training opt-out changes](#item-5) ⭐️ 8.0/10
6. [Paint.NET Creator Uses Claude for Clean-Room Direct2D Rewrite](#item-6) ⭐️ 8.0/10
7. [Claude Fable 5.1 Launch: Big Science Benchmark Jump, Pelican Skills Tested](#item-7) ⭐️ 8.0/10
8. [Deepity C++ Library Shows Predictive Coding Matches Backprop on MNIST](#item-8) ⭐️ 8.0/10
9. [Jasper Research Releases Cookbook, Code, and Dataset for Building Text-to-Image Models](#item-9) ⭐️ 8.0/10
10. [Open-Source AI Detectors Fail 0.5% False-Positive Benchmark, Study Finds](#item-10) ⭐️ 8.0/10
11. [Alibaba releases Qwen3.8-Max-0902, tops CodeArena with 1691 points](#item-11) ⭐️ 8.0/10
12. [Nvidia in Talks to Acquire Hugging Face at Over $13 Billion Valuation](#item-12) ⭐️ 8.0/10
13. [Moonshot AI in Early Talks with US Cloud Giants on Kimi K3 Revenue Share](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google releases Gemini 3.8 Flash and a dedicated cybersecurity variant](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 9.0/10

Google has announced Gemini 3.8 Flash, an updated fast-and-economical model, along with Gemini 3.8 Flash Cyber for automated security work. The new Flash model delivers strong benchmark results, rapid generation speed, and low cost, while the Cyber version targets autonomous vulnerability discovery and patching. This release pushes frontier-level performance into a cheaper model tier, making state-of-the-art AI more accessible for developers and enterprises building AI agents. It also signals Google's rapid iteration cadence and its entry into specialized AI security, with early community benchmarks even ranking it above models like Opus 5 on certain tests. According to the model card, Gemini 3.8 Flash is built on Gemini 3.7 Flash. Matt London notes an Artificial Analysis intelligence score of 59, matching Opus 5 medium, while the announcement reports the Cyber variant achieves +7.5–9.7% higher recall on internal penetration-testing benchmarks at 2.3–5.2x lower cost; Simon Willison also demonstrated a complete HTML/JavaScript output for just 1.8 cents in 13 seconds.

hackernews · bratao · Sep 2, 15:12 · [Discussion](https://news.ycombinator.com/item?id=49537553)

**Background**: Gemini is Google DeepMind's family of multimodal large language models, capable of processing text, images, audio, and video together. The Flash line is a cheaper, lower-latency tier aimed at high-volume tasks, and Cyber is a specialized variant for security use cases such as discovering and fixing software vulnerabilities. This launch follows other Flash releases in quick succession, reinforcing Google's pattern of rapid, iterative model deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3.8 Flash and 3.8 Flash Cyber</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3 . 8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/">Google releases Gemini 3.8 Flash, its third Flash model in six weeks - Ars Technica</a></li>

</ul>
</details>

**Discussion**: Community sentiment is positive: Simon Willison highlighted the model's speed and HTML/JavaScript strength, sharing a demo that cost just 1.8 cents in 13 seconds, and Matt London said it topped the DeepSwe leaderboard, beating Opus 5. Some commenters remain cautious — Willison also flagged a possible regression on 3.8's low 'thinking effort' setting compared to 3.7, and others noted that real-world usability is still to be determined.

**Tags**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#Machine Learning`

---

<a id="item-2"></a>
## [xAI Releases Grok 4.6, Boosts Long-Running Agent Tasks and Vision Capabilities](https://t.me/zaihuapd/43559) ⭐️ 9.0/10

On August 12, 2026, xAI released Grok 4.6, building on Grok 4.5 with enhanced long-running agent and interaction tasks as well as improved vision capabilities. The model immediately became available on Cursor, Grok Build, and the API, priced at $2 per million input tokens and $6 per million output tokens, with a double-priced fast version. This release shows xAI catching up with leading frontier models, as Grok 4.6 matches GPT-5.6 Sol on the Artificial Analysis Intelligence Index. Developers and enterprises building advanced agentic and vision-heavy workflows now have another competitive option with full platform and API support. The Artificial Analysis Intelligence Index v4.1.1 combines nine benchmarks covering reasoning, coding, knowledge, scientific reasoning, instruction following, and multi-step tasks. Grok 4.6 is available through Cursor, Grok Build, and the xAI API, with a faster version priced at double the standard rate.

telegram · zaihuapd · Sep 2, 08:10

**Background**: Grok is an AI assistant built by xAI, integrated with the X social network and available as a standalone platform; Grok Build is xAI's coding agent for professional software engineering. The Artificial Analysis Intelligence Index is a composite benchmark score that measures model capabilities across reasoning, coding, knowledge, instruction following, scientific reasoning, and completing multi-step tasks. Long-running agent tasks refer to AI agents that must execute extended workflows, often involving asynchronous background operations and complex interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index v4.1.1 | Artificial Analysis</a></li>
<li><a href="https://x.ai/news/grok-build-cli">Introducing Grok Build | SpaceXAI</a></li>
<li><a href="https://grok.com/build">Grok</a></li>

</ul>
</details>

**Tags**: `#xAI`, `#Grok`, `#AI Agents`, `#Machine Learning`, `#Model Release`

---

<a id="item-3"></a>
## [FBI Probes Nexus Dark Web Service Selling 153 Million Driver's License Scans](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 9.0/10

The FBI is investigating Nexus, a newly appeared dark web service that claims to be selling 153 million U.S. and Canadian driver's license scans. After KrebsOnSecurity published its report, Nexus's site went dark and its login page was replaced by the message "This service is no longer available." Because driver's licenses contain names, addresses, birth dates, and document images, this exposed data could enable large-scale identity theft and fraud. The case underscores how sensitive records leaked from dealerships and insurance companies can still surface years later on dark web marketplaces. The exact source of the scanned IDs is unconfirmed, but researchers suspect they may be old scans stolen from car dealerships, insurance firms, and similar businesses. Nexus also claimed to offer millions of additional identity documents and medical insurance cards, expanding the potential impact beyond driver's licenses.

telegram · zaihuapd · Sep 2, 09:31

**Background**: Driver's licenses are commonly used in the U.S. and Canada as proof of identity for banking, employment, and age verification, making them a high-value target for criminals. Dark web identity services aggregate stolen or scanned ID documents from multiple breaches and sell bulk access to buyers. The shutdown of Nexus following media attention is a typical pattern in such investigations, but it does not guarantee that copies of the data were not already sold.

<details><summary>References</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/">FBI Probes Service Selling 153M+ Drivers Licenses – Krebs on Security</a></li>
<li><a href="https://www.malwarebytes.com/blog/news/2026/09/dark-web-site-puts-153-million-drivers-licenses-and-millions-more-ids-up-for-sale">153M+ driver’s licenses for sale on new dark web platform | Malwarebytes</a></li>
<li><a href="https://shattered.io/nexus-dark-web-153-million-driver-licenses-2026/">Nexus Dark Web Sells 153M Driver Licenses: FBI Probes</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#dark web`, `#identity theft`, `#privacy`

---

<a id="item-4"></a>
## [Investigation: Three Sites Made 215,128 'Best Software' Pages for AI; Perplexity Cites Them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

A new investigation by Trellner found that just three websites programmatically generated 215,128 'best software' recommendation pages designed for AI search engines, and Perplexity frequently cites those pages in its answers. The report highlights how these manufactured sources have become a common basis for AI-generated recommendations. This matters because it exposes a concrete vulnerability in how AI search tools select sources: mass-produced SEO spam can hijack AI citations and undermine the reliability of answers from Perplexity and similar assistants. Users who rely on AI recommendations may unknowingly receive content shaped by manipulative publishing at scale. According to the report, these pages are template-based 'best software' listicles optimized for visibility in AI engines—a tactic often described as programmatic SEO or generative engine optimization (GEO). Commenters also observe that LLMs tend to favor AI-generated output, and that Perplexity's push for faster responses has degraded citation quality.

hackernews · jakobgreenfeld · Sep 2, 13:59 · [Discussion](https://news.ycombinator.com/item?id=49536375)

**Background**: Perplexity is an AI-powered conversational search engine that composes answers by drawing on online sources and listing citations. Programmatic SEO uses templates and automation to publish thousands of pages targeting niche search queries. Generative Engine Optimization (GEO) goes further by optimizing content so AI assistants like Perplexity, ChatGPT, or Google AI Overviews cite and recommend it. This investigation illustrates how these legitimate techniques can be abused to manufacture authoritative-looking sources at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perplexity_AI">Perplexity AI - Wikipedia</a></li>
<li><a href="https://mangools.com/blog/programmatic-seo/">What Is Programmatic SEO & How Does It Work? | Mangools</a></li>
<li><a href="https://www.brafton.com/what-is-generative-engine-optimization/">What Is Generative Engine Optimization ( GEO )? | Brafton</a></li>

</ul>
</details>

**Discussion**: Comments broadly agree with the finding and add context: one user points out that LLMs favor LLM-generated content, another describes Perplexity confidently recommending a place that does not exist, and a third notes Perplexity's speed-over-quality shift has left references feeling like 'garbage.' Another commenter argues that models lack source skepticism and that this exploitable window will eventually close.

**Tags**: `#AI search`, `#SEO manipulation`, `#web integrity`, `#LLM reliability`, `#Perplexity`

---

<a id="item-5"></a>
## [Mistral AI under fire over Team-tier data-training opt-out changes](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) ⭐️ 8.0/10

Mistral AI has reportedly changed data-training settings for Team-tier accounts, making user input/output data eligible for model training by default and removing the ability to centrally disable this at the organization level. Mistral's help page says users retain the right to opt out, but customers say that right is harder to exercise after the change. Mistral AI has positioned itself as a privacy-conscious European alternative to US AI vendors, but this change undermines that trust among enterprise customers. If European organizations cannot rely on centralized data-governance controls, it could push them toward self-hosted models and raise scrutiny under GDPR. According to the Hacker News discussion, a Team-tier customer reports that after switching to the Team plan to use its organization dashboard and privacy settings, Mistral updated the tier so it also became enabled for training by default. The ability to centrally disable training appears to have been removed, with only the enterprise tier now excluded from default training.

hackernews · teekert · Sep 2, 12:30 · [Discussion](https://news.ycombinator.com/item?id=49535284)

**Background**: Large-language-model providers such as Mistral often use customer prompts and outputs to improve their models, and the default opt-in/opt-out policy determines whether a company's proprietary data ends up in training runs. Privacy-conscious buyers increasingly look for vendors with strong organizational controls, but settings can change after a contract is signed, eroding trust. European companies also have to consider GDPR and the AI Act, which makes default data handling a compliance issue.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49535284">Mistral trains on user input by default, except on enterprise tier</a></li>
<li><a href="https://mistral.ai/news/all-new-le-chat/">The all new le Chat: Your AI assistant for life and work | Mistral AI</a></li>

</ul>
</details>

**Discussion**: Community comments are divided: teekert provides a detailed account of privacy-first customers feeling betrayed by Mistral's changes, while rectang describes an exhausting pattern among AI vendors that erodes trust. Others like saaaaaam argue the original title is misleading because Mistral's page explicitly says users can opt out, and maz1b questions whether Mistral broke earlier promises not to train on user data. Skeptics such as 20k suggest that companies train on data with or without consent regardless of policy.

**Tags**: `#privacy`, `#AI`, `#Mistral`, `#data governance`, `#ethics`

---

<a id="item-6"></a>
## [Paint.NET Creator Uses Claude for Clean-Room Direct2D Rewrite](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Rick Brewster, the creator of Paint.NET, announced an extremely experimental WINE/Linux support mode in which the application uses a from-scratch, clean-room reimplementation of Microsoft's Direct2D API instead of the original. The rewrite, contained in PaintDotNet.Windows.Direct2D1.Managed.dll and enabled by the /wine flag, was almost entirely generated by Anthropic's Claude AI. This marks one of the largest publicly described AI-generated clean-room reverse engineering efforts, with around 180,000 lines of code, and demonstrates that LLMs can be used to recreate complex, proprietary graphics APIs. If the approach proves viable, it could help WINE and similar projects overcome long-standing compatibility hurdles and expand the reach of Windows-only .NET applications. Brewster described most of the code as 'vibe coded,' meaning it has not been thoroughly reviewed, and he noted that he cannot realistically review 180,000 lines of code at the level of care he applies to Paint.NET's existing ~700,000 lines. During development, Claude initially mishandled reference-counted COM objects (omitting AddRef equivalents), and Brewster had to intervene on resource management and architecture decisions, though he praised its reverse engineering of the formulas behind Direct2D's built-in effects library.

rss · Simon Willison · Sep 2, 05:50

**Background**: Direct2D is a hardware-accelerated, immediate-mode 2D graphics API introduced with Windows 7 that Paint.NET relies on heavily, and it has been a persistent incompatibility point under WINE, a compatibility layer that lets Windows applications run on Linux and other systems. Clean-room reverse engineering is a legal method in which a system is studied to produce a specification, and a separate team independently implements the code without direct knowledge of the original—a practice used to avoid copyright infringement. Vibe coding is an AI-assisted development style, popularized in 2025, where developers accept generated code without thorough review, trusting results and iterative prompts to shape the final software.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Clean-room_reverse_engineering">Clean-room reverse engineering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/D2D">D 2 D - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI coding`, `#Direct2D`, `#WINE`, `#Paint.NET`, `#reverse engineering`

---

<a id="item-7"></a>
## [Claude Fable 5.1 Launch: Big Science Benchmark Jump, Pelican Skills Tested](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/) ⭐️ 8.0/10

Anthropic released Claude Fable 5.1 (and Mythos 5.1) on September 1, 2026, claiming new standards for coding, knowledge work, and long-running problem-solving tasks. It scored 52.6% on the new Terminal-Bench-Science 0.1 benchmark, up from 24.7% for Fable 5, and Simon Willison tested its pelican-drawing abilities across all reasoning levels. Claude Fable 5.1 is a major Anthropic release with a dramatic leap on scientific agentic tasks, an increasingly important area for AI research assistants. Willison's hands-on pelican test offers developers a practical look at how the model handles reasoning levels, costs, and output quality. Fable 5.1 supports five reasoning levels — low, medium, high, xhigh, and max — with no option to disable reasoning entirely. In Willison's test, low and medium levels generated no visible reasoning transcripts and about 2,000 output tokens each, while high used 2,612 tokens with a reasoning trace; Anthropic also notes Fable 5.1 keeps Fable 5's input/output prices, with cache reads at a quarter of the cost.

rss · Simon Willison · Sep 1, 23:57

**Background**: Claude Fable 5 is Anthropic's publicly available 'Mythos-class' model, released in June 2026 alongside the restricted-access Claude Mythos 5; the two models share the same underlying architecture but differ in safeguards. Terminal-Bench-Science is a new benchmark for AI agents working in terminal environments on scientific tasks, first announced on August 27. The pelican benchmark, created by Simon Willison, asks a model to 'Generate an SVG of a pelican riding a bicycle' and has become an informal way to compare instruction following, visual composition, and code generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5.1 and Claude Mythos 5.1 \ Anthropic</a></li>
<li><a href="https://www.tbench.ai/">Terminal - Bench</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#benchmark`, `#LLM`

---

<a id="item-8"></a>
## [Deepity C++ Library Shows Predictive Coding Matches Backprop on MNIST](https://www.reddit.com/r/MachineLearning/comments/1w5fuhm/deepity_a_c_library_showing_predictive_coding/) ⭐️ 8.0/10

A new C++ library called Deepity implements Predictive Coding Networks accelerated by Direct Kolen-Pollack Feedback Alignment, achieving 97.73% test accuracy on MNIST in about 59.5 seconds over 50 epochs. This nearly matches PyTorch backpropagation, which reached 98.27% accuracy in roughly 70 seconds. This result closes the practical performance gap between biologically plausible predictive coding and standard backpropagation on a classic benchmark, demonstrating that alternative credit assignment can be viable on CPU without GPU acceleration. It is significant for researchers interested in local learning, continual learning, and energy-efficient training methods. The implementation combines recent research on accelerated PCNs via Direct Kolen-Pollack Feedback Alignment with algorithmic caching that bypasses redundant forward projections during the inference settling phase. The author plans to port the kernels to CUDA to scale up the architecture and test continual learning scenarios where backpropagation struggles.

reddit · r/MachineLearning · /u/Important-Home4431 · Sep 2, 16:49

**Background**: Predictive Coding Networks (PCNs) are a neuroscience-inspired alternative to backpropagation in which layers minimize local prediction errors rather than propagating a global error signal. Naive PCN implementations are notoriously slow, which has hindered their practical adoption despite their appeal for biological plausibility and continual learning. MNIST, a dataset of handwritten digits, is a standard benchmark used to compare the speed and accuracy of training algorithms.

**Tags**: `#Predictive Coding`, `#Backpropagation`, `#C++`, `#MNIST`, `#Machine Learning`

---

<a id="item-9"></a>
## [Jasper Research Releases Cookbook, Code, and Dataset for Building Text-to-Image Models](https://www.reddit.com/r/MachineLearning/comments/1w5c9rd/detailed_explanation_of_how_to_create_a/) ⭐️ 8.0/10

Jasper Research has published a detailed technical cookbook explaining how to build a text-to-image model from scratch, together with a minimal codebase called nano-t2i and a 100M-image dataset named MONET. The release includes the full reasoning and intermediate results, so readers can understand and reproduce each stage. This matters because detailed, end-to-end educational resources for training frontier text-to-image models are rare; most labs only release models or papers. It lowers the barrier for researchers, students, and engineers who want to learn how large-scale generative models are actually trained and to run their own experiments. The cookbook is available as an interactive Hugging Face Space, while nano-t2i is a minimal, hackable Apache-2.0 codebase that trains a flow-matching model end-to-end on the MONET dataset using a single NVIDIA H200 GPU and costing under $300. MONET was distilled from 2.9 billion candidate images into 104.9 million high-quality samples and includes a retrieval interface for querying by text or image.

reddit · r/MachineLearning · /u/dh7net · Sep 2, 14:40

**Background**: A text-to-image model generates images from natural-language prompts; modern systems are typically built by first collecting and cleaning a large dataset of image-text pairs and then training a generative architecture such as a diffusion or flow-matching model to transform random noise into images conditioned on text. MONET provides an openly available dataset of this kind, and nano-t2i provides the surrounding training code, so together they form an end-to-end template for learning and research. This resource was released by Jasper Research, the research arm of the AI marketing company Jasper.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/gojasper/nano-t2i">GitHub - gojasper/ nano - t 2 i : Minimal training code of a nano...</a></li>
<li><a href="https://www.jasper.ai/blog/monet">Monet Lowering the Barrier to World Class Image... | The Jasper Blog</a></li>
<li><a href="https://huggingface.co/datasets/jasperai/monet">jasperai/ monet · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#text-to-image`, `#generative models`, `#deep learning`, `#tutorial`, `#dataset`

---

<a id="item-10"></a>
## [Open-Source AI Detectors Fail 0.5% False-Positive Benchmark, Study Finds](https://www.reddit.com/r/MachineLearning/comments/1w58erw/most_opensource_ai_detectors_cant_hold_a_05/) ⭐️ 8.0/10

A new benchmark of six open-source AI detectors finds that most cannot be calibrated to a 0.5% false-positive rate. The best model catches 93.2% of raw AI text but only 41.6% of humanizer-paraphrased text, while the OpenAI RoBERTa detector performs worse than a coin flip on modern generators. The results challenge the assumption that open-source AI detectors are reliable, revealing systematic bias against non-native English writers and near-total failure against paraphrased text. This could reshape development priorities and caution institutions using free detectors for academic integrity, content moderation, or hiring decisions. The evaluation uses only public datasets: Jabarian & Imas 2025, Liang 2023 TOEFL essays, 1,060 frontier-model texts, and 5,000 pre-LLM 2018 FineWeb pages as human text. Thresholds were set on 6,930 human documents; MAGE could not reach the target FPR because it flags 26% of ordinary human web text, and all models flag non-native essays more often than native ones.

reddit · r/MachineLearning · /u/grumpyp2 · Sep 2, 12:04

**Background**: AI text detectors are machine-learning classifiers that try to determine whether text was written by a human or generated by a model such as ChatGPT. A detector typically outputs a score and compares it to a threshold; false-positive rate is the fraction of human-written text incorrectly flagged as AI. In this benchmark, each detector's threshold was calibrated on the same human documents to a matched 0.5% false-positive rate. Older detectors like OpenAI's RoBERTa were trained on GPT-2 outputs, and AI humanizer tools are now widely available to rewrite generated text in ways that evade detection.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/openai-community/roberta-base-openai-detector">openai -community/ roberta -base- openai - detector · Hugging Face</a></li>
<li><a href="https://quillbot.com/ai-content-detector">AI Detector : Free AI Checker for ChatGPT, Claude & GPT-5</a></li>
<li><a href="https://ahrefs.com/writing-tools/ai-humanizer">Free AI Text Humanizer</a></li>

</ul>
</details>

**Tags**: `#AI detection`, `#machine learning`, `#benchmarking`, `#open source`, `#false positives`

---

<a id="item-11"></a>
## [Alibaba releases Qwen3.8-Max-0902, tops CodeArena with 1691 points](https://mp.weixin.qq.com/s/BfKRXMAR5ykD58LDkBftLg) ⭐️ 8.0/10

Alibaba released Qwen3.8-Max-0902, an upgraded large language model further post-trained on coding and professional office tasks. It scored 1691 points on the CodeArena front-end programming leaderboard, a 22-point improvement over the previous version. This release shows Alibaba aggressively competing in AI code generation with both top-tier benchmark performance and aggressive API pricing. The average price of about $5 per million tokens is much lower than the second- and third-ranked models' $20 and $12, which could reshape cost expectations for coding AI services. The model reportedly has 2.4T parameters and a 1M-token context window, with API pricing of $2 per million input tokens and $6 per million output tokens. It is now available on the Qwen AI platform and integrated into Qwen Office, Qoder, and the Qwen App.

telegram · zaihuapd · Sep 2, 06:05

**Background**: CodeArena is an online evaluation platform designed to assess LLM code generation capabilities across a wide range of subtasks and programming languages, aiming to reduce issues like benchmark leakage and data decay. Qwen is Alibaba's family of open and proprietary foundation models; Qoder is the company's agentic AI coding platform. The new model is positioned mainly as a coding-specialized variant with a large context window, ideal for long-file understanding and complex programming tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2503.01295">CodeArena : A Collective Evaluation Platform for LLM Code Generation</a></li>
<li><a href="https://ali-codearena.github.io/Ali-CodeArena/">CodeArenaEval</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Qwen`, `#benchmark`, `#Alibaba`

---

<a id="item-12"></a>
## [Nvidia in Talks to Acquire Hugging Face at Over $13 Billion Valuation](https://t.me/zaihuapd/43557) ⭐️ 8.0/10

According to Business Insider, Nvidia is in negotiations to acquire open-source AI platform Hugging Face at a valuation exceeding $13 billion. No deal has been finalized, and talks could still collapse. A successful acquisition would greatly deepen Nvidia's vertical integration in the AI stack, giving it control over one of the most widely used platforms for open-source models. This could reshape competition among AI infrastructure and model-hosting providers. Nvidia already holds a stake via Hugging Face's 2023 $235 million funding round at a $4.5 billion valuation, and Hugging Face reportedly turned down a $500 million Nvidia investment last year. Microsoft had also expressed interest, but those talks have stopped.

telegram · zaihuapd · Sep 2, 06:50

**Background**: Hugging Face is an AI community and platform often called the 'GitHub of AI,' where developers, researchers, and companies share and deploy open-source models, datasets, and demos. It hosts tools like the Transformers library and is a central hub for open-source machine learning. Nvidia is the dominant maker of AI training chips, so owning the platform would enable it to integrate hardware sales with model distribution and developer workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://mproma.medium.com/what-is-hugging-face-f11abc8b78a4">What Is Hugging Face . How I Went from Curious to Confident | Medium</a></li>
<li><a href="https://www.linkedin.com/posts/kossi-noumagno_hugging-face-the-ai-community-building-activity-7338715927540064256-qJwM">Hugging Face – The AI community building the future.</a></li>
<li><a href="https://kirenz.github.io/deep-learning/docs/hugging-face.html">Hugging Face — Deep Learning</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Hugging Face`, `#Acquisition`, `#AI`, `#M&A`

---

<a id="item-13"></a>
## [Moonshot AI in Early Talks with US Cloud Giants on Kimi K3 Revenue Share](https://www.jiemian.com/article/15040119.html) ⭐️ 8.0/10

Moonshot AI is in early-stage talks with Microsoft, Amazon, and Google about revenue sharing for its open-source Kimi K3 model, reportedly asking for up to a 30% share. If completed, it would be the first large-model revenue-sharing agreement between a Chinese AI company and major US cloud providers. A deal would give Moonshot AI a major new distribution and monetization channel through Western cloud platforms, reinforcing the commercial value of Chinese open-weight frontier models. It could also become a model for cross-border AI licensing between China and the United States amid rising scrutiny of Chinese AI use in America. Kimi K3, released in July 2026, has 2.8 trillion total parameters and is described as the first open-source model at the 3-trillion scale; Moonshot AI's annualized recurring revenue exceeded US$300 million by mid-June. The negotiations are still early, core terms are undecided, and the companies involved have declined to comment.

telegram · zaihuapd · Sep 2, 07:36

**Background**: Moonshot AI (月之暗面) is a Beijing-based company founded in March 2023, and by July 2026 it was valued at US$35 billion, making it one of China's most valuable private AI companies. Its Kimi series of open-weight models has rivaled frontier models from OpenAI and Anthropic. Kimi K3's license already includes a revenue-sharing clause requiring inference providers with more than US$20 million in annual revenue to share up to 30% with Moonshot AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cloud Computing`, `#Business Deal`, `#Open Source`, `#Moonshot AI`

---