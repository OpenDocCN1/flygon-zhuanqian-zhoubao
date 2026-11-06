# 用 RooCode + Copilot + MCP 给自己搭一个 Manus 替代体



整套实操我花了两天时间从零跑通，想一次成型的话最好空出一段完整的专注时段来弄。

这套组合不仅能白嫖 Claude 3.5 的使用体验，更关键的是它能拼出一个强力的智能体，绝对值得折腾一把。

最近 Manus 火得不行，但邀请码我一样没有....

翻了些 Manus 的演示案例，其实大多都是让模型开浏览器查资料、调用代码工具写代码，最后把结果打包成网页呈现。

说白了，核心在于编程能力去替人把事办了。

而编程正是 AI 的强项。

于是我琢磨着，完全可以用 AI 编程工具+搜索能力+代码生成+HTML 渲染的闭环，做出一个类似的效果。ps：Manus 肯定远不止表面这些功能，我只是探讨一种平替思路，在没有更好选择时，这个方案已经很能打。

搜了一下发现不少人也在这么玩，我整理出了下面这套可复现的搭建流程，直接开干

# 一、搭好 VSCode 基础环境

Vscode 是整套方案的载体，后续所有插件都基于它安装。如果还没装就先装。

下载地址：https://code.visualstudio.com/Download

装完默认是英文，建议补一个中文语言包。打开扩展面板，搜索 chinese 安装即可

![](img/7bc3281ffc50e81c9bffe9dcaddec34d.png)

插件装好后还要切换语言，按快捷键 ctrl+shift+p，输入 language，选择 configure display language

![](img/c721a55a1e9384b6e5fd39b588289376.png)

选上简体中文，重启 VSCode 就生效了

![](img/96a9bd8bad390c17029d65b887eb5af4.png)

# 二、装上 Roo-Code

Roo-Code 之前叫 Roo-Cline，是 Cline 的一个分支，现在进化得挺好。没有 Cursor 的同学可以用它替代。核心原因是它原生支持 MCP，可以挂载各种外部工具，后面会用到。

在扩展市场搜索 Roo Code，认准带火箭图标的那个，点安装

![](img/e91ef9bc4900d856c9098cd36f606e07.png)

# 三、装上 Copilot

Copilot 是 GitHub 出品的编程助手，本身也能写代码，但我更喜欢 Roo-Code 的体验。那为什么还要装它？因为 Copilot 能调用 GPT-4.0 和 Claude 3.5。免费版每月 2000 次代码补全额度，专业版只要 10 美元/月，比 Windsurf、Cursor 都便宜，很适合重度使用者。

继续在扩展里搜索 copilot 安装

![](img/faacfbb5d7746de679fa9658819b83c8.png)

装完点右下角的图标授权登录，走 GitHub 账号登录流程，没有就先注册

![](img/089a354ff32478d51274bdcc0b433a7e.png)

新版 VSCode 位置可能有变化，大致长这样：

![](img/8c7489dcc6d31a10cdd1748e3c7d08ff.png)

登录成功后会跳回 VSCode，点打开即可完成绑定

![](img/614249dbed36593f8b627449473de9ae.png)

# 四、把 Roo-Code 和 Copilot 的模型打通

到这一步工具都齐了，接下来让 Roo-Code 用上 Copilot 里的模型

打开 Roo-Code 的设置：

![](img/d2f9c00ecf51c66b4b08e50dad1144e2.png)

API Provider 选 VS Code LM API，下面就会列出 Copilot 可用的模型。我选了 Claude 3.5，代码能力更强

![](img/13ef98f585f2c72c50df52c8ed8e8d6f.png)

为了让模型拥有最大操作权限，把下面的权限选项全部勾上

![](img/b847ffbd06fa07547f1a81f2af77938c.png)

点 Save 保存，再点 Done 退出设置

![](img/c301aa33d0db49376e260f1b751e3c76.png)

先做一次简单验证。打开一个本地文件夹作为工作区

![](img/a9edd2c2ebd0e5aafcb75f5d443f2dce.png)

我让它先做个任务：分析 2024 年房价走势，做成报表并用 HTML 页面呈现

![](img/8633633f7fb7143b0c939ed20005bbdb.png)

它开始自动写代码生成网页，一会儿就说完成了

![](img/79e0347a0a5b5c8cdb40f95cadbc5f17.png)

打开生成的页面看看，效果还不错

![](img/9de9f1421a3029de94e1e3b5e897b3f7.png)

# 五、进阶玩法：接入 MCP

注意看上面的网页，数据其实全靠模型知识库，没有联网搜索，准确性存疑。要想更靠谱，就得让 Roo-Code 能联网拿数据。

这就要用到 MCP。MCP 全称 Model Context Protocol，即模型上下文协议，是让大语言模型和外部数据源、工具无缝对接的开放标准。

类比一下就是 USB 接口，按标准开发的工具都能即插即用。现在 Cursor、Windsurf 也都支持 MCP，原理一样。

会不会要写代码？不用担心，Roo-Code 内置了 MCP 创建能力，可以让 AI 帮你搭。今天先做两个实用工具：

1、浏览器自动化工具
2、图片生成工具

