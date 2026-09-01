---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 42 items, 7 important content pieces were selected

---

1. [Anthropic Releases Claude Fable 5.1 and Mythos 5.1 with Better Writing and Cheaper Caching](#item-1) ⭐️ 9.0/10
2. [Examining Ed Zitron's AI Skeptic Track Record](#item-2) ⭐️ 8.0/10
3. [Jujutsu Creator Martin Joins ERSC](#item-3) ⭐️ 8.0/10
4. [Small Transformer Trained in 1.5 Hours Outperforms Many LLMs on ARC](#item-4) ⭐️ 8.0/10
5. [Korea's Trillion-Dollar AI Investment: Nvidia Wins, Hynix and Samsung Lose](#item-5) ⭐️ 8.0/10
6. [Mapping Latent Reasoning: Five Families Beyond Chain-of-Thought](#item-6) ⭐️ 8.0/10
7. [EvoUndo Framework Ensures Recoverability for LLM Agent Self-Evolution](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic Releases Claude Fable 5.1 and Mythos 5.1 with Better Writing and Cheaper Caching](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic has announced Claude Fable 5.1 and Claude Mythos 5.1, featuring improved writing style, a cache read price cut from $1/M to $0.25/M, and multiple reasoning effort levels (low, medium, high, xhigh, max). The new models are now available, with a system card published for the release. This major release strengthens Anthropic's position in the competitive LLM market and could affect how developers choose models. The substantial cache discount and tunable reasoning effort may significantly lower API costs for high-volume users while making advanced reasoning more accessible. According to community analysis, the cache read price drop from $1/M to $0.25/M makes Fable 5.1's cache reads half the cost of Claude Opus's $0.5/M rate, potentially signaling a ceiling on LLM pricing. The release also includes a system card with safety evaluations, and the platform documentation highlights writing-style improvements that go beyond benchmark scores.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**Background**: Prompt caching is a common LLM API feature that reuses processing of a stable prefix, such as a system prompt or tool definitions, to reduce cost and latency; cache reads are billed at a discount compared to fresh input tokens. Reasoning effort levels control how much 'thinking' a model performs before answering, letting users trade latency and cost for accuracy. System cards are documents Anthropic publishes to describe a model's capabilities, safety evaluations, and responsible deployment decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://ofox.ai/blog/llm-api-cache-hit-math-real-bills-2026/">LLM API Cache Hit Math: Why Your DeepSeek Bill Says $4 But the Pricing Says $50</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/reasoning-effort">Reasoning effort - LLM Parameter Guide - Vellum</a></li>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Community reaction is largely positive. An Anthropic employee highlights a marked improvement in writing style and responsiveness to style instructions, while another commenter points out that the cache hit discount suggests users may need to re-optimize their autocompaction thresholds. A developer tested the reasoning effort levels from low to max, noting that max produced significantly better results after roughly 14 minutes of generation, and another commenter argued the new cache pricing could indicate a ceiling on LLM pricing.

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#Model Release`

---

<a id="item-2"></a>
## [Examining Ed Zitron's AI Skeptic Track Record](https://danluu.com/zitron/) ⭐️ 8.0/10

Dan Luu's new post examines how accurate Ed Zitron's AI-skeptic predictions have been, and the analysis has generated 259 comments debating whether Zitron is wrong or simply early. The discussion highlights hyperscaler accounting practices and government intervention as key factors. Zitron is one of the most prominent AI critics, so evaluating his prediction record helps audiences calibrate how much weight to give AI skepticism. The debate also reveals how unprecedented fiscal and monetary policy can distort the apparent accuracy of tech forecasters. Commenters note that hyperscalers like Google, Meta, and Microsoft invest in Anthropic and OpenAI, booking valuation increases as Other Income that inflates reported revenue and earnings. Others argue Zitron is just early because government interventions have repeatedly pushed risk into the future.

hackernews · jatins · Sep 1, 18:35 · [Discussion](https://news.ycombinator.com/item?id=49526069)

**Background**: Ed Zitron is a tech commentator and host of the 'Better Off Line' podcast, known for sharply critical takes on AI hype. Dan Luu is a software engineer and blogger who often analyzes industry claims with data. The broader context is a multi-year AI investment boom where skeptics and boosters are locked in a high-stakes argument over whether AI's economic returns justify the spending.

**Discussion**: The comments are largely sympathetic to Zitron's frustration but split on his accuracy. One top comment says he has become the mirror image of AI boosters and can never concede being wrong, while another argues he is not wrong, just early because government fiscal and monetary interventions have repeatedly supported near-term results. A third reader says Zitron's exaggerations make his urgent case harder to trust.

**Tags**: `#AI`, `#Skepticism`, `#Tech Analysis`, `#Community Discussion`

---

<a id="item-3"></a>
## [Jujutsu Creator Martin Joins ERSC](https://ersc.io/blog/martin-joins-ersc) ⭐️ 8.0/10

Martin, the creator of the Jujutsu version control system, has joined ERSC, an emerging GitHub competitor. The announcement was posted on ERSC's blog, with Steve Klabnik hinting that more news is coming soon. This move signals ERSC's ambition to build a next-generation developer platform while jj continues to gain momentum as a powerful Git-compatible version control system. The collaboration could accelerate jj's adoption and influence the future of developer tooling. The announcement appeared on ERSC's blog (ersc.io/blog/martin-joins-ersc), and Steve Klabnik said, "We'll have some more stuff to talk about very soon." ERSC's exact product plans remain undisclosed, but community discussions highlight jj's undo model and its compatibility with existing Git repositories.

hackernews · steveklabnik · Sep 1, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49525297)

**Background**: Jujutsu (also known as jj) is a modern version control system designed to overcome many of Git's usability limitations while remaining compatible with Git repositories. Its key ideas include treating every operation as a commit and making history easy to rewrite and undo. ERSC appears to be a new entrant aiming to provide a developer platform or a GitHub-like service.

<details><summary>References</summary>
<ul>
<li><a href="https://www.infovision.com/blog/git-and-jujutsu-the-next-evolution-in-version-control-systems/">Git and Jujutsu : The next evolution in version control systems</a></li>
<li><a href="https://neugierig.org/software/blog/2024/12/jujutsu.html">Tech Notes: The Jujutsu version control system</a></li>

</ul>
</details>

**Discussion**: The community response is mixed. Fallat is skeptical, arguing that Git already does everything Jujutsu does and questioning ERSC's value proposition as a GitHub competitor. Minraws and jph counter that jj's undo model and better UX make it genuinely superior, while steveklabnik teases upcoming news.

**Tags**: `#jujutsu`, `#version-control`, `#devtools`, `#ersc`, `#open-source`

---

<a id="item-4"></a>
## [Small Transformer Trained in 1.5 Hours Outperforms Many LLMs on ARC](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 8.0/10

The author trained a small autoregressive transformer from scratch in just 1.5 hours and reported it beats many large language models on the ARC benchmark. The result, posted as a blog article, includes a clarification that the model is not an LLM but a compact transformer. This result challenges the assumption that strong reasoning performance requires enormous models and training budgets. It suggests compact, task-specific architectures can still deliver competitive results on hard generalization benchmarks like ARC-AGI-1. The model reportedly reaches about 44% on the ARC-AGI-1 benchmark. The author notes that ARC is a meta-learning benchmark, so learning from the demonstration pairs in evaluation tasks is part of the intended setup, not a case of training on test labels.

hackernews · porridgeraisin · Sep 1, 09:52 · [Discussion](https://news.ycombinator.com/item?id=49519939)

**Background**: The Abstraction and Reasoning Corpus (ARC) was introduced in 2019 by François Chollet to measure fluid intelligence in AI systems. Its tasks require abstract reasoning and generalization from a few examples, which is why even large models struggle with it. A new benchmark variant, ARC-AGI-1, is used to evaluate AI systems' ability to solve unseen reasoning problems.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>
<li><a href="https://arcprize.org/arc-agi/1">ARC-AGI-1</a></li>
<li><a href="https://lab42.global/arc/">About ARC – Lab42</a></li>

</ul>
</details>

**Discussion**: Commenters were largely engaged and impressed; the author answered questions directly, clarifying that the model is not an LLM and addressing the 'training on test' criticism. Some commenters asked for a simpler explanation of why this is not cheating, while others wondered what score a competent human would achieve on ARC-AGI-1.

**Tags**: `#transformer`, `#ARC benchmark`, `#machine learning`, `#AI`, `#LLM`

---

<a id="item-5"></a>
## [Korea's Trillion-Dollar AI Investment: Nvidia Wins, Hynix and Samsung Lose](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 8.0/10

SemiAnalysis published an analysis of Korea's trillion-dollar sovereign AI investment, arguing that Nvidia is the biggest winner while domestic memory makers SK Hynix and Samsung face adverse implications. The report also describes a 'National AI Tournament' in which the best non-Chinese open-source model is eliminated, highlighting the contentious role of open-source models in sovereign AI strategies. This analysis matters because Korea's massive sovereign AI spending will reshape global AI supply chains, directly affecting Nvidia's accelerator sales and the HBM memory market dominated by SK Hynix and Samsung. The outcome could influence how other countries execute sovereign AI programs, especially their stance on open-source models and domestic chip procurement. The report references a 'Squid Games'-style National AI Tournament in Korea, where the best non-Chinese open-source model is eliminated — a detail that underscores the politically charged nature of model selection. It devotes specific attention to Hynix and Samsung, examining how the sovereign AI build-out might undermine their HBM and memory businesses despite being domestic champions.

rss · Semianalysis · Sep 1, 20:14

**Background**: Sovereign AI refers to national efforts to increase control over AI capabilities and reduce dependence on foreign providers, often through public computing infrastructure, local models, and data governance. High Bandwidth Memory (HBM) is a 3D-stacked DRAM technology used in AI accelerators like Nvidia's GPUs, delivering high data throughput for data-intensive workloads. Samsung and SK Hynix are the world's leading HBM producers, while Nvidia designs the accelerators that consume most of this memory, making the three companies highly interdependent in the AI supply chain.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI">Sovereign AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Semiconductors`, `#Sovereign AI`, `#Investment`, `#Nvidia`

---

<a id="item-6"></a>
## [Mapping Latent Reasoning: Five Families Beyond Chain-of-Thought](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 8.0/10

A Reddit post maps the 2026 latent reasoning landscape, categorizing work into five distinct families including Coconut-style continuous thoughts and BDH-CQ's recurrent in-context latent reasoning. It argues that progress toward AGI depends less on longer verbalized chains of thought and more on architectures that reason beyond the token stream. The post challenges a core assumption behind current LLM reasoning: that verbalized chain-of-thought reflects actual computation, arguing instead that it is often an imitation of reasoning. If latent reasoning proves more efficient, the industry's interpretability and evaluation practices that rely on readable traces may need to be rethought. The taxonomy separates continuous-thought models (Coconut, Soft Thinking), compressed non-linguistic discrete tokens (Abstract-CoT), recurrent-depth/looped Transformers, task-trained recursive solvers (HRM, TRM), and in-context recurrent latent solvers (BDH-CQ). The author highlights two key axes—how a system acquires a new task and where intermediate computation happens—and notes BDH-CQ reports surpassing a published cost–accuracy Pareto frontier on ARC-AGI-1 with pretraining scaling laws up to 600B parameters.

reddit · r/MachineLearning · /u/Typical-Scene-5794 · Sep 1, 15:14

**Background**: Latent reasoning is an alternative to chain-of-thought: instead of verbalizing every intermediate step, the model repeatedly transforms its continuous hidden state and decodes only the final answer. Coconut, introduced by Meta FAIR in 2024, was an early demonstration that feeding the last hidden state back as the next input embedding can enable reasoning in a continuous latent space. HRM and TRM are recursive solvers that refine latent and candidate-answer states, with the 7M-parameter TRM reaching 45% on ARC-AGI-1. BDH-CQ builds on the Dragon hatchling architecture to combine in-context learning with recurrent latent reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in a ... Coconut: A Framework for Latent Reasoning in LLMs GitHub - facebookresearch/coconut: Training Large Language ... Training Large Language Models to Reason in a Continuous ... ModalityDance/latent-tts-coconut · Hugging Face Coconut: Training Large Language Models to Reason in a ... Coconut LLM</a></li>
<li><a href="https://medium.com/@m.mastrodonato/thinking-small-reasoning-deep-how-hrm-and-trm-redefine-the-architecture-of-intelligence-68d748a9ffe5">Thinking Small, Reasoning Deep: How HRM and TRM Redefine the Architecture of Intelligence | by Marco Mastrodonato | Medium</a></li>
<li><a href="https://arxiv.org/abs/2608.09888">[2608.09888] BDH-CQ: In-Context Learning with Recurrent Latent Reasoning</a></li>

</ul>
</details>

**Tags**: `#latent reasoning`, `#chain-of-thought`, `#LLM`, `#AGI`, `#machine learning`

---

<a id="item-7"></a>
## [EvoUndo Framework Ensures Recoverability for LLM Agent Self-Evolution](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 8.0/10

EvoUndo, a new framework for recoverability-constrained self-evolution, lets LLM agents synthesize, diagnose, and verify reversible self-modifications across counterfactual states. In evaluations on 600 one-shot tasks, it identified 197 capability-improving mutations that fail recoverability verification, and an extended recovery calculus boosted oracle recovery from 48/197 to 191/197. This addresses a critical safety and reliability problem in AI agent systems: self-modifications can improve capability but leave persistent effects that cannot be safely reversed in different states. The results show that reliable agent self-evolution requires co-designing verification, state grounding, witness semantics, and recovery-language expressivity rather than relying on iterative prompting alone. A protocol-locked 2×2 grounding-by-expressivity intervention separated two bottlenecks: exact state-address grounding increased recovery from 0/48 to 38/48 (79.2%) when the original language was sufficient, while extending the recovery language enabled recovery on 142/143 (99.3%) failures in the S1 stratum. On the gpt-oss-120b backbone, adding exact-address diagnostics to the richer language reduced recovery to 133/143 (93.0%), but a Qwen3.8-27B replication preserved the main effects without the negative interaction, indicating model dependence.

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Sep 1, 19:17

**Background**: LLM agents increasingly modify their own prompts, tools, middleware, resources, and execution harnesses at runtime, a process known as self-evolution. A key danger is that a mutation successful in one state may leave persistent effects that cannot be reversed when the agent is in a different state. EvoUndo formalizes recoverability across counterfactual states and evaluates whether model-generated self-modifications can be safely undone, establishing a foundation for auditable self-evolving agents.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28363">[2608.28363] EvoUndo: Recoverability - Constrained Self - Evolution ...</a></li>
<li><a href="https://arxiv.org/html/2608.28363">EvoUndo: Recoverability-ConstrainedSelf-Evolution for LLM Agent Harnesses</a></li>
<li><a href="https://huggingface.co/papers/2608.28363">Paper page - EvoUndo: Recoverability - Constrained Self - Evolution ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#AI safety`, `#self-evolution`, `#recoverability`, `#systems`

---