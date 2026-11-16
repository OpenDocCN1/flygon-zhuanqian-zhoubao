# 用 n8n 批量产出带货类视频：拆解热门短片 → 自动生成 → 直接发布
作者：龙哥

做开发的 00 后小宋，6 月进的赚钱，待到现在差不多有一个季度了。这期来交份 n8n 自动化相关的作业。这套方案主要解决一个问题：把高播放量的带货视频模板，做批量化的稳定翻制，然后自动推到可带货的渠道上。

核心做法是：先拆开热门视频的创意结构，再用多视角的 AI 能力分析画面内容；出图阶段用 Liblib 微调出的模型来保证精度；最后用 nano banana 固定商品外观，让带货视频能按统一标准输出。

公号里给的拆解如下

![](img/zhuanqian_0118ef9128b3ae2dbc20fcf50acdde61.png)

我的：

![](img/zhuanqian_4e7ee67f936d1a19f2a41f9a81d808ed.png)

给几个提醒：

第一，建议有一定基础的朋友入手，新手容易被大量节点绕晕；

第二，要兼顾可扩展性、操作友好度，以及自己训练专属模型的能力；

第三，当前整套流程大约三十几步，配音、字幕、画面特效模块还没接上去，要是全部加上，体量只多不少。

## 平台选型思路

### Liblib 是做什么的

Liblib 主攻 AI 绘图、模型微调、图像合成这几块，资源池很深。无论是直接拿现成模型用、在线出图，还是训练自己的专属模型，平台上的工具链基本都能覆盖。

### 为什么最终定了 Liblib

* LoRA 支持自定义训练，想做什么风格都能自己练出来

![](img/zhuanqian_0002ef17476dbad305846afc167c1c2e.png)

* ComfyUI 环境拿来即用，省掉本地部署的麻烦

![](img/zhuanqian_439d9ed9979969277dc13db3f46fe3fc.png)

* 垂直场景的模板存量非常大，几乎要什么有什么

![](img/zhuanqian_527e57a2d046cf2cf7ba26f197892f66.png)

* 商用授权没问题，不会卡项目落地

### 更省精力的替代路径

LiblibAI：把部署变成了图形化操作，浏览器里点几下环境就起来了，本地不用装任何东西。平台内置了大量现成的节点和模型，Stable Diffusion、Flux、ComfyUI 都可以在网页端直接跑。新用户注册还送 90 天免费 GPU 额度，把节点放进画布编排就能出图，门槛非常低。

RunningHub：专门照顾不写代码的用户。登录后挑一个模板，靠拖放操作就能把流程搭好，省去了安装程序和搭建环境这些杂事。开发环境不收钱，只有当任务真正跑动时才会产生费用，全程可视化，几乎不需要学习成本。

另外也可以直接买云服务器自己部署，灵活度更高。

### 模型怎么选：认准商用授权

![](img/zhuanqian_d1a55fe582aa80ab3abb715c4c75d0fc.png)

![](img/zhuanqian_b4934910e2a1a463e305660082f00a6a.png)

![](img/zhuanqian_48f4f3dd989a9bfa6791616877b691cd.png)

## 案例一 卖鞋：核心是商品不掉样

参考原片

加了 nano banana 之后生成的 v2.0 成片

下面是换掉鞋子后的效果

![](img/zhuanqian_0a667d5ca0eb93700e4485deeeeaf191.png)

Liblib 出的静态图

![](img/zhuanqian_7b95ccf7a99e8bffa441319fbb44f3b6.png)

用 nano banana 替换成自己实际要卖的货

![](img/zhuanqian_1210a66adcaaeeeafc501f47f9c6eb18.png)

成片效果：

## 案例二 广告特效：核心是抽卡不翻车

![](img/zhuanqian_7b50c29b23b851df1f962c260af57320.png)

