---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 32 条内容中筛选出 12 条重要资讯。

---

1. [DeepSeek V4 Flash 0731 发布，速度与性价比大幅提升](#item-1) ⭐️ 8.0/10
2. [甲骨文禁止 OpenJDK 提交使用 AI 生成代码](#item-2) ⭐️ 8.0/10
3. [科技从业者丧失职业信念，行业面临意义危机](#item-3) ⭐️ 8.0/10
4. [批处理、算子融合与 SIMD 如何让 Postgres 提速 300 倍](#item-4) ⭐️ 8.0/10
5. [开发者分享与爬虫搏斗一年：150 万页网站 99%流量是机器人](#item-5) ⭐️ 8.0/10
6. [Wyzer：将编舞式编程引入编译型语言](#item-6) ⭐️ 8.0/10
7. [新墨西哥州法院判 Meta 赔付 5.67 亿美元，因其损害儿童心理健康](#item-7) ⭐️ 8.0/10
8. [SpaceX 10GW AI 算力豪赌：2027 年 3000 亿美元 ARR，微软为首要承购方](#item-8) ⭐️ 8.0/10
9. [Gemini 受挫，GCP 却因祸得福](#item-9) ⭐️ 8.0/10
10. [大模型量化位宽存在理论最优值吗？](#item-10) ⭐️ 8.0/10
11. [美国审查中国 AI 企业海外获取英伟达芯片渠道](#item-11) ⭐️ 8.0/10
12. [sub2api 曝 OAuth 高危漏洞，仅凭邮箱即可接管账户](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Flash 0731 发布，速度与性价比大幅提升](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10

DeepSeek 于 7 月 31 日发布了 DeepSeek V4 Flash 0731，这是对早期 Flash 预览版的高效优化升级。该模型在编程、推理和智能体（agentic）任务上的性能显著提升，同时保持了极低的推理成本和高速响应。 此次发布以极低的成本提供了接近前沿的模型质量，让开发者和爱好者能够以日常开销使用强大的 AI。它加剧了 LLM 提供商之间的性价比竞争，并可能对闭源竞争对手造成压力。 DeepSeek V4 Flash 是一个混合专家（MoE）模型，总参数 284B，激活参数 13B，支持 1M token 的上下文窗口。用户报告在双 RTX 6000 Pro Blackwell 配置下，预填充速度约为 8k token/s，单流生成约 250 token/s；不过 DeepSeek 已宣布即将进行大幅涨价。

hackernews · tosh · 8月7日 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

**背景**: DeepSeek 是一家发布开放权重大语言模型的中国 AI 实验室。V4 Flash 属于其 V4 系列，采用高效优化的混合专家（MoE）架构，每个 token 只激活一小部分参数，从而在保持强大能力的同时降低计算成本。近期 DeepSeek 与 Kimi 等竞争对手的发布迅速拉低了高质量 AI 推理的价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek - v 4 - flash</a></li>

</ul>
</details>

**社区讨论**: 用户对该模型的速度和性价比反应热烈，有人说它比预览版高出一个档次，日常使用每天只花几美元。也有人提醒，DeepSeek 宣布的价格上调可能会削弱其当前的成本优势，还有人指出市场性价比提升的速度之快（如对比 Kimi K3）。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#Model Release`

---

<a id="item-2"></a>
## [甲骨文禁止 OpenJDK 提交使用 AI 生成代码](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code) ⭐️ 8.0/10

甲骨文为 OpenJDK 发布了一项临时政策，禁止提交 AI 生成的代码，理由是法律风险和人力审查负担。该政策的最终版本仍由甲骨文的律师团队起草。 这是对最广泛使用的开源 Java 实现之一的一次重大政策转变，将影响依赖 OpenJDK 的贡献者和企业。这也在更广泛的行业辩论中增添了关于 AI 代码来源、版权以及志愿者维护者审查负担不断增加的议题。 该政策名为“OpenJDK 关于生成式 AI 的临时政策”，发布在 openjdk.org/legal/ai。政策明确提到“人类审查者本已有限的时间”是主要原因之一，并且在甲骨文法务团队敲定具体法律措辞之前保持临时状态。

hackernews · delduca · 8月7日 17:36 · [社区讨论](https://news.ycombinator.com/item?id=49213754)

**背景**: OpenJDK 是 Java 平台标准版（Java SE）的免费开源参考实现，采用 GNU 通用公共许可证第 2 版并附带 Classpath 例外（Classpath Exception），允许开发者链接 Java 类库而无需让自己的代码遵循 GPL。向 Oracle 管理的项目提交贡献的人通常需要签署 Oracle Contributor Agreement，以授权 Oracle 使用其贡献。AI 生成的代码可能带来法律不确定性，因为模型训练数据和生成代码段的实际来源可能不明确。因此，像甲骨文这样希望避免版权纠纷的公司，自然会倾向于制定更严格的代码来源审查规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenJDK">OpenJDK</a></li>
<li><a href="https://oca.opensource.oracle.com/">Oracle Contributor Agreement</a></li>
<li><a href="https://softwareengineering.stackexchange.com/questions/119436/what-does-gpl-with-classpath-exception-mean-in-practice">java - What does " GPL with classpath exception " mean in practice?</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一，但大多理解该政策的动机：有人指出甲骨文的法律优先文化以及其希望保留对“AI 洗白”专有代码提起诉讼的权利；也有人认为鉴于人类审查者负担和 Java 历史上的版权纠纷，这一做法是明智的。少数人质疑甲骨文一边大力推广 AI、一边禁止 AI 代码的时机，还有人称赞这是对“AI 垃圾”的“帝国反击战”，并顺便抱怨了内存价格。

**标签**: `#OpenJDK`, `#Oracle`, `#AI code`, `#policy`, `#open-source`

---

<a id="item-3"></a>
## [科技从业者丧失职业信念，行业面临意义危机](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/) ⭐️ 8.0/10

《Noema》杂志发表了一篇反思性文章，提出当整个科技从业者群体对职业失去信念时会发生什么。这篇文章引起广泛共鸣，吸引了近 300 条科技从业者分享自身幻灭感的评论。 这件事之所以重要，是因为科技行业的健康依赖于有动力、有信心的从业者；普遍的失望情绪可能加剧职业倦怠、削弱创新能力，并促使人才流失。它也反映了知识型工作中关于意义与身份认同的更广泛问题。 这篇文章将科技行业的悲伤视为一种文化与存在层面的状态，而非单纯的个人心理健康问题。评论者补充了历史类比（如印刷行业的衰落）和经济学层面的保留意见（如 K 型复苏）。

hackernews · RickJWagner · 8月7日 12:42 · [社区讨论](https://news.ycombinator.com/item?id=49209539)

**背景**: 这篇文章审视的是构建网络和软件的人群的情绪状态，而这一群体在历史上被视为享有特权和乐观向上。评论者将当下科技行业的萎靡比作印刷工的命运——随着技术变迁，这门熟练手艺彻底消失。还有人指出当今网络世界的毒性，另有评论引入“K 型经济”的概念，认为对大多数人来说，离开科技行业去做更简单的工作只是一种虚假的出路。

**社区讨论**: 评论区总体充满同理心且思考深入。有人将之与印刷行业的消亡作类比，有人指责当今网络的毒性消耗了科技从业者的韧性，还有人质疑对“接地气”职业的浪漫化想象，指出经营羊场仍离不开科技行业的收入。

**标签**: `#tech-culture`, `#career-satisfaction`, `#mental-health`, `#industry-analysis`

---

<a id="item-4"></a>
## [批处理、算子融合与 SIMD 如何让 Postgres 提速 300 倍](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 8.0/10

在一篇深度技术博文中，作者 Max (malisper) 描述了如何通过一个名为 pgrust 的项目，结合批处理、算子融合和 SIMD，使 PostgreSQL 在分析查询上提速高达 300 倍。 PostgreSQL 的行式逐行执行在处理分析负载时非常缓慢，而专用分析数据库正是利用这些技术。如果 pgrust 被证明可靠，它可以让 Postgres 用户在无需迁移系统的前提下获得接近分析数据库的性能。 作者称已通过形式化验证和差异模糊测试证明 1000 多个用户可见函数与 PostgreSQL 的逻辑完全一致。性能提升来自批量处理数据、融合算子以减少开销，以及利用 SIMD 指令在单条 CPU 指令中处理多个值。

hackernews · poly2it · 8月7日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**背景**: PostgreSQL 的执行器逐行处理数据，这种模式在分析型工作负载下会产生很高的逐行开销和较低的 CPU 利用率。向量化执行则将值按批处理，算子融合把多个计划算子合并起来，避免物化中间结果。SIMD 指令能让 CPU 同时对多个数据元素执行相同操作，进一步加速紧凑循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://clickhouse.com/resources/engineering/vectorized-query-execution">What is vectorized query execution?</a></li>
<li><a href="https://www.cs.columbia.edu/~kar/pubsk/simd.pdf">Implementing Database Operations Using SIMD Instructions Jingren Zhou</a></li>
<li><a href="https://bijuhanta.web.id/blog/operator-fusion-and-scan-pushdown">Operator Fusion & Scan Pushdown: A Deep Dive</a></li>

</ul>
</details>

**社区讨论**: 评论区对自适应规划充满期待，AsyncBanana 称赞这一进展并希望它证明该模式在学术/小众场景之外同样可行。但 sgt 和 ZiiS 对信任和生态兼容性表示怀疑，认为即使 pgrust 技术上更快，用户仍可能坚持使用官方 Postgres。还有评论者开玩笑说，想知道算子融合是否解释了为何 GROUP BY 仍然感觉很慢。

**标签**: `#postgres`, `#query-engine`, `#performance`, `#simd`, `#database`

---

<a id="item-5"></a>
## [开发者分享与爬虫搏斗一年：150 万页网站 99%流量是机器人](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/) ⭐️ 8.0/10

一位拥有 150 万页网站的开发者发布了一份年度回顾，讲述了与爬虫和机器人（约占 99%流量）搏斗一年的经历。文章中描述了激进的过滤策略，以及依赖 Cloudflare 等第三方服务所带来的权衡。 这篇文章揭示了机器人流量如何压垮小型网站运营、推高成本并扭曲分析数据。它还引发了一场更广泛的争论：网站所有者是否应该将访问决策外包给 Cloudflare 等大型中间商，还是应该使用工作量证明挑战等替代方案。 该网站每月的正常运营成本约为 90 美元，但一次严重的机器人流量高峰使成本飙升约 500%。一位评论者指出，Claude 的搜索机器人在 72 小时内从他网站上抓取了约 20.5 万个页面，却只带来了 1 次推荐，这体现了成本与回报之间的严重失衡。

hackernews · petercooper · 8月7日 14:51 · [社区讨论](https://news.ycombinator.com/item?id=49211386)

**背景**: 网络爬虫是大规模收集数据的常用技术，网站也越来越多地部署反爬措施，如 IP 封禁、验证码和行为分析。Cloudflare 充当反向代理，可以在流量到达源服务器之前进行过滤。工作量证明则是一种不同的方法，要求客户端执行一定的计算工作以证明自己是真实浏览器，Anubis 等项目即采用了这种方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/computer-networks/what-is-cloudflare/">What is Cloudflare | How it Works and When do you... - GeeksforGeeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_of_work">Proof of work - Wikipedia</a></li>
<li><a href="https://www.thordata.com/blog/api/anti-scraping-techniques">Top 7 Anti - Scraping Techniques in 2025</a></li>

</ul>
</details>

**社区讨论**: 评论者对网站日益依赖 Cloudflare 表示担忧，警告私人公司悄然做出的访问决定会损害开放互联网。另一些人则推荐替代防御方案：有人称赞 Anubis 的工作量证明方法适用于不依赖 CDN 的网站，有人建议改用静态网站以降低成本，还有多人对 AI 搜索机器人消耗大量资源却几乎不带来流量表示不满。

**标签**: `#web scraping`, `#bot mitigation`, `#cloudflare`, `#proof-of-work`, `#web operations`

---

<a id="item-6"></a>
## [Wyzer：将编舞式编程引入编译型语言](https://github.com/Wyzer-Lang/wyzer) ⭐️ 8.0/10

Wyzer 是一门新的静态类型、编译型编程语言，将编舞式编程（choreographic programming）与 Perceus 内存模型结合，以防止分布式死锁和跨服务协议不匹配。该项目已托管在 GitHub 上，0.1.0 版本即将发布。 Wyzer 是一次难得的尝试，将学术界的编舞式编程范式引入实用的通用语言。如果成功，它可以让分布式系统开发者在编译期就获得无死锁的保证，从而补充像 Rust 这类语言提供的内存安全能力。 Wyzer 没有使用借用检查器和生命周期，而是采用线性/仿射类型（linear/affine types）和 Perceus 风格的引用计数，作者表示这更易于 LSP 理解和分析。该语言的目标是在不需要垃圾回收器或显式生命周期标注的情况下，达到接近 C 语言的性能。

hackernews · v0id_isgood · 8月7日 12:28 · [社区讨论](https://news.ycombinator.com/item?id=49209385)

**背景**: 编舞式编程是面向分布式系统的一种编程范式，将多个参与者之间的交互写成单个“编舞”（choreography），从而保证每一次发送都有对应的接收，从构造上排除死锁。Perceus 是微软研究院提出的一种带复用（reuse）的精确引用计数方法，被用于 Koka 语言，使函数式代码无需垃圾回收器即可编译为高效的 C 代码。Wyzer 基于这两种思想，力图弥补 Rust 保证的缺口——Rust 覆盖内存安全，但不覆盖分布式环境下的无死锁性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Choreographic_programming">Choreographic programming</a></li>
<li><a href="https://www.fabriziomontesi.com/files/choreographic_programming.pdf">" Choreographic Programming "</a></li>
<li><a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2020/11/perceus-tr-v1.pdf">Perceus : Garbage Free Reference Counting with ReuseMicrosoft...</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了该项目的雄心，以及它与常见的渐进式语言设计的不同之处，但许多人希望文档更完善、示例更丰富。技术问题集中在 Wyzer 如何保证分布式无死锁（例如跨节点的循环等待），以及多所有者数据在 Perceus 式复用下是否会导致难以预料的性能问题。

**标签**: `#programming language`, `#distributed systems`, `#choreographic programming`, `#memory safety`, `#compiler`

---

<a id="item-7"></a>
## [新墨西哥州法院判 Meta 赔付 5.67 亿美元，因其损害儿童心理健康](https://www.theguardian.com/technology/2026/aug/06/new-mexico-court-meta) ⭐️ 8.0/10

新墨西哥州一家法院下令 Meta 因损害儿童心理健康而支付 5.67 亿美元，并要求其为未成年用户做出改变。相关报道发布于 2026 年 8 月 6 日，部分媒体给出的金额高达 9.42 亿美元。 这是针对大型科技平台的标志性裁决，可能鼓励其他州提起类似的公共妨害诉讼。它也进一步给社交媒体公司施加压力，要求其正视青少年心理健康和算法设计问题。 法院适用了新墨西哥州的公共妨害法（NMSA 1978 § 30-8-1），该法禁止故意维持任何损害公众健康、安全、道德或福利的事物。报道金额不一致：路透社和《卫报》称 5.67 亿美元，而《华尔街日报》报道为 9.42 亿美元；Meta 还被要求为未成年用户做出改变。

hackernews · boplicity · 8月7日 00:06 · [社区讨论](https://news.ycombinator.com/item?id=49204352)

**背景**: 该裁决是针对社交媒体公司损害青少年心理健康的系列诉讼中的最新进展。公共妨害法是一种州级法律工具，允许政府就污染等广泛损害提起诉讼；新墨西哥州的指控针对 Meta 涉嫌成瘾性的设计和 Instagram Reels 等功能。在美国，社交媒体监管和儿童上网安全已成为重大政策议题，尤其是在 Meta 内部文件和举报人证词揭示其对青少年用户可能造成的伤害之后。

**社区讨论**: 评论者承认这笔罚款对 Meta 来说相对较小，但也指出对于一个人口仅约 200 万的州，9.42 亿美元的判决按人均计算非常巨大。一位评论者指出了具体的公共妨害法规条文，其他人则称短视频成瘾算法和恶臭评论区具有更广泛的危害。还有人担忧，在全球越来越多国家限制儿童使用社交媒体的压力下，Meta 的财务前景和股价可能受影响。

**标签**: `#legal`, `#meta`, `#social-media`, `#regulation`, `#child-safety`

---

<a id="item-8"></a>
## [SpaceX 10GW AI 算力豪赌：2027 年 3000 亿美元 ARR，微软为首要承购方](https://newsletter.semianalysis.com/p/spacex-10gw-in-2027-why-its-real) ⭐️ 8.0/10

在一份新分析中，SemiAnalysis 认为 SpaceX 可凭借其发射能力在 2027 年前交付 10GW 的 AI 推理算力，并创造高达 3000 亿美元的年度经常性收入（ARR）。预计微软 Azure 将成为这一算力的最大承购方（offtaker）。 如果实现，这将极大加速 AI 基础设施建设，并改变云计算的经济格局，因为 SpaceX 将作为庞大的算力供应商入局。对微软而言，锁定 10GW 的推理算力可让 Azure 在 AI 竞赛中对竞争对手形成决定性优势。 该分析以“每 GW 每年 100B 推理量”为基准指标，并以微软 2026 年的“10GW 觉醒”作为需求触发点。这些预测极具推测性，取决于星舰的发射节奏、电力供应和部署物流等条件。

rss · Semianalysis · 8月7日 20:08

**背景**: AI 推理工作负载（如运行大型语言模型）需要数十 GW 级别的算力和电力，而 2024 年全球数据中心装机容量已超过 122GW。承购协议（offtake agreement）是一种长期合同，买方（如微软）承诺从生产方（如 SpaceX）购买一定数量的算力或电力产出，为大规模建设提供财务确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.visualcapitalist.com/data-center-capacity-around-the-world/">Mapped: Data Center Capacity Around the World</a></li>
<li><a href="https://www.energea.com/glossary/offtake-agreement/">Offtake Agreement Definition - Renewable Energy Glossary</a></li>
<li><a href="https://www.stonex.com/en/business/financial-glossary/offtake-agreement/">Offtake agreement in commodities and project financing | StoneX EN</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#AI infrastructure`, `#Microsoft Azure`, `#energy`, `#data centers`

---

<a id="item-9"></a>
## [Gemini 受挫，GCP 却因祸得福](https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking) ⭐️ 8.0/10

Semianalysis 发布分析文章，指出 DeepMind 在 Gemini AI 模型上的长期困境反而在短期内为 Google Cloud Platform（GCP）带来收益。文章将这一动态概括为“DeepMind 的长期失败，却是 GCP 的短期利好”。 该分析凸显了 Alphabet 内部日益明显的战略分化：DeepMind 在 AI 领域的高调受挫与 GCP 的商业增长形成鲜明对比。这之所以重要，是因为它可能改变投资者和行业对谷歌整体 AI 竞争力以及云业务前景的看法。 该文章聚焦于一个悖论：DeepMind 未能推出具有竞争力的 Gemini 模型，短期内反而可能利好 GCP——因为客户可能因此转向谷歌的云基础设施，而非其面向消费者的 AI 产品。文章从商业战略角度提出新见解：研究挫折对大型科技集团不同业务板块可能产生截然不同的影响。

rss · Semianalysis · 8月7日 02:32

**背景**: Google DeepMind 是 Alphabet 旗下的人工智能研究实验室，2010 年成立于英国，2014 年被谷歌收购，后与 Google AI 合并。Gemini 是谷歌推出的生成式 AI 聊天机器人和虚拟助手，由同名大型语言模型家族提供支持，此前基于 LaMDA 和 PaLM 2。GCP（Google Cloud Platform）是谷歌旗下的云计算服务平台，与 AWS 和 Azure 竞争，其收入独立于 DeepMind 的研究成果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_DeepMind">Google DeepMind - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Google`, `#Gemini`, `#GCP`, `#AI strategy`, `#cloud computing`

---

<a id="item-10"></a>
## [大模型量化位宽存在理论最优值吗？](https://www.reddit.com/r/MachineLearning/comments/1vi6im4/what_is_currently_considered_the_theoretically/) ⭐️ 8.0/10

一位 Reddit 用户提问：在固定内存和算力预算下追求最大模型能力时，当前研究是否已找到理论上最优的 LLM 量化位宽；帖子提到近期 3-bit、2-bit 乃至约 1.5-bit 量化已展现出很强效果。讨论指出目前尚无共识答案，并呼吁开展 2025–2026 年的新 scaling law 或大规模实证研究。 这个问题的答案直接影响本地部署时如何在“更低位宽”与“更多参数”之间取舍，尤其在使用 GGUF 这类格式时。如果找到经验验证的最优每权重比特数，模型压缩将更有章可循，也能在既定硬件预算下最大化模型质量。 帖子将问题表述为“2-bit 70B 模型对比 4-bit 35B 模型”这类取舍，而非尽量忠实保留某个预训练模型。相关近期研究（如 ParetoQ）表明，2-bit 和 1.58-bit 量化在“精度—模型大小”权衡上可能优于传统的 4-bit，但这仍是一个活跃的研究问题。

reddit · r/MachineLearning · /u/takuonline · 8月7日 17:10

**背景**: 量化的原理是用更低精度的数值格式存储权重（例如从每个权重 16 bit 降到 4 bit），从而减小 LLM 的内存占用，但会带来一定精度损失。GGUF 是 llama.cpp 的单文件格式，将量化权重、分词器和元数据打包在一起，使模型能在消费级硬件上离线运行。多年来 4-bit 常被称为实用的甜点位，但新的低位宽方法正在挑战这一经验之谈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2502.02631">ParetoQ: Improving Scaling Laws in Extremely Low- bit LLM...</a></li>
<li><a href="https://bentoml.com/llm/model-preparation/llm-quantization">LLM quantization | LLM Inference Handbook</a></li>
<li><a href="https://pguso.medium.com/the-gguf-format-explained-making-ai-models-run-anywhere-even-on-your-laptop-30dcb45358da">The GGUF Format Explained : Making AI Models Run... | Medium</a></li>

</ul>
</details>

**标签**: `#quantization`, `#LLM`, `#model compression`, `#efficiency`, `#GGUF`

---

<a id="item-11"></a>
## [美国审查中国 AI 企业海外获取英伟达芯片渠道](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 8.0/10

美国商务部工业与安全局（BIS）已启动系统性审查，调查中国 AI 企业如何在海外获取和使用英伟达芯片，包括通过其他国家的云计算平台远程访问。此次审查起因于一名白宫高官指控月之暗面在 Kimi K3 模型表现接近美国顶尖模型后，非法获取英伟达芯片并经泰国远程访问。 堵住云计算漏洞将把美国出口管制从实体货物延伸到服务层面，重塑中国 AI 实验室获取高端 GPU 的方式。此举将加剧美中科技竞争，并可能影响全球云服务商、英伟达的营收以及中国基础模型开发。 据报道，BIS 正在整理两份名单：一份是涉嫌将受限芯片走私入境中国的黑市国家，另一份是中国企业远程租用芯片的国家。由于远程访问本身并不违法，BIS 的法定权限尚不明确；美国众议院已通过两党法案拟明确授予该权力，但英伟达等科技公司预计会反对。

telegram · zaihuapd · 8月7日 11:18

**背景**: 美国已限制向中国出口先进的英伟达芯片，因此中国 AI 企业转而通过海外子公司、壳公司或云服务寻找替代途径。美国商务部工业与安全局依据《出口管理条例》（EAR）执行这些出口管制。基于云的访问处于法律灰色地带，因为芯片实际留在海外，交易属于服务而非物理出口。此次审查部分由月之暗面 Kimi K3 引发，该模型得分接近美国顶级模型；报道还提到阿里巴巴通过新加坡壳公司和 Megaspeed 在马来西亚使用英伟达芯片的例子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.gov/">Homepage | Bureau of Industry and Security</a></li>
<li><a href="https://www.academia.edu/107467807/An_Analysis_of_U_S_Competition_Against_China_on_Semiconductors">(PDF) An Analysis of U.S. Competition Against China on Semiconductors</a></li>
<li><a href="https://hao.cnyes.com/post/259840">實測 Kimi K 3 ：它真的站上了世界 之 巔 | 科技 | 鉅亨號 | Anue鉅亨</a></li>

</ul>
</details>

**标签**: `#AI`, `#Nvidia`, `#export-controls`, `#US-China`, `#semiconductors`

---

<a id="item-12"></a>
## [sub2api 曝 OAuth 高危漏洞，仅凭邮箱即可接管账户](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 8.0/10

sub2api v0.1.171 及之前版本存在一个 CVSS 8.8 的高危 OAuth 账户接管漏洞。攻击者仅凭受害者的邮箱地址，无需密码、验证码或用户交互，即可彻底接管账户。 该漏洞使攻击者能够完全控制受害者的 API 密钥、账单余额和订阅配额，对依赖 sub2api 的开发者构成严重威胁。由于 sub2api 是面向 Claude、OpenAI、Gemini 和 Antigravity 的统一代理，账户被接管还可能波及其他上游 AI 服务。 攻击者利用 pending session 流程中的 existingUser 分支未校验密码和验证码的缺陷，将目标用户 ID 设为受害者后完成 OAuth 身份绑定。此后攻击者每次 OAuth 登录都会解析为受害者账户，实现长期未授权访问。

telegram · zaihuapd · 8月7日 14:59

**背景**: sub2api 是一个开源 AI API 代理，用于统一管理 Claude、OpenAI、Gemini 和 Antigravity 等多个 AI 提供商的订阅，项目托管在 GitHub 的 Wei-Shaw/sub2api 仓库。OAuth 2.0 是一种广泛使用的社交登录框架，但配置不当可能导致账户接管漏洞。在此案例中，登录流程某个分支缺少密码和验证码校验，使攻击者能够将自己的身份绑定到任意账户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Sub2API">Sub2API</a></li>
<li><a href="https://portswigger.net/web-security/oauth">OAuth 2.0 authentication vulnerabilities | Web Security Academy</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#OAuth`, `#account takeover`, `#sub2api`

---