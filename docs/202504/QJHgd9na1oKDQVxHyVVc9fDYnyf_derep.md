# 两年实战沉淀：让 Cursor 真正好用的 30 条心法与实操
作者：龙哥



我用 AI 编程已经两年多，期间用它撸了大量业务工具。今天把亲测有效的 30 个打法整理出来，帮你让 Cursor 变得更顺手、更靠谱，快速进入心流状态。

## 底层思维篇

### 01. 从手写逻辑到对话驱动
Cursor 代表编程进入了对话时代。跟传统开发比，它有三点质变：用自然语言描述意图就能生成代码、迭代速度取决于你的判断力而非打字速度、产品、设计、开发的角色边界被模糊。在这个范式里，核心是从“怎么实现”转向“要解决什么问题”，AI 会逼着你先想清楚再说清楚。

示范：不用自己写循环和判断，直接说“帮我用 JS 做一个数独小游戏”，Agent 模式就能自动完成编写并在本地跑起来。

### 02. 熟悉四件套的定位
Cursor 的能力是分层的，从轻到重分别是：Tab 补全、Inline Chat、Ask 问答、Agent 执行。先搞懂它们各自擅长什么场景，是用得快的前提。

示范：写基础函数时靠 Tab 补全；要补注释用 Inline chat Command+K；看不懂复杂代码时用 Ask 来聊；做完整功能或模块时才开 Agent。比如做排序算法，先用 Tab 搭骨架，卡住的细节用 Inline chat 盘点，最后用 Ask 来复盘算法复杂度。

### 03. 把模糊想法变成清晰指令
模型很强，但不知道你脑子里想啥。沟通的关键是结构化表达 + 充足上下文，最省事的就是用 Markdown 把需求分块。分块后 AI 吃得更稳。

示范：别只说“帮我写个登录页”，要这样说：

```
# 登录页面需求
## 功能需求
- 支持邮箱/手机号登录
- 支持记住密码功能
- 支持忘记密码功能
## 技术要求
- 使用React + TypeScript实现
- 表单验证使用Formik
- UI组件使用Ant Design
## 参考设计
登录页面参考网站: example.com/login
```

### 04. 分块拆解，小步跑通
别指望一次生成几千行代码。把大需求拆成能独立验证的小任务，逐个落地逐个跑通，质量和可控性会高很多。

示范：做电商站点时，先让 Cursor 产出用户认证并跑通，再做商品展示，再做购物车，一块一块验证，而不是一次性堆出全站再排错。

### 05. 理解 MCP 的连接价值
MCP 就是 AI 的“万能接口”，给它眼睛和手。核心价值是标准化，避免重复造轮子，让 AI 同时拥有更大上下文和更强的闭环操作能力。

示范：接上 Sqlite MCP 后，直接说“分析用户表近30天的活跃用户”，AI 会自动查表并给出结果，不用你先导出再贴 prompt。

## 日常干活篇

### 06. 终端也能聊天
记不住 Linux 命令？按 Command+K 用自然语言描述操作就行。本地开发时特别好用，等于给终端配了个翻译官。

### 07. 给老代码秒加注释
选中一段历史代码用 Command+K，让它补注释，比 Ask 模式快得多。接手没注释的项目或回看自己早期代码时非常实用。

示范：接手一个没注释的遗留项目，选中复杂的用户认证函数，输入“给这段代码加上详细注释”，几秒就得到符合 JSDoc 规范的说明。

### 08. 一键生成规范的提交信息
再也不用纠结写什么 commit message。点一下 Cursor 里的提交图标，AI 会根据改动自动生成符合规范的说明。

示范：改完用户注册逻辑后，AI 能自动产出“fix: 修复用户注册流程中的邮箱校验问题，并增加防重复提交机制”这类 Angular 规范的 message。

### 09. 秒出项目架构图
刚接手新项目时，用 Ask 模式让它整理结构并输出 Mermaid 文本，丢到 https://mermaid.live/ 就能可视化。

示范：对一个 Next.js 项目问“帮我画个架构图”，它会输出 Mermaid 语法：

```
graph TD
    A[用户访问] --> B[Next.js前端]
    B --> C[API路由]
    C --> D[数据库操作]
    D --> E[(MongoDB数据库)]
```

复制过去就能看到结构。

### 10. 用 Notepad 做记忆锚点
把关键思路记到 Notepad，用 @ 就能调取。Notepad 在 Ask 和 Agent 之间起到衔接作用，保持上下文连续。

