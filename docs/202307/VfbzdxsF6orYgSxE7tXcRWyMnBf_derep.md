# 《爆肝7天！AI创意字终极攻略，光影、隐藏、嵌入、海报4种创意字全拆解！》

爆肝7天，我总算把AI创意字的4种玩法摸透了：光影、隐藏、嵌入、海报，一篇讲完

大家好，我是吴东子。

AIGC迭代越来越快，AI创意字这阵风也吹得越来越猛。我干脆闭关一周，把所有主流玩法从头到尾试了一遍，最后沉淀出一套傻瓜式流程。只要跟着“基础图→大模型→提示词→ControlNet”这个顺序走，上面的效果你也能做出来。需要用到的模型文件，我都打包在文末网盘了，不用自己翻遍全网找。

先看成品：

海报字，干净背景版：![](img/5d5ee8772863386aa058fb87fec9ea7f.png)![](img/2f3dfbc51b309b067b48a8c22d8c81f4.png)
海报字，场景背景版：![](img/3ae9fb12ada025dd22c966fa8655d559.png)![](img/ac2af7846a0d4a13b06ef089a04844d8.png)

嵌入字，文字直接“长”进环境里：![](img/10867627dab6367f000838d401a97452.png)![](img/216ab240e48d4618c0dc8a23e6847079.png)

隐藏字，左边“东子真帅”，中间“东子666”，右边“wudongzi”，缩小时文字清晰可见，放大后画面又很自然：![](img/f3c6379f68f7e2526e78b1696af89a46.png)![](img/e1435ed67ff96a27f364c36333e3ee83.png)![](img/536208f6cbec37c8f97e8816cf47e661.png)

光影字，直接写出“无敌”两个字的光效：![](img/1903d4872a4aba8a4eb801033f816e34.png)![](img/42af73ed428b2003b611a0342d346863.png)

下面，我先讲做图前必须搞定的通用环节。

### 准备一：做基础图

不需要专业软件，PS、美图秀秀甚至网页在线工具都行。核心就一句话：做一张白底黑字，或者黑底白字的图片。

怎么选？海报字和嵌入字用白底黑字；隐藏字和光影字用黑底白字。

拿美图秀秀举例：
1. 打开App，进“图片美化”模块：![](img/430379a2538808fcc8d971b592f98620.png)
2. 点右上角“制作壁纸”入口：![](img/6e4e8375144cd2397fa11b481a376437.png)
3. 在底部选背景色，本文只需要白、黑两色，选完点“下一步”：![](img/32cc2652a1b90e1161d4455e929205ba.png)
4. 在下方工具栏里裁剪尺寸，之后点“文字”输入内容：![](img/2bd0005e33ba5b08c756c2ed5ee5f3cf.png)
5. 在文字面板里改字体、颜色，用双指缩放调整大小：![](img/d68894999029d48c620162f55443c7f7.png)

这张底图决定了文字的最终位置和大小。比如做蛋糕、面包这类带“食物感”的文字，建议加粗字体，生成后更有立体感：![](img/6280c8a40473936ca88644eb71607cd8.png)

### 准备二：挑大模型

底图搞定，进Stable Diffusion换一个写实大模型。我实测比较靠谱的有：revAnimated、realisticVision、chilloutmix、majicmixRealistic、deliberate。

出真人图，用majicmixRealistic或chilloutmix；其他类型，优先revAnimated、realisticVision、deliberate。![](img/b0dfcb1733d33bd995df87bd4a196516.png)

没有绝对“最正确”的模型，同一组词配不同模型，效果可能完全不同。效果不好就换一个重试。

### 玩法一：海报文字

海报字有两种形态：纯文字版和背景版。

纯文字版：![](img/da3fbdeada8e05224e8a758e99b8c74a.png)![](img/0e726464896cd80a07db0410ba891db5.png)
背景版：![](img/b19895bb5be1607c33b4a0312da899cb.png)![](img/60b8bedc87fc3b265bbda4fe986fe7b0.png)

本质操作一样。纯文字版方便后面抠图，做海报、做字体设计都好用；背景版是直出效果，文字和环境天然融合。

操作路径：
- 基础图：准备白底黑字图。![](img/771d7bd035bcd87712dfeffc6ab8a8f3.png)
- 大模型：按上文思路选。![](img/14c17d1d0a327863ff6d3929073b2d97.png)
- 提示词：想生成“蛋糕”两个字，就在提示词里写上面料元素，比如蛋糕、奶油、巧克力、水果；再加“简单背景”“纯色背景”这类词。![](img/3c7281a2c918e8e2d525ef3ab53d317a.png)
- 采样参数：我习惯用30步+DPM++ SDE Karras。你也可以自己调，会有不同风味。![](img/322fa993081e7a9e2ae3cf6af446cd04.png)
- ControlNet：把底图传进去，预处理器选invert，模型选depth。![](img/b3423416a63b26b5c65d66efa41c5547.png)
- 点生成，完成：![](img/dfcb9d574c46ee01c9b574694b83369b.png)

小技巧：想做出奶油/液体飞溅效果，改用canny、lineart、softedg、scribble这些线稿模型，同时把ControlNet权重降低到0.6~0.8，液体感会更强。![](img/20ce4bb821acb644a182eac181f56cdc.png)![](img/3e5f81c37ab87f6a9ae82998d6cea8ae.png)

### 玩法二：嵌入文字

嵌入字的核心是“让文字融入场景”，在合理与不合理之间制造视觉趣味。![](img/cd7650fcda7e882ce790a09717380291.png)![](img/610e3e9bdf1a3439be4484409fb6dadf.png)

