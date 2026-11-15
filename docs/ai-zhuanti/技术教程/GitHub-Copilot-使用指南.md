# GitHub Copilot 使用指南
# Copilot 究竟是什么
Copilot 是 GitHub 面向程序员打造的 AI 编程助手，在编码过程中实时给出代码补全建议。
*   官网入口：https://github.com/features/copilot
*   官方文档：https://docs.github.com/copilot
涉及的核心概念有：
*   Transformer 架构
*   大规模预训练模型
*   代码片段
*   代码推荐
*   Prompt Engineering
# Copilot 能带来哪些价值
这款工具的实用性很强，可以明显提升开发效率、降低技术门槛与开发成本。
*   ⚡ 效率提升：能快速生成各类业务代码，覆盖增删改查、单元测试等常见场景。
*   🔑 门槛降低：面对新语言、新框架、新库时，可迅速帮助理解并完成原型代码。
*   💰 成本压缩：在 SQL、正则表达式、Cron 等机械重复类任务上表现突出，大幅减少编写成本。
# Copilot 的工作原理
底层是基于 GPT-3 的大模型，通过海量代码片段训练，学会语法、语义、结构等规律，再结合当前上下文生成片段并给出推荐。
*   代码片段
*   训练语料来自 GitHub 开源代码、Stack Overflow 代码片段等，包含丰富的语法和结构信息。
*   模型基于这些语料学习代码规律。
*   Prompt Engineering：
*   Prompt Engineering 是通过技巧将自然语言转化为模型可理解的输入，提升输出准确度。
*   例如把循环意图转化为 for i in range(10):。
# 优势与不足
🎉 优势：
*   补全建议准确度较高，能基于已写代码给出合理的续写。
*   语言覆盖广，涵盖 Python、Java、JavaScript 等主流语言。
*   编辑器适配多，如 VS Code 等常用 IDE。
*   系统兼容性好，支持 Windows、MacOS、Linux。
⚠️ 不足：
*   智能度有限，复杂逻辑场景下理解不足，推荐质量参差。
*   覆盖不全，部分冷门语言或特殊场景推荐不充分。
*   安全风险存在，偶尔会生成存在安全隐患的代码。
# 如何安装 Copilot
整体流程包含 4 步：
1.  申请账号
2.  申请 Copilot Chat 可选
3.  安装插件并配置语言
4.  登录授权
5.  开始使用
官方入门链接：https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment?tool=jetbrains
## 申请账号
前往 https://github.com/features/copilot 申请并开通，月费 10 美元，首月免费，支持国内信用卡。学生可申请免费额度。此处也存在转售使用名额的需求。
## 申请 Copilot Chat 选配
个人版与企业版流程类似，企业版优势是无需排队等待。个人版通常等待约半个月以上。
开通后可申请 Chat 功能，地址 https://github.com/features/preview ，通过页面入口提交申请。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_30b9ef84bb075668a03cf395fefc2781.png>
一般等待约一个月，审核通过后会收到标题为 You’re now in the GitHub Copilot chat private beta! 的邮件，内含安装指引：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_91d17cbf5c569b8071691ac7a3a2b2ac.png>
## 安装
### Visual Studio
1、确认使用 Visual Studio 2022 17.5.1 或更高版本。
2、搜索安装扩展 GitHub Copilot。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_67d49d449be7a090ebdf0053ebe13a03.png>
点击 Trust Workspace & Install。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b7e9c51e6cee66fe2dde66e89d41a62d.png>
3、搜索安装扩展 GitHub Copilot Chat。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e93576a47c624a8f7ee885e92f01b786.png>
4、重启软件并用 GitHub 账号登录授权。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e87e471776ede6665315963d515a1e9b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6dcfbd13ca460e9655abf88bc9d6984b.png>
输入账号/密码登录。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aef121b69c6b76acbea7231cad00319a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bbad315446a2a10c2601a58f750ec553.png>
点击 Open。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_921b0e3ee994a0f8e0dad44c3f90d3fc.png>
使用本地服务器验证，点击 Yes。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7aedda057e094c673199e28ec7a91e58.png>
浏览器打开显示已登录。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6673f427860144b554c1706ffb3f60d3.png>
显示设备授权码，点击 Copy & Continue to GitHub
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ab535c8c3ca742e77c8736d691630a47.png>
在浏览器中输入设备授权码并点击 Continue。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d93dfa2d6da591e5c527923f45bffaac.png>
选择 Authorize Visual-Studio-Code 授权设备。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5edb5bd38b7f94ec291455c264ca66b9.png>
授权成功。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_499ace52756f4777427273512a1f5792.png>
4、校验功能。
GitHub Copilot 聊天窗口会出现在视图菜单中，未申请 Chat 功能则不会显示。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_729579510d23ed2152743ac3dc467af6.png>
验证打开代码文件时，右键菜单顶部是否出现 Copilot 按钮。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ca44561748dae1b12910d62d16397119.png>
### Visual Studio Code - Insiders
1、下载安装 Visual Studio Code - Insiders，使用最新版。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1c23e4c5cf705e54ae7f7ba2e6d4e892.png>
2、在 VS Code Insiders 中安装 GitHub Copilot 和 GitHub Copilot Chat 插件，步骤与 Visual Studio 类似。
3、安装成功后，首页左侧会出现聊天菜单。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4a5ceba15749182356217d121f0f7a84.png>
### JetBrains IDEs
支持的 IDE 包括：
*   IntelliJ IDEA Ultimate/Community/Educational
*   Android Studio
*   AppCode
*   CLion
*   Code With Me Guest
*   DataGrip
*   DataSpell
*   GoLand
*   JetBrains Client
*   MPS
*   PhpStorm
*   PyCharm Professional/Community/Educational
*   Rider
*   RubyMine
*   WebStorm
以 IntelliJ IDEA 为例：
1、打开已有项目。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_537100fa7b1ef49d47c572f21bd9e624.png>
2、在插件市场搜索 Copilot 并安装。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8f060304eeb6a42e55f464860290ef33.png>
3、安装完成后点击 Restrat IDE。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a99d131cd33092d2cc6953ccade7e5be.png>
4、重启后点击 GitHub Copilot，选择 Login to GitHub。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0ecd42102e6dfa5d62ba358a2378a103.png>
获取设备授权码。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_903207a5a54ccb050865023e3ab3c2e8.png>
在浏览器完成验证。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8f4b21c04e86a6346b97cb91dad8e2c5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_daafa7b032368a94266eb61aab91fd81.png>
设备授权成功。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0b6f42633b8523a027be60cc01db81a9.png>
# 初次体验
## 基于注释自动生成
每写一行注释，Copilot 就会在光标位置给出建议，如下图：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_79f257a6f2bd4ff8cd36a82a28ccf577.png>
按 Tab 即可自动补全。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_254540c82f3017ed22e9ef81fbea9899.png>
## 基于已有代码自动补全
根据上下文自动续写代码。此处演示计算两个日期的间隔。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bbe5b7bc94ce3310f51f2b78751d2369.png>
计算结果为相差 1 天。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_60ef910493eac048d28c0f246371986e.png>
# Copilot Chat 初体验
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9ab981717f64b029ab090c024ffada00.png>
发送后获得 Copilot 的回复。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_04cb9f508817d10e23f95aa5571e9c78.png>
可选择 Copy 代码片段。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0eeb64cb6dee5c7eff5c06c117102e5c.png>
将代码插入到光标位置。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_455903908d0e4f18f1db724c2a903de6.png>
更多操作：插入到新文件或在控制台运行。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f58b3bd2bb96cce8cf6a2c8ca25b942d.png>
处理后的代码。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_eaa6a873b6cfc5575217e608be3a6deb.png>
运行成功。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8b37f3206d86cc0c08898f2c89e51d7d.png>
# 基础功能
## SQL 编写
在注释中写清需求，输入 CREATE 关键字，Copilot 会提示完整的建表语句，十分便捷。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_02146707a41e53948378ba816e8af576.png>
## 正则编写
新建 regex.js 文件，用于正则校验工具，测试如下场景：
*   是否为数字
*   是否为邮箱地址
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3f1527337b007174dac68fcadc45fa07.png>
## Cron 编写
Cron 脚本编写较为繁琐，可借助 Copilot 完成。先写说明文档，模型即可给出脚本建议。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a5a928f46c2a7df80c6c00c10d0f7082.png>
# 进阶功能
下面介绍开发中的常用场景：代码解释、单元测试、Bug 修复，结合实际更易体现价值。
## Copilot Chat 指令概览
在实际使用前，先了解常用指令，输入或选择即可：
1.  /tests : 为选中代码生成单元测试
2.  /fix : 针对选中代码提出修复建议
3.  /explain : 解释选中代码的工作原理
4.  /vscode : 询问 VS Code 相关问题
5.  /help : 获取通用帮助
## 代码解释
Chat 功能更强，这里以 VS Code 为例。
Copilot 学习能力强，可结合上下文解释代码含义，对源码或注释少的业务代码尤为实用。
基本操作步骤：
1.  选中代码
2.  打开 chat 菜单
3.  输入关键词及提示词
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c9d1d4d3342a4b53b4e26826e66ef453.png>
查看 Copilot 的回答。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_96f8a66754823b68e0f027e8534e8af8.png>
再以 Java 源码为例，让其解释 ArrayList.clone() 方法：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f3d880a6958c188db156248d7819a52f.png>
## 单元测试生成
以 VS Code 为例，借助 Copilot 快速生成测试用例。
### JS 代码
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bc3a6e51c1970ca32fe55d63e48bc772.png>
### Java 代码
选中代码，输入指令并说明用例目的，即可生成测试代码。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5880b0a3598e7bfa5f452d58971b3168.png>
## Bug 修复
上一步生成的测试用例运行时抛出 Exception java.util.ConcurrentModificationException，需要修复。
选中问题代码，输入指令及提示词调整代码。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e32dcbc6cc1b5d426ee16cc4e55d193b.png>
修改后代码运行正常，无错误。
# 常见问题
## Copilot Chat 无法正常工作
*   安装或更新最新版 Visual Studio Code，命令面板执行 检查更新
*   安装或更新最新 GitHub Copilot
*   GitHub 账号需同时满足：
*   订阅已激活
*   已接受 Copilot Chat 内测邀请
# 总结
本文介绍了 Copilot 的概念、价值、原理、优缺点、申请安装流程及基础使用。
最大亮点总结：
*   与编辑器深度融合，使用体验流畅，无需频繁切换。
*   /explain 功能强大，阅读源码时大幅降低理解成本。
*   本质是基于 GPT-3 的 AI 聊天工具。
*   可检查复杂业务逻辑中的 Bug 并给出改进建议，如询问“如何改进”、“是否需要重构”。
*   日常 CRUD 与通用代码可交给 AI，减少复制粘贴错误。
*   可学习 GitHub 上优秀开源实践，提供最佳实践风格代码，只需优化 Prompt。
Copilot 仍处于测试阶段，生产环境使用需谨慎，建议代码严格测试后再上线，避免安全风险。它能提升效率、减少机械工作，让开发者专注业务逻辑。
后续会持续分享更多使用技巧，欢迎交流探讨。