```
替换的参数：
地址：https://www.liblib.art/modelinfo/d1a16bd086d9434596f7ce02bba697a9?from=feed&versionUuid=2dd07e9bca2d49d1a1d19d1b784ebfb3&rankExpId=RVIyX0wyI0VHMTEjRTE3X0wzI0VHMjUjRTM4
替换id: versionUuid=2dd07e9bca2d49d1a1d19d1b784ebfb3&rankExpId
替换提示词：Realistic style,close-up,fruit in water scene. Several red plums with clear texture of flesh and small water droplets attached to the surface. Li Zizheng randomly scattered in the water,creating a large amount of water splashes and bubbles. With a professional photography lens,a red background,depth of field,light and shadow,freshness,and bright colors,the overall picture has a sharp contrast and is full of dynamism.,
Negative prompt: ng_deepnegative_v1_75t,(badhandv4:1.2),EasyNegative,(worst quality:2),
Steps: 30,Size: 864x1536,Seed: -1,Model: F.1基础算法模型-哩布在线可运行, 生鲜水果拍摄-质感细腻,Sampler: Euler,useLcm: false,CFG scale: 3.5,Clip skip: undefined
```

这一步要解决的是抽卡随机性的问题，相当于把一套已经调好的 ComfyUI 固化下来，每次跑都稳定出同样的特效。

拿橘子来试：它的核心逻辑就是经过微调的模型效果确实不一样，第一眼看到结果的时候，我甚至有点恍惚。

图片链接：https://liblibai-tmp-image.liblib.cloud/img/8b6ed71855aa450693b01ffa1e9986d5/b6e577fd76f98aa9c96deec7b96ee8dc79f36be0b4c7d0819dfd77ee36523268.png

![](img/zhuanqian_ef94ecbe0a9a60c9ae6f903be802d8eb.png)

第二遍再跑，结果还是这么好，稳定得让人想笑。

![](img/zhuanqian_777a2e242dacc24d3bfd76b6c34d2963.png)

## 案例三 电商广告：小音箱

![](img/zhuanqian_85f0269eaa23dbb548d5d180d1d46eb8.png)

```
地址：https://www.liblib.art/modelinfo/6039fc219a1e4be595f00b2f9321aea0?from=feed&versionUuid=da22c2037c654610beba1c4d64ee7904
替换id：da22c2037c654610beba1c4d64ee7904
替换提示词：This is a high-definition photograph of a washing machine with extremely detailed features against a clean background from a side perspective.Future technology style,Blue Light,A washing machine stands in the center of the frame,softly illuminated by natural light from above,creating subtle shadows that enhance the three-dimensional appearance of the device. The focus is on the product,allowing for a clear view of the round rotary buttons and the details on the metal surface,as well as reflections on the glass door. Every detail is captured with exceptional clarity and precision.,
Negative prompt: ng_deepnegative_v1_75t,(badhandv4:1.2),EasyNegative,(worst quality:2),
Steps: 30,Size: 1024x1536,Seed: 2225014950,Model: F.1基础算法模型-哩布在线可运行, 【摸鱼】Flux超写实商业渲染_电商产品场景, FLUX-家电,Sampler: Euler,useLcm: false,CFG scale: 3.5,Clip skip: undefined,
```

![](img/zhuanqian_93f55fff91f2ccf0be9f1f64fd3a049e.png)

换成我们自己的商品

![](img/zhuanqian_947a4d830c66aef5f881389576f63414.png)

## 案例四 人物和商品同框：背包

![](img/zhuanqian_57a041d95ecf5ec586f5b42c90086907.png)

![](img/zhuanqian_573ceacf117e2a2dc962bac48b3df778.png)

```
https://www.liblib.art/modelinfo/f54c62a5b8f743bbb855264f5c65fdf9?from=feed&versionUuid=e6bce843aaa947168c60c147d56a1c80
e6bce843aaa947168c60c147d56a1c80
提示词：DS Model,This photograph features an Asian woman with shoulder-length brown hair and bangs,positioned against a pinkish-purple background. She is wearing a navy blue spaghetti strap tank top,and her bare arms are visible. The woman is holding a white hairbrush with a black base and black bristles in her left hand,which is raised to her forehead,partially covering her face. Her right hand is also raised,with her fingers resting on the hairbrush. She has a slight smile and is gazing off to the left. The image is cropped just below her waist,and there is no text or additional objects visible.,
Negative prompt: ng_deepnegative_v1_75t,(badhandv4:1.2),EasyNegative,(worst quality:2),
Steps: 30,Size: 1000x1536,Seed: -1,Model: F.1基础算法模型-哩布在线可运行, 【梁工】超精致电商模特/人物场景,Sampler: Euler,useLcm: false,CFG scale: 3.5,Clip skip: undefined,
```

