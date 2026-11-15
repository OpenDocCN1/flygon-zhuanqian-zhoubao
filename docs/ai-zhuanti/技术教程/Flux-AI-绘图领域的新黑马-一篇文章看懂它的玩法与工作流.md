# Flux：AI 绘图领域的新黑马，一篇文章看懂它的玩法与工作流
大家好，我是龙哥，目前生活在深圳。2023 年，我曾在赚钱分享过两篇 AI 绘画相关的精华内容。2024 年基本处于观察状态，后来偶然看到龙哥发起的龙珠悬赏，想到自己平时接触过不少 AI 工具，于是决定整理这篇长文，和大家聊聊近期热度非常高的 Flux。
最近，小红书上的矩阵美女账号突然大量涌现，背后常见的组合就是：Flux 生成高真实感人物照片，再搭配可灵、海螺等工具制作视频。
不少原本完全不了解 AI 绘画的朋友也来询问 Flux。但当他们得知需要学习 ComfyUI 工作流后，往往还没开始就先放弃了。
实际上，ComfyUI 的使用门槛正在不断降低。除了本地安装之外，现在还可以选择在线平台直接使用，例如哩布；也可以租用云端显卡服务器，比如仙宫云、揽睿等。对于开发者来说，还能把 ComfyUI 工作流封装成小程序，让普通用户直接调用。
所以，即使不会 SD 或 ComfyUI，也不代表无法使用 Flux。很多现成工作流已经被部署好了，小白只要选择模型、填写提示词，就能完成出图。
## 本文涉及的工具
| 工具 | 主要用途 | 收费情况 | 地址 |
| ComfyUI（Flux 工作流） | AI 写真、电商商品图、视频转绘、AI 模特换装 | 本地部署免费；云端 4090 显卡约每小时两千多 | 本地部署 |
| 哩布（blib.ai） | 在线生成图片 | 每天提供一定免费次数，超出后收费 | https://www.liblib.art/、https://tusiart.com/ |
| 可灵 AI | 国产 AI 视频工具，国内头部产品 | 每天赠送 66 灵感值 | lingai.kuaishou.com |
| 飞影数字人 | 制作数字人口播内容 | 收费 | https://flyworks.ai/login |
## 文章结构
第一部分：认识 Flux AI 绘画模型
第二部分：Flux 的典型应用案例，包括小红书名媛、新闻女孩、Lora、PuLID 等
第三部分：Flux 的四种使用方式
# 一、Flux 为什么被称为 AI 绘画新王者？
很多人听说过 Flux，却还不清楚它究竟是什么，以及它能够解决什么问题。下面先做一个基础介绍。
如果你已经长期使用 ComfyUI，或者对 Flux 非常熟悉，可以直接跳过这一部分。
## 1. Flux 的诞生背景
今年 3 月底，Stability AI 面临资金和经营方面的多重压力，公司内部也发生了较大变化，联合创始人被解职，核心成员 Robin 随后离开。
沉寂了大约四个月后，原 Stable Diffusion 核心团队重新出发，推出了全新的开源文生图模型 FLUX.1。
这个模型一经发布，就被认为在多个维度上具备挑战 Midjourney 和 DALL-E 的实力。其背后的新公司 Black Forest Labs，也很快获得了 3200 万美元融资。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8be5c15ae0a734ef2a4e652fb885ac9a.png>
经过数月筹备，Robin 对外公布了新的创业项目，并成立 Black Forest Labs。2024 年 8 月 1 日，Black Forest Labs 正式发布 FLUX.1 图像生成模型。
按照官方介绍，FLUX.1 在图像细节、提示词理解、风格表现以及复杂场景还原方面，都达到了行业领先水平。
从官网公开的 ELO 评分来看，FLUX.1 的表现已经超过 Midjourney V6.0 与 Stable Diffusion 3 Ultra。
官网地址：https://blackforestlabs.ai/
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_448032738d35f524d29f236580df3b44.png>
## 2. Flux 的核心优势
评测里经常把 Flux 形容得非常强，那么它具体强在哪里？
### 更高质量的图像表现
Flux 可以生成更高分辨率的图像，并且支持自定义画面比例。无论是正方形、竖版还是其他构图，都可以直接设置。
在视觉美感和整体质量评分方面，Flux 在不少测试中已经超过 SD3 和 MJ6。
### 人体结构更加自然
过去 AI 绘图最容易暴露问题的地方，就是手指、脚趾和人体结构。
Flux 在手脚细节上的改进非常明显，出现多指、少指、肢体变形等情况的概率大幅降低。虽然并不是每一张图都完美，但整体稳定性已经有了很大提升。
### 更准确的文字与提示词理解
Flux 对英文文字的生成效果较好，同时能够理解更加复杂、具体的提示词。
对于新手来说，可以简单理解为：
> Flux 生成的图片更清晰、更真实，人物手脚出错的情况也更少。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b9dd3d28d6a23cb139ec0f9192836d21.png>
# 二、Flux 可以应用在哪些场景？
下面通过几个实际案例，看看 Flux 在内容创作中的具体用法。
## 1. 新闻女孩：Flux 出图，可灵转视频
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fd53c062fc62ed5a0e57282a13200d53.png>
此前，一组由 FLUX Dev 生成的“新闻女孩”照片在推特上迅速走红。后续再使用 Runway Gen3 生成视频，配合数字人口播后，成片的真实程度甚至让很多人难以判断真假。
更重要的是，这类效果并不一定需要复杂节点，使用最基础的 Flux 工作流就可以完成。
## 基础工作流操作步骤
工作流名称：`flux1-dev.json`
使用方法：
1. 导入 `flux1-dev.json` 工作流；
2. 选择对应模型，显存较小的电脑可以优先使用 FP8 版本；
3. 输入英文提示词；
4. 根据需求设置画面尺寸，例如 1024×1024 或 1024×1536；
5. 点击运行，等待生成结果。
模型目录：
```text
ComfyUI\models\unet
```
工作流与模型可以在文末网盘获取。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dc245571d4603612c1a4017b027d696e.png>
## 新闻女孩提示词
### 英文提示词
```text
A captivating young china woman is captured mid-speech,exuding confidence and charm. Her long,black hair cascades down her back,and her bright,expressive face is accentuated by a subtle,sultry smile. Her piercing green eyes sparkle with intelligence as she gestures with her left hand,showcasing a delicate silver ring on her pinky finger. She holds a sleek,black microphone in her right hand,speaking with passion and convicti
She wears a fitted, The uniform is adorned with intricate,shimmering patterns that catch the light,adding a touch of sophistication and glamour. A green lanyard with multiple badges and logos hangs around her neck,featuring the "AIGC" logos prominently.
Behind her,a blurred background with a white banner containing logos and text suggests a professional or conference setting. The overall scene is vibrant and dynamic,capturing the energy of a live presentation. The woman's poised demeanor and alluring smile command attention,conveying a sense of intelligence,confidence,and subtle sensuality.
```
### 中文理解
画面中是一位正在演讲的年轻中国女性。她留着乌黑的长发，神情明亮，自信而富有吸引力，脸上带着若有若无的微笑。
她一边用左手做手势，一边进行演讲，小指佩戴着精致的银戒指。她的右手握着黑色麦克风，表现出充满热情与感染力的状态。
她身穿合体制服，衣服上带有细致闪耀的纹理，颈部佩戴绿色挂绳，上面挂着多个徽章和标识，其中突出显示“AIGC”字样。
背景虚化，后方可以看到带有文字和 Logo 的白色横幅，整体环境类似会议或专业活动现场。画面氛围明快、动态感强，人物呈现出智慧、自信以及适度的魅力。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f250c37bae3211d300be384e7f9807eb.png>
Flux 生成的人物已经足够逼真。过去的 AI 图片通常一眼就能看出合成痕迹，而现在生成质量较高的图片，仔细观察很久也未必能判断出来。
当然，生成过程中仍可能偶尔出现手部、五官或局部细节异常，需要人工筛选和后期处理。
## 使用可灵生成视频
将图片导入可灵，输入类似下面的动作描述：
> 一位女士正在交谈，她面带微笑，并在说话时配合手势。
等待视频生成后，还可以继续使用飞影制作数字人口播作品。
飞影地址：
https://flyworks.ai/login
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3741fadab7e9584b603b4c99e1c596d7.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d1afdff7e3a64d3be9375611ab6eca5d.png>
## 2. 小红书名媛：加入 Lora，让人物更加真实
相比新闻女孩，制作小红书风格的名媛写真会复杂一些。
通常需要在基础工作流上替换 Flux 模型，加入人脸 Lora，再叠加细节增强、美颜等效果。这样生成的人物会更加稳定，也更接近真实摄影作品。
但需要注意的是，即便使用了增强节点，AI 仍可能出现手指、脸部结构等问题。实际制作时，最好加入修手、修脸等后处理节点，对瑕疵进行修正。
## Flux-Lora 工作流操作方法
工作流名称：`FLux-lora 工作流`
操作步骤：
1. 导入 Flux-Lora 工作流；
2. 选择合适的 Flux 模型；
3. 加载对应的人脸 Lora 或风格 Lora；
4. 设置参数；
5. 输入英文提示词；
6. 选择图片比例，例如 1024×1024 或 1024×1536；
7. 点击运行并等待生成。
模型存放位置：
```text
ComfyUI\models\unet
```
Lora 存放位置：
```text
ComfyUI\models\loras
```
通过替换不同模型和 Lora，就可以批量生成不同人物、不同风格的写实照片。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c061f0566bb26b66b6274104ba2fde42.png>
## 示例提示词一：骑行人物
### 英文提示词
```text
This is an image of a person wearing a pink and white cycling outfit, which includes a jersey, shorts, and a helmet. The person is sitting on a red bicycle, and there's a field with trees in the background. The person is wearing sunglasses and has long hair. The setting appears to be a rural or semi-rural area, given the open space and the presence of trees. The cycling outfit suggests that the person is engaged in cycling as a sport or recreational activity.
```
### 中文理解
画面是一位穿着粉白色骑行服的人，服装包括骑行上衣、短裤和头盔。人物坐在一辆红色自行车上，身后是一片带有树木的田野。
人物佩戴墨镜，留着长发。开阔的环境和自然景观，让画面看起来像乡村或郊区。整套骑行装备说明人物正在进行运动或休闲骑行。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ca84304ac0db81903d7bea5c8f57d256.png>
## 示例提示词二：海滩写真
### 英文提示词
```text
The image is a high-resolution photograph featuring a young Asian woman standing outdoors on a sunny beach. She has long, straight, dark brown hair and a fair complexion. She is wearing a fitted, light grey short-sleeve top with a square neckline and a high-waisted, grey pencil skirt that accentuates her slender physique. Her outfit is stylish and modern, with a minimalist aesthetic. She is holding a small, tan leather handbag over her left shoulder, and her right hand is raised in a peace sign, adding a playful touch to her expression. The background reveals a tranquil beach scene with a clear blue sky and gentle waves lapping the shore. A tall palm tree with a smooth trunk stands to her left, and a row of white lounge chairs with cushions is positioned behind her. The beach is sandy, and a few distant figures are seen enjoying the sun and the water. The overall mood is relaxed and serene, capturing a moment of leisure and enjoyment.
```
### 中文理解
这是一张高分辨率海滩照片。画面中，一位年轻的亚洲女性站在阳光明媚的海边，拥有笔直的深棕色长发和白皙肤色。
她身穿浅灰色短袖上衣与高腰灰色铅笔裙，方形领口和简洁剪裁让整体造型显得现代而利落。她左肩挎着一只浅棕色皮包，右手比出剪刀手。
背景是宁静的海滩、湛蓝天空和缓慢拍岸的海浪。人物左侧有一棵高大的棕榈树，身后摆放着带坐垫的白色躺椅。远处可以看到正在享受阳光和海水的人群，整体氛围轻松、舒适、悠闲。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f5323169a27342268d3ace1434ec4f78.png>
## 示例提示词三：街头生活感照片
### 英文提示词
```text
This is a photo of a person standing on a street. The individual is holding a pink teddy bear and a bottle of water. They are wearing a white dress with a black cardigan, and their hair is styled in loose waves. The person is also wearing a watch on their left wrist. The background shows a residential area with houses and a car parked on the street. The sky is overcast, suggesting it might be a cloudy day. The person appears to be posing for the photo, and the overall mood of the image is casual and relaxed.
```
### 中文理解
画面中，一个人站在街道上，手里拿着粉色泰迪熊和一瓶水。
她穿着白色连衣裙，外搭黑色开衫，头发自然地呈波浪状，左手腕上戴着手表。背景是一片住宅区，可以看到房屋和停在路边的汽车。天空阴沉，像是多云天气。
人物似乎正在面对镜头摆拍，整体画面偏生活化，氛围自然轻松。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4c4a2465176b95f798cac170fb7775fd.png>
# 三、提示词从哪里获得？
如果不知道如何写英文提示词，可以采用下面几种方式。
## 方法一：直接参考模型页面
在哩布、吐司或 C 站中，找到对应的模型或 Lora 页面。
许多作者会在页面中公开生成参数和提示词，直接复制并根据自己的需求修改即可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e2580367ca671ae8598f70c7e500829e.png>
## 方法二：借助反推工具
还可以通过图片反推出提示词。
目前常见的工具包括 SD、WD14，以及一些专门的图像描述工具。上传图片后，工具会尝试分析人物、服装、环境、构图和风格，并生成相应的提示词。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_934e5d89607bd941e6c6f7fa6606fd5e.png>
## 方法三：使用反推提示词工作流
在 ComfyUI 中，也可以利用工作流来完成图片分析。
例如 Joy_caption 插件，就是目前比较好用的提示词反推工具之一。它能够根据图片内容，生成较为详细的画面描述。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bb9598eb92bc005dc1566bb5d028a093.png>
除此之外，还可以继续尝试更高级的组合方式，例如：
- 图生图工作流；
- WD14 反推提示词节点；
- 使用大模型分析图片；
- 借助 IP-Adapter 进行风格迁移；
- 结合参考图控制人物与画面风格。
# 四、Flux 模型与 Lora 生态
前面提到的 Flux 模型和 Lora，通常可以在哩布等在线平台中找到并下载。
目前 Flux 的生态已经相当完善，创作者们围绕人物写实、摄影风格、服装类型、场景表现等方向，训练出了大量不同用途的模型和 Lora。
对于普通用户来说，不一定要从零训练模型。更高效的方式是先选择成熟的基础模型，再搭配合适的 Lora 和工作流，通过提示词与参数调整，快速获得稳定的写实效果。
Flux 真正强大的地方，不只是模型本身的画质，而是它已经逐渐形成了完整的工具链：
> Flux 负责生成高质量图片，ComfyUI 负责搭建流程，Lora 负责控制人物与风格，可灵、Runway 等工具负责把静态画面变成视频，飞影则可以继续完成数字人内容制作。
这也是为什么 Flux 能在短时间内迅速走红，并成为 AI 写真、短视频、电商视觉和内容矩阵创作中的热门选择。
经常有人问我：Flux出图时怎么快速改模特风格？答案其实就在LoRA身上。
把预制好的pipeline里换进另一个LoRA，成品气质立刻大变：御姐款、萝莉款、知性款任你挑选。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_85422c2e48b09b1275f00821730b6ea1.png>
这张是用墨幽随拍-F.1_v1直接生成的样张。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a28788f328c3f55a01c3abae83170880.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d8fd038bcde825a803b5d441cbe8fe2b.png>
这套则是把LoRA统一换成“深色高级西装”后的输出。同一个流程、不同的权重，效果就从日常随拍跳到了商务型录。
具体动手时只需四步：
其一，在模型库或LoRA列表翻到喜欢的样图，点样图下方的“在线出图”按钮，系统会就此加载对应的权重并打开一个云端ComfyUI编辑页。
其二，在页面右上方点下“运行”键。
其三，想换画面内容，就把自己的英文Prompt写进描述输入框。
其四，等图片渲染完毕，成品会在Liblib的个人相册里自动归档。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ca56e2cc50610bc6932da7c98ec20907.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d9f9f6e2a3e15b0ed00562d690e98e37.png>
若要把这套玩法平移到自己的电脑上，需要先把LoRA权重连同底模文件一起下载下来，再安置到个人电脑的ComfyUI数据目录中，具体路径可参考之前发过的两篇案例。
关于PuLID，值得多说几句。ComfyUI环境里其实早已出现换脸扩展组件，但部署过程对小白不太友好。省心的办法是直接用字节提供的网页演示版，打开就能出图，只是有次数上限。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a5b00cd84326087b9da6982f2b37dc12.png>
试用入口挂在HuggingFace的社区空间里，搜PuLID-FLUX即可找到。
我拿内置的默认模特跑了一遍，左栏是参考原图，右栏是换脸后的成图。
第一条Prompt描述的是户外骑行场景：穿粉白色骑行服的人骑在红色单车上，林间空地为背景，并强调头盔与墨镜等细节。英文拟写往往比中文更精准，这里就不逐字引用了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d3db0805717dbfb299c5097f6dc947ae.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c51ca7ef547a9ce1a667b913a8928906.png>
第二条Prompt换了室内氛围：一位年轻女性手握装饰折扇，穿浅紫色吊带长裙，站在红玫瑰花墙前，画面带有咖啡馆灯光的暖调。具体英文措辞同样略过。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8e70535cd7526e846d2c7c93c98da626.png>
我必须提醒：演示版限用极快，我生成到第五次就收到报错提示。想多试几次，最直接的办法是准备多个登录身份轮换使用。
论效果，该方案难敌亲手训练的Flux LoRA；但自训权重很费工夫，已经劝退一大波人。PuLID能不能胜任，取决于你的验收标准，我个人更看好它早日被接入ComfyUI体系，让LoRA、ControlNet、超分修复这些组件在同一套流程里自由组合。
接着，详细说说Flux在ComfyUI里的四种落地方案。
先做一点科普：ComfyUI的工作方式像搭积木。加载模型、编写描述、执行采样、存图，所有这些步骤都以独立模块呈现，模块间用连线传递数据。好处是流程高度透明，便于复现；代价是初次上手时，界面会比普通绘图软件复杂不少。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0ff5b3483dbd405f3c21762f5abf75a9.png>
如果是零基础朋友，建议先看知识星球里的《ComfyUI宝典》系列，里面有完整的入门说明。
四种玩法如下。
第一种，厂方演示站。Black Forest Labs在Replicate社区挂了FLUX三个版本：pro、dev、schnell。进入Replicate首页，搜索该厂商账号即可看到全部入口。以dev版演示：填写描述、选择分辨率、按下运行，不到一分钟就能看到成品。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fb51524f0c4a20d37debc83b0851a50b.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_56cb98b81049ef834871c68f24535666.png>
第二种，Liblib站点上的在线pipeline。Liblib为Flux准备了几套可直接运行的流程模板，模型已预装完毕。进入网站之后，在流程专区挑一套喜欢的，在文本输入区写上描述，然后按右上方的“执行”开始渲染。非会员用户每天会获得一定作图额度，升级会员后排队速度更快。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_067d395a7c55d810dcdc82c00e4f17ec.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8cf8f55eb764ec6f447db39f0238e953.png>
第三种，租借云端GPU实例。自建环境最烦两件事：装依赖和拉权重。现在不少内容创作者会把ComfyUI连同必装组件、常用权重一起打包成镜像，发布到云GPU租用平台。用户租一台带显卡的主机，开机即享受现成环境和显卡算力。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0ffbcaca37f24fe8fe20256db11055e3.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0f896de5a781c4f3f3d7d72f69bc1fe5.png>
第四种，在自己的电脑上部署。本地安装通常有两条路：一是官方纯净版，不掺额外内容，运行最稳定；二是社区懒人包，自带常用组件和基础权重，后续扩展起来更方便。
硬件底线是：Windows环境加一块NVIDIA GPU，显存不低于6GB。把ComfyUI更新到最新版本，即可原生驱动Flux，不需要额外做兼容配置。
完整文档可以在GitHub Pages查阅ComfyUI_examples/flux；Flux的代码仓库在该厂商名下。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_984c741a9d1397581e5a465b8780e4a9.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0ab0ddbef734dceca11121f60158c6f9.png>
最后，福利放在评论区。Flux相关权重与流程文件已打包上传网盘，输入访问密码9c38即可取用，链接会置顶在评论区。
再简单介绍一下我：我是行者，主要折腾AI图像生成、AI动态影像和ComfyUI流程设计，以后会继续在这里分享一手实操经验。