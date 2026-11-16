# 三年AI图像工程师跟你分享，无限贴近真人的调教方法，助力AI变现

我的本职工作，是跟图像打了三年交道的算法工程师；业余时间又特别喜欢拍照和研究人像视觉，所以一接触Stable Diffusion（SD），就自然而然地选定了“SD+人脸”这个方向。这篇文章想做一次阶段复盘，重点聊聊过去三个月里，我如何一步步让AI生成的脸更接近真实人像。内容会涉及：根据一张参考图复原脸部、动漫角色转真人、快速搭一份能用的脸部LoRA、基于模板照片换脸，以及借助SDXL做创意写真。

先讲我入坑的时间线。去年末我才第一次听说SD，真正频繁上手是在今年年中换了显卡之后。虽然较早就错过了生态最热闹的头几个月，但从六月下旬开始，我坚持在自己的订阅号上写SD相关的内容，陆续积攒了1800多位读者，也拉起了一个同好讨论群。

最早的一张头像，是用文生图功能、照着我的外貌特征硬写提示词生成的，描述里大约写着：白色毛衣、过肩发、星空底。

![](img/zhuanqian_5797e04ccdbbd6a04eafc923cc06b39c.png)

后来我把它迭代成了现在这版，核心变化是加了LoRA，五官明显更接近自己。再往后，控制网络（ControlNet）的出现让生成过程变得可控很多，既可以参考真实面孔的特征，也可以借用某类写真的整体氛围。但不管工具怎么进化，“看图说话”的基本功始终不能丢——你得先读懂一张图里到底藏着哪些关键元素，才谈得上精准控制。下面的第一个案例，就是在没有LoRA的前提下，把动漫人物转成真人。

# 这个方向到底有什么可做的？

纯二次元头像和真人定制是两件事，前者偏娱乐，后者则有更明确的市场价值。无论是把真人漫画化，还是生成一套数字写真，能不能让顾客认可，最核心的评判标准基本都是：脸像不像本人。

**Q版头像**是常见玩法之一。有人会拿明星脸做成品图来引流，因为这些面孔大家太熟了，看到图会主动认出是谁，互动量很容易上去；而且正因为熟悉，质量好坏一眼便知。当时我观察到，那位作者提过需要准备大约20张人脸素材，基本可以判断背后是训练了LoRA。SD生态里底模丰富，一个训练好的LoRA可以配合不同底模，生成风格差异很大的多种成品。

![](img/zhuanqian_ac900328e8f342da4852a52f91edd99b.png)

**职业照和写真照**是另一类更贴近刚需的方向。Midjourney的优点很多，可皮肤质感一直不够真实；相比之下，SD不只能自己训练和调优，人像生成的细节上限也更高。现在各种小程序（比如妙鸭）层出不穷，但标准化流程只能满足通用需求；职业照这种必须“像本人”的场景，私人定制依然有空间——客户看中的模板，APP里未必有。

![](img/zhuanqian_4c48aef3eb11efdd5eb765ffc2376547.png)

![](img/zhuanqian_66a4cd4fe017afb79b454c2d4b791761.png)

![](img/zhuanqian_46ffcbcc286178523a96cf9b9eca7fe0.png)

所以，想做形象照类定制，不一定非得从零生成，完全可以走“先积攒一些模板底稿、再做脸部替换”的快捷路线，就像小红书上有人用Photoshop接证件照单子一样。但这套流程里也藏着坑：不同换脸工具带来的最终效果，差距可能非常大，下面会结合案例细说。

# 动漫转真人：一次完整实战

我的第一笔定制订单，就来自订阅号里一位读者：他想把某个动漫角色变成真人形象，不需要和原作一模一样，保留气质就好，唯一明确的要求是希望身材丰满一些；预算对应一套图，数量在15到30张之间。

没有现成的LoRA，怎么实现这种漫改真人？关键一步，是从原角色图里反推出足够充分的描述词。

很多人想象的漫转真人，大概是“拿一张线稿图丢进写实底模，直接生成”。这种思路适合静态画面；但我的需求是一整套动作和场景都在变化的图，而且原型是迪士尼的茉莉公主。

![](img/zhuanqian_700a610ed66d1458980b9dcb6179bf52.png)

![](img/zhuanqian_2f857b639a7b557675d4537f62c9f118.png)

后来，对方发来了一组冰雪奇缘主题的漫改作品作参考，可以看出：发型保持得挺像，衣服则不需要一模一样，有类似的感觉就够。

![](img/zhuanqian_8bba3b5bc868f697e855955c0d330c8c.png)

![](img/zhuanqian_b4135ddd2495cf92e6c0fdd8bbf22005.png)

于是我的思路变成：选一个擅长欧美面孔、写实精度高的底模；如果这个角色恰好有人做过LoRA，那自然最好，毕竟公主类角色人气高，大概率有现成资源；剩下的场景、表情变化，全部通过描述词来控制。

