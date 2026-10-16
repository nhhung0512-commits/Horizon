---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 35 条内容中筛选出 7 条重要资讯。

---

1. [特斯拉发布可飞行 Roadster，配备冷气与火箭推进器](#item-1) ⭐️ 8.0/10
2. [Claude 逆向破解 NIST ECDSA 曲线种子的来源](#item-2) ⭐️ 8.0/10
3. [Jake Archibald 发布 JPEG XL 与 AVIF 网页图片格式实测对比](#item-3) ⭐️ 8.0/10
4. [苹果用 MLX 在四台 Mac Studio 上运行近万亿参数模型](#item-4) ⭐️ 8.0/10
5. [Mercor 报告：美国 90% 工时缺乏 AI 基准覆盖](#item-5) ⭐️ 8.0/10
6. [Big Fish：利用 OpenBSD 中一个 37 年前的内核漏洞](#item-6) ⭐️ 8.0/10
7. [阶跃星辰发布 Step 5 Preview 智能体旗舰模型](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [特斯拉发布可飞行 Roadster，配备冷气与火箭推进器](https://www.tesla.com/roadster) ⭐️ 8.0/10

特斯拉发布了一款配备冷气推进器（cold-gas thruster）并可选装燃烧式火箭推进器的新款 Roadster，并通过视频和 X（推特）帖子展示了夸张的垂直动作与飞行演示。该车分为两种模式：一种使用不燃烧的冷气，似乎只用于提供额外向前的加速；另一种采用真正的燃烧式火箭发动机，在视频中进行了飞行演示，且据称仅限受邀用户购买。 这是特斯拉近年来最受关注的产品发布之一，把电动车工程与航天推进技术结合在一起，并再次引发外界对该公司能把消费级汽车推到何种程度的讨论。它还引出了关于炒作式产品营销、预售定金融资模式，以及这类车辆是否真能在经济与法规层面落地的更大疑问。 冷气推进器通过喷嘴喷出加压惰性气体来产生推力，过程中不涉及燃烧，因此是结构最简单、最可靠的火箭发动机，但推力与效率都远低于单组元或双组元推进剂发动机。由于车载压缩气体储量有限，这类系统很可能只能完成一次或少数几次短暂跳跃；而视频中展示的燃烧式火箭版本仅限受邀用户，量产时间点则被提及为 2028 年前后。

hackernews · shekhar101 · 10月16日 01:32 · [社区讨论](https://news.ycombinator.com/item?id=50112657)

**背景**: 冷气推进器是一种火箭发动机，仅靠加压（通常为惰性）气体的膨胀产生推力，因其无污染且不涉及火工品，被广泛用于小型卫星和 CubeSat 的姿态控制。火箭推进器普遍通过高速喷出反作用质量产生推力，而推力更强的燃烧式型号则燃烧燃料与氧化剂，使尾气经喷嘴加速喷出。特斯拉 Roadster 的这次发布把上述航天概念搬到了公路跑车上，而该公司的销售模式要求买家在交付前数年就支付大额定金。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cold_gas_thruster">Cold gas thruster</a></li>
<li><a href="https://www.explainx.ai/blog/tesla-flying-roadster-cold-gas-thrusters-how-it-works-what-was-shown-2026">Tesla's Flying Roadster: What Was Shown, How Cold-Gas ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_engine">Rocket engine - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论区意见两极：不少人觉得飞行演示确实疯狂且令人惊叹，也有人认为把姿态控制（RCS）式推进器装在沉重物体上早已是成熟技术，谈不上多么“不可思议”。反复出现的批评聚焦于特斯拉的定金融资模式，有用户称这相当于为一辆可能永远无法交付的车提供多年无息贷款；也有人质疑垂直跳跃的工程约束、压缩气体储量有限，以及把火箭推进装置交到消费者手中所带来的安全隐患。

**标签**: `#Tesla`, `#electric vehicles`, `#engineering`, `#rocket propulsion`, `#industry news`

---

<a id="item-2"></a>
## [Claude 逆向破解 NIST ECDSA 曲线种子的来源](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 8.0/10

Anthropic 的 Claude 逆向破解了 NIST P-192、P-224、P-256、P-384 和 P-521 这几条 ECDSA 曲线长期以来来源不明的种子值，在不到半小时内判定它们并非由哈希函数生成，而是 C 标准库 lrand48 随机数生成器以 Unix 时间戳为种子所产生的输出。这一结论推翻了长期以来认为这些种子源自 SHA-1 等哈希函数的假设。 这一发现终结了围绕 NIST 曲线是否在其常量中暗藏后门的、长达二十余年的“袖中无物”（nothing up my sleeve）疑云，而这一疑云关系到所有依赖 ECDSA 的系统，包括 TLS、SSH、代码签名以及加密货币。这同时也是一个引人注目的例证，说明大语言模型能够完成原创且可验证的密码学研究，而不仅仅是总结已有工作。 关键线索在于 lrand48 返回的是 31 位数值，因此种子中每个 32 位字最高位始终为 0，这与观察到的“首位数字不超过 7”的模式完全吻合。而第五条种子——属于二进制曲线 B-163——仍无法用 Claude 的方法解释，讨论中提出的一种合理解释是：在发布流程的某个环节有人打错了一位数字。

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**背景**: ECDSA（椭圆曲线数字签名算法）是一种基于椭圆曲线密码学的数字签名方案，由于能用比 RSA 小得多的密钥达到同等安全强度而被广泛采用。1999 年 NIST 推荐了一组椭圆曲线（后写入 FIPS 186 标准），并公布了用于生成曲线参数的种子值，以便任何人都能验证这些曲线并非被人为挑选以植入弱点，这就是所谓的“袖中无物”（nothing up my sleeve）原则。然而这些种子从未被追溯到任何一种已知的生成方法，从而留下了存在隐藏后门的可能性，这正是密码学家们反复尝试逆向破解它们的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Elliptic-curves">NIST Elliptic-curves</a></li>
<li><a href="https://en.wikipedia.org/wiki/ECDSA">ECDSA</a></li>
<li><a href="https://pubs.opengroup.org/onlinepubs/7908799/xsh/lrand48.html">lrand 48</a></li>

</ul>
</details>

**社区讨论**: 评论区既感到惊叹又并未完全放心：有质疑者（fidotron）指出，确认生成方法并不能说明曲线是如何被挑选的，因为数月间生成的候选值可能被丢弃，而且仍存在通过遍历时间戳来挑选具有特定性质的曲线的可能性。其他人则提到此前已有独立尝试攻克同一问题，赞赏“31 位 lrand48”这一巧妙洞察可作为一个很好的提示交给模型，并推测那个无法解释的 B-163 种子可能只是笔误。

**标签**: `#cryptography`, `#ECDSA`, `#NIST curves`, `#AI/LLM`, `#security research`

---

<a id="item-3"></a>
## [Jake Archibald 发布 JPEG XL 与 AVIF 网页图片格式实测对比](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) ⭐️ 8.0/10

Jake Archibald 发布了一篇以基准测试为核心的详细文章，对比 JPEG XL 与 AVIF 在真实网页场景下的表现，涵盖照片、截图和插画三类素材的文件体积、编解码耗时以及编码器行为。该文在 Hacker News 上引发 133 条评论的讨论，开发者们分享了具体的 ffmpeg 转换命令，分析了 libjxl 最高压缩档位为何需要 9–46 秒，并指出使用更好的编码器可让无损 JXL 文件再缩小 30–39%。 图片体积至今仍是网页重量最大的来源之一，因此在 JPEG XL 与 AVIF 之间做选择会直接影响几乎所有网站的加载性能和带宽成本。由于两种格式在各浏览器中的支持度参差不齐，这种基于实测数据的实用指南能帮助开发者决定当下真正该上线什么，而不是只看规格表上的理论优势。 libjxl 的最慢档位对照片只缩小 2–7%，对截图和插画约缩小 25%，却要花 9–46 秒，是其默认档位的 50–180 倍，原因是它在 Butteraugli 感知误差指标上反复运行评估-优化循环。评论者指出，AVIF 沿轮廓压缩的特性使其在处理文字和线条图时能避开 JPEG 式的振铃伪影，而 JPEG XL 目前的编码器尚不成熟，换用其他编码器可显著减小无损文件体积。

hackernews · farlight · 10月16日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=50120224)

**背景**: JPEG XL 是一种免版税图片格式，目标是凭借更好的压缩率和渐进式解码超越 JPEG、PNG、GIF 和 WebP，并且可以无损地重新压缩现有的 JPEG 文件。AVIF 则是由开放媒体联盟（Alliance for Open Media）推出的开放免版税格式，把 AV1 压缩的静态图像封装在 HEIF 容器中，支持 HDR、8/10/12 位色深、透明通道和动画。两者都想取代传统网页图片格式，但底层路线截然不同：AVIF 源自视频编解码器，不具备渐进式渲染等特性，而 JPEG XL 是专为静态图像设计的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jpegxl.info/">JPEG XL : Superior Image Compression</a></li>
<li><a href="https://en.wikipedia.org/wiki/AVIF">AVIF - Wikipedia</a></li>
<li><a href="https://cloudinary.com/blog/how_jpeg_xl_compares_to_other_image_codecs">How JPEG XL Compares to Other Image Codecs</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同 JPEG XL 的潜力被当前孱弱的编码器拖累，有人指出换用更好的编码器后，文中那张无损 Firefox 截图可从 66.9kB 降到 40.7kB，猫咪插画可从 255.3kB 降到 178kB。也有人称赞 AVIF 在生产环境中处理截图和线条图的表现，并分享了具体的 ffmpeg 配方，其中一条能让文件缩小十倍以上且保留 PNG 透明通道；另一条讨论则剖析了 Butteraugli 优化循环，解释 libjxl 最高压缩档为何如此缓慢。

**标签**: `#image-compression`, `#jpeg-xl`, `#avif`, `#web-performance`, `#image-formats`

---

<a id="item-4"></a>
## [苹果用 MLX 在四台 Mac Studio 上运行近万亿参数模型](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 8.0/10

苹果机器学习研究团队发布文章，展示如何借助最新版 MLX 及其分布式推理能力，在由四台 Mac Studio 组成的集群上运行 Meta 近万亿参数的开源权重模型 Muse Spark Open。该配置的生成速度超过每秒 36 个 token，苹果称这已明显高于人类的平均阅读速度。 这表明前沿级模型不再必须依赖云端基础设施或数据中心 GPU，因为多台面向专业用户的苹果芯片设备可以被组合起来在本地提供服务，同时保证数据隐私。这强化了苹果将 Mac Studio 与 MLX 生态定位为可信本地 AI 平台的形象，也为开发者提供了除租用 GPU 之外的现实选择。 苹果给出的性能数据是在 8192 token 上下文长度下测得的，并描述了从单台最高 512GB 统一内存的 Mac Studio 起步、再横向扩展到多台机器的路径。有评论者指出，宣传中的对比把 Meta 的模型量化为 4-bit，却让 Qwen 保持原生 BF16，这种量化口径不一致可能使结果显得更好看。

hackernews · antipaul · 10月16日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=50118320)

**背景**: MLX 是苹果开源的机器学习数组框架，专为苹果芯片及其统一内存架构设计，使 CPU 与 GPU 可以共享同一份数据而无需在独立内存池之间复制。Muse Spark Open 被 Meta 称为迄今能力最强的开源权重模型，面向智能体式编程工作流优化，参数量接近一万亿。分布式推理指把单台机器装不下的大模型拆分到多台联网计算机上协同计算；而 Mac Studio 是苹果面向专业工作负载、以大内存为卖点的桌面产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MLX_(machine_learning_framework)">MLX (machine learning framework) - Wikipedia</a></li>
<li><a href="https://research.meta.ai/blog/muse-spark-open">Introducing Muse Spark Open, The Most Capable US Open‑Weight ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论整体偏怀疑：多人批评该基准不公平，因为它用 4-bit 的 Meta 模型对比 BF16 的 Qwen；也有人指出单台 256GiB 的 M5 Ultra 跑 DeepSeek 4.1 Flash 就能达到约每秒 45 个 token，因此集群成绩并不惊艳。还有人指出每秒 36 个 token 只在 8192 token 上下文下测得，对真实工作负载而言太短；另有一条评论调侃说，Meta 花数十亿美元训练开源权重模型，用户却要掏两万美元买苹果硬件。

**标签**: `#MLX`, `#Apple`, `#local-LLM-inference`, `#distributed-inference`, `#Mac-Studio`

---

<a id="item-5"></a>
## [Mercor 报告：美国 90% 工时缺乏 AI 基准覆盖](https://www.mercor.com/research/labor-index/benchmark-map/) ⭐️ 8.0/10

Mercor 的 Labor Index「benchmark map」研究报告指出，美国约 90% 的工作时间花在现有 AI 基准几乎没有覆盖或覆盖极差的任务上，因此很难判断模型在人们真正从事的工作上究竟表现如何。该报告将职业任务数据与当前评测所用的提示词进行比对，揭示出「被测内容」与「实际工作内容」之间的系统性错位。 如果基准分数是宣称「AI 正在接近替代人类工作」的主要依据，那么这一差距意味着相关结论可能系统性地偏向极少数岗位，从而影响企业的落地决策、劳动力影响预测以及公众对「AI 取代哪些职业」的讨论。这也暗示，AI 进一步进步的经济价值可能恰恰存在于当下排行榜完全没有衡量的领域。 报告指出，即便在控制「AI 暴露度」之后，工资总额更高的职业所对应的 O*NET 任务在基准提示词中仍被显著过度代表，并称主流评测集中在一小部分高价值白领任务上。评论者则反驳说，这份研究把「覆盖得好」和「至少覆盖了」混为一谈——例如社工任务「为有子女养育问题的父母提供咨询」仅凭 13 条提示词就被判定为「覆盖良好」。

hackernews · speckx · 10月16日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50121179)

**背景**: O*NET 是美国劳工部支持维护、被广泛使用的职业数据库，它把职业拆解为具体任务、技能与知识要求，因此常被研究者当作分析劳动力问题的通用语汇。AI 基准则是用于横向比较模型的标准化测试集（例如考试式问答题或编程任务），但它们围绕「容易测量」的内容构建，而非覆盖有偿工作的完整分布。Mercor 是一家招募各领域专家为前沿 AI 实验室生成训练数据与评测的公司，因此其 Labor Index 处在基准设计与劳动经济学的交叉点上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.onetcenter.org/database.html">O * NET Database at O * NET Resource Center</a></li>
<li><a href="https://www.dol.gov/agencies/eta/onet">O * NET | U.S. Department of Labor</a></li>
<li><a href="https://www.mercor.com/">Mercor | Organizing human intelligence to power the AI economy</a></li>

</ul>
</details>

**社区讨论**: 评论者总体认可这一观察视角，但对方法提出质疑：有人引用「门卫谬误」，指出用自动门取代门卫会忽略门卫承担的其他关键职能；也有人认为报告实际上把「覆盖良好」当成了「至少覆盖了」的同义词。还有人指出 AI 的投入似乎集中在高薪岗位上（「他们想让 AI 拿下好工作」），并援引 Karpathy 的说法——目前 AI 实际只能处理约 2% 到 5% 的工作；对于这种狭窄聚焦究竟是刻意为之还是技术当下的天然边界，讨论中并无定论。

**标签**: `#AI benchmarks`, `#labor economics`, `#AI evaluation`, `#future of work`, `#O*NET`

---

<a id="item-6"></a>
## [Big Fish：利用 OpenBSD 中一个 37 年前的内核漏洞](https://calif.io/research/big-fish) ⭐️ 8.0/10

一位安全研究人员发布了名为 "Big Fish" 的研究报告，详细描述了在 OpenBSD 中发现并成功利用一个存在了 37 年的内核漏洞的过程，该漏洞在业内审查最为严格的代码库之一中存活了数十年。这份报告随即引发了关于模糊测试、静态分析等自动化工具能否真正发现此类漏洞的广泛讨论。 OpenBSD 一向被视为最重视安全、被审查最严格的类 Unix 操作系统之一，因此一个潜伏 37 年仍可被利用的漏洞，会让人们重新审视“仅靠人工审计就能保证安全”这一假设。这一发现很可能进一步激化关于模糊测试与静态分析在特定内核漏洞类型上能力边界的争论。 根据 Hacker News 上的讨论，NetBSD 在 1999 年 8 月重写相关代码时“顺带”修复了同一缺陷，而非把它当作一次有针对性的安全修补。由于该漏洞已有 37 年历史，它早于 OpenBSD 于 1995 年从 NetBSD 分叉的时间点，源自双方共同的 BSD 代码血脉。

hackernews · rs_rs_rs_rs_rs · 10月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118977)

**背景**: OpenBSD 是由 Theo de Raadt 于 1995 年从 NetBSD 1.0 分叉而来、以安全为核心目标的自由类 Unix 操作系统，其血统可追溯到 BSD（伯克利软件发行版）。它的代码被广泛复用：Apple macOS 中的 pf 防火墙、Android 的 Bionic C 标准库、LLVM 的正则表达式库以及 OpenSSH 均源自 OpenBSD。内核漏洞利用研究通常不止于发现缺陷，还要证明该缺陷能被转化为权限提升等可用的攻击原语。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenBSD">OpenBSD</a></li>
<li><a href="https://grokipedia.com/page/OpenBSD">OpenBSD</a></li>

</ul>
</details>

**社区讨论**: 评论区有人称赞文章采用了 OpenBSD 发布公告风格的配图，并打趣说期待配套主题曲；同时也有更实质的讨论指出，该缺陷早在 1999 年就在 NetBSD 中被无意间修复。核心争议在于：模糊测试或静态分析是否真有可能发现这类漏洞，还是必须依赖人类从利用原语出发的思考。

**标签**: `#security`, `#OpenBSD`, `#kernel`, `#vulnerability-research`, `#exploit-development`

---

<a id="item-7"></a>
## [阶跃星辰发布 Step 5 Preview 智能体旗舰模型](https://huggingface.co/stepfun-ai/Step-5-Preview) ⭐️ 8.0/10

阶跃星辰在 Hugging Face 上发布了旗舰模型 Step 5 Preview，主打智能体（agent）工作场景，采用稀疏 MoE 架构，总参数规模达 6000 亿、激活参数为 270 亿。该模型支持最高 100 万 token 的上下文窗口，可接收文本、图像和视频输入，并以 StepFun Model License 1.0 许可协议发布。 这是中国大模型厂商推出的最大规模旗舰模型之一，6000 亿参数的稀疏 MoE 设计叠加 100 万 token 上下文，使其直接进入头部厂商的智能体模型竞争行列。由于该模型在软件工程、长周期智能体执行和专业知识任务（尤其是金融场景）上做了针对性优化，它面向的是希望在自有基础设施上运行自主编程与分析工作流的企业用户。 稀疏 MoE 架构意味着每个 token 只激活 6000 亿参数中的 270 亿，推理成本远低于同等规模的稠密模型。阶跃星辰表示该模型可通过 OpenAI 兼容 API 配合 vLLM 或 SGLang 进行部署，且采用的是自定义的专有许可协议，而非完全开源许可。

telegram · zaihuapd · 10月16日 06:36

**背景**: MoE（混合专家）是一种把网络拆分成许多专门化子网络（即“专家”）的架构，每个 token 只被路由到少数几个专家；稀疏 MoE 让总参数量保持很大，但每个 token 的计算量很小，因此厂商可以训练超大规模模型而不至于推理成本失控。vLLM 和 SGLang 是当前主流的开源推理引擎，负责批处理、显存管理和 KV Cache 复用等高效服务模型所需的工作。100 万 token 的上下文窗口意味着模型可以在单次请求中处理极长的输入——大约相当于数百页文本或一整个代码库——不过上下文窗口大并不等于模型真的能对所有内容进行有效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://github.com/vllm-project/vllm">vllm -project/ vllm : A high-throughput and memory-efficient inference ...</a></li>
<li><a href="https://benchlm.ai/best/large-context-window">Best Large Context LLMs (October 2026): 1M+ Windows Ranked</a></li>

</ul>
</details>

**标签**: `#LLM`, `#MoE`, `#AI agents`, `#multimodal`, `#model release`

---