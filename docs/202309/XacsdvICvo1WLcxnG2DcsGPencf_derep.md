# 如何通过ChatGPT生成视频特效？Code Interpreter GPT编写代码实现Chrome插件

自从今年年初迷上“用ChatGPT写代码”这件事之后，我陆续做了不少尝试，也踩了不少坑。最值得纪念的一步，是在GPT的帮助下从零做出了自己第一个Chrome插件，还因此收获了不少圈友的认可，甚至拿到了一颗龙珠。说实话，我并不是一个科班出身的程序员，编程基础很弱，但这段经历让我彻底改变了“非程序员能不能做技术产品”的看法。

先说一个大前提：我很清楚，靠ChatGPT来做开发并不是最专业、最高效的路径，很多资深的独立开发者会有更轻更快跑通MVP的办法。但我还是坚持用AI编程这条路，原因只有两个：

第一，以前我一个人根本写不出那种涵盖几十个功能模块的插件，光是拆分逻辑就能把我绕晕。但ChatGPT帮我在第一周做出雏形，第二周就完成了改版和上线，之后还一连迭代了好几版。现在插件虽然还没赚到钱，但用户数已经接近1000人，每天看着后台数字在涨，这种正反馈真的会让人上头。

第二，很多没有编程背景的人，即使拿到了GitHub上的开源代码，也不知道怎么改、怎么上线。但ChatGPT让这件事件的门槛大大降低了。你只需要能用中文把需求说清楚，再配合一点点沟通策略，完全可以让它帮你做出一款具备完整功能的小工具。

接下来聊聊重点：今年7月，ChatGPT发布了Code Interpreter，也就是后来的Advanced Data Analysis。当时我第一感觉是，这个功能太震撼了——它能读懂代码、自己写代码、自己运行代码，还能自己发现报错并且不断重试。但用了一阵子之后也发现，它的能力和GPT4相差不大，面对一些稍微复杂点的需求，同样会翻车。

我做过一些好玩的实验，比如让Code Interpreter用一段GitHub上现成的特效代码，把用户上传的图片生成“隐形特效”视频。成功后我还让它一口气列出了10种可实现的视频特效：

缩放波动、色彩旋转、镜像翻转、3D旋转、像素化、融化效果、扭曲波、光晕闪烁、破碎效果、心跳效果。

整个过程它都能自己写Python程序，然后在临时环境里运行出来。但过程中也频繁报错，受限于运行环境和算力，有些任务并不能顺利完成。但最惊艳的地方在于：这些错是它自己发现、自己试着修正的。换句话说，ChatGPT已经不只是“生成代码”了，它开始像人一样，接到任务后自己构思方案、自己执行。

后来我又试了一次更大的挑战：让它把GitHub上那段Python特效代码，改写成Chrome插件。这个过程非常磨人，整整耗了一个下午，中间经历了大量失败和反复调试。但正因如此，我才慢慢摸索出一套和ChatGPT协作编程的方法论。

第一个策略是分步走。不要让ChatGPT一次性输出整个项目的代码，它会非常容易中断，而且功能逻辑越复杂越容易出错。先让它列出“这个项目需要哪些文件”，再一个一个文件让它写出来，效果会好很多。

第二个策略是切入点一定要小。别想着把整个项目丢过去让AI一把梭。先抽象出最小可用功能，比如插件先做到“上传一张图片→做个简单滤镜效果”，先跑通，再去加新的功能模块。这样出了bug也容易修，整体成功率极高。

第三个策略是只给它“最小相关代码”。每次要求改功能时，不要贴一大堆无关代码，只需要把需要改动的那一段代码给ChatGPT，把其他部分用“部分代码省略”替代。它在这种约束下给出的修改方案，基本不会和你原有逻辑冲突。

第四个策略是让它反复检查。每添加一个新功能之前，重新开一个对话窗口，把需求和相关代码重新发一次，让它确认逻辑、检查问题。Code Interpreter还能直接对压缩包里的代码做整体审查，在整个过程中，它既当程序员又当测试员，效率提升是肉眼可见的。