正式做图时，我选了一款当时热度很高的欧美写实底模。起初没有找到可用的茉莉公主LoRA，所以决定先用反推工具把原图转成一组标签，让SD先出一批看看方向对不对。

![](img/zhuanqian_8cd74c33fe3d2f86ad4f1233bb79b6a3.png)

第一轮生成直接把反推得到的标签丢给SD，得到下面的效果。

![](img/zhuanqian_f09ae56595a95e709402820774f77f5d.png)

反推出的信息确实包含了人种、服装、配饰、姿势等基本要素，但衣服颜色和装饰细节仍然有偏差。我就在原标签基础上做修改，把服装色调、头饰这些信息固化下来。茉莉那条发带实在难以完美还原，于是换成皇冠或吊饰来替代。最后发给对方挑选，对方看中了其中一张的王冠造型和另一张的脸部状态，并要求之后所有图都保持这张脸。

![](img/zhuanqian_7c404da512d40c37de7ebaab90e33851.png)

![](img/zhuanqian_35329f43d216694f66876dceac702005.png)

“固定同一张脸”这个要求，确实让我为难了一下。专门训练一个LoRA倒也不是不行，但那就需要至少十几张同一角度的高质量素材，周期和成本都不低。当时我先试了ControlNet的Reference功能，但对风格不统一的两张真人照来说，想换得足够像还是挺难。不过这次的素材都由同一个底模生成，风格天然一致，是有机会用Reference加遮罩来锁脸的。

实际操作是：先生成几张候选图，再使用“以图改图”模式，在脸部位置画上遮罩，选择客户想要的那张脸作为唯一参考，开启“仅参考”控制方式，同时启用ADetailer做人脸修复。遮罩的作用是让程序只修改脸部区域，背景、身体都不参与计算；重绘范围也只限定在遮罩以内。

![](img/zhuanqian_2af17bc8f8d0792a40a3e48d02259fa1.png)

![](img/zhuanqian_b673ccfdfd5beb05f97d5b86c5a0d7a1.png)

控制网络的参数选用Reference预设，权重按实际输出情况调整。

![](img/zhuanqian_0beb89d8e3b4f1cb3b911edcc66ca8fb.png)

如果只开Reference而不做修复，脸崩的概率很高。我也截过中间过程图，五官错位、比例不协调、肤色不统一这些毛病几乎都会出现。

![](img/zhuanqian_a08acb5ed4226069353a5a5a829398b9.png)

此时用ADetailer把脸拉回来，生成质量会稳定不少。需要说明的是，这批实验是两个月前做的，插件和模型后来更新过一轮，我最近重新用同样参数复现，相似度反而不如当时。后来我在Civitai上找到了茉莉公主的LoRA，为了发型更贴合，也顺手测试了一版，效果见下。

![](img/zhuanqian_67af41c3a02ae40ba1e2c8222e619d05.png)

![](img/zhuanqian_f7dcb2acbbf277c23b53a04565413497.png)

这次成功的关键，部分在于参考素材统一；假如拿这些方法去换我自己的脸，相似度未必能过关。其实这类“遮罩+重绘”的思路，完全可以交给脸部检测算法来完成，原理和Roop换脸插件差不多。趁复盘的机会，我又补做了两组对比实验。

一组是直接用“以图改图+Roop”，重绘幅度调到0。

![](img/zhuanqian_495a79a918906b66966d50c648b1a458.png)

![](img/zhuanqian_e4769baabebcae224ee7a426d3ab5947.png)

直接上Roop的结果还不错，因为原图本来就不是强烈的超写实风格，Roop的表面质感恰好能匹配。而且Roop对欧美脸的支持度比亚洲脸更好，嘴部微张的表情也基本保住了，跟之前Reference的效果接近。

另一组是在Roop基础上分别叠加两个不同的修脸插件，结果是有插件的版本妆感更偏向原图，尤其右侧某一款，妆感明显更强。

![](img/zhuanqian_3c2d6aaf8e4b1aa4c0235e828a8aea66.png)

![](img/zhuanqian_46dacca0251dee0bc3babb2f0340369b.png)

小结：固定人脸时，可以优先考虑Roop；参考图来源越统一，换脸效果越理想。Reference也是常见的脸部/材质参考方案；不过现在有了IP-Adapter，参考能力更强，遇到类似需求不妨先看它的表现。

# 真人转动漫：三套不同思路

真人转动漫也有几条路线。一条是直接用线稿配合对应风格的底模，参考的是整张图的构图，操作简单，但局限大，脸部只能做到近似，很难谈得上形似；如果直接把真人脸丢给Roop转漫画，很容易变成下面这种效果。

![](img/zhuanqian_8948e6d288989066b57fb6fc559830ad.png)

