# 一天搭好：RPA + Claude 组合，我做出了一款小红书爆款商品挖掘器
想做变现，选品永远是第一关。怎么找细分赛道、怎么挖冷门爆款，是每个想赚钱的人都绕不开的话题。最近我在小红书搜商品关键词时，撞见了几款让我完全没想到的产品。
比如 AI 头型检测，一份卖 98 到 1998 元不等，累计销量竟然突破了 5000 单，按保守估算流水就超过 500 万了。更离谱的是，上架账号粉丝才 4000 多。还有 NFC 游戏卡之类，也是之前从未关注过的隐藏爆品。
这一刻我转了念头：能不能把小红书上的商品信息批量抓下来，基于客单价和销量算出预估销售额，再按销售额从高到低排？这样最赚钱的品、潜在的机会就能一目了然。
想法一出来我就动手了，整套流程靠 RPA 做采集，Claude 做页面封装。从零到一的实操过程，今天完整复盘给大家。
# 采集与分析两步走
实现这个工具的关键节点就两个。
### 数据采集
要的是关键词下的商品信息和笔记信息。
这块我选了 RPA。原因很简单，小红书风控极严，加密也在常变，传统爬虫很容易被封。RPA 模拟真人操作，稳定性高很多。思路和我之前写的移动端笔记采集文章基本一致：
好处是走的是人工流程，只不过在后台自动跑，不易触发风控，效率也高，数据实时准确。
商品采集的逻辑和笔记采集相差不大，搜完关键词后切到商品 tab，RPA 会自动捕获到商品列表，再按需导出成 Excel 或 json。本篇就不再展开细节，前面那篇教程里已经讲得很透了。
### 数据分析
以关键词“AI”为例，我一共抓到约 2000 条商品记录。按预估销量倒序排一遍，排面全是惊喜。
前面提到的 AI 头型检测，销量 5000+，客单价不低，足见其赚钱能力。再一次证明，市场上总有我们想不到的变现点。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7f3f01c28b9eb7069cd8a6dd13b49269.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ca78d6d900129904701fd104c9a95874.png>
再看“搜索资料”这个关键词下的列表，更让人意外：有卖中药药方的，有 29 元的《学生家长必备手册》，销量也轻松过万。宝妈人群的消费潜力被低估了很久。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9554194883322a5a3f4f5ae65c85815d.png>
按这个方法，每个关键词背后都能挖出几条意想不到的盈利路径。只要有数据，就能持续刷新对机会的认知。
## 用 Claude Sonnet 3.5 一键封装展示页
采集完数据后，新的难题来了：怎么看？Excel 能存但筛选体验很差。于是我把数据倒进了 SQLite 数据库，xhs_note_mobile.db。
为了更方便查，我直接让 Claude Sonnet 3.5 帮我生成一个可视化页面。我的对话提示词大致是这样的：
“请为我设计一个简洁的网页界面,用于展示和筛选小红书商品数据。页面应包含以下功能:
1.  数据表格显示,包括商品名称、价格、销量、预估销售额等字段
1.  排序功能,允许用户按不同字段排序
1.  筛选功能,让用户可以按关键词筛选商品或者笔记
“请使用python和html帮我获取当前桌面上的xhs_note_mobile.db表中的xhs_goods，然后渲染到html中”
“请再次帮我修改，首先新增一个筛选条件为：search_keyword，另外请给我进行分页，因为数据过多容易卡顿”
“请再次新增一个页面，用于提交关键词，提交后请保存到这个库中的xhs_goods_keyword表中，你需要创建这个表，我后续要根据这个表中的关键字进行采集”
“接下来请你帮我优化下样式，现在表格是偏右的，左边一大块空间都白着浪费掉了”
“请再次帮我修改，goods页面中去掉商品ID，商家链接，卖家ID，抓取时间字段”
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3033a48d0170b6406acac4af013565e5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_156656afc0cb5f81e871faf65c82e1e9.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d016173e58a6cdfe2ebc6e27336216d.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7ace8f590e108ae46fe4d65d818fcae9.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3acef4e4f5548e89d7c7ade685237cb7.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4de547c548880e5bb97b3c508a0419b4.png>
当时是手动复制粘贴提示词，现在直接用 Cursor 会更顺手，官方还送 500 次 Claude Sonnet 3.5 额度，用过的都说好。
几轮对话下来，页面基本成型。完整代码不贴了，大家按需跟 Cursor 对话就行，几乎不用写代码，全是 AI 生成：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4b24f0c8230b0bdf0db1b900b87c3d80.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2a16d1d5fe9a639e6fafb8c0dae58ff9.png>
在线体验地址在这里：http://xhsgoods.lzzadvance.cn/，目前后台只有一台手机在采集，速度有限，请耐心等待。欢迎大家提建议、一起优化。
最后聊点感悟。有了 AI 加持，我整套采集加展示的闭环基本一天就跑通。更重要的是，我真正体会到数据驱动选品有多可怕——很多机会，你不看数据根本想不到。
RPA 负责自动化采集，Claude 负责快速搭建界面，两者结合，能让我们更高效地发现并抓住市场机会。一起加油吧。