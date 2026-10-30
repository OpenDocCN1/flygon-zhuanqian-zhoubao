# 【干货】用 ChatGPT 搭上 Zapier，这套自动化组合拳有多香？

> 来源：[https://zzi7a49xoa.feishu.cn/docx/H4L5dC5VFozWrlx6sI7cmnRpn8e](https://zzi7a49xoa.feishu.cn/docx/H4L5dC5VFozWrlx6sI7cmnRpn8e)

## 一、为什么要把两者绑在一起

在信息爆炸的节奏里，我们被邮件淹没、被待办压垮、被重复操作拖进消耗战。创造力被琐事一点点磨掉，效率也被一点点吃掉。

如果你也在被这些问题困住，GPTs 加上 Zapier 就能让局面逆转。

GPTs 的能力大家基本都摸熟了，没接触过的小伙伴可以先回顾下基础配置。那它要真正跑起来，还是得有人把它接到你每天都在用的工具里，这就是 Zapier 的角色。Zapier 是一款零代码的在线连接器，能把上千款应用串成一条线。把 GPT 接进 Zapier，就能把智能从聊天窗口解放出来，变成可执行的自动化。

下面这篇就是一份通俗好上手的实操笔记，带你把 GPTs 和 Zapier 串起来用。

## 二、Zapier 到底能干嘛

### 一）核心玩法

Zapier 靠的是 Zap，也就是自动化流程。它能把两个及以上的应用连起来，让数据自动流动、任务自动触发。

*   搭建流程：你在 A 应用里完成一个动作，Zapier 就自动在 B 应用里执行对应的步骤。
*   生态很广：目前接入的应用超过 3000 个，涵盖 Gmail、微软办公套件、Slack、Trello、Google Sheets 等主流工具。
*   真正无代码：不用写一行代码，拖拽配置就能完成。

### 二）用它有什么好处

*   省时间：把重复劳动丢给机器，人去做思考。
*   降失误：流程固化后，数据更准确也更一致。
*   高度可定制：按自己的工作习惯搭流程，个性化强。
*   协作更顺畅：信息和提醒自动同步，团队配合更顺。

对于想把 GPT 落地到日常工作的用户来说，Zapier 就是那把钥匙，让智能真正进入工作流。

## 三、从零开始的配置步骤

### 一）先建账号

支持用 Google 或其他邮箱免费开通。

官网： https://zapier.com/

[PRE0]

填好基本信息，点击 Continue。

[PRE1]

进入应用选择页。这里可选的应用非常多，比如 Gmail、Nition、Google Forms、Discord、Stripe、ChatGPT、YouTube、Microsoft 系列、EverNote 等。为了演示我选了 Gmail 和 ChatGPT。

[PRE2]

国内可用的应用相对有限，我在国内办公软件里看到过 Tencent Docs。

[PRE3]

### 二）给 GPTs 赋能

1、打开 Explore > Create a GPT，进入编辑页。

[PRE4]

2、在编辑页点 Create new action。

[PRE5]

3、填入 url 并点 Import，再补上 Privacy policy。

1.  url : https://actions.zapier.com/gpt/api/v1/dynamic/openapi.json?tools=meta

1.  Privacy policy: https://zapier.com/legal/data-privacy

[PRE6]

[PRE7]

4、返回上一步，填 Instruction。

[PRE8]

5、名字、描述、Logo 等随你喜好设置。

[PRE9]

6、输入 配置zapier，开始配置。点 Sign in with actions.zapier.com 登录

非开发人员可以忽略：配置期间会进入调试模式，能看到接口请求和返回日志。

[PRE10]

7、点 Allow。

[PRE11]

页面会自动跳回，会出现成功提示。"You have successfully signed in via OAuth"

[PRE12]

8、发送 请列出我可以配置的 Zapier AI Actions，并使用中文和我对话 , 点 配置 Zapier 的链接.

[PRE13]

9、在链接里点右下角 Add a new action。这里演示用 查看邮件。

没登录的话会先要求登录。

[PRE14]

10、搜索 查看邮件 的功能。输入 Gmail，找到 Gmail：Find Email。

[PRE15]

11、点 Connect a new Gmail account，绑定邮箱。

[PRE16]

点 Yes，Continue to Gmail。

[PRE17]

选定邮箱账号。

[PRE18]

点允许，完成授权。

[PRE19]

12、点 Enable action。

[PRE20]

启动完成。想加更多动作就继续点 Add a new action。

[PRE21]

13、回到 GPTs，回复完成配置。

[PRE22]

### 三）小试牛刀

1、让助手列出过去一周关于 AI 的邮件。执行时会弹出是否信任站点确认，点 Allow 授权即可。

[PRE23]

2、结果基本符合预期。

[PRE24]

3、指定时间段，对邮件内容做个简单汇总。

[PRE25]

## 四、案例一：邮件摘要与关键信息批量提取

### 一）场景

作为项目经理，每天收到的工作邮件里全是项目进展、会议纪要、客户反馈。人工精读费时，还容易遗漏重点。

目标是搭一条自动化流，从长邮件里自动抽出要点和摘要，让你快速抓住核心。

### 二）实操要点

注意一个坑：邮件正文如果是图片，或者是特定排版样式，GPTs 通过 Zapier 可能拿不到正文内容。

比如把 ChatGPT 里的 Markdown 内容原样复制进邮件正文，我这边测试时就读取不到。

1、输入相关信息后，GPT 会提示先登录 Zapier。

[PRE26]

2、登录成功。

[PRE27]

3、先查看账号下已有的 Zapier AI Actions，判断是否还需要新增动作。

[PRE28]

4、用提示词让它把项目相关邮件汇总，输出 “当前状态”、“主要问题”、“下一步计划”。

[PRE29]

5、不同项目背景差异大，这里不再展开。基于第 2 步的信息，就能继续规划后续动作。

## 五、案例二：智能分类邮件并自动回复

### 一）场景

做客服或独立开发，每天要处理咨询、投诉、感谢等各种客户邮件。手工分类又写回复，慢而且容易出错。

思路是让工具自动识别邮件类型，生成合适的回复草稿，再发给发件人。

### 二）实操

1、先获取可用动作列表。

[PRE30]

2、点 Sign in with actions.zapier.com，在新窗口点 Allow 完成初始化。

[PRE31]

3、再次获取可用动作。

如果没有 Reply to Email，可参考 三、操作流程 / GPTs 章节，手动添加 Gmail：Reply to Email。

[PRE32]

4、获取昨天邮件的简要汇总。

[PRE33]

5、自动分类并生成对应的回复建议。

[PRE34]

6、把生成内容自动回复给发件人。

[PRE35]

7、去邮箱核对，回复已正确发出。

[PRE36]

[PRE37]

## 六、收尾

本文结合了配置方法和两个实操案例，演示了如何借助 Zapier 放大 GPTs 的工作能力，相信能给你更多灵感去设计自己的自动化流。【有条件的小伙伴，建议用 API 拿更精确的数据，再配合 GPT 处理，稳定性会更高！】

动手试试，把这套组合嵌入到你的日常里，你会感受到效率的质变。技术的价值永远在于怎么用好它来改善工作和生活。期待你的实践反馈，下期再见！