另一条是训练LoRA：让模型学习你的面部特征，生成时再指定画面元素，但需要几十张照片来训练，周期和成本偏高。还有一条更省力：用ControlNet家族里的面部参考模型，一张照片就能解决。下面结合案例说明。

线稿这条线，最关键的是尽量还原原画面内容，所以需要先用反推工具把画面拆成标签。

![](img/zhuanqian_a7690139f937ac526c067e14e505c821.png)

控制端很简单：把原图放入控制网络，开启线稿预处理即可。

![](img/zhuanqian_bbd810c909102abbfa821cbdad00f3c4.png)

标签是否写得贴近画面，最终效果差别不小。

![](img/zhuanqian_03c877ca6000d4ef0c5223aa864ee467.png)

![](img/zhuanqian_762ed19d5cb7a5ad1a899c9be7907938.png)

这种方式的缺点是：画面尺寸和构图一旦有变动，重生成时就不太容易保持稳定。

另一种思路是使用IP-Adapter模型。我用的版本叫face-sd15，它能比较充分地参考面部特征，发型这类细节也能还原得很接近，而且不依赖原图尺寸。

![](img/zhuanqian_38fa687256001f976c78c03ea7c0e5d4.png)

当只想保留头部特征、其他内容都交给随机发挥时，face-sd15就够用。此时描述词不用写原画面内容，模型会自动记住你的头部特点，其余任由变化。

![](img/zhuanqian_bddc66bf6deb585378dd24e2ffe66e24.png)

如果改用ip-adapter_sd15_plus，它还能同时参考背景和穿着，整体还原度更高，也比基础版准确。

![](img/zhuanqian_5ff46ea54f4041deec3af2ff85a1a49d.png)

不过就我的多次测试来看，想精准还原发型和表情，face-sd15仍然最稳，其他版本的发型都不如它。这种控制方式不受线稿限制，姿势可以任意变化，做起定制头像来，比Midjourney更可控、更像本人。控制权重可以根据自己的审美调整，找到合适的手感就行。

IP-Adapter还有一个扩展玩法：用来固定角色。虽然它目前不能百分百复刻真人脸，但足够稳定地维持同一个人的基本特征。我在SD1.5和SDXL两套环境里分别做了验证：SDXL推荐用plus face sdxl vit-h出图，SD1.5推荐用plus face sd15出图。

![](img/zhuanqian_c6e55e59f24931d09268c25506273d70.png)

![](img/zhuanqian_0d075db3152075b9b333661020ba455d.png)

![](img/zhuanqian_fae1199303d8e4cad8e843d7c0936259.png)

![](img/zhuanqian_4f0fa5a7fc39ca764d211d27617ce271.png)

![](img/zhuanqian_dc2fdb7f4cb463e15bbb2ef7ad8238c4.png)

![](img/zhuanqian_28dd7fe5a3613d696306ff07138d392d.png)

借着这个思路，我试了试快速生成手办和摆台效果：只需要一张人脸参考图，再配上一个“手办LoRA”和写实底模，就能做出稳定的Q版手办感。

![](img/zhuanqian_9cedf49c8796d9798e3ff5061e13eb79.png)

![](img/zhuanqian_9622eda57e4a4a290f6c326cce9131a3.png)

![](img/zhuanqian_493a9ff52728d90b0c5f138599cce820.png)

那次实验跑在SD1.5生态，选了一款偏厚涂质感的国产写实底模；LoRA来自Liblib。控制端只挂一个IP-Adapter，记得选1.5版本的face模型，预处理器和模型不能选错，权重则按效果微调。提示词里要出现几个触发词才会触发摆台效果：shouban、chibi、faux figurine。LoRA权重我加到1.2，是为了保证“摆台感”更明显；负面描述词我直接采用Liblib模型页提供的现成配置，你也可以自行替换。我的描述词写得很简单，所以生成基本以参考图为主；如果想自定义内容，可以自己补充服装或场景标签，比如给自己的汉服形象加一个Hanfu关键词。

最后说说LoRA训练。我现在使用中的头像，是以一个主打亚洲人像的英文缩写为BRA的底模来做训练、再换到另一款偏厚涂风格的底模上生成的，所以最终图像既能保留真人结构，又能看到厚涂质感。

![](img/zhuanqian_81569449f621087c2bc5be9f6e8583b3.png)

想保住生成底模原有的画风，训练LoRA时最好不要使用和生成时同一个底模。下面的宠物合照可以直观看到区别：最左是同一底模训练兼生成；右边几种则是用不同底模训练后、再切到厚涂底模来生成，可以看到右侧两张明显保留更多厚涂风。

![](img/zhuanqian_173d8640ab3246590f1956186e04eede.png)

![](img/zhuanqian_87c315827186123cb5b2038b8a27aa6c.png)

