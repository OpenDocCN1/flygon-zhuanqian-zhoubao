# Flux.1 Kontext 到底是什么？优势在哪？实测表现如何？
作者：龙哥



上篇聊到 Lovart 的时候，身边已经有不少人在聊 Black Forest Labs 刚推出的绘画模型 Flux Kontext。趁着这两天空档，我立刻去上手体验了一把。

一致性真的惊人，这个维度的表现可以直接把现在市面上大部分模型甩开，生成速度也快得离谱。肯定不是十全十美，问题点后面也会提到。

![](img/a20db90441f5c6c38177645d6ac6a8e6.png)

先简单捋一下背景。Black Forest Labs 黑森林实验室你肯定不陌生，Stable Diffusion 就是从那里走出来的，影响了整个 AI 绘画浪潮。核心团队因为商业化方向的分歧集体出走，在德国黑森林成立了新公司。

他们认为过去的绘图范式还能再进一步，于是推出了 FLUX 系列。画得更快、画得更美，对指令的理解也更接近人类语言。今天的主角 Kontext 就是 FLUX.1 Kontext 版本，Kontext 在德语里就是“上下文”的意思，从名字就能看出这次产品的核心思路。

下面进入正文，文中的 Prompt 我都会一并给出：

* * *

# 实测能感知的 4 大核心优点

结合官方介绍和我的实测，有这四点最突出：

1、角色一致性：跨场景也能锁住关键元素 —— 多次迭代修改后，主体依然稳定
Character consistency: Preserve elements across scenes

2、局部编辑：只改指定区域，其余部分完全不动
Local editing: Target specific parts without affecting the rest

3、风格参照：基于已有画面延伸出新场景 —— 风格迁移能力在线，不过我觉得对比 4o 还是稍弱一些
Style reference: Generate new scenes in existing styles

4、交互速度：迭代几乎没有延迟感 —— 我这边最慢 8 秒，多数在 5 秒内完成，比 4o 快很多
Interactive speed: Iterate with minimal latency

这次一共发布了两个版本
FLUX.1 Kontext [Pro]：主打快速迭代编辑，首个能在不同场景间保持角色特征、风格统一的累积式编辑模型
FLUX.1 Kontext [Max]：在高速运行下追求极致性能，已完成优化升级

实际使用下来，Pro 的综合效果更稳；需要多图参考时才需要切到 Max。下面的测试全部基于 Pro。

## 1、角色一致性

先看最关键的多次对话连贯性问题。

首先用 文生图 生成了一只戴着 VR 眼镜的小绵羊

![](img/62f55e68e339e74db17910ae0fff4a62.png)

第1图，我要求它直视镜头，坐在酒吧里喝可乐 —— 角色的面部、眼镜细节、蓝色的斜挎包都完整保留。

第2图，复制出第二只绵羊 —— 核心特征依然在，只是体型稍有缩小，整体无问题。

![](img/7caef0089e2867451bfcd9a69d58072f.png)

![](img/ba7e786608eace2c5f0483823d18d484.png)

第3图，让它们背对镜头 —— 背包、眼镜、可乐等细节基本保留，不过背包带子的理解出现了小偏差。物理上从背后其实看不到啤酒瓶，但模型为了保留特征还是显示出来了，算敬业还是多余自己体会😂

第4图，放它们到大草原上 —— 羊毛质感和比例与最初有一定漂移，但主要特征依然牢牢锁定。

![](img/f059add20fc7e01acf69028bc60b02ab.png)

![](img/f125e51f14871599f90e95a42ce74a83.png)

再换到新场景做动作：超市推购物车、办公室过生日。这两个场景下，角色的轮廓、穿戴细节都被非常精准地保留住，一致性极强。

![](img/b55c232604d469388b1769f994407bf0.png)

![](img/cbf21ffff1eb15dac204b4ab8dd52377.png)

本节全部 Prompt：

A realistic close-up of a fluffy white lamb standing against a clear blue sky, wearing a futuristic white VR headset strapped securely around its head. The VR headset has a sleek, minimalistic design, allowing the lamb’s nose to fit naturally. A small, vivid blue shoulder bag hangs diagonally across the lamb’s body

1、Face the camera directly,the white lamb now sitting in a bar and enjoying one cup of Coca-Cola.

2、There are now two of these lambs.

3、Observe them from behind.

4、The two lambs are on a vast grassland with nothing in their hands.

5、The two lambs are now grocery shopping