把这两样挂上，VSCode 基本就变成一个会编程的智能体了

## 1、浏览器工具

### ① 为什么要模拟浏览器

如果自己搭搜索，通常要接搜索 API，大部分收费，免费的又质量一般。我想的是直接让 AI 像人一样用浏览器去访问、搜索，这不正是 Manus 常用的做法吗？

单就搜索而言 API 更稳定，但浏览器方案一旦跑通，后续就能让 AI 写各种自动化脚本，想象空间更大。

### ② 装浏览器 MCP

GitHub 上有现成的 mcp-playwright，地址：https://github.com/executeautomation/mcp-playwright

这是个浏览器自动化工具，打开它的安装说明

![](img/8e71770266ff669ac0ac948b0581dd96.png)

直接把说明丢给 Roo-Code 让它代为安装

![](img/4d5bfef32f7d2bb6148ec036aa73f585.png)

Windows 用户注意避坑：npx 在 Windows 上经常报错，我折腾了四五个小时才过关。后来找到一份 Windows 专用的安装指南：https://github.com/trevorwilkerson/Windows-MCP-Server-Installation-Verification-Guide

![](img/81275e55755d7b849df16a4a022a6a80.png)

不用看懂英文，把 README 全部复制给 Roo-Code 让它处理

![](img/5e337e649b8ca551de2aafb5b43547f5.png)

它会提示执行命令，一路选 runCommand 直到出现安装成功的信息

![](img/9f848604f8070ceb0bfb78000ba1b48f.png)

然后打开 MCP_Server 配置看看

![](img/9b4da8e191b8eeb82e80dd1567b5f2d2.png)

能看到配置就说明装成功了

### ③ 实战：搜热点新闻并做成网页

我让它用百度搜热点新闻，整理后再生成一个分享网页。第一次运行要勾选 Always allow，之后就不用反复确认了

![](img/6b403220c8e459bbcaa826064349cd8a.png)

它会自动打开网站、解析源码、模拟点击抓取内容。过程看起来繁琐，但能拿到真实页面数据。

如果你只想要搜索结果，直接接 Bing 搜索 API 会更高效。回到本例，任务完成

![](img/6e919db55e686e9966df774cbfd2a92d.png)

执行 Run Command 后自动打开网页，效果如下

![](img/18d927996453a0b8e63cfe887cbcc2e1.png)

浏览器自动化通了之后，很多爬虫、自动化流程都能玩。举个例子

### ④ 再举一例：读链接仿写再排版

AI 经常需要参考网页原文，复制粘贴效率很低。链接读取是必备能力。我试过 fetch 这类读取 MCP，头条、🛰️文章要么被 robot 拦截要么需要登录，基本拿不到。模拟浏览器反而更稳定。

示范操作：

![](img/e9638aca5f55340b7b579f8b09b728e1.png)

等它生成完

![](img/82d4660c5fa51775ed850c3672e2ef1d.png)

有了浏览器工具+编程环境，爬虫、自动化几乎都能轻松实现

## 2、图片生成工具

编程环境本身不生成图片，如果要做设计类网页，就得自己找图。接入图片生成 MCP 很有必要。

### ① 用 Roo-Code 自建图片工具

这次展示另一种 MCP 安装方式：不装现成包，而是让 Roo-Code 根据接口自己创建工具。

打开硅基流动的图片生成文档：https://docs.siliconflow.cn/cn/api-reference/images/images-generations

这是个免费的图片模型。复制 CURL 示例到 Roo-Code，注意把 <token> 换成自己的

![](img/939f5354a1458a6e09b478c8af5478f2.png)

Token 在硅基流动官网登录后就能创建

![](img/fd687be5f77f639b7ff27f3e8bd3f06d.png)

把替换好的完整内容贴给 Roo-Code，提示它：请根据以下 curl 请求，创建一个图片生成 MCP 工具

![](img/71a1e59856205a1ba399f2a0e590a985.png)

创建时会要求确认输入 Y 继续

![](img/d345aaa10960f81d76c7c65dc5450058.png)

后面的选项默认回车即可

![](img/fac22f0780293dc230c8454a84bf982b.png)

Windows 环境下路径问题容易失败，可能需要反复调试。调不通的话可以找我要源码参考，差不多环境直接用也行。

### ② 案例1：自动出图并生成站点

在 Roo-Code 输入建站指令：

![](img/edc8f8afb3ca2974824f6754004a854c.png)

它会自动调用图片模型生成配图并嵌入网页

![](img/83e7cfd682ce5d589133d22590baddbf.png)

打开看看，免费模型画质一般，但链路已经打通。如果换成 ComfyUI 接口，效果会质变

![](img/41d987e38b60e092ad0a5c8ba3b7a3d8.png)

### ③ 案例2：写文章自动配图

再试一次，让它写文章并自动配图，指令如下：

![](img/cf993e3a9b31cbd34f0ff80dd338ca8b.png)

生成完成后的效果还算可用

![](img/0cb94a2c5b57395700cbc9b21c344fb2.png)

以上只是入门示例。后续接入 PPT API 就能自动生成 PPT，接入视频生成 API 就能一键出视频。可能性非常多，而且会越来越完善。