![](img/zhuanqian_3c2e1089919d6ae16963bde1e975d3fb.png)

做动漫头像也是同一个道理：比如用原生SD1.5训练LoRA，出图时再换到喜欢的二次元底模。最后，就用原生1.5模型搭配几款不同底模生成的成品作为收尾——训练方式和风格取舍，大家都可以按自己的喜好来调整。

今天想跟大家聊聊，在AI绘画里怎么让“人”长得像、风格也不跑偏。无论是做漫画风还是真人写真，方法其实有好几条，但效果和适用场景完全不同。我把自己踩过的坑和实测经验整理出来了，希望能帮到正在纠结的你。

先说漫画效果。现在的工具思路大致有三类，主要看你想还原到什么程度。

第一种，如果你希望画面完全跟着原图的结构走，那就直接用线稿控制。现在市面上大部分“人转漫画”产品，基本走的是这个路子——简单直观，但姿势、表情、发型基本都定死了。

第二种，你手头有一张真人照片，但既想保留发型，又想自由换姿势。这时候可以上ControlNet里的IP Adapter。不过要注意，它更适合做成漫画或偏Q版的效果。一旦想要写实或2.5D质感，相似度就会明显掉档，毕竟漫画讲“形似”，写实则更吃五官还原度。

第三种，也是我个人最推荐的方式：训练一个自己的LoRA。它能锁定脸部特征，但发型、姿势、表情都不受限，而且模型原本的画风也不会被破坏。唯一的门槛，就是需要准备更多的照片数据来训练。

我自己试下来，同样的模型下，用LoRA加ADetailer修脸，出来的图不仅像，质量也稳。相比之下，如果用IP Adapter或者Reference去参考原图，表情和发型就会被原图“拴住”，自由度低。我还专门试过Q版头像，IP Adapter很容易把脸搞崩，即便强行修脸，特征也保不住。所以到头来，还是LoRA+AD组合最省心。

![](img/zhuanqian_238c1220b20fbae359dbe6fdce81ecc5.png)

![](img/zhuanqian_2f1909b53548ec46035998276dcccce6.png)

![](img/zhuanqian_1d8bf15a798a4ca28ceb4208d6650ca9.png)

大家看上面这组，人物特征保留得就很稳，大模型自己的画风也没乱。如果换成ControlNet参考，同样底模出图就变成下面这样：

![](img/zhuanqian_530e627a0a31a647ae14c4cd904bf970.png)

![](img/zhuanqian_22ebf08d26bbc159b1f088881f577234.png)

![](img/zhuanqian_16b2802093eb37b7d80413570341d15b.png)

![](img/zhuanqian_b4d4cff05a33764c00c527bc26aaa92d.png)

能看出来，表情和发型基本被参考图拿捏了。

那个Q版头像我也折腾过，用IP Adapter或Reference，脸基本没法看；再上一道修脸，人的味道又丢了。只有LoRA配合AD修脸，才能同时拿下“像”和“好”两个指标，出图完全不费劲。

![](img/zhuanqian_a623852c8084ecde654128bd2b162781.png)

![](img/zhuanqian_92e48fac8f44bc15cda635a96280554e.png)

![](img/zhuanqian_290ab824930aded9e9b0b54392e25ba3.png)

模型用的是civitai上这个：https://civitai.com/models/143396?modelVersionId=159133

提示词很省事，不用搞特殊魔法，直接在1girl后面加little_girl就能出小女孩效果；想生成男孩，把1girl换成1boy、加个little boy就行。

我这个效果的具体参数也一并贴出来：

1girl, looking_at_viewer, outdoors, little_girl, street, <lora:xxx:0.8>, upper_body, masterpiece, best quality

Negative prompt: EasyNegative, badhandv4, bad-image-v2-39000, two human, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry

Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3465045641, Size: 512x768, Model hash: c8a8af0bdd, Model: bambiEyes_v10, VAE hash: 63aeecb90f, VAE: vae-ft-mse-840000-ema-pruned.safetensors, Clip skip: 2, ADetailer model: mediapipe_face_full, ADetailer confidence: 0.3, ADetailer dilate/erode: 4, ADetailer mask blur: 4, ADetailer denoising strength: 0.4, ADetailer inpaint only masked: True, ADetailer inpaint padding: 32, ADetailer version: 23.10.0, Lora hashes: "aj30_bra: 63abf49e02c0", TI hashes: "EasyNegative: c74b4e810b03, badhandv4: 5e40d722fc3d, bad-image-v2-39000: 5b9281d7c6ad", Version: v1.6.0

## 总结一下漫画这条路

先问用户想要哪种感觉：

1. 完全照搬原图画面 → 用linear线稿控制，这也是现在大多数“人转漫”产品的底层逻辑。