6、The two lambs are now celebrating birthdays in the office

### 背景与颜色的一键替换

这个需求过去一直难处理，GPT-4o 也常翻车。这次用 Kontext 基本实现了一键换背景，商品主体、前置物品几乎零变化，远看很难分辨真假。

![](img/1c75dd6f222b5eaacc4c9db294bb4156.png)

![](img/69d6ce204987cec929f100e5a672030f.png)

![](img/0ce14265223a5622c89e1bb948e86c65.png)

![](img/625577fa1906f89fd41dadefb308752b.png)

1、 Change the background to a European-style kitchen, with sunlight streaming in from behind.

2、Change the background to a different style of kitchen, while keeping the lighting consistent — soft and bright.

3、Change the background to a different style of kitchen.

### 仅换颜色

换色听起来简单，模型做起来却容易失真。以小米YU7为例：

Change the car color to pink.

GPT-4o 在改色的同时细节大量丢失。即梦好一些，基本保留但有轻微失真。Kontext 则是几乎 1:1 保留细节，只换了颜色。

![](img/d010b9ffe3ff8ec710455ac5615496d7.png)

GPT-4o 的结果里，侧进风口、后轮宽体、进气口、前引擎盖的光影都还原不出来。即梦尚可，但车牌文字不够准。下面是 Kontext 的前后对比，用蒙版一看，细节几乎无差别，仅有轻微位移，可以忽略。

![](img/446e6251f726090140ffc76f78fedc18.png)

我还试了内饰换色，同样还原度极高。图片里的文字完全不动，只改颜色，其他部分纹丝不乱。电商平台的“一键改色”功能感觉可以上线了。

![](img/31373441599a4f0531e282d3bf5c5420.png)

![](img/c4f9bb11b88b52ed5fc0cd6e69d80cff.png)

### 人物换装/虚拟试衣

换装同样丝滑，以川普为例演示：

一键换成比基尼、病号服、T恤、和服……想换什么换什么。Keep the character’s appearance and pose unchanged, and change the clothing to a Bikini，把 Bikini 换成对应服装即可。

Kontext 在主体、虚化、背景上完全一致，肉眼几乎分辨不出。

![](img/4bce0fd276f399070df5fea7f3a3f371.png)

![](img/8d455aaa8e9ea9b6d870582afafd2303.png)

![](img/2dfaa37ba7d4b3bcace3f952a7a78c14.png)

![](img/408147b9cfab78a177f1c4ff49b6cc26.png)

![](img/861ce82b84dbbb803b2110ebd1f82aaa.png)

## 2、局部修改

第二个核心能力是局部编辑，也是日常最常用的。

“把这个 P 掉”“把这个放大”“能不能……”之类的需求都能满足。

### 一键去除物体

📕上这类需求泛滥，我随手找了三组测试。

![](img/32bf493434031ea7b02c81c8cb7527fb.png)

![](img/29f80befc0e90f8b9a755bbfc232c585.png)

1、功夫小哥的栏杆😂
Remove the pole and keep the background scenery harmonious and natural.
栏杆位于画面纵深中部，去除后背景非常自然，几乎看不出痕迹。

![](img/8b28f60003e48a2d26c713f8839ee18e.png)

![](img/0aa8dd1195bde312752f4ce1b1902e1e.png)

2、沙滩美女背景游客
Remove the people on the beach in the background.
人物被无痕抹除，女生党以后可以自用。

![](img/eb94bd876358d57ae339b5123c88511e.png)

![](img/610647c9f1633dfa68aa671cc10e1612.png)

3、海里穿绿衣的“电灯泡”大妈
Remove the person in the background wearing green clothes.
主体去掉了，海面有轻微违和，roll几次即可。

![](img/828940a4b4c81e388c9cca55164ff7ec.png)

![](img/994951fb071b10f68d699750ecfd47ab.png)

官方的 Edit 模式逻辑清晰，还有 hint 功能，配合使用会更精准。

![](img/52ff0ca3e27d2b017b5cc1afcced3bb4.png)

点“➕”后可在图上画框，配合 Prompt 精准局部修改。

### 文本修改

局部编辑也覆盖文字修改。中文支持目前一般，建议优先改英文。

1、给川普照片加文字
Add the text “Did you follow me?” in the center of the image.
自动加了透明黑底框，效果可接受。

![](img/7168394a60f581a8ab1799dc572c15e7.png)

![](img/14eb90dc361374629e292aa2a852ef93.png)

