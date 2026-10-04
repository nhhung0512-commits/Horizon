---
layout: default
title: "Horizon Summary: 2026-10-04 (EN)"
date: 2026-10-04
lang: en
---

> From 25 items, 4 important content pieces were selected

---

1. [Strata claims 125B Qwen3.8-Flash-Next runs on a single RTX 4090](#item-1) ⭐️ 8.0/10
2. [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](#item-2) ⭐️ 8.0/10
3. [SK Telecom Apologizes for Massive Breach, Offers Free USIM Replacements](#item-3) ⭐️ 8.0/10
4. [Google Releases VeriHarness Agentic Verification Framework for Long-Horizon Tasks](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Strata claims 125B Qwen3.8-Flash-Next runs on a single RTX 4090](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

A GitHub project called Strata (Niko1221/Strata) released one-click installers for Windows and Linux that let users run the 125B-parameter Qwen3.8-Flash-Next model on consumer hardware, offering an OpenAI/Anthropic-compatible API on localhost. In the Hacker News thread, a user (snehesht) reported achieving 124 tokens/sec on an RTX 4090 paired with 128GB DDR5 and a Ryzen 7950X3D, matching the project's ~100 tokens/s claim. If the performance claims hold up, this would bring a 125B-class open-weight multimodal model onto prosumer hardware at usable throughput, challenging established inference stacks like llama.cpp and widening access to large models beyond data-center GPUs. However, the debate over quality at extremely low bit-widths means the real-world usefulness — not just raw speed — is what the community is now scrutinizing. Qwen3.8-Flash-Next is a 125B-parameter Mixture-of-Experts model with an additional 51B N-gram embeddings and only about 6B parameters activated per token, a configuration that makes high throughput feasible despite the large total size. The key caveat comes from commenter Jackson__, whose 50-image vision benchmark found Strata produced a median error distance of 154.8 pixels versus 46.5 pixels when running the exact same GGUF and vision adapter weights on llama.cpp — a large quality gap suggesting sub-4-bit quantization tradeoffs.

hackernews · snehesht · Oct 4, 12:51 · [Discussion](https://news.ycombinator.com/item?id=49953495)

**Background**: Mixture-of-Experts (MoE) models like Qwen3.8-Flash-Next contain many parameters but only activate a small subset per token, which is why a 125B model can run quickly on limited hardware. Quantization reduces the numerical precision of weights (e.g., to 4-bit or less) so large models fit into limited VRAM, trading some accuracy for memory savings and speed. Strata's approach combines GPU and system RAM to host the model, and the whole discussion reflects an ongoing tension between how fast a model runs and how much quality is lost when you compress it hard.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Niko1221/Strata/releases">Releases · Niko1221/ Strata · GitHub</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/qwenlm/qwen3.8-flash-next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>

</ul>
</details>

**Discussion**: Sentiment is split: some users report strong results (snehesht's 124 tok/s, AntiRush's 255 tok/s decode on an RTX 6000 Pro), while others are skeptical of going below 4-bit quants. The most substantive counterpoint is Jackson__'s independent vision benchmark showing Strata's error being roughly three times higher than llama.cpp on identical weights, and a11r notes that 4-bit quants are already 'good enough' for difficult coding tasks, implying sub-4-bit may not be worth the quality loss.

**Tags**: `#local-llm`, `#inference-optimization`, `#quantization`, `#gpu`, `#llm-serving`

---

<a id="item-2"></a>
## [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

Over the past 30 days, the top ARC-AGI-3 scores on Kaggle rose from 7% to 56%, according to a Reddit post on r/MachineLearning. Smallish local models wrapped in an evaluation harness have now reportedly started beating average human performance on this benchmark. ARC-AGI is explicitly designed under the principle "easy for humans, hard for AI" to measure progress toward general intelligence without leaning on scale or memorized training data, so a rapid jump toward and past average-human performance is a meaningful signal about reasoning progress. The fact that the gains come from small models plus harness scaffolding rather than frontier-scale compute suggests agentic design and evaluation engineering may matter as much as raw model capability. The Reddit poster notes the leaderboard graphic they shared is slightly out of date, and that Kaggle competition rules restrict participants to smallish local models, so the improvement is largely attributable to harness/agent scaffolding rather than to very large models. ARC-AGI-3 is positioned as an agentic benchmark, meaning tasks involve interacting with an environment over time rather than solving a single static puzzle.

reddit · r/MachineLearning · /u/we_are_mammals · Oct 4, 10:24 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**Background**: ARC-AGI (Abstraction and Reasoning Corpus) was introduced by François Chollet and is now run by the nonprofit ARC Prize Foundation; each task gives a few input-output grid examples and the solver must infer the underlying transformation rule, with tasks constructed so the patterns cannot simply be memorized from training data. ARC-AGI-3 extends the idea toward interactive, agentic environments. An "eval harness" is the scaffolding that runs a model against a benchmark — handling prompting, sampling, tool use and scoring — which is why the same underlying model can score very differently depending on how it is driven.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - The only AI benchmark that measures AGI progress.</a></li>
<li><a href="https://arcprize.org/">ARC Prize Foundation is a nonprofit advancing open-source AGI ...</a></li>
<li><a href="https://github.com/EleutherAI/lm-evaluation-harness">GitHub - EleutherAI/lm-evaluation-harness: A framework for ...</a></li>

</ul>
</details>

**Tags**: `#ARC-AGI`, `#Kaggle`, `#benchmark`, `#AI reasoning`, `#local models`

---

<a id="item-3"></a>
## [SK Telecom Apologizes for Massive Breach, Offers Free USIM Replacements](https://t.me/zaihuapd/44206) ⭐️ 8.0/10

South Korea's largest telecom operator SK Telecom (SKT) confirmed that hackers breached its internal systems, including a core Home Subscriber Server (HSS), exposing sensitive data such as IMEI, serial numbers, ICCID, PIN2/PUK2, eID, encrypted K values and private keys, affecting more than 25 million users. CEO issued a public apology and announced free USIM card replacements for all SKT subscribers who want one (including MVNO users on its network, with some device exceptions), plus reimbursement for those who already paid for a replacement recently. This is one of the largest telecom data breaches ever disclosed, and the exposure of SIM authentication keys and private keys strikes at the root of trust for mobile identity, potentially enabling SIM cloning, account takeover and interception attacks at scale. It affects roughly half of South Korea's population and puts pressure on carriers worldwide to harden core network systems and reconsider how subscriber secrets are stored. The compromised HSS is the master subscriber database in 4G/5G core networks responsible for authentication and service profiles, and the leaked ICCID is the globally unique 19–20 digit serial number assigned to each SIM per the ITU-T E.118 standard. SKT is fast-tracking USIM replacements to force new authentication credentials, though replacements do not retroactively undo any data already exfiltrated, and some devices (notably certain eSIM or embedded modules) are excluded from the offer.

telegram · zaihuapd · Oct 4, 09:02

**Background**: Every mobile subscriber is authenticated by a secret key (the 'K' key) stored both in the SIM card and in the operator's Home Subscriber Server; the SIM and network run a challenge-response handshake to prove identity without ever transmitting the key itself. The ICCID is the SIM's unique serial number printed on the card, while PIN2/PUK2 are secondary PIN and unblock codes, and eID is an embedded identity identifier. If an attacker obtains the K key and associated identifiers, they can in principle clone a SIM or impersonate a subscriber, which is why operators treat HSS data as highly sensitive.

<details><summary>References</summary>
<ul>
<li><a href="https://www.p1sec.com/blog/home-subscriber-server-hss">Home Subscriber Server (HSS): The Backbone of Modern Telecom ...</a></li>
<li><a href="https://telnyx.com/resources/iccid-number">ICCID number: how to find, decode, and use it - Telnyx ICCID/SIM Card Number Checker/Decoder - phone.fyicenter.com ICCID decoder online — validate and break down any SIM number Free Sim Card Decoder - Decode ICCID & IMSI Online ICCID Lookup. Decode Any SIM Card Serial Number | Irreva ICCID Checker - IMEI.info How to Find Your SIM Card Number (ICCID) on Any Device</a></li>
<li><a href="https://en.wikipedia.org/wiki/SIM_card">SIM card - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#telecom`, `#privacy`, `#SK Telecom`

---

<a id="item-4"></a>
## [Google Releases VeriHarness Agentic Verification Framework for Long-Horizon Tasks](https://arxiv.org/abs/2610.00972v1) ⭐️ 8.0/10

Google Research released VeriHarness, a training-free, plug-and-play agentic verification harness that uses the same model that produced candidate answers to verify them: it checks environment evidence for divergent claims and actively challenges consensus claims, then selects, revises, or rebuilds the final output. Across 5 long-horizon benchmarks and 2 models it achieved the best selection scores, and evidence-driven revision improved Gemini 3.5 Flash by 6.2 points and Claude Opus 4.8 by 6.4 points on average over single-pass generation, with roughly 26,000 rollouts released publicly. Verification is widely seen as the bottleneck for long-horizon agents, where a single wrong step can derail an entire trajectory, so a harness that improves output selection and revision without any fine-tuning could be broadly applied to existing frontier models. Releasing ~26k rollouts also gives the community a dataset for studying and training verifiers, which may accelerate progress on agentic reasoning and evaluation. A notable design choice is same-model verification, meaning the verifier does not depend on a stronger external judge model, which keeps the method cheap and self-contained. The framework is training-free and plug-and-play across benchmarks and models, and its two verification modes split claims into divergent ones (checked against environment evidence) and consensus ones (adversarially challenged); the reported gains are measured on selection and revised final outputs rather than on raw single-shot generation.

telegram · zaihuapd · Oct 4, 13:32

**Background**: Long-horizon tasks are multi-step jobs that require an agent to make many sequential decisions over a long trajectory — for example multi-site web browsing workflows or office-suite tasks — and existing benchmarks for short, single-site tasks are approaching saturation for frontier models. A common way to improve agent outputs is best-of-N sampling, where several candidate attempts (called rollouts) are generated and then a verifier or judge picks the best one. VeriHarness targets exactly that selection step, and also adds revision so that a weak candidate can be repaired rather than merely discarded.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.00972">VeriHarness : Scaling Agentic Verification for Long - Horizon Tasks</a></li>
<li><a href="https://github.com/google-research/veriharness">GitHub - google -research/ veriharness · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#LLM verification`, `#long-horizon tasks`, `#agentic reasoning`, `#Google Research`

---