# 从0到1做出能扫的艺术二维码：我跑了几百张图后总结的实操笔记



近半年AI绘画几乎是坐火箭在往上冲，Midjourney和Stable Diffusion稳稳占据了两大热门位置。围绕它们衍生的创意玩法也层出不穷。半个多月前，站内就有圈友在聊艺术二维码怎么玩，我当时一边感叹技术迭代太快，一边又被自己的硬件配置卡住。电脑小白一个，云端部署看着就头大，也没有SD使用经验，只能干看着。

# 一、需求是怎么被点燃的

大概在半个月前，有位圈友丢了个链接https://t.zsxq.com/10vQhYFkY 我点进去一看立刻上头，当天就去小程序充了周会员开整。连着试了几张，效果还挺惊艳。晚上刷抖音正好刷到教学视频，我顺手把自己生成的图丢评论区就去睡了。结果第二天一早醒来，微信一堆添加申请，几十条直接把我吓到。

![](img/965689ea51d08492dfb4a2ff8432ceb9.png)

![](img/1bf6fbb71ae83b2a92b391a9189218bd.png)

大部分人只是图个新鲜想扫一下尝尝鲜，但也有不少人直接来问能不能定制。我之前完全没调研过市价，就随手报了29.9一张，小程序出图成本大概1元。第一天就有近60人通过二维码加我，成交7单。后面几天累计加粉破百，净利润四百出头。钱不多，但从0到1验证了需求是真的。

正好家里连续停电两天，我跑了网吧两天，靠4080实操。中间崩的图数不清，崩脸断手断脚是常态，前后试了几百张，反复调参，才终于刷出第一张既好看又能扫的成品。那一刻的成就感真的爆棚。

![](img/2635bfede0dc7cb84341318625ccc9f3.png)

![](img/043f40989fdca411ba8003c0b78468f2.png)

![](img/74f6b2eeffda0352443984321893a6b5.png)

帮朋友生成二维码，请勿添加

有了正反馈我开始发力，也去小红书、B站补了不少关于艺术二维码的干货。市面上已有两位前辈做了很系统的分享，基础部分我就不再赘述，感兴趣的可以自行查找。本篇主要做补充和拓展，直接上干货。

目前比较火的艺术二维码到底怎么玩？以及如何用SD把质量拉满？站在巨人的肩膀上，感谢前人的分享。

# 二、制作流程拆解

## 1、Antfu 的多变用法

Antfu的玩法很灵活。网址栏直接输文字就能生成文字型二维码，再丢进SD渲染。对于个人二维码来说，审核相对宽松。小红书上很多人点名要文字艺术二维码，表白、惊喜场景很吃香。还能上传背景图，后面会讲到。这里注意两点就够了：

1、二维码点阵分布尽量均匀，生成出来的画面才协调
2、务必先用手机实测扫描，识别率是艺术二维码的生命线

![](img/125a080c648489d6872866538c5627d9.png)

![](img/6921ac576295f56c4440ebd93041f109.png)

![](img/aa7a8016fb3bac254c8a9b3c32039a70.png)

## 2、SD 生成环节

### 1、常规艺术二维码

![](img/c7ffa166212b514186e09aa9124fd059.png)

![](img/82a7b5392e8c8501b1115c6cc9161765.png)

![](img/e103d22fada73ac81c529594e1666b60.png)

![](img/a20e251cbe098346c7d0bb1dcc6ad410.png)

这是目前最常见的形态。按参数走就行，靠抽卡出效果，也能配合各种Lora指定风格。比如王者荣耀角色风，提示词里出现人物建议加上full body，让人物全身入画，这样脸部占比小，不容易被二维码点阵覆盖。脸部变小容易崩，ADetailer修复神器可以兜底。文末有资源包链接，方便自助安装。

我的起手正面词：masterpiece,best quality,1girl,blonde hair,blue eyes,beautiful eyes,detail,flower meadow,cumulonimbus clouds,lighting,detailed sky,garden,full body,

反面词：(((nsfw))),EasyNegative,badhandv4,ng_deepnegative_v1_75t,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), bad anatomy,DeepNegative, skin spots, acnes, skin blemishes,(fat:1.2),facing away, looking away,tilted head, lowres,bad anatomy,bad hands, missing fingers,extra digit, fewer digits,bad feet,poorly drawn hands,poorly drawn face,mutation,deformed,extra fingers,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,teethcroppe,signature, watermark, username,blurry,cropped,jpeg artifacts,text,error,Lower body exposure

