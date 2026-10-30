# 1分钟就能做出AI艺术二维码，新手也能上手（实操贴）

> 来源：[https://tjqtxsd47u.feishu.cn/docx/Y2mYd0L9dooiGQxxz8gcdskwneb](https://tjqtxsd47u.feishu.cn/docx/Y2mYd0L9dooiGQxxz8gcdskwneb)

嗨，大家好，我是火星人。

最近在AI玩家圈子里流传的一个案例挺炸裂，有位朋友靠一张定制艺术二维码就到手了2万块收入。

就是下面这张图

![](img/c2c0a200f2a4c0cb31ca3cfd1258b508.png)

（PS：现在扫不到是因为我把关键区域做了马赛克处理，真实版本是可以正常识别的，像下面这样）

![](img/e27ad4af1aeb34fded8bb285fa6ecd53.png)

我在另一个微信群里也捕捉到真实需求了：

![](img/fb98e4e4ef68eef4608e789677f36e13.png)

相信不少人最近刷到过类似内容。艺术二维码不只是好看这一个优点，它的赚钱方式其实挺多的，我帮大家梳理了下常见的几种玩法：

1、做教学类内容，教别人怎么做出效果，卖教程和工具的往往最赚钱
2、给自己的个人IP做专属艺术二维码，用来在某音、某红书做导流，还能绕过平台的检测机制
3、接私人定制单，开个小店，现在某宝、某咸鱼上已经有不少人在接了
4、为各类周边做视觉升级，比如帆布袋、纸杯、背包等产品上的二维码
5、把做出来的作品丢到各个微信群里做引流，吸引对这块感兴趣的人主动找你
6、如果有一定技术积累的，可以把流程封装成模型，提供一键生成服务，收点卡费

......

还有更多变现思路，欢迎大家在评论区补充！

说回正题，怎么快速做出AI艺术二维码？

最传统的做法是借助 quickqr.art 搭配 discord 来完成，这条路老玩家都知道，需要科学上网，操作起来对新手来说有点绕。

好在国内已经有同行把模型本地化了，直接给了傻瓜式入口，目前我实测在用的有这三家：

1：https://hysli.io/#/app?i=9n6sd7
2：https://qr.zzfw.cc/draw
3：https://qr.mewx.art/?invite_code=jsxgyhGR

综合体验来看，第一家功能最全、性价比最高，我就拿它来做手把手演示了。

## 第一步：进入站点

## https://hysli.io/#/app?i=9n6sd7

![](img/7018b82656352da42092cede91d0ae70.png)

点开【立即生成】后，左上角会弹出【立即登录】入口

![](img/8a72beb922d0600c1118d4b3b2c44137.png)

点【立即登录】-【新用户注册】，填手机号收验证码即可

![](img/52590d6a4baf099caaba08df4727834d.png)

注册完后进入主界面

![](img/f2bf8ae19c4e30b3ee39e6e036c4f13e.png)

## 第二步：准备素材

参照上图，界面主要分这几块：

*   左上角【原始二维码】是用来上传你自己的源二维码，比如微信收款码、个人名片码等
*   左下角的【绘画】区域有两种操作方式

### 方式一，直接用站内的现成模板

模板分普通版和高级版

![](img/e6836858b4e2606f69d824260940beae.png)

*   普通模板，一张大概10点，几毛钱一张，新手福利是送400点，价格很香，但效果一眼就能看出是二维码，模型比较基础
*   高级模板，一张要100点，价格贵不少，但画面质感明显更好，目前只有3个高级模板，后续会持续更新

是我自己生成的样例：

![](img/e74b467d4908ec35125b25d691a37b2b.png)

### 方式二，点【自由创作】输入自己的提示词

这里也要先选引擎，普通引擎出图更像传统二维码，高级引擎则更偏艺术化

![](img/e8c0f1b4947985d72553ff2a740682ea.png)

这一步就看大家的调参功力了，多试几次总能找到满意的效果。友情提示：每次尝试都会扣点。

我抛一段我用过的提示词，以及对应成片：

([balloons:Small planets:0.5]:1.4), (Small_planets inside of balloons:1.4), (lots of colorful Small_planets:1.35) (colorful planets, earth, floating petals, big balloons:1.22), 1 girl, cute face, Full body, sitting, detailed beautiful eyes, costume combination, Goddess, perfect body, [nsfw:0.88] (sitting on ice_planet:1.22) (lots of [floting blue Butterflies:floting ice:0.4]:1.22) (detailed light), (an extremely delicate and beautiful), volume light, best shadow,cinematic lighting, Depth of field, dynamic angle, Oily skin,

![](img/de502670570aae40673ff84aaf91dcab.png)

提示词可以直接写中文，系统会自动转成英文处理。

## 第三步：开始生成

点生成前，注意底部【二维码强调程度】的滑块。往左拉，画面更艺术但可能扫不了；往右拉，可识别性高但画面会变丑，需要找个中间值。

![](img/f654afe5a81fc35c8f1b961c436f1d76.png)

我个人常用60-70之间，如果60扫不出就试65、70，还是不行建议换提示词，别盲目重复刷，每刷一次都扣点。

准备好后点【开始绘制】，大概等一分钟左右就能出图。

我用普通引擎和高級引擎各做了一张对比：

普通引擎的成果

![](img/98966d8453319e2f251a6b8bf4d7a5aa.png)

高级引擎的成果

![](img/ddc64f39d75972a96c1cbe2b1eb73035.png)

差距是不是很明显

不满意就点【重新绘制】，再试一次。

再放几张我觉得做得比较顺眼的作品：

![](img/09de01cf1e86578997b130077beccf5e.png)

![](img/fb244af06c3192a8240fc727cae91884.png)

最后附一张充值价格的截图，个人感觉门槛不高，还算友好

![](img/87851057c50946d58afeee29becbcea3.png)

免责声明：我和该网站没有任何合作关系，只是单纯觉得好用才推荐给大家！