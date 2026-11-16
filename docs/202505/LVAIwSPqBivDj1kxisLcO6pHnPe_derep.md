# 图像API工作流3_OpenAI（全能4种）
作者：龙哥

OpenAI绘图全家桶接入ComfyUI？这三个模型能批量出图了！连支付都变得接地气

如果你最近在追AI绘画圈的动态，应该已经听到消息：OpenAI放出了GPT-Image-1 API，跟ChatGPT 4o里的图像模型是同款。而ComfyUI这次也够给力，直接上了原生API节点（测试版），等于在ComfyUI里内置了一条通往OpenAI最新图像能力的高速路。

重点来了：你不需要去折腾复杂的API密钥，也不需要注册ChatGPT账号。🛰️或支付宝充值，就能用上GPT-Image-1、DALL·E 3和DALL·E 2三个模型。对国内玩家来说，这简直是“零门槛”体验。

那为什么非得用ComfyUI来跑？因为它的使命不只是生成一张图，而是批量自动出图。更妙的是，它还能和AI视频、AI音频、AI数字人模型联动，一起拼出一条完整的AI视频制作流水线。

![](img/ae627f126b8b72ccf80593295f421d31.png)

下面这份保姆级教程，就把三种模型在ComfyUI里的玩法拆开揉碎讲清楚。

一、GPT-Image-1：技能拉满的全能选手

GPT-Image-1节点一口气支持四种操作：文生图、图生图、多图生图，以及基于蒙版的图像编辑（说白了就是局部重绘）。

1. 文生图
玩法最简单。拖一个OpenAI GPT-Image-1节点出来，在prompt框里写下你想要画面的描述，再接一个保存图像（Save Image）节点，整个工作流就齐了。比如输入“cat stickers（猫贴纸）”。

![](img/dc87c87d3b3a315ddae90fe8904f7d5c.png)

跑起来之后，成品就出来了。

![](img/8d120e4c67fc3df20323515b0bedc624.png)

工作流里还有参数详解和积分消耗的说明，按需选择即可。

2. 图生图
如果你有一张现成的图，想让它换个风格，就用到图生图。加载图像（Load Image）节点把输入图接进来，连到GPT-Image-1节点的image输入口。提示词可以直接下英文指令，比如“turn this image into ghibli style”，让图片变身吉卜力画风。

![](img/33c79c431c19aa03e47a0399eaf9ed4c.png)

别担心只会中文，直接输入“帮我改成适合激光镭雕的黑白线稿”这种描述，它也能照做。

![](img/1fdc257166e8f001eec01b87c73429b1.png)

比如拿下面这张图当输入。

![](img/66a9a8b95d364e8d8cb9acf737cd77d3.png)

运行之后，效果立刻见分晓。

![](img/015c0326f18f55109a37c429416c26e6.png)

同样的，节点参数和积分消耗都有对应说明，照着调就行。

3. 多图生图
以后想“合并”两张图，也不用找PS了。用多个加载图像（Load Image）节点分别读入图片，再用图像组合批次把两个输入拼起来，最后一起喂给GPT-Image-1节点的image输入。想给猫咪加个帽子、顺便统一改成吉卜力风格？提示词写“Put the hat on the cat's head and turn into ghibli style”就行。

![](img/f3e530c6d2c5f7615f4c2a1c501a5c4c.png)

中文需求也没问题：“让猫带上帽子，让图1角色坐在夜间的路边咖啡馆喝咖啡，日本动漫风格，确保2个图片的原始特征保持一致不能改变。”模型会尽量保持两张原图的特征。

![](img/9596174b95fd78797556bcd4e5dee630.png)

布局完成后运行，你会发现两图融合得很自然。

![](img/953d626675445503bf6607ac7040e88f.png)

![](img/97a44ca69832e69108d75913fc26f6ac.png)

这一通操作下来，同样会产生积分消耗，记得留意。