不管怎么说，AI编程的想象空间远不止“写几个脚本”这么简单。它现在已经能自己写代码、自己跑、自己修，以后再加装各种“手和脚”——连接外部工具和硬件，变成能够闭环执行任务的智能体，那一天真的不远了。

![](img/03ec16051789398970029b3987a133bc.png)

![](img/bb6a1ed103199bfe3c064353bc6852b9.png)

![](img/ddbe32977500f54731c760f47c753937.png)

```
I want to apply the disintegration effect from Avengers to this image. Can you help me with it? Provide me with a link to download the video generated. Use the code below:

import imageio
import numpy as np
import random

# Load the image
image_path = "[INSERT IMAGE PATH HERE]"
image = imageio.imread(image_path)

# Define the block size
block_size = 4

# Get the dimensions of the image
height, width, _ = image.shape

# Make sure the image dimensions are divisible by block size
height -= height % block_size
width -= width % block_size

# Crop the image to the new dimensions
image = image[:height, :width]

# Calculate the number of blocks in each dimension
num_blocks_y, num_blocks_x = height // block_size, width // block_size

# Create an index map of blocks
blocks = np.dstack(np.mgrid[0:num_blocks_y, 0:num_blocks_x]).reshape(-1, 2)

# Multiply the indices by the block size to get the pixel coordinates
blocks = block_size

# Define the distance to move the blocks (Ask the user for X in percentage, tell user default = 10%)
distance = round(0.1  width)  # Replace 0.1 with X

# Define the number of times to move each block
move_count = 3

# Create a copy of the original image to work on
working_image = image.copy()

# Convert the blocks to a list and randomly shuffle it
blocks_list = list(map(tuple, blocks))
random.shuffle(blocks_list)

# Define the number of blocks to move (Ask the user for Y in percentage, default = 2% of the total blocks)
num_blocks_to_move = int(0.02 * len(blocks_list))  # Replace 0.02 with Y

# Create a video writer context
with imageio.get_writer('/mnt/data/disintegration_effect.mp4', mode='I', fps=30) as writer:
    # Write a static image to the first 3 frames
    for _ in range(3):
        writer.append_data(working_image)

    # Loop over the blocks in the shuffled list
    for _ in range(move_count):
        for i in range(0, len(blocks_list), num_blocks_to_move):
            # Select a slice of blocks to move
            blocks_to_move = blocks_list[i:i+num_blocks_to_move]

            # For each block, move it to the left by the specified distance
            for block in blocks_to_move:
                y, x = block
                shift_distance = int(min(distance * random.random(), x))  # Don't shift more than the x-coordinate of the block

                if x-shift_distance >= 0:
                    working_image[y:y+block_size, x-shift_distance:x+block_size-shift_distance] = working_image[y:y+block_size, x:x+block_size]
                    working_image[y:y+block_size, x:x+block_size] = 0

            # Write the frame to the video file
            writer.append_data(working_image)
```

![](img/5862bdb20cdadecf5056b3ac17409e81.png)

![](img/4e705db573ca83f4a744adfade1a7b7e.png)

![](img/0dfebceb3ebcf92e7ec82122da380e47.png)

![](img/09e8ea9e14dd8b49eec722c119c6d93e.png)

![](img/09b3a50f56b52756d69e96de652f111d.png)

![](img/99cce29455cb2d5a230639d3474958dc.png)

![](img/6faba6aa2465e937587b517925c1c3c6.png)

![](img/ff2438f7f2f026005e8c6330b3da71e0.png)

![](img/c17409a5e986905918b17273e8f100e9.png)

![](img/9d08fea490ea43fa3ee7271034528d6d.png)

![](img/a4a7c6fa348157fdab4bb8c6972df98f.png)

![](img/4ff8874ed11afdf3d4c4e3d1d86bdf68.png)