2、修改马斯克手举白纸上的文字
rewrite the text “Did you follow me?” in the center of the image.
几乎无违和。

![](img/04bd2717b4a7355a8a014c2f8aa73ee6.png)

![](img/e79be36c20bad9a92bbd8f8429d10282.png)

3、最惊艳的包装文字替换
Replace "FLUX" with "2YAI." Keep the same font style.
包装内文字被替换，边缘贴合度非常自然，细节控会喜欢。

![](img/057dff633ddcdebeb688cbc5231eac3f.png)

![](img/1abb50da1a5146b6dc60576344f2fe47.png)

## 3、风格参照

这是官方的第三大亮点。纯从风格表现力看，我觉得还是不如 GPT-4o，但风格一致性保持方面，Kontext 更稳。

两个案例演示：

#### 1）基于同一风格续画

我在 BFL 官网挑了一张图，让 GPT 生成五个连贯分镜设定。

![](img/f7c6390bb14929843f5f0d162d23dcd0.png)

![](img/aa3293392883a3cda991d647ab1ecc39.png)

![](img/7fa3843f02c8c779d4991d26f873a8ea.png)

![](img/4775e535c3a401f7e9acf1f46bf564eb.png)

![](img/583dede2f851fa48a350545fe041a290.png)

![](img/d5b46ae710dea41c888f2c38fb6de643.png)

![](img/812e769e21f090fc4166b5b319732b4f.png)

风格统一度、人物连贯性、情绪表达都很到位，后续做成连续剧情或视频会很强。

1、raw image

2、Keep the raw image style, a fluffy rabbit in sailor clothes holds a flag high on a wooden ship deck, surrounded by excited cats and dogs, setting sail at sunrise. The ship leaves a vibrant harbor, the morning sky glowing with golden light, fluffy clouds, and seagulls circling overhead. Warm, soft anime style with dynamic composition, sense of beginning an adventure, pastel color palette, high-detail fur textures, lens flare effect from the sun.兔子举起航海旗帜，所有猫猫狗狗激动地欢呼，帆船从港口起航，迎着朝阳

3、Keep the raw image style, the rabbit captain sits cross-legged on the ship’s deck, drawing a map with a feather pen, while cats and dogs lounge lazily around, basking in the sunlight. Calm sea stretches to the horizon, gentle waves sparkle, a few seagulls fly overhead. Serene atmosphere, soft ambient lighting, fluffy and cozy anime style, warm pastel colors, detailed wooden textures, vintage travel vibes.兔子坐在甲板上画航海图，猫猫狗狗们懒洋洋地晒太阳，海鸥在天空飞翔。

我又做了一套，这次连一分钟都用不到。

先把之前那组海上冒险的画面串起来感受一下。

4、保留粗糙写实影像基调，海上忽然掀起暴风，墨黑的云团疯狂盘旋，巨浪拍向甲板。兔子面容坚毅地指挥，猫狗们在呼啸的风里紧固帆索，缆绳被吹得乱飞。雷光乍现，灯光明暗剧烈，色调沉郁压抑，动漫冒险质感，机位多变，情绪张力十足，水花四溅，毛发湿漉漉的细节清晰。天空陡然阴云密布，风急浪高，兔子在安排收帆，猫狗惊慌却又默契配合。

5、保留粗糙写实影像基调，风暴散去后，一道明亮的彩虹横跨澄净的天空。兔子与伙伴们聚在甲板上抬头仰望，满是惊叹。海面在柔和日光下闪烁，整体氛围宁静而充满魔幻感。通透清新的动漫风格，柔粉与炫彩渐变配色，湿润表面慢慢变干的细节被刻画出来，心境安宁喜悦，波面点点星光。

6、保留粗糙写实影像基调，船只抵达一座郁郁葱葱又带点神秘的岛屿。兔子第一个跃上金色沙滩，回头向船上的猫狗挥手。身后是茂密的热带丛林和高耸山峰，蓝天白云缓缓飘动。探索感十足，色彩饱和度高，柔和的冒险动画质感，热带植被与材质细腻丰富，节奏明快振奋，角色动态张扬。帆船靠岸了，兔子领着猫狗跳上沙滩，远处是苍翠森林与神秘岛景。

![](img/25d6c5055b5a8855fea7a2744cb4d32e.png)

![](img/4a7b8f901536995a95912128df0d8397.png)

![](img/bb6ddfb9f4784ef96c188fab27e000cc.png)

