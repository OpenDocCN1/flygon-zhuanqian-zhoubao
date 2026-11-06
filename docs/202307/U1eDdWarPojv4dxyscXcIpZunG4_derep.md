# 【技术图文教学】零基础也能玩转SD，做📕抖音爆款隐形引流图



先做个自我介绍，我花名玉米，主要在做AIGC的探索和落地。

之前做过一个小玩意，用图隐文技术把彩色隐藏图和微信二维码做在一起，保存到手机里用微信扫一扫就能加好友。

![](img/b4457a1e740ec60486928c5771f45601.png)

![](img/d539d06659032dfe1adf3db27af761eb.png)

![](img/147dc32258d6a3a1d6af80cc6df4a36e.png)

这次要聊的是生成式艺术二维码，也就是最近在网上炸开锅的隐文引流图。

# 一、为什么现在要做这个

最近AI画二维码火了，Stable Diffusion又被大家重新关注。与此同时，同样基于图像隐藏技术的生成式图隐文也在📕周末期间引流大爆发。

一张看上去很普通的AI美女图：

![](img/5e85fdfba2147e021263ece89f44b861.png)

仔细眯眼就能在画面里看出“牛逼”两个字，所以大家也戏称它为🐂🖊姐。

📕和抖音的引流团队很快嗅到机会，用新包装的老办法做导流。

![](img/b8bac534c037d8e23c15762d895526c7.png)

上线两天就拿到4000多个赞，1000多个收藏，300多条评论，全都是在问怎么做。实际引流到私域成交的量想必也不小。

关键是，这种帖子曝光还在持续，说明📕目前对这种藏微信信息的图片没办法识别，正好适合把公域流量沉淀到微信。

反应快的同行已经开始批量复制变现了。

那做起来真的很难吗？

用PS当然可以，但SD能做到更低成本的流水线生产。

而且难度并不高，基本就是SD入门级别的操作。

下面放几张我用龙哥盟主题做出来的效果图，分辨率压过方便看隐文：

![](img/9f333805341f7474e850d8f4110d012f.png)

![](img/998e4209885d7b89a2a794e920e8e7ee.png)

![](img/aacc998e1d428ecbe2b1913109efdb02.png)

![](img/7e443b63dc1f475eb201845c2f66f94f.png)

# 二、从零开始的保姆级实操

# 安装Stable Diffusion

直接去B站找秋葉aaaki的整合包教程，一键解压就能用，配置问题全包。

https://www.bilibili.com/video/BV1iM4y1y7oA/?share_source=copy_web&vd_source=6c09aa7f53b69992e1cd572bbd2dbf94

解压后找到启动器打开就行。

![](img/ba3760a857a4746c4cfca3b7201344ea.png)

# 模型准备

参考蓝鸟的歸藏大佬，常用的是Beautiful Realistic Asians

https://civitai.com/models/25494/beautiful-realistic-asians

不过我实测下来，模型对最终效果影响有限。

一张隐文图本质上是背景画面加前景文字，模型和提示词只决定画面里“画什么”，并不决定“怎么把文字藏进去”。

门槛因此很低，上限却很高。用对的物体去和文字结合，呈现会更惊艳；但就算用默认模型，效果也足够用。

下载完模型后，打开秋叶启动器，左侧模型管理，右侧选 Stable Diffusion 模型，点击上方打开文件夹，把模型拖进去。完成后点一键启动等待加载。

![](img/301e46f48d004f4f5cc6992f2a11c27a.png)

# 安装ControlNet

ControlNet是SD的一个插件，能给生成过程加入额外控制，比如草图、边缘、分割、人脸关键点、深度图等。

照着B站视频走即可：

https://www.bilibili.com/video/BV1fa4y1G71W/?spm_id_from=333.337.search-card.all.click&vd_source=e99f85042059f286d2dbf94

在Web UI里打开扩展页，点击可从URL安装，输入 https://github.com/Mikubill/sd-webui-controlnet 安装，装完重启。

![](img/3afe2b65d2dc2624407a07801bd82e4c.png)

重启后还要放进项目的核心模型 Brightness

https://huggingface.co/ioclab/control_v1p_sd15_brightness/tree/main

把文件放到 \models\ControlNet 目录下，回到SD刷新加载。

![](img/c3b7e517f36c761e201032a7c7d79000.png)

# 真正的生成环节

前面的都是铺垫，下面才是干货。

## 先用PPT或Word做一张黑底白字图

![](img/548a200fa5df0773e536a4db5a3ab91e.png)

## 选好模型，填入正向提示词和反向提示词

![](img/822b707aefdb9f9fa033d8d18409c4cf.png)

## 调整基础参数

![](img/0470f32a0f99da509f5ea0a8e6672b53.png)

## 载入ControlNet并选择Brightness模型，设置参数

![](img/5f6cf9ed7f4291dd5e9cd8c4cbd9fca9.png)

权重一般建议在0.4到0.65之间。数值越高，隐藏文字越清晰，但画面融合度会下降；图案复杂就调高一点，简单就调低一点。

另外两个时间参数，简单理解为ControlNet介入的时机。整体生成过程算1，百分比代表它开始工作的时间点。数值越大，留给模型融合的时间越少，文字会更生硬；数值越小，介入太早容易破坏结构导致文字看不清。

设置完点生成，多试几次就能找到手感。

# 三、最后的经验总结

多试几种风格后会发现，决定成败的关键在ControlNet和提示词，本体模型换不换差别不大。

Brightness本质是光影对比，所以在明亮对比强的元素上效果更好。

如果打算用来做微信引流，有几个坑要避：

微信名别太长，否则字会糊掉

尽量别用容易混淆的字母，比如a c o

可以适当加空格来区分，比如rn和m

错误示范如下：

![](img/d88e0a69ae91414b25b736df1a2c0be3.png)

![](img/de21fabc5b7d860d3b7ddb53e96ed906.png)

![](img/eedfd2dc420bfb7f898ba88c8d98a47a.png)

![](img/7069b9a4a2cc9e790202372a3d1a1377.png)

另外一个小技巧，底图的文字可以稍微倾斜一点，降低被平台检测到的概率。

![](img/9d06039a02b1f30bac91d8b48189d14f.png)