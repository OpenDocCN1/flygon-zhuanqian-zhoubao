[PRE0]

最近在折腾 Cursor，发现一个特别实用的技巧：让 AI 写代码时，如果能附上现成的示例，效果会好很多。比如我写一个调用大模型的 demo，代码就是直接从 API 文档里复制过来的。

提示词 2

[PRE1]

import OpenAI from "openai";

const openai = new OpenAI({

        baseURL: 'https://api.deepseek.com',

        apiKey: ''

});

async function main() {

  const completion = await openai.chat.completions.create({

    messages: [{ role: "system", content: "You are a helpful assistant." }],

    model: "deepseek-chat",

  });

  console.log(completion.choices[0].message.content);

}

main();

[PRE2]

就这么简单的两条提示词，一个能直接对话的聊天界面就搭出来了。

[PRE3]

整个过程只花了不到十分钟，界面还很粗糙，功能也谈不上完善。但这都不是事儿——你想让它怎么改，直接跟 Cursor 提，它就能慢慢帮你优化。后面有新想法，也可以很方便地往站点里加。

代码我已经传 github 了：https://github.com/leyonglin/cursor-demo.git

clone 下来之后，只需要把 config/index.js 里的 apiKey 改掉，就能直接用。

说完这些，再分享几个 Cursor 的提速技巧。

[PRE4]

**Cursor 建议**

Tab：接受整段 AI 代码建议

Esc：拒绝当前的建议

Ctrl + →：只接受建议中的某一部分

[PRE5]

**Chat 聊天**

Ctrl + K：调出内联编辑工具

[PRE6]

Ctrl + L：打开 AI 聊天窗口，选中的代码会自动发送过去

[PRE7]

Ctrl + I：打开 Composer 工具窗口

Ctrl + Shift + I：全屏模式打开 Composer

[PRE8]

**@ 符号命令**

Files：把某个文件加进来作引用

Folders：把某个目录加进来作引用

Codebase：引用整个代码库

[PRE9]

**通用快捷键**

Ctrl + Shift + P：呼出命令面板，所有命令都在这

Ctrl + , ：打开编辑器设置

Ctrl + B：显示/隐藏侧边栏

Ctrl + `：显示/隐藏集成终端

Ctrl + N：新建文件

Ctrl + S：保存文件

[PRE10]

这里专门说说 .cursorrules 规则文件。很多人搞混它和 README.md，但在 Cursor 眼里这俩完全不是一个级别：README 和普通文件没区别，.cursorrules 却是相当于规则/提示词的存在。

[PRE11]

.cursorrules 同样是 markdown 格式写的。更多现成的规则可以从 GitHub 上扒：

https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules

再聊一个有意思的案例。亦仁在 Cursor、v0、Claude 上花了 217 个小时，现在 4~7 天就能独立完成一个完整的 Web 应用，前端、后端、登录页、着陆页全都不在话下。

这其实说明了两件事：一是 AI 编程的入门成本极低，学习周期被压缩得很短；二是整个开发周期也大幅缩短。对普通人来说，花一点时间去折腾，绝对不亏。

而且资料也特别好找：菜鸟教程、w3schools、B站、X、YouTube，应有尽有。更奢侈的是，你可以随时随地直接问 AI。

**普通人学编程，到底图什么？**

最本质的作用，就是 AI 编程能让你把脑子里那些创意，真正变成产品。在生财这边，学以致用是基本操作——不管学编程还是学 AI 编程，核心就两个字：用起来。学不是为了当摆设，是为了解决问题，是为了赚钱。

我整理了一下，编程能带来的价值至少有下面这几个方向：

**自用**

很多需求网上早就有人做出工具了，但每个人的需求都不一样，免费或付费的产品未必能完全满足自己。只要你有一点编程基础，借助 AI 就能自己二次开发，甚至把多个工具揉在一起用。

**做独立站**

9 月份的航海《出海工具站》，专门带大家做独立站开发，做成了就是一个长期副业。

**卖网站**

在 acquire.com 这类平台上，如果能做出好看又实用的网站，绝对是一门长期的“睡后收入”生意。

**知识付费**

抖音、小红书上已经有不少程序员博主了，完全可以把它当成一个副业来经营。

**接兼职**

可以试试这些平台：

- 程序员客栈：面向中高端程序员、产品经理、设计师，提供自由工作、远程和兼职机会
- 码市：Coding 旗下的外包平台，连接需求方和开发者
- 开源众包：专业的软件众包平台，号称有 350 万+开发者，支持网站、App、微信/小程序、企业应用等
- 猪八戒网：面向中小微企业的人才共享平台，服务类型很丰富
- 当然还有英选、快码众包、码易众包、开发邦、人人开发、Sxsoft、猿急送、实现网、智城外包网等

说到底，AI 编程已经把普通人的门槛降到了历史最低。也许你离第一个能上线、能赚钱的产品，就差一次动手尝试。