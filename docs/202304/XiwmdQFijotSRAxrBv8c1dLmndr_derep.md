# 用 SD 一把梭，小红书爆款头像壁纸批量刷屏的极简打法



要问小红书 3 月份最卷、最火的头像壁纸题材是什么？

答案就是那波「流光女孩」。

先感受下这套模型出来的质感。

![](img/ac9fc3740b4bcd6119808197fd0e2348.png)

![](img/07b00f763584bafc4f341de9f0cc5d9d.png)

![](img/347f39ab7377b39e0b7a5cb2f30fddbf.png)

![](img/bd817ca618cc0bd1e25204bd801c9c25.png)

是不是又潮又上镜、让人忍不住保存？

小红书本身就是女性用户为主阵地，这类壁纸头像的吸粉和转化效率，真的离谱。

## 爆款背后的变现逻辑

拿 3 月 15 日发布的笔记举例，博主 子鱼哎吖 首发后不到一个月，粉丝冲到 1.7 万，点赞收藏破 5.1 万。

![](img/ee2f0093929a40b02b9e26acc89c4d4b.png)

她的赚钱方式很清晰，

1：卖知识付费
2：接私人高配定制
3：小红书店铺直接卖图

![](img/e48852b583972d5240b20d1206bef805.png)

店铺里销量排名第二的猫耳少女单品，累计流水 418.6 元。私下聊了下，博主的月收入已经稳定过万。

更狠的是另一位创作者橘鹿，上线 3 天涨粉 2 万。

![](img/1c4729147f3057dcb8f004d7314626a3.png)

他的套路更完整：

开了 3 个付费社群，还做垂直穿搭教程。按他的说法，月入已经是 6 位数了。

![](img/2326b3e1ff12f9e046d7e9c3f9291b52.png)

## 小程序画图，为什么创作者都在跑路

这些小姐姐图基本都靠小程序 AI 画出来，看着方便，坑却不少。

### 1：等图等到怀疑人生
非会员要排队，单张 5 分钟起步。最夸张的一次等了 45 分钟，直接劝退。

![](img/406af434036bc2b4b3303e46a683f98d.png)

![](img/c39814fdcb590d4793ff9f0dd8685299.png)

### 2：产量被锁死
不充钱每天只能画 5 张左右，想批量根本不现实。

### 3：时间成本拉满
一天要发 20 条笔记，每张 5 分钟，算下来就要 1 小时 40 分钟。做头像号的人基本全天都在等图。

![](img/c7492acb2762adf9c4a5445356efc02d.png)

那有没有又快又省钱的办法？

折腾一段时间后，我找到了一套不挑电脑、成本极低的云端方案。

## 核心思路：花小钱上 24G 显存的云端 SD

这次的主角是 Stable Diffusion，2022 年开源的文本生成图像模型。说人话就是：你打字描述，它给你画图。

本地部署太折腾，Python、Git、环境配置一堆坑，还要看显卡。6G 显存跑 20 张高清图要 45 分钟，4090 24G 要上万，整套主机直奔 3 万。

我们要的就是用几块钱的体验价，享受 24G 显存的云端算力。

## 四步搞定云端 Stable Diffusion

整体就 4 步：

1：注册平台
2：上传绘画模型
3：一键部署 SD WebUI
4：批量出图

![](img/3934bdd3a717e0b93e7336d805297ad5.png)

# 一：注册平台

注册地址：https://www.lanrui-ai.com/register?invitation_code=4106

注册填邀请码 4106，关注公众号【揽睿星舟】后扫码领客服福利金。不要时长的话，关注这一步可以跳过。

### 2：创建工作空间
进控制台

![](img/a33b7f2fe5b94ba6c6268a2d19023d47.png)

![](img/312fe5c3573334d9bd5a36f18438d783.png)

现在平台在促销，3090-24G 只需 1.9 元/小时。

![](img/35bcfb8b13072b14815d452796ac33c8.png)

点使用后，实例名随意。运行环境选 公有镜像 / others / sd-webui-2.0 / v3

数据集选 sd-base

![](img/c4abca02a0045c1bce9da0659683feab.png)

等实例状态变成运行中，进入 Jupyter 执行下面命令。

![](img/93cebb3d50f42bf54a3791d649e3967d.png)

![](img/402765e177e5425eaf03a1fd9efb2a11.png)

![](img/5e917df01f388458a51aa3d0f94855ba.png)

// Some code

cd /app

bash start.sh

![](img/5aa514afad4a27d981e393a70b580fb9.png)

然后在实例-操作栏复制调试地址，浏览器打开就是 SD WebUI 了。云服务按小时计费，2 块钱起，千万别频繁开关，反而浪费钱。

![](img/572d989b807f619925f1c0fd53b57ee2.png)

复制调试地址新建网页，就能进入 SD 的 WebUI 界面了。

# 二：上传制图模型

第一次启动，先执行第三步 创建应用，这样文件夹才会显示。

这次用更省心的方式传模型，用网盘上传下载。

以 Windows 为例，装一个 Cyberduck。装好后桌面不显示图标，去开始菜单搜一下。

![](img/0365303979ff516d24887f21abe27f3d.png)

![](img/39b2a55689e641751e085a7939fa87ec.png)

新建链接，点更多选项

![](img/11f65351adf8fb4474071018d707489d.png)

找到 AWS PrivateLink for Amazon S3 并勾选

![](img/e7f3afa3182acdc31f1a4dd1df6a53a9.png)

关闭后回到首页再新建链接

![](img/ebdb7ca3deb10cc7d7406ae1c43f25cc.png)

服务器地址：官网左侧点网盘→命令行，把命令行里 HTTPS:// 后面的那串复制过来

![](img/c89ffcf6cfe6c98c281f3cd348ca45a6.png)

访问密钥和私钥在官网头像下方设置里

![](img/b6d4d4415e993b9c7b9c0dec0522aa72.png)

把 AK SK 填成账号密码

![](img/bc7fb5755f591abd3335ac69a2b60fd6.png)

搞定后就像用百度网盘一样拖拽上传下载，不用再敲命令行了。

![](img/a7edc46ae28ae124eb2403db03f0906c.png)

## 上传制图模型

本次用的大模型：YesMix-V1.5.safetensors
LoRA 皮肤：fashionGirl_v50.safetensors

YesMix-V1.5.safetensors 下载地址

fashionGirl_v50.safetensors 下载地址

YesMix-V1.5.safetensors 放到 models/stable-diffusion 文件夹

![](img/0ce98d05ae588f9705742ed9047853d3.png)

fashionGirl_v50.safetensors 放到 models/lora 文件夹

![](img/c9343c26c019d970b88001b8799256ce.png)

# 四：生成图片

设置里 stable diffusion → SD VAE 选择 None

VAE 就相当于滤镜，先不用。

![](img/3690cf4994f2608aac57c8e4d7285fd9.png)

模型选 yesmix，TAG 里加上 < lora:fashionGirl_v50:1>，记得把前面的空格删掉

![](img/a58efdaa8b83f16b92d0c1e898382650.png)

想复刻文章开头那种流光效果，可以直接用参考图。

原图下载链接

![](img/f19082d778970b3c8f6966fe179c739f.png)

把原图丢进 png info，点 send to txt2img 就能一键套用风格。

如果这套极简流程对你有用，给个免费赞支持一下，谢谢！