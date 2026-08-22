---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 26 items, 5 important content pieces were selected

---

1. [SGLang v0.5.18 releases with 710 PRs and new model support](#item-1) ⭐️ 8.0/10
2. [Munder Difflin: Local Harness Runs Deterministic 'Office of Clones' Simulations](#item-2) ⭐️ 8.0/10
3. [Developer builds sub-2-bit quantized LLM, 60 MB model runs at 400 tok/s on CPU](#item-3) ⭐️ 8.0/10
4. [Tesla Announces Supervised FSD Now Available in China](#item-4) ⭐️ 8.0/10
5. [Amazon Exposed for Buying and Destroying Scanned Books for AI Training](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.18 releases with 710 PRs and new model support](https://github.com/sgl-project/sglang/releases/tag/v0.5.18) ⭐️ 8.0/10

SGLang v0.5.18 has been released, incorporating 710 pull requests from 212 contributors. The release adds support for new models including Muse Glimmer, Intern-S2-Mobius, SANA-Video, LTX-2.5, and several diffusion models, alongside performance optimizations such as overlapped checkpoint staging and TP LMHead with All-to-All. SGLang is a widely adopted LLM inference engine, and this release broadens its scope to cover diffusion and multimodal models, not just autoregressive language models. The measurable performance gains, such as 2.38x faster startup for Qwen3-32B on H100, directly benefit production deployments and the broader open-source inference ecosystem. The release upgrades core dependencies to torch 2.13.0, triton 3.7.1, flashinfer 0.6.17, and sgl-kernel 0.4.6.post1. A notable breaking change consolidates all compiled-kernel caches under a single SGLANG_CACHE_DIR, requiring a one-time recompilation after upgrading.

github · Fridge003 · Aug 22, 00:09

**Background**: SGLang is an open-source inference framework initially designed for efficient serving of large language models, and it is now expanding to diffusion models as well. The release's cookbook recipes provide deployment guidance for newly supported models, making it easier for users to run a wide range of generative models on their own hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model">Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device | Meta AI Research</a></li>
<li><a href="https://huggingface.co/Efficient-Large-Model/SANA-Video_2B_480p">Efficient-Large-Model/SANA-Video_2B_480p · Hugging Face</a></li>
<li><a href="https://ltx.io/model/ltx-2-5">LTX - 2 . 5 : LTX's Latest AI Open-Source Foundation Model | LTX</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#SGLang`, `#release`, `#model support`, `#open source`

---

<a id="item-2"></a>
## [Munder Difflin: Local Harness Runs Deterministic 'Office of Clones' Simulations](https://munderdiffl.in/) ⭐️ 8.0/10

Munder Difflin is a local multi-agent harness that wraps existing coding agents such as Claude Code and Codex to run deterministic 'office of clones' simulations. Its builder Chaitanya reports over 20,000 users in the first week and says most users see reduced token consumption. It tackles two urgent pain points in AI-assisted development: multi-agent orchestration and token costs. By letting developers prototype an 'office' of agent clones locally, it makes multi-agent workflows more practical and testable. The tool wraps 'almost all' coding agent harnesses and claims deterministic, non-token-consuming simulations on top of users' existing Claude Code and Codex subscriptions. Early user feedback has questioned the design, with one reviewer arguing it is really pipelines and roles rather than true agents.

hackernews · simonpure · Aug 22, 09:49 · [Discussion](https://news.ycombinator.com/item?id=49398152)

**Background**: An agent harness is the software infrastructure around an LLM that manages tool use, memory, state, execution environments, and feedback loops; it turns a language model into an agent that can perform work. Coding agents like Claude Code and Codex use sub-agent orchestration, context compression, and CLI interaction to complete tasks step by step. Deterministic simulation in this context means repeatable, scripted workflows rather than relying on live model inference at every step.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/concepts/harness">Agent Harness | Microsoft Learn</a></li>
<li><a href="https://israynotarray.com/en/ai/2026/07/14/why-more-ai-agents-lag-your-computer/">AI Runs in the Cloud — So Why Does Opening More Agents Lag Your...</a></li>

</ul>
</details>

**Discussion**: Reception is largely enthusiastic and amused by The Office theme, with the author joining the thread to answer questions and share the 20K-user milestone. A longer review praises the concept but criticizes the agent abstraction, saying it feels like pipelines and roles rather than independent agents; another commenter compares the experience to managing Michael and Dwight.

**Tags**: `#multi-agent`, `#LLM`, `#coding agents`, `#harness`, `#simulation`

---

<a id="item-3"></a>
## [Developer builds sub-2-bit quantized LLM, 60 MB model runs at 400 tok/s on CPU](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 8.0/10

A developer trained a 250M-parameter LLM from scratch on 30B tokens of FineWeb and quantized it to under 2 bits per weight, yielding a 60 MB deployment that runs at about 400 tokens per second on a laptop CPU with no GPU. The model also uses a 512-bit fixed code vocabulary (8.4 MB for 131k tokens, zero trained parameters) and a disk-based long-context cache that compresses older tokens to 1 bit. This demonstrates that highly compressed LLMs can be trained and deployed on-device with minimal memory and disk footprint, pushing the boundaries of efficient inference for edge devices and personal use. It also challenges the assumption that long-context handling requires massive RAM or specialized hardware, as the disk cache enables retrieval from up to 100M tokens of history. The model has a cross-entropy of 3.15 nats per token (perplexity 23.3, 0.99 bits per byte) on held-out educational web text. The most recent 2048 tokens stay in fp16 as a normal KV cache, while older tokens are compressed to 1 bit and written to disk at about 320 bytes per token; the author notes the model was trained only to retrieve and answer from the disk cache, not to reason over it. WordSim-353 Spearman correlation is 0.619 for the fixed-code table vs 0.029 for random codes.

reddit · r/MachineLearning · /u/Final-Data-1410 · Aug 22, 04:39

**Background**: Quantization reduces the precision of model weights to lower-bit representations (e.g., 8-bit, 4-bit, or in this case sub-2-bit) to shrink memory and accelerate inference. The FineWeb dataset is a 15-trillion-token web-scale corpus released by Hugging Face, often used for LLM pretraining research. A KV cache stores intermediate key and value matrices during autoregressive generation to avoid recomputation; here it is partially offloaded to disk to handle long contexts. The model uses a fixed 512-bit code per token instead of a learned embedding table, cutting storage and enabling the disk cache to reference tokens efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/AI-Efficiency/Awesome-Model-Quantization">GitHub - AI-Efficiency/Awesome-Model- Quantization : A list of papers...</a></li>
<li><a href="https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1">FineWeb: decanting the web for the finest text data at scale ...</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#efficient-inference`, `#on-device`, `#training`

---

<a id="item-4"></a>
## [Tesla Announces Supervised FSD Now Available in China](https://t.me/zaihuapd/43321) ⭐️ 8.0/10

Tesla announced on social media platform X that its supervised Full Self-Driving (FSD) system is now available for use in China. This marks the official entry of the feature into the Chinese market. This is a significant regulatory and market milestone for autonomous driving in China, as Tesla's FSD enters one of the world's largest automotive markets. It could intensify competition among local autonomous driving developers and influence future regulation. The announcement was brief and did not disclose specific pricing, vehicle model compatibility, or rollout timelines. FSD (Supervised) remains a Level 2 driver-assistance system that requires a fully attentive driver at all times.

telegram · zaihuapd · Aug 22, 01:56

**Background**: Tesla's Full Self-Driving (Supervised) is an advanced driver-assistance system that can handle route navigation, steering, lane changes, and parking under active driver supervision. It is classified as Level 2 automation by SAE standards, meaning the driver must remain engaged and ready to take control. Tesla has shifted its branding from 'full autonomy' to 'supervised' to reflect the system's actual capabilities and the need for driver oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tesla.com/fsd">Full Self-Driving (Supervised) - Tesla</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot">Tesla Autopilot - Wikipedia</a></li>
<li><a href="https://opentools.ai/news/teslas-bold-dreams-of-full-autonomy-shift-to-supervised-reality">Tesla 's Bold Dreams of Full Autonomy Shift to Supervised Reality</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#FSD`, `#autonomous-driving`, `#China`, `#regulation`

---

<a id="item-5"></a>
## [Amazon Exposed for Buying and Destroying Scanned Books for AI Training](https://t.me/zaihuapd/43331) ⭐️ 8.0/10

404 Media's investigation reveals that Amazon is mass-purchasing print books, scanning them for AI training, and then destroying the physical copies. A tracking device placed in a rare book traced it to an Amazon warehouse in Las Vegas, where workers reportedly cut off bindings to speed up scanning before discarding the pages. This practice raises serious copyright and ethical concerns, as it mirrors Anthropic's similar reported behavior and highlights the lengths AI companies will go to secure training data. It could intensify scrutiny of how tech giants obtain and treat copyrighted material, affecting authors, publishers, and the broader AI/ML community. Workers at the Las Vegas warehouse reportedly receive large quantities of printed books, cut off the bindings to accelerate scanning, and then dispose of the pages. The investigation used a tracking device hidden inside a rare book to confirm the book's journey into Amazon's facility.

telegram · zaihuapd · Aug 22, 15:40

**Background**: This news follows similar reports about Anthropic using copyrighted books in AI training. Training large language models often requires massive text corpora, and some companies resort to scanning physical books to obtain digitized text. The reported destruction of originals adds a new dimension to existing debates about fair use, piracy, and intellectual property in the AI era.

**Tags**: `#AI training`, `#copyright`, `#Amazon`, `#books`, `#ethics`

---