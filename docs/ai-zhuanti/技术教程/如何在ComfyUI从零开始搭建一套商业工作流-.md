# 如何在ComfyUI从零开始搭建一套商业工作流？
最近不少朋友在后台问我，说拿到一套 ComfyUI 商业工作流，但完全看不懂那些密密麻麻的节点，想改又不知道怎么下手。今天这篇就来聊聊，怎么从拆解到搭建，一步步搞定一套能用的商业工作流。哪怕你之前只会跑现成的流程，看完这篇也能学会自己改造和组合。
先说点背景。我之前写过一篇零基础在线上用 ComfyUI 跑图的教程，只要导入工作流就能出图，没看过的朋友建议先去补一下那篇。今天的内容算进阶篇，核心就一条：把别人的工作流拆开看懂，再自己从零拼出来。
其实，任何一套商业工作流，骨架都是相似的，差别只在于细节。只要抓住主干，剩下的就顺理成章了。下面我会用电商场景来演示，重点拆两个最常见的需求：换背景和换装。
## 先从一套电商换背景工作流说起
打开 LiblibAI，搜索“换背景”，找一个运行次数最多的来当案例。比如这套“电商产品换背景”，跑一下看看效果——产品保留，背景被替换成符合场景的AI图，连产品上的文字也清晰保留，不糊不乱码。
![](img/zhuanqian_815ac733653cc3bd1201b6c68f68c115.png)
![](img/zhuanqian_69946cb065c7c343b9c1f7225a76839d.png)
![](img/zhuanqian_4b23a6095d37990e6b86b6bd8550183e.png)
刚打开工作流时，看到那些密密麻麻的节点有点吓人。但别慌，先分层看，整体可分为三段：首次出图、FLUX二次细化重绘、最终打光+高清放大。首次出图这块才是换背景的核心，后面两段相当于在已有结果上做润色和提升。FLUX重绘说白了就是图生图，放大模块则是通用的高清放大基础流程上面叠加打光组件而已。这样一拆，核心其实就落在首次出图这一块。
![](img/zhuanqian_c3c93cc5fdd0463b9a48f252026d2143.png)
![](img/zhuanqian_7f9cacafcbebb0ccd8a69f5a537af6d2.png)
![](img/zhuanqian_6776468b15ceb217ed553991ceccbc10.png)
![](img/zhuanqian_77f29e74d5580c48cd116e8343d4e8cb.png)
## 首次出图究竟做了什么？
这个模块一共干四件事：
1. 图像预处理：先抠图，比如用 SegmentAnything 把产品从原图中分离出来，同时限制输入图片的宽高。
2. 风格化 + 局部重绘：产品保留，只重画背景，还要让背景和产品自然融为一体。
3. 控制背景稳定性：为了不让提示词飘，需要加 ControlNet 来约束图像的一些属性，像是线条、深度这些。
4. 文字保护：AI生成的图像里文字基本是乱码，所以要把原产品图混回去，让文字清晰可见。
想从零搭出来，思路其实很简单——任何工作流都是从一个基础文生图或图生图流程长出来的。你要做的，就是在基础流程上不断添加所需组件，再把这些组件串联进主链路里。
![](img/zhuanqian_609addefe729f6ad86d06fb952b50475.png)
## 各个组件分别是什么角色？
**图像处理**需要四个小工具：宽高比缩放（固定尺寸）、SegmentAnything（自动抠图并生成蒙版）、遮罩模糊生长（让蒙版边缘平滑并扩大范围）、混合（把原图和AI图按比例融在一起，专门用于修复文字）。
![](img/zhuanqian_e07daf87c07143e880ce0a62a053ff56.png)
**风格化**这一块，用 IPAdapter 拿一张或多张参考图，让生成结果的风格、内容细节贴近参考图。
![](img/zhuanqian_abe84c357371a2782e95af60bd3f684a.png)
**局部重绘**用的是 BrushNet，它负责对分割出来的蒙版区域重新绘制背景，这里要选 segmentation_mask 模型。
![](img/zhuanqian_8a4ea5e0c17ad58f296ac32336f3921e.png)
**ControlNet 控制**则借助 Aux 预处理器，把图转成线稿和深度图，再分别用对应模型做精确控制。
![](img/zhuanqian_e5d583597eaa9bf75f9788b895c94075.png)
**提示词和 Lora** 部分就比较常规了，选好底模和Lora就有效果增强。另外可以加个翻译组件，直接用中文写提示词也没问题。
![](img/zhuanqian_7d4fbd682ae843e8ca008376ce825517.png)
## 动手搭建工作流
搭建过程不用一步到位，先把每个模块单独串好，再整合进基础图生图流程。
### 图像处理模块
先缩放原图 → 抠图 → 处理蒙版 → 加载背景图混合。这里先用加载图像的方式做简化，后续打通整套流程时把加载背景图那步去掉即可。参数先用默认值，后面看效果再微调。
![](img/zhuanqian_de7dde40eedf69fe3ada024faf526909.png)
### 重绘模块
先接 IPAdapter，再接 BrushNet。启动和结束的位置需要调一下。
![](img/zhuanqian_be8e2c3ccbe226e601a3c30c8eecaf80.png)
![](img/zhuanqian_dc6304aec3b2c72e1897c97ed4723638.png)
![](img/zhuanqian_f182348bb6b35908a2abb47178a69bd6.png)
### ControlNet 模块
把Aux和CN加载器连到CN应用，再串联一个CN应用。
![](img/zhuanqian_f34fa17d8cf2a9857601c2cb45e353c0.png)
### 提示词和Lora 模块
参考案例里的底模和Lora是可以替换的，按自己的风格选即可。例如这些模型都可以用。
![](img/zhuanqian_f6a63a528d53b2bc01df3294d113d69e.png)
把这些模块串起来，再补上图生图基础流程，缺什么接什么。
## 正式搭建完整工作流
为了避免连线太乱，我用了设置节点和获取节点。你可以把它们理解为代码里的变量——先把某个值存起来，后面要用的时候直接取，不用拖一根长长的线。
![](img/zhuanqian_4274ab4e7252a3f4496c4c1f9889b5c1.png)
![](img/zhuanqian_82708072fd5f06eb60c726ec12b24779.png)
![](img/zhuanqian_629a3615c14aed7b41c6d6cc0b44d5c7.png)
### 输入部分
开头放一个VAE，后面会用到。图像处理模块里分别设置图像节点、抠图图像节点和抠图蒙版节点。
![](img/zhuanqian_5700a9368b5fb182e824f6c0a0811fe9.png)
![](img/zhuanqian_a28ecada343eab5b82b95be80d029d69.png)
### 绘图部分
把提示词模块的模型节点和正负条件连接到重绘模块。用获取节点把之前设置的VAE也拉过来。
![](img/zhuanqian_ab6ff1369f28f3fca2a7ac6d0f0ce90e.png)
这里有个细节要特别注意：IPAdapter 连接的图像并不是抠图后的结果，而是宽高比缩放后载入的原图。BrushNet 那边才连抠图图像和抠图蒙版。
![](img/zhuanqian_f0aa6ec7359ef0a1bf5207b948ee693f.png)
![](img/zhuanqian_323479520d452d7c9b9c6169bbc19a89.png)
BrushNet 的正负条件继续传给 ControNet，再一路传到 K采样器。另外，把VAE和抠图图像接到 Aux 处理器上。
![](img/zhuanqian_84cefc44eb5a86cc47c011f194aaf164.png)
### 输出部分
最后连采样器。ControNet 的正负条件、BrushNet 模型和 Latent 全部接到 K采样器上。
![](img/zhuanqian_dcd18fef59630b71a4f80c59352f982e.png)
跑一下，能出图就说明连线没问题。
![](img/zhuanqian_c7511ca64600b3c8bd014390afda9daa.png)
### 处理文字乱码
生成后放大看，文字应该是乱的——这是 AI 的通病。还记得前面提到的混合组件吗？它的背景图和输出图还没接上。混合组件就是用来修文字的。
![](img/zhuanqian_31a5eaea4261960e25f25255a0f0be33.png)
![](img/zhuanqian_927902f1a301ef06c56e73ec191cfb53.png)
所以，把VAE解码后的 AI 图像接过来，混合后输出，这才是最终成品。
![](img/zhuanqian_9b08eb829bf02f0362f797bfb886bb46.png)
![](img/zhuanqian_7c9bad36bd1c2afc0455591921c6bcf8.png)
看，这样文字就正常了。
### 高清放大
效果满意后如果需要放大，我建议单独开一个工作流来跑。因为放大很耗时，而且只有确认了最终效果才值得放大。放大方式可以自由选，我用的是 Flux + SDUpscale 方案。
![](img/zhuanqian_6a0467b7448a8b90497fbf8737815de1.png)
![](img/zhuanqian_4298b7f6558f36ad338c4440f8296c9b.png)
注意，一个工作流里只能同时跑一套流程，两套并行容易爆显存。所以平时不用放大时，可以把整套放大工作流屏蔽掉。
![](img/zhuanqian_4e449a5449d76d568c63ea3f9abed25d.png)
具体操作：右键工作流框 → 忽略框内节点。要恢复就右键 → 启用框内节点。
![](img/zhuanqian_72738d4fd9f273daac11cff5b4650222.png)
![](img/zhuanqian_fe74b07327359959e5ae9edb8f311f95.png)
我把自己搭好的电商换背景工作流放出来了，另外也提供了一个一键抠图的工作流，里面展示了多种抠图模型。抠图没有哪一种最好，适合你的场景就是最佳选择。
电商换背景.json
一键抠图.json
## 从零搭建 Fill-Redux 万物迁移工作流
前面是拆解别人的流程，现在换个玩法：直接从基础文生图流程开始，自己从头搭一套 Fill-Redux 工作流。在 Liblib 搜 Redux，你会看到一堆 Fill Redux 的换装、迁移案例，核心思路都差不多。这里我就带你从最底层开始拼。
![](img/zhuanqian_b8dd6ff0005cc0f55e9ec7e0f503fc3c.png)
### Fill 和 Redux 是什么？
Flux 模型在文生图上效果很顶，但图生图尤其是局部重绘有点拉胯。所以官方专门出了 FLUX.1 Tools 工具包，里面有两个关键模型：
FLUX.1 Fill —— 专门负责重绘。
FLUX.1 Redux —— 负责风格迁移。
![](img/zhuanqian_798388163cb9215dc4fe1f1c8031bc1a.png)
![](img/zhuanqian_39688f3e2623b69d84605c2af38e2384.png)
官方详细说明可以看这里：https://blackforestlabs.ai/flux-1-tools
简单解释：Redux 相当于 IPAdapter 的升级替代，在 Flux 生态里用它来引导风格，再用 Fill 模型做局部重绘。实际体验下来，迁移效果相当能打，商用场景基本够用。
### 怎么用这套工作流？
先用参考图区域上传单色背景的产品图，比如服装图。当然其他物品也没问题。
![](img/zhuanqian_00a4e3a25375c026f94a516ccc469388.png)
![](img/zhuanqian_6151e7b65005266b1abe2ab3aa0c1328.png)
然后在模特图片区域上传模特图。右键点击图片，打开遮罩编辑器，涂抹要重绘的部分。注意手要稳，把区域全部盖住，稍微多涂一点没关系。涂抹好遮罩，点生成。
![](img/zhuanqian_89b41691a47a7254c668286677d0e69a.png)
![](img/zhuanqian_9526354e1f3e037cad68b90a8e63a995.png)
比如这组效果：涂抹模特服装区域之后生成，对比看下，换装非常自然。
![](img/zhuanqian_9a724e4c4ead8d454611efbc2409669a.png)
![](img/zhuanqian_b0d60f88a93bb52c61b0c16f2eb1a104.png)
![](img/zhuanqian_5cc06e71544cac94affa61f84a66b9ea.png)
![](img/zhuanqian_ea145ef0b256fa946a0f0c36b668680b.png)
### 开始搭建
#### 第一步：Flux 文生图
从默认的 SD 文生图工作流开始，把 Checkpoint 加载器换成 UNET 加载器和双CLIP 加载器，模型用 Flux-fp8 这类。
![](img/zhuanqian_0acd38e469f03d4a0fb51f9730646d00.png)
![](img/zhuanqian_8e1dcb40fdb8d9160eb82685576ff4f5.png)
正面条件前加一个 Flux 引导节点，同时把 K采样器的 CFG 设为 1。Flux 引导值推荐默认，官方给的建议是 3.5。采样步数默认 20，可以按需调高。
![](img/zhuanqian_396cd14ff5f4d58dde37c8132dd55bb5.png)
Flux 其实没有负面条件。你可以加一个“条件零化”节点接到负面条件上，然后把原来的负面 CLIP 文本编码器删掉。条件零化的作用就是清空提示词文本。
![](img/zhuanqian_e652aeb04c48947551d8f09c3b16e134.png)
#### 第二步：Flux 图生图
把刚才的文生图改成图生图：删掉空 Latent，换成 VAE 编码 + 加载图像节点，再接 VAE 加载器。
![](img/zhuanqian_43de47f453f2f0d755e349bc27f6c561.png)
#### 第三步：Flux 局部重绘
加一个“设置Latent噪波遮罩”节点，连上蒙版，就变成一个简单的局部微调工作流了。
![](img/zhuanqian_a681c78f730271f981c929b7065583fc.png)
#### 第四步：升级为 Fill 局部重绘
再把 Flux 重绘换成 FLUX.1 Fill 模型，注意几点：
- Fill 模型不推荐用常规的 Latent 噪波遮罩节点，重绘效果不理想，要用内补模型条件节点。
- Fill 官方原版模型 23.8G，本地显卡没有 24G 显存的话，建议在线上环境跑。
- Fill 模型的引导值按官方推荐设成 30。
![](img/zhuanqian_d163ce8bc61a091b89be2aa0632ec7af.png)
到这里，一套 Fill-Redux 万物迁移工作流就搭出来实际能用了。你现在可以拿它来给产品换背景、给模特换装，甚至迁移各种你想要的风格。拆解和搭建的底层逻辑都一样——抓住核心，理解每个组件的位置，然后像拼乐高一样把它们接起来。
如果这篇对你有帮助，点个赞，后续我会继续拆解更多商业工作流。
今天继续和大家分享一套非常实用的 ComfyUI 图像处理流程。整套思路围绕 Fill 模型与 Redux 风格迁移展开，核心是让重绘结果无限接近原图，最终做到“万物迁移”。下面直接进入正题。
先把内补模型条件节点接入到“条件节点（Flux引导）”和“K采样器节点”之间。模型这里记得切换成 F.1-Fill-fp16_Inpaint&Outpaint（在 LiblibAI 上可以找到热门推荐官版本），同时把 Flux 引导值调整为 30。
![](img/zhuanqian_5d466ed65d210e8640a36f713ee04a51.png)
先用一个简单的例子验证效果。提示词写“Wear a cute cat hat”，意思就是戴一顶可爱的猫帽子。载入一张女生照片，右键选择“在遮罩编辑器中打开”，把头顶区域涂抹出来，点击生成。
![](img/zhuanqian_c651aba698a018825a82333161bc30bf.png)
出来的结果还挺惊喜的。
![](img/zhuanqian_c2e2a192ede57f46b0a3f01627d43c14.png)
![](img/zhuanqian_ee13de2bb19a9ef7996817aa4a973dd1.png)
工作流顺手整理一下：按住 Ctrl 选中全部节点，再按 Ctrl+G，就会自动新建分组框，看起来清爽很多。
![](img/zhuanqian_61b0f70cb3c0cd44e4d0d1b89b2747d3.png)
接下来是重头戏：Fill + Redux 风格迁移。找到 ReduxAdvanced 节点，把它串在“条件节点（Flux引导）”和内补模型条件节点之间。
![](img/zhuanqian_7dc14503214228bf6d21a33779aebb92.png)
输入端需要补上三个节点：风格模型加载器、CLIP视觉加载器、加载图像节点。参数按这个设：downsampling_factor 设为 1，代表参考强度最大；mode 选 keep aspect ratio，也就是参考整张图像；模型分别选 sigclip_vision_patch14_384 和 flux-redux-dev。
![](img/zhuanqian_bc20da001f7f9ce448bae0439681e3db.png)
悄悄告诉你一个小技巧：不用去节点列表里一个个搜，直接从 ReduxAdvanced 的输入端拖一根线出来，松手后选择需要的节点，连线就自动接好了，省事很多。
![](img/zhuanqian_9f8f7f4b66786203f404ed3849c39b08.png)
到这里整体骨架就搭完了。
![](img/zhuanqian_e961fbf006d087329746696b8f4cd5a6.png)
接着还要加上“按宽高比缩放_V2”节点。因为平时上传的图片分辨率五花八门，必须统一缩放到模型能接受的大小。注意这里“倍数取整”要改成 None，“缩放到边”要选长边 longest。
![](img/zhuanqian_a9f04de9b13d02b08b3d5dc7be173513.png)
把“按宽高比缩放_V2”接进主流程，上下两个加载图像的位置都要串联进去。
![](img/zhuanqian_c690ae40aafa5a10e03c7bbcc5c4bb92.png)
准备好就可以生成试试了。
![](img/zhuanqian_013917caa67c08193c45d5851e42e531.png)
对比之后会发现：换装虽然成功了，但相似度只有一丢丢，整体观感差异仍然很大。
![](img/zhuanqian_53036d7573380bcda2156186b8da23fd.png)
![](img/zhuanqian_1ae7b5c4c749662ee1ab941014fb45c0.png)
这就引出一个关键问题：Fill + Redux 换装的效果如果只有这种程度，显然不够商用。那怎么把相似度拉满呢？
回看一下工作流里放的效果对比图，是不是疑惑为什么生成图是两张图拼在一起？
![](img/zhuanqian_79e3e675cbf559796423303fcd39ebe6.png)
原因很简单：AI 生成一张图时，图中元素会保持高度相似。利用这个特性，可以先把模特图直接拼接在产品图右边，生成时只重绘右边的模特部分，参考性会大幅增强，最终重绘结果也会高度贴近预期。
所以需要拼接两幅图——原图和蒙版图，这样才能让蒙版对应上原图。而蒙版本身，可以先造一张黑色图，再和模特的蒙版拼起来。
![](img/zhuanqian_5886e60f04e90136c9e92eb2fe0351ef.png)
![](img/zhuanqian_ebe5c7ac5add7acc79e43b52fc3fed39.png)
最后再把生成结果里模特那一半裁掉，就完成风格迁移了。
到了“Fill + Redux 万物迁移工作流”环节，先看图像联结部分。拼接图像用“图像联结”节点，黑色蒙版则由“空图像”节点生成。
![](img/zhuanqian_d192bf24c81352c12743fa9b4084473c.png)
注意：空图像的宽和高要转成由外部传入。右键空图像，选择“转换为输入”，依次点“转换宽度为输入”和“转换高度为输入”。
![](img/zhuanqian_513031430434bbb26fb1f35bd78443e4.png)
![](img/zhuanqian_243c292c14ef5c933bd8dc61a568f147.png)
另外还有两个节点很关键：“遮罩到图像”和“图像到遮罩”。
![](img/zhuanqian_e069346fa18844306122249b23c4873c.png)
![](img/zhuanqian_49413250e9b84b948218b44cbec18d31.png)
具体连接方式看图：用图像联结节点，把模特图拼到产品图右边，然后图像联结的出口接到内补模型条件。
![](img/zhuanqian_1a9d09c5347acccc376a46f300d477a0.png)
遮罩那边的图像联结也同理，只不过要先靠空图像生成底图，空图像的宽高引用产品图，再连到图像联结；另一侧把遮罩接过来，但遮罩要变身成图像，所以得经过“遮罩到图像”和“图像到遮罩”这两个转换节点。
![](img/zhuanqian_8a9f1751f075e05b3fb0be6a5217e821.png)
连线完成后整理一下工作流，顺手加个“图像预览”节点方便观察，图像联结部分就算搞定。接着加载图片、涂抹蒙版、运行，两个预览里都能看到图像已经成功拼合。
![](img/zhuanqian_b9e0e8d92370c136c1b27e922ab2f44f.png)
再看生成图的效果：这次融合非常自然，相似度极高，几乎看不出破绽。
![](img/zhuanqian_e6767f2a447f98d1592c8d3505e79748.png)
![](img/zhuanqian_9a5b638f464474342fe58a0d719ec4c8.png)
既然只要右半边，接下来就得做图像裁剪。这个环节用“桥接预览图像”和“图像裁剪”两个节点就够了。需要注意的是，图像裁剪同样要把宽高转为外部输入——右键节点，选择“转换为输入”，依次转换宽度和高度。裁剪位置记得选右上 top-right。
![](img/zhuanqian_2351feb6d0f476a90204459ca25577d4.png)
![](img/zhuanqian_b7e309968e21d27817cf610acfcfc34b.png)
把这个裁剪节点接到 VAE 解码之后，宽和高从模特图的缩放图像节点传入。运行一次，裁剪效果就正常出来了。
![](img/zhuanqian_c589d3600b5a01bb1b2ef7c6b0d8d53d.png)
最后补一个高清放大。这里推荐用 Flux 模型来放大，而不是继续用 Fill 模型——Fill 更适合重绘，放大不是它的强项。放大模型加载器可以按喜好随意选，SD 放大的输入端直接连到 Fill 生图工作流出来的节点就行。
![](img/zhuanqian_323eabb3e2c59016d954a3dd3d25f78d.png)
![](img/zhuanqian_49d74fde7382c4b618e20ce60b33eb38.png)
方便大家直接上手，我把这套案例工作流也放出来了，需要的朋友可以拿去看看：
Fill+redux万物迁移.json