# 《ControlNet 完全掌握手册》
《一周啃下15个ControlNet模型，我的实战笔记》
大家好，我是龙哥
全部干货都在我的公众号「吴东子AI」
这是SD三部曲的收官篇——ControlNet终极攻略
在前面我们聊过，要把Stable Diffusion真正用起来，绕不开两个核心：LoRA 和 ControlNet
LoRA负责把你想要的人物、场景炼成专属模型
ControlNet负责把这个模型画得更听话、更可控
LoRA的教程已发，需要的同学可以回看
ControlNet全系共有15个模型，每个模型对应一种图像采集方式，对应一种使用场景，每个场景都能找到变现路径
我花了7天把15个模型全部过一遍，从安装到实操跑通了完整流程，才整理出这篇笔记
里面涵盖ControlNet是什么、怎么装、模型怎么采集、实操案例，以及目前玩起来最爽的几个方向
1.动漫转真人
2.真人转动漫
3.姿势、表情精细控制
4.线稿AI上色
5.人设固定
照着步骤走就能上手
配套的整合包和模型我都打包好了，链接放文末
整理耗时很久，希望对你有用
严禁搬运，必追究！
# 一、ControlNet到底能做什么
## 1.锁定人物姿态
能精确指定生成人物的站姿、坐姿、表情，甚至到手指骨骼的细节
![](img/zhuanqian_9bfc8fc88fd05e70a90e37960f9cc03b.png)
![](img/zhuanqian_6cf6dddf23db5e7eb3872e51be8772a1.png)
## 2.线稿上色
![](img/zhuanqian_a5731657b91104cf91463286e31c2981.png)
![](img/zhuanqian_17f6102ee6b47ffe9d0e05a969d1fa75.png)
![](img/zhuanqian_48683f4a984856b4bbde314f4fc06f56.png)
![](img/zhuanqian_9b1da3e81da639ef6b730a9adbcda2aa.png)
## 3.画质修复
![](img/zhuanqian_89bafc7daba852ce4686fd607746056a.png)
![](img/zhuanqian_fffe22e05c0ec5ae53ca13687895d8a1.png)
## 4.动漫变真人
![](img/zhuanqian_95287a72d9aee8c3bd89e77c5ba7572d.png)
![](img/zhuanqian_c75be5b0e222f101d2cd55d548d1cfe5.png)
ControlNet的玩法远不止这些，后续会继续展开
# 二、ControlNet是什么
AI绘画的终极目标，是让输出的结果和脑中想象一致
现实是随机性太强，大多时候靠大量抽卡撞概率
如果能同时控制出图的三大要素，就能大幅提升命中率
1.提示词
2.LoRA
3.ControlNet
提示词定基调，决定画面大体走向
LoRA定主体，让角色、场景符合预期
ControlNet做精细化控制，对主体、背景、风格、形式进行微操
提示词需要长期积累和AB测试来建立敏感度
LoRA的训练我已另文讲解
本篇聚焦ControlNet的使用逻辑，我会把15个模型逐一演示，让你明白每个模型的用途和用法
ControlNet的核心思路很简单：你给一张参考图，选择一种采集方式，生成一张新图
比如给一张人像图
可以采集人物的骨架，让新图保持同样姿势
可以采集线稿，让新图保留相同轮廓
可以采集风格，让新图延续相同画风
不用纠结哪个模型最好，关键是你想要什么画面
多尝试，甚至叠加多个模型，最终把结果调到你理想的状态即可
# 三、ControlNet安装流程
开始学习前先升级版本，不然部分功能会异常
新版ControlNet安装分四步：
* 下载ControlNet
* 更新ControlNet
* 安装预处理器
* 安装模型
## 1.下载ControlNet
通过整合包安装的Stable Diffusion通常已自带ControlNet插件
先看SD最下方是否有ControlNet面板，没有就手动装
已有插件直接跳到更新步骤
![](img/zhuanqian_cfd011510534f2767806805066631088.png)
安装方法：
①打开状态栏的“扩展”
②点“加载扩展列表”
③搜索“controlnet”
④点击右侧安装
我这已装好所以搜不到
![](img/zhuanqian_90014088e7c1aafb721b09e7ea5089c2.png)
安装完即可
## 2.更新ControlNet
①启动界面点最左“版本管理”
②点“扩展”
③找到controlnet，点“更新”
![](img/zhuanqian_4b50849bf8f76d84300a307f62c688c8.png)
## 3.下载预处理器
预处理器模型放网盘，链接在文末
下载《1.预处理器》文件夹
找到里面的“downloads”文件夹，整体复制到SD目录下
路径：SD文件 > extensions > sd-webui-controlnet > annotator
![](img/zhuanqian_0ccc686c24c37a40208bb72fc90c7c8c.png)
## 4.下载模型
下载网盘《2.模型》文件夹
内含14个模型，复制到SD目录
路径：SD文件 > models > ControlNet
![](img/zhuanqian_c2986b5d82593a2f3a86d4389c6eb787.png)
至此ControlNet已更新完毕
# 四、通用操作步骤
ControlNet共14个可用模型，理论上可做14种用法，甚至可多模型叠加
但操作逻辑基本一致
先讲统一用法，再讲每个模型
以最常用的“姿势控制”为例
目标：让黑衣小姐姐摆出白衣小姐姐的动作，得到右侧效果图
![](img/zhuanqian_659a7cff22086a0a9530f593f32502fe.png)
## 1.基础设置
先用正常流程生成一张满意的基础图
包括选大模型、写关键词、使用LoRA、参数调试等
这些在Stable Diffusion教程里已详细讲过，这里不再重复
![](img/zhuanqian_843ef35a293f5e6f3a857796302f8ca3.png)
生成一张相对满意的结果
![](img/zhuanqian_72fe271683c2fea079c164d3fb5d016f.png)
为了后续加ControlNet后仍保持一致，需要固定随机数种子
![](img/zhuanqian_bf6dec6079bd52cc504285fc54828891.png)
## 2.ControlNet使用
ControlNet使用就两步：上传图片、选模型
下拉到SD底部打开ControlNet面板
![](img/zhuanqian_e3ba16eae845aab38de1a13a3eaeb44a.png)
上传一张参考姿势图
“启用”必须打开，其他参数可按我示例设置
显存不足可开“低显存模式”，但会变慢
![](img/zhuanqian_7539a8b0854e6c96195c067a132219af.png)
控制类型有很多选项，本质是快捷预设
选择“OpenPose”
会自动加载对应预处理器和模型
![](img/zhuanqian_3e1fac9e55fea4ea516fa60903b93588.png)
点开预处理器选项卡
所有预处理器都是识别姿势，只是识别粒度不同
这里先用最基础的“openpose”
![](img/zhuanqian_b8e6d16c5f4a8abc032b300e8e9ac18c.png)
点爆炸按钮“💥”，右侧即可看到处理后的姿势线条
![](img/zhuanqian_fcc5a1ef1d036b54a62cb4c6a579a5ab.png)
点生成，小姐姐就摆出指定姿势了
![](img/zhuanqian_2627957d02c93bcf0aa3a023ccb6d643.png)
![](img/zhuanqian_6e9317336774e83e9f9e821f41a4e9d2.png)
不同功能的核心就是换参考图、换预处理器和模型
通常预处理器和模型同名配套使用
ControlNet只是辅助工具，大模型和关键词依然关键
换风格记得换大模型，二次元用anything，真人用chilloutmix
接下来逐个讲解各预处理器和模型的作用
# 五、姿势约束
本节讲OpenPose模型，主要控制人物姿势
可控范围：身体姿势、表情、手指形态，可单控也可组合
身体姿势
身体姿势+面部表情
仅面部表情
身体姿势+手指+表情
身体姿势+手指
![](img/zhuanqian_840136cf012201d2d37a8ad6e3b55b45.png)
## 1.控制身体姿势
SD默认人物动作随机，ControlNet可让人物摆出你指定的任何姿势
![](img/zhuanqian_99dcba4efcfb30c2e695a5d70a4345a8.png)
![](img/zhuanqian_f99f9682fad1e2e1bb4448ec871272f9.png)
正常设置大模型和关键词后，打开ControlNet上传参考姿势图
模型选择：
预处理器：openpose 模型：openpose
![](img/zhuanqian_7a32dcacdf34b7585a1acb07b03c782f.png)
点爆炸按钮，模特姿势被提取成火柴人，小圆点为关键关节
![](img/zhuanqian_bee775a3f45dde292abb35260b340663.png)
生成后，模特姿势基本完全复刻
![](img/zhuanqian_53bdd5b2416fbd9cbbb045e64f27c617.png)
## 2.控制姿势与手指
除整体姿势外，还可识别手指骨骼，有效规避多指缺指问题
![](img/zhuanqian_085e40f64170acd9a09cd7ba8944cb91.png)
![](img/zhuanqian_5bfec7f19d024be241d2e78e66780bd4.png)
操作同上，仅预处理器不同
模型选择：
预处理器：openpose_hand 模型：openpose
![](img/zhuanqian_ddaef8203c1b900b3ee145b88a7f3cc5.png)
预处理后火柴人增加手指线条和节点
![](img/zhuanqian_9f2ccc37eeaa361ca744a8ceec08995f.png)
## 3.控制表情
OpenPose还能控制表情，适合大头特写，识别更准，也只能生成特写
![](img/zhuanqian_65d201d55e87099af3d25e4dd3e0f1a6.png)
![](img/zhuanqian_f271883d48fb256445e78a166e8d55ef.png)
模型选择：
预处理器：openpose_faceonly 模型：openpose
![](img/zhuanqian_38e9bf23c0dfe71c11924f7f12cb69ae.png)
预处理后脸部五官被点位描出
![](img/zhuanqian_a3503ea5f037adc49319c5f1a43f68ff.png)
生成后脸型五官有一定还原
注意，若生成时用了LoRA，再用ControlNet控制表情，可能导致与LoRA人设冲突
![](img/zhuanqian_8b7c15bb00e405a1d9cf297f13caed07.png)
## 4.全方位控制
同时复刻整体姿势、手指、表情
![](img/zhuanqian_c4579dae024a0c3aeace3db75f90cda0.png)
![](img/zhuanqian_34ff8c20222efcb11818fe55dfdc439c.png)
模型选择：
预处理器：openpose_full 模型：openpose
![](img/zhuanqian_e5f1d466aa8aedefe36aee590cffc4e6.png)
处理后结果包含上述所有信息
![](img/zhuanqian_2b2c1f28299e1fbea56569e0e4141885.png)
## 5.手动编辑火柴人
预处理器偶尔识别不准，或需要更精细调整，可装一个编辑插件
![](img/zhuanqian_83d0b107643f71206fb7bbb6ca9055a5.png)
### 01.安装方法
①扩展-可下载页面
②点“加载扩展列表”
③搜索“openpose”
④安装“sd-webui-openpose-editor”
![](img/zhuanqian_66e16492e84946fb6a66e81cf004899b.png)
⑤点“已安装”页面
⑥点“应用更改并重载前端”
![](img/zhuanqian_e262ffe3d2420c8db7afa2e79145b1f5.png)
安装完成
### 02.使用方法
回到ControlNet，点预处理图旁的“编辑”按钮即可手动调节点
若编辑区空白，先点一下预处理图再编辑
![](img/zhuanqian_6a0c3bb376c4496a5f5d1ed86a76b46b.png)
鼠标拖动圆形节点调整位置，调好后点左上角“发送姿势到controlnet”
![](img/zhuanqian_946d323cd1f90f978eb536c5d288893d.png)
例如把腿部节点拉长即可生成大长腿效果
![](img/zhuanqian_500485a4baa48c96f0e909b4f015682c.png)
![](img/zhuanqian_831e45f34af1be295c112409f03c13ec.png)
## 6.小结
人体姿势有五个预处理器，使用建议：
原图手指清晰时用带手指识别的预处理器
识别出来手指线条混乱且调不好，就只用身体姿势
表情控制建议用近景特写，识别精度更高
![](img/zhuanqian_bd18b3318570393c79a205d679083633.png)
# 六、线条约束
本节讲lineart、canny、softedge、scribble、mlsd五种模型
原理都是提取画面线稿，再基于线稿生成新图
![](img/zhuanqian_0d5ab17e815abcc11013c2ef633df362.png)
## 1.lineart
lineart专用于线稿提取，可针对不同画风处理
选择“Lineart”，预处理器和模型会自动切换
![](img/zhuanqian_73d6cfe6de807878f2c5bb6e8907f483.png)
打开预处理器
不同预设识别不同类型线稿
动漫：lineart_anime 或 lineart_anime_denoise
素描：lineart_coarse
写实：lineart_realistic
黑白线稿：lineart_standard
![](img/zhuanqian_abe667ce8d0fce21d9b388a80c7d8d09.png)
### 01.动漫上色
提取动漫线稿再重新上色
![](img/zhuanqian_0b4c8f3b3e8a57e56e170930e92549c5.png)
![](img/zhuanqian_5c8e6187511fdf515b1344789d377400.png)
处理动漫图记得切换二次元大模型
在正式上手之前，先说两个通用小窍门。提示词不要只是标签堆砌，尽量带上质感、氛围一类的描述，并把画面里存在的物体、场景、光影也写清楚，模型才知道哪些元素要保留。
另外上传素材时，注意保持原始的长宽比。比例被拉歪后系统会自动裁切拉伸，成片就会变形。
下面按类别展开实操。
### lineart 线稿方向
ControlNet 的模型选择：
预处理器：lineart_anime 或 lineart_anime_denoise 模型：lineart
![](img/zhuanqian_3f9c6de4521c9730cc0a460abbd99baf.png)
两种预处理器的视觉不太一样，建议各跑一次后挑自己更顺眼的那套。
lineart_anime
![](img/zhuanqian_709fb537b170738e2dad01df5247b8f7.png)
![](img/zhuanqian_9c8b453a7c58fe9abb7d56d64fd36378.png)
lineart_anime_denoise
![](img/zhuanqian_9c0e67e1cfa3fc03363428e13a186165.png)
![](img/zhuanqian_716f487d021ff60ba5c1debe1f9341d4.png)
### 02.素描类照片
![](img/zhuanqian_db25b505505f09aa6a842e3f1143c692.png)
![](img/zhuanqian_d14af5162e9ce180fa0dfbe57b735a5f.png)
ControlNet 的模型选择：
预处理器：lineart_coarse 模型：lineart
![](img/zhuanqian_2d2e08a5eb26e01eeb2dfc65eb0f170d.png)
### 03.写实人像
可以把日常的生活照丢进去，先提炼轮廓再做二次元头像。
![](img/zhuanqian_d304a68d00f15ab9d5b1e65202a79d3c.png)
![](img/zhuanqian_465fcd404d237ad1db9ea2c545bcfc63.png)
真人转二次元时，最好先换成偏向人物的绘画大模型。
ControlNet 的模型选择：
预处理器：lineart_realistic 模型：lineart
因为真人五官与动漫比例差异明显，这时可把 ControlNet 的影响强度适当调低。
![](img/zhuanqian_ce684d25f8e26f87ed52682685c190f3.png)
如果目标只是做高度相似的写实复刻，同样思路也能把一张真实照片映射成另一张长得很像的真实照片。
![](img/zhuanqian_965416fb1cbf599d9fcc209bb2d14a5e.png)
![](img/zhuanqian_dee12ef11675a7a9dd477183dce90471.png)
### 04.黑白线描
![](img/zhuanqian_fa3f866b989a198b83e36b4036da65b9.png)
![](img/zhuanqian_d87936da5af2b193c758bfce6a2c4ef0.png)
![](img/zhuanqian_53430ffd90f63e69a203b80e380f5685.png)
ControlNet 的模型选择：
预处理器：lineart_standard 模型：lineart
![](img/zhuanqian_6a1dec807e250c8f5af2166d11516819.png)
## 2.canny
canny 能捕捉画面里绝大部分边缘，保真度很高，比较契合二次元质感。
![](img/zhuanqian_d25928276036dc7704e579f1bcb462ec.png)
![](img/zhuanqian_fcc7f85bfc1d2f03644505b0642098e7.png)
ControlNet 的模型选择：
预处理器：canny 模型：canny
![](img/zhuanqian_eb346d68bd62b17a3ea67b1f971f89ab.png)
![](img/zhuanqian_b3dbfb8644f89428d50f7efea3480038.png)
![](img/zhuanqian_dfa874248c63859141ae62128276180e.png)
## 3.softedge
softedge 只保留轮廓的大致走向，线条柔和，会给 Stable Diffusion 更大的创作空间。
![](img/zhuanqian_d64629762c77a7a93379eaf2d8e4febf.png)
![](img/zhuanqian_b69450153a80a294092b524d962a0389.png)
ControlNet 的模型选择：
预处理器：softedge_pidient 模型：softedge
![](img/zhuanqian_a1c6394ab81a5e219c10cc73a4cb3889.png)
![](img/zhuanqian_d45c7ae96be0bb22c10098b48fd49fb7.png)
![](img/zhuanqian_29489a5e18de05e85241ede819eab997.png)
## 4.mlsd
mlsd 仅识别直线，很适合建筑、室内结构这类题材。
![](img/zhuanqian_b6472127c093a0a696d443e6bd26a2e5.png)
![](img/zhuanqian_8fb109f6e2184b31c77fbd6f2dc1783f.png)
ControlNet 的模型选择：
预处理器：mlsd 模型：mlsd
![](img/zhuanqian_e3e83ac901924d2817842147309c32d0.png)
预处理后的结果基本只剩直线，带弧度的绿植、瓶罐等线条会被舍弃。
![](img/zhuanqian_44b886b0e7f37d3bc91dc0f9d0b4193c.png)
## 5.scribble
使用逻辑跟图生图的涂鸦差不多，把自己随手画的线套进去，再用提示词生成同线条的画面。
![](img/zhuanqian_70d493faee2f46c0cb7f6488f1d08b4f.png)
![](img/zhuanqian_99b830cb766045db31fa47f0c239001a.png)
ControlNet 的模型选择：
预处理器：invert 模型：scribble
![](img/zhuanqian_9a946a366dd59ae2762c683a1864c2fa.png)
## 6.小结
线稿类选择可以参考：
1. 想最大程度贴近原图：canny
2. 只想固定构图，给 SD 更多变化：softedge
3. 人像、素描类素材：lineart
4. 建筑装潢类：mlsd
# 七、空间深度约束——depth
对建筑线条的还原很到位，前后景的远近层次也很清晰。
![](img/zhuanqian_8a933fbf4274f6cd708ef28ae1865826.png)
![](img/zhuanqian_df07530340edcdf938bcd79045c0a0ab.png)
ControlNet 的模型选择：
预处理器：depth_leres++ 模型：depth
![](img/zhuanqian_6a66799f337c7e3bfb048d85859f3aea.png)
# 八、物品种类约束——seg
会用不同色彩区分画面里的不同物件。
![](img/zhuanqian_630d2fe29b19d1c8e25f2be1907e9594.png)
![](img/zhuanqian_6eb37f709030d514b5eba27137a7ea59.png)
ControlNet 的模型选择：
预处理器：seg_ofade20k 模型：seg
![](img/zhuanqian_e40bb1f036d5c9187e6d3c1e5c7d61a0.png)
可以把 seg 产生的色块图导出，用 PS 等修图软件改动物件颜色，SD 就会按改动后的色块生成对应内容。
网盘里附了一份对照表，说明了各颜色代表的物品。
![](img/zhuanqian_b69a836a9267afecb33108be6b1db9ef.png)
![](img/zhuanqian_b8a0948826be2b58b54573882c7e0923.png)
## 小结
建筑装潢目前有三种思路：
1. 只保留整体结构：mlsd
2. 保留物体的前后顺序：depth
3. 还原原图物品并支持后期改色块：seg
depth 与 seg 除建筑外，也能用在人物照上。
# 九、风格约束
本节涉及 shuffle、reference、normal、t2ia 四个方向。
![](img/zhuanqian_fa24d16bbeea70167781f343a83ee6e7.png)
## 1.shuffle
能把其它图片的画风迁移到自己的照片上。
下图第一张为原图，后三张分别是水墨、油画、赛博朋克风格迁移的结果。
![](img/zhuanqian_2510b7e98229b82b1fd08a8638e7fe43.png)
![](img/zhuanqian_8a307d8f59d8a87518f7556f288892d0.png)
![](img/zhuanqian_b6f96daa85aac4d79ff23b832d22ea18.png)
![](img/zhuanqian_c9b0bf0f6c810f9203f58c5c31edee6c.png)
建议先用大模型和提示词生成一张满意的图并固定随机种子，再打开 ControlNet 把目标画风作为参考。
ControlNet 的模型选择：
预处理器：shuffle 模型：shuffle
shuffle 有时会牵动原图形貌，可把“引导介入时机”调到 0.2~0.3，先定大形再改画风。
也可以挂两套 ControlNet，一套锁线稿，一套负责画风。
![](img/zhuanqian_f578b0c996056ab8ca149adf0e84b490.png)
## 2.reference
能比较完整保留原图的角色特征。
### 01.让照片动起来
让坐着的小狗跑起来。
![](img/zhuanqian_9d761b62078562f0913695936e1888cb.png)
![](img/zhuanqian_00be00131cd401f32083039d969e017b.png)
先选用写实大模型，提示词写：一只狗在草地上快乐地奔跑
![](img/zhuanqian_3aaaa46c06612bb21de3a921044522f0.png)
ControlNet 的模型选择：
预处理器：reference 不用模型
![](img/zhuanqian_bc1540731924a0a2919fdfad97f537c9.png)
### 02.还原角色
给 SD 一张人物参考，它会依据五官、发式还原该人物。
![](img/zhuanqian_4b46d07fc15b469852158013dbf2eff4.png)
![](img/zhuanqian_48baa5eb7293a1bb81dbd08a0de14bf5.png)
操作同上，提示词里还可以加上情绪、服饰、发型的描述。
![](img/zhuanqian_0dbc76b947d5b0cc6422304db1f1c969.png)
![](img/zhuanqian_fd3de7b7b48bd100ae7e7820d7ad9c99.png)
## 3.Normal
可借鉴原图的明暗关系，同时保留姿势。
![](img/zhuanqian_9f0af40afe23cbf6fce6c1970c556055.png)
![](img/zhuanqian_e745dcd5548bf4947ed06b9e475ca4e1.png)
ControlNet 的模型选择：
预处理器：normal_bae 模型：normalbae
![](img/zhuanqian_7c495244e3a0b70cd5229c336cf3f35e.png)
## 4.t2ia
t2ia 比较特殊，不同预处理器对应不同模型，主要有三类用途：
1. 把原图色彩模糊成马赛克再重绘
2. 提取素描线稿生成真人照片，效果一般，用 lineart 更直接
3. 参考原图风格生成相似风格
参考原图色彩，把画面模糊成马赛克再生成。
![](img/zhuanqian_309efe6350723e2ec7d6a4a8cb8e39a8.png)
![](img/zhuanqian_895c4dc2d5e7072339e359f25e011eb2.png)
ControlNet 的模型选择：
预处理器：t2ia_color_grid 模型：t2iadapter_color
![](img/zhuanqian_c3eb6af65acd8b4afe070d677170ed24.png)
# 十、重绘——inpaint
跟图生图的局部重绘类似，但 inpaint 的融合更自然。
## 1.消除图片信息
![](img/zhuanqian_4ba6665e805ec4f38af6f75cc6196ab3.png)
![](img/zhuanqian_b55c138af9ac16e5102be1b222c9fa1b.png)
![](img/zhuanqian_af773b59c4f83d2eee430c51e7ef0a1b.png)
提示词填写照片背景的描述。
ControlNet 的模型选择：
预处理器：inpaint_global_harmonious 模型：inpaint
inpaint_global_harmonious 会整图重绘，融合感强但色调可能变化。
inpaint_only 只重绘涂黑区域。为了更贴近原图，可把控制强度拉满。
![](img/zhuanqian_47d6c248cdc30417604d3221e02c40a3.png)
对比图生图局部重绘，inpaint 明显更通顺。这张是筛选多张后挑出的。
![](img/zhuanqian_878cdb80e36266bd6b68f03e0b06a310.png)
## 2.给人物换衣服
![](img/zhuanqian_5df58c9313f252e170b262f533da41c6.png)
![](img/zhuanqian_d621786130d4dfe6f7c19dcd68ddf0bc.png)
操作同上，只是提示词改为服饰相关。
# 十一、特效——ip2p
给照片加特效，目前偏娱乐，比如让房子变冬日、着火。
![](img/zhuanqian_ce9e157fb590936dd6f844aec476d064.png)
![](img/zhuanqian_3793c2cb3307419c1995f711e665bd91.png)
![](img/zhuanqian_ab31f6dc7793894321c99b99551b6a85.png)
提示词写法比较固定，用：make it....
例如让它变成冬天，写：make it winter
ControlNet 的模型选择：
预处理器：无 模型：ip2p
![](img/zhuanqian_a716908b95fd13de9fa83bedf4bb5169.png)
# 十二、加照片细节——tile
tile 玩法很多。
## 1.恢复画质
![](img/zhuanqian_16e956651dd6202c8dea3fbe1cad5653.png)
![](img/zhuanqian_5817ecce1710a68654a679b6bea62837.png)
ControlNet 的模型选择：
预处理器：tile_resample 模型：tile
![](img/zhuanqian_3ac328b4eb11bcb22b41e793e261d7af.png)
但对真人可能不友好。tile 的原理是先舍弃部分细节再重新添加，SD 补上的细节容易让面部失真。
![](img/zhuanqian_dd7ee477c365752da808dcc360089394.png)
![](img/zhuanqian_dd4eed85d0d11a4401385b9f057b2628.png)
## 2.涂鸦
把手绘草图交给 SD 润色。
![](img/zhuanqian_b9e42b039940872f743ab00dcf006da6.png)
![](img/zhuanqian_5f4a0cf02adf9c90b2aee4585568906d.png)
## 3.真人变动漫
![](img/zhuanqian_773df3995c155e3924f0877717af7d48.png)
![](img/zhuanqian_1624a9ed26f86ef2b6060d28f21d2f80.png)
## 4.动漫变真人
![](img/zhuanqian_739bcdf17b0d1725224982a88e4d1576.png)
![](img/zhuanqian_1ce75726713994fbce60bfe25835a51a.png)
![](img/zhuanqian_1715b61bc09584d2e69d1f2ae38c8114.png)
![](img/zhuanqian_42cc619bdf6e93fe4e92ec67c3a35c7a.png)
# 十七、结尾
这是整套 ControlNet 的思维导图，希望帮你理清功能。
现在用 SD 很多时候仍是“抽卡”，ControlNet 的作用是提升中奖率，并非保证必出满意图。模型、提示词、参数都需要反复微调。
AI 技术仍在快速迭代，未来模型会更多，最终目标或许是让出图与脑海想象完全一致。
如果你对 AI 感兴趣，欢迎关注我的公众号：吴东子AI，也欢迎分享给身边想学 AI 的朋友。里面有我之前的所有文章，后续也会持续更新实用的 AI 干货。
我是吴东子，用奶奶都能听懂的方式分享可落地实操的干货，我们下期见！
网盘链接：https://pan.baidu.com/s/1EFXv7dgWu2vIH86gwSpfkQ?pwd=4dxj
提取码：4dxj
吴东子AI账号简介：https://ry5hwpuf7b.feishu.cn/wiki/space/7283841978071072772?ccm_open_type=lark_wiki_spaceLink