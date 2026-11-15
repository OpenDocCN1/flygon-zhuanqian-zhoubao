# DeepSeek R1 本地部署实操：Ollama 卡顿不再烦，GPU 模式全攻略
你是不是也遇到过这种情况？在本地用 Ollama 跑 DeepSeek，后台一看，CPU 直接飙到 100%，显卡却跟睡着了一样，GPU 利用率连 1% 都不到。更让人抓狂的是，对话生成速度慢到一个字一个字往外蹦，根本没有发挥出电脑的真实实力。别急，这篇就把“从 CPU 切换到 GPU”的完整方法讲透，顺带把 Ollama 的部署教程也一并送上，两篇合一篇，一次搞定。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6a7e93040f82ab2760e51fde72b5fc58.png>
先说明一下，这篇内容对非程序员来说算是进阶教程，但别被吓到——操作步骤不复杂，只要照着走，有点耐心就能搞定。前提是你的电脑得是 N 卡（NVIDIA 显卡），并且内存足够跑得动本地 AI。动手前，一定要先确认自己的显卡型号在 Ollama 支持列表里（官方页面可查），只有支持才能调用 GPU 算力。这里也给大家一个参考：我用的配置是 AI 电脑的入门水平——显卡 NVIDIA 4060 Ti 16G，CPU 是 Intel i5-12400F，内存 32G，硬盘 2T 固态拿来放各种模型和工具，跑 SD、ComfyUI、本地 8B 及以下的模型都很流畅。
如果你想直接部署 Ollama，跳到第三步；如果已经部署好了，只想切换 GPU 模式，直接看第四步。新手建议从头按顺序读。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_31f185404a3bcbfddd588d6da33306b1.png>
## 一、这几个常见问题，先弄明白
### 为什么要在本地部署？
本地部署最大的意义有两个：
- 第一，数据完全留在自己手里，不经过任何在线平台，隐私不会泄露，也可以绕过平台那些审核机制。在线问答时，内容生成一半却被“安全审核”拦下来的尴尬，完全可以避免。
- 第二，配合本地知识库，可以把你自己的文档、日记、私人记录进行 AI 化管理，相当于打造一个“第二大脑”。这对喜欢整理的人来说非常友好，而且数据完全隐私可控，不会被拿去训练平台模型。
### 本地部署有什么优缺点？
- 优点：不联网，彻底离线。
- 缺点：不联网，需要什么资料都拿不到。
### 我到底需不需要本地部署？
需要的人：问 AI 问题总被提示违规，或者想搭建本地知识库（比如日记、私人记录 AI 化、和过去的自己聊天）。
不需要的人：需要联网搜集资料，想用满血版 DeepSeek 的体验，或者提问内容都很正常、完全符合核心价值观。
其实，大部分场景下，直接用各家 App 在线访问 DeepSeek 就够用了。本地部署更多是为了特殊需求，不必强求，这篇教程就当知识储备。
## 二、Ollama 搭建本地模型，三步走
整体思路就三步：下载 Ollama → 把模型拉到本地 → 在命令行里对话。
### 第一步：下载并安装 Ollama
1. 打开官网：https://ollama.com/
Ollama 本身是个管理工具，集合了当下热门的本地模型，你只需一条指令就能下载并使用最新模型。唯一不友好的是它没有图形界面，所有操作都得在 CMD 黑色窗口里敲命令。
2. 点击首页的“Download”按钮，根据你的操作系统选择对应版本。比如 Windows 用户，就下载“OllamaSetup.exe”，注意别装在 C 盘。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e269e2c32380e760677f4cc52f96890c.png>
3. 下载完成后，双击“OllamaSetup.exe”开始安装，点“Install”按提示走完流程。
4. 按 `Win + R` 组合键，在弹出的窗口里输入 `cmd` 回车，打开黑色“命令提示符”窗口，后续操作都在这里进行。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2fad46fe83385a1c86885f01e85e932b.png>
5. 验证是否装好：在命令行里输入 `ollama` 回车，如果有相关输出，就说明安装成功。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_638d9d3f2c9b3722c320730d3a83baac.png>
### 第二步：把 DeepSeek 模型装进 Ollama
1. 回到 Ollama 官网，点击左上角的 `Models` 进入模型库。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e1b77da184b269c361e3fd2642200445.png>
2. 在模型列表里找到 `DeepSeek R1` 并点击进入模型详情页。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_df234b1bff0bc7fcb950edcacd271323.png>
3. 选择模型版本。默认是 7B，下拉框选 1.5B 版本。这里有个小技巧：模型参数“B”前面的数字乘以 2，就是你内存能跑的最大模型大小。比如你的内存是 16G，那么 7B 模型可以流畅运行，因为 7×2=14，小于 16。
4. 复制页面右侧对应的下载命令。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_127842e81926e358a5c1244c493fc21a.png>
5. 回到黑色命令行窗口，粘贴刚才复制的命令并回车，看到下载进度条就说明模型开始拉取了。等它跑完。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_faf0002ba9e299091f338da90395d72f.png>
6. 下载完成后，再输入一次运行命令，就能在窗口里直接和模型对话了。
### 第三步：常用命令速查
记不住也没关系，输入 `ollama` 回车，它会列出常用操作。
- `ollama run deepseek-r1:1.5b`：运行指定模型并进入对话模式。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0e057dce707a98b1c1422c677d344c35.png>
- `ollama list`：显示你下载过的所有模型和日期。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a646dba3d6ad6d44390db521efd1c39e.png>
- `ollama show deepseek-r1:1.5b`：查看该模型的详细信息，一般用不上。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_156bd13cf1dc5e29d607eab16dea2d65.png>
## 三、从 CPU 切换到 GPU，就这么办
当你熟练使用 Ollama 后，大概率会遇到开头说的那个问题：电脑性能明明很强，但生成就是不连贯，任务管理器一看，GPU 根本没干活，反而是 CPU 被拉满到 100%。这时就需要请出英伟达的专属工具——CUDA。
CUDA 可以理解为英伟达显卡的“加速器”，既能优化游戏性能，也能管理显卡运行状态。想让 Ollama 调用 GPU，就得靠它来搭桥。
### 第一步：安装 CUDA Toolkit
1. 打开英伟达开发者官网：https://developer.nvidia.com/
根据自己的系统版本选择合适的包。**特别注意：安装类型一定要选“Local”（本地）而不是“exe”（网络）**，很多人折腾半天装不上，就是在这里选错了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_87c3bb93e6ba9aa7f0f3211689e19bcf.png>
2. 下载完成后一路安装就行。但有一个坑要避开：安装目录记得选一个空文件夹，别选在安装包所在文件夹里。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cb5c2cbbda7cb6c9091d03ac7d9d94fb.png>
3. 安装完，到命令行里验证一下。和验证 Ollama 同理，输入 `nvcc --version`，如果能显示版本号，就说明 CUDA 装好了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_30f306d2d40179d930816b7b6abfea7e.png>
### 第二步：设置系统变量
系统变量相当于给电脑开了个“传送门”，告诉它“走这条路可以更快地调用 GPU”。如果不设，Ollama 默认只会傻傻地用 CPU。
1. 在 Windows 搜索框里搜“系统变量”，打开对应设置页，然后点击“环境变量”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a6aac7d6fa34ec13163a7a6a82265ea1.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8aafa09dad360ceebc980288b3584494.png>
2. 环境变量分上下两栏：上面是用户变量，下面是系统变量。我们看下方的“系统变量”，在这里添加两个新变量。这两个变量就好比两个路标，一个负责让 Ollama 连上 CUDA，另一个让 CUDA 找到对应的显卡。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c4005dd8b40ffa12ed55dc8ed0e39119.png>
3. 添加第一个变量：
- 变量名：`OLLAMA_GPU_LAYER`
- 变量值：`cuda`
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d0a15ec38b6b69a1995815b259a61fa.png>
4. 添加第二个变量，需要用到 GPU 的 UUID。这个 UUID 得先在命令行里查出来，执行 `nvidia-smi -L`。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bc9839c7f8917354f0dc7a983ce811ea.png>
5. 查到 UUID 后，再添加：
- 变量名：`CUDA_VISIBLE_DEVICES`
- 变量值：你的 GPU UUID
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8f68b213c6f8ac57c90a4c010e05e551.png>
### 第三步：验证是否真的在跑 GPU
1. 重新打开一个命令行窗口，输入 `ollama run deepseek-r1` 启动对话。
2. 同时，再开一个新的命令行窗口，输入 `ollama ps`，看看当前模型是在用 CPU 还是 GPU。
3. 还可以按 `Ctrl+Shift+Esc` 打开任务管理器，切到“性能”选项卡，选择 GPU 观察占用情况。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_791f792569727743fa47e234599ce7c1.png>
到这里，你的 DeepSeek R1 应该已经跑在 GPU 上了，生成速度会有质的飞跃。如果还有问题，建议再检查一遍显卡驱动、CUDA 版本是否匹配，以及环境变量是否设置正确。折腾成功的那一刻，你会觉得一切都值了。