![](img/zhuanqian_7402d7cf8b6a6a3b7c8e25ce11f7a445.png)

预算到顶了，就不再往下测了。到这里已经能看出模型本身的底子够不够好。

## 零、先领点免费出图额度

Liblib 有一个零成本出图的通道：注册时用 QQ 账号登录，系统直接送 500 积分，能跑不少图。

![](img/zhuanqian_8403dea400b7c3626c7ba61d6d492b6b.png)

## 一、这套方案主要解决什么

* 第一，Liblib 中任意模板都可以接入

* 第二，人物形象能保持稳定，这个能力很能打

* 第三，可用模板超过十万，范围非常广

比如想做“古风美女加山海经异兽”这类题材，把参考短片的抖音分享链接填进去，链接用 http 开头的完整地址。

![](img/zhuanqian_872ba7e60cd03dc1bf1770f596353163.png)

这就是从抖音复制出来的链接

```
4.17 B@T.LW 03/15 icN:/ oi 小鬼 有点火热了 #
黑长直 # 美女
https://v.douyin.com/Ytrgp-sWcVw/
复制此链接，打开Dou音搜索，直接观看视频！
```

![](img/zhuanqian_4fee0aafd1ea9785bed78013399cde4d.png)

镜头拆分的数量可以设置，单个镜头默认 5 秒，按需调整即可。

回到 Liblib 找同款模型，可选择范围非常大。

![](img/zhuanqian_db88d499faaf8e379c7d559a63439529.png)

把页面上生成的这串 ID 复制下来，填到自动化流程的对应位置。

![](img/zhuanqian_52debd6c4218ee02da2ea87f11a3f259.png)

![](img/zhuanqian_86befa200b5773ce27fb125f57eec721.png)

![](img/zhuanqian_e62087a1e848e61a8031e124e2e3b12b.png)

![](img/zhuanqian_78dc1246717ddc9af9b47f5286a427bf.png)

完工后，这个模型就能直接被后续节点调用了。

## 二、整体实现路径

### 1. 先看全景

![](img/zhuanqian_520b55993865ffebccc076470f8ce71a.png)

### 2. 整体设计思路

![](img/zhuanqian_e34bd613246d2ed23ba07b901a66d925.png)

### 3. 项目架构脑图

![](img/zhuanqian_e3b440ae00ecb2b45f2cf1afe509c541.png)

## 三、按四层结构看整条流水线

* 第一层是入口层：负责拉取视频、拆解内容、产出镜头脚本

* 第二层是出图层：根据镜头脚本生成静态画面

* 第三层是动态层：把静态画面交给视频模型生成短视频段

* 第四层是后期层：完成剪辑、配音、字幕等处理，导出最终成片

## 四、流水线的具体运行方式

1. 用户在表单里填好任务主题、参考视频地址和镜头拆分个数

2. 系统按这些信息生成镜头脚本，其中包含旁白和画面提示词

3. 把画面提示词交给 Liblib 的图片生成接口，产出静态图

4. 静态图再送入海螺的视频模型，转成短视频段

5. 把这些短视频段按顺序拼接成完整视频

6. 整片最后上传到抖音这类目标渠道，并取回不带水印的播放地址

## 入口层细节

### 1. 提交入口：n8n 的 Form Trigger 节点

用途：接收用户提交的任务信息

任务主题（文本框）

参考视频地址（抖音分享链接）

镜头拆分个数（下拉框选择，1 到 6 个）

页面效果长这样↓

![](img/zhuanqian_9031252548e85c7e3533c7480e6777c9.png)

配置过程看这里↓

![](img/zhuanqian_3fb4ce6dea897b75a35e40f365777a36.png)

![](img/zhuanqian_d027e16fcfa142e0f71ab94a2f374b3b.png)

