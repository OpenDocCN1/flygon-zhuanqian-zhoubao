# 《AI障眼法完全攻略：三步做出刷屏全网的魔幻影像》
大家好，我是老吴。
今天要聊的玩法，就是最近在各大内容平台上疯狂刷屏的“AI障眼法”——简单说，让AI生成一张表面看不出毛病、实际却暗藏另一个人物的图片。
这类内容因为新鲜又直观，在抖音、B站快速扩散，几十万赞的帖子比比皆是，单条冲到千万级播放也不算稀奇。
内核逻辑其实很朴素：把曾经火过的梗或表情图，交给AI重新演一遍，新的爆款就诞生了。
我把市面上的相关套路几乎都试了个遍，最后整理出一条从零上手的完整链路：素材分割→绘图参数准备→CN控制模块调校。按顺序走，你也能复刻同款。
场景上我挑了户外风光、动漫、建筑、表情梗图四类常见方向来拆解。
全部模型文件我已经汇总到文末网盘链接，省得你满世界找资源。
这次整理花了挺多时间，希望真能帮到你。不支持搬运，发现必究。
# 一、障眼法到底是什么
障眼法做的事情，用一句话概括：把你想要的主角，悄无声息地藏进一张看起来再普通不过的照片里。
乍一眼画面毫无异常，放大看局部也挑不出毛病，但只要把图片缩小，某个标志性面孔就会突然浮现。
比如下面这张：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_781e0e93cb58f0f0895c499087d0dff3.png>
类似的还有街头实景：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d22d5723aa92495ca3cbf5b8157adb98.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4270a9f1ac8ccc71ffbcba38e6846db2.png>
也有大尺度的户外景观：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a8d83f7ca2911fc89a1ecd32d568d0de.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b48da00cd0cd545c12c0ba557cc044ee.png>
不管是动漫女孩、小猫咪，还是一栋独立的房子，同一个人的轮廓都能稳稳嵌进去：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_07fa67fb0f7c310740da5c4ab6d414c6.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1a793372bb8bfdf55ad46500bdf1b45c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5384a3d563b2aff9ef02849e49d2b2f1.png>
把静态图替换成动态后，被藏起来的主角甚至会在画面里直接跳舞。
这类作品放到抖音上，动辄收获几十万赞；B站百万播放的案例同样不难遇见。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8919902f350f561eca7fa0dd7a9bd1f4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_312808c144e8dfac5c55524e5d019692.png>
而且不管最后成品是哪一种形式，背后的生产流程都只有三步。
接下来我就带着你亲手把这些神奇的作品做出来。
# 二、三步做出一张障眼法图片
以“某位练习生”同款效果为例，整体分为三个环节：
1. 素材分割
2. 绘图参数准备
3. CN控制模块调校
下面就用城市夜景图来做一个完整演示：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1a212b271efd7c982f444787db387c52.png>
## 环节一：素材分割
先挑一张你想改造的底图，把画面中的人物独立分离出来，做成一份黑白遮罩。这份遮罩相当于后面控制模块要用的“骨架”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_75b072930180e77a8bff966fbd5d7a50.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d23e63c0d7c758501337eaba0ceae719.png>
分离主体用到的工具，是Stable Diffusion平台里的扩展插件：Segment Anything。
### Segment Anything怎么用
整套使用流程分三步：装扩展、放权重、开始切图。
01. 装扩展
操作不复杂：
①启动SD后进入“扩展”页面
②切到可下载标签，把线上插件清单刷新出来
③在搜索框输入segment
④找到目标后点安装按钮
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_73c6b11180ed2289fc54e521a4e9f9f6.png>
02. 放权重
Segment Anything还差一个预训练模型，去网盘把“sam”文件夹里的内容下载好，放到如下路径：
SD文件夹\extensions\sd-webui-segment-anything\models\sam
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d7de4c6e60a339c37a6571ff843a5881.png>
放好后回到扩展页，点“应用更改并重启”，插件入口才会出现在界面上。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_362b4f4bf1288d186a4ed9a45a3f76b6.png>
03. 开始切图
重新进入SD，在菜单里打开Segment Anything面板。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_15c11819a128c3fbd57e586d9ee6f112.png>
上传需要处理的照片。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0361d85d0cbc2ce95870335303719255.png>
接着用鼠标打点：左键生成黑色标记点，表示此处是保留的主体；右键生成红色标记点，表示此处是排除的背景。沿着人物外围点上一圈即可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8c5629617323978d00e004a0c0df0a31.png>
标记完成后，按下“预览分离结果”，稍等片刻就能得到遮罩。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f394ff27ef80d92b71d40067fc3f18fb.png>
程序每次会返回三张候选分割结果，挑主体最完整的一张保存下来。
如果三张都差口气，就在残缺处补几个点，再重新分离一次。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e261e022660dbccf1933e9f88680e071.png>
到这里，底图预处理已全部结束，下一步可以去配置绘图参数了。
## 环节二：绘图参数准备
这个环节集中处理三件小事：选底模、填描述词、调画幅。
### 01. 选底模
底模可以选动漫风格，也可以选写实风格。
示范用的城市夜景图，走的就是写实路线：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a929473d64f42c11a91661da0688bdc3.png>
本地没有这款底模的话，去网盘里拿majicmix文件夹，把里面的模型文件放到
SD文件夹\models\Stable-diffusion
目录下即可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ffa8b5fc0955d62a3a55e8f82b4dee32.png>
### 02. 填描述词
描述词没有标准答案，每个人的语料库都是在一次次抽图中沉淀出来的。
下面这组夜景描述是我反复测试后觉得相对稳定的版本，可以直接参考：
画面描述：
masterpiece, high quality, high-resolution, rich texture,
urban night scene, roads, vehicles, architecture, streets, traffic flow, bustling downtown, artificial lighting, plants, water reflections, night sky, clouds, neon lights, headlights
中文释义：
高画质、细节充分；城市夜景、道路、汽车、建筑、街道、繁忙车流、灯火通明的市中心、灯光、植物、水面倒影、夜空、云层、彩色霓虹与车灯。
通用负面词（可直接原样粘贴）：
EasyNegative, ng_deepnegative_v1_75t, badhandv4, (worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), bad anatomy, DeepNegative, skin spots, acnes, skin blemishes, (fat:1.2), facing away, looking away, tilted head, bad hands, missing fingers, extra digit, fewer digits, bad feet, poorly drawn hands, poorly drawn face, mutation, deformed, extra fingers, extra limbs, extra arms, extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed, mutated hands, polar lowres, bad body, bad proportions, gross proportions, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, teeth cropped, signature, watermark, username, blurry, cropped, jpeg artifacts, text, error
### 03. 调画幅
输出宽高记得与底图比例保持一致。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6d1cf17af81a13b017a7fb7ad8a0819e.png>
## 环节三：CN控制模块调校
先把刚才存好的黑白遮罩拖进ControlNet下方的图像区域。
控制模型选择qrcode monster，本地没装就去网盘拿，模型放置路径是：
sd文件夹\models\ControlNet
权重范围可以取0.75到1.5，数值设得越高，轮廓会被压得越紧。
然后按下生成键。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_18c504460e77cad0fc4175b8d4eb73cc.png>
第一张障眼法图片就这么出来了：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_649d4126a06a0dc7954127943a8cc142.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c126fb81ae3497485a6940292f8d4964.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_59f8b95eeaf154e153aee9202f4e732d.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_28dc69d7deb723a4d9f158b88608adf3.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f6e7e8677d7b70ada9f58f7c7e23a1a2.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_189254d1dd76f4b0f9f98a0a4ef65070.png>
单张图的制作方法到这里就全部讲完。
考虑到大家可能想尝试不同方向，我又跑了大量测试，从成批出图里整理出几套效果稳定的描述词，一并放进网盘，复制即可用。
## 附加：几类常用风格的参考词条
### 户外风光类
画面描述：
high-quality, masterpiece, finely detailed, alpine views, blue sky, drifting clouds, lakeside vegetation, trees, tranquil natural landscape
中文释义：
最高质量、细节丰富；山景、蓝天、流云、湖滨植物、树木以及安静的自然风光。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_57215ddb4e7bd4f0fd7861c84e73c2ed.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d9447f7001e910aeebbdd9c59525817b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fbb03dfcacfb9212a27f82931423d42d.png>
如果你更想要黑色剪影那种效果，也就是人物轮廓直接以深色块呈现：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9e2e92858fdfb69979dc5314970d0df2.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0475b67e6deb8f9be93d7b728f658fe4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_24ed03bc24e2a2d951809589593eee58.png>
做法很简单：在ControlNet面板把预处理器调整为invert（反转），黑白区域就会对调。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1d7a1d77a3b6024b7208b12f4e98b2a9.png>
### 动漫少女类
画面描述：
masterpiece, high quality, high-resolution, rich details,
a single girl, refined facial features, bright big eyes, long flowing hair,
elegant dress, delicate outfit, upper body composition, garden background
中文释义：
高画质、精细细节；单人少女，五官精致、大眼睛、长发；穿着精致裙装；取上半身构图，背景是花园。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_291a94b500a0dc7712a627631c688184.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_40cae067c74bef12e568e296276fd9fe.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4bd32c692a32fe3d01e8a8a48cd361f2.png>
### 小屋住宅类
画面描述：
masterpiece, high quality, high-resolution, rich details,
one house, courtyard, residential building, outdoor setting
中文释义：
一栋住宅自带庭院，突出户外建筑的整体氛围。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_373e1cab756dfa4e25bfe348d0909284.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ad3f3029b165cb9c6d72fe46b1e402cc.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_14773d9f7c9bcf177243134ed3358b59.png>
### 表情梗图类
藏人目标不限于那位练习生，任何出圈素材都可以拿来做实验，比如姚明的经典笑脸：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a74e1f815869f21732dc535d832a2bb3.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bba031e4fc1646f2bbb3c4b9c489e0e4.png>
像这类高度依赖五官特征的图，可以省掉分割遮罩的环节：直接把原始图片丢进ControlNet，调高权重数值，生成时五官轮廓就会被牢牢锁住。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aa6e1f50118aa66b2ae6951c193773f4.png>
一个实用经验：把障眼法与正在上升期的热点话题绑在一起，传播数据往往会有惊喜。
# 三、动态视频也能如法炮制
视频和图片在原理上是相通的，本质上就是大量静态帧按顺序连续播放。
区别只在于：以前是生成一张，现在要批量生成成百上千张。
所以操作流程也需要同步调整：
1. 批量分离主体
2. 批量生成画面
3. 剪辑为视频
下面逐步拆解。
## 第一步：批量分离主体
先把视频拆成一帧一帧的画面，再为这些帧图配上对应的黑白遮罩。
具体可分成三小步：装工具、拆视频、出遮罩。
### 1. 装工具
这个插件可以同时完成拆帧和遮罩生成，安装相当省事：
①在SD中进入扩展页面
②选择“通过链接安装”方式
③把仓库地址粘贴进输入框：https://github.com/ClockZinc/sd-webui-IS-NET-pro.git
④点安装
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_167abda1945bdb96702a409ac192d72a.png>
接着把网盘《IS-Net》文件夹里的模型放到指定位置：
sd文件夹\extensions\sd-webui-IS-NET-pro\saved_models\IS-Net
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_de824cecbb4fc3a24125b19241074d23.png>
工具就算准备好了。
### 2. 拆视频
①重启Stable Diffusion，侧边栏会出现isnet_pro入口
②打开isnet_pro页面
③把视频文件拖进指定区域
④打开抽帧开关，抽帧密度设为10，也就是每秒留下10帧画面；数值越高输出帧图越多，设10是效率与效果的折中
⑤新建一个文件夹，命名时避开中文；把路径复制到界面里的“图片输入地址”栏，作为帧图保存位置
⑥按下“gene_frame”开始抽取
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f3905b845a13e51fecef9582c2c1defb.png>
路径获取方法：在文件夹上按右键，选择“复制文件地址”，然后粘贴进对应输入框。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8ee65cad8ac395b80cfc61fc742dea2f.png>
注意：粘贴完毕后要手动删掉地址前后残留的双引号，否则程序会报错。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3d596cad909dfd4a417f4a72124306c5.png>
处理完成后，打开文件夹就能看到从视频里截出来的所有画面。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_72bbf31e55a145912189ca1eba433e11.png>
接下来给这些帧图逐一生成遮罩。
### 3. 出遮罩
①打开ISNETpro2页面
②把刚才存放帧图的文件夹路径再次填入“图片输入地址”
③再新建一个文件夹专门存放遮罩，命名同样避开中文；将路径填到“图片输出地址”
④按下“仅生成蒙版”按钮
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9b7f0a285df04dbf9a3baabecc914b0a.png>
跑完之后，输出目录里全是配套好的黑白遮罩。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_64827512a8237568b71bd33ff9a0dddd.png>
至此，视频素材的前置处理已经全部完成。
## 第二步：批量生成画面
这一步的操作和单张出图几乎一模一样：底模、描述词、各项参数全部保持原样。
唯一区别是ControlNet右侧要切换到批量模式：
01. 打开ControlNet，设置不动，点“批量处理”标签
02. 把存放遮罩图的文件夹路径粘到输入路径栏
03. 按下生成键，让程序把每一帧依次补齐
到这里，整套AI障眼法的制作流程就全部结束了。
正式批量出图前，建议大家先用单张蒙版图跑一次看看效果。只要参数设定都没问题，就可以放心大胆地批量生成了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8f7aef0b8582aed8a580db0d1c6e3a55.png>
整个生成耗时并不固定，取决于你的照片数量、分辨率设置以及迭代步数，耐心等待即可。
## 3. 把图片串成视频
所有图片都生成完毕，下一步就是剪辑成片。点击“📂”文件夹图标，找到刚输出的图像文件，并把它们统一存放到一个新的文件夹中。特别提醒：这个新建文件夹的名称里不要出现中文字符。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_30d75c0e2affd37319904367f2646b08.png>
接着打开 isnet-pro 插件，用它来把图片拼接成动态视频。帧率调到 10，然后把刚才那个文件夹的路径粘贴到“输入地址”栏，再选一个用于存放视频的文件夹路径，点击生成按钮就好。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b65a0768dd8d248a9c515a12f9aabfb1.png>
最后打开剪映，配上你喜欢的 BGM，整个作品就完成了。再来看一眼最终的成品效果吧。
# 四、结尾
以上就是本次分享的全部内容啦，希望这些方法能帮你创作出更多有趣好玩的 AI 幻术图片。如果你对 AI 感兴趣，欢迎关注我的公众号“吴东子AI”，也欢迎把文章分享给身边想学 AI 技术的朋友。公众号里不仅有我之前发过的所有文章，以后还会持续更新实用的 AI 干货教程。我是吴东子，坚持用奶奶都能听懂的方式，分享能落地的实操内容，咱们下篇文章再见！
网盘链接：https://pan.baidu.com/s/19Xnof-BSA-FubkMc_0XNhA?pwd=wdz6
提取码：wdz6
吴东子AI账号简介：https://ry5hwpuf7b.feishu.cn/wiki/space/7283841978071072772?ccm_open_type=lark_wiki_spaceLink