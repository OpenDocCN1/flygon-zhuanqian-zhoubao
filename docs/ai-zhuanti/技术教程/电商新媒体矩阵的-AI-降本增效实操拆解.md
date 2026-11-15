# 电商新媒体矩阵的 AI 降本增效实操拆解

大家好，我是龙哥。

自从各类生成式工具相继上线，我的团队便会优先挑那些上手快、实战感强的应用，迅速结合电商业务落地。今天就把这套在抖音、小红书等平台跑通的经验完整拆开，希望你能直接套用到自己负责的板块，真正实现降本提效。

# AI 助力引流：让抖音/小红书/快手二维码无感触达私域

别怀疑，扫一下就知道

![](img/zhuanqian_ab0d5f3f786f5a5af161445256b58ada.png)

![](img/zhuanqian_203a7a636993a6657c990fcf7d56a8d1.png)

抖音/小红书/快手/微信等渠道——隐蔽投放二维码

## 规避拦截的思路

直接发布裸二维码会被平台判定违规。核心在于让图像识别模型看不出画面里藏着可扫码结构，从而完成私域导流。

这种手法，LSP、黑五以及莆田系团队早已熟悉其威力。

## 解析原始码址，再用 antfu 重构

为何不能沿用现成二维码？两点原因：

1、网上的现成码点阵往往不连续，送进 AI 绘制时必须在美观与可读之间取舍，要么无法识别，要么颜值低。

2、平台自带二维码如微信公众号，原信息量庞大，结构复杂。

实测显示，链接超过 50 个字母数字后，艺术化二维码的扫描成功率会急剧下滑。所以必须自行重建，而非照搬。

### 第一步：

把自有二维码上传至草料二维码 https://cli.im/ 进行解码

![](img/zhuanqian_5c0f3a9bca2d3697acb4ef66281f67ae.png)

上传后可获得解析出的短网址：

![](img/zhuanqian_1a9a30251a2e664daf84d4423bafa9a9.png)

### 第二步：

打开 https://qrcode.antfu.me/ 依据常用参数生成新码

![](img/zhuanqian_28d411bad38006d9f3f796ee9923cf63.png)

### 第三步：模型准备

#### 启动 Stable Diffusion，主模型选用麦橘 V6

![](img/zhuanqian_a6470da1140ff3dba58a8ff6e4e705db.png)

除主模型外，还需搭配两套 ControlNet

CN Brightness:https://huggingface.co/ViscoseBean/control_v1p_sd15_brightness/tree/main

CN QRMonster:https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster/tree/main

将两套模型放入 SD 主目录 /extensions\sd-webui-controlnet\models 文件夹下，切记同时下载 ckpt/safetensor 与 yaml 配置。

### 第四步：绘图

先从简易的正反向提示词入手，稳定后逐步丰富：

正向：（photographic equipment），3d， Knolling，masterpiece， The best quality， ultra-high definition，extreme detail，8k，

反向：pale skin，（worst quality， low quality， normal quality:1.4），（inaccurate limb:1.2），white background，simple

![](img/zhuanqian_5dce9de8e600347cb69882ca2227c95c.png)

### 第五步：

启用两层 ControlNet 控制，分别使用 QRMonster 与 Brightness

![](img/zhuanqian_6396f851150187dd342c0f1ac837a548.png)

权重建议调至 1.4，经多次实验，过高则艺术感下降，过低则扫码失败！！！！！

若想提升艺术度，可缩短 CN 干预时长，例如将 Ending 设为 70% 时停止。

![](img/zhuanqian_a859968e4061f33ed0b4d0a2d3e7a455.png)

第二层选用 Brightness，它能强化二维码可识别区与边缘的清晰度，提升扫描率，但会牺牲部分艺术性。

因此仅在中间阶段介入，选取 60% - 80% 时间段控制。

### 第六步：生成与校验

点生成后检查图片是否可正常扫描，连续 10 张均失败则回溯检查参数。

如果只是单纯美化，也有小程序可付费制作，但实测这类工具生成的码无法绕过平台拦截，像这样

# AI 生成爆款短视频标题：ChatGPT/Claude 量产钩子

在星球里大家常问如何用 AI 制作 3 秒钩子或标题，今天以标题为例演示实操。

