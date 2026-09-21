---
layout: default
title: "Horizon Summary: 2026-09-21 (EN)"
date: 2026-09-21
lang: en
---

> From 35 items, 5 important content pieces were selected

---

1. [Apple unveils 2nm M6 and quad-die M5 Ultra chips for Mac mini and Mac Studio](#item-1) ⭐️ 9.0/10
2. [NASA's Mars Sample Return mission effectively cancelled](#item-2) ⭐️ 8.0/10
3. [Bryan Cantrill's Post-Mortem of Sun Microsystems' Strategic Failures](#item-3) ⭐️ 8.0/10
4. [Cloudflare Python Workers reach general availability after two-year preview](#item-4) ⭐️ 8.0/10
5. [SemiAnalysis Analyzes Computation and Data Movement for MoE Inference](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Apple unveils 2nm M6 and quad-die M5 Ultra chips for Mac mini and Mac Studio](https://t.me/zaihuapd/43965) ⭐️ 9.0/10

Apple announced two new Apple Silicon chips: the M6, its first chip built on a 2nm process, debuting in a new Mac mini with a 12-core CPU, 12-core GPU, dual 16-core Neural Engines and up to 170GB/s of unified memory bandwidth, and the M5 Ultra, debuting in a new Mac Studio as the first four-die M-series chip with up to a 36-core CPU, 80-core GPU, 512GB of memory and 1.2TB/s of memory bandwidth. The M6 makes Apple one of the first vendors to ship a consumer chip on the 2nm node, which should translate into meaningfully better performance-per-watt and denser transistor budgets across the Mac lineup, while the four-die M5 Ultra pushes Apple Silicon into workstation-class territory with memory capacity and bandwidth previously reserved for high-end GPUs and server chips — a direct play for local AI and heavy creative workloads. The M5 Ultra's four dies reportedly communicate over ultra-low-latency links with more than 4.4TB/s of aggregate inter-die bandwidth and behave as a single unified processor, and its 1.2TB/s memory bandwidth is 50% higher than the M3 Ultra's; as with all modern node names, "2nm" is a marketing label rather than a measurement of any actual physical feature size.

telegram · zaihuapd · Sep 21, 16:32

**Background**: Apple Silicon's M-series chips are system-on-a-chip designs that integrate CPU, GPU and unified memory on a single package; the Neural Engine is Apple's dedicated AI accelerator, first introduced in the 2017 A11 Bionic and now a standard block in both iPhone and Mac chips. Process nodes such as 3nm and 2nm describe successive generations of semiconductor manufacturing, where smaller nodes generally allow higher transistor density, faster switching and lower power consumption. "Ultra" chips in Apple's lineup are built by joining two Max dies together, so a four-die design doubles that approach again, using advanced packaging — the same chiplet-style strategy AMD and Intel use to scale past the reticle limit of a single piece of silicon.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcmag.com/news/apple-m5-ultra-and-m6-silicon-explained">Forget Foldables: Apple's 2nm M6 and Quad-Die Monster Just Reset the AI Race | PCMag</a></li>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_Engine">Neural Engine - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#M6`, `#M5 Ultra`, `#2nm`, `#Apple Silicon`

---

<a id="item-2"></a>
## [NASA's Mars Sample Return mission effectively cancelled](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) ⭐️ 8.0/10

NASA's Mars Sample Return (MSR) campaign — a joint NASA–ESA effort to retrieve samples cached on Mars by the Perseverance rover — has been effectively cancelled, according to a Science report. The program, which had ballooned to roughly $11 billion and slipped to a 2040 sample-return date, is now dead rather than merely delayed. MSR was widely regarded as the top-priority planetary science goal of the decade, and its cancellation removes the first planned round-trip to another planet's surface, leaving a strategic opening for China's Tianwen-3 sample-return attempt. It also raises questions about the future of JPL and NASA's ability to execute flagship-class robotic missions within budget. The NASA–ESA plan approved in 2022 involved three elements: Perseverance as the sample collector, a Sample Retrieval Lander carrying a Mars Ascent Vehicle, and an Earth Return Orbiter, targeting samples back around 2033 before slipping to the 2040s. Critics in the community argue JPL designed the architecture around legacy launch vehicles such as Ariane 64 rather than cheaper, higher-capacity commercial options like Starship or New Glenn.

hackernews · Muhammad523 · Sep 21, 19:14 · [Discussion](https://news.ycombinator.com/item?id=49791939)

**Background**: A Mars sample-return mission would bring Martian rock and dust to Earth so that laboratories here can analyze them with far greater precision than any rover-mounted instrument, primarily to determine whether Mars ever hosted life. NASA's Perseverance rover has been drilling and sealing pencil-sized titanium sample tubes in Jezero Crater since 2021, leaving them on the surface for a future mission to collect. Getting samples from Mars requires an unprecedented chain of steps — landing, launching a rocket off another planet, and rendezvousing in Mars orbit — which is what drove the cost and schedule growth.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NASA-ESA_Mars_Sample_Return">NASA-ESA Mars Sample Return - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mars_sample-return_mission">Mars sample-return mission - Wikipedia</a></li>
<li><a href="https://www.globaltimes.cn/page/202609/1369763.shtml">Tianwen - 3 mission enters prototype phase, prioritizing... - Global Times</a></li>

</ul>
</details>

**Discussion**: Commenters largely blamed JPL leadership, citing the jump to $11 billion and a 2040 return date, and contrasted the 1.1 pounds of planned Martian samples with the 842 pounds Apollo brought back from the Moon, arguing it may be better to wait for crewed missions. One commenter who worked on the ExoMars Rosalind Franklin rover noted how repeatedly delayed that mission has been, while others highlighted China's Tianwen-3 sample-return effort launching in 2028 and questioned why Perseverance was made to cache samples for an underdefined follow-up mission.

**Tags**: `#space-exploration`, `#NASA`, `#Mars`, `#JPL`, `#space-policy`

---

<a id="item-3"></a>
## [Bryan Cantrill's Post-Mortem of Sun Microsystems' Strategic Failures](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 8.0/10

Bryan Cantrill, a former Sun Microsystems engineer best known as a co-creator of DTrace, published an essay titled "What Sun got wrong" on his dtrace.org blog, dissecting the strategic and technical decisions that led to Sun's decline. The post drew 469 points and roughly 260 substantive comments on Hacker News, with readers adding firsthand accounts of Sun's sales culture, the 2002 cancellation of Solaris on x86, and a failed deal with Google. Sun's collapse reshaped the computing industry — it cleared the way for x86 and Linux to dominate servers, ended one of the last vertically integrated Unix hardware vendors, and set up Oracle's 2010 acquisition of Solaris and SPARC. Cantrill's analysis is a widely cited case study in how technical excellence alone cannot sustain a business, a lesson that resonates with today's AI hardware and infrastructure vendors facing similar lock-in-versus-openness trade-offs. The discussion adds concrete specifics: commenters note that Sun's sales process forced buyers into live meetings and endless quote revisions, so that rails and power cords for an Alpha server could cost more than a complete Dell server delivered next-day. Others point to Sun's brief 2002 cancellation of Solaris on x86, which damaged trust among customers unwilling to be locked into SPARC, and a failed 2002 Google deal reportedly scuttled because Sun insisted on knowing how many servers Google operated.

hackernews · chmaynard · Sep 21, 14:03 · [Discussion](https://news.ycombinator.com/item?id=49787436)

**Background**: Sun Microsystems built the SPARC reduced instruction set computer (RISC) architecture and the Solaris Unix operating system, which introduced influential technologies such as DTrace and ZFS. Sun open-sourced most of Solaris in 2005 as the OpenSolaris project, but after Oracle acquired the company in 2010 the operating system was renamed Oracle Solaris, the OpenSolaris distribution was discontinued, and Oracle later laid off most of the Solaris teams in 2017; OpenSolaris lived on as the Illumos fork. Bryan Cantrill is a systems engineer who worked at Sun and later at Joyent, and is known for DTrace, an observability tool still used across Unix-like systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SPARC">SPARC - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Solaris_operating_system">Solaris operating system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Oracle_Solaris">Oracle Solaris - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with Cantrill and supply their own war stories: coreyh14444 describes the painful, quote-revision-heavy buying experience at Sun and DEC compared with Dell's next-day delivery, while cryptonector enumerates Sun's 2000s mistakes, including the brief 2002 cancellation of Solaris on x86 and the botched Google deal. jedberg pushes back on Cantrill's framing by arguing Sun was never interested in running a business and cared only about building great technology, and labrador draws a cautionary parallel between selling Sun stock at $70 before its slide to $7 and today's extremely high valuations for Tesla, SpaceX and AI stocks.

**Tags**: `#Sun Microsystems`, `#Solaris`, `#SPARC`, `#tech history`, `#Bryan Cantrill`

---

<a id="item-4"></a>
## [Cloudflare Python Workers reach general availability after two-year preview](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 8.0/10

Cloudflare announced that Python Workers are now generally available, making Python a first-class, fully supported language on the Cloudflare Developer Platform after roughly two years in preview. The implementation runs Python compiled to WebAssembly via Pyodide inside Cloudflare's V8-based workerd runtime, rather than using a native CPython interpreter. Serverless Python on the edge has long lagged behind JavaScript and TypeScript on Cloudflare's platform, so GA status signals that Python developers can now build production workloads on Workers with vendor support. It also reflects Cloudflare's broader investment in the Python and Pyodide ecosystems, since two of the three people credited on the release announcement are Pyodide core maintainers. The WebAssembly-based runtime comes with documented limitations, most notably that both multiprocessing and threading do not function inside the WebAssembly VM. Local development is handled by the pywrangler tool (published on PyPI under the easily confused name workers-py), which simulates the full stack locally by running Pyodide in WebAssembly inside V8 within a 123MB workerd binary, typically installed under node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd on macOS.

rss · Simon Willison · Sep 21, 22:25

**Background**: Cloudflare Workers is a serverless platform for running code on Cloudflare's edge network; its runtime, workerd, is a JavaScript and WebAssembly engine that was open-sourced in 2022 and is also used by Wrangler for local development. Pyodide is a project that compiles CPython and many scientific Python packages to WebAssembly so they can run in environments that do not provide a native Python interpreter, originally aimed at the browser. WebAssembly is a portable binary instruction format that lets languages other than JavaScript run in JavaScript virtual machines, which is what makes this approach possible.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Workerd">Workerd</a></li>
<li><a href="https://flaviocopes.com/workerd/">How workerd , the Cloudflare Workers runtime, is built</a></li>
<li><a href="https://pyodide.org/en/stable/usage/downloading-and-deploying.html">Downloading and deploying Pyodide — Version 314.0.7</a></li>

</ul>
</details>

**Tags**: `#Cloudflare Workers`, `#Python`, `#WebAssembly`, `#Pyodide`, `#Serverless`

---

<a id="item-5"></a>
## [SemiAnalysis Analyzes Computation and Data Movement for MoE Inference](https://newsletter.semianalysis.com/p/computation-and-data-movement-for) ⭐️ 8.0/10

SemiAnalysis published a deep technical analysis of how Mixture-of-Experts (MoE) models are mapped onto inference hardware, focusing on model structure, data flow, and efficient serving. The piece frames inference of sparse expert models as primarily a data-movement problem rather than a raw compute problem. MoE has become the dominant architecture for frontier large language models because it decouples total parameter count from the compute spent per token, so the industry's cost, latency, and throughput increasingly depend on how well these models can be served. Infrastructure and ML systems engineers building or buying inference stacks need this level of hardware-aware analysis to make sensible decisions. MoE inference is typically constrained by memory bandwidth and interconnect rather than peak FLOPs, since expert weights must be gathered and scattered across devices, and techniques such as expert parallelism involve heavy all-to-all communication. Practical complications include routing imbalance across experts, small per-expert batch sizes that underutilize tensor cores, and the trade-off between keeping experts in high-bandwidth memory versus moving them over slower links.

rss · Semianalysis · Sep 21, 18:14

**Background**: Mixture-of-Experts is a machine learning approach that splits a model into multiple "expert" sub-networks, each specializing in a subset of the input, with a router selecting only a few experts per token. Because only a fraction of parameters are activated for any given input, MoE models can be pre-trained with far less compute and can scale to enormous total parameter counts while keeping per-token cost roughly constant. Model serving, meanwhile, is the infrastructure practice of deploying trained models for low-latency, high-availability inference at scale. This article sits at the intersection of the two: how the sparsity that makes MoE cheap to train translates into very specific computation and data-movement patterns on real inference hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://inferenceengineering.tech/learn/ai-inference-hardware/">AI Inference Hardware Guide</a></li>

</ul>
</details>

**Tags**: `#Mixture-of-Experts`, `#Inference`, `#AI Hardware`, `#Model Serving`, `#Systems`

---