![](img/53436a469c941f228e5f0ff8dc08c83e.png)

![](img/07a1c9000641875c98ca0956a7199069.png)

下面来试试把已有成片做风格重绘。

#### 2）参照图片做风格迁移

这张底图是我用文生图生成的，海边一对情侣对着镜头。随后我把它丢进不同风格里做转换：

![](img/a53a26018725a94a6276bdbc6db1bd81.png)

![](img/a79d74faeb846696460d21bbe2425969.png)

![](img/93713518fbbecba9da9378c321547aa4.png)

![](img/f3613cfa29234b8727231b2d50671ed6.png)

![](img/b8c4633984b58b9168f17d88499bf219.png)

![](img/86a0e3cbef3a63cf87f10f06a1bd73c5.png)

![](img/6f0d21a31b457db88971381a3d2ec83b.png)

1、原图：晴朗蓝天下，海边情侣望向镜头。

2、（赛博朋克）把整体画风转为赛博朋克，保持人物与场景不变

3、（吉卜力）把整体画风转为日本吉卜力风格，保持人物与场景不变

4、（扁平插画风格）把整体画风转为扁平插画，保持人物与场景不变

5、（像素风）把整体画风转为像素艺术，保持人物与场景不变

6、（数字野蛮主义风格）把整体画风转为数字野蛮主义，保持人物与场景不变

7、（蒸汽朋克风格）把整体画风转为蒸汽朋克，保持人物与场景不变

顺带我还让画面里的动作也跟着变了，

互相拥抱、深情对视、比出心形手势、摆出舞蹈姿态

![](img/6b06710a5d6ab62786bb6890e61fcaa0.png)

![](img/ab200ba071226e595b2109a33dc2a591.png)

![](img/d245040a5d8583fc8ef1d07204b6561e.png)

![](img/9ce5a46c683eb208d8ba30a971373350.png)

1、情侣正紧紧拥抱在一起。

2、情侣面对面站立，中间留一点距离，目光相对。

3、情侣用双手比出心形造型。

4、情侣摆出跳舞的姿势。

## 4、交互速度

除了角色一致性，这交互的响应速度也让人意外。

平均下来约7秒，最快能到5秒，基本都在5到10秒区间里。

![](img/a9775f361a55628ec9f0de519a113e69.png)

这个效率比GPT-4o快太多，甚至比即梦还快。

交互速度看似小事，对我们作为生产力后端来说，直接决定效率；对前端用户来说，体验感也会大幅提升！

过去的Web AI绘画站点，等GPT-4o出图只能靠后端轮询，API未开放时用户只能邮件收结果。

而现在用Flux Kontext，屏幕往下滑的功夫，差不多两三句话的空档，图就出来了。

# 可用的入口

## 1、BFL官方【最简易】

https://playground.bfl.ai/image/edit

官方页面非常干净，左侧菜单一目了然，选好需求上传图片就能用。

现在注册送200积分，一张图扣4分，理论能玩50张。

重点提醒Edit里的hint功能，务必打开，用起来很顺手。

![](img/97a27938fde0361a1c218363a8e7fbd5.png)

不过官方的History记录做得比较简陋，反观下面的fal就很实用。

## 2、fal 【好用且开发友好】

https://fal.ai/models/fal-ai/flux-pro/kontext

fal的API平台是我当前主要在用的，很多案例都是fal跑的，之前拿了$50额度。

推荐点在于，每次生成完成后下方的一排操作按钮，体验很到位。

Flux Kontext出图默认不是极致清晰点选upscale就能提升，Make Video能直接转视频，Use Output还能把这次结果直接作为下次参考图链起来。

![](img/384261b8afe325e4b378c5c017962bd4.png)

而且每条API请求记录都清清楚楚：缩略图预览、耗时、完整Prompt，这三样就是我回溯历史时最依赖的信息，fal真的很懂需求。

![](img/9965721053ce4a6274b03f88c2bea8a6.png)

当然fal完全可以接入自己的应用做API调用，我下一步就会接进去，先关注我获取进展。

![](img/2991238e7bd7efdba44032570ff8c0bf.png)

## 3、Liblib【国内体验友好】

https://www.liblib.art/

接下来是国产的Liblib，注意不是bilibili。

最大优势是全中文界面，还自带“翻译成英文”功能，对我们这种半混用用户非常贴心。

![](img/24c597c21ea396bf51f7bf08b8b6eab6.png)

