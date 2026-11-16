# AI拟真魔法：三步把纸片人变成写实真人，还能顺手赚BGM推广费



各位朋友，我是龙哥。喜欢动画和游戏这些年，我总在脑补一个画面：那些活在二次元的角色，要是落到现实世界中会长着一张怎样的脸？没想到AI绘画如今把这个脑洞变成了实际可玩的操作。无论是动漫人物、游戏英雄、古代卷轴上的美人，还是早年网上的🐧头像图，都能被改写成精细的写实人像。这项玩法既可以满足好奇，又能用作文史科普、课堂辅助；更棒的是，把成品剪辑成短视频发出去，吸粉涨赞之余，还能通过音乐商单赚钱。今天这篇就手把手拆解全流程，配套模型也全部打包在文末云盘，省得大家到处找。整理起来挺费心血，希望你能用得上。

# 一、AI拟真可以还原哪些角色

## 1. 动漫人物写实化

我小时候痴迷《火影忍者》，里面某个女角色的真人版，AI还原成了这个样子：

![](img/17be73c98dae67ddd4055a5758a31bf7.png)
![](img/096a78049f8bf9e807ef8f94227be3a7.png)
![](img/6b588fe33e635174b99b056029a5156c.png)

童年女神静香也有了现实版，看起来依然清纯可爱：

![](img/b5445ed1ee5a742c4393a0470fc2b408.png)
![](img/7af6ee2685987008ded0ed92a830b556.png)

## 2. 游戏角色写实化

游戏里的人物同样能完成真人化转变。这是《王者荣耀》里的一位英雄：

![](img/1730680f75cadc80c4d8a96929fc657c.png)
![](img/6b8190812e8c8ffd8d1e47a5fae7e6a8.png)
![](img/568b68058e53d655224769b437eb23dd.png)

这是《拳皇》里的战士：

![](img/de2124ac86260d1a2254f809b41b03ad.png)
![](img/b06dbcb44e7cfb51dbd7f3face23e2aa.png)

## 3. 古代画像写实化

小学课本里的四大美人，画像太抽象，我一直好奇她们真实容貌。现在AI把它们推演成了具体人像。杨玉环被还原成这样：

![](img/fa851ec1659c6156633c06c66061d725.png)
![](img/9c05223edb1bd76e6158aa2074df9192.png)
![](img/ad86c210180be58f806a9ed77bdb2b2c.png)

乾隆皇帝也有了真人版面孔：

![](img/5cd0c5e6b29f29af4d9bcf486e9f0490.png)
![](img/7d8885d7456cfe7a53813f4f7c019d99.png)

除了上面的类型，只要是非写实图像，包括早期🐧头像，都能拿来改造：

![](img/e70b35771a35418bd4dd7d42c03a5ee5.png)
![](img/46fa2dcc65a3bac32e782e6c143c88dd.png)
![](img/13451eadb6131abd32bc5d8b5350b0ce.png)
![](img/9eab09efe693e7266261d9006f3ea21a.png)

## 4. 用成品引流和变现

在抖音平台，已经有人专门做“动漫美女变真人”的账号，多条视频收获几十万点赞，粉丝也逼近50万：

![](img/232e0e3e35f9b8126e55c9ca480cb085.png)
![](img/dba83dcc7a3500f32b57a56eb92bc1f0.png)

再给视频加入BGM，就可以参与音乐推广分成。而且AI拟真内容本身眼球效应强，相比常规音乐号，转化优势更明显：

![](img/16a81a0181bc57cf5bf84713f998ed9a.png)

接下来，我把详细制作流程完整展开。

# 二、两条拟真路线

想做动漫转写实人像，主流方向有两种。

一种是“死磕原图”，把构图、姿势全部保留：

![](img/153d5ffa8f8ee266df3430b34ebc9005.png)
![](img/762eb065360d79f2e1e77d062b669f2a.png)

另一种是“提取特征”，只学习人物的外观设定，但改换全新的构图和姿势：

![](img/4fc8bc38b48640c91b3eb7f7d4664d0c.png)
![](img/668c3a2f7c64cb6def80409499eedc11.png)

下面按不同情况分别说明。

# 三、严格还原原图的完整做法

要保留参考图的构图和姿势，可以借助两个工具：img2img，以及ControlNet里的Tile模型。先看三张对比效果：

