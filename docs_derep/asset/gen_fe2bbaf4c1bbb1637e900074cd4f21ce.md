# 用 Llama2 搭起自己的本地大模型，我把部署全流程拆给你看

> 原文：[`www.yuque.com/for_lazy/thfiu8/vnq4w0y09bbb6r73`](https://www.yuque.com/for_lazy/thfiu8/vnq4w0y09bbb6r73)

## 25 赞 用 Llama2 为例，教你部署自己的私有大模型

作者： 小辉 AI 教练

日期：2023-09-04

## 一、为什么现在值得自己部署

AI 圈最近被一则消息带飞。Meta 携手微软正式放出 Llama 2 的开源商用版本。

LLaMA 是 Meta 推出的一个基础大语言模型，近几个月来大量优秀开源项目都是在它之上二次开发。Vicuna、LongChat 等热门模型都源自 LLaMA 的微调。LLaMA 的开放极大推动了开源大模型生态的繁荣。而微软 Azure 官宣上架 Llama 2，也等于是为其正式发布盖棺定论。

对个人开发者和企业来说，这无疑是质的飞跃。国内还在卷百模大战的时候，我们已经能像玩 Stable Diffusion 一样，把模型拉到本机跑，甚至自己微调 LoRA 了。过去做垂直行业定制，只能靠科学上网调用 GPT 接口，做个简易套壳。现在你可以拥有完全私有的模型，数据不出内网也能干定制化应用。

当然，横向比较下，Llama 2 与 GPT 之间仍有距离。但从一代到二代仅隔数月，迭代速度惊人。

[PRE0]

[PRE1]

[PRE2]

本篇就手把手演示如何落地部署 Llama2。官方提供了 3 个尺寸的模型：7B、13B、70B。这里我以参数量最大的 70B 为例展开。7B 版模型包大概 7GB 左右，在 A5000 显卡上体验已经很顺畅。70B 版则需要 35GB 左右的模型文件，显存建议 40GB 起步，我在 A40 48G 的机器上跑起来很流畅。

[PRE3]

## 二、实操部署步骤

1.  准备算力

我以 AutoDL 云容器为例讲解，其他云厂商流程大同小异。

先去算力市场挑一台满足显存需求的实例。部署 70B 建议选 A40，显存 40GB 以上，约 2.8 元/小时。

[PRE4]

选定配置后点租用，进入实例创建环节

[PRE5]

镜像建议选 PyTorch 基础版即可，别选最新版，系统兼容性会有问题。确认后点“立即创建”

等约一分钟，容器就会启动成功：

[PRE6]

进入 Jupyter ，打开 Terminal 终端，就可以开始动手了

[PRE7]

2.  部署 Text Generation Web UI

先把项目仓库 [`github.com/AYLIEN/text-generation-webui`](https://github.com/AYLIEN/text-generation-webui) 克隆到服务器，接着按官方文档装环境依赖：

1.  安装 Conda

2.  [`docs.conda.io/en/latest/miniconda.html`](https://docs.conda.io/en/latest/miniconda.html)

3.  On Linux or WSL, it can be automatically installed with these two commands ([source](https://educe-ubc.github.io/conda.html)):

1.  新建一个 conda 环境

1.  安装相关依赖

1.  下载模型

界面部分搞定后，就差模型了。操作和 SD 一样，把模型文件放到 models 目录下，UI 就会自动识别加载。

[PRE8]

想从 Meta 官方拿原版模型需要先提交申请，官网填表后几分钟就会把下载 key 发到邮箱。

[PRE9]

不过原生的模型格式不能直接在 text-generation-webui 里用，默认只支持 Hugging Face 格式。所以要么自己转格式，要么直接用别人转好的。这里我推荐直接用 TheBloke 大佬在 Hugging Face 上转换好的 GPTQ 版本，省事又稳定，各版本地址如下：

1.  [`huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ`](https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ)

2.  [`huggingface.co/TheBloke/Llama-2-70B-GPTQ`](https://huggingface.co/TheBloke/Llama-2-70B-GPTQ)

3.  [`huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ`](https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ)

4.  [`huggingface.co/TheBloke/Llama-2-13B-GPTQ`](https://huggingface.co/TheBloke/Llama-2-13B-GPTQ)

5.  [`huggingface.co/TheBloke/Llama-2-7b-Chat-GPTQ`](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GPTQ)

6.  [`huggingface.co/TheBloke/Llama-2-7B-GPTQ`](https://huggingface.co/TheBloke/Llama-2-7B-GPTQ)

### Hugging Face Hub 下载方式，推荐

1.  启动 UI

下面这条命令把模型映射到 “TheBloke_Llama-2-70B-GPTQ”，并监听 6006 端口，利用 AutoDL 的自定义服务就能通过浏览器访问。

[PRE10]

打开 UI 后可以看到主界面，先点顶部菜单进入 Model 页面，选择已下载的 70B 模型加载

[PRE11]

当页面提示“Successfully”就说明模型加载成功

[PRE12]

加载完就能直接和 Llama2 开聊了

[PRE13]

默认的生成模式体验感一般，可以切换到更熟悉的 Chat 聊天模式

[PRE14]

[PRE15]

Web UI 的一个亮点是可以自定义角色，比如设定人设、语气、背景等

[PRE16]

[PRE17]

多模型共存：

Text generation web UI 天生支持多模型混用，只要把不同模型都放到 models 文件夹，就能在界面里一键切换。

[PRE18]

飞书和视频教程链接：https://j0oqwdylc47.feishu.cn/docx/G2uvdNJIloP8D8xIXBccKZDunYg

* * *

评论区：

暂无评论

[PRE19]

* * *