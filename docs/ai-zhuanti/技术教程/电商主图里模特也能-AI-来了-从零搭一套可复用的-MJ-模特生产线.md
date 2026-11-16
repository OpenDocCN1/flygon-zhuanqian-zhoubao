# 电商主图里模特也能 AI 来了：从零搭一套可复用的 MJ 模特生产线
作者：龙哥

看到抖音上有人直接用 AI 画出电商模特主图，我就把整套可操作的思路拆出来，变成文字版的实战流程。

## 核心工具组合：ChatGPT + Midjourney

先把需求描述写出来。第一步我会让 ChatGPT 帮忙生成模特的人物 Prompt，沟通可以用中文，写好后再用翻译工具翻成英文就行。

市面上可用的接口链接变化很快，今天能用明天可能就挂了，所以就不放具体地址了，自己找个稳定的就行。

拿到关键词后，生成环节就开始了，这里有个坑要避开。

![](img/zhuanqian_25316f89e642d7fa881fa28bf1f8facd.png)

实测发现 Midjourney 对“性感”这类词很敏感，一写上去基本直接拒图。把这个词去掉再试，如果还是不过，就按 MJ 返回的提示逐步删减敏感描述，直到能正常出图为止。

![](img/zhuanqian_ccada4a89f32f4bd0c6140a1c94d9a42.png)

四张初稿出来后，觉得不够满意想微调，或者直接图生图迭代，在 MJ 界面就能操作。

U1、U2 指的是你当前这个四宫格里的序号位置。V1、V2 指的是你要拿哪几张图去做图生图的来源。

比如我看中第四张，就点 V4 进入图生图，再选定那张作为底图继续优化。

![](img/zhuanqian_9a8872f5e38dd32121a4ca170bc816c5.png)![](img/zhuanqian_070d9210a400e54b713614efa8b0d501.png)![](img/zhuanqian_e3049ce4c354d535763e067959dcfcb0.png)

最终挑定一版满意的模特图，下载下来，这一步模特素材就算有了。

![](img/zhuanqian_9ad9ed6d854c3810a9716e8bede13fa9.png)

接下来需要一件衣服。手头没有实拍图，又不想碰版权风险，我直接让 AI 帮我也生一件。英文表达不熟练也没关系，靠翻译软件过渡就行，敢上手就上手。

这次给 AI 的描述是：A solid gray short sleeve with a dot of colored lettering print

![](img/zhuanqian_6031335aaa8a6d225264f8cc3d1ecf21.png)

![](img/zhuanqian_9c55655b668232b0bf545e643a146dac.png)

有了模特和衣服两件素材，进入合成环节。衣服图默认是白底，先把背景抠掉。

打开 PS，用魔棒工具点选白底，记得反向选区，快捷键 Ctrl+J 新建图层。

![](img/zhuanqian_2cb292a4146ee48e2620a3000b131d65.png)

![](img/zhuanqian_853877760b437b0811e610182a9e6661.png)

边缘残留的锯齿和飞边，用快速选择工具再细修一下就行。我的 PS 水平也就入门级别，能用就行，有追求的可以做得更精细，我这里主要讲方法论。

![](img/zhuanqian_821ccf14580dd3c0d0713820ecb62fad.png)

抠干净后把衣服图导出，再把文件发到 Discord，也就是连接 Midjourney 的地方。

![](img/zhuanqian_ac1ddbb0cba64c1f0fb88af95383822e.png)

上传完自己的图片后复制它的链接地址。

![](img/zhuanqian_73c63392ff0f67b160724f5ae2047339.png)

然后在输入框里输入 /image prompt，后面依次拼接：你的图片链接 + 之前生成模特时用的完整英文描述。末尾加上 Upscaled by --v 5 --iw 2 这样的参数。

完整指令示例：The 185cm tall male model is wearing a white short sleeved T-shirt made of comfortable textured fabric, highlighting his athletic figure. His arms are very strong, and he is obviously a regular exerciser. The lower body of the male model is also very attractive. You can see him wearing a pair of slim fitting jeans. The close fitting design highlights the lines of his hips and legs. His leg muscles are well defined, indicating that he is strong and athletic. Standing against a white background, the male model looks very fresh and natural, giving a feeling of sunshine and confidence. His posture is very natural, showing confidence and elegance. Overall, this male model is a very charming and charming person with outstanding appearance and temperament. - Upscaled by --v 5 --iw 2

![](img/zhuanqian_38cf3aba4c49ab2239d2bc43102d8088.png)

目前的经验是，衣服上不要带字母或复杂图案，效果会更稳定，纯色款最好。时间有限这次就先到这里，后续有余力可以继续深挖玩法。

整体思路就是这样，英文功底更好的朋友完全可以玩出更高级的效果。这个版本是我参考抖音原视频教程后，结合自己的实操补充出来的文字复盘。

总之先把框架搭起来，后续再不断迭代。思路通了，实战玩法自然就多了。

![](img/zhuanqian_48551018b96d9901014957df0c1a8bac.png)

我做的图不算顶尖，但拆解思路比成品更重要，有了思路才能衍生更多变种。

MJ 会员没 Visa 卡的，可以淘宝找人代充，速度很快，具体操作就不展开了。

别问我像不像真人，最终效果靠后处理和多生成几次来调整。这套方法胜在快，不满意就多跑几遍就行。

原视频参考：https://v.douyin.com/AuXENRn/

最后感谢 @淘金之路太白姐姐 帮忙排版，我的图片一直传不上去。

圈内交流欢迎加我：微信 3957165，公众号：侠狼网创