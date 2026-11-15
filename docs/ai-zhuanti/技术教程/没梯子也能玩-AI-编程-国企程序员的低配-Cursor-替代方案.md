# 没🪜也能玩 AI 编程？国企程序员的低配 Cursor 替代方案
# 先说背景
我是牧童，一名在国企摸鱼的程序员。最近 AI 编码风头正盛，Cursor、Windsurf 之类的工具一个接一个出来，看着眼馋却用不上，公司网络环境不允许上外网。折腾了一圈后，我找到了一个能在国内直接用、成本极低的替代组合：VS Code 里的 Cline 插件 + DeepSeek 的 API。
这套组合的优势很直观：
1.  不需要🪜，内网就能跑
2.  用起来很省钱
当然也得泼点冷水：智能程度比不上 Claude Sonnet，遇到复杂需求时容易反复试错，甚至陷入死循环。
总体来说，这个方案更适合网络受限、想先尝鲜、且任务复杂度不高的开发者。
# 具体怎么搭
## 先装 VS Code
VS Code 是微软出品的免费开源代码编辑器，2015 年上线后凭借轻量易用和插件生态成为程序员标配。Cursor 本质上就是在 VS Code 基础上魔改而来，使用逻辑几乎一样。直接去官网 https://code.visualstudio.com/ 下载对应系统的安装包即可。
## 安上 Cline 插件
Cline 是一个开源的智能编码助手，能直接嵌入 VS Code。它可以对接 DeepSeek-V3、Gemini 2.0 等大模型，提供代码生成、调试辅助、任务管理等功能。最近它接入了 Model Context Protocol，也就是 MCP，能自主读写项目文件，几乎可以全自动干活，坐看 AI 爬就行了，属实爽。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_812117cc72a49e5e1b6bf5d8759491e1.png>
## 准备 DeepSeek API
DeepSeek 近期凭借 DeepSeek-V3 在开源阵营里拿下第一名，能力逼近顶尖闭源模型。去官网 https://www.deepseek.com/ 申请接入 API 即可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1bda08b6a50a6e7a72f14b51e15cd008.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_881730eceb3ca92d3849fcea0ae0f4ef.png>
## 在 Cline 里接入 DeepSeek
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9793980a5cc9d4cd6df81d53e9b88b51.png>
1.  打开 VS Code 左侧的扩展商店
2.  进入 Cline 的设置界面
3.  在模型列表里选择 DeepSeek
4.  填入刚刚申请到的 API Key
5.  填入系统提示词，我这边设置的是强制中文回复
# 实际试用
最近看到 Super 黄的《AI 编程蓝皮书》，里面提到一个 Flomo 插件的案例。我自己也是 Flomo 的重度用户，就照着思路让 AI 帮我做了个 Chrome 插件，方便我在浏览各种信息源时一键记录到 Flomo，之后回溯原文也更快。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcb7010febb37f199f36ae37eed1e5c9.png>
我给 AI 的指令是这样写的：
```
我想做一个Chrome的浏览器插件，使得能够在阅读文章时，通过打开这个插件，在右侧边栏按照制定结构输入内容，然后点击提交，一键通过flomo的API，同步到flomo内。
侧边栏里有几个输入框和一个提交按钮，下面我说说都有哪些文本输入框：
1\. 原文标题和链接（这个输入框自动带上当前网页的文章内容标题、链接）
2\. 原文摘要：这里留白给用户自己Copy进来
3\. 个人感想：这一部分让用户自己输入
flomo的API地址是：https://flomoapp.com/iwh/MzYxMjI0/********************/
在flomo的API说明里，给了个案例，你可以参考：
我想自己开发
POST https://flomoapp.com/iwh/MTY1OA/30d923d91fe52a7c9eb6b11111111/
Content-type: application/json
{
"content": "Hello, #flomo https://flomoapp.com"
}
```
# 到底花了多少钱
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_abf31c32c652eb88fe2ac281f09e71f5.png>
我只充值了 10 块钱，用一个月写了 5、6 个小工具，其中包括小程序、网页和浏览器插件，平时工作也时不时丢给它做。一个月下来账单才刚超 1 块钱，确实白菜价，想怎么造都不会心疼。