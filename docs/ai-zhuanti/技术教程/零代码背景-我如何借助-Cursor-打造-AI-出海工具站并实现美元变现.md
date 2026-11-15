# 零代码背景，我如何借助 Cursor 打造 AI 出海工具站并实现美元变现
大家好，我是阿西，一名互联网运营从业者。完全没有编程基础的情况下，我自学 Cursor 搭建海外工具站，站点上线约半个月就收到首笔付费，实现了盈利。同时我在即刻、X、普刊运营相关账号【阿西_出海】，持续输出出海与 AI 方面的内容，多篇被官方推荐，在 X 平台阅读量多次破万。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bf50171a65f82690a7029794299f2251.png>
先说下做 AI 出海工具站的起因。去年 3 月，我在赚钱【AI 出海工具航海】里第一次接触到 AI 编程的概念。那时我还是个零基础的小白。从去年下半年起，我开始用 Cursor 制作海外站点。目前的阶段性成果是：5 个月业余时间做了 6 个站，包括游戏类、工具类、导航类。其中一个工具站已实现正向现金流，每月稳定到账美元；另一个工具导航站上线一周单日 UV 突破 200，之后日均自然流量保持稳定。
我保持每月上线 1-2 个站的节奏来练手感，现在做一个基础的 AI 工具站，从开发到部署，1 小时内就能完成。
这次重点分享的是去年国庆期间上线的 AI 工具站 AI Answer Generator。上线半个月就产生付费。那天收到通知时很激动，金额虽小，却是第一次靠自己站点赚到美元，也证明了产品被用户认可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8d964872450cf687f2f7aca363a5802a.png>
先展示下站点界面。功能非常简洁，是一款 AI 问答生成器，目标人群是营销从业者，主要解决营销场景下的提问需求。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_738ccd3c9c8b355542a78378b37644c4.png>
当时做过的站点有限，对页面设计并不熟练，所以美观度比较一般。放到现在复盘，视觉会做得更精致一些，毕竟界面颜值也会影响用户好感度。
接下来我会拆解零编程新手如何从 0 到 1 找到对标、挖掘需求、借助 Cursor 完成建站的全流程，结构如下：
1. 为何做这个站
2. 如何寻找对标并拆解
3. 如何用 Cursor 开发并上线
4. 冷启动怎么做
### 1、为什么做这个网站？
在出海工具航海中，我了解到 SEO 引流的基本逻辑：先锁定 SEO 难度低、搜索量尚可的关键词，弄清楚词背后的真实需求，围绕需求搭建站点，持续优化排名，从而获取 Google 自然流量。
#### 找词
怎么找这样的词？可以用词根扩展法。比如 generator 就是一个常用词根，背后对应用户对工具类产品的需求。比如想做二维码会搜 qr code generator，想取名会搜 name generator。类似的词根还有 Creator、Guide、Maker、Editor 等，可以长期积累。
确定词根后，我会去 Google Trends 看衍生词是否有上涨趋势，从中筛选有潜力的词。
#### 筛词
在 generator 词根下我发现 ai answer generator 近期流量在上升。但与 gpts 对比后判断，日搜索量约在 500 左右，规模不大。
判断流量的小技巧：在 Trends 里把目标词与 gpts 并排比较。gpts 日 UV 约 2500，若目标词曲线是 gpts 的 2 倍，则日 UV 约 5000。截图里能看到 ai answer generator 的曲线仅为 gpts 的约 1/5。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f43a5d353b5fffa3b4f4dce7a86f4f2f.png>
虽然量级偏小，但作为新手练手正合适。小词竞争小、更容易出效果。于是我用 ahrefs 查了该词难度，发现难度很低，约 4 个外链就能进前十。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8406f5b1e6e4793a4d27f0daaddfa01a.png>
相关工具：
Google Trends：https://trends.google.com/
ahrefs：https://ahrefs.com/keyword-difficulty
这个词对新手很友好。不过当时我还不清楚词背后的具体需求，以及技术实现是否复杂。
我在 Google 搜索该词，发现排名前 4 的站点里，只有 1 个站点把该词放在首页做，其余都是子页面功能，并非主营业务。用整站去竞争这个词，优势会更大。
点开排名第一的站点后，我发现该词的核心需求是帮助用户解答问题，且可用 AI 完成。我向 Claude 咨询在网页中实现 AI 问答的方式，得到的建议是接入 API 接口，且存在免费方案。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e0ec726707e76d2fa06bcb8cc3fa1c50.png>
到这里判断清晰：流量不算大，但难度低、竞争弱、实现成本几乎为零，适合拿来练手。
### 2、找到对标并分析
#### 功能拆解
我选取的是 Google 搜索该词排名前两名的站点做对标。借鉴龙哥的说法，抄作业就要抄头部。
竞品分析我先让 Cursor 初步梳理，提示词如下：
我现在要基于“XXXX”这个关键词搭建网站，请先不要写代码，先和我讨论框架与功能：
1、基于该关键词下主要竞争对手，分析用户需求与站点所需内容
网站1链接
网站2链接
2、确定一期与二期功能
3、页面区块如何布局
让 Cursor 把回复保存为 .md 文件放在代码目录，便于后续迭代时快速理解上下文。
通过分析，我了解到站点核心就是用户输入问题，AI 输出答案。排名第一的站点 akkio 主营是为广告公司提效，AI 问答只是其子功能，面向营销人员，解决营销工作痛点。
这个思路很有价值：给功能绑定明确的人群，切一个细分赛道。虽然人群小，但做到细分头部仍有流量。若做成通用 AI 对话，则直接与 ChatGPT 等巨头竞争，难度极高。所以我也把站点包装成面向营销的问答工具。
#### 流量拆解
我用 Semrush 对两家对标进行了流量拆解，先看 akkio：
##### 流量来源
流量分布显示直达与自然搜索约各占一半，意味着一半用户是老用户直接访问，一半来自搜索引擎，还有约 10% 来自引荐，主要是外链与社媒带来的。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b9e892250c914997c13ca6275b46ef11.png>
在来源细分中，搜索流量主要来自 Google，少量来自 Bing。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_144b38e1e72b6f2c86ee8970a5bd546c.png>
##### 搜索关键词
再看带来流量的关键词。虽然我们主攻 ai answer generator，但也可以学习竞品的其他长尾词。
可以看到 akkio 的核心词是 question ai，每月约 246k，折算日均 8200，流量很大，但难度为 Hard，放弃。排第二、三的是 ai answer 和 ai answer generator，其中 ai answer 难度较低，可作为补充关键词一起布局。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ee8c4bce19743fa3de010178aac4451b.png>
##### 外链情况
这里看 akkio 的外链体量，判断能否超越。
有人会问外链有什么用？一是提升权重，相当于他人背书；二是直接导流。
结果是外链 2.9 万个，非常庞大，超越难度高。但可以复制其外链策略，查看它投的外链站点，我们也可以去投。Semrush 也列出了全部有效外链，一键导出即可作为外链库。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7cdac6e364f37cd0595f56cc389b3b27.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4d3993c445c1a087e9c77120886e7f31.png>
第二个对标，我同样按流量来源、搜索词、外链三个维度拆解。
至此，我已明确站点应做哪些功能、布局哪些关键词、去哪些渠道投放外链，准备工作就绪。
### 3、如何通过 Cursor 开发、上线
##### 页面搭建
前文提到我已让 Cursor 完成竞品分析与页面规划。下一步提示词为：
根据上面竞品分析结果帮我搭建网站，使用 Next.js 框架。
围绕关键词“ai answer generator”撰写页面内容，要求 SEO 友好，配色简洁清晰，有落地页常见区块，页面总词数大于 1000，核心关键词密度约 3%。
选用 Next.js 的原因是生态里可用的 UI 库很多。缺点是部署时需安装依赖，流程稍繁琐。
Cursor 生成代码后，我问它如何本地预览。
回复需安装依赖。在 Cursor 终端新建终端，执行 npm install -g pnpm 开始安装，遇到报错把信息丢回给 Cursor 处理。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_67935d86c3a5209dd7b0d7040085f76d.png>
安装完成后执行 npm run dev，浏览器打开 http://localhost:3000 即可看到雏形。首页结构为导航栏、核心功能区、优势区、FAQ、页脚。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c5ccf0338b0fe2ff4f20ee0b0f211f98.png>
##### 核心功能开发，接 AI 接口
最核心的是 AI 问答，需调用模型接口。出于成本考虑先用免费接口，我选用 https://openrouter.ai/，内含免费与付费模型，标注 free 的为免费。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3d8bd45c6712d3b860250b2df80bbb95.png>
具体步骤：
第一步：获取 openrouter 接口文档与 API Key：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_79704ea56e0a94ca9bb1a601639df0bf.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a846c0405c198fd3731285ae692d86fe.png>
第二步：将文档与 Key 发给 Cursor，提示：
网站问答功能需通过 API 接入，以下是文档与密钥，请完成对接
到这里核心功能已完成。遵循“先发布再迭代”原则，先上线收集数据再优化，避免过度打磨。接下来部署上线。
##### 部署上线
* 先购域名，建议与关键词相关，后缀优先 .com/.org/.ai，价格较高。新手练手可选便宜后缀，我选了 .pro 约 $2。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0e09a613e78b091457839deffbf36e14.png>
我常在 https://porkbun.com/ 购买。次年续费可先不管，首年盈利后再考虑。
* 解析域名，推荐 Cloudflare 免费使用
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_32cc8ff68b9df351bdd7e64be6743c8a.png>
Cloudflare 地址：https://dash.cloudflare.com/。在独立开发者圈被称为“赛博菩萨”，除解析外还有免费图床等功能。
* 部署到服务器：代码推至 GitHub，新建 Vercel 项目关联仓库，最后在 Vercel 项目中绑定域名 aianswer.pro。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_76acd5ce183618a21e990a20eaf2d334.png>
至此可通过域名正常访问，完成整套上线流程。
工具汇总：
github：https://github.com/
vercel：https://vercel.com/
域名解析与部署细节限于篇幅不展开，熟练后每次 20 分钟内可完成。
### 4、如何冷启动
冷启动分为常规动作与个性化动作。常规包括收录、导航站提交、外链获取；个性化包括跟进竞品外链、数据驱动优化。
##### 常规动作
1. 网站收录
让主流搜索引擎收录后才有曝光机会，主流为 Google、Bing、Yandex。以 Google 为例：
1、打开 GSC，点击左上角下拉选择“添加资源”
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d166573b3028bb47c3be881606aee510.png>
2、输入域名，按提示完成校验
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e2ab3e6fa15982906db29e332cd3493a.png>
3、用 Cloudflare 解析的域名可通过授权验证所有权
4、收录查询：提交后等待一段时间，搜索 site:网址 可查看是否收录。也可通过提交高权重站点加速爬虫。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_79158acef02e0ceb08f10c57db2c1389.png>
2. 提交导航站
目前不少 AI 工具导航站支持免费或付费提交，如龙哥提到的 https://www.toolify.ai/。前期我先找免费站提交，等有转化再付费。
提交前准备好站点信息：链接、名称、邮箱、分类、简介文案、站点截图，提升通过率。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ea21067c58cf9656db3088c9315e45d2.png>
免费导航站清单我整理在：https://freelancer-tools.shop/backlinks/1
3. 获取高权重外链
例如在 YouTube 创建频道，简介里放链接即可获得一条外链，类似操作还有很多。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_166993ebfcc9cfd11b7e45ddf41062a3.png>
##### 个性化动作
1. 跟进竞品外链
前文提到的 Semrush 导出的竞品外链，我整理成 Excel，每天提交。我定目标每天至少提交 5 个。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0f47c755ac726450de33b720d436cc66.png>
2. 数据驱动优化
主要看 GSC 与 Google Analytics。GSC 可看关键词排名、是否有潜力长尾词、用户地域分布。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1279e11bc5388b8cce641aab4871048b.png>
Analytics 可看停留时长、流量来源渠道、用户访问页面分布、搜索/引荐/直达占比。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d4436cfed549256166340cdfe3320d5d.png>
据此我做了两项优化：
1. 增加多语言
默认英语，但 GSC 显示菲律宾、中国、日本也有访问。于是我在顶部加语言筛选器，优先翻译首页。多语言翻译同样由 Cursor 完成，提示词：
第一句：请列出主流语种
第二句：在首页导航栏增加语言筛选器，选项为上述语种
第三句：翻译首页文字内容，不要改动布局，站名 ai answer generator 不翻译
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e8987baceaf97c70bef862a3779d51fc.png>
2. 补充长尾关键词
把竞品使用的低难度长尾词逐步加入网站，扩大流量入口。
整体来看，零代码做 AI 出海工具站，本质是找低竞争关键词、抄对标作业、用 AI 工具快速搭建、再配合收录与外链。单步不难，关键在于执行。
如果你也想尝试，欢迎交流，或关注账号“阿西_出海”获取更多实战分享。
网站上线没几天，我在GSC后台发现又冒出了几个新关键词，正持续为站点带来自然流量。为了把这些长尾词的引流效果进一步放大，我索性在站内增设了一个博客栏目，围绕数据表现较好的几个关键词，分别产出一篇专题文章。当然，这些内容同样交给Cursor完成，当时用的提示词是这样的：
“请围绕关键词‘XXX’创作一篇不少于1500字的博客文章，文中关键词密度不得低于3%。”
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_82aebf62d2fa6b1a661e02502fbaa4be.png>
博客模块上线后，流量出现了肉眼可见的增长。趁着这波势头，我着手在站内布局付费入口。由于当时还没开通Stripe这类收款渠道，就先放了一个Ko-fi赞赏按钮，没想到第一笔海外收入就这样意外落地了。
### 最后说几句
以上便是一款AI出海工具站从需求挖掘、竞品调研到流量获取的完整链路，希望能给那些和我一样没有编程背景、却想借助AI编程搭建出海站点的朋友，在前行的路上点亮一盏小灯。
在流量获取部分，我重点写了如何用SEO来导入流量，包括关键词优化、外链建设等等。可能有人会问：为什么偏偏选SEO？难道没有别的路子吗？
当然有，像社交媒体推广、付费投放都是常见选择。但对刚做出海站的新手而言，SEO是最容易上手的路径。社媒推广需要你长期泡在平台上，摸清内容调性，还得花时间慢慢积累粉丝——顺带一提，我目前也在运营自己的社媒账号，对推特运营感兴趣的朋友欢迎来聊；而广告投放则要真金白银去测试素材和转化率，试错成本不低。
不过，SEO虽然门槛低、花费少，一个明显短板是见效偏慢。尤其是那些老关键词，已有不少竞争对手深耕许久，想反超只能一步步来。所以我个人比较推荐的节奏是：前期先用SEO做基础引流，当作练手，等有了稳定流量池后，再叠加社媒和广告投放来拉增量。
最后想说，2024年AI的爆发对所有人都是新机会。如果你也对AI编程或出海工具站抱有热情，不妨大胆试一次，沿途获得的惊喜远比想象中多。祝你成功！