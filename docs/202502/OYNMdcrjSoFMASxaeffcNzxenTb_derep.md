# 图文详解：教你离线在本地电脑跑通 DeepSeek
作者：龙哥



DeepSeek 今年春节一夜爆火，随之而来的就是服务器频繁宕机、排队回复。更关键的是，官网服务条款里明确写着用户上传的内容都会纳入数据采集范围，涉及隐私的信息并不适合直接在网页版里输入。

我在 B 站刷到一个本地部署 DeepSeek 的教学视频，讲解很细，UP 主是“NathMath”。看视频上手总不如图文顺手，我就结合视频内容加上自己的实操，整理成下面这份一步到位的手把手图文版，帮你把 DeepSeek 完整跑在自己的电脑上。

整体流程：

一、安装 LM Studio
二、获取 DeepSeek R1 模型文件
三、把模型导入 LM Studio
四、为 DeepSeek R1 调整运行参数
五、用 Windows 高级防火墙切断 LM 的内外网连接
六、开始离线使用本地 DeepSeek

## 一、安装 LM Studio

1.下载并安装 lmstudio
（1）打开 lmstudio.ai，下载 Windows 版。

![](img/aa365ac3b09d518737f94d9ec73b5fdb.png)

（2）按提示完成本地安装，安装成功后的界面如下

![](img/a6832c9baa23a2b9d1a9d6e68ed42936.png)

## 二、获取 DeepSeek R1 模型【推荐方法二】

1.方法一：在 LM 内直接下载 DeepSeek R1 大模型
切换底部菜单到 Power User 模式，点击左上角 LM Runtimes 按钮

![](img/aecc039c910ecedaf7d3ff77ecdf954a.png)

在弹出的窗口点 Model Search，在搜索框输入 deepseek。

![](img/4ead537565bb5a78b25993354c481e9f.png)

搜索结果会列出相关大模型，选中想要的版本开始下载。举例来说，8B GGUF 量化版，模型体积约 4.92G。

![](img/0764a4725de2946369e9c20d7ff29452.png)

2.方法二：从第三方渠道下载 R1 大模型【推荐】
方法一需要🪜才能顺利获取，UP 主原视频里给了 HuggingFace 镜像站，但实际速度很慢。

更省事的做法是直接用我整理的网盘链接下载 Deepseek-R1-Distill-Llama-8B-GGUF 和 1.5B GGUF 版本模型。

https://pan.quark.cn/s/5e45ea2a1a1c

## 三、在 LM 中导入 R1 模型

1.先把下载好的模型放到正确位置
（1）在 C 盘用户目录下找到 .lmsudio 文件夹，内部有 models 文件夹

![](img/7dc3d671573be78eb8e6e30e0b925ea8.png)

（2）models 目前是空的，需要手动创建两层目录，路径必须严格对应
在 models 下新建第一层文件夹，名字随意，我这里用 LLM

![](img/12c52b02e3501ceebdfb4eb05ba607c1.png)

在 LLM 下新建第二层文件夹，命名必须与模型文件名完全一致，去掉后缀.gguf 即可。例如模型文件名是 Deepseek-R1-Distill-Llama-8B-Q4_K_M.gguf，第二层文件夹就必须命名为 Deepseek-R1-Distill-Llama-8B-Q4_K_M

![](img/717a4aa1cb025a3a43d5461ee0931c28.png)

把下载的模型文件放到这个第二层文件夹里

![](img/83592e5fdb8d75385def1fe326ef4f5e.png)

2.在 LM 中加载模型
点击顶部 select a model to load，就能看到已放置在正确位置的 R1 模型，点击即可加载

![](img/b65bfebd41a59952b1f11183c5c5160f.png)

![](img/4ae713d1b5a99992557cb4265c1194bb.png)

加载后左侧文件夹图标里也能看到该模型

![](img/4f3ab434120273d94aec0ae70a32f280.png)

## 四、为 DeepSeek R1 配置参数

选完模型会直接弹出参数配置页，可在此处调整

![](img/3261ffb0dddb96770fb730d768f947bf.png)

后期想改设置，切换到下方 power user 模式，点击模型旁边的齿轮即可重新打开配置

![](img/68e42c6bd167f52a6c3ca65e0c817fc3.png)

参数含义简述：