![](img/a36a5b0ebe04a6228628dab20879cf16.png)

![](img/b5a1829382a531f08556d395079ec00b.png)

![](img/1bf19f504e2763e2bd296bfba49aa724.png)

![](img/218e61d873ceb2d36bdc95791fc05abd.png)

![](img/3253be0076e7cec2342cb7cd41d9267b.png)

Code Interpreter在过了一遍代码后，把里面存在的症结给指出来了。紧接着我们问ChatGPT，如果要达成图像隐形的效果，代码该怎么改：

![](img/7c9b9a95cc56421459a354588a934cd0.png)

ChatGPT给出了一批修改方向，随后我们就着这些建议逐条让它去改：

![](img/b76c622bcb388b88ec21210154178840.png)

思路五：深入到具体功能和代码层面去引导ChatGPT

当ChatGPT围绕同一个问题反复拉扯，几次对话下来依然卡住不动时，最有效的做法是把需求拆到功能层和代码层，用自己的经验去判断，主动给它换一条实现路径。

就拿这个插件来说，ChatGPT始终死磕 pixi.js 去做图像隐形，一直搞不定。我们就可以这样牵着它走，让它换个思路达成同样效果：

![](img/027f86e74b1eab4cd4a4c5d9bd3fc898.png)

于是我们让它放弃pixi.js，改用fabric.js来完成图像处理：

![](img/9054f351f625396c7ad49c62d434fc27.png)

思路六：让ChatGPT自己审视代码并修复Bug

一般在聊了好几轮仍然不通时，ChatGPT会开始在代码里加 Console 日志来排查。如果它没主动加，你也可以直接提示它在关键片段里加上跟踪日志，然后把运行时的输出或报错原样复制给它检查。

比如我们在测试插件时撞上了这个错误，就可以把报错贴给ChatGPT：

![](img/55655964cac10d55c4ac68e9a1535703.png)

ChatGPT通常会回溯前面的逻辑链条，顺着错误给出对应的修复方案：

![](img/1c3fdfac9411116964d147482f6ef104.png)

这种方法在用ChatGPT写代码的路上几乎是标配，尤其当项目复杂度上去，或者需求描述不够精准时，更需要反复对话、反复确认。想想看，跟你一起做产品开发的同事写代码时，也会碰到各种坑，只有把一个个问题怼开，产品才有可能上线。我们用ChatGPT编程时，虽然不用亲手敲代码，但必须同时扮演产品经理和测试工程师：把需求讲清楚、把代码跑通后发现的问题提炼清楚再反馈。ChatGPT不只是个工具，它更像一个搭档，必须并肩作战，才能把难题一个个拿下。

最终在ChatGPT的帮助下，这个插件的雏形就出来了：

![](img/fa9de291dc9ded22202682b03cd37258.png)

上传一张图片，点击“Apply Effect”，它就能生成一段视频，再点“Download Video”就能下载。我们可以看到，这个Chrome插件已经能实现一个比较粗糙的把图片转成隐形特效视频的功能了：

## 对Code Interpreter的展望

有不少人把Code Interpreter称为ChatGPT发布以来最具分量的升级，它的解析能力和自主运行能力正在重塑我们的认知。除了常见的数据分析和图表生成，我的朋友文韬武韬正在用它做亚马逊的数据分析和选品，已经挖出不少蓝海潜力的产品。

我自己的侧重点则在编程上，ChatGPT已经帮我搭出了若干产品的雏形。尤其是Custom Instructions上线后，通过预设指令在一定程度上缓解了ChatGPT记忆时长不足的问题。基于此，我尝试用Code Interpreter配合Custom Instructions，实现半自动甚至全自动生成贪吃蛇、飞机大战、连连看这类Chrome插件小游戏。受限于GPT4在编程上的先天短板，这个尝试并非每次都成功，目前仍在持续测试中，有新进展会再来和大家分享讨论。