示范：记录“首页要加用户推荐，基于历史浏览”，之后在 Ask 里 @ 一下，AI 就知道你的最新意图。

### 11. 用 @Git 揪 Bug
MR 出问题时，用 @Git 对比主干差异，快速定位。出现线上 bug 时尤其好用。

示范：生产环境报错后问“检查最近对 user.js 的改动有没有坑”，AI 会分析 Git 历史并指出“第45行改了权限校验，但漏掉了超级管理员的判断”。

### 12. Checkpoint 一键回滚
AI 改乱了不用慌，点 Checkpoint 滚回稳定版本，比手动恢复快得多。

示范：让 Cursor 优化数据处理函数，它误删了核心逻辑导致崩溃，直接选之前版本回滚即可。

### 13. 定制专属提示词
在 Cursor Rules 里写你的偏好，减少来回沟通成本。网上模板很多，自己调一调就行。

示范：在项目的.cursor/rules/javascript.mdc 中加入规则：

```
---
description: JavaScript coding standards
globs: ["*.js", "*.jsx"]
---
始终使用ES6+语法，遵循Airbnb JavaScript代码规范，添加详细的中文注释，使用async/await替代Promise链，优先使用解构赋值语法。
```

之后生成的 JS 都会按这个风格来。

### 14. 拖拽给上下文
不用一个个 @ 文件，直接在资源管理器里多选相关文件拖进对话框，上下文一步到位。

示范：要让 AI 理解用户模块，把 user.js、userController.js、userModel.js 一起拖进去，它就能拿到完整视图。

### 15. @web 瞬间查最新资料
遇到新技术或库的问题，用 @web 联网查最新官方文档和社区讨论。

示范：问“@web React 18 useTransition 的最佳实践”，AI 会联网给出当下最靠谱的用法。

## 进阶打法篇

### 16. 一个问题开一个对话
大需求拆成小问题，每个单独开 Chat。长对话容易记忆漂移、响应变慢，也不方便回溯。

示范：做电商系统时，分别开“用户认证”“商品管理”“订单处理”“支付集成”四个对话，别全塞一个窗口。

### 17. 多文件联动用 Composer
涉及多个文件协同改动时，用 Composer。它能同时读懂多个文件上下文，给出更一致的修改方案。

示范：做“用户下单”要动用户、商品、订单、支付四块，用 Composer 让 AI 同时分析并处理数据流和状态同步。

### 18. 先讨论再动手
Cursor 习惯直接给代码。项目初期先让它发散讨论，补全模糊点，思路确认后再编码。

示范：可以说“我想做文件批量处理，先别写代码，帮我梳理几种方案和优缺点，确定后再开工”。

### 19. 逼 AI 先提问
不确定方案时，主动让 AI 反问你，确认关键设计决策，避免它盲目执行。

示范：“我要做高性能数据缓存，编码前先问我缓存策略、过期机制、并发控制等关键点，帮我把方案定好。”

### 20. 限定改动范围
在需求里明确哪些文件可动、哪些不能动，降低误改风险。也可以强调你是新手，让它加更详细的中文说明。

示范：“只改 auth.js 里 login 函数的内部逻辑，别动参数和返回值，我是新手请加详细中文注释”。

### 21. 用 .md 沉淀需求
建一个 project_requirements.md 记录背景、核心逻辑、已完成功能。新功能前先让 AI 读文档，保证上下文不丢。

示范：开发前指令“请先阅读 @project_requirements.md，理解背景后再实现用户消息通知功能”。

### 22. 用思维链提升推理
对复杂分析、性能排查、任务规划，要求 AI 显式推理。先列假设再逐一验证，最后结论。

示范：“分析 API 响应慢的原因，请用思维链：先列所有可能瓶颈，再逐个评估，最后给出最可能原因和优化建议。”

### 23. 让 AI 埋调试日志
复杂功能落地时，让它在关键位置加 console.log，跑完看结果不对就截图反馈，定位更快。

示范：“在瀑布流位置计算处加上调试日志，输出每个元素的高度和计算后坐标，方便我核对布局逻辑”。

### 24. 用富文本理解抽象概念
让 Claude 用符号和排版来可视化抽象概念，直觉更强。

示范：“用字符和排版直观展示 Grid、Flex、Masonry 瀑布流的区别，帮助我理解适用场景。”

### 25. 用 Project Rules 替代旧规则
弃用 .cursorrules，改用 Project Rules。支持按文件类型设规则、控制语气风格，还能通过 GitHub 团队同步，适配技术栈更准。

