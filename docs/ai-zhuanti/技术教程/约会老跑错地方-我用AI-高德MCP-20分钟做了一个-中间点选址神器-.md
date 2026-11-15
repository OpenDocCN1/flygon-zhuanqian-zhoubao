# 约会老跑错地方？我用AI+高德MCP，20分钟做了一个“中间点选址神器”
你有没有经历过这种“社死”瞬间：和好友约咖啡，俩人都到了，结果一个在南，一个在北，压根不在同一个商圈？
最近我就栽了一回。一位创始人约我喝咖啡，他在中关村，我在望京，咱俩想着折中找个地儿。早上10点我美滋滋地晃到北辰荟，找了张椅子坐下，二郎腿都翘好了，低头一看微信——好家伙，约的是环宇荟！
就差了两个字，我俩愣是分头行动了。后来琢磨了一下，怪就怪我看到“荟”字就没细看，心想北辰荟有蔚来牛屋，顺嘴说了句“牛屋见”。对方也不熟，压根不知道环宇荟没有牛屋，就这么稀里糊涂答应了。其实北京还有个带“荟”字的商圈，离北辰荟还不远。
当时我脑子里突然蹦出一个念头：要是AI能自动帮我们算一个双方都方便的中间点咖啡馆，还发给俩人确认，是不是就不会闹这种笑话了？
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6362b79f87d262e0a287b787d3b9aa44.png>
巧的是，那阵子我刚好刷到一张关于MCP的图，一下子就想起了这次尴尬约会。于是立马动手，用Windsurf + 高德MCP + 32kw.com，只花了20分钟就把这个需求跑通了！
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_43ccfc7b77bd8096b4f967d31d15ee87.png>
上面这张图就是我20分钟做出来的页面，是不是有点东西？最绝的是头图直接标出了我俩的坐标，以及中间那家咖啡馆的精确位置——它真的落在中间点附近。你也可以直接打开这个链接体验：https://www.32kw.com/view/b109136
下面这份“喂饭级”教程，保证比市面上那些MCP科普更接地气，看完你也能上手。
## 到底咋做的？三步搞定
整个流程其实特别简单：
1.  在Windsurf里装好高德MCP
2.  直接告诉AI你的需求
3.  一键生成可视化网页
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7e2a6d3be7a0797214a83e5bb9550ca7.png>
### 第一步：给Windsurf装上高德MCP
先打开idoubi开发的MCP.so，在里面找到高德地图MCP Server（搜“高德”也行）：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9310a281126edb95b05ba048b9bd82ff.png>
点进去之后切到“Content”标签页，把接入配置代码复制下来：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_43e011e42dcc638472e6a9f3f7f37f86.png>
接着打开Windsurf，点“Configure MCP”，把复制好的代码粘贴到左边窗口，保存就完事。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9507f0c0b7867ccd7f12b9b875ce64a8.png>
要是看到红色报错也别慌，直接把代码丢给Windsurf，让它自己修：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8b3eeff35058f85e510a2a71569a814b.png>
它会自动搞定。不过还有个关键点——得申请高德地图Key。在MCP.so的高德MCP Content页面有个“复制key”链接，点进去有详细的申请教程：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3dc41f896731cf547587f745af35bf30.png>
申请完Key之后，填到Windsurf的MCP配置界面里，保存，然后点“Refresh servers”刷新一下。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f0ac4595335f45d1afa49035273ffd24.png>
如果@amap-maps前面亮起绿灯，恭喜，配置成功！到这一步你已经超过70%的人了，因为最劝退的就是配MCP。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dd8f5b1319c5a1165977c2f9c114ce91.png>
### 第二步：直接说出你的需求
配好后，我就在Windsurf里输入了一段提示词：
```
我住在北京朝阳区望京的宝星园，朋友在海淀中关村地铁站，帮我推荐几个离两个人比较近，方便停车的咖啡馆，并给出咖啡馆的具体信息。
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ec235655a89eacc4203844e94b51388a.png>
用的是Claude 3.7，它马上调用高德MCP的一系列工具来处理这个需求，没过多久结果就出来了！
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1bc52be8569d1b71bcf442b9d99fcc68.png>
### 第三步：一键生成可视化网页
拿到推荐结果后，我跟Windsurf说了一句“帮我做个网页”：
```
上面的推荐内容，能不能帮我生成一个html，用好看的图像化表达出来
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7ac5bae6032af4df8f8c25606dea12a0.png>
它瞬间就生成了一份HTML代码。我打开32kw.com，把代码粘贴进去，点一下“生成链接”，一个能直接分享的网址就到手了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_392af5529594055c5a2e57fe91bbd19d.png>
32kw.com相当于免费帮你把网页部署上线，发个链接给朋友就能看。就是文章开头那个页面：https://www.32kw.com/view/b109136
## MCP到底解决了什么问题？
能看到这里，你已经超过绝大多数人了。最后聊聊MCP的核心价值。
我们平时用高德地图导航、打车都没问题，但要是想找俩人的中间聚会点，可就费劲了。两点之间有好多商圈，每个商圈里又有不同的咖啡店，在手机上翻来翻去太麻烦。
但给大模型接上MCP之后，这事儿就变得特别轻松。因为高德App本身没法精确算中间点坐标，可大模型+高德MCP可以：
1.  先定位我的坐标
2.  再定位对方的坐标
3.  算出两点的中点
4.  以中点为中心搜咖啡馆
5.  把合适的咖啡馆列出来
6.  再把文字结果转成可视化网页呈现
再往深了说，大模型+MCP在哪些场景最有价值？
+   过去的产品本身搞不定，大模型单独也搞不定的问题
+   无法自动化解决的问题
后面我会顺着这个思路，继续整理更多MCP实战案例，感兴趣的朋友记得关注我的公众号。
## AI+MCP：从单打独斗到指挥千军万马
MCP（Model Context Protocol）的出现，意味着AI应用进入了一个全新的阶段。它不再只是个聊天的文本工具，而能成为连接各种外部系统的智能助手。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9fcd151ed9f04b1193091f95b44194d3.png>
想象一下，当AI能调用各种专业工具和数据源时，它的能力边界会被迅速拓宽。这就像是从一个单打独斗的士兵，一下子升级成了指挥各兵种协同作战的将军。无论是地图、数据分析、图像处理，还是内容创作，AI都能找到最合适的“专家”来解决问题。
在我看来，MCP会彻底改变人和AI的交互方式。未来我们不用再频繁切换App，只要告诉AI想要什么，它就能自动调用最合适的工具去完成。这种“一站式”服务会大幅降低技术门槛，让更多普通人享受到AI的红利。
MCP就像给大模型装上了翅膀，让它飞得更高、看得更远，解决更多现实问题。咖啡馆这个小例子，只是冰山一角。随着越来越多MCP出现，AI还将在更多领域带来惊喜。
试想一下，如果你常用的所有工具都接入了AI，会发生什么？欢迎在评论区聊聊你的看法！
对了，后续我还会在AI编程蓝皮书里更新更多案例。如果MCP足够颠覆，我打算联合几位朋友，一起做一份MCP蓝皮书，敬请期待。