# 四个人一起做了一个 AI 吐槽大会
作者：龙哥

大家好，我是龙哥，全栈出身。去年基本没什么产出，今年算是重新开工了。

# 起源

这个项目的诞生很偶然。当时 @黄小刀 刀姐在传术师群里丢出了一段 GPT 吐槽的回复，被龙哥老大注意到了。

![](img/zhuanqian_a34c523047c8808831cdd3335b673d14.png)

![](img/zhuanqian_d130127f9c9068b142d91ce2bf671060.png)

龙哥老大说也想听 AI 吐槽他几句，这句话点燃了灵感。

![](img/zhuanqian_668959d643d06cb1ff5b6b6a6709015b.png)

![](img/zhuanqian_68166e8e936cc0cbcb82427b3d3b315a.png)

![](img/zhuanqian_67c3c1bd2d9bd6d48b65836f98fb24eb.png)

随后刀姐提议用两天时间做一个 H5 页面。我看了看觉得太保守了，两天？一小时就够了。觉得这个小玩意挺有意思，就跟刀姐对了下想法，用一个小时敲了个 Demo。

![](img/zhuanqian_b97088a17ee8fec7d6054961390b5b09.png)

![](img/zhuanqian_64383cc203ba632e050594d984f79c27.png)

![](img/zhuanqian_b0fc82ea668d237ee1b886b355a131ef.png)

第一版就这样出来了，右图就是当时的效果。

![](img/zhuanqian_f9cd191230d955728dc9aa1bb3f5e4f2.png)

![](img/zhuanqian_86fc1022ac40ec44b84c001519e65bc8.png)

故事没完。极简风在刀姐眼里太简陋了，不够“吐槽味”，她想要更有游戏感的界面。于是我们拉上了圈友 @YolyArk 百合负责视觉，@陈财猫负责 Prompt 和后端 API 支持，组成了一个小而精的作战小组。

最后的成品已经上线，可以去 https://tucao.space 试试。

![](img/zhuanqian_241fed18067c173b5817d71fa1c6be59.png)

![](img/zhuanqian_8b7239cc004b5a423bd1b2952fdbf0f4.png)

![](img/zhuanqian_694e7372d9f9dc336c597c1656d89153.png)

顺带一提，“AI 吐槽大会”这个名字是龙哥老大起的，和他之前发的两篇 AI 吐槽帖子一脉相承。

![](img/zhuanqian_e20e67c60ba1a672ccb64937dac95e82.png)

![](img/zhuanqian_5ffdf830171301eb1c5336f4afda2902.png)

![](img/zhuanqian_8fc0fc5e37ae4d7c570176e5e912f6e5.png)

前情说完了，讲清这款产品的来龙去脉，也讲清我为什么会加入进来。

# 竞品盘点

虽然需求来自群聊，但市场上已有类似尝试。主要的有：

