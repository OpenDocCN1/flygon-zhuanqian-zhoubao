# 航海总结网页怎么做？这份回忆感满满的教程，手把手教你复刻

> 原文参考：[飞书文档链接](https://fmu80oi2fx.feishu.cn/docx/OE0BdLyxboiLKGxa16JcfBy3n5d)

## 先看看成品效果

### 视频演示

### 原始网页地址

*   https://web.orime.top/ai-report/ai-video-touch.html（记得打开电脑音量，体验更佳）

[PRE0]

[PRE1]

[PRE2]

[PRE3]

[PRE4]

[PRE5]

[PRE6]

[PRE7]

[PRE8]

## 一些碎碎念

因为平时一直在做群聊精华整理（），航海活动收尾那天，有圈友跑来问我：这么多聊天内容，AI 能不能搞定？

[PRE9]

抱着试试看的心态，我还真去把全部聊天记录拉了出来。

[PRE10]

68 万个字符，对拥有 100 万 token 的 Gemini 2.5 pro 来说完全没压力，于是这个网页就诞生了。

说实话，这个网页做起来不算复杂，设计上也没用什么花哨的东西，但发到群里之后，意外收到了很多群友的点赞。

仔细想了想，大家喜欢大概是因为两个点：

1、文案本身很能打动人

2、背景音乐选得好，氛围感直接拉满

有领队建议我写个教程。其实基本原理和每日群聊精华总结一样，但真正决定成败的，是那些抽卡抽到崩溃才调出来的提示词。下面进入正题，一步步教你怎么做出航海 21 天回顾版网页。

## 准备工作

### 整体流程

拉取全部群聊记录 → 整理成结构化的 Markdown 文档 → 套用 HTML 模板生成网页

### 需要用的工具

#### 2.1 获取群聊记录：chatlog

地址：https://github.com/sjzar/chatlog

具体使用方法看这里：

#### 2.2 长上下文 AI 工具

*   推荐 Gemini 2.5 pro

*   Claude 系列也不错

*   DeepSeek R1 0528 可以试

*   没有梯子的话，国内用豆包 1.5 pro 或 kimi 也能凑合

## 实操步骤

### 第一步：用 chatlog 拉取指定群聊的全部记录

假设你本地已经能流畅运行 chatlog，如果还没装好，参考这个：

[PRE11]

启动 chatlog 后，浏览器打开 http://127.0.0.1:5030/

[PRE12]

接下来填时间范围和聊天对象：

时间格式有要求，直接复制这个格式：2025-06-01~2025-06-30

聊天对象就是群聊名称，必须一字不差，比如：AI 视频制作6群-6月航海

想复制得更准，按下面这种方式操作比较好

[PRE13]

填完点查询，正常情况下就能看到结果。你会发现滚动条变得非常细，说明内容量巨大（大概六七十万个字符）

[PRE14]

### 第二步：用 Gemini 生成结构化文档

打开 https://gemini.google.com/

注意左上角一定要选 2.5 pro，别选 2.5 flash

[PRE15]

把下面这段提示词，加上你的群聊记录一起发过去：

[PRE16]

提醒：聊天记录太长的话，直接粘贴可能影响速度，也可以先写进 txt 文件，再在 AI 对话框里上传发送

[PRE17]

[PRE18]

实测和直接粘贴文本效果差不多，没太大区别

稍微等一会儿，结构化文档就出来了

[PRE19]

### 第三步：制作 HTML 网页

拿到结构化文档后，就可以开始做网页了。

可以继续在当前聊天窗口操作，也可以新开一个 Tab 开个新对话。

复制下面这段提示词之前，要先处理好背景音乐和头像链接：

1.  背景音乐嵌入网页有两种办法：一种是把音乐片段上传到你部署 HTML 的地方；另一种是找网上可以直接访问的音频链接，比如从网易云拿指定音乐的链接（这个又能单独写一篇教程了）。有点编程经验的话，可以照下图自己摸索一下。

1.  给一个现成的例子：房东的猫-至此
    http://m801.music.126.net/20250628135014/bfb3915e3c9669c188664eabc993c8dd/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/28482233878/dd38/7497/fdf6/3775c330c02ef2a8a5ea40f097a15af2.mp3?vuutv=hGATS48oOO2gbLLjl86dXciJysILJ9duK/HzWYc+z0fGxG55WwMfIXayIDUxlhtMY+sKTaX1T2sr+tasWEtCZnnomUYoo9sTlolQ2+PH/0Oes9/T224Z/SdHlYydb2BR5fxYGgHqDMN0fhpTHt9CZw==

    想自己换歌的话，直接把下面这个 URL 位置替换掉就行：
    http://m801.music.126.com/20250628135014/bfb3915e3c9669c188664eabc993c8dd/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/28482233878/dd38/7497/fdf6/3775c330c02ef2a8a5ea40f097a15af2.mp3?vuutv=hGATS48oOO2gbLLjl86dXciJysILJ9duK/HzWYc+z0fGxG55WwMfIXayIDUxlhtMY+sKTaX1T2sr+tasWEtCZnnomUYoo9sTlolQ2+PH/0Oes9/T224Z/SdHlYydb2BR5fxYGgHqDMN0fhpTHt9CZw==

    [PRE20]

2.  群成员头像图片怎么获取

    1.  把头像直接传到你的 HTML 部署仓库里，让 AI 引用
    2.  上传到图床，拿到 URL 后发给 AI 用

注意：背景音乐和头像设置比较麻烦，可以跳过。背景音乐直接用我上面给的链接就行；头像不弄的话，网页头像位置会显示成花花绿绿的首字符，没有真人头像。

[PRE21]

接下来就是根据模板和数据生成 HTML 页面。复制下面这段提示词贴到对话框里（如果有群成员真实头像也可以加进去），后面再拼上一步生成的结构化文本。如果用的是文件上传，就告诉 AI 引用你上传的 txt 文件：

[PRE22]

记得一定要勾选 canvas 选项

[PRE23]

再稍微等一会儿，就能看到成品啦。

[PRE24]