![](img/zhuanqian_c6daae0a934fe28883509da7b26fa2be.png)

### 2. 参数集中管理：Edit Fields 节点

作用：所有账号凭据和全局设置都统一放在这里维护

需要人工填写的包括三项：

1. LoRA 标识

2. Liblib 的 SecretKey 和 AccessKey

3. 抖音下载服务对应的 AppID 与 AppSercert

一句话总结：API 账号信息和项目参数都在这里存档

![](img/zhuanqian_90334f110f2d696bfa5c51a7f8a7f98f.png)

![](img/zhuanqian_c372556a4cdaffa622241daf2fca0f98.png)

![](img/zhuanqian_320981f4e3ca083654beb3592f0a7385.png)

#### LoRA 标识从哪来

1. 当前 Lib 已经把站内允许商用的模型全部开放给 API 了，到站内筛一下“商用授权”，就能看到可用的 Checkpoint 和 LoRA

![](img/zhuanqian_a3835ed7a4a538c33fa2bbc0e1858dba.png)

1. 选好模型版本后，从浏览器地址栏里把 versionUuid 原样取出来

![](img/zhuanqian_26427b2c1cc7b1969c471e02c07147a1.png)

1. 再把它填进出图接口的参数模板，作为 LoRA 标识来使用

#### Liblib 密钥怎么拿

先登录 liblib.art 的后台，进入生图相关设置页

![](img/zhuanqian_9743e45128804a368cea065dfa0bf42d.png)

![](img/zhuanqian_bf761187106b89f3408c9b4a52f8dd8c.png)

![](img/zhuanqian_91e05479b5ce375d1e94fcf78598c6e1.png)

#### 抖音下载服务的账号信息

去抖音解析服务商那边申请 AppID 和 AppSercert

![](img/zhuanqian_698f57323dc343dc43b7f40bde0f3d48.png)

![](img/zhuanqian_b6095d9626bc7e1ab2538d530c80fdeb.png)

### 3. 视频地址加密

这里的加密是为了满足服务商对接口传输的要求。

视频拉取这件事交给 Roll 来做，配套说明文档叫“抖音下载”。

流程上会先把链接加密：

![](img/zhuanqian_29ede13cc0c0d4d97ed65658e2ae0e80.png)

上面这段代码负责把原始链接转成加密格式，再提交给后续接口使用。

在短视频内容创作日益内卷的今天，如何高效产出爆款视频成了许多人的痛点。今天我们不聊创意，直接拆解一套全自动化的“视频工厂”流水线，从脚本到成片，全程由AI和代码接管，你只需要做最终的审核者。

**第一步，先搞定素材源头。**

想用别人的视频做二次创作，最烦的就是水印。这套流程里，我们通过一个HTTP请求接口就能直接拿到无水印视频。你只需要把视频链接转成加密格式，再配上你自己的专属ID，接口就会立刻返回一条干净的视频直链，省去了下载、去水印的繁琐操作。

**紧接着，让AI大脑来生成脚本。**

这里接入的是Gemini模型，它承担的是“编剧”角色。你只需输入一个简单的主题，它便会自动生成结构化的分镜脚本。每个分镜都包含三个关键要素：序号、旁白文案（还贴心地按抖音爆款风格优化），以及图片提示词（这个提示词非常讲究，包含了触发词、人物特征、场景、动作、氛围和风格，直接喂给AI绘图工具就能用）。输出的格式是标准的JSON，方便后续程序直接读取。

**脚本有了，下一步就是配图。**

系统会把刚才生成的分镜脚本挨个拆开，然后通过加密节点生成一个“安全令牌”。这个令牌的生成过程很严谨，需要用你的密钥（SecretKey）通过HMAC-SHA1算法对时间戳、随机数等参数进行签名计算，确保每次请求的合法性。签名生成后，还要经过一次Base64编码转换，让它在URL里能安全传输，最后才能调用画图API，把文字变成真正的图片。

**图片到位，视频就该登场了。**

