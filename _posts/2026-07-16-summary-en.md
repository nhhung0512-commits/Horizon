---
layout: default
title: "Horizon Summary: 2026-07-16 (EN)"
date: 2026-07-16
lang: en
---

> From 51 items, 14 important content pieces were selected

---

1. [Kimi K3: New Open-Weight Frontier Model with 1M Context](#item-1) ⭐️ 9.0/10
2. [Mira Murati's Thinking Machines Lab Releases Inkling Open-Weights Model](#item-2) ⭐️ 9.0/10
3. [xAI Open-Sources Grok Build CLI After Privacy Backlash](#item-3) ⭐️ 9.0/10
4. [New Schema harness achieves 99% on ARC-AGI-3](#item-4) ⭐️ 9.0/10
5. [Decoy font fools AI text recognition with hidden blurred message](#item-5) ⭐️ 8.0/10
6. [Rust-to-Zig Compiler Rewrite: Progress Report](#item-6) ⭐️ 8.0/10
7. [Sony deletes more purchased movies, raising digital ownership concerns](#item-7) ⭐️ 8.0/10
8. [GPT-5.6 Codex bug can delete $HOME directory](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds Endorses AI in Linux, Warns Dissenters to Fork](#item-9) ⭐️ 8.0/10
10. [ExTernD: Expanded-Rank Ternary Decomposition Boosts LLM Quantization Accuracy](#item-10) ⭐️ 8.0/10
11. [250% Speed Boost: 98GB DeepSeek on 4060 Ti Hits 7 t/s](#item-11) ⭐️ 8.0/10
12. [xAI sues user for generating child sexual abuse deepfakes with Grok](#item-12) ⭐️ 8.0/10
13. [Japan to Buy 27,500 Nvidia Rubin Chips for Robot AI](#item-13) ⭐️ 8.0/10
14. [TSMC Invests Additional $100B in Arizona, Q2 Profit Soars 77% to Record](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3: New Open-Weight Frontier Model with 1M Context](https://www.kimi.com/blog/kimi-k3) ⭐️ 9.0/10

Kimi K3 is a new open-weight frontier AI model developed by Moonshot AI, featuring a 1 million token context window, strong performance competitive with leading models, and a proof-of-concept chip design built autonomously using the model itself. As an open-weight model that rivals proprietary frontier models like GPT-4 and Claude, Kimi K3 could democratize access to high-performance AI while its chip design capability suggests a pathway toward AI-driven hardware optimization. Pricing is $3/$15 per million tokens (with cache at $0.3), positioning it comparably to Anthropic's Sonnet series. The chip design proof of concept was completed in a single 48-hour autonomous run using open-source EDA tools on a 45nm library, achieving 100 MHz timing closure at 8,700 tokens/s decode throughput within 4 mm².

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Open-weight models allow researchers and developers to inspect and fine-tune model weights, unlike closed proprietary models. Frontier models are large-scale foundation models that push the boundaries of AI capabilities. A context window determines how much text an LLM can process at once; 1M tokens is exceptionally large, enabling analysis of entire books or long documents.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>
<li><a href="https://www.ibm.com/think/topics/context-window">What is a context window ? | IBM</a></li>
<li><a href="https://medium.com/@bhagyarana80/why-open-weight-models-matter-more-than-you-think-1d1d8787a4fe">Why Open - Weight Models Matter (More Than You Think) | Medium</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some praise the technical achievements and competitive performance, while others note the high pricing relative to Chinese open-weight models and express concern about Moonshot AI's data usage policy, which allows training on API content unless customers opt out.

**Tags**: `#AI`, `#LLM`, `#open-weight`, `#frontier model`, `#chip design`

---

<a id="item-2"></a>
## [Mira Murati's Thinking Machines Lab Releases Inkling Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

Mira Murati's Thinking Machines Lab released Inkling, an open-weights multimodal Mixture-of-Experts transformer with 975 billion total parameters and 41 billion active parameters, licensed under Apache-2.0 and trained on 45 trillion tokens of text, images, audio, and video. This release strengthens the US open-weights ecosystem, providing a competitive alternative to Chinese open models and enabling fine-tuning via Thinking Machines' Tinker platform, with Apache-2.0 licensing ensuring broad accessibility for research and commercial use. Inkling is not a frontier model but is designed as a strong base for customization; documentation is sparse, with the model card and training data documentation lacking detail. Additionally, a smaller variant Inkling-Small (276B total, 12B active) is still being tested and will be released later.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that activates only a subset of parameters per input, enabling large model capacity with efficient computation. Open-weights models, like Inkling released under Apache-2.0, allow users to download and use the trained weights freely, in contrast to open-source models that also require source code distribution under an OSI-approved license.

<details><summary>References</summary>
<ul>
<li><a href="https://researchaudio.io/p/mixture-of-experts-moe-in-large-language-models">Mixture of Experts (MoE) in Large Language Models</a></li>
<li><a href="https://kilo.ai/open-source-vs-open-weight-models">Kilo - Open Source vs Open Weight AI Models Explained</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#large language model`, `#multimodal`, `#Mixture-of-Experts`, `#AI announcement`

---

<a id="item-3"></a>
## [xAI Open-Sources Grok Build CLI After Privacy Backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI open-sourced the entire Grok Build CLI codebase on GitHub under an Apache 2.0 license after severe backlash over the tool uploading entire user directories to Google Cloud by default. This incident exposes critical privacy vulnerabilities in AI-powered coding tools, and xAI's response—open-sourcing and deleting retained data—could pressure other companies to adopt similar transparency measures. The initial repository commit contains 844,530 lines of Rust code with only about 3% vendored, including a Mermaid diagram terminal renderer and the main system prompts for the coding agent.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok Build is an AI-powered CLI tool that helps developers with coding tasks by leveraging xAI's Grok models. The tool can upload files to cloud storage for processing, but a default setting caused entire directories to be uploaded when the command was run, leading to a massive privacy breach.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://support.google.com/cloud/answer/6250993?hl=en">Cloud Storage - Google Cloud Platform Console Help</a></li>

</ul>
</details>

**Discussion**: Users expressed outrage on social media, with one reporting that all personal files including SSH keys and password manager data were uploaded. Elon Musk responded by promising deletion of all uploaded data and open-sourcing the codebase to restore trust.

**Tags**: `#grok`, `#xAI`, `#privacy`, `#open-source`, `#CLI`

---

<a id="item-4"></a>
## [New Schema harness achieves 99% on ARC-AGI-3](https://www.reddit.com/r/MachineLearning/comments/1uyf8oo/new_fable5opus48_harness_called_schema_claims_99/) ⭐️ 9.0/10

A new inference harness called Schema has achieved 99% accuracy on the ARC-AGI-3 Public benchmark by optimizing the inference process of existing models without modifying their weights. This result is significant because ARC-AGI is a benchmark for general intelligence, and achieving near-perfect scores suggests that improved inference processes can unlock latent capabilities in current models, potentially shifting focus from scaling models to better harnessing them. The harness uses a fallback strategy: Claude Opus 4.8 and GPT-5.6 Sol run first, and if a game scores below 80, Fable 5 and GPT-5.6 Sol with higher reasoning are rerun, retaining the higher score per game. It does not change model weights.

reddit · r/MachineLearning · /u/we_are_mammals · Jul 16, 21:02

**Background**: ARC-AGI is a benchmark designed to measure progress towards general intelligence. A harness is a system that orchestrates the inference process, including how inputs are presented and outputs are evaluated, without altering the model's parameters. This approach contrasts with fine-tuning or training new models.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>

</ul>
</details>

**Tags**: `#ARC-AGI`, `#AI benchmark`, `#harness`, `#Claude Opus`, `#Fable 5`

---

<a id="item-5"></a>
## [Decoy font fools AI text recognition with hidden blurred message](https://www.mixfont.com/experiments/decoy-font) ⭐️ 8.0/10

A new font called Decoy Font displays one message to AI text recognition while hiding a different message visible only to humans when the text is blurred or viewed from a distance. This demonstrates a simple yet effective adversarial attack on optical character recognition and large language models, highlighting a vulnerability in automated text understanding. It could lead to practical applications in creating human-readable but machine-resistant text for anti-bot or privacy purposes. The font uses two overlaid layers: sharp outlines in one color form the decoy text, while blurred shading in a different color creates the hidden message. When viewed normally, AI reads the sharp text; when the image is resized or blurred, the hidden message becomes dominant, exploiting differences in human and machine perception.

hackernews · ray__ · Jul 16, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48936584)

**Background**: Adversarial examples are small, often imperceptible perturbations to inputs that cause machine learning models to make errors. This font is a physical adversarial example for text recognition, leveraging human tolerance to blur. Similar techniques have been used in optical illusions that combine high and low spatial frequencies. The Decoy Font concept parallels early experiments with blending high-pass and low-pass filtered images.

<details><summary>References</summary>
<ul>
<li><a href="https://www.turbolens.io/blog/2025-12-20-watermarks-and-background-noise-a-silent-ocr-killer">Watermarks and Background Noise: A Silent OCR ... | TurboLens Blog</a></li>
<li><a href="https://christophm.github.io/interpretable-ml-book/adversarial.html">30 Adversarial Examples – Interpretable Machine Learning</a></li>

</ul>
</details>

**Discussion**: Community members tested the font with GPT, Claude, and Gemini, finding that GPT partially detected the hidden message when prompted, while Claude could not see it. Some noted that resizing the image to 150x150 pixels caused AI to read the blurred text instead. Overall sentiment was that while not practically useful for fooling AI, the font is visually clever and sparks interesting discussion.

**Tags**: `#typography`, `#adversarial AI`, `#OCR`, `#font design`, `#computer vision`

---

<a id="item-6"></a>
## [Rust-to-Zig Compiler Rewrite: Progress Report](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

The article describes the motivations and experience of rewriting the Roc compiler from Rust to Zig, highlighting improvements in safety, performance, and cross-compilation. This rewrite is significant because it provides a real-world comparison between Rust and Zig, two modern system programming languages, and explores trade-offs in safety, performance, and tooling. The insights affect compiler developers and the broader programming language community. The author notes that compilers emitting machine code often require unsafe operations for features like hot binary patching, but Zig's ReleaseSafe mode can catch use-after-free errors at runtime. The rewrite also targets better cross-compilation and incremental builds.

hackernews · jorangreef · Jul 16, 11:39 · [Discussion](https://news.ycombinator.com/item?id=48933149)

**Background**: Zig is a general-purpose system programming language designed as an improvement to C, featuring manual memory management, compile-time generics, and cross-compilation as a first-class feature. Rust emphasizes memory safety through its borrow checker without a garbage collector. The article discusses the trade-offs in choosing Zig over Rust for compiler development, particularly regarding safety and performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**Discussion**: Comments debate whether compilers actually need unsafe code, with Steve Klabnik arguing that only specific features like binary patching require unsafe, not general code emission. Others question Zig's memory safety claims, such as its ability to catch use-after-free errors, and compare Zig's incremental build speed to Rust's. Some express curiosity about why OCaml, used for prototyping, was not chosen for the final implementation.

**Tags**: `#Rust`, `#Zig`, `#compiler design`, `#memory safety`, `#programming languages`

---

<a id="item-7"></a>
## [Sony deletes more purchased movies, raising digital ownership concerns](https://www.techdirt.com/2026/07/15/sony-deletes-a-bunch-more-movies-from-the-accounts-of-people-who-bought-them/) ⭐️ 8.0/10

Sony removed a number of movies from users' accounts that were previously purchased on the PlayStation Store, effectively revoking access to content that consumers believed they owned. This incident underscores the fragility of digital ownership, where purchases are often mere licenses that can be revoked at any time, impacting consumer trust and pushing the debate on true digital ownership rights. The exact number and titles of deleted movies were not disclosed, but this is not the first time Sony has removed content; similar deletions occurred in 2024. Affected users received no compensation or refunds.

hackernews · nekusar · Jul 16, 12:13 · [Discussion](https://news.ycombinator.com/item?id=48933419)

**Background**: Digital rights management (DRM) technologies allow companies to control access to digital content, such as movies and software, even after a consumer pays for it. In many cases, what is labeled as a 'purchase' is actually a revocable license. This model contrasts with physical media ownership, where buyers retain access indefinitely unless the item is physically lost or damaged.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management</a></li>
<li><a href="https://www.fortinet.com/resources/cyberglossary/digital-rights-management-drm">What Is DRM? Digital Rights Management Explained | Fortinet</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with Sony's actions, with some arguing that consumers should receive actual video files instead of licenses. Others proposed that revocations should come with full refunds to balance the economic impact. A few highlighted the ongoing pattern of such deletions and the inadequacy of current digital ownership models.

**Tags**: `#digital rights`, `#ownership`, `#movies`, `#sony`, `#consumer protection`

---

<a id="item-8"></a>
## [GPT-5.6 Codex bug can delete $HOME directory](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

A bug in GPT-5.6 Codex can accidentally delete the user's $HOME directory when overriding environment variables without proper sandboxing or review. This bug underscores critical safety risks in AI coding agents with full system access, highlighting the need for sandboxing and human review to prevent destructive actions. The issue occurs when full access mode is enabled, sandboxing and auto-review are disabled, and the model attempts to override $HOME to define a temporary directory but mistakenly deletes $HOME instead.

rss · Simon Willison · Jul 16, 17:45

**Background**: OpenAI Codex is an AI coding agent that can autonomously read, write, and execute code, often with access to the user's file system. Sandboxing isolates the agent's operations to prevent damage to the host system. Without sandboxing and review, the agent's mistakes can have severe consequences.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://amux.io/guides/ai-agent-sandboxing/">AI Agent Sandboxing in 2026: Docker, E2B, Firecracker... — amux</a></li>

</ul>
</details>

**Tags**: `#codex`, `#generative-ai`, `#ai-safety`, `#coding-agents`, `#bug`

---

<a id="item-9"></a>
## [Linus Torvalds Endorses AI in Linux, Warns Dissenters to Fork](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the creator and lead maintainer of the Linux kernel, explicitly stated that Linux is not an anti-AI project and that AI is a clearly useful tool, warning that those who disagree can fork the project or leave. This definitive statement from the top maintainer settles potential community controversy over AI in kernel development, providing clear guidance and likely accelerating adoption of AI-assisted tools within the Linux ecosystem. Torvalds emphasized that AI is a tool like any other and its usefulness is no longer in question, while acknowledging open questions about the AI economy. He was responding to a discussion on the Linux media mailing list.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linus Torvalds is the creator and long-time maintainer of the Linux kernel, the core of the Linux operating system. Debates have emerged in open-source communities about the ethics and utility of using AI tools (like code generation from LLMs) in development, with some projects adopting explicit bans or restrictions.

**Tags**: `#Linux`, `#AI`, `#Linus Torvalds`, `#kernel development`, `#open source`

---

<a id="item-10"></a>
## [ExTernD: Expanded-Rank Ternary Decomposition Boosts LLM Quantization Accuracy](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

ExTernD proposes an expanded-rank ternary decomposition for post-training quantization of large language models, decomposing a weight matrix into two ternary matrices and a diagonal scaling matrix to allow arbitrary inner rank and achieve accuracy approaching any quantization level. This approach addresses the fixed-matrix-size limitation of prior ternary PTQ methods, enabling high accuracy with minimal VRAM overhead, which is crucial for efficient deployment of large language models on resource-constrained hardware. The decomposition effectively increases the rank of the ternary representation, and the authors demonstrate that only a slight VRAM increase over standard quantization methods is needed while leveraging ternary arithmetic for efficiency.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Post-training quantization (PTQ) compresses neural networks by reducing weight precision without retraining. Ternary quantization maps weights to {-1, 0, +1}, offering high compression but often limited accuracy due to fixed matrix size constraints. ExTernD overcomes this by expanding the representation rank via matrix decomposition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/ternary-weight-ptq-framework">Ternary -Weight PTQ Framework</a></li>
<li><a href="https://www.researchgate.net/publication/395573778_Network_Splitting_Techniques_and_Their_Optimization_for_Lightweight_Ternary_Neural_Networks">(PDF) Network Splitting Techniques and Their Optimization for...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#ternary decomposition`, `#PTQ`, `#efficient inference`

---

<a id="item-11"></a>
## [250% Speed Boost: 98GB DeepSeek on 4060 Ti Hits 7 t/s](https://www.reddit.com/r/LocalLLaMA/comments/1uy33fw/deepseek_v4_flash_98gb_on_1x_4060ti_cpu_got_300/) ⭐️ 8.0/10

A user reported that recent llama.cpp commits (between b9986 and b10034) improved inference speed from 2 to 7 tokens per second for the 98GB DeepSeek-V4-Flash-UD-Q2_K_XL model on a system with an RTX 4060 Ti (16GB VRAM) and a 6-core CPU. This represents a 250% speedup. This demonstrates that large Mixture-of-Experts models like DeepSeek V4 Flash (284B total, 13B active) can become usable on budget consumer hardware through aggressive quantization and CPU-GPU hybrid inference. It lowers the barrier for running state-of-the-art local LLMs without expensive GPUs. The model uses the UD-Q2_K_XL quantization (an ultra-low bit variant of Q2_K), squeezing 98GB of parameters into memory via CPU RAM. The system has 138GB of system RAM and offloads to CPU for layers exceeding 16GB VRAM. The user employed split-mode=layer and flash attention to achieve the speedup.

reddit · r/LocalLLaMA · /u/Chuyito · Jul 16, 13:35

**Background**: llama.cpp is an open-source library for efficient LLM inference on consumer hardware, supporting CPU, GPU, and hybrid inference via layer offloading. Quantization reduces model precision to fit into limited memory, with K-quants like Q2_K being the smallest viable formats. DeepSeek V4 Flash is a Mixture-of-Experts model with 284B total parameters but only 13B activated per token, which helps reduce compute cost.

<details><summary>References</summary>
<ul>
<li><a href="https://craftrigs.com/guides/llama-cpp-cpu-gpu-hybrid-inference-limited-vram/">llama . cpp CPU + GPU Hybrid Inference : Run 70B on Any... | CraftRigs</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#local-llm`, `#inference-optimization`, `#llama.cpp`, `#hardware-efficiency`, `#deepseek`

---

<a id="item-12"></a>
## [xAI sues user for generating child sexual abuse deepfakes with Grok](https://www.reuters.com/legal/litigation/musks-xai-sues-grok-user-over-sexualized-deepfakes-2026-07-15/) ⭐️ 8.0/10

xAI has filed a lawsuit against Terry Harwood, a South Carolina man, for using its Grok AI chatbot to generate child sexual abuse material and non-consensual adult deepfake pornography, violating the terms of service. This is one of the first cases where an AI company has sued a user for generating CSAM, potentially setting a legal precedent for AI safety and content moderation across the industry. xAI is seeking damages and a permanent injunction barring Harwood from using Grok; the company reports it has suspended 52,222 accounts and referred 73,604 incidents to the National Center for Missing & Exploited Children, leading to at least 244 arrests this year.

telegram · zaihuapd · Jul 16, 01:45

**Background**: Deepfakes are synthetic media generated using machine learning, often via Generative Adversarial Networks (GANs), which pit two neural networks against each other to create realistic fake images or videos. This technology can be misused to produce non-consensual explicit content, including child sexual abuse material, raising serious legal and ethical concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://spectrum.ieee.org/what-is-deepfake">What Are Deepfakes and How Are They Created? - IEEE Spectrum</a></li>
<li><a href="https://in.norton.com/blog/emerging-threats/what-are-deepfakes">Deepfakes : What they are and why they’re threatening | NortonLifeLock</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#legal`, `#Grok`, `#content moderation`, `#deepfakes`

---

<a id="item-13"></a>
## [Japan to Buy 27,500 Nvidia Rubin Chips for Robot AI](https://www.bloomberg.com/news/articles/2026-07-16/japan-to-buy-nvidia-rubin-chips-to-build-sovereign-ai-for-robots) ⭐️ 8.0/10

Japan announced plans to purchase 27,500 next-generation Nvidia Rubin chips, led by new company Noetra, to build a large data center and develop a sovereign AI foundation model for robotics, backed by 387.3 billion yen ($24 billion) in government funding. This move marks a strategic shift for Japan to reduce reliance on foreign AI technology and strengthen its robotics industry, aiming to capture over 30% of the global robot market by 2040, potentially reshaping the competitive landscape against the US and China. Noetra, led by Hironobu Tabata, aims to release its first AI model by March 2027 and a robot-specific version within a few years, with participants including SoftBank, Toyota-backed Preferred Networks, and NEC.

telegram · zaihuapd · Jul 16, 10:59

**Background**: Nvidia's Rubin architecture is its next-generation GPU platform designed for large-scale AI factories, combining GPUs, CPUs, networking, and storage. Sovereign AI refers to nations developing their own AI capabilities for strategic autonomy, a concept gaining traction amid US-China tech rivalry.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thundercompute.com/blog/nvidia-rubin-architecture">Nvidia Rubin Architecture : Everything You Must... | Thunder Compute</a></li>
<li><a href="https://www.linkedin.com/posts/itmatterss_nvidia-unveils-rubin-architecture-at-ces-activity-7414182623264059393-ZHRl">Nvidia Unveils Rubin Architecture for AI Workloads | LinkedIn</a></li>
<li><a href="https://www.aol.com/finance/nvidia-rubin-architecture-game-changer-172211628.html">Nvidia ’s Rubin Architecture Is a Game-Changer. Here’s Why. - AOL</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI chips`, `#robotics`, `#Japan`, `#sovereign AI`

---

<a id="item-14"></a>
## [TSMC Invests Additional $100B in Arizona, Q2 Profit Soars 77% to Record](https://www.reuters.com/world/asia-pacific/tsmcs-second-quarter-profit-seen-hitting-record-ai-boom-2026-07-15/) ⭐️ 8.0/10

TSMC announced an additional $100 billion investment in its Arizona facilities, bringing total planned investment to $265 billion, while reporting a 77% year-over-year surge in Q2 net profit to a record 706.6 billion New Taiwan dollars ($22 billion), exceeding market expectations. This massive investment underscores TSMC's strategic pivot to diversify manufacturing away from Taiwan amid geopolitical tensions, while its record profit highlights the insatiable demand for AI chips, solidifying TSMC's central role in the global semiconductor supply chain. TSMC also raised its 2026 capital expenditure forecast to between $60 billion and $64 billion and expects full-year dollar revenue to grow slightly over 40%; the Arizona site currently has eight factories under construction or planned, with potential for four more.

telegram · zaihuapd · Jul 16, 12:29

**Background**: TSMC is the world's largest dedicated semiconductor foundry, producing chips for companies like Apple, NVIDIA, and AMD. AI demand has driven explosive growth for advanced chips, particularly those built on leading-edge process nodes. The U.S. government has encouraged chip manufacturing reshoring through the CHIPS Act, making TSMC's Arizona expansion a key element of supply chain security.

**Tags**: `#semiconductor`, `#TSMC`, `#AI`, `#investment`, `#supply chain`

---