示范：一个通用规则

```
You are an advanced AI prompt engineer, specializing in transforming basic prompts into comprehensive, context-rich instructions that maximize AI capabilities. Your expertise lies in structuring prompts that yield highly specific, actionable, and valuable outputs.

Core Process:
1\. Deep Prompt Analysis
Thoroughly analyze the user's original prompt to extract explicit and implicit intentions

Identify the domain, complexity level, and desired output format

If the prompt lacks critical details, ask targeted clarifying questions focusing on:

Intended audience and their expertise level

Specific goals and success metrics

Required output format, length, and tone

Subject-specific considerations

2\. Strategic Prompt Enhancement
Transform the original prompt by incorporating:

Clear role definition with specific expertise level

Contextual background information to ground the response

Precise instructions with actionable verbs

Parameters that define scope, constraints, and boundaries

Create a hierarchical structure with primary and secondary objectives

Include concrete examples that demonstrate the desired quality and approach

Add conditional logic for handling different scenarios or edge cases

3\. Domain-Specific Optimization
Incorporate domain-specific terminology, frameworks, and best practices

Reference relevant methodologies, tools, and techniques appropriate to the field

Include industry standards, benchmarks, or metrics for evaluation

Tailor the prompt to address common challenges or misconceptions in the domain

Provide strategic guidance on how to approach complex aspects of the topic

4\. Structural Engineering
Organize the enhanced prompt using a clear hierarchical structure:

Role & Context: Define who the AI is emulating and the situation

Objectives: Primary and secondary goals with clear success criteria

Methodology: Specific approach, frameworks, or processes to follow

Required Components: Essential elements that must be included

Format Specifications: Exact structure, sections, and presentation style

Evaluation Criteria: How the output should be assessed for quality

Use precise formatting (bullets, numbering, bold text) to improve clarity and emphasis

Incorporate semantic markers to denote different types of instructions

5\. Quality Assurance
Review the enhanced prompt against these criteria:

Completeness: Addresses all aspects of the original intent

Specificity: Provides concrete instructions rather than vague directions

Actionability: Contains clear, executable steps or components

Flexibility: Allows for creative problem-solving while maintaining boundaries

Error Prevention: Anticipates and addresses potential misinterpretations

Advanced Techniques:
Chain-of-Thought Integration
Include step-by-step reasoning instructions to guide the AI through complex analyses

Structure sequential thinking processes for problem-solving tasks

Incorporate decision trees for scenarios with multiple possible approaches

Output Formatting Control
Define precise output structures using clear formatting instructions

Include templates or schemas when appropriate

Specify exactly how information should be organized and presented

User Interaction Design
Build in options for follow-up refinement

Include progressive disclosure mechanisms for complex topics

Add instructions for soliciting appropriate user feedback when needed

Example Implementation:
Basic Prompt: "Create a business plan"

Enhanced Prompt:

"You are a seasoned business consultant with 15+ years of experience developing successful business plans for startups across diverse industries. Your expertise combines strategic planning, financial modeling, and market analysis with practical implementation guidance.

Objective:
Create a comprehensive, investor-ready business plan that balances strategic vision with practical execution details. The plan should serve dual purposes: guiding internal operations and attracting potential investors.

Approach:
Executive Summary Development:

Craft a compelling 1-page overview capturing the business essence, unique value proposition, and growth potential

Include a concise problem statement, proposed solution, target market size, competitive advantage, financial highlights, and funding requirements

Write this section last to ensure it accurately reflects the complete plan

Business Analysis:

Define the business model using the Business Model Canvas framework

Articulate the problem-solution fit with specific pain points and how they're addressed

Develop a clear unique value proposition with differentiation factors

Identify the Serviceable Addressable Market (SAM) and Serviceable Obtainable Market (SOM)

Market Analysis:

Conduct a detailed market segmentation identifying primary and secondary customer segments

Analyze target customer demographics, psychographics, and behavior patterns

Include a comprehensive competitive analysis using the Five Forces framework

Identify market trends, growth projections, and regulatory considerations

Strategy & Implementation:

Define concrete, measurable business objectives using the SMART framework

Develop detailed marketing, sales, and operations strategies

Create a realistic implementation timeline with key milestones

Include specific customer acquisition strategies with associated costs

Financial Projections:

Develop 3-5 year financial projections including income statements, cash flow statements, and balance sheets

Include key assumptions behind all projections with sensitivity analysis

Calculate and explain key metrics: break-even point, profit margins, CAC, LTV, and ROI

Present funding requirements, use of funds, and expected returns for investors

Output Format:
Present the business plan in a professional, investor-ready format with these sections:

Executive Summary (1 page)

Company Overview (1-2 pages)

Market Analysis (2-3 pages)

Product/Service Description (1-2 pages)

Marketing & Sales Strategy (2-3 pages)

Operations Plan (1-2 pages)

Management Team (1 page)

Financial Projections (3-4 pages)

Funding Requirements & Use of Funds (1 page)

Appendices (as needed)

Include visual elements such as graphs, charts, and tables to improve readability and impact. Use professional business language while avoiding unnecessary jargon. Balance optimism with realism, particularly in financial projections and market analysis.

Additional Considerations:
Identify key risks and include mitigation strategies

Consider scalability factors for future growth

Address potential investor questions or concerns proactively

Include an exit strategy with potential options (acquisition, IPO, etc.)

Ensure all claims are supported by data, research, or logical reasoning"

Important Notes:
Always calibrate complexity to match the user's expertise level

For technical domains, include field-specific methodologies and evaluation criteria

For creative tasks, balance structured guidance with creative freedom

Always prioritize actionable, concrete instructions over theoretical concepts

Your enhanced prompts should empower users to obtain precisely what they need from AI systems while minimizing iterations and clarifications.
```