2. 一张真人图参考，发型尽量还原，姿势随意换 → 用ControlNet的IP Adapter。但它只适合漫画范儿，写实或2.5D会失真，因为漫画只要大概像就行，写实则对长相还原要求高得多。

3. 脸部特征锁死，但发型、姿势、表情都不限制，同时保持模型原有风格 → 训练LoRA，不过需要更多照片做数据。

关于练LoRA的具体门道，下一节聊真人写真时会更详细地展开。

# 再说真人写真

目前常见的路子大体三种：

1. 摄影棚场景实拍，后期修背景、服饰等。

![](img/zhuanqian_1016ce1ec85a0c0e43c4be596b8395c5.png)

![](img/zhuanqian_00ddd049f5da159f7ac25c9f2b84df44.png)

2. 拿现成写真图直接换脸。可以用roop，也可以训练人脸LoRA来换。LoRA训练好了效果很自然；训练得不好，成品就一言难尽。

3. 靠人脸LoRA直接生成。想换风格，可以再叠一个风格LoRA，比如妙鸭那类固定模板；或者直接用“人脸LoRA+提示词”自由发挥，适合各种创意场景。

下面重点说后面两种。

## 一、换脸法

换脸的好处是——脸以外的部分不用管，不容易乱来，整体照片质量很有保障。

### 1. roop / face swap

roop在茉莉公主那组测试里表现还行。现在还有个face swap，底层逻辑和roop差不多，效果也没太大区别，用法可以看这个：https://zhuanlan.zhihu.com/p/658605755

但有一说一，roop跟LoRA比，质感和自然度都差一口气。脸上有遮挡的时候，更容易翻车。

### 2. LoRA换脸

图生图时，把重绘幅度调到0.05（不调到0，是因为一些修脸插件在0时会报错），再配合AD、fe这类修脸插件，用LoRA提示词来换脸。

提示词写在修脸插件里，或者页面最上面的提示词框，二者皆可。关键是加一些质量词，比如best quality、masterpiece、highres、portrait等等，不然画质容易拉胯。

![](img/zhuanqian_760524d15258b7cb760598a0cb7bbc56.png)

![](img/zhuanqian_06d95047be010a258b11e71fe08de20d.png)

如果出图后脸特别糊，去高级选项那边把脸部尺寸调大就行。以fe为例：

![](img/zhuanqian_f0d21cabed7fe85cedaad2977505221a.png)

这样脸部细节就清楚多了。

LoRA训练得当的话，这个方式会比roop自然不少。不过偶尔也会出现“不像”的情况，这跟原图的表情和五官有关系。比如你训练数据里没有露齿笑，后期就不容易还原那种笑容状态。

LoRA换脸还能细分为两种情况：

1) 模板图不是模型生成的 —— 这时候不太好保留妆效。

2) 模板图本身就是模型生成的、提示词也已知 —— 那就有机会把原模板的妆效一起留下来。

下面做几个小实验。

### 3. roop和LoRA对比

底模用的是beautifulRealistic_brav5，在上面训练过对应的LoRA，换脸插件用AD的mediapipe_face_full。

roop的原图是这个：

![](img/zhuanqian_b060aa84e3ed4616ebd510ab70b15cff.png)

拿angelababy的一张写真来试，脸部局部有遮挡：

![](img/zhuanqian_dbbb39ea4d53af168b106b6e542db71f.png)

![](img/zhuanqian_cbffa8fc7efcff82b6db24488530f107.png)

![](img/zhuanqian_81bd69f7c22e6a0de55af03ebceac637.png)

这种遮挡情况下，LoRA还是扛住了相似度，roop却没有很好地还原脸。另外发现AD换脸时，脸部检测框会扫到手部，导致手指也发生一定变形。

换脸嘛，妆感基本都会被吃掉。就算LoRA带一点妆色，那也是底模自身的妆，不是baby的妆。

再用一张露齿笑的职业照试试：

![](img/zhuanqian_92403451152defecf2217c97637c1aa9.png)

![](img/zhuanqian_9cba24dc18e2e03fd1b1c4657133f175.png)

![](img/zhuanqian_c4805e6d4b8896fbc08aa969428bc335.png)

遇到露齿笑这种表情，LoRA换脸就有点力不从心了——形能对上，但说不清哪里不像，职业照要求的高统一度满足不了。之前接过几单职业照，客户点名要这种笑容，一共4个人，只有1个人的LoRA能正常出，其他3个怎么练都不像。最后是靠roop换脸再加手动修图，把脸部质感拉回来的。

露齿笑确实是硬骨头，原因有二：

1）模型本身对牙齿的绘制就不擅长。

2）就算客户数据里有露齿笑，每个人的牙也各有特色。我实验过，LoRA能把牙齿特点学个大概，roop出牙的风格则全都像一个模子。

所以真心不建议接露齿笑这种高难度图，哪怕妙鸭，露齿笑的模板也少得可怜，因为做出来也不太像我。

