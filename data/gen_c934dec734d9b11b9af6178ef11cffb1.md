# 文章总结卡 2.0 正式上线：全量适配 Deepseek V3，质感直追 Claude 3.7，再添竖版适配手机端阅读

> 来源：[https://t16jzwqrzjx.feishu.cn/docx/Q0Vnd9GYboXU5pxmdyHcHlB2noh](https://t16jzwqrzjx.feishu.cn/docx/Q0Vnd9GYboXU5pxmdyHcHlB2noh)

# 写在前面

上周我们先行放出了 AI 文章总结卡 和 AI 自我介绍总结卡之后，我和大魔、相柳、辛亥就拉起了提示词攻坚小组，核心目标就是深挖怎样才能把提示词写得更到位。

[PRE0]

[PRE1]

[PRE2]

在对文章总结卡进行迭代升级的同时，我们也同步在尝试能否用 AI 卡片方案来解决教育类落地页的问题。最初的打算是一口气把这两个成果一起发布。

不过在实测后我们发现，教育落地页想要做到真正合格，单靠一个提示词是不够的，很可能需要一套由多个提示词协同工作的工程化方案来支撑。

目前我们做出来的版本更接近于精致海报，并不能称得上是完整的落地页。

[PRE3]

[PRE4]

所以我们决定先把教育卡片的项目搁置回炉，重新梳理逻辑。今天先把刚刚打磨好的 文章总结卡 2.0 版本拿出来跟大家分享。

本次 2.0 升级主要包含三点：

1. 卡片整体视觉焕新，图标、字体、配色与版式排布都做了全面优化。
2. 新增竖版 750px 宽度不限高的卡片样式，长文章兼容性更强，手机端浏览体验更友好。
3. 全系卡片已完成 Deepseek V3 适配，生成效果已达到与 Claude 3.7 相当的水平。

# 一、AI 文章总结卡 V2.0 版本详解

## 1.1 视觉层全面升级：图标 + 字体 + 配色 + 版式

旧版 V1 视觉示例，模型为 Claude 3.7

[PRE5]

[PRE6]

新版 V2 视觉示例，模型为 Claude 3.7

[PRE7]

[PRE8]

## 1.2 横版 1080 x 800 卡片 示意

Claude 3.7 生成效果

[PRE9]

[PRE10]

[PRE11]

Deepseek V3 生成效果

[PRE12]

[PRE13]

[PRE14]

## 1.3 竖版 750 x 不限高 卡片 示意

Claude 3.7 生成效果

[PRE15]

Deepseek V3 生成效果

[PRE16]

[PRE17]

[PRE18]

# 二、提示词获取

本版本提示词同时兼容 Claude 3.7 与 Deepseek V3。

注意：Deepseek V3 需使用 0324 版本更新后的模型，官方与 API 端已支持，如需通过第三方平台调用请确认模型版本号。

提示词复制链接：

## 2.1 横版 1080 x 800 卡片 提示词

[PRE19]html

  文章概念卡片

<main class="flex-grow flex flex-col gap-6 overflow-hidden">

      </main>

[PRE20]

## 2.2 竖版 750 x 不限高 卡片 提示词

[PRE21]html

  文章概念卡片

<main class="flex-grow flex flex-col gap-6">

      </main>