4. 局部重绘
局部重绘看着眼熟？其实和图生图的工作流长得很像，唯一区别是：需要在加载图像（Load Image）节点上右键，打开遮罩编辑器（MaskEditor），把想改的区域涂出来，连到GPT-Image-1节点的mask输入口就完成了。

这里有几个小提醒：上传大尺寸图片时，节点会自动把它缩到合适的尺寸；API返回的URL不会永久保存，只有短期有效，所以看到满意的结果一定要及时保存。

![](img/4264311d4f9b24f02d721baa4b90bcf0.png)

具体操作是：在输入图片上右键，选择“在遮罩编辑器中打开”。

![](img/9aec2fa6ac1da3ef45e4d0938fae98fb.png)

然后在遮罩编辑器里把要重绘的位置涂上，点保存。

![](img/765f71a34e69feb14c0e274c11ee2333.png)

补好遮罩后，把提示词改成类似“Let the cat hold a big fish（让小猫举着一个大鱼）”。

![](img/690cd9ae41097c8694fa1ea73a7443a9.png)

跑完就能看到一只抱着大鱼的小猫了。

![](img/0f1ff28d7ec9b592d0f51b2147d2e523.png)

二、DALL·E 2：老将依然能打，但能力有边界

![](img/f1cfbb3d8e846bd181ceab862131de75.png)

DALL·E 2节点支持文生图和带蒙版的图像编辑，但不支持图生图和多图生图。想直接用图片改图，它办不到。

不过文生图流程很轻松：加载OpenAI DALL·E 2节点，在prompt里写描述，接一个保存图像节点，运行就出图。

![](img/e4ad1e7b25535442c09e46ea336f0068.png)

生成效果如下。

![](img/5a2ccb9f6742f62763c543d3240f2a34.png)

参数设置和积分消耗也都在工作流里给了参考，基本不用费心。

局部重绘虽然能用，但限制条件比较严格：如果要用图像编辑，必须同时提供图像和蒙版，两者缺一不可；而且蒙版和图像尺寸必须一致；大图会自动缩小；API给出的URL同样是短时效，记得及时下载。

![](img/f712a75a89dc54ca0e6da16010b62e13.png)

比如拿下面这张图作为输入。

![](img/878a6390729c13f26150aa550d211ae9.png)

在加载图像节点上右键，找到“遮罩编辑器”。

![](img/1ea5b3d24e98bc840c5aa3ddfef0b749.png)

用画笔把要重绘的区域划出来。

![](img/b989488e59389324f17d003ce68f7f8d.png)

点击运行，结果就在眼前。

![](img/e25997ee6ea6955298e9a8fcb89147f1.png)

三、DALL·E 3：直来直去的文生图典型

![](img/bb86024fe6614b51a317c848f62d68c2.png)

DALL·E 3的定位很纯粹：支持文生图，其他的一律不支持——不能图生图，不能多图，也没有图像编辑功能。

所以它的工作流也最简单：加载OpenAI DALL·E 3节点，填入提示词，连好保存图像节点，运行。试试“A fox running in the snow, with snowflakes swirling around it. The background features coniferous forests and mountains, and there is the evening light.”，也就是一只狐狸在雪中奔跑，雪花旋转，背景是针叶林和山脉，还有傍晚的光。

![](img/28e095e177961b9645904269f500cf04.png)

出图效果相当有氛围感。

![](img/caa77a168d6f800027a4981477b97959.png)

参数配置和积分消耗也有说明，跟着默认调整就行。

四、工作流去哪下载？

完整的JSON工作流已经打包好，直接到下面这个地址拿：

https://gitee.com/lailai666/comfyui_workflow/blob/master/API%20PIC/%E3%80%90API%E5%9B%BE%E5%83%8F%E3%80%91openai.json

下载后放进ComfyUI就能用。三种OpenAI图像模型，四种玩法，批量出图加视频联动，想怎么玩就看你的想象力了。