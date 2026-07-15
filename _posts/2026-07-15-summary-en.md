---
layout: default
title: "Horizon Summary: 2026-07-15 (EN)"
date: 2026-07-15
lang: en
---

> From 36 items, 9 important content pieces were selected

---

1. [Stripe and Advent Jointly Offer to Buy PayPal for $53B](#item-1) ⭐️ 9.0/10
2. [DeepSeek Raises $74 Billion, Maintains Founder Control via Special Structure](#item-2) ⭐️ 9.0/10
3. [Telegram Launches Serverless Platform for Bots and Mini Apps](#item-3) ⭐️ 8.0/10
4. [Claude web_fetch flaw enables data exfiltration attack](#item-4) ⭐️ 8.0/10
5. [New Method Disentangles Convolutional Neurons in InceptionV1](#item-5) ⭐️ 8.0/10
6. [PyTorch model 170x slower on T4 vs A100: extreme bottleneck](#item-6) ⭐️ 8.0/10
7. [DeepSeek Plans IPO, Seeks New Funding at $710B Valuation](#item-7) ⭐️ 8.0/10
8. [Judge Questions Epic's $800M Deal with Google in Antitrust Case](#item-8) ⭐️ 8.0/10
9. [Sandbox Escape Lets Filza Access iOS 27 Notes Database](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe and Advent Jointly Offer to Buy PayPal for $53B](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

Stripe and private equity firm Advent International have made a joint offer to acquire PayPal for over $53 billion, according to sources. This acquisition would consolidate major payment processors, potentially reducing competition and raising concerns about higher fees and restrictive policies for merchants. The deal would bring together Stripe, PayPal, Venmo, Braintree, and Xoom under one umbrella, leading to a very high Herfindahl-Hirschman Index for online card-not-present checkout.

hackernews · rvz · Jul 15, 03:32 · [Discussion](https://news.ycombinator.com/item?id=48915953)

**Background**: Stripe is a leading online payment processor, while PayPal is a long-established digital payments company. Advent International is a global private equity firm. The combination raises significant antitrust concerns due to market concentration.

**Discussion**: Commenters express concerns about reduced competition, potential fee increases, and restrictive policies by Stripe, especially for cannabis and adult businesses. Some users worry about account flagging risks and suggest unwinding Venmo and Braintree to pass antitrust scrutiny.

**Tags**: `#fintech`, `#acquisition`, `#payments`, `#antitrust`

---

<a id="item-2"></a>
## [DeepSeek Raises $74 Billion, Maintains Founder Control via Special Structure](https://t.me/zaihuapd/42589) ⭐️ 9.0/10

DeepSeek completed its first financing round, raising over 500 billion yuan (approximately $74 billion), using an unconventional structure where investors invest in a limited partnership controlled by CEO Liang Wenfeng, accepting a five-year lock-up without voting rights. This massive funding round signals strong investor confidence in DeepSeek and the AI sector, while the special structure ensures founder control, which could influence how other AI labs approach fundraising and governance. Founder Liang Wenfeng personally invested 20 billion yuan, while Tencent and CATL are considering or planning investments of 10 billion and 5 billion yuan respectively, potentially becoming the largest external investors. DeepSeek has not commented on the report.

telegram · zaihuapd · Jul 15, 12:56

**Background**: Limited partnership structures are commonly used in venture capital to separate control and economic rights. The general partner (GP) manages the partnership and retains voting power, while limited partners (LPs) contribute capital but have no management authority. In this case, investors are LPs in a partnership controlled by Liang Wenfeng, allowing him to maintain control over DeepSeek despite raising significant external capital.

<details><summary>References</summary>
<ul>
<li><a href="https://rbrf.xnai.edu.cn/__local/3/2C/1E/D04DD95BE51FEBBF23E8B5AFCD0_BDED923C_954AA.pdf">1 科创板公司“有限合伙”架构创新实践 及管理建议 摘要：2019 年7 月科创板开板以来，已有400 多家公司实</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/383462470">公司控制模式之三：有限合伙控制 - 知乎</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#DeepSeek`, `#venture capital`, `#corporate governance`

---

<a id="item-3"></a>
## [Telegram Launches Serverless Platform for Bots and Mini Apps](https://core.telegram.org/bots/serverless) ⭐️ 8.0/10

Telegram has officially launched a serverless platform that allows developers to deploy JavaScript backend code for bots and Mini Apps directly on Telegram's infrastructure using a single command: npx tgcloud push. This simplifies bot and Mini App development by eliminating server management, scaling concerns, and deployment complexity, potentially attracting millions of Telegram users to build more interactive services. The platform runs code in an isolated V8 sandbox close to the Bot API, and includes a built-in SQLite database. However, details on quotas (execution time, storage) and pricing have not been disclosed yet.

hackernews · soheilpro · Jul 15, 10:06 · [Discussion](https://news.ycombinator.com/item?id=48918534)

**Background**: Serverless computing allows developers to run code without managing servers, where the cloud provider handles scaling and maintenance. Telegram Mini Apps are web-based applications built with JavaScript and HTML5 that run inside Telegram, providing interactive experiences. Previously, developers had to host bot backends on their own servers or use third-party serverless providers like AWS Lambda.

<details><summary>References</summary>
<ul>
<li><a href="https://core.telegram.org/bots/serverless">Telegram Serverless</a></li>
<li><a href="https://core.telegram.org/bots/webapps">Telegram Mini Apps</a></li>
<li><a href="https://grokipedia.com/page/Telegram_Mini_Apps">Telegram Mini Apps</a></li>

</ul>
</details>

**Discussion**: Community members expressed interest but raised concerns about missing details: quotas for execution time and storage, secrets management for API keys, SQLite database size limits, and pricing. Some commented that the built-in SQLite is a nice touch, while others wished for similar features from other messaging platforms like Signal.

**Tags**: `#Telegram`, `#serverless`, `#bot development`, `#JavaScript`, `#deployment`

---

<a id="item-4"></a>
## [Claude web_fetch flaw enables data exfiltration attack](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Researcher Ayush Paul discovered a method to exploit Claude's web_fetch tool by using a honeypot site that tricks the AI into following nested links, leading to exfiltration of user's name, city, and employer. This demonstrates a critical flaw in AI tool design that bypasses Anthropic's protections against data exfiltration, highlighting ongoing risks in the "lethal trifecta" attack vector where private data, untrusted content, and tool access combine. The attack required the user to directly ask Claude to fetch a URL, and the attacker's site only displayed the malicious content to clients with 'Claude-User' in their user-agent. The loophole was that web_fetch was allowed to follow links embedded in previously fetched pages.

rss · Simon Willison · Jul 15, 14:21

**Background**: The "lethal trifecta" refers to three conditions that enable AI agent data theft: access to private data, exposure to untrusted content, and ability to communicate externally. Claude's web_fetch tool was designed to only navigate to exact user-provided URLs or search results to prevent exfiltration, but this design was circumvented.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cyera.com/research/when-language-becomes-the-attack-vector-the-lethal-trifecta-of-ai-agents">When Language Becomes the Attack Vector: The Lethal Trifecta of AI...</a></li>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#Claude`, `#prompt injection`, `#data exfiltration`, `#vulnerability`

---

<a id="item-5"></a>
## [New Method Disentangles Convolutional Neurons in InceptionV1](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 8.0/10

A researcher introduced a novel technique using the Hadamard product of a neuron's receptive field and its weights to cluster and visualize all patterns detected by a single convolutional neuron in InceptionV1, revealing monosemantic clusters for concepts like cars and cats, as well as low-valued clusters like letters. This work advances mechanistic interpretability by providing a finer-grained method to analyze convolutional neurons, potentially improving our understanding of how neural networks represent and combine features in vision models. The method clusters Hadamard products to yield both high-activation monosemantic clusters (e.g., cars, dogs) and low-activation clusters (e.g., letters). Analysis of low-valued clusters shows that downstream neurons also fire on the same concept, with positive and negative weights balanced to suppress the summed activation, suggesting deliberate noise injection by gradient descent.

reddit · r/MachineLearning · /u/narang_27 · Jul 15, 06:59

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks by understanding their internal circuits and features. InceptionV1 (GoogLeNet) is a classic convolutional neural network for image classification, often studied in interpretability research. The Hadamard product is an element-wise matrix multiplication; here it is used to combine the receptive field patch with the neuron's weight vector to isolate what the neuron is 'seeing'.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inception_(deep_learning_architecture)">Inception (deep learning architecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_product_(matrices)">Hadamard product (matrices) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#neural network interpretability`, `#InceptionV1`, `#neuron analysis`, `#convolutional networks`

---

<a id="item-6"></a>
## [PyTorch model 170x slower on T4 vs A100: extreme bottleneck](https://www.reddit.com/r/MachineLearning/comments/1ux6a9x/pytorch_model_running_170x_slower_on_t4_vs_a100/) ⭐️ 8.0/10

A user reports that a PyTorch point-tracking model using 4D correlation volumes and transformer layers runs approximately 170 times slower on an NVIDIA T4 GPU (85 seconds) compared to an A100 (0.5 seconds) for the same 47-frame video at 256x256 resolution, despite using FP32 precision and showing 99% GPU utilization on the T4. This extreme performance gap is far beyond typical hardware differences and points to a specific algorithmic or kernel-level bottleneck, likely related to the 4D correlation volume construction or memory access patterns on the T4's architecture. Understanding this issue can help ML engineers optimize similar models and avoid costly deployment mistakes. The user has already ruled out common issues: GPU utilization is 99%, the model is on GPU, and cudnn.benchmark had no effect. The model runs in pure FP32, which on the T4 means it cannot leverage Tensor Cores (available only in mixed precision), but this alone does not explain a 170x slowdown. The 4D correlation volume operation is memory-intensive and may suffer from poor memory coalescing on the T4's smaller memory bandwidth (300 GB/s vs 1555 GB/s on A100).

reddit · r/MachineLearning · /u/Future-Structure-296 · Jul 15, 13:44

**Background**: The NVIDIA T4 (Turing) GPU has a memory bandwidth of about 300 GB/s and relies on Tensor Cores only for mixed-precision operations, while the A100 (Ampere) offers 1555 GB/s bandwidth and much larger caches. 4D correlation volumes are a common technique in point-tracking models (e.g., TAPIR, LocoTrack) that involve dense matching between frames, creating large intermediate tensors. The combination of FP32 execution and memory-bound operations can disproportionately hurt performance on the T4.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.26087v1">MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation</a></li>
<li><a href="https://discuss.pytorch.org/t/how-to-calculate-the-gpu-memory-that-a-model-uses/157486">How to calculate the GPU memory that a model ... - PyTorch Forums</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#GPU Performance`, `#NVIDIA T4`, `#NVIDIA A100`, `#Model Optimization`

---

<a id="item-7"></a>
## [DeepSeek Plans IPO, Seeks New Funding at $710B Valuation](https://t.me/zaihuapd/42577) ⭐️ 8.0/10

DeepSeek has initiated preparations for an initial public offering (IPO) and aims to file as early as late 2025 or early 2026, targeting a listing in 2027. Simultaneously, it is seeking new private funding at a pre-money valuation of at least 710 billion USD (approximately 4800 billion RMB). This represents a major milestone for DeepSeek and signals strong market confidence in the AI sector, as the valuation has surged from about $50 billion in its first external funding round in June to over $710 billion. The IPO could become one of the largest tech listings in recent years. The company completed its first external funding round of $700 million in early June 2025, with investors including Tencent and CATL. The new funding round aims to raise at least 10 billion RMB, with the total possibly multiplying depending on investor interest. Discussions are ongoing and plans may adjust with market conditions.

telegram · zaihuapd · Jul 15, 07:04

**Background**: DeepSeek is a Chinese AI startup based in Hangzhou, focusing on large language models and AI applications. The company gained significant attention for its competitive models like DeepSeek-V2. An IPO would provide it with public market capital to scale operations and compete with global AI leaders.

**Tags**: `#DeepSeek`, `#IPO`, `#AI funding`, `#venture capital`, `#financing`

---

<a id="item-8"></a>
## [Judge Questions Epic's $800M Deal with Google in Antitrust Case](https://t.me/zaihuapd/42588) ⭐️ 8.0/10

Judge James Donato revealed in a hearing that Epic Games and Google have entered a new commercial cooperation, with Epic paying Google approximately $800 million over six years. The judge questioned whether this deal could conflict with Epic's push for Android ecosystem reforms in its antitrust lawsuit. This development is significant because it potentially undermines Epic's credibility in its antitrust case against Google, which has broader implications for mobile app store competition and developer fees. If the judge finds the deal compromises Epic's stance, it could weaken the case for forcing Google to open up its Android ecosystem. The cooperation involves joint product development, marketing, and partnerships relating to Unreal Engine, Fortnite, and Android-related businesses. Epic CEO Tim Sweeney stated that the agreement does not include terms for Epic Games Store distribution on Android.

telegram · zaihuapd · Jul 15, 11:15

**Background**: Epic Games sued Google in 2020, alleging that Google's Play Store policies and fees (30% commission) constitute an illegal monopoly. This case, similar to Epic's lawsuit against Apple, seeks to force Google to allow alternative app stores and payment systems. The recent commercial deal between Epic and Google has raised concerns that it might indicate a cozy relationship contrary to Epic's public stance.

**Tags**: `#antitrust`, `#Epic Games`, `#Google`, `#Android`, `#app store`

---

<a id="item-9"></a>
## [Sandbox Escape Lets Filza Access iOS 27 Notes Database](https://x.com/0xjohnny/status/2077216973256274272) ⭐️ 8.0/10

Developer johnny modified the Filza file manager to exploit a sandbox escape vulnerability on iOS 27 beta 3, allowing it to access the system's Notes database on an iPhone 17 Pro Max. This demonstrates a significant security flaw in a new iOS version, potentially exposing sensitive user data. It highlights ongoing challenges in iOS sandbox enforcement and could prompt Apple to patch the vulnerability before final release. The exploit was performed on iOS 27 beta 3 using a modified version of Filza, a popular file manager for jailbroken devices. The attack bypasses app container restrictions to read external data, specifically the Notes database.

telegram · zaihuapd · Jul 15, 14:35

**Background**: Filza is a file manager that provides full filesystem access on jailbroken iOS devices. Sandbox escape refers to breaking out of an app's restricted environment to access system data. Such vulnerabilities are critical as they can lead to data theft or malware installation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ios-repo-updates.com/repository/tigisoftware/package/com.tigisoftware.filza/">Package: Filza File Manager • com.tigisoftware....</a></li>
<li><a href="https://www.tigisoftware.com/default/?page_id=78">Filza – TIGI Software</a></li>
<li><a href="https://vulners.com/thn/THN:E828782CB52567D01CA178688A53E3A6">Microsoft Details App Sandbox Escape Bug Impacting Apple iOS .</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#iOS`, `#sandbox escape`, `#vulnerability`, `#mobile security`

---