![](img/06c3cc63a9f53f3ccf42205aab828184.png)
![](img/3092a030b7128ef8bab43e61c12af970.png)
![](img/d57b27584b338115ba6eccdd98811ba7.png)

两条路线产出的图肉眼难分高下，但Tile会更主动补充细节，甚至会加上一些原图本来没有的元素。

整个流程可划分为三步：挑底模、写提示词、调参数。两种方法只有最后一步不同。下面就用这个动漫角色作例子：

![](img/9c3fe5fa127a30d42ff074d968c49c48.png)

## 1. img2img流程

### 01. 选择底模

必须使用写实向底模。我常推两款：majic Mix和极氪写实MAX。它们出图质感在线，人脸也漂亮。文件已经在云盘里，自取即可：

![](img/82193aa755d487d23a1b189c7debc7f9.png)

### 02. 编写提示词

提示词的核心是准确描述原始画面。推荐用WD1.4标签器辅助生成描述。打开标签器，左侧上传原图，右侧自动给出描述词：

![](img/00ad89ed31dbbc456b11b868439c79c1.png)

把结果复制到翻译软件，粗查一遍，剔除无用的词条，比如haruno sakura、肚脐切口、头发入口、衣服切口等：

![](img/1e1ecdca763066ca9c3b7799ba1f2323.png)

接着追加画质词，比如大师杰作、最高质量、超高分辨率。想要人脸更养眼，关键要叠加Lora模型。云盘里有几款常用Lora，不同权重能组合出不同气质的女生：

![](img/6b18ca56bcad920d6765ca1bd0cc2c4c.png)
![](img/3fd95b750838afaf9ce109b4d22cc8f6.png)

于是最终提示词是这样的（中英文对照）：

英文：

Best quality,masterpiece,ultra high res,(photorealistic:1.4),
1girl,solo,pink hair,navel,long hair,crossed arms,green eyes,forehead mark,cherry blossoms,looking at viewer,red hairband,hairband,jewelry,breasts,earrings,sleeveless,closed mouth,smile,bare shoulders,medium breasts,floating hair,branch,stomach,
<lora:mix4:0.4>,<lora:>,<lora:gini_s2:0.3>,</lora:gini_s2:0.3></lora:></lora:mix4:0.4>

中文：

最佳质量，杰作，超高分辨率，（照片真实感：1.4），
1女孩，独唱，粉色头发，肚脐，长发，双臂交叉，绿色眼睛，前额标记，樱花，看着观众，红色发带，发带，珠宝，胸部，耳环，无袖，闭着嘴，微笑，裸露肩膀，中等胸部，漂浮的头发，树枝，胃，
<lora:mix4:0.4>,<lora:>,<lora:gini_s2:0.3>,</lora:gini_s2:0.3></lora:></lora:mix4:0.4>

通用负面提示词也已备好，直接粘贴进SD即可：

EasyNegative, ng_deepnegative_v1_75t, badhandv4,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), bad anatomy,DeepNegative, skin spots, acnes, skin blemishes,(fat:1.2),facing away, looking away,tilted head, lowres,bad anatomy,bad hands, missing fingers,extra digit, fewer digits,bad feet,poorly drawn hands,poorly drawn face,mutation,deformed,extra fingers,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,teethcroppe,signature, watermark, username,blurry,cropped,jpeg artifacts,text,error,

提示词这块就齐了：

![](img/36cae53640a6760f354b1ca398b47567.png)

### 03. 调整参数

进入img2img面板，先上传原图：

![](img/4269939b43d74732c5f26e3b11d487ab.png)

然后参考下面的数值：迭代步数30，采样器DPM++2M Karras。重绘尺寸按原图比例来，点三角尺即可自动同步。同步后数值不合适，就自行除以2或乘以2，控制在1000上下即可：

![](img/cd4b3d98af7b33bc4d8791a3e6987e3b.png)

接下来是最为关键的重绘强度。这个参数决定了输出图像与原图的接近程度。建议先设为0.5试跑一张，再根据结果微调。不同素材需要不同强度，只能自己反复试。画面不够真实，就调高强度；画面离原图越来越远，就调低。

![](img/30a1d88d9bfbb789f1e39271f6bd2670.png)

可以看看下面这些对比，强度越低，还原度越高：