![](img/18f3405a69b1e499d8c602f400eccd6c.png)

## 4、comfyui【最强但最重】

最强力的还是comfyui，强到需要单独一套学习成本。

本地部署：https://www.comfy.org/zh-cn/download

网页部署：可选择Liblib https://www.liblib.art/comfy

![](img/31b63fc1f121a57be5dfcba21b943903.png)

发文前臧师傅刚发了用comfyui跑Flux Kontext的节点配置，可以直接套用。

唯一要注意的是，在Liblib上跑comfyui速度偏慢且费用偏高，建议还是本地部署更划算。

# 目前实际使用中的问题：

1、人脸总是有点像。

生成几次人脸图后会发现人物长相趋同，原因目前未明。

![](img/74d4e40cc0e74a237fdd283befe05f90.png)

![](img/bdc5e577c6e392ccb75aa3cf81d9a1fd.png)

![](img/0cc473bf9393d7f4675f1ba46d1fac7c.png)

2、对话超过6轮后，人物的统一性会开始漂移。

这里的操作是每次都引用上一次的结果。

如果你想让角色进入全新的场景讲新故事，建议直接回溯到最初的角色基准图。

3、kontext对提示词写法很敏感。

我试了上百张，Flux对描述的细微差别反应很明显。

这种差异主要影响风格表现，对角色一致性的影响也很大。

![](img/4024259b71c5ecd78d35bd128f81929a.png)

多图融合、局部修改时提示词更关键，建议使用英文描述，当然客户端若有中转翻译也行，主要看平台策略。

下面我整理一个简易提示词模板，可以交给你的AI助手，让它在会话里帮你产出适配Flux Kontext的提示词。

### Flux Kontext提示词助手

### 元提示词（中英文对照）

中文：

你是一个Flux Kontext提示词助手，专门根据用户需求生成精准、清晰、符合Flux Kontext标准的提示词。你的工作规则是：

*   使用清晰明确的动词（如：更改、替换、保持、移除）

*   精准描述变化内容与保留内容

*   指定风格或细节特征（如风格迁移、材质、光影、姿势）

*   逐步拆分复杂修改，确保每步清晰单一

*   保持语句简洁流畅，适合直接用于AI模型理解与执行

你的输出格式：

*   中文要求：简洁准确

*   English Prompt：符合Flux Kontext标准的高级英文指令

*   （可选）进阶版Prompt：补充细节特征，优化生成效果

*   必须确保：风格清晰、动作明确、细节具体、保持稳定性

English：

You are a Flux Kontext Prompt Assistant, specialized in generating precise, clear, and Flux Kontext-standard prompts based on user requirements. Your operating rules are:

*   Use clear and specific action verbs (e.g., change, replace, keep, remove)

*   Clearly describe what to modify and what to retain

*   Specify styles or detail features (such as style transfer, material, lighting, posture)

*   Break down complex edits into clear, singular steps

*   Keep sentences concise and fluent, suitable for direct understanding and execution by AI models

Your output format:

*   Chinese instruction: concise and accurate

*   English Prompt: Flux Kontext-standard advanced prompt

*   (Optional) Advanced Prompt: add detailed features to optimize generation

*   Must ensure: clear style, specific actions, detailed attributes, and stable control

# Flux Kontext到底带来了什么？

有了Flux Kontext，我们收获的究竟是什么？仅是几张风格统一的图吗？不，我们拿到的是全新的创作者权杖。

在此之前，AI绘画对很多人而言更像一台“灵感老虎机”。投进Prompt，等待惊喜或惊吓。

就算撞大运得到一张惊艳之作，那个鲜活角色、独特场景也难以复制，像昙花一现。我们像是灵感的赌徒。

Flux Kontext彻底改写规则，它把我们从赌徒变成了可持续的故事讲述者。

借由它，我们第一次能真正“拥有”一个数字角色，赋予它稳定身份与灵魂，它不再是海量数据里随机的投射。

我们能让它换装、换场景、经历不同情绪，完成连贯的视觉叙事。

这不只是技术升级，更是创作权的下放。过去只有数百人规模的工作室才能实现的高度角色一致动画或漫画，现在独立创作者在电脑前就能启动可持续的视觉连载。

因此，Flux Kontext的真正价值，是把AI从“单帧图像生产器”升级为支撑“连续世界观”的绘画笔。它给了我们稳定、持续创作的能力，这就是这个时代创作者的新权杖。