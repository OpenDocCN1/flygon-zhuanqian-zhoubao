# AI-Shorts两类视频复刻教程：从“融合怪”到“动物跳舞”
我是龙哥。最近一直在折腾AI短视频，之前已经拆过AI动物故事视频的复刻，最近又刷到一些门槛更低、数据表现也很不错的玩法。研究了一圈下来，最有代表性的其实就两类：一类是“融合怪”，一类是“动物跳舞”。今天就把这两类的复刻思路完整分享一下。
## 一、AI融合怪视频怎么复刻？
这类视频的核心，是用AI视频生成能力，把两种或者三种动物融合在一起，产生一种很吸睛的“怪”效果。可以先看看这个hashtag下面的案例：
https://www.youtube.com/hashtag/fusion/shorts
![](img/zhuanqian_81f8cb85e2610a5a25fa8b1717d4ec09.png)
![](img/zhuanqian_f8888df686743e2223e584ef68f351e1.png)
想上手的话，先找到适合自己的对标方向。我梳理了比较常见的几种类型：
- 动物融合，但是纯图片，不靠AI生成视频：参考 @HeshanMalinda-nf6ws
![](img/zhuanqian_7fd7c3c949894d658c4d727bd8005be9.png)
- 动物融合，但是包含AI生成的“怪物融合过程”：参考这条shorts
![](img/zhuanqian_cc4cfbf8804898c113030d8d9dc7ba52.png)
- 人与动物融合：参考 @AnimolFacts
![](img/zhuanqian_5f19999602c5e78169c8de478d5e026b.png)
- 人与动物融合，再加上达人秀剪辑：参考 @TalentSnap
![](img/zhuanqian_5473ba51e15e47ad2e5dcbd8669b7e9e.png)
### 示例视频
先看两个案例：
https://www.youtube.com/shorts/-alVWmtIRYM
https://www.youtube.com/shorts/2YmX-9auHUw
左边那条是纯图片路线，复刻比较简单，用 Dalle3 或 Midjourney 就能生成类似图片。右边那条多了一个融合过程，这时候就需要用到“首尾帧视频生成”。
什么是首尾帧？其实就是告诉AI开始画面是什么、结束画面是什么，中间的变化过程让AI自己脑补出来。目前常用工具是即梦AI和可灵AI，我更推荐即梦AI，免费生成而且不用排队。
即梦AI：
- 国内版：https://jimeng.jianying.com/
- 海外版（不推荐，功能不太全）：https://dreamina.capcut.com/
可灵AI：
- 国内版：https://klingai.kuaishou.com/
- 海外版：https://klingai.com/
我做片段对比的时候，左边用的是即梦AI（视频模型1.2），右边用的是可灵AI：
![](img/zhuanqian_6865a3f2e5ab5f73a2d89d46975a2f7f.png)
![](img/zhuanqian_b8edebab9ced63cfaed69b55fd0aecf2.png)
这样，一个融合片段就生成了。如果目标是一分钟的长视频，大概需要拼7段左右。刚开始模仿时可能会觉得有点难度，所以不用一上来就冲长视频，先做十几秒的短视频、拼接三段左右就够练手了。
而且对标参考里的第四类“舞台表演融合怪”，往往只拼接三段AI视频，制作难度就小很多。下面就拿达人秀融合类视频做案例，完整拆解一遍。
### 案例拆解
对标视频：https://www.youtube.com/shorts/4dsM0zD-tdo
先感受下效果，左边是原视频，右边是我模仿出来的版本：
融合怪的核心原理，还是首尾帧视频生成：
![](img/zhuanqian_f708419a429e6c77c2b775986f84546b.png)
### 制作演示
演示我用的是即梦AI，用可灵AI也可以跑。地址：https://jimeng.jianying.com/
第一步，先生成图片。可以输入提示词，也可以导入图片当参考：
![](img/zhuanqian_a7b28c57f783e707d8c8ba27deef30b6.png)
我先做了一张“美女+白马”的底图，提示词是“舞台上一个美女和一匹白马走在一起”。即梦AI会生成四张图片，我选了第二张，欧美人脸：
![](img/zhuanqian_4907afa51f8669637dc6e6cbd0ae381b.png)
再来一张融合完成后的结果图。我同样选了第二张，提示词是：“舞台上，一个长着马耳朵的欧美人美女，穿着白色礼服，留着金色的长发”：
![](img/zhuanqian_8ef3677b36ef8e896b16aa214a3d1ffd.png)
接着生成融合前的图片，这里我用了参考图。提示词是：“舞台上，一匹白马和一个穿着白色礼服的欧美人美女靠在一起”：
![](img/zhuanqian_874a1e1cfc39e3db60ec3f844d926b35.png)
![](img/zhuanqian_a1c0b724c6dd99b23f94553f9b680b95.png)
图片准备好之后，接下来生成三段视频：
第一段，融合过程的视频：
![](img/zhuanqian_651b786d764f0c53f4127e477d1071bf.png)
![](img/zhuanqian_b6a0c8633a0481b804f59e324234abf6.png)
第二段，融合前的视频：
![](img/zhuanqian_17390e5d5a5b6460a923952fec306e68.png)
![](img/zhuanqian_f6618c3b6d0e77bd09be1df69dc36afe.png)
第三段，融合后的视频：
![](img/zhuanqian_5e786a6ee56a6618a767dc1ebeafb1bc.png)
![](img/zhuanqian_c3440c547da3a3c3fc452803d5ca9778.png)
最后就是剪辑：把三段视频拼接起来。对标视频里惊讶反应的画面可以直接保留，想自己发挥的话，也可以用AI生成或者去其他视频里截图。AI生成的部分用自己的素材替换掉，配上同样的音乐，一条融合怪视频就完成了。
![](img/zhuanqian_b63116d858367ecfa96a9e28c4ac06f7.png)
## 二、AI动物跳舞视频怎么复刻？
另一类热度很高的AI短视频是猫猫跳舞，YouTube上流量很猛。先放个参考链接：
https://www.youtube.com/source/bWYB4u3M3uk/shorts?bp=8gVbCk4SPwoLYldZQjR1M00zdWsSC2JXWUI0dTNNM3VrGgswS0tKU18yZDJqT2PayIKEggIBxDAu9C2ASoKEggIBxDAu9C2ARoLMEtKU18yZDJqT2so48qu2bTLip7CAQ%253D%253D
![](img/zhuanqian_c455266605605a3074c4f15563624f53.png)
![](img/zhuanqian_4497ad0490bffcb13ee3481f8ccfc682.png)
这类视频做起来也不复杂，只要找对对标，很快就能复刻。我整理了四个参考账号（注意：对标只是参考，具体账号要根据自己的定位来选）：
账号1：@CatKitten99
![](img/zhuanqian_fad0f7d602b009500d0bbbcf4d341bba.png)
这是一个国人运营的YouTube账号，第一条视频7月18号发布，已经跑到2000万观看量。
![](img/zhuanqian_1129ab183287800ebc48ed89e10fd957.png)
账号2：@serenovive
这个账号从8月12号开始转做猫猫跳舞视频。
![](img/zhuanqian_cad4368cedd896417ba5d96ca5233135.png)
账号3：@AnimalsShorts-h1f
9月11号注册，单条shorts流量能做到5万以上。
![](img/zhuanqian_aac63b205699fe287929105afcddce30.png)
![](img/zhuanqian_ff463d2f1ca414bad20a21cbacc15074.png)
账号4：@furry-cornerz
从7月7号开始转做猫猫跳舞视频。
![](img/zhuanqian_9cb53bc906e96ad97acc2b3821634ba9.png)
### 制作方式
目前能做动物跳舞视频的方式主要三种：
第一种，通义千问App。打开App里的“全民舞王”频道，就能免费生成跳舞视频：
![](img/zhuanqian_2cb9b220f6dbc80615246839072a6d55.png)
第二种，Viggle。平台地址是 https://viggle.ai/ ，你只需要上传一张图片和一段示例视频，它就能让图片里的人物或动物跳起来。官网每天有10次免费额度，Discord目前免费。模板地址：https://viggle.ai/prompt ，Discord群：https://discord.gg/viggle
![](img/zhuanqian_2481adb48cf9a90bba7185ca1608284d.png)
![](img/zhuanqian_9e66742629d7fa9f7bf8bcc1bb1dd3ab.png)
第三种，ComfyUI。可以结合阿里开源的UniAnimate模型来搭建动物跳舞工作流：
https://www.liblib.art/modelinfo/b73fac6d3ae44a8ba3f02364f74b4938
- 节点：https://github.com/Isi-dev/ComfyUI-UniAnimate-W
- 模型：https://www.modelscope.cn/models/iic/UniAnimate
![](img/zhuanqian_60941a3c5351688de2a174e6e1ba22d1.png)
### 制作演示
个人实际体验下来，通义千问App的全民舞王效果最稳定，Viggle的测试效果会差不少。ComfyUI暂时不能在哩布哩布平台在线跑，需要自己下载模型、解决报错，比较折腾。
所以这里用全民舞王来演示。进入“全民舞王”，在创意广场挑一个模板，点击“做同款”，导入一张AI图片，然后点“立即生成”就行：
![](img/zhuanqian_9f204aca463f6695eb7ad56edc3b6cd7.png)
![](img/zhuanqian_ea5dc748361a390e9ced46f7aeb19958.png)
![](img/zhuanqian_7b6d9d2096161d4c90c37d1e633f3f93.png)
生成出来的效果，整体还是挺真实的。
如果你看中的动作在自带模板里找不到，就需要自己上传一段视频来制作模板（每天免费10次，每次登录也会送1次），然后再用这个模板生成相似视频：
![](img/zhuanqian_4be0250226790a7e0425fb40a726b396.png)
![](img/zhuanqian_a389300f9e27ee4a0a7a4b09c8be4b64.png)
![](img/zhuanqian_cbf5cc9570fe54f7664c1c3a2336e03b.png)
实际生成效果会比自带模板稍微差一点。左边是原视频参考：
https://www.tiktok.com/@animaldance0711/video/7421795597981601042
## 补充
之前还分享过几个实操技能，感兴趣的可以继续研究：
【赚钱技能】AI动物故事视频复刻与批量生产
【赚钱技能】抛弃显卡！ComfyUI+Flux 纯网页跑图喂饭级教程
【赚钱技能】海螺AI图生视频如何用RPA提升10倍速高效产出视频？