# 用 Llama2 搭起自己的本地大模型，我把部署全流程拆给你看

## 25 赞 用 Llama2 为例，教你部署自己的私有大模型

作者： 龙哥 AI 教练

日期：2023-09-04

## 一、为什么现在值得自己部署

AI 圈最近被一则消息带飞。Meta 携手微软正式放出 Llama 2 的开源商用版本。

LLaMA 是 Meta 推出的一个基础大语言模型，近几个月来大量优秀开源项目都是在它之上二次开发。Vicuna、LongChat 等热门模型都源自 LLaMA 的微调。LLaMA 的开放极大推动了开源大模型生态的繁荣。而微软 Azure 官宣上架 Llama 2，也等于是为其正式发布盖棺定论。

对个人开发者和企业来说，这无疑是质的飞跃。国内还在卷百模大战的时候，我们已经能像玩 Stable Diffusion 一样，把模型拉到本机跑，甚至自己微调 LoRA 了。过去做垂直行业定制，只能靠🪜调用 GPT 接口，做个简易套壳。现在你可以拥有完全私有的模型，数据不出内网也能干定制化应用。

当然，横向比较下，Llama 2 与 GPT 之间仍有距离。但从一代到二代仅隔数月，迭代速度惊人。

![](img/zhuanqian_72a9939c5a1a3ccecf141a60de7a7835.png)

![](img/zhuanqian_3037591bb991934878232de14eb5d88a.png)

![](img/zhuanqian_cdc25a7a620878f707abef16b6b198d2.png)

本篇就手把手演示如何落地部署 Llama2。官方提供了 3 个尺寸的模型：7B、13B、70B。这里我以参数量最大的 70B 为例展开。7B 版模型包大概 7GB 左右，在 A5000 显卡上体验已经很顺畅。70B 版则需要 35GB 左右的模型文件，显存建议 40GB 起步，我在 A40 48G 的机器上跑起来很流畅。

![](img/zhuanqian_603db663cd403b6bab645d74067d7c62.png)

## 二、实操部署步骤

1.  准备算力

我以 AutoDL 云容器为例讲解，其他云厂商流程大同小异。

先去算力市场挑一台满足显存需求的实例。部署 70B 建议选 A40，显存 40GB 以上，约 2.8 元/小时。

![](img/zhuanqian_fa2732e2ba00d571be090e5ff453add6.png)

选定配置后点租用，进入实例创建环节

![](img/zhuanqian_b0ac940029ef4666b2080fa5770f8d08.png)

镜像建议选 PyTorch 基础版即可，别选最新版，系统兼容性会有问题。确认后点“立即创建”

等约一分钟，容器就会启动成功：

![](img/zhuanqian_8418574e2f4cb86dfad671a20e9942c3.png)

进入 Jupyter ，打开 Terminal 终端，就可以开始动手了

![](img/zhuanqian_3005834b7f15637a60c70042d0d6e76a.png)

2.  部署 Text Generation Web UI

先把项目仓库 [`github.com/AYLIEN/text-generation-webui`](https://github.com/AYLIEN/text-generation-webui) 克隆到服务器，接着按官方文档装环境依赖：

1.  安装 Conda

2.  [`docs.conda.io/en/latest/miniconda.html`](https://docs.conda.io/en/latest/miniconda.html)

3.  On Linux or WSL, it can be automatically installed with these two commands ([source](https://educe-ubc.github.io/conda.html)):

1.  新建一个 conda 环境

1.  安装相关依赖

1.  下载模型

界面部分搞定后，就差模型了。操作和 SD 一样，把模型文件放到 models 目录下，UI 就会自动识别加载。

![](img/zhuanqian_2766108c7b5343756f6c81c6b838ed25.png)

想从 Meta 官方拿原版模型需要先提交申请，官网填表后几分钟就会把下载 key 发到邮箱。

![](img/zhuanqian_2a94514e1d14da318db8673a3b47039e.png)

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

![](img/zhuanqian_1c90dc331562561600f16e2623fa010e.png)

打开 UI 后可以看到主界面，先点顶部菜单进入 Model 页面，选择已下载的 70B 模型加载

![](img/zhuanqian_fffa61c85f982c23aaf615224468b210.png)

当页面提示“Successfully”就说明模型加载成功

![](img/zhuanqian_36724662b361fcdb6b72b801eab3d70a.png)

加载完就能直接和 Llama2 开聊了

![](img/zhuanqian_83f46f165daccc6c40e6a8ea23df9b13.png)

默认的生成模式体验感一般，可以切换到更熟悉的 Chat 聊天模式

![](img/zhuanqian_8a348dfa016b30e5fb096f94d9f6b988.png)

![](img/zhuanqian_ba3a1e6dcc6f0c7417cd99130b26829f.png)

Web UI 的一个亮点是可以自定义角色，比如设定人设、语气、背景等

![](img/zhuanqian_69750b494fe3fb6821a76d7f97914536.png)

![](img/zhuanqian_1e0a8350ffcf3cde189b0b2be4e19c39.png)

多模型共存：

Text generation web UI 天生支持多模型混用，只要把不同模型都放到 models 文件夹，就能在界面里一键切换。

![](img/zhuanqian_24f3f97b98129fc0c0bd856b83722aca.png)


* * *

评论区：

暂无评论

![](img/zhuanqian_1c37d505930596d12a88ab23e11aa07a.png)

* * *