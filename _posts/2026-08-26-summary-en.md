---
layout: default
title: "Horizon Summary: 2026-08-26 (EN)"
date: 2026-08-26
lang: en
---

> From 34 items, 11 important content pieces were selected

---

1. [Qwen3.8-Flash-Next: N-gram Embedding MoE with 6B Active Parameters](#item-1) ⭐️ 9.0/10
2. [DeepSeek-V4-Pro Launches with Agent Upgrades and Peak-Valley API Pricing](#item-2) ⭐️ 9.0/10
3. [vLLM v0.28.0 Released with Kimi-K3 and DeepSeek V4 Optimizations](#item-3) ⭐️ 8.0/10
4. [Tailcat: A Netcat-like Tool Over Tailscale's Data Plane](#item-4) ⭐️ 8.0/10
5. [GLM-5.3-Flash: near-flagship AI performance at a fifth of the cost](#item-5) ⭐️ 8.0/10
6. [AWS Acquires DuckLabs; DuckDB Open Source Remains with Foundation](#item-6) ⭐️ 8.0/10
7. [575k Recovered Crop Labels Show Human Clicks Beat Bigger Models in Book Digitization](#item-7) ⭐️ 8.0/10
8. [ImageBench: Open text-to-image benchmark with 52 models and 9k images](#item-8) ⭐️ 8.0/10
9. [X Sends Cease-and-Desist to Nitter, Shuts Down Main Instance](#item-9) ⭐️ 8.0/10
10. [Zhipu Confirms Ox Alpha Is New GLM Iteration, Topping DeepSeek in Usage](#item-10) ⭐️ 8.0/10
11. [Tencent Open-Sources WeMM-Embedding Multimodal Models with SOTA Results](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Qwen3.8-Flash-Next: N-gram Embedding MoE with 6B Active Parameters](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 9.0/10

Alibaba Qwen released Qwen3.8-Flash-Next, a large language model built on the new Qwen4 architecture. It features a 125B-parameter Mixture-of-Experts model with an additional 51B N-gram embeddings, activating only 6B parameters per token. This release introduces a novel N-gram embedding architecture that trades memory for compute, training at 1/9 the cost of Qwen3.7-Plus while outperforming it across the board. It could pave the way for more efficient LLM designs and make state-of-the-art models more accessible to run locally. The model's effective size is roughly 176B parameters, raising questions about quantization: a 4-bit quant may exceed 100GB, potentially not fitting in 128GB unified memory. According to BenchLM, it ranks #25 of 226 at 67.54/100 overall, with strong SWE Multilingual performance.

hackernews · tosh · Aug 26, 12:52 · [Discussion](https://news.ycombinator.com/item?id=49448210)

**Background**: N-gram embeddings are a technique that represents words by sequences of tokens (n-grams), allowing the model to capture more context without increasing active parameters. In Mixture-of-Experts (MoE) models, only a subset of parameters is activated per token, enabling much larger total model sizes while keeping inference efficient. Qwen3.8-Flash-Next is the first open model based on the Qwen4 architecture, designed to run on a 128GB workstation or Mac at 4-bit quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://atomic.chat/blog/guides/how-to-run-qwen-3-8-flash-next-locally">How to Run Qwen 3 . 8 Flash Next Locally: GGUF... - Atomic Chat</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen/ Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://benchlm.ai/models/qwen3-8-flash-next">Qwen 3 . 8 - Flash - Next Benchmarks & Context (August 2026)</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed but engaged. Simon Willison tested it at different reasoning levels and was surprised it didn't match his preferred Qwen 3.8 27B results, while rohansood15 noted it beats 3.8 27B cleanly. Several commenters (andy99, schopra909) discussed the N-gram architecture's effective size, quantization feasibility, and intuition behind the approach, referencing DeepSeek's earlier paper. tosh highlighted the new architecture as a foreshadowing of Qwen4 and its 1/9 training cost advantage.

**Tags**: `#AI`, `#Qwen`, `#Large Language Models`, `#Architecture`, `#Machine Learning`

---

<a id="item-2"></a>
## [DeepSeek-V4-Pro Launches with Agent Upgrades and Peak-Valley API Pricing](https://t.me/zaihuapd/43417) ⭐️ 9.0/10

DeepSeek-V4-Pro, the official version, has launched simultaneously on the app, web, and API, with the model name set to deepseek-v4-pro. The release enhances agent capabilities, natively supports the Responses API format, and adds low, high, and max thinking modes for V4-Pro and V4-Flash. This is a major version release of a widely used AI model, boosting its agentic capabilities and interoperability with tools like Codex. The new peak-valley API pricing, with off-peak rates at half the peak price, could significantly affect developer costs and usage patterns in the AI/ML community. The API call method remains unchanged, with the model name set to deepseek-v4-pro. New peak-valley pricing starts on August 17, 2026, cutting off-peak rates to half of peak-hour prices; the V4-Pro and V4-Flash thinking modes now offer low, high, and max levels.

telegram · zaihuapd · Aug 26, 08:02

**Background**: DeepSeek is a Chinese AI company known for releasing large language models, and its API lets developers integrate AI capabilities into applications. The Responses API is a newer interface that brings together chat completions and assistant functionality into a unified, stateful multi-turn experience. Peak-valley pricing is a common utility model where off-peak usage costs less, encouraging load shifting. Agent capabilities refer to a model's ability to reason, plan, and act autonomously, often with tool use.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses">Use the Azure OpenAI Responses API - Microsoft Foundry | Microsoft Learn</a></li>
<li><a href="https://aws.amazon.com/what-is/api/">What is an API ? - Application Programming Interfaces Explained -...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI`, `#LLM`, `#API`, `#Release`

---

<a id="item-3"></a>
## [vLLM v0.28.0 Released with Kimi-K3 and DeepSeek V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) ⭐️ 8.0/10

vLLM v0.28.0 was released with 584 commits from 270 contributors, featuring major performance optimizations for Kimi-K3 (including Decode Context Parallel and fused FlashKDA kernels) and end-to-end sparse MLA support for DeepSeek V4, along with ROCm enablement and tiered KV cache offloading. New defaults include raising max_num_batched_tokens to 16384 and enabling prefix caching by default for Mamba models. vLLM is one of the most widely used LLM inference engines, so these optimizations directly enable faster and more memory-efficient serving of frontier models like Kimi-K3 and DeepSeek V4. Practitioners can expect lower latency, higher throughput, and reduced GPU memory costs, especially for speculative decoding and MoE workloads. Notable improvements include an adaptive speculative token budget delivering ~60% better DSpark TTFT, combined all-gathers with 1.5–3x kernel-level speedup, and optional shared-expert sharding saving ~17 GiB of memory per GPU. Breaking changes include bitsandbytes moving to an out-of-tree plugin and Transformers being bumped to 5.15.0.

github · khluu · Aug 26, 09:46

**Background**: vLLM is an open-source high-throughput LLM inference engine that optimizes memory management with PagedAttention and supports continuous batching. Kimi-K3 and DeepSeek V4 are large language models that use Mixture-of-Experts (MoE) architectures, where tokens are routed to specialized expert modules; MegaMoE is a high-performance architecture for such models. DeepSeek V4 also uses sparse multi-head latent attention (MLA) and DSpark, an open-source speculative decoding framework that accelerates inference by having a draft model propose tokens that the target model verifies in parallel.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark : Confidence-Scheduled Speculative Decoding...</a></li>
<li><a href="https://codersera.com/blog/deepseek-dspark-explained-2026/">DeepSeek DSpark : 51–400% Faster V4 Inference (2026)</a></li>
<li><a href="https://deepwiki.com/deepseek-ai/DeepGEMM/3.3-mega-moe-architecture">Mega MoE Architecture | deepseek-ai/DeepGEMM | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#LLM inference`, `#performance optimization`, `#DeepSeek`, `#release`

---

<a id="item-4"></a>
## [Tailcat: A Netcat-like Tool Over Tailscale's Data Plane](https://github.com/tailscale/tailcat) ⭐️ 8.0/10

Tailscale has released tailcat, a netcat-like command-line utility that uses Tailscale's data plane (magicsock) to establish peer-to-peer TCP/UDP connections between machines. It provides secure, WireGuard-encrypted tunnels without relying on Tailscale's control plane for traffic forwarding. Tailcat simplifies building peer-to-peer networking tools and services, lowering the barrier for developers to leverage Tailscale's NAT-traversal and secure tunneling infrastructure. It opens up practical use cases such as remote access, custom protocols, and even Minecraft mods, and reflects a broader trend toward trivialized p2p connectivity. Tailcat uses Tailscale's magicsock data plane to create point-to-point WireGuard-encrypted tunnels, with DERP acting as a NAT-hole-punching side channel and relay-of-last-resort if NAT traversal fails. It works without Tailscale's control plane, and the project includes a Nix development/install environment.

hackernews · nderjung · Aug 26, 17:42 · [Discussion](https://news.ycombinator.com/item?id=49452990)

**Background**: Tailscale is a software-defined mesh VPN that connects devices into a 'tailnet'. Its control plane handles coordination and policy, while the data plane runs on each device and carries encrypted traffic directly between machines in a mesh. Netcat is a classic Unix networking utility for reading/writing data over TCP/UDP, often used for testing and scripting; tailcat brings a similar interface to modern p2p networking.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tailscale/tailcat">GitHub - tailscale/tailcat: like netcat, but over Tailscale's data plane, without Tailscale's control plane · GitHub</a></li>
<li><a href="https://tailscale.com/docs/concepts/control-data-planes">Control and data planes · Tailscale Docs</a></li>
<li><a href="https://tailscale.com/blog/how-tailscale-works">Tailscale: How it works</a></li>

</ul>
</details>

**Discussion**: Community reaction to tailcat was positive and enthusiastic. Brad Fitzpatrick highlighted a Minecraft mod built on tailcat, users compared it to Iroh, and one developer said it inspired them to rethink their own SSH-to-home solution. Others noted that widespread IPv6 (without CGNAT) would make such tools less necessary, and one user asked about Tailscale's use of Nix as a dev environment.

**Tags**: `#networking`, `#tailscale`, `#p2p`, `#developer-tools`, `#golang`

---

<a id="item-5"></a>
## [GLM-5.3-Flash: near-flagship AI performance at a fifth of the cost](https://z.ai/blog/glm-5.3-flash) ⭐️ 8.0/10

Z.ai has released GLM-5.3-Flash, a cost-efficient multimodal model that delivers near-GLM5.3 performance at a fraction of the cost, with weights available on Hugging Face. The model uses a 320B parameter MoE architecture with 18B active parameters. This release signals a broader industry trend toward drastically cheaper inference for near-frontier models, potentially making advanced AI accessible to smaller developers and enabling local or semi-local deployment. It also intensifies competitive pressure among AI labs, especially as Chinese labs like Z.ai push open-weight models at disruptive price points. GLM-5.3-Flash is the first native multimodal model in the GLM-5 series, scoring 57 on the Artificial Analysis Intelligence Index with output speed of 48.7 tokens per second on Z.ai's API. It reportedly cuts parameter count roughly in half and reduces serving cost to about a fifth of GLM5.3, and can run on Chinese-made chips.

hackernews · Philpax · Aug 26, 14:08 · [Discussion](https://news.ycombinator.com/item?id=49449507)

**Background**: GLM is a series of open-weight large language models developed by Z.ai, a Chinese AI company known for ChatGLM. MoE (Mixture-of-Experts) architectures like this one activate only a subset of parameters per token, reducing compute and cost while retaining high capacity. Open-weight releases from Chinese labs have become increasingly competitive on performance-per-dollar, driving rapid iteration in the AI ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/vlm/glm-5.3-flash">GLM-5.3-Flash - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://artificialanalysis.ai/models/glm-5-3-flash">GLM-5.3-Flash - Intelligence, Performance & Price Analysis | Artificial Analysis</a></li>
<li><a href="https://unsloth.ai/docs/models/glm-5.3">GLM-5.3-Flash | Unsloth Documentation</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were broadly impressed by the rapid pace of improvement and the price-performance ratio, with one noting it is 'smarter and cheaper' than several competitors. Others discussed the financial viability of local hardware for heavy users, while some warned about Z.ai's terms of service and cautioned against over-reliance on vendor benchmarks.

**Tags**: `#AI`, `#machine learning`, `#LLM`, `#model release`, `#benchmarks`

---

<a id="item-6"></a>
## [AWS Acquires DuckLabs; DuckDB Open Source Remains with Foundation](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐️ 8.0/10

AWS has acquired DuckLabs, the commercial company behind DuckDB. The open-source DuckDB project remains owned by the nonprofit DuckDB Foundation. This acquisition marks a major event in the database world, as DuckDB has become a widely used embedded analytical SQL engine. Since the foundation retains the open-source IP, the core project's governance may stay independent, but AWS's influence on the commercial ecosystem could be significant. DuckLabs was spun out of CWI, and the DuckDB Foundation was created at that time to hold all IP of the open-source project. The acquisition does not transfer ownership of the DuckDB source code, but the future of DuckLabs' commercial services and features remains to be seen.

hackernews · onderkalaci · Aug 26, 12:59 · [Discussion](https://news.ycombinator.com/item?id=49448321)

**Background**: DuckDB is an open-source, in-process, column-oriented analytical SQL database designed for fast queries on large datasets without requiring a separate server. It has gained popularity for embedded analytics in Python, R, and other environments, competing with tools like Apache DataFusion and large cloud data warehouses. The DuckDB Foundation was established when DuckLabs spun out of CWI to protect the project's open-source nature.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DuckDB">DuckDB - Wikipedia</a></li>
<li><a href="https://duckdb.org/">DuckDB – An in- process SQL OLAP database management system</a></li>

</ul>
</details>

**Discussion**: Commenters are split between congratulations and concern. Some worry AWS has a poor track record with open-source projects and may not nurture DuckDB, while others note the foundation's IP ownership limits AWS's control. One commenter recommends Apache DataFusion as an alternative, and another mentions AWS internal turmoil and talent departures.

**Tags**: `#AWS`, `#DuckDB`, `#acquisition`, `#database`, `#open-source`

---

<a id="item-7"></a>
## [575k Recovered Crop Labels Show Human Clicks Beat Bigger Models in Book Digitization](https://www.reddit.com/r/MachineLearning/comments/1vz2ojw/we_recovered_575k_crop_labels_from_a_decade_of/) ⭐️ 8.0/10

The author recovered 575,729 crop labels from a decade of manual Photoshop work on 1,765 Urdu books and used them to train a model for book digitization. Scaling training data, switching to ResNet-50, and using higher resolutions all failed, while just ten operator-corrected crops per book raised pass@80 from 0.71 to 0.83. This is a valuable negative result for the machine learning community: it shows that when the dominant error is a per-volume human bias not present in the pixels, adding data or model capacity cannot fix it. The human-in-the-loop calibration approach offers a practical template for archival digitization and document processing where perfection matters. The recovered geometry was obtained with SIFT + MAGSAC under conservative acceptance gates; per-book error analysis revealed the failures were near-constant offsets reflecting the operator's margin inset. For retouching, the author used a U-Net only for detection, classical OpenCV for reconstruction, and a REMOVE/KEEP/IGNORE label scheme with a diacritic-veto rule, which improved mark IoU from 0.56 to 0.60 while eliminating diacritic false positives.

reddit · r/MachineLearning · /u/laamaleph · Aug 26, 16:53

**Background**: Book digitization often involves photographing pages and manually cropping them to the content area; for rare Urdu lithographs and dictionaries, this is an extremely labor-intensive process. The Ibteda Digital Library in Pakistan spent ten years hand-finishing pages in Photoshop, unknowingly recording implicit crop decisions. The author registered those finished pages back to raw photos to create supervision, and used pass@k as the metric and MAGSAC for robust geometric estimation. The negative results show that a hidden human preference — the operator's preferred margin inset — is fundamentally absent from the pixels of a new book.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1912.05909">MAGSAC ++, a fast, reliable and accurate robust estimator</a></li>
<li><a href="https://openaccess.thecvf.com/content_CVPR_2020/papers/Barath_MAGSAC_a_Fast_Reliable_and_Accurate_Robust_Estimator_CVPR_2020_paper.pdf">MAGSAC ++, a Fast, Reliable and Accurate Robust Estimator</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Computer Vision`, `#Book Digitization`, `#Negative Results`, `#Dataset`

---

<a id="item-8"></a>
## [ImageBench: Open text-to-image benchmark with 52 models and 9k images](https://www.reddit.com/r/MachineLearning/comments/1vz9x9c/a_dataset_with_52_text_to_image_model_evaluation_p/) ⭐️ 8.0/10

The author released ImageBench V1, a text-to-image benchmark with 192 curated difficult prompts and results for 52 models. The dataset includes more than 9,000 generated and analyzed images, along with the full methodology, prompts, and scoring code on Hugging Face and GitHub. This benchmark addresses a key gap in text-to-image evaluation by publishing the actual generated images instead of only aggregate scores. It provides a reusable, transparent resource for comparing model performance on hard cases such as text rendering, spatial reasoning, and negations. The benchmark uses a fixed set of 192 prompts designed to stress-test text-to-image models across categories like text rendering, spatial reasoning, human realism, and negations. A vision-language model (VLM) judges each output against a binary question with ground truth, though the author notes that VLM judges are not perfect.

reddit · r/MachineLearning · /u/dh7net · Aug 26, 21:10

**Background**: Text-to-image benchmarks typically rank models using aggregate metrics or human preference scores, but many public leaderboards do not release the actual images generated during evaluation. Releasing images lets researchers inspect failure modes and verify scorer behavior. VLMs are increasingly used as automated judges to scale evaluations, but their judgments can be noisy or biased. This benchmark aims to combine reproducibility with transparent output sharing.

<details><summary>References</summary>
<ul>
<li><a href="https://imagebench.ai/">ImageBench — AI image model benchmark</a></li>
<li><a href="https://imagebench.ai/methodology-v1">Benchmark V1 Methodology</a></li>
<li><a href="https://huggingface.co/spaces/ArtificialAnalysis/Text-to-Image-Leaderboard">Image Arena Leaderboard - a Hugging Face Space by ArtificialAnalysis</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#text-to-image`, `#evaluation`, `#dataset`, `#machine-learning`

---

<a id="item-9"></a>
## [X Sends Cease-and-Desist to Nitter, Shuts Down Main Instance](https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/) ⭐️ 8.0/10

On August 24, 2026, X Corp. sent cease-and-desist letters to the open-source Nitter project and its instances, alleging illegal scraping and API misuse. The main Nitter instance has shut down and author Zedeus has paused development while seeking legal advice. This legal action targets a widely-used privacy tool, potentially setting a precedent for enforcement against client-side scraping and open-source frontends. It affects many users who relied on Nitter for ad-free, account-free browsing of X, and raises concerns about the future of similar open-source projects. X demanded permanent shutdown of all Nitter instances and removal of the code repository by 5 PM on August 25. Nitter previously used internal Twitter APIs to serve a lightweight front-end without JavaScript or ads, and had been blocked by X in 2024 over API restrictions.

telegram · zaihuapd · Aug 26, 06:30

**Background**: Nitter is a free and open-source alternative frontend for Twitter (now X) that prioritizes privacy and performance. It acts as a proxy, requesting data server-side and serving pages without tracking, ads, or account login. Cease-and-desist letters are formal demands to stop allegedly illegal activity, often preceding litigation. Web scraping and unauthorized API use are common legal grey areas, especially after platform policy changes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://github.com/zedeus/nitter">GitHub - zedeus/nitter: Alternative Twitter front-end · GitHub</a></li>
<li><a href="https://nlnet.nl/project/Nitter/">NLnet; Nitter</a></li>

</ul>
</details>

**Tags**: `#open source`, `#legal`, `#web scraping`, `#privacy`, `#twitter`

---

<a id="item-10"></a>
## [Zhipu Confirms Ox Alpha Is New GLM Iteration, Topping DeepSeek in Usage](https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek?srnd=phx-technology) ⭐️ 8.0/10

Chinese AI company Zhipu (Z.ai) confirmed that Ox Alpha, a model that went viral after a stealth launch, is the latest iteration of its GLM series. The model has topped OpenRouter's usage rankings with usage more than double that of DeepSeek. This marks a strong competitive move from a major Chinese AI lab against fellow Chinese lab DeepSeek, whose models have been widely adopted globally. It also signals that Zhipu is pushing forward aggressively with new GLM releases on open model routing platforms. Ox Alpha is currently in a free preview expected to last about one week, with no exact pricing announced yet. It is the latest iteration in the GLM line, a series of open-weight large language models developed by Zhipu.

telegram · zaihuapd · Aug 26, 09:33

**Background**: GLM, short for General Language Model, is a series of open-weight large language models developed by Chinese software company Z.ai (Zhipu). The first GLM model was published in 2021 and later released as the ChatGLM chatbot in March 2023. OpenRouter is a platform that provides a unified API to access 400+ models from providers including OpenAI, Anthropic, and these Chinese models. DeepSeek is another prominent Chinese AI lab whose models compete directly with Zhipu's offerings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://z.ai/blog/glm-4.5">GLM-4.5: Reasoning, Coding, and Agentic Abililties</a></li>

</ul>
</details>

**Tags**: `#AI`, `#GLM`, `#Zhipu`, `#DeepSeek`, `#LLM`

---

<a id="item-11"></a>
## [Tencent Open-Sources WeMM-Embedding Multimodal Models with SOTA Results](https://github.com/Tencent/WeMM-Embedding) ⭐️ 8.0/10

Tencent's WeChat Vision team open-sourced the WeMM-Embedding family of multimodal embedding models in three sizes (2B, 4B, and 9B), unified for text, images, videos, visual documents, and mixed multimodal inputs. The models, released under the Apache 2.0 license, achieve state-of-the-art results on several benchmarks, though audio input is not supported. This release gives developers and researchers a permissively licensed, open-source multimodal embedding model family that can power retrieval-augmented generation, multimodal search, and document understanding across text, image, video, and PDF-like documents. It strengthens the open ecosystem around multimodal models and offers competitive alternatives to proprietary embedding APIs. The models are built on natively multimodal Qwen3.5 backbones and unified for representation and retrieval of text, image, video, visual documents, and mixed inputs. The 2B, 4B, and 9B sizes offer scalability across different deployment scenarios, and the project is available under Apache 2.0.

telegram · zaihuapd · Aug 26, 13:15

**Background**: Multimodal learning is a deep learning approach that integrates and processes multiple data types, such as text, images, audio, and video. Embedding models convert data into dense vector representations, enabling similarity search and retrieval. Visual document retrieval is a specific task that searches for relevant image-based documents, such as PDFs, and is important for multimodal retrieval-augmented generation (RAG) systems. WeMM-Embedding unifies these modalities into a single embedding space.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent/WeMM-Embedding">GitHub - Tencent/ WeMM - Embedding : WeMM - Embedding is a family...</a></li>
<li><a href="https://arxiv.org/html/2608.24053v1">WeMM - Embedding : WeChat Multi-Modal Embedding Technical Report</a></li>
<li><a href="https://huggingface.co/tasks/visual-document-retrieval">What is Visual Document Retrieval? - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#multimodal-embedding`, `#open-source`, `#tencent`, `#retrieval`, `#AI`

---