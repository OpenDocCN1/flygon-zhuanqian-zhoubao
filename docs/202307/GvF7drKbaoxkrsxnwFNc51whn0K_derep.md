# 十几分钟上手AI绘图，用Stable Diffusion做出流光出片效果

> 来源：[https://vchmk6v2g8.feishu.cn/docx/GvF7drKbaoxkrsxnwFNc51whn0K](https://vchmk6v2g8.feishu.cn/docx/GvF7drKbaoxkrsxnwFNc51whn0K)

最近那种光影感十足的SD作品在网上到处都是，相关的教学帖也铺天盖地。可惜绝大多数教程都直接一句“用Stable Diffusion就能做”，却不讲从零开始怎么跑起来。

现实是，对大部分人来说，本机根本跑不动SD，配置门槛卡死了一大片，于是连第一步都迈不出去，后面的技巧也无从谈起。

我把流程拆到最简，今天就带你用最省事的方式，五分钟内把SD跑起来，开箱即用，不用折腾下载模型，十块钱就能玩很久。

本篇会先讲怎么快速启动Stable Diffusion，再带你复刻那种流光隐藏图的效果。

![](img/73cf4fc4e31ee81aca56eb4d72495466.png)

![](img/ed0ea982636f6f8ecd8294d2b27110f1.png)

![](img/20b6761cc5ef81357ed77a926214b520.png)

![](img/d3154d74b508266b5a1964b65bbd24a0.png)

![](img/3960373bba0e0ffc9ff669d7cbd17d62.png)

![](img/ec1bf81811f9874e9e509cdd4d631976.png)

以上几张算是演示稿，还没做到极致精细，但都是可以继续调优的。我自己前期光调参和试图就花了大量时间，所以出图部分就停留在能用的阶段，有追求的朋友可以自行深度打磨。

## 第一步：注册青椒云

建议直接下APP，方便下次快速登录。

https://www.qingjiaocloud.com

注册后实名认证，流程就不多赘述。认证完进入服务器购买页，优先选自带镜像的机型，比如“小李子”镜像。

充值10元按小时计费即可，用完记得关机不扣费，10块钱能续航很久。

如果小李子没库存，其他带SD镜像的服务器也可以，用起来一样。

核心是机器自带启动器和基础模型就行了，其他配置不重要！！！！！！

![](img/44d939a1e69b5b8337fc5a709a3d0097.png)

下载完镜像后，我们以桌面端为例，点击开机。开机后进入系统桌面，找到 A启动器.exe 图标，双击打开。

![](img/e6e09041b7724de519387e684fe7e517.png)

![](img/358458d71136060b73e8885cdd62fc6e.png)

注：如果界面默认全屏导致操作不便，将鼠标移到屏幕中间位置，点击取消全屏即可。

![](img/f5f357bab68093c59ef796605a214e16.png)

![](img/ded2e43114d47ff8ea944eadde5d0da1.png)

继续下一步。

进入青椒云后打开SD客户端，点击启动会弹出更新提示，先等更新完成。更新完再统一更新所有插件，保持版本和教程一致。

一定要点一键更新。启动界面和我不一样，多半就是没更新。

更新完毕后，点击启动器执行一键启动，首次启动大概需要3到5分钟，耐心等待。

![](img/9a93d77e3f63429b2a7e2fc5d1d4044d.png)

![](img/36ec420ae155b8bb6b805ab42a877790.png)

![](img/9ef438face3906985b85007f8eec5da5.png)

![](img/7d95c472921ddbbb5724bed4312ad235.png)

等待启动的空档，我们可以提前准备模型。

注：我放在夸克网盘里有两个较新的大模型，画质提升明显，建议换上，能很好改善手部细节。

大模型存放路径：C:\stable-diffusion-webui\models\Stable-diffusion

夸克链接：https://pan.quark.cn/s/072d110f012f

百度链接：https://pan.baidu.com/s/1m5fYOpR1bs0PSA7z-m71Ew?pwd=7mui

阿里网盘分享不稳定，建议用夸克，速度不会只有100k。

![](img/89e5854354ffced2c69b36958c04b60d.png)

这个模型是强烈建议更换的，其它模型属于进阶玩法，可装可不装。

![](img/39f3d96c02ec3dfe2ba90780237f16cb.png)

下载完以后，把文件放到对应目录即可。用同一镜像的同学直接用完整路径。

在系统任务栏粘贴以下地址回车，然后把下载好的模型拖进去。

完整路径：C:\stable-diffusion-webui\extensions\sd-webui-controlnet\models

相对路径：你的stable-diffusion目录\extensions\sd-webui-controlnet\models

![](img/609d660768667dc6642bfc9642c0578e.png)

准备工作做完，SD基本就启动完成了。

默认会自动打开浏览器，你会看到一个熟悉的WebUI界面。

如果和我的不一样，基本可以确定是插件没更新完全。

这就是后续出图的操控面板。

![](img/0e770f31d491f18fb956ec5c8b1c4e75.png)

这里可以像我一样先切换模型，再把咒语粘贴进去使用。

![](img/bd9d8ee81385991dd83904a190f4c6c7.png)

## 出图咒语参考

不少人不会写提示词，这里给你一套可直接用的基础咒语，参数自需微调。

(8k, best quality, masterpiece, ultra highres:1.2),1girl

Negative prompt: (worst quality:2.0), watermark, paintings, sketches,(worst quality:2), (low quality:2) ,lowres, ((bad anatomy)), ((bad hands)), text, missing finger, extra digits, fewer digits, blurry, ((mutated hands and fingers)), (poorly drawn face), ((mutation)), ((deformed face)), (ugly), ((bad proportions)), ((extra limbs)), extra face, (double head), (extra head), ((extra feet)), monster, logo, cropped, worst quality, jpeg, humpbacked, long body, long neck, ((jpeg artifacts)), deleted, ((censored)), ((bad aesthetic)), (mosaic censoring, bar censor, blur censor),skin spot, ((monochrome)), ((grayscale)), accesory,(cropped), text, logo

Steps: 20, Size: 512x768, Seed: 297525418, Model: majicmixRealistic_v5, Version: v1.3.1, Sampler: DPM++ SDE Karras, CFG scale: 7, Model hash: 33c9f6dfcb

复制后直接导入SD即可使用。

![](img/f3335644b1f828b1ac7aeb3b00f7fe5c.png)

![](img/fadb0215924cb55ab94180bc59bdfa77.png)

![](img/c8810629f6e85340dba563da789823de.png)

ControlNet 的配置要点我已标注，重点部分都圈出来了。

![](img/4877eefd83b4e717280848eb71a0615b.png)

最终我使用的完整参数，关闭高清修复版。

![](img/84a08b9715e772e10c3775765700bd04.png)

![](img/7f50f5040344193d4b1f1679406b1b54.png)

如果对速度更敏感，可以直接关闭高清修复，生成速度能快一倍。

新手第一次体验建议先不开高清修复，避免等待时间过长。

生成的图片默认保存在：C:\stable-diffusion-webui\outputs\txt2img-images

也可以在SD界面下方点击文件夹图标直接打开。

底图部分需要你用PS提前做好，操作并不复杂。

注意字体要选用无版权字体，字重建议偏粗。

例如宋体，或参考这两个字体站：https://www.100font.com/thread-331.htm，https://www.100font.com/thread-233.htm

PS制作好的底图可以直接粘贴上传到青椒云使用。

![](img/b203acdce38996f8acc375cbedd1b94e.png)

![](img/afc2e7c7a2df6075ebb3969aaf3c85f7.png)

![](img/a82b04d4e77c03c37a11ce3bed3a046e.png)

![](img/804f2310114b8a8f5ff3c9d9c2b5a979.png)

![](img/d2c8a3b49d73e0f555231a44ac246cbe.png)

![](img/2bef44808a8beb25a761f7eaab01d298.png)

![](img/7bdc4efd74ddb1a64df157012db9e224.png)

## 提示词小技巧

正向提示词可以直接在插件栏输入，输入中文回车后会自动翻译成英文，非常省事。

![](img/950efc5f07f501b4ec7704c8dfd0820b.png)

用完青椒云一定要记得关机，关机后才不计费，所以十块钱真的能玩很久。

![](img/fee9ba0d2561cf930a1200f7391edbe5.png)

本教程在思路上参考了淘金之路@黛色翩翩提供的青椒云入门教程，光影制作部分则感谢@千穹的分享。

我看到圈内有朋友说这个光影教程是我原创，其实并非如此，是千穹提供的思路，我只是整理后让更多人可以看到。

信息本身不值钱，但能把有效方法整理清楚，就能帮到更多人。

本文首发于淘金之路，由侠狼编辑，转载搬运请联系侠狼。