这只是基础模板，提示词可自行用翻译工具微调，也可以用提示词网站辅助优化。不同二维码的调参需要反复试验。想增强某个效果就加权重：

1、公式：圆括号() + 冒号: + 数字，意思为增强/减弱n倍
2、公式：圆括号()，意思为增强1.1倍，可叠加
3、公式：大括号{ }，意思为增强1.05倍，可叠加
4、公式：方括号 [ ]，意思为增强0.9倍，可叠加

我常用的出图参数如下：

![](img/2314659ba0b529f040fa9c53168a559c.png)

建议至少开两个ControlNet窗口。我日常就用两个，熟悉后可以增减，也能加入艺术文字等玩法，当然耗时也会增加。此图比较粗糙，凑合看，后续有机会再深挖美观度。

![](img/c255d8e61e86bb2d0fbe6c3874ba2edb.png)

第一个ControlNet设置
上传图后勾选启用和Pixel Perfect完美像素
预处理器可不选，模型选qrcode monster
Weight一般1.5左右，可自行微调，无固定值
Start step和End step写0.1-0.85，给模型创作空间

![](img/83387607c41d43616a32fc789e55fcd8.png)

第二个ControlNet设置
同样上传图，启用+Pixel Perfect
预处理器不选，模型选brightness。作用是调节画面与二维码的明暗关系，提升可扫性。Weight设0.2-0.5即可，我一般0.25，Start step和End step设0.65-0.85

![](img/8e36244db8ac12dab733a59c63abbd24.png)

### 2、局部呈现的二维码

![](img/7655ebeec2190f2f0270e6ddc7bf9d23.png)

![](img/1738612304893fe11c0e7ab2da4fc83f.png)

![](img/71e3108c8329d0106d937fc9e469a0d2.png)

在上面流程上多加一步，让二维码只出现在画面局部，比如裙摆、袖口等。留白多，SD发挥空间大，成品既能当壁纸用也兼具实用性。可以放到壁纸套样机里沉浸体验：https://mjcn.club/ ，小红书很吃这一类。

操作方式：用Antfu生成的图在P图软件里新建一张图，这里以稿定设计为例，先构思二维码位置，比如裙子下方。放好后先用手机扫一下，确认尺寸不影响识别。然后按第一种方法进SD出图即可。

![](img/b788ecbeddfbc70b7cb90c1b716762c1.png)

### 3、圆形二维码

![](img/db3aaf979c252511c37cfc7ac2fbf77a.png)

![](img/955328ee9c722770b446e3555757b567.png)

![](img/9d216b8504185e6d78b6ecab9b3967d7.png)

![](img/43a8900a9ed2710fd315d812fdd83edb.png)

前面提到的Antfu上传背景功能在这里派上用场，隐藏感和观赏性都更强。

先做一张圆形底图上传到Antfu，注意不断调节Margin值，保证二维码完全落在圆内，但数值别过大，否则噪点增多。调好后手机先扫一下是否顺畅。

![](img/4b2062670c783662466f9aa28d5a18de.png)

![](img/6aace0dd1893f8b0ee911165e824e424.png)

生成后照旧丢进SD渲染。

### 4、二维码修复技巧

有时候抽到一张非常惊艳的图，却扫不出来怎么办？Antfu有个隐藏功能可以救场。

进入网址/插件页面选择Compare，把生成的艺术图和原二维码分别导入

![](img/c0aa6a7a1455bf8ecfc4d5139991bfd6.png)

![](img/5e5bb6f1b097097c9fed965dd61d5594.png)

系统会对比两张图，找出像素不匹配的地方。图像难扫通常是因为对比度不足或点阵错位。鼠标悬停在Highlight Mistmatch上可高亮不匹配点，点击Preview Correction可预览修复效果，点击Download可下载修复后图片。下方还有微调参数，可在不大幅改动画面的前提下提升可扫率

![](img/ebe5416a3c207a51d1055da4d487f2e4.png)

# 三、收尾提醒

艺术二维码自带引流属性，各大平台审核比较严，公域发图建议关键信息做遮挡，避免限流。除了线上，线下企业对定制需求也很大，二维码+行业结合的方向值得深挖。

AI绘画迭代极快，玩法也在不断更新。未来一定会有更隐蔽、更精致的二维码玩法出现，拭目以待。有新发现我也会持续更新本文。

所需资料链接：https://pan.baidu.com/s/1ccWsMn16E8kcBYBzC5hpJQ?pwd=56t7

提取码：56t7

ADetailer安装教程

二维码提示词汇总