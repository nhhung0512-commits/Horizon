---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16
lang: en
---

> From 35 items, 7 important content pieces were selected

---

1. [Tesla Unveils Flying Roadster with Cold-Gas and Rocket Thrusters](#item-1) ⭐️ 8.0/10
2. [Claude reverse-engineers the origins of NIST ECDSA curve seeds](#item-2) ⭐️ 8.0/10
3. [Jake Archibald benchmarks JPEG XL vs AVIF for web images](#item-3) ⭐️ 8.0/10
4. [Apple runs near-trillion-parameter Meta model on four Mac Studios via MLX](#item-4) ⭐️ 8.0/10
5. [Mercor report: 90% of US work hours lack AI benchmark coverage](#item-5) ⭐️ 8.0/10
6. [Big Fish: Exploiting a 37-Year-Old OpenBSD Kernel Bug](#item-6) ⭐️ 8.0/10
7. [StepFun Releases Step 5 Preview Agent Flagship Model](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Tesla Unveils Flying Roadster with Cold-Gas and Rocket Thrusters](https://www.tesla.com/roadster) ⭐️ 8.0/10

Tesla unveiled a new Roadster equipped with cold-gas thrusters and optional combustion rocket thrusters, releasing a video and X post demonstrating dramatic vertical maneuvers and flight. The car is offered in two modes: a cold-gas version apparently using non-combusting gas for extra forward acceleration only, and a combustion-rocket version that was shown flying and is described as invite-only. This is one of the most attention-grabbing Tesla product announcements in years, mixing EV engineering with aerospace propulsion and reigniting debate about how far the company can push consumer vehicles. It also raises broader questions about hype-driven product marketing, deposit-based financing, and whether such a vehicle can ever be economically and legally viable. Cold-gas thrusters work by expelling pressurized inert gas through a nozzle with no combustion, making them the simplest and most reliable rocket engines but also far less thrust- and efficiency-efficient than monopropellant or bipropellant engines. Because onboard compressed-gas storage is limited, such a system would likely allow only one or a couple of brief hops, and the combustion-rocket variant shown in the video is invite-only, with production talk pointing to around 2028.

hackernews · shekhar101 · Oct 16, 01:32 · [Discussion](https://news.ycombinator.com/item?id=50112657)

**Background**: A cold-gas thruster is a type of rocket engine that generates thrust purely from the expansion of a pressurized, typically inert gas, and is widely used on small satellites and CubeSats for attitude control because it is contaminant-free and avoids pyrotechnics. Rocket thrusters in general produce thrust by ejecting reaction mass, and the more powerful combustion variants burn fuel and oxidizer to accelerate exhaust through a nozzle. Tesla's Roadster announcement borrows these spacecraft concepts and applies them to a road car, while the company's sales model asks buyers for substantial deposits years before delivery.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cold_gas_thruster">Cold gas thruster</a></li>
<li><a href="https://www.explainx.ai/blog/tesla-flying-roadster-cold-gas-thrusters-how-it-works-what-was-shown-2026">Tesla's Flying Roadster: What Was Shown, How Cold-Gas ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_engine">Rocket engine - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were split: many found the flying demo genuinely wild and impressive, while others argued that rigging RCS-style thrusters onto a heavy object is well-understood and hardly 'incredible'. A recurring criticism targeted Tesla's deposit-based financing, with one user calling it years of interest-free loans for a car that may never ship, and others questioned the engineering constraints of vertical hops, limited compressed-gas supply, and the safety implications of putting rocket propulsion in consumer hands.

**Tags**: `#Tesla`, `#electric vehicles`, `#engineering`, `#rocket propulsion`, `#industry news`

---

<a id="item-2"></a>
## [Claude reverse-engineers the origins of NIST ECDSA curve seeds](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 8.0/10

Anthropic's Claude reverse-engineered the long-unknown provenance of the seed values behind the NIST P-192, P-224, P-256, P-384 and P-521 ECDSA curves, determining in under half an hour that they were outputs of the C library's lrand48 random-number generator seeded with a Unix timestamp. This contradicts the long-standing assumption that the seeds were derived from a hash function such as SHA-1. The result settles a quarter-century-old "nothing up my sleeve" mystery about whether the NIST curves contain a hidden backdoor baked into their constants, which matters for every system that relies on ECDSA for TLS, SSH, code signing and cryptocurrencies. It is also a striking demonstration of an LLM performing novel, verifiable cryptographic research rather than just summarizing existing work. The key tell was that lrand48 returns 31-bit values, so the leading bit of each 32-bit word in the seeds is never set — matching the observed pattern where the first digit never exceeds 7. The fifth seed, for the binary curve B-163, remains unexplained by Claude's method, and one plausible explanation raised in discussion is that a digit was mistyped somewhere in the publication chain.

hackernews · ahlCVA · Oct 16, 18:55 · [Discussion](https://news.ycombinator.com/item?id=50122800)

**Background**: ECDSA (Elliptic Curve Digital Signature Algorithm) is a digital signature scheme built on elliptic-curve cryptography; it is widely used because it offers the same security level as RSA with much smaller keys. In 1999 NIST recommended a set of elliptic curves, later specified in FIPS 186, and published the seed values used to generate their parameters so that anyone could verify the curves were not deliberately chosen to contain a weakness — the "nothing up my sleeve" principle. Those seeds had never been traced back to a known generation method, leaving open the possibility of a hidden backdoor, which is why cryptographers have repeatedly tried to reverse-engineer them.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Elliptic-curves">NIST Elliptic-curves</a></li>
<li><a href="https://en.wikipedia.org/wiki/ECDSA">ECDSA</a></li>
<li><a href="https://pubs.opengroup.org/onlinepubs/7908799/xsh/lrand48.html">lrand 48</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed but not fully reassured: one skeptic (fidotron) pointed out that confirming the generation method says nothing about curve selection, since candidates generated over months could have been discarded, and it is still conceivable that the curves were chosen to have a specific property by searching over timestamps fed to the RNG. Others noted prior independent attempts at the same problem, highlighted the elegant 31-bit lrand48 insight as a promising hint to give the model, and suggested the unexplained B-163 seed may simply be a typo.

**Tags**: `#cryptography`, `#ECDSA`, `#NIST curves`, `#AI/LLM`, `#security research`

---

<a id="item-3"></a>
## [Jake Archibald benchmarks JPEG XL vs AVIF for web images](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) ⭐️ 8.0/10

Jake Archibald published a detailed, benchmark-driven comparison of JPEG XL and AVIF for real-world web use-cases, covering file sizes, encode/decode times, and encoder behavior across photos, screenshots, and illustrations. The article has sparked a 133-comment Hacker News discussion in which developers shared concrete ffmpeg conversion commands, analyzed why libjxl's maximum effort takes 9–46 seconds, and reported that better encoders can shrink lossless JXL files by 30–39%. Image bytes remain one of the largest contributors to web page weight, so choosing between JPEG XL and AVIF directly affects page load performance and bandwidth costs for virtually every site. Because both formats are supported unevenly across browsers, this kind of practical, benchmark-backed guidance helps developers decide what to actually ship today rather than what looks best in a spec sheet. libjxl's slowest setting produces files only 2–7% smaller for photos and about 25% smaller for screenshots and illustrations, yet takes 9–46 seconds — 50–180x longer than its default — because it runs an iterative evaluation-optimization loop over the Butteraugli perceptual error metric. Commenters note that AVIF's contour-following compression handles text and line art well by avoiding JPEG-style ringing, while JPEG XL's current encoders are considered immature, with alternative encoders cutting lossless file sizes substantially.

hackernews · farlight · Oct 16, 16:12 · [Discussion](https://news.ycombinator.com/item?id=50120224)

**Background**: JPEG XL is a royalty-free image format designed to outperform JPEG, PNG, GIF and WebP with better compression and progressive decoding, and it can losslessly recompress existing JPEG files. AVIF is an open, royalty-free format from the Alliance for Open Media that stores AV1-compressed still images inside a HEIF container, supporting HDR, 8/10/12-bit color, transparency and animation. Both aim to replace legacy web image formats, but they differ fundamentally: AVIF descends from a video codec and lacks features like progressive rendering, while JPEG XL was purpose-built for still images.

<details><summary>References</summary>
<ul>
<li><a href="https://jpegxl.info/">JPEG XL : Superior Image Compression</a></li>
<li><a href="https://en.wikipedia.org/wiki/AVIF">AVIF - Wikipedia</a></li>
<li><a href="https://cloudinary.com/blog/how_jpeg_xl_compares_to_other_image_codecs">How JPEG XL Compares to Other Image Codecs</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree that JPEG XL's potential is undermined by today's weak encoders, with one noting that a better encoder shrinks the article's lossless Firefox screenshot from 66.9kB to 40.7kB and the cat illustration from 255.3kB to 178kB. Others praise AVIF in production for screenshots and line art and share concrete ffmpeg recipes, including one that yields files over 10x smaller while preserving PNG transparency, while another thread dissects the Butteraugli optimization loop to explain libjxl's slow maximum-effort mode.

**Tags**: `#image-compression`, `#jpeg-xl`, `#avif`, `#web-performance`, `#image-formats`

---

<a id="item-4"></a>
## [Apple runs near-trillion-parameter Meta model on four Mac Studios via MLX](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 8.0/10

Apple Machine Learning Research published a post showing that Muse Spark Open, Meta's near-trillion-parameter open-weight model, can run on a cluster of four Mac Studios using the latest release of MLX and its distributed inference support. The setup generates over 36 tokens per second, which Apple notes is well above average human reading speed. It shows that frontier-class models no longer strictly require cloud infrastructure or data-center GPUs, since prosumer Apple silicon machines can be pooled to serve them locally with privacy intact. This strengthens Apple's positioning of Mac Studio and the MLX stack as a credible platform for local AI, and gives developers a concrete alternative to renting GPU capacity. Apple's benchmark numbers are measured at an 8,192-token context, and the company describes starting on a single Mac Studio with up to 512GB of unified memory before scaling out across multiple machines. Commenters point out that the headline comparison pits Meta's model at 4-bit quantization against Qwen at native BF16, a quantization mismatch that may flatter the results.

hackernews · antipaul · Oct 16, 13:43 · [Discussion](https://news.ycombinator.com/item?id=50118320)

**Background**: MLX is Apple's open-source array framework for machine learning, built specifically for Apple silicon and its unified memory architecture, which lets the CPU and GPU work on the same data without copying it between separate memory pools. Muse Spark Open is described by Meta as its most capable open-weight model to date and is optimized for agentic coding workflows, with nearly one trillion parameters. Distributed inference means splitting a model too large for any single machine across several networked computers so they compute jointly; Mac Studio is Apple's high-memory desktop aimed at professional workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MLX_(machine_learning_framework)">MLX (machine learning framework) - Wikipedia</a></li>
<li><a href="https://research.meta.ai/blog/muse-spark-open">Introducing Muse Spark Open, The Most Capable US Open‑Weight ...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters were largely skeptical: several criticized the benchmark as unfair because it compares a 4-bit Meta model against BF16 Qwen, and one noted that a single M5 Ultra with 256GiB already runs DeepSeek 4.1 Flash at roughly 45 tokens per second, making the cluster result less impressive. Others flagged that the 36 tokens/second figure was measured at only an 8,192-token context, which many consider too short for real workloads, while one commenter wryly observed that Meta spends billions training open weights and users then hand Apple $20,000 for the hardware.

**Tags**: `#MLX`, `#Apple`, `#local-LLM-inference`, `#distributed-inference`, `#Mac-Studio`

---

<a id="item-5"></a>
## [Mercor report: 90% of US work hours lack AI benchmark coverage](https://www.mercor.com/research/labor-index/benchmark-map/) ⭐️ 8.0/10

Mercor's Labor Index "benchmark map" research report argues that roughly 90% of American working hours are spent on tasks that have little or no coverage from existing AI benchmarks, making it hard to judge how good models really are at the work people actually do. The report maps occupational task data against the prompts used in current evaluations and highlights a systematic mismatch between what is tested and what is worked. If benchmark scores are the main signal used to claim progress toward automating work, this gap means those claims may be systematically biased toward a narrow slice of jobs, complicating deployment decisions, labor-impact forecasts, and public debate about which roles AI will replace. It also implies that the economic value of further AI progress may lie in domains that today's leaderboards do not measure at all. The report notes that even after controlling for AI-exposure, O*NET tasks from occupations with larger wage bills are significantly overrepresented among benchmark prompts, and it claims that widely used evaluations focus on a small set of high-value, white-collar tasks. Commenters push back that the study blurs "covered well" with "covered at all" — for instance, the social-work task "counsel parents with child rearing problems" is counted as well covered on the basis of just 13 prompts.

hackernews · speckx · Oct 16, 17:08 · [Discussion](https://news.ycombinator.com/item?id=50121179)

**Background**: O*NET is a widely used database maintained for the U.S. Department of Labor that decomposes occupations into detailed tasks, skills and knowledge requirements, which is why researchers use it as a common vocabulary for labour analysis. AI benchmarks are standardized test suites (such as exam-style question sets or coding tasks) used to compare models, but they are built around what is easy to measure rather than around the full distribution of paid work. Mercor is a company that recruits domain experts to generate training data and evaluations for frontier AI labs, so its Labor Index sits at the intersection of benchmark design and labour economics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.onetcenter.org/database.html">O * NET Database at O * NET Resource Center</a></li>
<li><a href="https://www.dol.gov/agencies/eta/onet">O * NET | U.S. Department of Labor</a></li>
<li><a href="https://www.mercor.com/">Mercor | Organizing human intelligence to power the AI economy</a></li>

</ul>
</details>

**Discussion**: Commenters broadly welcomed the framing but questioned the methodology: one reader invoked the Doorman Fallacy, noting that replacing a doorman with an automatic door ignores the other vital functions the doorman performed, while another argued that "covered well" is effectively being used as a synonym for "covered at all." Others observed that AI efforts seem concentrated on higher-wage jobs ("they want AI to take the good jobs") and cited Karpathy's claim that AI is realistically tackling only 2–5% of work today, with some debate over whether that narrow focus is deliberate or simply the current limit of the technology.

**Tags**: `#AI benchmarks`, `#labor economics`, `#AI evaluation`, `#future of work`, `#O*NET`

---

<a id="item-6"></a>
## [Big Fish: Exploiting a 37-Year-Old OpenBSD Kernel Bug](https://calif.io/research/big-fish) ⭐️ 8.0/10

A security researcher published "Big Fish," a writeup describing the discovery and exploitation of a 37-year-old kernel bug in OpenBSD, a flaw that survived decades in one of the most heavily audited codebases. The post prompted extensive discussion about whether automated tooling such as fuzzing or static analysis could realistically have found it. OpenBSD is widely regarded as one of the most security-focused and heavily audited Unix-like operating systems, so an exploitable bug that lingered for 37 years challenges assumptions about how much code review alone can guarantee. The finding is likely to fuel ongoing debate about the limits of fuzzing and static analysis for certain classes of kernel bugs. According to the Hacker News discussion, the same flaw was apparently fixed accidentally in NetBSD in August 1999 during a rewrite of that code rather than as a targeted security fix. Because the bug is 37 years old, it predates OpenBSD's 1995 fork from NetBSD and originates in the shared BSD code lineage.

hackernews · rs_rs_rs_rs_rs · Oct 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=50118977)

**Background**: OpenBSD is a security-focused, free Unix-like operating system created in 1995 by Theo de Raadt as a fork of NetBSD 1.0, which itself descends from the Berkeley Software Distribution (BSD). Its code is widely reused elsewhere: the pf firewall in Apple's macOS, Android's Bionic C standard library, LLVM's regular expression library and OpenSSH all trace back to OpenBSD. Kernel exploitation research typically goes beyond merely finding a bug, aiming to show that a flaw can be turned into a working attack primitive such as privilege escalation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD">OpenBSD</a></li>
<li><a href="https://grokipedia.com/page/OpenBSD">OpenBSD</a></li>

</ul>
</details>

**Discussion**: Commenters praised the writeup's "OpenBSD Release"-style visuals and joked about an upcoming theme song, while a more substantive thread pointed out that the bug had been fixed accidentally in NetBSD back in 1999. The central debate was whether fuzzing or static analysis could realistically have caught this class of bug, or whether it required a human reasoning about the exploit primitive.

**Tags**: `#security`, `#OpenBSD`, `#kernel`, `#vulnerability-research`, `#exploit-development`

---

<a id="item-7"></a>
## [StepFun Releases Step 5 Preview Agent Flagship Model](https://huggingface.co/stepfun-ai/Step-5-Preview) ⭐️ 8.0/10

StepFun (阶跃星辰) has published Step 5 Preview on Hugging Face, a flagship model built for agentic work that uses a sparse Mixture-of-Experts architecture with 600 billion total parameters and 27 billion activated parameters. It supports a context window of up to 1 million tokens and accepts text, image, and video inputs, and is distributed under the StepFun Model License 1.0. This is one of the largest flagship releases from a Chinese model lab, combining a 600B-parameter sparse MoE design with a 1M-token context — a combination that puts it in direct competition with frontier agent-oriented models from larger players. Because it is optimized for software engineering, long-horizon agent execution, and professional knowledge tasks (especially finance), it targets enterprises that want to run autonomous coding and analysis workflows on self-hosted infrastructure. The sparse MoE design means only 27B of the 600B parameters are activated per token, keeping inference costs far below what a dense model of comparable size would require. StepFun says the model can be served through an OpenAI-compatible API using vLLM or SGLang, and it is released under a custom proprietary license rather than a fully open-source one.

telegram · zaihuapd · Oct 16, 06:36

**Background**: Mixture-of-Experts (MoE) is a model architecture that splits a network into many specialized sub-networks, or "experts", and routes each token to only a few of them; the sparse variant keeps total parameter count high while keeping per-token compute low, which is why labs can train very large models that remain affordable to serve. vLLM and SGLang are popular open-source inference engines that handle the batching, memory management, and KV-cache reuse needed to serve such models efficiently. A 1M-token context window lets a model ingest very long inputs — roughly hundreds of pages of text or an entire codebase — in a single request, though raw window size does not guarantee the model actually reasons well over all of it.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://github.com/vllm-project/vllm">vllm -project/ vllm : A high-throughput and memory-efficient inference ...</a></li>
<li><a href="https://benchlm.ai/best/large-context-window">Best Large Context LLMs (October 2026): 1M+ Windows Ranked</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#MoE`, `#AI agents`, `#multimodal`, `#model release`

---