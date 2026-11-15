# 第11章：在 Cursor 中接入 MCP，让 AI 拥有“万能插头”
如果 AI 只能依赖训练数据回答问题，它更像一个知识丰富、却无法接触现实世界的“理论专家”。
但如果它能够读取项目文件、查询数据库、访问网页、操作 GitHub，甚至直接辅助编写前端代码，AI 的能力就会从“会回答”升级为“能办事”。
Cursor 中的 MCP 服务，正是实现这一变化的关键。
## 一、MCP 到底是什么？为什么值得了解？
MCP，全称是 **Model Context Protocol**，由 Anthropic 于 2024 年 11 月推出，是一种开放标准协议。
可以把它理解成 AI 的“万能插头”：
> AI 是设备，外部工具和数据源是电器，MCP 就是连接两者的通用接口。
通过 MCP，AI 不再只是对着已有知识进行推理，还可以与外部环境建立连接，读取信息并执行操作。
### MCP 出现之前，AI有哪些限制？
过去的 AI 更像是被困在信息孤岛中的“高智商助手”：
- **信息有边界**：无法主动获取训练数据之外的最新内容；
- **操作能力有限**：不能直接访问数据库、文件夹或第三方系统；
- **环境感知不足**：难以持续掌握项目状态、对话历史和工作上下文。
而 MCP 为 AI 补上了这些能力：
- **获取实时信息**：查询最新数据库内容、网页资料；
- **调用外部工具**：执行文件操作、接口请求以及其他自动化任务；
- **保持上下文状态**：理解结构化历史信息和当前工作环境。
简单来说，MCP 让 AI 从“只会思考”变成“能够连接现实并完成任务”。
## 二、MCP可以应用在哪些地方？
MCP 的价值并不局限于编程，它可以融入多种工作流。
### 1. 智能编程助手
Cursor 不仅可以阅读代码，还能够连接 GitHub、执行测试、查阅接口文档，从而更完整地参与开发过程。
### 2. 数据分析助手
连接数据库后，AI 可以根据自然语言生成查询语句、执行分析，并将结果整理成图表或报告。
### 3. 内容生产工具
AI 可以抓取网页资料，提炼重点、整理文章结构，甚至协助将内容发布到博客平台。
### 4. 自动化办公助手
从管理日历、发送邮件，到创建任务、处理文件，MCP 可以让 AI 真正参与日常工作。
# 三、实操：在 Cursor 中安装并使用 Filesystem MCP
下面以 Filesystem MCP 为例，体验如何让 Cursor 读取指定项目目录。
Filesystem MCP 的作用很直观：它可以帮助 AI 理解你的文件夹和项目结构。
## 1. 安装 Filesystem MCP
### 第一步：打开服务详情页
访问：
https://smithery.ai/server/@smithery-ai/filesystem
进入 Filesystem MCP 的介绍页面。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_70efc3c9d92e0b47d018ecac4647dcd2.png>
### 第二步：切换到 Cursor 配置页
点击页面中的 **Cursor** 选项卡，然后填写允许访问的目录。
例如：
```text
/Users/liyihang/Downloads/cursortest/pixpof
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b8ba72e94da2cfe324338deb4e15a686.png>
### 第三步：保存并连接
点击 **Save and Connect**。
### 第四步：复制安装命令
页面会生成对应的客户端安装命令，将它复制下来。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2ab6af9c35cc6c1574492dad44a13f90.png>
### 第五步：在终端执行命令
打开命令行工具，执行以下内容：
```bash
npx -y @smithery/cli@latest install @smithery-ai/filesystem --client cursor --config "{\"allowedDirs\":\"/Users/liyihang/Downloads/cursortest/pixpof\""
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0f319020684ce175f2e008c88205da64.png>
### 第六步：创建 Cursor 的 MCP 配置文件
进入你准备启用 MCP 的项目，在项目根目录下建立 `.cursor` 文件夹，并在其中创建：
```text
.cursor/mcp.json
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b0a7d63c827c0f8c9e74e28afd4b1cc7.png>
### 第七步：检查是否安装成功
打开 Cursor 设置，依次进入：
```text
Cursor → Setting → Cursor Setting → MCP
```
如果列表中出现 **filesystem** 服务，说明注册已经完成。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2b5df1e1bc44eb9e8d10eeae0ea429f1.png>
## 2. 调用 Filesystem MCP
安装完成后，就可以让 Cursor 分析指定目录了。
### 第一步：打开 AI 面板
- macOS：按下 `Cmd + I`
- Windows：按下 `Ctrl + I`
### 第二步：输入指令
例如：
```text
使用 filesystem MCP，帮我分析 /Users/liyihang/Downloads/cursortest/pixpof/Tests/Unit/Skills 目录的文件树结构。
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_94328fe60e8d0f388bb1654c2a175a60.png>
Cursor 会通过 Filesystem MCP 访问对应路径，并返回目录层级和文件结构分析。
### 环境准备提醒
许多 MCP 服务使用 Node.js 或 Python 编写，因此运行前需要准备相应的开发环境。
- Node.js：推荐使用 nvm 安装
https://github.com/nvm-sh/nvm
- Python：
- Linux/macOS 通常可以直接使用系统环境；
- Windows 用户可从官网下载：
https://www.python.org/downloads/
# 四、值得尝试的 MCP 服务
MCP 生态中有许多实用工具，下面列出一些常见选择。
## 1. Neon Database MCP：连接云数据库
它可以帮助 AI 与云端 PostgreSQL 数据库交互。
你只需要提出类似这样的需求：
> 帮我找出上个月销量最高的电子产品，并生成销售趋势图。
AI 就可以协助生成查询、读取数据库结果，并整理成可读的分析报告。
Neon 的特点是按需使用，闲置时可以自动休眠，对控制云服务成本比较友好。
## 2. Magic MCP：快速生成前端界面
如果你想制作一个具有渐变、动画或赛博朋克风格的页面，可以直接描述需求。
例如：
> 帮我生成一个赛博朋克风格的导航栏。
Magic MCP 可以根据描述生成相应的前端代码，让原型设计和界面开发更高效。
## 3. Filesystem MCP：理解项目文件
Filesystem MCP 适合用来读取项目目录、梳理文件关系、分析代码组织方式。
面对一个陌生项目时，你可以让它：
- 展示目录树；
- 查找指定类型文件；
- 分析项目结构；
- 定位配置文件；
- 辅助整理文件内容。
## 4. Browser-tools MCP：排查网页问题
Browser-tools MCP 可以获取浏览器控制台信息，协助分析页面异常。
当网页出现报错、组件失效或交互异常时，它能够帮助你查看控制台日志，定位相关 JavaScript 代码，并生成带截图的 Bug 报告。
## 5. SQLite MCP：用自然语言查询本地数据库
对于不熟悉 SQL 的用户，SQLite MCP 非常实用。
你可以直接说：
> 找出下单次数超过三次的客户。
AI 会协助完成数据库查询，并将结果用更容易理解的方式解释出来。
## 6. Tavily MCP：增强网络搜索能力
当你需要查找技术资料、框架文档或解决方案时，Tavily MCP 可以帮助 AI 搜索并整理互联网上的信息。
它适合用于：
- 查询开发文档；
- 搜索错误解决方案；
- 汇总技术社区内容；
- 对比不同实现方案。
## 7. Fetch MCP：提取网页内容
Fetch MCP 可以把网页内容转换为更适合 AI 处理的形式。
例如，你可以让它将一篇文章整理为 Markdown 笔记，保留正文、图片和代码块，并进一步提炼重点。
## 8. GitHub MCP：通过对话完成代码协作
接入 GitHub MCP 后，AI 可以参与更多代码仓库操作，例如查看项目内容、协助处理 Issue、分析提交记录以及辅助 Git 工作流。
代码协作也因此从命令操作，逐步转向自然语言交互。
## 9. Figma MCP：打通设计与开发
Figma MCP 可以把设计稿中的元素转换为前端实现。
例如，设计师在 Figma 中完成一个按钮设计后，AI 可以协助生成带有 hover 状态的 React 代码，还能将配色转换为 CSS 变量。
它的价值在于减少设计稿与实际代码之间的沟通成本。
# 五、从哪里寻找更多 MCP 服务？
如果想继续探索，可以访问以下平台：
1. MCP 服务目录：
https://mcp.so/
2. Glama MCP 服务集合：
https://glama.ai/mcp/servers
3. PulseMCP：
https://www.pulsemcp.com/
4. Smithery：
https://smithery.ai/
5. Composio MCP：
https://mcp.composio.dev
6. GitHub Awesome MCP Servers：
https://github.com/punkpeye/awesome-mcp-servers
7. Anthropic 官方 MCP Servers：
https://github.com/modelcontextprotocol/servers
## 进一步学习资料
MCP 官方网站：
https://modelcontextprotocol.io/
Cursor 官方 MCP 文档：
https://docs.cursor.com/context/model-context-protocol
# 六、MCP带来的真正变化
MCP 的意义，不只是增加几个工具，而是改变了 AI 的工作方式。
### 从封闭走向开放
AI 不再只能依赖既有训练数据，也可以访问网页、数据库和本地项目中的实时信息。
### 从被动回答转为主动执行
它不再只是等待用户提问，而是能够调用工具、获取资源并完成具体任务。
### 从通用能力变成专业能力
接入数据库、浏览器、设计工具或代码仓库后，AI 可以在不同领域发挥更强的作用。
### 从单点工具升级为协同系统
多个 MCP 服务可以组合起来：一个负责搜索资料，一个负责分析数据，另一个负责生成代码，最终形成完整的自动化流程。
## 写在最后
下次遇到编程问题时，不妨不要只问 Cursor“应该怎么写”，而是进一步思考：
> 能不能让它通过 MCP 直接读取项目、查询资料、调用工具并完成任务？
你可能会发现，Cursor 的能力远远不止代码补全和对话问答。
而且，MCP 不仅可以使用现成服务，你还可以进一步开发自己的 MCP 服务，为 AI 增加专属能力，打造真正属于自己的智能助手。