* Context length：模型思考时能参考的上下文长度，日常 4096 足够，显卡和内存充足可适当提高，写小说类任务可调到 20000 左右。数值越高对硬件要求越高。
* GPU offload：本地显卡承担的计算层数。无独显选 0，有独显可按需设置。我用 4060 8G，设置了 24 层跑在显卡上。
* CPU Thread Pool Size：CPU 可调用的线程数，建议拉满。
* Evaluation Batch Size：单次计算批次大小，默认 512，有独显可适当上调，我用 1024。
* 其他选项保持默认即可，不要随意修改。

![](img/2bd3ce0621daed9c4d0c6585d7ff278a.png)

配置完成后开始加载模型，加载完毕后可以打开 Windows 任务管理器看一下资源占用。

以 8B GGUF 版 R1 为例，设置上下文长度 8000、GPU offload 24 层、批次大小 1024 时，GPU 8G 中占用约 6G，运行完全流畅。当前还有一定余量，必要时可以再小幅提升参数比如上下文长度。

![](img/afbc690de1c024108537652464dc4d5d.png)

怎么根据本机硬件估算参数？

B 站原视频 UP 主的经验是：
* 无 GPU：1.5B Q8 或 8B Q4
* 4G GPU：8B Q4
* 8G GPU：32B Q4 或 8B Q4
* 16G GPU：32B Q4 或 32B Q8
* 24G GPU：32B Q8 或 70B Q2

但有网友反馈 4060 8G + 16G 内存跑 32B Q4 非常卡。经过实测，给出一个更实用的估算公式：

GPU 显存 + 系统内存 的总和 ＞ 模型参数量数字，就基本能跑。

比如我的电脑显存 8G + 内存 16G = 24，24 < 32，所以 32B 版本会吃力，最终我选择了 8B 版本。

## 五、用 Windows 高级安全防火墙断开 LM 的网络

前面解决了本地部署和运行的问题，还差最后一步：防止本地对话内容被上传。核心就是断网，让 LM 软件与模型之间完全本地交互，不与外网产生任何数据传输，这对处理隐私信息至关重要。

1.打开 Windows 高级防火墙

![](img/c44121771a784956ab6009b35d3fbaa9.png)

2.新建入站规则，分别阻止 lm studio.exe、elevate.exe、lms.exe 三个程序的入站连接
![](img/7b40d05da10c9d85a12321bec9cac1c9.png)

在弹框里指定 LM 安装目录下的 LM Studio.exe

![](img/43648317d57db35b3d5d7d1b52bb3ce4.png)

选择 阻止连接

![](img/91c61a5f1629ff85a8631c56e0a5dea5.png)

为规则命名

![](img/8047fbcd3d30d2b6b68db3749cfb8f5b.png)

同理再建两条入站规则，阻止 elevate.exe 和 lms.exe
elevate.exe 位于 LM 安装包的 resources 文件夹下

![](img/70810d90c5a81d05d8d21cf1a85e9a74.png)

lms.exe 位于 C 盘用户文件夹 .lmstudio/bin 下

![](img/4c99cd6214058ab1381e3cef540b7c76.png)

3.新建出站规则，同样分别阻止 lm studio.exe、elevate.exe、lms.exe 三个程序的出站连接
操作方式与入站一致，再创建三条出站规则

![](img/63992478a0e5697fb559c6e65ff4a345.png)

## 六、离线使用本地 DeepSeek

设置完成后就可以开始对话了。我把 B 站做饭视频的录音转成文字后喂给本地 R1，让它整理成结构化的菜谱，离线也能用。

R1 的最大亮点是可以看到完整的思考链条，这对提升自己的思考方式很有帮助。思考结束后，整个推理过程可以折叠，不占页面空间。

![](img/bffe3098fc2c438b03168f4b64fed190.png)

![](img/a7b945671283850077b3111576c72f86.png)

![](img/e8606e8771278c6dacffcc551d19cf08.png)

再验证一下断网效果，尝试让 LM 访问外部数据，会提示获取失败。

![](img/999b28e29947f5f235746dc389dccd76.png)

## 核心要点回顾：

* 选择合适的 DeepSeek R1 模型版本，参考公式：GPU 显存 + 内存 ＞ 参数量数字；
* 手动下载的模型必须放到指定目录结构下才能被 LM 识别；
* 参数配置要结合本机显卡和内存实际调整；
* 通过 Windows 防火墙分别对 lm studio.exe、elevate.exe、lms.exe 建立 3 条入站 + 3 条出站阻止规则，共 6 条，确保完全离线。