## 登录你的账号

若未使用过生成式 AI 或不便🪜，可用同事搭建的 gpt.pcbso.com 免费体验。

Prompt：

你是一名非常专业的电商运营，现在需要你根据我给的爆款短视频标题，来帮我改写出更多的标题，请注意有以下几个需要注意的：

1.不能有绝对化词语

2.要吸引人，让读者看完标题 想了解更多内容

3.每次生成 20 个让我选择，不要有其他的解释

4.我的产品是 XXX，结合我的产品来创作

爆款参考：

1."新婚之夜，34 岁老公突然提出不寻常的要求，我泪流满面，却瞒着所有人"

2."我 26 岁，大学教授悄然约我晚修，结果他的一句话让我瞬间惊愕"

3."我 38 岁，只身一人前往山区教书，不料晚上山里有个陌生男人敲我门"

4."我的丈夫去外地打工，我被婆婆强迫做她一件无法接受的事情"

5."40 岁离婚的我，租住在农村，房东老汉每天晚上都会来敲我的门"

6."我 35 岁，每晚都要应付隔壁老王的夜袭，我的人生像是一部廉价的小说"

![](img/zhuanqian_fe4446bba7ea8e418e3900d54d47affc.png)

其中的爆款案例与第四条里的 XXX 需替换为你自家内容，每个品类对爆款的定义不同，取同行近期最火的几条即可。

最需要掌握 ChatGPT 的是所有线上内容生产者，而围绕 GPT 的教学，其目标人群是创作者而非普通用户。

可以把 GPT 看作一个 3 岁神童，知识储备很浅，但学习极快，几千字内容瞬间就能吸收。因此它可以成为我们 24 小时在线、任劳任怨、一教即会的天才助手。

# AI 做短视频：改写+剪映智能成片

该方法不适用于全部品类，带货口播类不适用，知识科普、口播、EMO 风格适配度高

![](img/zhuanqian_5282374c00a303fd73e94fa90fe35734.png)

以知乎上一篇爆文为例，先用 GPT 改写

不难看出，GPT 重写后每句话都换了表述，整体主线保留，已达原创水准

![](img/zhuanqian_5676d22c82f2464425bed72bed576357.png)

打开剪映升级到最新版本，点击文字成片入口

![](img/zhuanqian_b8a494a280d30db2b73cf79d5b3e9603.png)

进入生成视频，再点智能匹配素材

![](img/zhuanqian_c54b67c797afa76a4d16cb4ea1328f58.png)

![](img/zhuanqian_43f1424b09910806a0de101bdf82d9b9.png)

几分钟即可得到成片，若觉得此类内容不爆，可参考抖音账号：emo 乌托羊

视频已发布到抖音，可自行观看测试！

# AI 制作直播间背景：MJ/SD 美工方案

我们常做无人或半无人直播，背景需随产品变化，这里演示最近用 MJ 制作直播背景的做法

未使用过 MJ 的可用 #小程序：//闪电炼丹/GcBWjvOM8FPKduc 体验，无需魔法微信小程序即可

本次要搭建高端口红专柜促销场景，需要商场化妆品柜台装修考究，画面中无人物，档次感强，口红明显，竖版，高清

依据需求写 MJ 关键词 prompt：China's high-end shopping mall， lipstick counter， luxurious decoration， bright light --no people --ar 9:16 --s 250 --v 5.2

约 30 秒即可获得 4 张质感强的场景图

![](img/zhuanqian_4f945d494215a914c6d7981ff4ff5f45.png)

挑选我认为最契合的第一张放大展示

![](img/zhuanqian_57144e1f2bd212391aebbde1cb06c6c6.png)

同理可生成服装卖场、生鲜区、玩具区、采茶基地等任何能用语言描述的直播场景。

![](img/zhuanqian_3b4ff2d4d7b80ffdb807b7eaf515fc72.png)

到此，AI 已帮助我们完成了抖音等电商新媒体平台的 4 项核心工作，后续更多用法我会持续分享，欢迎与我取得联系，

姓名：陈思成

联系方式：你想，你细想... 第一部分的内容里，我留了不少二维码。

# 5.彩蛋

觉得有用，看完记得给小弟点个赞～感谢！！！