再看半身写真这组：

![](img/zhuanqian_02fdc7b2a3d9ac9580977f49284b8b51.png)

![](img/zhuanqian_7bb222c7dfdb76284d3aafb28ae2ec3a.png)

![](img/zhuanqian_517d04de8c5d43a1d87a78c5b296bdb2.png)

![](img/zhuanqian_5f02683803b2e9b8e33be51c8be8383c.png)

作为本人来打分，LoRA的效果更胜一筹——脸部光泽保留得比较多，只是掉妆。roop则总有一种过度磨皮、塑料假面的观感，脸部也显得平，高光全没了。

### 模板图由模型生成的情况

这里用一个妆感很强的LoRA风格试：美式证件照。

原提示词是：high quality, best quality, photorealistic, ultra detailed, extremely detailed face, textured skin, USportrait, 1girl, freckle, many braids, blue long sleeved shirt, red tie, headset, looking at viewer, blue background, studio lighting, <lora:usportrait_20230621151016:0.7>, navel

提示词1：best quality, masterpiece, highres, portrait, 1girl,<lora:aj30_bra:1>

提示词2：high quality, best quality, photorealistic, ultra detailed, extremely detailed face, textured skin, USportrait, 1girl, freckle, many braids, blue long sleeved shirt, red tie, headset, looking at viewer, blue background, studio lighting, <lora:usportrait_20230621151016:0.7>, navel,<lora:aj30_bra:1>

![](img/zhuanqian_af90f7676e3094689ebf2c40b5eca371.png)

![](img/zhuanqian_507655c7c1d60e33ade298734c273703.png)

![](img/zhuanqian_e00668f0be4afc19ee0d79147de3b06c.png)

![](img/zhuanqian_26229c951e920b3f13e55ff09a1fcf6e.png)

试下来，用提示词2能稳稳保留原图的妆感。

### 4. 顺手试了个小程序

最近看到不少写真类小程序，其中「绘之境」本质就是换脸逻辑。现在它训练LoRA免费，有好几个写真模板也免费，我就浅试了一下。

![](img/zhuanqian_4c99b28a95ddf8847a7420fc91101fb4.png)

用“紫梦花园”这个主图出了两张照片：

![](img/zhuanqian_847e4c6fcd0721d6f21c155663bce095.png)

![](img/zhuanqian_896c2159bbf8c1852e799d451a412f4e.png)

能看到妆感有点出入，但没有原图那么浓。另外换脸时，耳饰可能会悄悄变化。

看它的模板，其实也都是用模型生成的写真，本质上和妙鸭的“更像一点”是一个套路——只动脸部区域。所以这个小程序就是“模型生成图+换脸”，靠提示词锁妆效。

不过妆感这东西，出图后自己再上个美颜、加个妆容也能补。就我的体验来说，它换完脸的质感还可以，当然这跟我自己数据集质量好也有关系。我在小红书上也翻过别人的返图，包括妙鸭的，有些人脸发糊，那基本就是训练数据本身不清晰。

## 二、LoRA直出法

直接用训练好的人脸LoRA，走文生图路线，自由度非常高，能出各种创意画面。

也可以像妙鸭那样，另外训一个风格LoRA，再用ControlNet控制姿势，出图效果会更有保障。

### 1. 风格LoRA + ControlNet姿势

妙鸭的底层逻辑就是这样：用ControlNet的openpose控制景别。所以你会发现妙鸭很多都是半身照、大头照，聪明的避开了手部废片。另外它还支持上传姿势图参考，还搞了个盲盒模式，增加了不少趣味性。

还用刚才的美式证件照举例，如果希望它按特定姿势出图，可以这样设置：

![](img/zhuanqian_48b4f01bcbc6cead6ba87717b0dcfcb6.png)

这样一来，姿势就能高度还原。

### 2. 文生图做创意写真

SDXL出来之后，模型对提示词的理解能力明显上了一个台阶。我用xxmix模型训练了自己的LoRA，然后直接文生图，收获了好多有意思的写真。

（模型地址：https://www.liblib.ai/modelinfo/69c41904b2fc4ed896866b1f4dd2b240）

很多人跑来问是不是还得另外练风格LoRA？真不用，全靠提示词想象。

先放几张效果：

![](img/zhuanqian_db60ca840e26b90dd130e3cfcaf6528e.png)

![](img/zhuanqian_3210915dcad7ad592cfd8e952554e96b.png)

![](img/zhuanqian_db00870f62b7d9452d3849a26e4f895e.png)

![](img/zhuanqian_80e4397a20369991d27a12814dc4239b.png)

以碎纸为例，提示词长这样：

A woman made of Chinese art paper, ((with shattered paper skin)), face is made of shredded paper, calligraphy and landscape paintings on the paper,