1. 毒舌AI Wordware(https://twitter.wordware.ai)

一个用自然语言搭 AI Agent 的 IDE 平台。里面比较火的是推特罗伯特，能调用 Claude 分析用户推文，输出人格化吐槽报告。

量子位报道：https://www.qbitai.com/2024/08/177145.html

![](img/zhuanqian_da2286bab9e52dbc99d2d338cb3c11ef.png)

1. 哄哄模拟器(https://hong.greatdk.com)

面包多创始人王登科做的，2024 年 1 月在 QQ 群里火过一波。后来受腾讯链接拦截影响，流量断崖式下跌，SimilarWeb 显示 2024 年 12 月访问量只剩 33.9K。

他的复盘：https://mp.weixin.qq.com/s/DQDQX9Bomnx6ScS6dlGdVQ

![](img/zhuanqian_b0275b4970c024386b34b702b6ed6d69.png)

做完粗略的竞品梳理就开干了。刀姐想做，我也想试试合作开发，所以后面的分享更偏向如何把想法落地，以及过程中的一些感悟。

# 一小时做出 MVP

![](img/zhuanqian_b00cc710ab308847c9ef55c617b71f03.png)

首个原型我用的是 bolt 平台加定制 Prompt 的组合，很快搭出了基础 UI 框架。

参考刘小排老师的文章：https://scys.com/articleDetail/xq_topic/4848511545851418

文中给出的 Prompt 可直接丢进 https://bolt.new ，5 分钟就能起一个网页 UI

```
1\. 技术栈：用纯粹的HTML + TailwindCSS来做
2\. 核心功能：我要做一个运势网站，用户填入自己的姓名、选择生日，点击按钮，就可以就行运势计算。运势计算具体算法我不管，你帮我完成，但是要算出来让用户感觉专业、有理有据、愿意付费。 计算出来的运势至少要包括运势评级、运势分数、宜、忌、理由等等。
3\. 功能区域：你要有完整的header,hero, testinoials, faq, features, pricing, how it works ,footer 区域。网站的版权所有人是刘小排，联系方式bourneliu66@gmail.com，其他内容需要编写得专业、真实。
4\. 网站文案：所有网站上的文案内容，我要求你使用中文。关于这个运势计算网站，你需要强调我们是结合东方玄学、紫微斗数、易经、星座等等，强调中西方结合。
5\. 网站风格：网站配色和风格需要现代化、高级，类似于苹果官网的风格。网站需要自适应各种屏幕尺寸。
```

我在此基础上改了改，搭出了 AI 吐槽生成器的雏形。界面能出来，API 还没接。

![](img/zhuanqian_9015c1e14b68c0032112e4de7c90c5cb.png)

随后把代码导出，用 Cursor 补上 API 逻辑，几小时的对话后适配 Cloudflare Page，最终放到 https://ai-tease.pages.dev/ 上跑通了。

可见现在做 MVP 网站真的很容易。

不过需求评审时这个版本被否了，UI 太素功能太单，暴露出个人摸鱼和团队协作在迭代思路上的差异。

# 初版网站的搭建尝试

会后我分别用 https://bolt.new/ 和 Cursor 试着重做第一版，主要想验证两件事：做初版 UI 是否必须用 Bolt？Cursor 开启 Agent 模式能不能搞定？

## 用 Bolt 搭

喂入改造后的提示词，右侧是生成的截图：

![](img/zhuanqian_530fc52a33d72e9d2587f87f574ac0a5.png)

![](img/zhuanqian_0d3f587b2791ffe2be52c5e1450eeb20.png)

## 用 Cursor 搭

同样的需求，用 Agent 模式跑。

![](img/zhuanqian_de4d70b8022985f89de93b1e019bd950.png)

Cursor 的 Agent 模式会按你的指令自动执行多轮，最高 25 轮。

![](img/zhuanqian_6861fe7256592ad896775e7a66d9e90c.png)

过程中需要手动确认一些命令，比如右图创建 Nextjs 项目时要选 No/Yes，没确认就不会继续，走默认就行。

![](img/zhuanqian_a7fd7b12a4d43dcf051c3b2d54c822df.png)

![](img/zhuanqian_f8a0da67219b62ef544031f3c239ac8d.png)

跑完可以本地试跑，出错就把报错丢回去让 Agent 再改，重复两三次基本能得到一个可运行版本。

![](img/zhuanqian_e05f7f443fb3c078be409054a235916e.png)

![](img/zhuanqian_e7cd3e07a17075f2df2d2112688d62f4.png)

![](img/zhuanqian_87d500123b9f264802c67f1b7150064a.png)

效果和 Bolt 基本差不了多少。所以原型阶段 Bolt 和 Cursor 都行，Cursor 只是偶尔需要手动修 bug。

![](img/zhuanqian_7ec662131f7b0bbd9e1ba2c87affcac4.png)

# 接入定制 UI

原型有了，如果没有视觉需求就能继续加功能。奈何我们有 UI 设计师，就得按设计稿还原。

这块我大概花了两天在 Cursor 上做视觉适配，挺折磨的。AI 自动还原设计稿并不容易，尤其是这张图不是 Figma 来的，是 PS 切出来的。只能走老路子，一个元素一个元素抠，还要兼顾 H5 和 PC 的自适应。

复盘下来，想快的话第一版最好用模板 UI；如果一定要定制，最好让设计师基于网站的基础框架做图，直接换素材即可，别反过来让开发去硬怼设计稿，效率完全提不起来。

![](img/zhuanqian_b7c984f051480fce3b04af7002976209.png)

# 用 AI 探路技术方案

我觉得用 Cursor 开发到什么程度，取决于人本身的技术判断。

大家常看到的是 UI 长什么样，很少看到背后的技术坑。这时先问 AI 再让 AI 执行会更稳。

比如本项目需要存数据、选部署方式，我对这些也不熟，就先问 Clau de 再让它改代码，这样指令更准。

![](img/zhuanqian_2c39dd8c1954b7e27d532dc0beb0f667.png)

![](img/zhuanqian_d7797c1d979b8a4ea53c78d21c25de58.png)

![](img/zhuanqian_a595ad561fe9d864b830a239208fdedd.png)

再比如上线时域名一直 404，折腾半天才在 Clau de 反复追问下定位到原因：Nginx 的 80、443 端口没映射，Http 端口映射不对域名就解析不了。

![](img/zhuanqian_bef9d3f1ca561148e456183a969c9639.png)

![](img/zhuanqian_36f5e057806ce4d4c5ae517535b55644.png)

另外你可能注意到截图里 Clau de 先思考再回答，这是我喂了一个系统提示词，让它先自问自答再输出，提问体验很不错。

![](img/zhuanqian_cc5920b47b457ce70e7864d342e615ef.png)

提示词是开源的：

https://github.com/richards199999/Thinking-Claude/blob/main/model_instructions/v5.1-extensive-20241201.md

使用方法可参考卡兹克的文章：

https://mp.weixin.qq.com/s/IAKD0FfcYehs5FsDkLbTJQ

# 补充文档与部署脚本

开发收尾时让 Claude 补了文档和 Docker 部署脚本：

![](img/zhuanqian_eb502aef0132600cfe6ef4fa9f739478.png)

Docker 环境部署也会报错，把错误贴回去让 Claude 迭代，几轮对话就能解决。

![](img/zhuanqian_59a605523e6865eda576d695b6f18852.png)

![](img/zhuanqian_cc5099767d930f7835a968a0697fcc1a.png)

关键是自己要能看懂 Claude 写的文档，看不懂就继续追问，否则项目细节掌握在 AI 手里。

![](img/zhuanqian_98b5fe330a04b7baf26af31460e5ba9f.png)

![](img/zhuanqian_d996eeb758cd985b5ed32f3040131357.png)

我还让 Cursor 写了打包脚本，同样配了文档，否则根本用不起来。

![](img/zhuanqian_b6274a3b0b49575c8cdd5df244bcaf66.png)

![](img/zhuanqian_98966ea4f10a9907825395a82048c641.png)

# 网站发布

到这一步就可以发布了。

本项目我放在自有服务器上，前后端一起用 Docker 跑，更灵活，也避开 Serverless 的限制。

面板我没用宝塔，用的是开源替代品 1Panel: https://1panel.cn ，推荐。

官方文档一键脚本装好就行：

https://1panel.cn/docs/installation/online_installation

界面大致这样

![](img/zhuanqian_30d6a3e61c6b5615bcee7dec52581f82.png)

面板里装了 Nginx Proxy Manager，负责域名端口映射和自动申请 https 证书。

![](img/zhuanqian_602d2dc14472ae6a1f22a5eab264fe58.png)

界面如图

![](img/zhuanqian_a3e29eb72902dcba9d1f367b0c03eb79.png)

Nginx 配置很简单

![](img/zhuanqian_22281a89b31ad5f0d468e1385074cf21.png)

![](img/zhuanqian_1c02f7d7f3821375b8a8b5e7046f9cc4.png)

域名解析走 Cloudflare，CDN 也开了小云朵。

![](img/zhuanqian_95a29dd55906cb4c48690a376c077155.png)

# 接入数据统计

上线后要知道有多少人来。一般会接 GA4，现在是 GA4 版。入口我找了很久，最后靠 YouTube 一个教程找到路子：

https://www.youtube.com/watch?v=UtDPmhCKx3Qa

注册入口：

https://marketingplatform.google.com/about/analytics/

按视频操作拿到 ID 再填到站上：

![](img/zhuanqian_bac060c3ee81522bed8fd44b0054b5a7.png)

至于站内如何配置，直接问 Claude 就行。

![](img/zhuanqian_c99a90198d93452e9dc2de3eea06c04f.png)

![](img/zhuanqian_1744f4c79684dfcea8128304a5842d36.png)

除了 GA4，我还上了 Umami 的统计，https://umami.is 。GA 数据全但不直观，Umami 开源替代更直观，数据量没 GA 大，两者一起看更稳。

Umami 部署方便，可直上 Vercel 自带数据库。文档：https://umami.is/docs/guides

对比一下数据：

Google Analytics 4

![](img/zhuanqian_be2dd27bf82464f7b543ef5d45a45aaa.png)

Umami

![](img/zhuanqian_79071ff27d43ec1e9de45e9a67e9f2c2.png)

网站 1 月 17 号上线的，一上来就有 2K 多流量，原因后面再说。

# 提交搜索引擎

网站上线想被搜到，最好主动提交。实际我们还没提交，发布当天流量大，Google 就主动收录了。

提交方式很简单，搜 site:域名 找到入口就行。

![](img/zhuanqian_cf0b469ed6d1936b8edb1768865eebe8.png)

![](img/zhuanqian_e562ce9329347800a9f67597723bc6a0.png)

![](img/zhuanqian_cc6dd666343449282f369e3f534059d0.png)

提交后最好生成 robots.txt 和 sitemap.xml，方便爬虫抓取，具体怎么生成问 Claude 就行。

![](img/zhuanqian_0d3ad6ceb4e0637911de88d934d86d81.png)

![](img/zhuanqian_2d368ef0bdae5977eb64fb48d15a7aed.png)

# 冷启动

上线后要冷启动。一般靠 SEO 和外链。但我们没走这条路，当晚刀姐开了一场直播，现场演示 AI 吐槽大会，当晚拿到 2.2K 冷启动流量，还被 Google 主动收录。

![](img/zhuanqian_467bb8061bf8898b75380b61e72729cd.png)

![](img/zhuanqian_a33200b20807479e05c6ca7fb7d43c8b.png)

这是 1 月 17 日直播当天的流量图。

![](img/zhuanqian_1103c9c774e7a093b117f608b9c583cb.png)

![](img/zhuanqian_f38c0ce6e1d8e9e5c37b032554677d05.png)

![](img/zhuanqian_6f6363bb8349908b537d711528b5f6a6.png)

上线第一天流量就冲到了 2.2K，背后是刀姐一场社群直播带来的直接拉动。从数据侧看，绝大部分进入的都是来自微信移动端的用户。

产品本身的社交基因也起了关键作用，生成的卡片化内容很容易被转发扩散，再加上二维码扫码的低门槛机制，让传播变得顺滑。甚至直播当晚，曹大也在现场参与了这场 AI 吐槽大会。

![](img/zhuanqian_7312aec79f6ef6e297df0d1002dc5d9a.png)

![](img/zhuanqian_aead75c5439852173e2f4a2b4fe673c6.png)

# 后续计划

经历了刀姐直播的首秀后，现在网站日均稳定在几百的访问量，冷启动阶段基本可以算打通了。接下来更关键的问题是，这个产品的演进路径该怎么选。

结合现阶段的反馈，我梳理出两条可能的路线：

方向一：走社交传播路线，强化用户情绪发泄的价值感，用内容裂变换取流量，再通过广告实现变现。

方向二：做付费分析服务，面向自媒体创作者提供专业的账号吐槽诊断。

综合来看，我更倾向于方向二。因为在群里的日常观察中，大家最真实的诉求其实是想看 AI 会怎么吐槽自己，像龙哥老大这样的例子就很典型。

![](img/zhuanqian_ab7cbdd6a5f6ed439a9ade15ffb51e78.png)

![](img/zhuanqian_0aa7230b447c4c5ab6c8ac46900c85e5.png)

如果最终确定走方向二，我的打法是这样的：第一步，先锁定不同赛道的自媒体大 V，提供免费的吐槽体验；第二步，也可以自建产品号，日更吐槽大 V 的卡片内容来持续造势。用内容吸引关注，再逐步转化付费。

这个节奏有点像此前 Wordware AI 推出的产品，通过运营推特账号罗伯特先做声量沉淀，再打开付费墙。各位圈友觉得这个判断靠谱吗？欢迎来聊聊，给点更具体的建议~