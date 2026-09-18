---
layout: default
title: "Horizon Summary: 2026-09-18 (EN)"
date: 2026-09-18
lang: en
---

> From 41 items, 7 important content pieces were selected

---

1. [Dan Abramov uses AI to vibe and verify a Conway conjecture refinement](#item-1) ⭐️ 8.0/10
2. [ZCode silently uploaded users' Git history to the cloud](#item-2) ⭐️ 8.0/10
3. [South Korea raises data breach fines to 10% of revenue](#item-3) ⭐️ 8.0/10
4. [US Military Near-Miss After Acting on AI-Hallucinated Intelligence](#item-4) ⭐️ 8.0/10
5. [Rust Security Team Warns of Targeted Social-Engineering Attacks on Maintainers](#item-5) ⭐️ 8.0/10
6. [SemiAnalysis: Co-design for Efficient DRAM/SSD Offloading in LLM Inference](#item-6) ⭐️ 8.0/10
7. [Researchers: xAI Grok Build CLI uploads entire codebases and .env secrets by default](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Dan Abramov uses AI to vibe and verify a Conway conjecture refinement](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/) ⭐️ 8.0/10

Dan Abramov, best known as a core React developer, published the blog post "How I vibed a proof of Conway's conjecture" together with the gaearon/conway-refinement repository, documenting how he used AI assistance to develop and check a refinement of Conway's cosmological theorem. The post triggered a 194-point, 172-comment Hacker News discussion about what LLM-assisted mathematical work is actually worth. It is a concrete case study of a non-specialist using LLMs to push on a problem in formal mathematics, which raises pressing questions about how much a "vibed" proof can be trusted and who is responsible for verifying it. The discussion also previews a likely division of labor, in which AI generates candidate arguments while trained mathematicians supply the understanding, simplification, and validation. The result is described as a refinement of Conway's theorem rather than a field-changing breakthrough, and Abramov's own repository includes a section titled "why I think it's correct" that lays out his reasoning for trusting it. He also reports emailing mathematicians with proposed typo fixes and getting confirmation that at least some of them were genuine, an informal but notable sanity check on the AI-generated material.

hackernews · m-hodges · Sep 18, 14:36 · [Discussion](https://news.ycombinator.com/item?id=49755024)

**Background**: Conway's cosmological theorem concerns the look-and-say sequence, which starts 1, 11, 21, 1211, 111221…, where each term is produced by reading off the digits of the previous term in groups ("one 1" becomes 11, "two 1s" becomes 21). John Conway proved that any such sequence eventually decays into a compound of 94 "atomic elements" that never interact with their neighbors again. Formal verification means proving correctness against a precise mathematical specification, and proof assistants are interactive tools in which a human guides a machine-checkable proof. The post combines both ideas: an LLM proposes mathematics, and formal or informal checking is used to see whether it holds up.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conway's_cosmological_theorem">Conway's cosmological theorem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Look-and-say_sequence">Look-and-say sequence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant</a></li>

</ul>
</details>

**Discussion**: Sentiment is broadly encouraging but methodologically cautious: one self-described trained mathematician (pretzellogician) advises Abramov to keep simplifying the proof until he can follow it himself and to check whether parts of the argument are just copies of known results. gbjcantab draws a fantasy-flavored distinction between "wizardry" (deep understanding plus powerful tools) and "sorcery" (summoning and controlling entities you do not fully understand), while bwfan123 argues mathematicians capture the most value and offers an "LLM corollary" to the infinite monkey theorem. Other commenters recommend external learning resources, such as a prize-winning video introducing Hackenbush and the surreal numbers, showing the thread doubled as a genuine mathematics discussion.

**Tags**: `#ai-assisted-math`, `#formal-verification`, `#llms`, `#mathematics`, `#proof-assistants`

---

<a id="item-2"></a>
## [ZCode silently uploaded users' Git history to the cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) ⭐️ 8.0/10

ZCode, the AI coding development environment from Z.ai, was found to be silently uploading users' Git history to the cloud through its "codebase indexing" feature, prompting Z.ai to run an internal review and issue an official apology to affected users. The write-up and the company's response drew heavy attention from the developer community, with 234 points and 88 comments on Hacker News. This is a concrete case of an AI coding assistant exfiltrating source-code metadata without explicit consent, which undermines trust in tools that request broad filesystem and repository access by default. It also intensifies the broader industry debate over agent permissions, sandboxing, and whether telemetry in AI developer tools should be opt-in rather than on by default. According to Z.ai's statement, the upload originated from ZCode's codebase indexing feature, which is intended to give the assistant better context about a project; the incident response focused on apologizing and explaining rather than detailing exactly what files were transmitted or how long data was retained. Because a .git directory can contain full commit history, deleted secrets, and hard-coded credentials, silently exfiltrating it is considerably more sensitive than uploading ordinary source files.

hackernews · csmantle · Sep 18, 06:11 · [Discussion](https://news.ycombinator.com/item?id=49750694)

**Background**: ZCode is a desktop AI coding environment built by Z.ai around its GLM model family, positioned as a competitor to tools like Claude Code and Codex that run AI agents with direct access to a developer's local files. Such tools typically scan or index a project so the model can retrieve relevant code as context, and that indexing is usually presented as a local operation. Git is the near-universal version-control system for source code, and its hidden .git folder stores the entire history of a repository, which is why uploading it can leak far more than the current working files.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Z.ai">Z.ai - Wikipedia</a></li>
<li><a href="https://zcode.z.ai/en">ZCode | Official Harness for GLM-5.3</a></li>
<li><a href="https://www.cerbos.dev/blog/permission-management-for-ai-agents">Access Control and Permission Management for AI Agents: Building With Security in Mind | Cerbos</a></li>

</ul>
</details>

**Discussion**: Commenters largely treated the incident as a symptom of a structural problem rather than an isolated bug: several argued it is naive to assume an agent will not touch anything on your disk, and that "permission classifiers" in auto mode are just models guessing whether their own actions are acceptable, making sandboxes somewhat circular. Others reported unrelated concerns such as Windows Defender repeatedly requesting to upload Codex working files, said they stick with OpenCode because its incentives discourage file vacuuming and token inflation, and noted that GLM and DeepSeek models are unusually fond of reading dotfiles and files listed in .gitignore.

**Tags**: `#security`, `#privacy`, `#ai-coding-tools`, `#git`, `#zcode`

---

<a id="item-3"></a>
## [South Korea raises data breach fines to 10% of revenue](https://www.koreajoongangdaily.com/business/korea-raises-data-breach-fines-to-10-of-revenue/12869899) ⭐️ 8.0/10

South Korea has raised the maximum penalty for data breaches to as much as 10% of a company's revenue, moving its privacy enforcement closer to the GDPR-style fines used in the European Union. The higher cap applies to serious violations, with liability tied to intent or gross negligence. Fining companies a percentage of revenue rather than a fixed cap gives regulators real leverage, since penalties can scale with the size of the offending company and can no longer be shrugged off as a cost of doing business. If other countries follow suit, it could materially change corporate incentives to invest in security, privacy engineering, and vulnerability disclosure programs. The size of the actual fine depends on whether the breach resulted from intent or gross negligence, a standard that some observers argue is a high bar that may limit how often the maximum penalty is actually levied. As with the GDPR, the headline 10% figure is a ceiling rather than a default, so enforcement practice will matter as much as the statute.

hackernews · throw7 · Sep 18, 20:02 · [Discussion](https://news.ycombinator.com/item?id=49759466)

**Background**: Data breach notification laws require organizations to disclose when personal data is exposed, and regulators can then impose penalties. The EU's General Data Protection Regulation (GDPR) set a precedent by allowing fines of up to 4% of global annual turnover (or €20 million, whichever is higher), which reshaped how multinationals treat privacy compliance. South Korea's new 10% cap is stricter than the GDPR ceiling, signaling an escalation in Asia's privacy enforcement.

**Discussion**: Commenters largely welcomed the move as a rare sign that legislators are willing to make corporations care about security, and predicted rising bug bounty payouts if similar rules spread globally. Skeptics raised two main concerns: that the "intent or gross negligence" standard is a high bar that may mean few fines are ever levied, and that companies can dodge liability via shell entities — one commenter recounted a university that stored data at a three-employee shell firm which simply went bankrupt after a hack. Others argued that from a customer's perspective, the cause of a breach matters far less than the harm suffered, so fault-based standards are the wrong approach.

**Tags**: `#privacy`, `#security`, `#regulation`, `#data-breaches`, `#korea`

---

<a id="item-4"></a>
## [US Military Near-Miss After Acting on AI-Hallucinated Intelligence](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) ⭐️ 8.0/10

A CNN report describes how the US military narrowly avoided a dangerous incident after acting on an intelligence report that had been fabricated — hallucinated — by an AI system. The near-miss has reignited debate over how much operational trust militaries should place in automated analysis. The episode shows that the failure mode of AI in high-stakes settings is not runaway superintelligence but confident, plausible falsehoods that humans act on before anyone can catch them. Because military AI is already being used to support targeting and intelligence work, a single hallucinated report can escalate into real-world consequences for personnel, civilians, and international stability. In this context, hallucination means AI-generated content that is fluent and confident but false or unsupported by the source material, which makes it very hard for an analyst to distinguish from a genuine finding. Public details remain thin: the report does not identify which model or system was involved, whether human analysts reviewed the output before it was used, or exactly how the near-miss was caught, and CNN's account rests on unnamed sources.

hackernews · realsarm · Sep 18, 17:28 · [Discussion](https://news.ycombinator.com/item?id=49757520)

**Background**: Hallucination is a well-documented reliability problem in large language models: rather than retrieving verified facts, these systems generate text that is statistically plausible, and errors appear in the same confident tone as correct answers. Researchers distinguish factuality (correspondence to the real world) from faithfulness (consistency with the provided source), meaning an output can be wrong even when it looks well-supported. Militaries have been steadily adopting AI for intelligence analysis, surveillance, and even target selection, while watchdogs note that testing, evaluation, and oversight of these systems lag far behind deployment. Historical precedents loom large in the discussion, including the 2003 Iraq WMD intelligence failure and Soviet officer Stanislav Petrov's 1983 refusal to act on a false early-warning alert.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM_hallucination">LLM hallucination</a></li>
<li><a href="https://ainowinstitute.org/publications/safety-and-war-safety-and-security-assurance-of-military-ai-systems">Safety and War: Safety and Security Assurance of Military AI Systems - AI Now Institute</a></li>
<li><a href="https://www.brennancenter.org/our-work/research-reports/militarys-use-ai-explained">The Military’s Use of AI, Explained | Brennan Center for Justice</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News (329 points, 263 comments) were largely skeptical of the framing that LLMs are a "relatively poorly understood technology," with one arguing that they are essentially statistical retrieval systems whose outputs can be arbitrary concatenations of data. Others drew explicit historical parallels to the fabricated WMD intelligence that preceded the Iraq War and to Stanislav Petrov's 1983 false alarm, warning that pressure to "find targets" plus opaque black-box systems is a recipe for catastrophic error. A recurring fatalistic thread held that this — humans over-trusting moderately capable AI and acting on bad information — is far more likely to cause disaster than any superintelligent takeover.

**Tags**: `#AI safety`, `#LLM hallucination`, `#military AI`, `#national security`, `#AI governance`

---

<a id="item-5"></a>
## [Rust Security Team Warns of Targeted Social-Engineering Attacks on Maintainers](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 8.0/10

On September 17, 2026, Adam Harvey and the crates security team published a warning that an ongoing campaign is targeting rust-lang members and owners of popular crates, luring them into fake video calls framed as job, project, or contract opportunities and then tricking them into installing malware (such as a purportedly missing audio codec) or executing commands placed on their clipboard. The same technique was used in last month's successful supply chain attack against the arrayref crate and related packages. Rust is increasingly used in security-critical and infrastructure software, and a single compromised maintainer account can push malware into every downstream project that builds on that dependency — the earlier arrayref, internment, and append-only-vec compromise reached crates with hundreds of millions of downloads. The warning highlights that the human accounts behind open-source packages, not just the code, are the weakest link in the software supply chain that virtually all modern software depends on. The attack relies on social engineering rather than a software vulnerability: the initial contact is a benign-looking call, and the payload arrives either as a fake codec the victim is asked to install or as a command planted on the clipboard for the victim to run. Simon Willison notes that the most practical defense today is dependency cooldowns — delaying upgrades of new package releases by a few days so that a malicious version is more likely to be spotted by someone else first.

rss · Simon Willison · Sep 17, 23:59

**Background**: "Rustaceans" is the nickname Rust developers use for themselves, and crates are the packages distributed through crates.io, Rust's official package registry. A supply chain attack works by compromising an upstream dependency so that malware spreads automatically to everyone who builds on it, instead of attacking each target directly. The arrayref crate is a small utility library that supplies macros for working with fixed-size array references, but because it sits deep in the dependency trees of many large projects, publishing rights to it are extremely valuable to attackers.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack">Rust Supply-Chain Attack: arrayref, internment, and append-only-vec Poisoned by the proc-macro1 Build-Time Dropper - StepSecurity</a></li>
<li><a href="https://crates.io/crates/arrayref">arrayref - crates.io: Rust Package Registry</a></li>

</ul>
</details>

**Tags**: `#supply-chain-security`, `#rust`, `#security`, `#social-engineering`, `#open-source`

---

<a id="item-6"></a>
## [SemiAnalysis: Co-design for Efficient DRAM/SSD Offloading in LLM Inference](https://newsletter.semianalysis.com/p/engrams-embedding-entendre-codesign) ⭐️ 8.0/10

SemiAnalysis published an in-depth newsletter analysis on hardware/software co-design for efficient DRAM/SSD offloading in large language model inference, framing it as a question of the total addressable market (TAM) for DRAM and NVMe. The piece works through new model architecture implications and cites DeepSeek V4.1 Flash, the AgentX and InferenceX projects, and a set of NVMe offloading experiments. As models scale and context windows grow, KV cache and weights increasingly spill out of HBM and DRAM into local NVMe, so offloading efficiency directly determines inference cost and the memory mix that AI datacenters must buy. This analysis shapes how vendors and investors forecast DRAM/NVMe demand and how accelerator and storage roadmaps are prioritized. DeepSeek V4.1 Flash is described as the smallest model in DeepSeek's new architecture family, using an asymmetric structure and featuring native visual understanding for faster, cheaper inference, while InferenceX is SemiAnalysis' open-source Apache-2.0 continuous inference benchmark that compares platforms such as GB200 NVL72, GB300 NVL72, B200, MI355X and Google TPUs. The article's NVMe experiments focus on how data movement and cache placement policies interact with these architectures rather than announcing a new product.

rss · Semianalysis · Sep 18, 14:34

**Background**: LLM inference keeps a KV cache — the stored attention keys and values for every token in the conversation — and that cache grows with context length, often far exceeding HBM or even DRAM capacity. Tiered memory designs therefore offload cold data to NVMe SSDs and fetch it back when needed, trading PCIe bandwidth and latency for capacity and cost. "Co-design" here means changing model architecture and serving software so that the workload's access patterns are friendlier to that slow tier, rather than treating memory hierarchy as a fixed constraint.

<details><summary>References</summary>
<ul>
<li><a href="https://inferencex.semianalysis.com/">Open-Source Agentic Inference Benchmark | InferenceX by SemiAnalysis</a></li>
<li><a href="https://github.com/SemiAnalysisAI/InferenceX">GitHub - SemiAnalysisAI/InferenceX: Open Source Continuous Inference Benchmark Research Platform — Kimi K3 2.8T, MiniMax M3, DeepSeekv4, GLM5 - GB200 NVL72 vs MI355X vs B200 vs GB300 NVL72 & soon™ TPUv6e/v7/Trainium2/3 | 开源持续推理基准研究平台 — Kimi K2.7-Code、MiniMax M3、DeepSeekv4、GLM5 - GB200 NVL72 vs MI355X vs B200 vs GB300 NVL72，即将推出™ TPUv6e/v7/Trainium2/3</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#memory offloading`, `#LLM inference`, `#NVMe`, `#hardware co-design`

---

<a id="item-7"></a>
## [Researchers: xAI Grok Build CLI uploads entire codebases and .env secrets by default](https://t.me/zaihuapd/43897) ⭐️ 8.0/10

Security researchers performing packet-capture analysis on xAI's official coding CLI, Grok Build version 0.2.93, claim the tool transmits code to xAI servers through two channels by default: any file the tool reads (including secret files such as .env) has its contents embedded verbatim into model conversation requests and simultaneously packaged and uploaded to a Google Cloud Storage bucket, while the entire repository is uploaded as a git bundle regardless of whether the prompt asks it to read files. If confirmed, this represents a serious data-exfiltration risk for every developer using Grok Build, because source code and credentials could leave the local machine without meaningful consent — and since the upload reportedly happens even when the model is explicitly told not to read a file, prompt-level instructions offer no protection. The disclosure lands in a crowded field of terminal AI coding agents (Claude Code, Codex CLI, Gemini CLI) where trust in how code and secrets are handled is central to adoption, so it could shape enterprise policies and vendor transparency around data retention. The researchers report that in their experiment a file explicitly marked with an instruction not to open it still had its contents recoverable in the uploaded data, and that secrets flow to both the model request body and a Google Cloud Storage bucket without any additional configuration. The claim currently comes from a brief Telegram summary rather than a full technical write-up, and there is no mention of a CVE, a vendor response, or mitigation guidance, so the finding awaits independent reproduction.

telegram · zaihuapd · Sep 18, 05:57

**Background**: Grok Build is xAI's official terminal-based AI coding agent, released on July 25, 2026 and powered by the Grok 4.6 model, which runs inside a developer's shell and can read, edit, and reason over local project files. A git bundle is a standard Git command that packs an entire repository — including its full history — into a single binary file that can later be cloned from, which makes it an efficient but complete way to move a codebase off a machine. Files such as .env typically store API keys, database credentials, and other secrets that must never leave a developer's environment, so any tool that reads them requires careful scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/build">Grok Build | SpaceXAI</a></li>
<li><a href="https://git-scm.com/docs/git-bundle/zh_HANS-CN">Git - git-bundle Documentation</a></li>
<li><a href="https://nav.useaiwriter.com/reviews/grok-build-cli-review">Grok Build CLI 评测：马斯克的终端AI编程代理能挑战Cursor吗？</a></li>

</ul>
</details>

**Tags**: `#security`, `#privacy`, `#AI-coding-tools`, `#data-exfiltration`, `#xAI`

---