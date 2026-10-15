---
layout: default
title: "Horizon Summary: 2026-10-15 (EN)"
date: 2026-10-15
lang: en
---

> From 36 items, 7 important content pieces were selected

---

1. [Citizen Lab: AdFection used targeted ads to deliver zero-click spyware](#item-1) ⭐️ 9.0/10
2. [Meta Releases Muse Spark Open, an 816B-A42B Open-Weight Model for Consumer Hardware](#item-2) ⭐️ 8.0/10
3. [Goodfire's Nick Cammarata argues neural networks are fundamentally 'clean'](#item-3) ⭐️ 8.0/10
4. [Libreboot 26.10 "Ominous Olive" adds UEFI/EDK2 and 233 Chromebooks](#item-4) ⭐️ 8.0/10
5. [Essay Explores Mathematicians' Existential Dread as AI Nears Discovery](#item-5) ⭐️ 8.0/10
6. [Anthropic tells investors Q3 revenue hit $16.8bn, up nearly 50%](#item-6) ⭐️ 8.0/10
7. [MIT and PNAS: Neural Networks Self-Assemble Their Own Learning Circuits](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Citizen Lab: AdFection used targeted ads to deliver zero-click spyware](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 9.0/10

The Citizen Lab published research on a campaign it calls "AdFection," in which an Israeli-registered advertising firm, Discover-Tech, allegedly turned targeted advertising infrastructure into a delivery pipeline for zero-click mercenary spyware aimed at specific individuals. The findings were covered by The Guardian, The Verge, and WIRED in October 2026, and the underlying Citizen Lab report documents both the distribution chain and the command-and-control servers involved. If ad networks can be used as a spyware delivery channel, then the common assumption that "not clicking anything" keeps you safe no longer holds for journalists, activists, and civil society targets. It also puts fresh pressure on the adtech industry and regulators to answer who is accountable when ad delivery itself becomes the attack vector. An AdTech engineer with 13 years of industry experience noted in the discussion that the report is "highly sensationalist" about the zero-click aspect: it details distribution and C&C but is vague on the actual mechanism that activated the malware without user interaction. Commenters also stressed that there is no single monolithic "ad provider," since the adtech ecosystem is made up of many intermediaries such as exchanges, SSPs, DSPs, and publishers.

hackernews · jcomp · Oct 15, 10:43 · [Discussion](https://news.ycombinator.com/item?id=50101813)

**Background**: Zero-click spyware is malware that infects a device without any click or interaction from the victim, typically by exploiting flaws in the operating system or an app. Mercenary spyware is commercial surveillance tooling sold to government clients, a threat category Apple has repeatedly warned users about through threat notifications sent to people in over 150 countries. Targeted advertising lets a buyer select audiences by criteria such as location and device type through ad exchanges, which means an attacker could in principle "buy" impressions aimed at one specific person and turn the ad pipeline into a delivery channel. The Citizen Lab is a University of Toronto research group that has long tracked the abuse of commercial surveillance technology.

<details><summary>References</summary>
<ul>
<li><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Exposing AdFection : How Discover-Tech Turned... - The Citizen Lab</a></li>
<li><a href="https://www.wired.com/story/nightmare-scenario-zero-click-spyware-is-infecting-phones-via-targeted-ads/">‘Nightmare Scenario’: Zero-Click Spyware Is Infecting Phones... | WIRED</a></li>
<li><a href="https://news.ycombinator.com/item?id=50101813">Zero-Click Spyware Delivered via Targeted Ads : AdFection</a></li>

</ul>
</details>

**Discussion**: Hacker News discussion (roughly 347 points and 505 comments) was divided: an AdTech engineer disputed the zero-click framing and the notion of a single responsible "ad provider," while others argued for banning online advertising outright or instead suing the websites where the ads were actually displayed. Several commenters questioned whether Israeli cybersecurity firms can be trusted as independent actors given their ties to the state, and debated why Israel ranks so high among global cyber powers.

**Tags**: `#spyware`, `#adtech`, `#cybersecurity`, `#privacy`, `#zero-click exploits`

---

<a id="item-2"></a>
## [Meta Releases Muse Spark Open, an 816B-A42B Open-Weight Model for Consumer Hardware](https://research.meta.ai/blog/muse-spark-open) ⭐️ 8.0/10

Meta released Muse Spark Open, an open-weight Mixture-of-Experts model with 816 billion total parameters and 42 billion active parameters (816B-A42B), published on Hugging Face alongside deployment documentation and a launch blog. Meta emphasizes that the model is optimized to run on consumer hardware such as a Mac Studio, with day-one support across runtimes including Unsloth and MLX. This is Meta's most significant push back into the open-weight race, and it arrives in a market where Chinese open-weight models such as Qwen and GLM have become strong defaults for self-hosting. If large MoE models can realistically run on a single high-end desktop, it reshapes who can deploy frontier-adjacent capabilities without renting cloud GPUs. The license is not unrestricted: it contains a "Model as a Service" clause that restricts third parties from offering the model's outputs via an API or similar interface if the licensee and its affiliates exceed $20 million in aggregate gross revenue. Because it is a Mixture-of-Experts design, the 42B active parameters determine inference speed while the full 816B parameter set still drives memory requirements, meaning consumer-hardware runs depend on aggressive quantization.

hackernews · bigwheels · Oct 15, 17:47 · [Discussion](https://news.ycombinator.com/item?id=50107379)

**Background**: Mixture-of-Experts (MoE) models split the network into many specialized "expert" sub-networks and activate only a few per token, so they have two parameter counts: a large total for stored knowledge and a much smaller active count for speed. A model labeled 816B-A42B therefore stores 816 billion parameters but only computes through 42 billion at a time, which is why such models can be fast yet still demand enormous memory. "Open-weight" means the trained weights are downloadable and runnable locally, but it is a separate question from the license terms, which can restrict commercial or hosted use. Rivals in this space include Alibaba's Qwen series and Z.ai's GLM series, both widely hosted and self-hosted, and benchmark aggregators such as Artificial Analysis compare such models on intelligence, speed and price.

<details><summary>References</summary>
<ul>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts (MoE) explained for local LLMs · localmodel.run</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(large_language_model)">GLM (large language model)</a></li>
<li><a href="https://artificialanalysis.ai/leaderboards/models">LLM Leaderboard - Comparison of AI models from... | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Commenters were split: one cited Artificial Analysis data showing Muse Spark Open underperforming Qwen3.8 Flash Next and GLM 5.3 Flash, both of which fit on a single B300, and argued Meta has catching up to do. Others pushed back on the "open" framing, quoting the license's Model-as-a-Service clause and $20M revenue threshold, while supporters praised Meta's broad runtime support (Unsloth, MLX) and argued that if Meta's model becomes the standard, its ecosystem lock-in — not raw license openness — is the real moat.

**Tags**: `#open-weight-models`, `#Meta`, `#LLM`, `#model-licensing`, `#AI-benchmarks`

---

<a id="item-3"></a>
## [Goodfire's Nick Cammarata argues neural networks are fundamentally 'clean'](https://already-clean.goodfire.com/) ⭐️ 8.0/10

Nick Cammarata, an interpretability researcher at Goodfire who co-authored early mechanistic interpretability work at OpenAI, published a post titled "Neural networks are clean" at already-clean.goodfire.com, arguing that neural networks are largely non-superpositional and mostly interpretable rather than messy. The post is accompanied by an interactive "microscope" demo that Cammarata describes as "the first non-trivial neural network I feel I mostly understand." If neural networks are genuinely "clean" and largely interpretable by default, it would undercut the assumption that superposition is the core obstacle blocking mechanistic interpretability, which many researchers frame as a prerequisite for solving AI alignment. The claim therefore matters to alignment and interpretability labs such as Goodfire, Anthropic and OpenAI, and to the broader debate about how much of a model's internals we can actually reverse-engineer. Cammarata frames the finding as an alignment-relevant breakthrough, arguing in his launch post that "we can't solve alignment if we don't know what we're building," and links an interactive demo. Critics counter that the claims go beyond what has been proven, noting that progressive feature complexity and the Lottery Ticket Hypothesis have long been known and are not mutually exclusive with parameter overloading/superposition, and that multimodal gap work (arXiv:2203.02053) suggests networks tend toward condensed representations.

hackernews · themgt · Oct 15, 16:04 · [Discussion](https://news.ycombinator.com/item?id=50105647)

**Background**: Mechanistic interpretability (mech interp) is a subfield of explainable AI that tries to reverse-engineer the concrete structures, algorithms and circuits inside neural networks into human-understandable explanations. A central concept is superposition: because models have far fewer neurons than features they must represent, features are thought to be packed together in overlapping, hard-to-read directions — the main reason interpretability is considered difficult. Goodfire is a San Francisco interpretability research lab and public benefit corporation founded by researchers who pioneered interpretability work at OpenAI and Google DeepMind, and it has raised over $200M.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://www.goodfire.com/">Goodfire AI</a></li>
<li><a href="https://www.goodfire.com/company">About Goodfire</a></li>

</ul>
</details>

**Discussion**: Commenters were split: one praised Cammarata as "a force of nature" and highlighted the launch post's framing of interpretability as the most important scientific problem, while another called the claims "an overreach of what is actually proven," citing the Lottery Ticket Hypothesis and multimodal gap work. Others pointed to concrete resources — an audio version of the post and a link to the "microscope" demo node — and one commenter compared the tone to the "hypomanic energy" of Anthropic's mech interp team around the first large-scale SAE results, when many believed the key paradigm had been found and only scaling remained.

**Tags**: `#mechanistic-interpretability`, `#AI-alignment`, `#neural-networks`, `#machine-learning`, `#research`

---

<a id="item-4"></a>
## [Libreboot 26.10 "Ominous Olive" adds UEFI/EDK2 and 233 Chromebooks](https://libreboot.org/news/libreboot2610.html) ⭐️ 8.0/10

Libreboot 26.10, codenamed "Ominous Olive", integrates UEFI support via the EDK2/TianoCore payload and imports all 233 Chromebooks currently supported by the MrChromebox coreboot distribution. The release is source-only, meaning users must build the firmware themselves rather than downloading prebuilt ROMs, and it also formalizes a strict policy against LLM-assisted contributions. Adding a UEFI/EDK2 payload plus the entire MrChromebox Chromebook device tree dramatically multiplies the number of machines Libreboot can run on, and makes porting future devices far easier by giving developers an upstream reference. This moves a project historically known for a small, carefully curated hardware list toward much broader mainstream coverage. Only Baytrail (Kip) Chromebooks are listed as tested so far, with the remaining imported devices still needing verification, and no binaries are shipped in this release. The project has also published an AGENTS file in its lbmk repository spelling out its rejection of AI-generated patches, while accepting AI-assisted bug reports in some form.

hackernews · iamnothere · Oct 15, 12:52 · [Discussion](https://news.ycombinator.com/item?id=50102923)

**Background**: Libreboot is a distribution of coreboot, the free and open-source firmware that performs low-level hardware initialization and then boots an operating system, replacing proprietary BIOS or UEFI implementations. Because coreboot must be ported to each individual chipset and motherboard, hardware support depends on how many boards contributors have ported. EDK2 (TianoCore EDK II) is Intel's de facto reference implementation of the UEFI specification, and MrChromebox is a coreboot distribution that provides firmware for a large range of Chromebooks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Libreboot">Libreboot</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coreboot">Coreboot</a></li>
<li><a href="https://en.wikipedia.org/wiki/EDK2">EDK2</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree the UEFI/EDK2 integration and Chromebook support are the real headline, with one noting it "multiplied the devices available by many times" while the AI policy dominated attention. A Heads/LinuxBoot contributor (cwiggs) described overlapping work porting ChromeOS devices using MrChromebox code as an upstream dependency, and the anti-LLM-contribution stance drew both praise as "refreshing" and acknowledgment of the project's broader stance against frontier AI.

**Tags**: `#firmware`, `#coreboot`, `#libreboot`, `#UEFI`, `#open-source`, `#Chromebook`

---

<a id="item-5"></a>
## [Essay Explores Mathematicians' Existential Dread as AI Nears Discovery](https://www.derekthompson.org/p/i-know-why-the-mathematicians-weep) ⭐️ 8.0/10

Writer Derek Thompson published a philosophical essay titled "I know why the mathematicians weep," arguing that mathematicians are experiencing a form of existential dread as AI systems increasingly encroach on mathematical discovery. The piece drew 529 substantive Hacker News comments and 325 points, with much of the debate focused on whether AI is commodifying the prestige of mathematical work and eroding the social machinery that validates mathematical truth. The essay captures a broader cultural shift: as AI systems produce research-level mathematical proofs and results, the prestige, career structures, and epistemic authority of an entire academic discipline may be reorganized, not just individual jobs. It also raises a question with implications well beyond mathematics — whether truth-validation is being replaced by mere believability in an AI-saturated information environment. Commenters connected the essay, without Thompson naming it, to philosopher Robert Brandom's theory of "deontic scorekeeping," which holds that conceptual systems are sustained through a social give-and-take of reasons and entitlements. The core debate is whether AI-supplied mathematical results are validated or merely accepted on the basis of believability, shape, or volume, since even Hacker News readers reportedly treated some problems as solved without reading or checking the proofs.

hackernews · RickJWagner · Oct 15, 13:44 · [Discussion](https://news.ycombinator.com/item?id=50103630)

**Background**: Automated theorem proving, a subfield of automated reasoning and mathematical logic, has aimed to have computer programs generate formal proofs since the earliest days of computer science. Since the mid-2020s, large language models, particularly reasoning models that are trained to solve multi-step problems, have made growing progress in producing proofs at research level, mostly from OpenAI and Anthropic. This is the backdrop against which mathematicians now ask what remains distinctively human about their craft.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_mathematical_discoveries_by_artificial_intelligence">List of mathematical discoveries by artificial intelligence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reasoning_model">Reasoning model - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters broadly shared the sense of dread but traced it to different losses: one argued that the whole architecture of a life built on prestige and hard-won skill is rendered moot once that status is commodified, while another mourned not the job but the disappearance of the desire to seek truth, since nothing is validated anymore and volume or loudness substitutes for proof. A prominent thread invoked Brandom's deontic scorekeeping to argue LLMs encode our normative regularities yet are bound to be deficient in the social practices that sustain meaning, and one skeptic pushed back that Thompson misunderstands pure math entirely — mathematicians, echoing Einstein's wish to know "God's thoughts," mourn not sunk costs but the prospect of never again discovering fundamental truth themselves.

**Tags**: `#AI and mathematics`, `#AI existential impact`, `#philosophy of mathematics`, `#LLM reasoning`, `#academic culture`

---

<a id="item-6"></a>
## [Anthropic tells investors Q3 revenue hit $16.8bn, up nearly 50%](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 8.0/10

Anthropic told investors on Wednesday that its quarterly revenue rose nearly 50% to $16.8bn in Q3 (July–September), up from $11.5bn in Q2 and about $4.8bn in Q1, according to an FT report written up by Simon Willison. The company also disclosed that distillation accounted for 5% to 7% of revenue and that it had cut that usage back "materially" during the third quarter, ahead of a planned IPO. At a $16.8bn quarterly run rate, Anthropic is now operating at a scale comparable to major public software companies, which makes its IPO one of the most closely watched events in the AI industry. The disclosure that rivals were spending hundreds of millions of dollars distilling Anthropic's models also highlights how competitive dynamics and API-driven data usage are becoming material financial line items for frontier labs. In Q3 Anthropic generated $1.70 in revenue for every $1 spent on computing power, and adjusted operating margins excluding stock-based compensation were 11%, meaning profitability is still thin once compute costs are accounted for. Willison estimates that if distillation was 5% of Q2 revenue, unnamed rival labs spent over half a billion dollars distilling Anthropic's models in that quarter; notably, Anthropic appears to have stopped citing "annualized run-rate revenue" in investor communications.

rss · Simon Willison · Oct 15, 13:04

**Background**: Knowledge distillation is a technique in which one AI model (the "student") is trained on the outputs of another, usually stronger model (the "teacher") — a legitimate and widely used method for making smaller, cheaper models, but a controversial one when labs use a competitor's commercial API outputs to train rival models. Anthropic's figures come ahead of a long-anticipated IPO, and "annualized run-rate revenue" is a startup metric that extrapolates a single period's revenue across a full year, which critics say can inflate the apparent size of a fast-growing business.

<details><summary>References</summary>
<ul>
<li><a href="https://innodata.com/what-is-knowledge-distillation-in-ai/">What is Knowledge Distillation in AI ? — Innodata</a></li>
<li><a href="https://blog.roboflow.com/what-is-knowledge-distillation/">What is Knowledge Distillation ? A Deep Dive. | Roboflow Blog</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI industry`, `#IPO`, `#revenue growth`, `#distillation`

---

<a id="item-7"></a>
## [MIT and PNAS: Neural Networks Self-Assemble Their Own Learning Circuits](https://www.reddit.com/r/MachineLearning/comments/1x6hmyg/how_artificial_neural_networks_build_their_own/) ⭐️ 8.0/10

A PNAS paper published on 9 October 2026, covered by MIT News on 13 October, reports that randomly interconnected neuron-like units governed by shared local plasticity rules can spontaneously self-assemble "learning motifs" and then perform pattern recognition and image classification at a level comparable to the backpropagation-trained networks tested in the study. The key shift is from hand-designing a learning circuit to specifying only local rules from which the learning machinery organises itself. If gradient-based learning can emerge bottom-up from random connectivity and simple local plasticity rules, it offers a principled bridge between biological plasticity and modern machine learning, and could inspire more biologically plausible training approaches for hardware or neuromorphic systems. It also raises the possibility of networks whose learning circuitry does not need to be engineered by hand. The reported accuracy comparison is limited to the specific pattern-recognition and image-classification tasks tested, and the paper explicitly cautions that self-organisation does not prove the brain actually uses this mechanism — the motivation is biological plausibility rather than a claim that backpropagation can be replaced in large-scale models. Open questions include how stable the emergent motifs are under different initial connectivity and whether the approach extends beyond the demonstrated tasks.

reddit · r/MachineLearning · /u/Dorian182 · Oct 15, 10:01

**Background**: Backpropagation is the workhorse algorithm behind modern deep learning, but it requires global error signals and weight transport that are widely considered biologically implausible in real brains. In contrast, local plasticity rules — such as Hebbian-style updates that depend only on the activity of nearby neurons and synapses — are closer to what neuroscientists observe experimentally. This line of research asks whether such simple local rules, applied to a randomly wired network, can collectively give rise to something functionally equivalent to a gradient-learning circuit.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.2606245123">How biological synapses self-assemble gradient learning | PNAS</a></li>
<li><a href="https://news.mit.edu/2026/how-artificial-neural-networks-build-their-own-learning-machinery-1013">How artificial neural networks build their own learning machinery</a></li>
<li><a href="https://arxiv.org/pdf/2412.20018">Self - Assembly of a Biologically Plausible Learning Circuit</a></li>

</ul>
</details>

**Tags**: `#Neural Networks`, `#Self-Organization`, `#Plasticity`, `#Backpropagation`, `#Computational Neuroscience`

---