为了赋予静态图片“生命”，系统选用的是海螺2模型。这个模型最大的特点就是画面动作幅度大，很有视觉冲击力，非常适合短视频的节奏。由于这个API只在海外平台（比如fal）上提供，所以我们需要通过请求它的队列服务来提交任务。提交后，系统会不断轮询任务状态，一旦后台完成渲染，就能拿到生成好的视频片段。

**最后，把所有素材拼装成完整的作品。**

各个分镜的视频片段生成后，会通过一个聚合节点汇总。接着，系统会提交一个“合并任务”给后期处理服务，然后实时监控合并进度。当检测到任务状态变为“完成”时，系统就会自动下载最终剪辑好的成片。

至此，一条从创意构思、文案撰写、画面生成到剪辑合成的全链路短视频，就漂漂亮亮地出现在你的硬盘里了。

```
// Loop over input items and add a new field called 'myNewField' to the JSON of each one
for (const item of $input.all()) {
const videoLink = item.json['视频链接http'];
if (videoLink) {
// 将视频链接转换为 Base64 编码
item.json.videoLinkBase64 = Buffer.from(videoLink).toString('base64');
}
item.json.myNewField = 1;
}
return $input.all();
``` ![](img/zhuanqian_fb518c5363e29a3823a48ff9ab8f1d99.png) ![](img/zhuanqian_3fa73e7db5ed3801458f85f6b9d73090.png) ```
# **角色**
抖音爆款文案大师 & AI视觉创意总监
* 模仿爆款风格：语言节奏、口头禅、视觉习惯
* 普通文案 → 爆款旁白
* 每句旁白 → 匹配英文图片提示词（画面与文案融合）
# **输入**
* **参考片段：** 爆款视频（分析语气/节奏/句式/画面风格）
* **主题：** {{ \$('提交表单').item.json\['视频文案'] }}
* **分镜数：** {{ \$('提交表单').item.json\['分镜数量'] }}
* **旁白字数策略：**
* 每镜10-25字随情感节奏变化
* **提示词示例：** {{ \$('参数设置').item.json\['Liblib 提示词示例'] }}
* **触发词：** {{ \$('参数设置').item.json\['Liblib 触发词'] }}
# **任务**
1\. 文案按分镜拆解 → 数量一致
2\. 旁白深度改写 → 保留核心，套用爆款风格
3\. 严控字数 → 按策略执行
4\. 每镜生成独立英文图片提示词 → 含完整人物/场景/动作/风格
5\. 同一角色 → 外貌描述完全一致
6\. 每个提示词首行加触发词
7\. 所有提示词 → 健康正面，合规全年龄
# **输出格式**
``` ```
``` ![](img/zhuanqian_1bf42d5b5d29aafe9c352695639c359d.png) ![](img/zhuanqian_152cd04df436344eb0579a2a2ca6778c.png) ![](img/zhuanqian_a3eddca8fe6526ab79f3e648fad3f0b3.png) ![](img/zhuanqian_3c37fecd2ba56a988e34b228c69a454e.png) ![](img/zhuanqian_854b4252b5efb8a04ad8333c0f147edb.png) ![](img/zhuanqian_212c634c9627e0ce35547db4553a2099.png) ![](img/zhuanqian_c97ae6b1a1dedf7d8dd94f567c6bfe59.png) ![](img/zhuanqian_b83f39f27020363ddc6a001329497ca3.png) ![](img/zhuanqian_7d5692a8d9d1dc62bd13c33e59a96629.png) ![](img/zhuanqian_2b4d8f70bc7038a8c2df2b183a9e25dc.png) ![](img/zhuanqian_d2f372f4bff028645dfc4cb62561b50c.png) ![](img/zhuanqian_f180c892e136f0d245ab7b05cd0415dc.png) ![](img/zhuanqian_a57608d73de2568c935668651399a841.png) ![](img/zhuanqian_bdcc960224eb689fb18eefc8939378dc.png) ![](img/zhuanqian_31735a8d259311664e8b3595e16bf46c.png) ![](img/zhuanqian_4ec71931e02969bb6497e9dc1f2d45bb.png) ![](img/zhuanqian_9d5452f1dc456c31fa6ae04aa64c7c7d.png)