high quality, best quality, realistic, photo, detailed skin, detailed face, realistic, photorealistic,

xxmix girl, <lora:ajia_xx_v1:0.8>, ajia, black eyes, bust, upper_body

Negative prompt: (worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), tooth, open mouth, nsfw

Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3717684114, Size: 768x1024, Model hash: ecb947b4ea, Model: XXMix_9realisticSDXL(Test)_Test_v2.0, Style Selector Enabled: True, Style Selector Randomize: False, Style Selector Style: base, ADetailer model: mediapipe_face_full, ADetailer confidence: 0.3, ADetailer dilate/erode: 4, ADetailer mask blur: 4, ADetailer denoising strength: 0.4, ADetailer inpaint only masked: True, ADetailer inpaint padding: 32, ADetailer version: 23.9.1, Lora hashes: "ajia_xx_v1: e2b01d92cf91", Version: v1.6.0

说白了，就是放开想象力，把你想要的画面描述出来就行。

最近还出了明星下车照、中秋主题。文生图的另一个好处是能随便融合风格，比如叠加工笔画风，出来的味道立刻就不一样了。

![](img/zhuanqian_05e4c96f966b2cb78202018d40a23d49.png)

![](img/zhuanqian_80704e1d21422a09128d3c735ea596b0.png)

![](img/zhuanqian_9826bc20443ef429b07a48eb86b2300c.png)

上面那些可用的词条，本质上都是围绕同一组基础描述词扩展出来的，只需要在最上方加上场景描述即可。

high quality, best quality, realistic, photo, detailed skin, detailed face, realistic, photorealistic,

xxmix girl, <lora:ajia_xx_v1:0.8>, ajia, black eyes,</lora:ajia_xx_v1:0.8>

小提醒一下：若生成时面部出现虚化，未必是 LoRA 本身的问题，提示词的质量权重也很有影响，该加的质量类词还是要保留。

## 四）LoRA 训练实战经验

前面聊 LoRA 聊了很多，有小伙伴想动手却无从下手，这里我就按自己最顺手的流程，讲讲我是怎么快速跑通训练的。

从零安装不展开，想看详细搭建可以去看吴东子写的 LoRA 训练攻略或 B 站上的教学视频，这里主要做踩坑避雷，让上手更快。

### 1、炼丹工具怎么选

纠结工具的话，直接上秋叶的炼丹脚本就行，用起来最省心。

从 6 月用到现在，我一直靠它。

下载地址【AI绘画】模型训练器发布！简单又不失专业的LoRA模型训练一键包_哔哩哔哩_bilibili

视频简介里有网盘链接，基础操作也能在视频里跟着学。

中途也试过赛博炼丹炉这类工具，后来维护停了还总出 bug，现在我只把它当作打标工具用，删标签、改标签确实很方便。

### 2、数据集准备

我的方向主要是人像，所以下面说的也以人像训练为主。

1）清晰度要够

数据质量很重要，即便都是 512*512，单反拍出来的和手机前置的效果天差地别。

要避开噪点大、模糊泛白的图，也要保证多样性，光线、色调别全一样，不然很容易过拟合。

![](img/zhuanqian_c9ec4543f4a7912cc59a14f1b1e28025.png)

![](img/zhuanqian_b668b32f638aff33f526c0ca0a93a1e9.png)

2）大头照还是全身照？

有人担心只用大头照训练会只出大头，其实画面比例是可以靠提示词控制的。我展示的效果里，LoRA 都是大头照训出来的。

以 SDXL 为例，我的训练集一共 20 张：

![](img/zhuanqian_e408e5e30ed41f80e5e2df50201b88d8.png)

所以想做人像，直出更建议先用大头照。

之后可以混进少量半身、全身照做补充。我不太爱加半身照，因为衣服信息很容易污染 LoRA。

大头照目前我还是手工裁的，自动检测偶尔不够准。

### 3、打标签

大头照打标相对简单，我基本走自动流程，人工干预很少。

有赛博炼丹炉的话可以用它来打标，下面以它为例。

打开后上传素材，现在素材已经是大头了，就不需要额外脸部增强了。

![](img/zhuanqian_c06bd86237177d69f91763ed57616bce.png)

点预处理拿到标签后，要删掉和面部特征强相关的词，我一般会删掉 lips 和 nose。

![](img/zhuanqian_7ecbe76944b471bc23be18e5ec17aea4.png)

再检查一下眼神方向有没有标错，比如实际看向侧边却被标成看向镜头：

![](img/zhuanqian_8dab402503943198b1d15e65f5675541.png)

这种朝向标错，训练出来容易出现斗鸡眼，素材最好先筛掉。

整理完后点「打开训练集」，把 image 文件夹直接复制到秋叶训练包的 train 目录下，重命名一下就可以开始准备训练了。

![](img/zhuanqian_2ef17b56115799455d0ce92e3721f117.png)