- 基础图：白底黑字。![](img/10fbf90e3d5d61ef994d619227346166.png)
- 大模型：同上，按场景类型选。![](img/a01a81bece8e420829fae61068acb03f.png)
- 提示词：多试！不同字配不同场景效果差很多。我跑图时发现“东子”跟“竹林、竹子、池塘、瀑布”凑一起特别出效果，于是就有了下面这组。![](img/dfc6d6f442663ec5c060eb28a21d8e27.png)
- ControlNet：用canny、lineart、softedg、scribble其中之一，实测canny和scribble最稳。权重保持在0.65~0.85，想文字更突出就调高一点。![](img/e58411a5ad231ff3b5a48b1618233243.png)
- 点生成，看结果：![](img/b7a10ef966d3ff2dba80ed73a497a2cc.png)![](img/85fb9561e871600db103040661d1e8eb.png)

### 玩法三：隐藏文字

隐藏字是把字“伪装”进场景，比如藏在建筑里、变成衣服纹理。![](img/b67e1c4b58d03871b6453513351b0c78.png)![](img/94e3a1b6a7ff879dfbda876e082f5546.png)![](img/f52708d3ba0b534732cc396690f181e5.png)

- 基础图：这轮要反过来用黑底白字。![](img/6f189b7f986c90b3f5a977b2c7950b20.png)
- 大模型：人物图用majicmixRealistic，人像质感好；建筑/风景用写实大模型即可。

提示词我试了两组，直接抄：

城市建筑：
Best quality, ultra high definition, masterpiece, ultimate details, 8K,
Urban night view, buildings, cars, headlights, streets, roads, water reflection
（高质量、超高清、杰作、极致细节、8K、城市夜景、建筑、汽车、车灯、街道、道路、水面反射）

人物：
The highest quality, masterpiece, ultimate detail,
1 girl, beautiful, full body, long skirt, standing with hands in pockets
（最高质量、杰作、极致细节、1个女孩、漂亮、全身、长裙、站着、双手插兜）

- ControlNet：需要一个新的controlnet模型，在网盘里下载，放到 sd目录\models\ControlNet 下。预处理器不需要选，直接选这个新模型。控制权重很关键，设在0.45~0.65之间；想让字更清晰就调高。![](img/a4a0409d42283422d7b8ae061e89c9c9.png)

出图后缩小看，字就显形了：“牛逼”“东子真帅”“东子666”。下次还可以做个“东子真不要脸”。![](img/99fabb6854e726161b23f5f63364f40a.png)![](img/d493796ccdf2bc4917a0a9e0b5a8b313.png)![](img/76ddfb3f78647c02e056a5e5a6338b5c.png)

用微信号做图也是这套方法，比如“wudongzi”（非真实微信号，仅做演示）。![](img/78cad911641aacfb464bf17e0c03914c.png)![](img/9e728aa39351dee1cf0b3c7aca6d5fb2.png)![](img/76acdc57be458e3a599931634e9ba49f.png)

### 玩法四：光影文字

光影字是把文字本身变成光源。![](img/a6908e404b3fdd467f9ec6b4373f32fa.png)![](img/1280bc33f564187ee681a2c367938eb3.png)![](img/4f045672eda30995f9c1bd8730b9308d.png)

- 基础图：黑底白字，文字占比可以适当放大。![](img/7ccf63330607e633d7f7b9c39e1d26bc.png)
- 大模型：选写实模型，比如majicRealistic或chilloutmix。![](img/055bcd50832969621979621b4f7aaedc.png)
- 提示词：先堆画质关键词，再写小姐姐的外形描述，最后补上“阳光”“光与阴影”“明暗对比”等词，并给这些词加一点权重。![](img/df7c496fb01bb575cc385643e412b690.png)
- ControlNet：用tile模型。重点记住两个数字——
  - 控制权重：0.35~0.55
  - 引导终止时间：0.7~1，越靠近1，字越清楚。
  
  参数没有标准答案，不同文字需要反复微调。![](img/e2a76d146c9bccec91c1d6754a9723a2.png)

生成一下，“牛逼！”的光影图就出来了：![](img/cb79b4d4e44eb56abed259f3226449b8.png)![](img/091e09864a720a9a4ff067081068216f.png)

### 变现方向

除了好玩，这四类玩法也能变成钱。总结四个方向：艺术设计、定制头像、定制祝福、引流方式。变现模式无非两种：提效和定制。

提效：
- 设计师以前做艺术字要开3D软件慢慢渲染，现在用SD几步搞定，时间成本直接降低，还能产生更大胆的设计。![](img/5ad761fcb80291a91ad41e843aae41fb.png)
- 团队做公域引流，可以在内容里植入创意字来规避平台检测，短期引流效率提升。不过平台迟早会升级检测，只能当阶段性红利。![](img/7c6a88e871eddee32f9509dd4ff69e89.png)

定制：
比如做定制头像，把客户名字或指定文字生成专属图片；做祝福图，把“XX生日快乐”变成创意礼物；做定制引流图，为客户批量产出带文字的营销素材。核心玩法就是公域做视频引流，私域承接成交。![](img/82fb0454cb53700896c3cce68671677a.png)

以上就是本文全部内容。对AI感兴趣的朋友，欢迎关注👸号“吴东子AI”，也可以把文章分享给身边想学AI的伙伴。之后我会继续更新实用的AI干货。

我是吴东子，用最通俗的大白话，讲最能落地的实操，下篇见。

网盘链接：https://pan.baidu.com/s/11p8zSDRs5XLgQPSqkcqe-Q?pwd=wdz6
提取码：wdz6

账号简介：https://ry5hwpuf7b.feishu.cn/wiki/space/7283841978071072772?ccm_open_type=lark_wiki_spaceLink