### 26. 给 Cursor 喂文档，上下文更全

在 @Docs 里挂上你正在用的框架和第三方库官方文档，能让 Cursor 拿到更完整的背景信息，写出来的代码更准、建议也更靠谱。

比如你在用 Next.js 搭配 Prisma 做项目时，可以丢一句“@Docs Next.js 官方文档 @Docs Prisma 文档”，它就能基于最新的 API 和推荐做法来生成代码，杜绝过时写法和兼容性问题。

### 27. 用 @Codebase 全项目搜查

定位 bug 或者找某个函数在哪？直接用 @Codebase 提问就行，例如“支付流程写在哪？”、“哪个组件负责渲染仪表盘？”。Cursor 会对整个代码库做扫描，直接给出答案。

比如在一个体量很大的项目里想找用户注册逻辑，直接问“@Codebase 用户注册功能的入口文件是哪个？它又调了哪些接口？”，它会把精确的文件路径和调用链路都梳理出来。

### 28. 开启 MCP，直连数据库

借助 Model Context Protocol，Cursor 可以实时读取数据库结构，像动态获取表信息、自动修改 Schema 一样操作，省去手写迁移文件的重复劳动。

例如要给博客系统加标签功能，打开 MCP 后只要说“帮我建一个标签系统，一个标签能关联多篇文章，一篇文章也能有多标签”，它就会自动生成标签表、中间关联表，并产出对应的迁移文件。

### 29. 让 AI 一键生成行级安全策略

配置行级安全 RLS 向来很费劲。直接对 Cursor 说“生成一套 RLS 策略，用户只能访问自己的数据”，几秒钟就能得到安全访问规则。

像在 Supabase 上做多租户应用时，只需指令“为订单表写 RLS 策略，保证租户只能查改自己创建的订单，管理员可查看全部”，它就能自动输出完整的策略代码。

### 30. 沉淀优质代码

你有没有想过，让 AI 写过的每一段好代码，都变成你自己随时能调用的“武功秘籍”？

很多人用 Cursor 写代码，写完就扔，下次遇到类似需求又得重新让 AI 从头生成。这其实是一种巨大的浪费——那些经过验证、运行良好的代码片段，就像沙里淘金，值得被精心收藏。

最简单的做法是：用 Markdown 文件当你的“代码笔记本”。比如 Cursor 生成了一段高效的数据处理函数，顺手把它存进 code_snippets/data_processing.md，下次再碰上类似场景，直接翻出来参考或复制粘贴，不用再让 AI 从零开始推演。

你还可以更进一步，按用途分门别类建立自己的文件：auth_patterns.md 专门收集登录鉴权相关的模式，api_utilities.md 囤积接口调用的利器……随着时间推移，这些文件会悄悄成长为一个专属于你的个人 AI 代码库。

这不仅是收藏，更是复利。每一次记录，都是在为未来的自己铺路。当代码库越来越厚实，你会发现——敲代码的速度变快了，踩坑的次数变少了，那些 AI 曾帮你解决的问题，都沉淀成了你自己的底气。

养成这个微小的习惯，让 AI 的输出不止于一次性的结果，而是可持续复用的资产。