![](img/zhuanqian_efc48dc857b32d94876698c689e0ea9e.png)

### 4、参数设置

参数调参党可以先放下心，基本用默认就行，只改底模路径、训练轮数之类的，学习率没必要特意去动。

我用 20 张人脸，习惯设 repeat20、epoch10、batch1，出来的模型 7-10 个基本能用。

优化器就用 AdamW8bit，体验不错。

换别的优化器 loss 掉得快也不代表效果好，数据集里只要有一张很糊，loss 很低的模型可能就学到了糊的特征，生成也会糊。

### 5、底模选择

SDXL 建议同款底模训练同款底模出图，拟合度更可控，不会过拟合得太严重。

SD1.5 更容易过拟合，如果想要保留原底模质感，可以考虑直接用 SD1.5 基模训练，或用相关底模训练。比如我会用 bra 模型训 LoRA，再去 magic 出图。

### 6、训练后测试

测试最好用 xyz 图表，提示词尽量选原图里没有的新元素，比如白头发、赛博朋克背景之类。

测试时的提示词要写好，生成质量和提示词关系很大。

## 五）IP Adapter 参考写真风格

我平时出人像写真比较多，最近的一些心得总结如下。

1、不必绞尽脑汁写提示词，光线滤镜风格都能跟着参考图走，滤镜 LoRA 基本可以省了。

比如荷叶写真，我就参考了妙鸭的胶片感。

![](img/zhuanqian_598a935cf8ad91a963872cfe7e9e633c.png)

![](img/zhuanqian_8d14d34dd292860c83b23fa707999171.png)

![](img/zhuanqian_9b24c551e74f6e36ab38638d85b19139.png)

飘起的发丝、发丝透光的感觉都参考出来了。

2、发型、妆容、画面元素都能跟着搬

比如 baby 的那种头发，怎么写提示词都难描述。

![](img/zhuanqian_34bf72acf74fd2da34065d1edc2ae553.png)

用 IP Adapter 直接迁移就很稳，内行才懂。

![](img/zhuanqian_554026c859d5e9e3e6946239aeca2608.png)

再配合自己的 LoRA 跑脸。

![](img/zhuanqian_729561d6c8ee4d293c3cf09fbc123c5c.png)

使用时如果效果不理想别急着放弃，多调一下权重就行。

比如我上图时会出现刘海单独变黑，或嘴巴过度参考原图导致嘴唇过厚。

解决办法是把控制权重稍微拉低，比如降到 0.85。

我日常用的权重通常更低，在 0.5 左右。

指定背景风格

最近的一个新尝试。

有朋友问 AI 模特怎么固定背景，训练 LoRA 对场景约束有限，SD 本质上很难让场景完全一致。

试了 IP Adapter 后发现确实能把背景元素带进来，只喂一张环境图就能正常出人像。

![](img/zhuanqian_1cec361daf7c3bf2630002640c9e2256.png)

![](img/zhuanqian_03a5a49ab2ee3f760cd260661faed420.png)

权重太高会崩，调低一点就还行，甚至能“把我带到东方明珠下面拍照”。

不过 SD 画建筑细节比较弱，放大的话会显得假。

朋友反馈说背景风格确实有点像了。

![](img/zhuanqian_94946fbf68bc701ee0fc219f50aae519.png)

![](img/zhuanqian_f8d7df29ddcf7deb7f7107d33c83e2b0.png)

但要做到完全统一比较难，只要风格统一就已经不错了。

## 六）总结

本节对换脸和直出法做了大量实验。

换脸方面：

优先 LoRA，想保留妆感就用带妆感的 LoRA。

roop 效果一般，后期还需要美颜微调。

LoRA 直出方面：

选一个能力强的基模，靠提示词发挥创意，效果范围更大。

需要固定风格时，可配合风格 LoRA 控制。

另外 IP Adapter 用好了，可以直接借鉴别人的写真风格，非常好用。

# 六、结语

以上就是我目前在人像出图上的全部研究心得。感兴趣的话，可以用这些方法做人像，不管是漫画头像定制还是创意写真定制，都是有市场的。

最后感谢赚钱提供的平台，感谢靠谱姐让我认识赚钱。

我是今年加入赚钱的新人，已经参加过两次航海，8 月的 AI 绘画＋自媒体航海认识了不少优秀教练。

感谢明月教练主导的《AI 绘画一本通》，照着手册学到很多新技巧。

感谢小鹅教练关于审美的分享，每次干货都很大，还总会给我们鼓劲，真的很暖心。

另外加入赚钱后感觉运气变好了，刚来就抽中了定制 T 恤，会员日还抽中了 sky 盖哥的 AI 绘画课程，开心到飞起~

赚钱的帖子每篇都很高质量，期待自己快点成长，也能给更多人分享经验！