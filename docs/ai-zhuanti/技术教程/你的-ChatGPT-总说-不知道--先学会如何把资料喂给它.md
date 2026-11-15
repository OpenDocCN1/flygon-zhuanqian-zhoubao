# 你的 ChatGPT 总说“不知道”？先学会如何把资料喂给它
作者：龙哥
阵地：龙哥盟 知识星球
身份标签：《人人都能玩赚ChatGPT》作者（京东能买到）、龙哥盟 ChatGPT 自媒体航海营教练
是不是总在羡慕别人家的 ChatGPT？
让它拆 PDF，它三两下给出摘要；
让它盯网页，它马上抓回最新消息；
让它看表格，它一眼说清趋势；
让它读文章，它模仿得一模一样；
让它翻聊天记录，它顺手把好友分了组；
让它啃完一整本书，它还能缕清重点；
再喂给它一个公众号，它就能告诉你号主对某个话题的态度。
听起来像“别人家的模型”？其实这些能力并不遥远。
差别往往只在：你有没有好好“喂”它。
### 01 | 先弄懂“喂”的意义
ChatGPT 的常识库主要来自 2021 年 9 月之前的公开数据，4.0 虽然后来接上了联网插件，但也不是什么内容都认识。
我们要分析的素材，通常逃不脱两种情况：
- 属于私有信息，网上根本没有；
- 虽在互联网上，但模型没来得及收录。
所以，它不懂很正常，我们要做的就是把“不懂”变成“懂”。
打个比方：你雇了一位机器管家，它什么都会，就是把没用过咖啡机。你把使用手册递过去，它当场学会煮咖啡，还能顺便解释咖啡机的结构和原理。
想让模型更懂你的意图，就不能省去这步“知识输送”。甚至不妨大胆想：未来每个人身上都能装一个学习接口，数据一键导入，知识秒变本能。
### 02 | 哪些资料可以喂？
一句话：凡是以文字为载体的内容，都能喂。
- Office 系列（Word、PDF、PPT、Excel）随便传；
- 图片里的文字，先用 OCR 工具转成文本再喂；
- 短视频内容，用语音转文字工具把字幕提取出来再喂；
- 公众号、网页上的文章，直接复制文字粘贴即可。
唯一的约束不是格式，而是长度。
文件太大没关系，真正的痛点是“怎么切”。1M 的内容很快能处理完；如果硬塞 30M，可能等到花儿都谢了。
网页版对话还有一重限制：官方对单次对话的 token 数量设了上限。最常见的 GPT-3.5 大约是 4096 tokens，折合约 2000 个汉字。一旦超限，页面会红字提示，逼你把内容压回去。
### 03 | 资料被“吃掉”之后，发生了什么？
以下内容偏原理，非技术玩家可以跳过，直接看第四节实操。
网页端最简单的投喂，就是在对话框里直接补充材料。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bae70713b648ad4f4aefd2dd02358d23.png>
通过对话输入更多信息，就能完成基础版投喂。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_34b4f866b0439edc5f954f94c224bb31.png>
但资料太长时，对话框就吃不消了。这时有两条路：Fine Tuning 和 Embedding。
打个粗浅的比方：
Fine Tuning 像亲手带一个“弟子”，他会活学活用、自由发挥；
Embedding 像给模型配一本“参考手册”，手册里写了的才能答，没写就答不出。
一个是开放式大脑，一个是检索式助手。
**Fine Tuning（微调）**
在 OpenAI 预训练模型的基础上，用你自己的小数据集再做一轮训练，让它在某个领域成为专家。不过效果要反复验证，测试数据也要覆盖得够广，才敢说“训练成功”。
比如你问它：“我们请的月嫂，相比别家的有什么不同？”
它可能会给出一个让你摸不着头脑的回答：
```
到家月嫂是一个纯洁的工作
```
这种“跑偏”，就是典型的发散型输出。
**Embedding（向量嵌入）**
把文本变成向量，然后比较语义距离。长文会被切成若干小块；用户提问时，系统先把问题变成向量，再从库里捞出最相关的内容，交给 ChatGPT 组织答案。
比如说，“苹果”和“橘子”的向量距离，一定比“苹果”和“沙发”近。
再比如说，“我要寄快递”这个表达，和“哪家物流速度好”这个问题，在语义上非常接近。
在线客服机器人，很多就是这么做的。
**主流工具的隐藏流程**
像 ChatPDF 这类工具，基本都是 Embedding 思路：
1. 你上传长文本，工具按策略切成块；
2. 每块文本做向量计算，存入向量数据库；
3. 你把问题拿过来，也向量化；
4. 系统在库里找最相似的若干块；
5. 把命中内容+原始问题一起打包，请 OpenAI 的对话模型生成回答；
6. 最终答案返回给你。
原理部分到此结束，非技术朋友们可以回归了。
### 04 | 不同场景，具体怎么喂？
**短文本**
内容不长时，直接在 New Chat 里粘贴就行。比如给 GPT 一段小红书文案，让它学完语气再仿写，这就是最基础的操作。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_13af9fdfff9d0157cc1d2bdda4446294.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a018e15e2cdaa7f724e47ae9a557be9e.png>
你看，我甚至没下指令，GPT-4 已经顺着风格往下写了。
**网址**
我们真正想喂的，不是那个链接，而是链接背后的文字。比如公众号文章。
能用得上的方式有三种：
- 用 New Bing：最省心。它跑的是 GPT-4，又自带搜索能力，可以理解成“能联网的 ChatGPT”。优点：免费、快；缺点：回复偏短，还容易聊着聊着就拒绝接话。具体开通方法，搜一下就知道了。
- 用 Chrome 插件：比如 WebChatGPT，装上之后直接把联网功能嵌进 ChatGPT。优点：免费且即装即用；缺点：ChatGPT 页面一旦改版，插件可能失灵。
插件地址：https://chrome.google.com/webstore/detail/webChatGPT-ChatGPT-with-i/lpfemeioodjbpieminkklglpmhlngfcn
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_13f2b6e38debb54fe540ff9a12ca3c46.png>
- 用官方插件应用市场的联网插件：审核严格，稳定性好，但前提得是 Plus 会员。先在设置里手动打开插件功能，然后搜索 WebPilot 装上，GPT 就能自己去访问网页了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a5a7e2208e8d9945174be5be120bb418.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_14374f4d677fa9bed559605c185dee9b.png>
看，它已经跑到 ESPN 去抓比赛数据了。
写给开发者的一段话：
如果你不打算用网页端，而是直接调 API，网址就要自己处理。可以用爬虫抓取页面，再用 readability 之类的工具清洗正文，最后把内容放进请求上下文。文档过长就切段，挑出和问题相关的部分再拼进去。
**PDF**
PDF 和网址同理，有官方插件，也有“野生”工具。
插件方面，AskYourPDF、ChatWithPDF 都能让 GPT 边读 PDF 边回答。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b323ba6426f8a5e0d0e75238dc173700.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5bf656d7e7e800a2df3fc576c3782cd2.png>
不是 Plus 用户也没关系，可以试试 ChatPDF：
https://www.chatpdf.com
或者圈友自制的 Chatpan：
https://chatpan.ai/
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_677f42415b4846bf3c0bd89040c51737.png>
我把龙哥过去说过的内容全丢进去，之后随时都可以开口问。这个“龙哥分身”从不嫌烦，而且秒回。
**Excel**
喂表格也不需要什么高深操作，把表格结构和你的诉求描述清楚就行。
比如下面这张表：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5e647c58483c1851a291134eae19b11e.png>
你想找出各维度表现都不错的网页，就直接在对话里提需求：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d2a316723364d3b50d0da78dce6a5de.png>
GPT 会给出对应公式，你复制到 E1 单元格：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_547c9dccc7d3b0179538abf2e3c6ef6f.png>
回车，结果就出来了：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_42be1acb72c1410318822e70831ebc9b.png>
这张表是虚构的，但这套方法可以复制到很多表格场景，能省掉不少重复劳动。当然，结果未必一步到位，剩下的优化和微调，还得自己来。
**图片、短视频**
GPT-4 发布时说过支持多模态，也就是音频、图片、视频都能输入输出，但目前还没全面开放，只能等。
如果图片里的内容是文字，先用 OCR 识别成文本，再送给 GPT；如果是人物、物体等画面类图片，暂时还得靠人工转述。
### 05 | 怎么问，才能得到好答案？
**提问本身就是能力**
这是公认最难的环节。
一个高质量的问题，往往直接决定答案质量。人和人之间的差距，有时就藏在提问方式里。
提问能力可以拆成两种：
1. 知道哪里有现成的优质提示词，拿过来直接用；
2. 自己掌握了提问的底层逻辑，随时能生成好问题。
底层逻辑这次不展开，之前航海分享过。这里先给一些“拿来就能用”的模板。
比如，你想让 GPT 分析一篇文章讲了什么：
第一步，先让它联网访问文章地址；
第二步，给它一个结构化的分析指令。
假设文章链接是：
https://mp.weixin.qq.com/s/guBFNFtwR9WdmYlFDKtJNg
按自己的模板输入后，得到这样的结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_83bbe21ade0dbbbff4b4f1e71d962550.png>
当时用的提示词是：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3793c01e1b5db19297bd1c85f57b580d.png>
再换一组思路，让 GPT 做分析：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1699146fbc8b998244a746c7402d8dfb.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_95cfa85055e10ab816c1abc06ddd64d3.png>
看完之后，原本想跟老婆一起创业的人，估计会冷静不少，甚至开始怀疑婚姻。
**借力高手的模板库**
在还没熟练掌握调教技巧之前，完全可以先用成品。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6d5e8b651339e825dbf456eb99b3ce91.png>
比如这个网站：https://www.aishort.top/
里面内置了 200 多套提示词模板，按需求复制、粘贴，基本就能生成你的自媒体内容。
一篇不够，就让 GPT 再来十篇，查重率控制在 5% 以内。
无非多耗点电。
如果还有具体困惑，不妨学学易仁永澄老师的方法：把“我想要”直接说出口。
- 我需要更多提示词模板；
- 我需要更多调教专题分享；
- 我需要某个平台的变现路径拆解。
把需求发到群里，教练们汇总后，会请对应领域的前行者来做分享。
好，这期“投喂”专题就聊到这里。
如果觉得有用，欢迎点赞、投币、关注。你的点赞、投币和关注，就是作者继续写下去的最大动力。
### 06 | 文中提到的资料
**1. 龙哥的电子书**
龙哥盟星主的电子书，可自行搜索。
**2. 龙哥盟星球**
在知识星球上万个社群里，龙哥盟的活跃度多次排名第一。从 2017 年运营至今，已走到第七年，累计 4.6 万人加入。
各行业的赚钱项目，几乎都能在这里找到成熟的“流量—产品—变现”打法。
因为信息前沿、内容扎实，官方还会请高手带队实操，很多圈友因此赚到了钱。最新一期的提前续费率已经接近 70%，有人称这里是“赚钱圈的黄埔军校”。
内容质量高、实战项目多、交流氛围好、价值观正，这四点都是公认的。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ede8af3ba7b13074589a28312c584bb3.png>
**3. ChatGPT风向标 星球**
一个免费的 GPT/AIGC 交流社区，目前用户数已超过 4 万。大家在这里交换最新案例和合作机会。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c480e200c2e62b6f5014411300be11b3.png>
**4. AI探索家 电台**
在网易云音乐、小宇宙等播客平台搜索“AI探索家”就能找到。每周五更新，黄小刀陪你谈 AIGC 应用、谈投喂、谈一切你关心的话题。
**5. 风向标拆解模板**
```
Q：你今天关注的风向标是哪一个？请填写参考案例:
A：船员填写：
Q：请给出这条风向标的1-3个知识点？
A：船员填写：
Q：请说出它的商业模型是什么？
A：船员填写：
Q：请判断它的盈利状况，如有可能，请说出月盈利预期。
A：船员填写：
Q：请判断为什么它是机会/为什么它不是机会？
A：船员填写：
Q：如果你要来做这个项目，它的最小 MVP 是什么？你会怎么开展工作？
A：船员填写：
```
请你扮演我的商业参谋，帮我拆解某个赚钱风向标。请从创业者的视角，基于下面这张模板作答，并适当延伸，覆盖变现空间、异常值、商机、用户需求、变现手段等维度。
备注：本文完成于 2023 年 5 月 25 日，文中工具后续可能更新或调整。