![](img/a19dded59116d3c787a0d18ffec45827.png)
![](img/5b4c98de5fd948d6218498a18e68a227.png)
![](img/f3659bae5d205d317beead3818a4f24e.png)

最后点击生成，一张动漫角色的写实头像就出来了：

![](img/9959e35954f24481a5a8c28cedef0b36.png)
![](img/06c3d3b9e701793768a00af557e6af90.png)

## 2. Tile流程

第二种做法，是在txt2img中接入ControlNet。底模和提示词部分完全复用刚才的配置，直接拷贝即可：

![](img/1c2276da16c86a2a5f95e64726344495.png)

第三步参数照旧：

![](img/c6ec62278b30b0f6cbffb17cb2ad1ffc.png)

差别集中在ControlNet区域：上传原图，勾选“启用”和“完美像素模式”，控制类型选择Tile，控制权重约0.7：

![](img/1e2de7f869ddaf80f8ea896a50a10eaf.png)

设置完毕，点击生成：

![](img/53144c61700976ad322032f2e2172654.png)
![](img/5cdec17572a59f4183669169e90a7748.png)

两种方法最终成片观感接近，只是细节风格略有不同。大家各试一次，挑顺手的用即可：

![](img/ba0bd4ec614780b4edef0974d09900ff.png)
![](img/bf62cf355c4a3128884242ce86e317b0.png)
![](img/b5e79a249ea4b1dee6a6f52900c28336.png)
![](img/6e3abbcec36e04fa06e81de0042f072d.png)
![](img/4d7c0d2eb86fd4a7d231270a0cf48876.png)
![](img/1d1747131f321b902aee1825766a5f9c.png)

# 四、只提取角色特征的进阶玩法

前面两种方法都会严格保留原图构图。如果想让角色换动作、换背景，可以改用ControlNet的IP-Adapter模型。先看两组样片：

![](img/4058e03def2b90b9f3c1056a5c0e9291.png)
![](img/c343815487c62c68cd86e495ccdc1ab1.png)

操作依然分三步，底模和提示词沿用前面设定的内容：

![](img/66d26186bdfac2e66e7b204d0f532972.png)

在ControlNet区域，模型选择IP-Adapter，控制权重同样设置在0.7左右：

![](img/031baa7e0319d087a6b291254ef36a1f.png)

成品会吸收原角色的相貌和衣着特征，但姿势和构图可以完全自由发挥：

![](img/01310a1a539afc9cf01780c7a203bf76.png)
![](img/c5b2e577a37d7ccb56509d63c613dd90.png)
![](img/b272b431ee38fefbdd49af783891f33a.png)
![](img/2596e7913bf3c0c57108ea4ea6d3d285.png)

# 五、特殊难题的救场方案

不过有些动漫角色并不“好伺候”。比如静香、阿尼亚这类身体比例、五官比例和真人差距太大的角色，直接转换有可能变成惊悚图：

![](img/96b0f0d57d987cc4b5a13300bcdc84ef.png)
![](img/843a0f124807694e9990c373e49d08c1.png)

针对身体比例失调，最有效的做法是裁剪原图，仅保留头部一带：

![](img/5a185612146c550c68c926150ed7d37b.png)

针对五官比例不对，尝试加大重绘强度进行调整：

![](img/84626d680a507e97746a6920572a9c4f.png)
![](img/2952b03f84124776b8815000094f1233.png)
![](img/109c3a695d6a3254d84b5e1371f84e66.png)
![](img/2d3cff8f7416ec53e85b7c2726a0d7c8.png)

也可以换用IP-Adapter处理，效果如下：

![](img/4fc4550fb4ed101fb8b1b8e245d7f95f.png)
![](img/aa4788cca257e00a43d6f38b63b5a7f2.png)
![](img/ca0f5f9b645c22a95c9a1b4384c7d2f8.png)
![](img/7649239deb4115fa635b9b0bd337c5cc.png)

# 六、结语

到这里，完整攻略就结束了。希望你能亲手将自己钟情的二次元角色带到现实世界，玩得开心。

各位读者朋友，本期内容就到这里啦！我是吴东子，咱们下次推送再碰面。要是需要相关资源，我已上传至百度网盘，大家按需取用即可。链接在此：https://pan.baidu.com/s/1Dq4IE8q_ZfJdVeuxHGlkjA?pwd=wdz6 ，提取码依旧是 wdz6。我们下篇文章见！