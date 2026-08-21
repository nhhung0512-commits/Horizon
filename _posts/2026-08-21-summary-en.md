---
layout: default
title: "Horizon Summary: 2026-08-21 (EN)"
date: 2026-08-21
lang: en
---

> From 39 items, 7 important content pieces were selected

---

1. [Cobalt opens Kobo e-readers to third-party apps](#item-1) ⭐️ 8.0/10
2. [Accidental e164.arpa Logging Exposes Military Call Metadata](#item-2) ⭐️ 8.0/10
3. [US Citizen Faces Felony Charges for Deleting Phone Data at Border](#item-3) ⭐️ 8.0/10
4. [ChatGPT search now uses site: operator at scale](#item-4) ⭐️ 8.0/10
5. [Are Open Models Catching Up with Frontier AI?](#item-5) ⭐️ 8.0/10
6. [Apple Reportedly Ends Vision Pro Development Due to Weak Sales](#item-6) ⭐️ 8.0/10
7. [Anthropic's Project Panama scanned millions of books to train Claude](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cobalt opens Kobo e-readers to third-party apps](https://bandarlabs.github.io/Cobalt/) ⭐️ 8.0/10

Cobalt is a new open-source app platform for Kobo e-readers, offering a launcher, a signed App Store, a Rust SDK, and a capability-isolated runtime. It enables custom apps to be installed via USB once and then delivered over Wi-Fi. This significantly expands what Kobo owners can do with their devices, moving beyond stock firmware and existing hacks like NickelMenu. It creates a foundation for developers to build purpose-built apps for e-ink reading, annotation, and syncing, potentially revitalizing the Kobo ecosystem. Cobalt is currently tested only on the Kobo Clara BW N365 (device code 391) and is not affiliated with Rakuten Kobo. Hardware limitations apply; for example, color display models like the Clara Colour appear to be blocked from running Cobalt.

hackernews · thepoet · Aug 21, 16:25 · [Discussion](https://news.ycombinator.com/item?id=49390427)

**Background**: Kobo e-readers run a Linux-based operating system called Nickel. Existing community tools like NickelMenu add custom menu entries but do not provide a full app runtime. Cobalt aims to fill that gap by providing a safe, sandboxed environment with an SDK, though the limited hardware of e-ink devices remains a constraint.

<details><summary>References</summary>
<ul>
<li><a href="https://bandarlabs.github.io/Cobalt/">Cobalt: apps and an SDK for Kobo e-readers</a></li>
<li><a href="https://github.com/BandarLabs/Cobalt">GitHub - BandarLabs/Cobalt: An SDK for building real apps for your Kobo eInk reader · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=49390427">Kobo can run apps now | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed Cobalt, with some noting existing alternatives like NickelMenu and even PostmarketOS on Kobo hardware. There is enthusiasm for writing custom apps to manage highlights and quotes, but concern was raised that color Kobo models like the Clara Colour are not supported; one user wished for a Libby client.

**Tags**: `#Kobo`, `#e-reader`, `#open-source`, `#custom apps`, `#hacking`

---

<a id="item-2"></a>
## [Accidental e164.arpa Logging Exposes Military Call Metadata](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

An author accidentally logged hundreds of thousands of telephone call metadata records destined for military bases by observing DNS queries on the supposedly dead e164.arpa ENUM infrastructure. The findings reveal that the infrastructure is still receiving live queries and leaking sensitive information. This exposes a serious privacy and security gap in global telephony infrastructure, affecting military personnel and organizations that rely on ENUM. It also shows that neglected internet protocols can continue to leak sensitive call metadata for years. The author apparently controlled a nameserver that received NAPTR queries for numbers under e164.arpa, logging hundreds of thousands of records before handing the data to authorities. Commenters note that e164.arpa is not completely dead—it is still used privately for number-porting information.

hackernews · gavide · Aug 21, 13:11 · [Discussion](https://news.ycombinator.com/item?id=49387570)

**Background**: ENUM (E.164 Number Mapping) is an IETF-standardized protocol (RFC 6116) that translates E.164 telephone numbers into DNS names under the e164.arpa domain, allowing IP-based services to interact with the traditional phone network. Although ENUM was designed to unify telephony with the internet, it never saw widespread public adoption and is often considered dead, but private services still use it for number portability and routing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telephone_number_mapping">Telephone number mapping - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/wg/enum/about/">Telephone Number Mapping (enum) - Internet Engineering Task Force</a></li>
<li><a href="https://en.wikipedia.org/wiki/E.164">E.164 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were surprised the author wasn't jailed for reporting the issue, and some pointed out that e164.arpa is still alive in private number-porting services. Others expressed interest in further testing (e.g., setting up a SIP server) and noted that such holes can persist unnoticed for years until someone stumbles upon them.

**Tags**: `#security`, `#DNS`, `#telephony`, `#privacy`, `#ENUM`

---

<a id="item-3"></a>
## [US Citizen Faces Felony Charges for Deleting Phone Data at Border](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) ⭐️ 8.0/10

A U.S. citizen, Samuel Tunick, faces felony charges for deleting data on his phone during a border inspection. The case could set a legal precedent on whether deleting data during a border search is a crime. The outcome of this case may determine whether travelers can protect their digital data at the border without facing criminal prosecution. It raises critical questions about the balance between border security and privacy rights. The charges reportedly stem from Tunick deleting data during a border examination. It remains unknown whether the deletion was seen as obstruction of justice or destruction of evidence, and the case has not yet reached a verdict.

hackernews · floathub · Aug 21, 12:10 · [Discussion](https://news.ycombinator.com/item?id=49386895)

**Background**: U.S. border agents have historically claimed broad authority to search electronic devices without a warrant, citing national security. Courts have given mixed rulings on the limits of these searches, particularly regarding device encryption and cloud data. Legal scholars and civil liberties groups argue that Fifth Amendment protections may apply, since revealing or deleting data could be seen as compelled self-incrimination. This case adds a new dimension by charging a citizen after the fact for deleting their own data.

**Discussion**: Comments focus on technical countermeasures, such as creating encrypted device images, using automated factory-reset triggers, or carrying burner phones to minimize data exposure. Some commenters expressed deep pessimism about U.S. civil liberties, comparing the situation to historical surveillance states, while others offered practical advice and warned about the legal risks of such actions.

**Tags**: `#privacy`, `#border search`, `#digital rights`, `#surveillance`, `#law`

---

<a id="item-4"></a>
## [ChatGPT search now uses site: operator at scale](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/) ⭐️ 8.0/10

Data from Promptwatch shows the share of ChatGPT Search fanout queries containing the site: operator jumped from 0.3–0.5% to 16–17% on August 8, coinciding with the GPT-5.6 rollout. A follow-up on August 18 reports ChatGPT has greatly reduced the likelihood of Reddit being used in those searches. This is a significant, observable shift in ChatGPT's search behavior that affects SEO/GEO, web traffic, and content discoverability. It shows that changes in AI search design can be tracked via aggregate prompt data, giving site owners and marketers new signals for optimization. The figures only reflect prompts that Promptwatch has automated tracking for, not all ChatGPT users. Simon Willison suspects OpenAI's search tool now has a shape like search(query, recency, domains) rather than encouraging the site: operator directly, while OpenAI's August 6 announcement was vague.

rss · Simon Willison · Aug 20, 23:57

**Background**: Generative Engine Optimization (GEO) is the practice of structuring content to improve visibility in AI-generated answers, similar to SEO for chatbots. Promptwatch tracks responses to prompts across ChatGPT, Claude, and Gemini, publishing aggregate data. A fanout query is an AI search technique that splits a user query into multiple sub-queries to gather information, and the site: operator restricts search results to a specific domain. These concepts help explain why a jump in site: usage matters for how sites get cited in AI search.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_engine_optimization">Generative engine optimization</a></li>
<li><a href="https://promptwatch.com/">Promptwatch | #1 AI Search Visibility & GEO Platform</a></li>
<li><a href="https://www.semrush.com/blog/query-fan-out/">What Is Query Fan - Out & Why Does It Matter?</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#AI Search`, `#SEO`, `#GEO`, `#Simon Willison`

---

<a id="item-5"></a>
## [Are Open Models Catching Up with Frontier AI?](https://newsletter.semianalysis.com/p/are-open-models-catching-up) ⭐️ 8.0/10

SemiAnalysis published a detailed analysis investigating whether open-weights AI models are closing the capability gap with closed frontier models, and how that gap has evolved across successive eras of frontier model development. This analysis matters because it provides an evidence-based look at one of the AI industry's most consequential debates: whether open-source models can match the performance of proprietary frontier models. The outcome shapes decisions made by researchers, enterprises, and policymakers about where to invest in AI development. The article is published on the SemiAnalysis newsletter and frames the comparison across different 'eras' of frontier models rather than as a single snapshot. Its high reader score suggests the analysis is considered substantive and timely by the AI community.

rss · Semianalysis · Aug 21, 16:40

**Background**: Frontier models are the most advanced general-purpose AI systems, typically defined by being at or near the boundary of capability, scale, or risk. Open-weight models, in contrast, publicly release the trained parameters of a model so anyone can download and use them, though modification and redistribution rights depend on the license. This distinction is central to the open-vs-closed debate, because open releases enable reproducibility, customization, and local deployment, while closed models are optimized for commercial performance and safety control.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#machine learning`, `#frontier models`, `#analysis`

---

<a id="item-6"></a>
## [Apple Reportedly Ends Vision Pro Development Due to Weak Sales](https://t.me/zaihuapd/43301) ⭐️ 8.0/10

Apple has reportedly stopped further development of its Vision Pro product line. The planned lower-cost 'Vision Air' model, originally slated for 2027, has also been shelved, with the team reportedly shifting focus to AR glasses. This marks a major setback for Apple's spatial computing ambitions and suggests the current high-priced XR headset form factor is still struggling to gain mainstream adoption. It could also reshape competitive dynamics in the XR market, benefiting rivals like Meta and Samsung that offer more affordable alternatives. The Vision Pro launched at $3,500, and while an M5 chip upgrade arrived in October 2025, the device reportedly suffered from high return rates, excessive weight, and a lack of killer apps. Samsung introduced its competing Galaxy XR headset at $1,800 late last year.

telegram · zaihuapd · Aug 21, 01:32

**Background**: Apple Vision Pro is a mixed-reality headset announced at WWDC in June 2023 and released in 2024, marketed by Apple as a 'spatial computer' that integrates digital media with the real world. It runs visionOS and relies on eye tracking, hand gestures, and speech recognition for input. Such devices fall under extended reality (XR), an umbrella term covering AR, VR, and mixed reality, as well as the broader concept of spatial computing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Vision_Pro">Apple Vision Pro</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spatial_computing">Spatial computing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Extended_reality">Extended reality</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Vision Pro`, `#AR/VR`, `#Hardware`, `#Product Strategy`

---

<a id="item-7"></a>
## [Anthropic's Project Panama scanned millions of books to train Claude](https://t.me/zaihuapd/43305) ⭐️ 8.0/10

The Washington Post reported that Anthropic ran a covert 2024 program called Project Panama, destructively scanning millions of physical books — spending tens of millions of dollars — to train its Claude models. Court filings in a class-action lawsuit by authors also allege Anthropic downloaded pirated data from the LibGen shadow library. This is significant because it tests whether using copyrighted books — even destructively scanned or obtained from pirate libraries — to train AI counts as fair use. The outcome could reshape how AI companies collect training data and how publishers and authors are compensated or protected in the generative-AI era. Project Panama reportedly started in early 2024 and focused on older books not widely available online, with internal documents emphasizing that Anthropic did not want outsiders to know about the operation. A judge has suggested that scanning for training could qualify as fair use, but obtaining data via LibGen may still be infringing, and the class-action filings highlight this as a central legal risk.

telegram · zaihuapd · Aug 21, 04:52

**Background**: LibGen (Library Genesis) is a 'shadow library' that gives free access to scholarly articles and books that are otherwise paywalled or hard to find, but it has long faced copyright disputes and lawsuits from publishers. Shadow libraries are online repositories that host or link to pirated content. Anthropic is the AI company behind Claude, and this report concerns the copyrighted books used to train its models. The fair-use doctrine can allow limited use of copyrighted material without permission, which is central to the legal debate around AI training data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibtimes.co.uk/anthropic-secret-book-scanning-operation-1811155">Inside Project Panama , Anthropic 's Secret Effort To... | IBTimes UK</a></li>
<li><a href="https://www.yahoo.com/news/us/articles/project-panama-anthropic-secretly-destroyed-140251488.html">Project Panama : How Anthropic secretly destroyed millions of books...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Library_Genesis">Library Genesis - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#copyright`, `#training data`, `#legal`

---