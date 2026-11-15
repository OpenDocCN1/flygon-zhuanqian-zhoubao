# 用 Cursor 做出复杂点的产品要怎么做？多个 AI 协同结伴编程可行吗？
Cursor 近期势头非常猛。先是 8 岁小女孩 45 分钟做出聊天机器人的视频刷遍全网，之后热度就一直没掉。在赚钱以及整个 AI 编程圈子里，很少有工具能像现在这样每天都在被晒成果。刷动态时，随处可见圈友分享的新尝鲜案例，其中不少都给了我很大的启发。
Cursor 初期爆火的时候，我正好被手头项目牵着走，并没有立刻投入精力去研究这款新工具。我的原想法很简单：它底层接的是 ChatGPT 和 Claude，那编程上限应该也逃不出大模型本身的能力范围。
转折发生在参加赚钱九月份的英文工具站航海。听完 Time 教练和大铭教练的讲解后，我对 Cursor 的定位才算清晰。于是赶紧装上试水，先做了一个俄罗斯方块的 Chrome 插件：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4b656bb9ffd8ad02989bbbc4031c6a8f.png>
实际上手后，Cursor 确实带来了更强的项目掌控感，但同样也暴露出和 ChatGPT 编程时类似的瓶颈。很明显，工具再强也还是被大模型的智力天花板卡住。于是我开始思考：之前总结的那套 ChatGPT 编程方法论，能否搬到 Cursor 上做改造？借助 Cursor 在项目统筹和代码掌控上的优势，有没有可能把复杂度拉得更高一点？
之后我在 YouTube 上看了不少 Cursor 的实操拆解，对它的能力边界有了更具体的认识。我给自己设了个小目标：不再满足于贪吃蛇、PDF 转图这类单一功能的玩具项目，直接挑战需要多模块联动、功能相对完整的产品。更进一步，我还刻意选了两个自己没碰过的方向：微信小程序和 WordPress 主题模板。
从 10 月 31 日到 11 月 20 日，正好 21 天，一个完整的航海周期内，我用 Cursor 闭环了 3 个项目：
*   临摹“块时间”App 的功能，做了一个微信小程序
*   对之前的网页内容抓取与下载 Chrome 插件做二次完善
*   从零搭起一个轻量级的 WordPress 主题模板
需要说明的是，我的编程基础大概只够看懂部分代码，接触 Cursor 也只有这短短 21 天。下面分享的体感和思路难免有偏颇，欢迎大家一起交流校正。
## Cursor 如此好用，之前那套 ChatGPT 编程打法还吃得上吗？
在讲 Cursor 实操前，先回顾一下我此前在赚钱里输出过的 ChatGPT 编程思路，后面 Cursor 的实践都是在这些思路上做了微调。
Cursor 之前，我已经在 ChatGPT 编程上做了不少尝试，也连载了 5 篇相关文章：
工具站新手怎样通过ChatGPT编程落地工具站产品
如何通过ChatGPTCode Interpreter生成视频特效和编写代码实现Chrome插件
怎样在航海21天通过ChatGPT编程上线20个Chrome插件
怎样通过ChatGPT编写Python爬虫工具，赚钱AI编程航海带给我们的潜在机会？
怎样通过ChatGPT编程开发价值百万的亚马逊选品分析工具？
其中第三篇里我整理过 10 条 ChatGPT 编程思路：
*   需求挖掘：项目方向模糊时，可以让 ChatGPT 帮忙做需求发掘，把零散点子梳理成可落地的需求点，并形成完整的需求分析。
*   需求分析：进入开发前，把自己的需求丢给 ChatGPT 优化成它能更好理解、后续好接手的开发说明。
*   分步输出：按步骤分文件或模块出码，先定好文件清单，再逐个让 ChatGPT 输出，减少上下文串线风险。
*   小步切入：入口要小，小到能先跑出一个完整可用但极简的版本。代码量少、功能点少，后续改错成本也低。
*   最小模块：要改或新增的功能，单独抽出来，每次只喂最小的代码片段给模型，降低逻辑跑偏概率。
*   代码学习：在加新功能前，重新开对话，把需求和相关代码再喂一遍做确认，确认无误后再继续。
*   指定代码：先让 ChatGPT 学习一段参考代码，再在其基础上做增量开发。
*   深度引导：反复对话仍不通时，要沉到具体功能点和代码行上，用自己的经验去引导。
*   自检问题：久拖不决时，可让它在代码里加 Console 日志，跑完把结果或报错原样喂回去让它自检修正。
*   适时回退：屡试不果时，回退到上一个可用版本的对话节点，从那里重新开发，并把之前踩坑的经验作为引导。
Cursor 已经很强了，这些老思路还有价值吗？
这 21 天的独航给了我答案。接下来用三个案例说明如何把这些思路做轻微改造，再用 Cursor 做出复杂度更高的产品。为了更清晰地对比能力，我还给自己设了限制条件：
第一个项目全程只用 Cursor 的 Composer；
第二个项目的二次开发全程只用 Cursor 的 Chat；
第三个项目尝试 Composer 搭配多个 Chat 窗口协同结伴编程。
## 如何用 Composer 启动一个时间块小程序的开发？
Cursor 的真正价值不只是自动建文件、省去复制粘贴的体力活，而是能借助合理的引导方式，让我们更好地驾驭整个项目。从教练分享里能看出，Cursor 可以读懂并梳理项目全貌，能检索代码与内容，还能在指定文件甚至代码片段的范围内做分析与开发，这为 AI 编程打开了新的空间。
结合之前 ChatGPT 的思路，我们完全可以提前把需求分析和开发步骤准备好、细化到足够小，再把这些材料存成项目根目录的一个文档，让 Cursor 依此来推进开发流程。
### I. 怎样借助 Cursor 启动一个项目？
为了让开发更顺滑，我先用 ChatGPT 长对话梳理了小程序开发的流程，并整理出本项目的需求分析和开发步骤：
需求分析文档：
```
# 时间感微信小程序——“时间分块管理”模块需求分析文档
## 1\. 项目背景
时间感微信小程序是一款时间管理工具，通过“时间分块”模块帮助用户更有效地管理日常生活，提升时间利用效率。该模块以时间块的形式记录并管理活动时间，满足用户对碎片化时间管理、目标设定和自我审查的需求。
## 2\. 需求概述
本模块允许用户将一天划分为多个时间槽，以小时为单位展示一天的24小时，并支持在每小时中进一步划分5、10、15、20或30分钟的小单位时间块，便于用户灵活管理碎片化时间活动。此外，通过数据导出和备份功能，支持用户迁移数据至另一设备上的微信小程序。
## 3\. 功能需求分析
### 3.1 基础时间块创建
- **需求描述**：用户可以按小时创建基础时间块，并在每小时内使用小单位时间块记录活动。
- **详细说明**：
- **时间块单位**：每天24小时划分为小时，每小时可按5、10、15、20或30分钟的小单位划分，满足碎片化管理需求。
- **打点记录**：通过点击按钮创建时间块记录。
- **颜色与标签**：时间块可自定义颜色与标签（如“工作”、“休闲”）。
### 3.2 事件印章（模板）
- **需求描述**：支持通过高频活动模板（印章）快速记录常用活动。
- **详细说明**：
- **模板设置**：用户可以保存常用活动为印章，简化重复记录。
- **快速填充**：选择印章后直接填充活动信息。
### 3.3 自定义分类与事件排序
- **需求描述**：支持用户按类别组织时间块，且自动排序常用活动。
- **详细说明**：
- **多级分类**：支持创建多层级分类（如“工作 > 会议”）。
- **自动排序**：根据前日或一周使用频率自动排序，常用活动置顶。
### 3.4 目标与提醒设置
- **需求描述**：支持活动目标设定和提醒功能。
- **详细说明**：
- **目标类型**：支持设定日、周、月目标（如“每日阅读1小时”）。
- **提醒功能**：当时间块累计达到目标时自动提醒。
### 3.5 时间槽划分与可视化分析
- **需求描述**：按时间段展示时间块，并提供数据可视化功能。
- **详细说明**：
- **时间槽划分**：每天24小时划分为小时单位，用户可在每小时内添加多个小单位块。
- **统计图表**：通过饼图、条形图等形式展示高效时间与浪费时间。
### 3.6 灵活小时间块使用
- **需求描述**：用于记录短时活动的时间块。
- **详细说明**：
- **小时间块设置**：支持按5、10、15、20或30分钟使用，以安排短时任务。
- **颜色区分**：使用颜色区分“浪费时间”和“重要时间”。
### 3.7 周期性任务与重复时间块
- **需求描述**：支持设置周期性任务，用于重复记录高频活动。
- **详细说明**：
- **周期任务**：支持每日、每周、每月的周期任务。
- **自动生成时间块**：根据周期性任务自动生成时间块，简化日常记录。
### 3.8 时间审查与时间黑洞检测
- **需求描述**：定期生成时间审查报告，帮助用户优化时间使用。
- **详细说明**：
- **时间审查报告**：每周生成报告，显示高效和低效时间。
- **黑洞检测**：标识浪费时间多的活动或时段，供用户分析。
## 4\. 数据存储与备份需求
### 4.1 数据存储
- **本地文件系统 API**：通过微信小程序的 `wx.getFileSystemManager` API，将数据以 JSON 文件格式存储在本地文件系统中，确保短期内的数据持久化。
- **防缓存清理策略**：本地存储在文件系统的 JSON 文件比 `wx.setStorage` 缓存更为持久，可以在一定程度上避免被微信自动清理。
### 4.2 数据导出与迁移
- **导出与备份**：支持用户将本地 JSON 数据文件导出到用户设备，提供下载或导出选项，以便在本地存储之外额外备份。
- **数据迁移**：用户可手动将备份文件下载至本地存储，并在新设备上导入该文件，恢复数据而无需云端依赖。
## 5\. 非功能需求
- **用户体验**：界面设计需简洁，操作流程流畅，确保在微信环境中的触屏适用性。
- **兼容性**：支持不同分辨率设备，并在多种微信版本下兼容运行。
- **数据安全**：用户数据加密存储，提供导出备份文件的加密选项，确保隐私保护。
## 6\. 测试需求
- **功能测试**：确保时间块创建、模板应用、周期任务设定等模块稳定运行。
- **性能测试**：验证在微信小程序本地文件系统中进行高效读写操作，确保性能稳定。
## 7\. 风险分析
- **存储空间限制**：微信小程序的本地文件系统存储空间依赖用户设备，存在空间清理的风险，需做好备份导出提醒。
- **数据迁移风险**：使用本地 JSON 文件进行跨设备数据迁移时，需确保文件格式的兼容性并设计易用的导入导出流程。
```
开发步骤和文件结构：
```
# 时间感微信小程序开发步骤与文件结构
## 开发步骤
### 最小可用模型 (MVP)——“基础时间块创建”功能
#### Step 1: 初始化项目结构与主界面展示
1\. **新建项目结构**
- 创建基础的项目文件结构和配置文件 `app.js`、`app.json`、`app.wxss`，并初始化页面。
2\. **创建主页面结构**
- **新增**：`pages/index/` 文件夹，并创建 `index.wxml`、`index.js`、`index.wxss` 文件。
- **编写内容**：在 `index.wxml` 中实现简单的页面布局，展示“欢迎使用时间感小程序”字样，用于基本的页面加载测试。
3\. **测试**：启动项目，确保页面能够正常加载，且主页面的展示内容无误。
#### Step 2: 基础时间块创建的页面设计
1\. **创建“时间块创建”页面**
- **新增**：在 `pages/create-block/` 文件夹中创建 `create-block.wxml`、`create-block.js`、`create-block.wxss`。
- **添加路由**：在 `app.json` 中配置该页面的路由。
- **页面内容**：在 `create-block.wxml` 中添加表单元素（如选择时间、颜色和标签的控件）。
2\. **编写页面跳转**
- **更新**：在 `index.wxml` 中添加一个“创建时间块”按钮。
- **跳转逻辑**：在 `index.js` 中编写跳转逻辑，使得点击按钮时可以跳转到 `create-block` 页面。
3\. **测试**：点击“创建时间块”按钮，确认是否跳转到时间块创建页面。
#### Step 3: 实现时间块数据输入与本地存储
1\. **实现时间块输入功能**
- **更新**：在 `create-block.wxml` 中设计输入表单，支持选择时间、颜色和标签信息。
- **初始化表单数据**：在 `create-block.js` 中定义表单输入的初始值（如颜色列表和默认标签）。
2\. **使用本地文件系统存储时间块数据**
- **新增**：创建 `utils/fileManager.js`，封装文件写入功能，使用 `wx.getFileSystemManager` 保存 JSON 文件。
- **调用存储方法**：在 `create-block.js` 中添加保存按钮，并在点击后调用 `fileManager.js` 保存表单数据。
3\. **测试**：完成表单填写并保存，查看 JSON 文件内容是否正确保存。
#### Step 4: 主页面显示已保存的时间块
1\. **读取数据并在主页展示**
- **更新**：在 `index.js` 中调用 `fileManager.js` 读取 JSON 数据，并将数据渲染到 `index.wxml` 中。
- **布局调整**：在 `index.wxml` 中编写时间块的展示样式，包括颜色和标签的显示。
2\. **自动刷新页面**：当用户保存新时间块后，主页数据自动刷新。
3\. **测试**：保存多个时间块，确保主页能够正确展示所有已保存时间块。
#### Step 5: 增加事件印章（模板）功能
1\. **模板页面结构**
- **新增**：创建 `pages/templates/` 文件夹，并创建 `templates.wxml`、`templates.js`、`templates.wxss` 文件。
- **路由配置**：在 `app.json` 中添加 `templates` 页面路由。
2\. **添加模板增删功能**
- **模板设计**：在 `templates.wxml` 中编写模板添加表单，用于用户输入模板名称和默认颜色、标签。
- **数据存储**：在 `fileManager.js` 中扩展存储方法，新增对模板的保存和删除。
3\. **模板引用**：在 `create-block.js` 中加载模板，并显示到创建表单，允许用户选择模板。
4\. **测试**：添加模板并在创建时间块时使用模板，确认模板功能正常。
#### Step 6: 添加时间块分类和自动排序
1\. **自定义分类实现**
- **分类设计**：在 `create-block.js` 中新增“添加分类”选项，支持用户定义不同类别。
- **数据存储**：将分类信息保存在本地 JSON 文件。
2\. **按使用频率自动排序**
- **更新**：在 `index.js` 中读取时间块时，根据频率字段排序。
3\. **测试**：添加多个分类并保存时间块，确保主页面按频率正确排序。
#### Step 7: 目标与提醒设置
1\. **目标设定界面**
- **新增**：在 `pages/create-block/` 表单中增加目标时长字段。
- **提醒设置**：在 `create-block.js` 中定义目标时长和提醒触发逻辑。
2\. **提醒触发**：在主页中检测时间块累计时长，达到目标时提醒。
3\. **测试**：设定目标并查看提醒触发。
#### Step 8: 数据统计与时间黑洞检测
1\. **统计页面**
- **新增**：`pages/statistics/` 文件夹和对应文件。
- **数据展示**：在 `statistics.js` 中读取时间块数据，并进行高效时间和低效时间的统计。
2\. **图表显示**：在 `statistics.wxml` 中使用饼图、条形图显示统计结果。
3\. **测试**：在统计界面查看数据的可视化效果。
#### Step 9: 灵活小时间块使用
1\. **小时间块选择**
- **更新**：在 `create-block.wxml` 中新增5、10、15、20、30分钟小时间块选项。
2\. **时间块分配**
- **逻辑调整**：在 `create-block.js` 中调整分配逻辑，确保可以选择小时间块。
3\. **测试**：选择不同的小时间块，确认数据保存和显示正确。
#### Step 10: 周期性任务与重复时间块
1\. **周期性任务设置**
- **页面更新**：在 `create-block.wxml` 中新增周期选项（每日、每周、每月）。
- **数据存储**：将周期信息保存在时间块数据中。
2\. **重复时间块生成**：在 `fileManager.js` 中扩展数据读取逻辑，自动生成周期性时间块。
3\. **测试**：设置周期性任务，确认在首页定期生成相应时间块。
#### Step 11: 导出与迁移功能
1\. **数据导出**
- **新增**：在 `fileManager.js` 中添加数据导出功能，将数据保存为文件供用户下载。
2\. **数据导入**
- **导入逻辑**：在 `fileManager.js` 中实现从文件导入，自动识别数据格式并恢复。
3\. **测试**：导出当前数据并在新设备导入，确保数据一致性。
## 文件结构与用途说明
```plaintext
时间感小程序/
├── app.js                     # 小程序主逻辑文件，负责全局生命周期管理
├── app.json                   # 小程序全局配置文件，定义页面路由和小程序配置
├── app.wxss                   # 小程序全局样式文件
├── pages/                     # 页面文件夹
│   ├── index/                 # 主页，展示所有已创建的时间块
│   │   ├── index.js           # 主页逻辑，加载并显示时间块数据
│   │   ├── index.wxml         # 主页布局，显示所有时间块
│   │   └── index.wxss         # 主页样式
│   ├── create-block/          # 时间块创建页面，支持用户添加新时间块
│   │   ├── create-block.js    # 创建页面逻辑，处理用户输入并保存时间块数据
│   │   ├── create-block.wxml  # 创建页面布局，包括时间、颜色、标签输入表单
│   │   └── create-block.wxss  # 创建页面样式
│   ├── templates/             # 模板管理页面，管理高频活动模板
│   │   ├── templates.js       # 模板页面逻辑，实现模板的添加、删除与应用
│   │   ├── templates.wxml     # 模板页面布局，展示模板列表和添加模板表单
│   │   └── templates.wxss     # 模板页面样式
│   ├── statistics/            # 数据统计页面，展示时间使用情况和黑洞检测
│   │   ├── statistics.js      # 数据统计逻辑，生成统计图表和分析数据
│   │   ├── statistics.wxml    # 统计页面布局，包括统计图表和时间分析
│   └── settings/              # 设置页面，管理用户的偏好设置与数据导出
│       ├── settings.js        # 设置页面逻辑，管理导出、备份和偏好设置
│       ├── settings.wxml      # 设置页面布局，包括备份与导入选项
│       └── settings.wxss      # 设置页面样式
├── utils/                     # 工具文件夹
│   ├── fileManager.js         # 文件管理模块，封装本地文件的读写操作
│   ├── dataProcessor.js       # 数据处理模块，用于处理统计和周期性任务
│   └── reminder.js            # 提醒模块，用于设置和管理时间块的提醒功能
├── assets/                    # 静态资源文件夹
│   ├── colors.js              # 颜色配置文件，定义时间块可选择的颜色
│   ├── icons/                 # 图标资源，用于小程序的UI
│   └── chart.js               # 图表库文件，用于生成统计页面的可视化图表
└── config.js                  # 配置文件，存放全局配置和默认参数
```
```
我把这两份材料放到工程根目录下。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ce8710377c9e91a590a00588cead8e69.png>
动手编码之前，有三件事必须提前安排妥当：
第一，下载并安装“微信开发者工具”，之后预览、调试代码都靠它；
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8b9a820de99ae06bae8db1dc99060759.png>
第二，手动新建一个工程目录，并让 DevTools 和 Cursor 都指向这个共同目标，切勿直接在 DevTools 中新建工程。这样一来，Cursor 生成的代码会实时出现在该目录内，免去手动合并与复制粘贴的烦恼；
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_592289de244bc7c416743048434835ae.png>
第三，把官方开发文档的链接 https://developers.weixin.qq.com/miniprogram/dev/framework/ 录入 Cursor 的 doc，作为后续开发的知识底座。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0cc9b37f31abe7aa86908b1c5e15ffab.png>
这些前置工作就位后，便可正式启用 Cursor 的 Composer 来编码。告诉 Composer：以我们拟好的需求分析与实施步骤为蓝本进行开发，并把“需求分析.md”、“开发步骤与文件结构.md”以及官方文档一并交给它，每推进完一个环节，就示意它继续。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d18567c8f373050a6c086c2f981fa884.png>
过程中如果冒出报错或意外状况，就按后面的策略二处理——把错误现象或提示原样丢给 Composer 去整改。没花太长时间，Composer 便交付了一个时间块应用的初版。这个初版离最终设想还有很大差距，但对我而言意义十足：它是我独立完成的第一个应用，而且已经能添加第一块时间块。接下来，我会与 Composer 一路协作，把这款产品逐步推向理想的形态。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f8e0100ee218bdc9e61aa41745be4e99.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9b1f667c0c8a4cbcd0f5689150cf51aa.png>
这是我借助 Cursor 编程的策略一：预设框架，分步实施。
先把需求拆透，再列出细致的施工步骤，让每个入口都足够小而清晰。然后把这两份文档保存到仓库根目录，让 Cursor 依据它们按图索骥、循序完成全部流程。
### 二、出问题时，怎么借助 Cursor 排雷？
那么，Cursor 能一路绿灯地把应用写完吗？显然不能。前面已经说过，它终究被 LLM 的能力边界所限。编码过程中，各种错误依旧层出不穷——有时是 AI 选错了方向，有时是上下文窗口太长放不下，更多时候是我没能把意图表达周详。
代码报错后，究竟该怎么办？
这正是我实践出的策略二：引导 AI 自查自纠。
程序崩溃时往往有异常表现，有些还会附上清晰的错误提示。把现象和提示发给 Cursor，让它自行修正。若连着几轮都没解决，再引导它在代码中插入跟踪日志，把运行结果或日志信息递回去供它定位问题。
例如，开发这款时间块应用期间，出错时 DevTools 的控制台常常会出现红字报错：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_25d0350de2c5467585d35741ae47e218.png>
把这段错误信息复制给 Composer，请它处理：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bf46d310ea765281c6c0b99dcb1ddc67.png>
代码规模膨胀后，Cursor 也撞上了 ChatGPT 时代的通病——上下文窗口受限。逻辑耦合度高的程序尤其如此，一旦某段关键代码没有被包含在窗口内，Cursor 就可能产出有 bug 或偏离预期的内容。
和 Composer 经过多轮对话与修复，应用终于有了看得见的进展：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c6c850c6c4fbcc70527ea757d9327a77.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e663c77e7a0c83962dce00742641ec2d.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_253b9063f6db850d05d740a71ee1d47a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_46d9629c12a7b26d7f7efb13985c515d.png>
### 三、想给项目加新功能，怎么做？
不得不承认，Composer 帮我搭这个应用的过程挺曲折。为了搞定一个 bug，我们经常要展开大量对话，会话记录越积越多，开发节奏也被打乱。我只好一次次让 Composer 重新审视项目现状，努力把它拽回预设的步伐。这也是我后来在第三个项目中，考虑让 Composer 和 ChatGPT 协同工作的直接原因。
另外，最初由 ChatGPT 拟定的需求文档和实施步骤也存在疏漏，没有准确描述时间块应有的功能与外观，使得实现出来的逻辑和预期相去甚远，给后来临时改需求、二次开发增添了额外负担。
为了化解这个难题，我总结出了策略三：化简功能，分部交付。
一旦功能比较复杂，AI 很难一次性给出正确代码。此时，除了应用后面的第七种办法跟它深入讨论方案，还应让它把方案切分成多个小步骤编码输出。假如每个步骤都能实测并反馈，AI 完工的概率和最终质量都会明显提高。
比如，请 Composer 重新梳理时间块的相关逻辑：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6e1eaa61c8a5bd889f0f4f2e3782780a.png>
而后让它生成一份二次开发的施工文档：
```
# 时间感小程序二次开发步骤
## 一、设置页面增加时间单位配置
### Step 1: 更新设置页面的数据结构
1\. 在 `settings.js` 中添加时间单位配置数据
2\. 添加保存和读取时间单位配置的方法
### Step 2: 添加时间单位选择UI
1\. 在 `settings.wxml` 中添加时间单位选择器组件
2\. 在 `settings.wxss` 中添加相应样式
### Step 3: 实现时间单位配置的存储
1\. 在 `fileManager.js` 中添加时间单位配置的读写方法
2\. 确保配置在应用启动时被正确加载
## 二、首页改版 - 时间分布展示
### Step 1: 重构首页布局
1\. 修改 `index.wxml` 布局结构，将时间分布板块移至日期选择器下方
2\. 调整 `index.wxss` 中的样式以适应新布局
### Step 2: 实现时间分布网格
1\. 创建时间网格组件 `components/time-grid/`
2\. 根据配置的时间单位动态生成网格
3\. 添加网格单元格的默认样式（浅灰色背景）
### Step 3: 添加事件模板侧边栏
1\. 创建模板侧边栏组件 `components/template-sidebar/`
2\. 实现模板的纵向排列展示
3\. 添加模板项的样式和交互效果
## 三、时间块选择与设置功能
### Step 1: 实现单元格选择逻辑
1\. 在时间网格组件中添加单元格点击事件
2\. 实现单元格的选中状态管理（高亮显示）
3\. 添加多选功能支持
### Step 2: 添加事件模板应用功能
1\. 实现模板点击事件处理
2\. 添加选中单元格的事件设置逻辑
3\. 更新单元格显示（事件名称和背景色）
### Step 3: 实现单元格编辑功能
1\. 添加已设置事件单元格的选中逻辑
2\. 实现事件重新设置功能
3\. 添加双击清空事件的功能
## 四、数据存储与状态管理
### Step 1: 更新数据结构
1\. 修改时间块数据结构以适应新的时间单位
2\. 更新 `fileManager.js` 中的数据处理方法
### Step 2: 实现状态同步
1\. 确保时间块状态在组件间正确同步
2\. 实现实时保存功能
### Step 3: 优化性能
1\. 添加数据缓存机制
2\. 优化渲染性能
3\. 添加必要的错误处理
## 五、UI优化与交互改进
### Step 1: 优化视觉反馈
1\. 添加选中/取消选中的动画效果
2\. 优化高亮状态的视觉效果
3\. 添加操作成功/失败的提示
### Step 2: 改进交互体验
1\. 添加拖动选择功能
2\. 实现快捷键支持
3\. 添加撤销/重做功能
### Step 3: 适配与测试
1\. 确保在不同屏幕尺寸下的正确显示
2\. 进行兼容性测试
3\. 进行性能测试
## 六、文档与发布
### Step 1: 更新文档
1\. 更新用户使用说明
2\. 更新开发文档
3\. 添加新功能的示例说明
### Step 2: 测试与修复
1\. 进行完整的功能测试
2\. 修复发现的问题
3\. 进行用户体验测试
### Step 3: 发布更新
1\. 更新版本号
2\. 准备更新说明
3\. 发布新版本
```
然后我们让Composer根据这个二次开发步骤的文档做开发：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8a8a87eef18a1fb7538babeb67ccd604.png>
借助Cursor的Chat连续一周的高频交流与反复调试，我最终用它完成了人生中第一个小程序。借助这个小程序，我验证了Composer在驾驭一个完整项目时的表现，以及它是否能独立把一个项目跑通。
## 怎样用Cursor的Chat对Chrome插件做二次开发与完善？
在Composer独立把小程序做出来之后，我紧接着要检验Chat在编程上的实战能力。这一次，我没有从零开新项目，而是直接让Chat在已有Chrome插件的基础上进行二次开发。这个插件原本是靠ChatGPT一点点写出来、多次迭代堆起来的，随着代码体量变大、复杂度提升，我越发难以用ChatGPT去掌控。现在插件正好卡在两个我觉得比较棘手的问题上，我想看看Cursor的Chat能不能在已有代码量和复杂度尚可的项目里做增量开发并把难题解决掉。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d1ecafafada9bc1ca1dff8a7a3c46cb9.png>
### IV. 如何用Cursor来做项目的二次开发？
打开项目后，我先让Chat进入Codebase模式，对插件做一个初步的认识和分析：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cb751183c768e814840d68288c69388b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ddca2e699efe7306f7cb482f1bd5711f.png>
Cursor有板有眼地给我做了一番梳理，覆盖了插件的部分核心功能，但整体并不算完整。这也情有可原，因为插件的核心js文件代码量已经接近1万行，早已超出Cursor调用的Claude3.5能处理的上下文上限。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9ebd148282559f6db1066bca1160cfef.png>
由于我对这套代码本身比较熟，所以和Chat的对话很容易就深入到具体逻辑层，并且能对Chat做针对性的引导。受篇幅限制，这里不展开整个过程，重点说说我在该项目里对Cursor编程的一些思路。
我总结的Cursor编程思路四：借助经验做明确引导
在用Cursor编程时，如果你对需求和逻辑足够熟悉，就可以用自己的经验去引导Cursor按你的思路产出代码。随着项目复杂度升高，Cursor会因大模型上下文长度的限制而对项目整体的掌控力变差。这个时候，主动引导Cursor编程，而不是让Cursor牵着你走，会让项目推进和迭代更顺畅。
举例来说，在这个项目里，我多次要求Cursor必须按照我的方案来写：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_91c4835921a8d9519e448e28c647ad13.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ce9d58bc1c62a168e43628a05b20090f.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cf34792b705eeb039f48cf621cc0635a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b9784564d04c968f5f5b56ae39564c23.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7ad12038a8fc55716a56db6ef3194068.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f907454bd1bd5c49a31c22fe71189e1e.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_98760cfab00efac039f7c3a295840ca7.png>
从截图里也能看出，我习惯用“@”调取相关文件，或通过“Add to Chat”把特定代码片段丢给Chat，让它基于这些片段进行分析和修改<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9ebd148282559f6db1066bca1160cfef.png>。这正是我的Cursor编程思路五：限定代码范围、指定上下文。Cursor新版已取消“Add to Chat”，可以用快捷键 Cmd + Shift + L 在Mac或 Ctrl + Shift + L 在Windows下添加片段。在实现某个功能或解决某个问题时，尽量把所有关联代码都喂给Composer或Chat，让它在我们划定的范围内工作，这样能最大程度削弱上下文限制对代码生成的干扰。
### V. Cursor写出来的代码老是报错怎么办？
用Cursor或ChatGPT编程时，经常会遇到AI给的代码一遍遍报错、反复调试仍不达标。我是怎么处理的？
第一步是回滚代码，也就是我总结的Cursor编程思路六：做好备份，必要时回退
用Cursor改代码时，如果你没有做版本控制，至少要在每个关键节点留好备份，防止代码被改乱后无法恢复。某个问题经过多次对话仍未解决时，继续硬聊大概率会越走越偏，这时不如退回之前能正常跑的版本，在原对话位置重新提问，让Cursor基于正确的版本继续开发。重写时可结合之前调试确认的结论对Cursor做引导。
如果回退后依然不行，可以试试我的Cursor编程思路七：先把问题聊透再动手写
很多时候代码写不出来，并不是模型不行，而是需求没表达清楚。对需求敏感的产品经理和逻辑清晰的程序员在这方面天然有优势，他们能用经验给AI做精准引导。当Cursor在某个问题上卡很久时，不妨先暂停，不急着让它输出代码，先和它把预期功能、涉及的文件和逻辑细节充分讨论清楚，等双方达成共识后再让它写代码。这样需求更明确、代码范围更精准，产出的逻辑往往更靠谱。
赚钱圈友黄钊说过一句很到位的话：“用AI时要把AI当成人，设计AI时要把人当成AI。”确实如此。
比如在解决下面这个问题的过程中，我没有直接让Chat写代码，而是反复强调“先告诉我你的方案，不要输出代码”。和Cursor来回聊了十轮左右，直到问题理解完全对齐：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b1966ecf8db5623cbe892c99e7fadeb2.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d4b2524f42ee5a7723af524b01a59e8.png>
在方案明确、共识达成后，我们本可以让Chat直接写，但我又用了前面提到的“Cursor编程思路三：拆分功能、分步输出”，先让Chat给出该功能的开发步骤，因为这个方案涉及多个环节，流转比较复杂。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bc5768333664327796db05fd6a727a6b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b4a2e5ad5f612bda74bfd6b58b419b67.png>
正是这种方式，最终帮我解决了Chrome插件爬虫功能里手动识别同类潜在行元素的问题，还把缓存方案从原来的chrome.storage.local迁移到了IndexedDB，大幅提升了插件存储更大内容、爬取更多数据的能力。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6299b5ebc5fa4af79c2174209dac8284.png>
## 怎么让多个AI协作结伴，合力开发一个WordPress主题模板？
### VI. Cursor的Composer和Chat各有什么特点？区别在哪？
Cursor相比其它编程IDE，并不只是简单集成了Claude、ChatGPT等主流大模型，而是一个融合了知识库、联网能力以及多种AI编程方式的AI编程工具。我们可以用Composer生成文件和代码，用Chat做编程，也可以用“Ctrl+K”做局部代码生成和处理，还能用“Tab”键让Cursor自动补全后续代码。
于是我开始思考，同一个IDE里为什么要集成这么多AI编程方式，尤其是Composer和Chat。前面实践证明，二者都能独立完成一个项目，甚至能搞定复杂度不低的项目，它们之间到底是什么关系？各自擅长什么？
带着这些疑问，我特意去问了Cursor的Chat<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_179128daceff6cee054fe2d50559c0ec.png>。对话比较长，详见附录III，有兴趣的朋友可以看看，或许能从中看出AI编程的内在逻辑。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_179128daceff6cee054fe2d50559c0ec.png>
Chat很快给出了二者的区别和能力定位，很清晰：Composer更擅长“搭建初始代码框架、给出具体实现方案”，而Chat更擅长“代码审查、优化建议、问题定位、架构建议、最佳实践指导”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b99134214322aee4301b7293ae0f3da3.png>
基于这两个能力画像，我就想：能不能让它们组队PK、结伴编程？带着这个想法，我启动了第三个Cursor项目：做一个轻量级的WordPress主题模板。
### VII. WordPress主题网站概览
WordPress作为全球最大的开源建站框架，以其灵活的架构和庞大的生态著称，第三方主题和插件生态服务了海量公司和开发者。
其中，Avada主题在ThemeForest上已售出99万份，按售价折算约人民币4.95亿元，即使扣除联盟佣金和推广成本，净利润也有2.5亿元左右。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0720bff2b17146dc43e23b3432de72bd.png>
Avada是一个偏重型的模板，可集成商城和论坛等功能，复杂度很高，使用方式甚至有人专门做成课程来教。
我个人比较偏爱的是国内团队出品的一套模板，先看演示效果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1099b8dcd69b2e83a28ed43fe5624296.png>
链接：https://www.wpcom.cn/themes/justnews.html
是不是看起来很眼熟？
没错，这正是龙哥盟官网改版前使用的WordPress主题JustNews。这套模板可以灵活定制网站界面框架，使用体验也相当不错。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_54032783fe4915b416d8d0dfbbabdd25.png>
### VIII. 如何让Cursor的Composer和Chat协作结伴编程
我们的计划是先让Cursor学习这套模板，总结其功能和特点，再从中挑选相对基础的部分作为我们WordPress主题项目的需求清单。虽然最终没能复刻JustNews全部功能，但有了对标目标，逐项追赶会更清晰。
接下来，先做这次项目的“人员”分工：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bd0e05243ff27e037c43cef120c39c68.png>
*   产品经理由一个Chat担任，负责梳理需求并规划开发步骤；
*   核心开发骨干Composer，负责按产品经理的方案和步骤生成代码，并把控项目整体进度；
*   多个代码审查专家由多个Chat担任，负责找出并解决Composer代码中的问题；
*   UI设计专家由一个Chat担任，负责样式优化和细节处理。
为什么要这样安排？Composer不能自己审查修复吗？Chat不能直接开发吗？原因如下：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c2584dbe5515b5c61fa4171a8100241b.png>
1、Composer在项目掌控和文件生成上更有优势，所以由它负责全局和代码产出。但它同样受上下文长度限制，因此我们尽量不让它做代码审查和修复，因为审查调试通常需要多轮对话，会更快吃掉上下文。
2、Chat更适合深入审查某段代码，我们可以和它细聊某个或多个具体问题，这个过程对话量容易膨胀，所以安排多个Chat作为审查角色。
3、Composer和Chat底层都是大语言模型，比如Claude，在不同对话窗口里对同一问题的视角往往会不同，这种安排能让它们用不同方案解决同一个问题。
4、我自己用Cursor才21天，还是新手，以上分工只是一次实验，并非定式。后续完全可以尝试让多个Composer协作，或者调整角色配置，编程体验可能会大不一样。
这就是我总结的Cursor编程思路八：多AI协作、结伴编程
提前为Composer和Chat分配不同的AI角色，让每个AI各司其职，从不同角度配合，最终共同解决Cursor编程中的各种问题。
和之前的思路一一样，我们先让“产品经理Chat”学习JustNews主题的功能，然后整理出一份需求文档，并附上开发步骤和文件结构<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bd0e05243ff27e037c43cef120c39c68.png>。对话较长，详见附录II。
```
# CentLight WordPress主题开发需求文档
## 1\. 项目概述
### 1.1 项目名称
- 主题名称：CentLight
- 版本：1.0.0
- 定位：轻量级SEO友好的博客/资讯类WordPress主题
### 1.2 项目目标
- 开发一个性能优异的WordPress主题
- 确保优秀的SEO表现
- 提供清晰的内容展示
- 实现响应式设计
## 2\. 技术规范
### 2.1 开发环境
- WordPress 6.0+
- PHP 7.4+
- MySQL 5.7+
- HTML5 + CSS3
- 原生JavaScript (无jQuery依赖)
### 2.2 浏览器支持
- Chrome (最新3个版本)
- Firefox (最新3个版本)
- Safari (最新2个版本)
- Edge (最新2个版本)
## 3\. 核心功能需求
### 3.1 主题框架
必需功能：
1\. 响应式布局
- 断点设置：1200px, 992px, 768px, 576px
- 移动优先设计
2\. 头部设计
- LOGO支持（图片/文字）
- 主导航菜单
- 搜索框
- 移动端菜单按钮
3\. 页面布局
- 内容区域宽度：1200px
- 文章列表：右侧边栏布局
- 文章页：可选无侧边栏
4\. 页脚设计
- 版权信息
- 社交媒体链接
- 底部菜单
### 3.2 SEO优化
核心功能：
1\. Meta信息优化
- 自动生成title标签
- 智能描述生成
- 关键词提取
2\. 结构化数据
- 文章Schema
- 面包屑Schema
- 站点信息Schema
3\. 内部链接
- 相关文章推荐
- 分类链接优化
- 标签云
4\. 技术优化
- 语义化HTML5标签
- 自动生成sitemap
- 规范的URL结构
### 3.3 文章功能
基础功能：
1\. 文章列表
- 大图模式
- 小图模式
- 无图模式
- 分页导航
2\. 文章页面
- 文章标题
- 特色图片
- 作者信息
- 发布时间
- 阅读量
- 分类标签
- 文章目录
- 分享按钮
- 上下篇导航
3\. 文章互动
- 点赞功能
- 评论系统
- 分享功能
### 3.4 性能优化
优化措施：
1\. 资源加载
- 关键CSS内联
- JavaScript异步加载
- 图片懒加载
- WebP支持
2\. 代码优化
- CSS/JS压缩
- HTML压缩
- 资源合并
3\. 缓存策略
- 浏览器缓存
- WordPress对象缓存
- 静态资源缓存
## 4\. 文件结构
centlight/                        # 主题根目录
├── style.css                    # 主题信息和主要样式文件
├── index.php                    # 主页模板
├── header.php                   # 头部模板
├── footer.php                   # 底部模板
├── sidebar.php                  # 侧边栏模板
├── functions.php                # 主题函数和功能
├── single.php                   # 文章详情页模板
├── page.php                     # 页面模板
├── archive.php                  # 归档页面模板
├── search.php                   # 搜索结果页模板
├── 404.php                      # 404错误页面
├── comments.php                 # 评论模板
├── screenshot.png               # 主题预览图
│
├── assets/                      # 资源文件目录
│   ├── css/                    # CSS文件
│   │   ├── style.css          # 主要样式
│   │   ├── mobile.css         # 移动端样式
│   │   ├── admin.css          # 管理后台样式
│   │   ├── editor-style.css   # 编辑器样式
│   │   └── customizer.css     # 定制器样式
│   │
│   ├── js/                     # JavaScript文件
│   │   ├── main.js            # 主要脚本
│   │   ├── customizer.js      # 定制器脚本
│   │   └── modules/           # 功能模块脚本
│   │       ├── navigation.js  # 导航菜单
│   │       ├── search.js      # 搜索功能
│   │       ├── lazyload.js    # 图片懒加载
│   │       ├── likes.js       # 点赞功能
│   │       └── share.js       # 分享功能
│   │
│   └── images/                 # 图片资源
│       ├── default-header.jpg  # 默认头部图片
│       └── icons/             # 图标文件
│
├── inc/                        # 包含文件目录
│   ├── core/                  # 核心功能
│   │   ├── setup.php         # 主题设置
│   │   ├── init.php          # 初始化函数
│   │   ├── scripts.php       # 脚本加载
│   │   ├── styles.php        # 样式加载
│   │   └── widgets.php       # 小工具注册
│   │
│   ├── customizer/           # 主题定制
│   │   ├── customizer.php    # 定制器主文件
│   │   ├── settings.php      # 定制器设置
│   │   └── controls.php      # 定制器控件
│   │
│   ├── seo/                  # SEO功能
│   │   ├── meta-tags.php     # Meta标签
│   │   ├── schema.php        # Schema标记
│   │   ├── sitemap.php       # 站点地图
│   │   └── breadcrumbs.php   # 面包屑导航
│   │
│   ├── optimization/         # 性能优化
│   │   ├── cache.php        # 缓存功能
│   │   ├── minify.php       # 资源压缩
│   │   └── lazy-load.php    # 懒加载功能
│   │
│   └── template-tags.php     # 模板标签函数
│
├── template-parts/           # 模板部件
│   ├── content/             # 内容模板
│   │   ├── content.php      # 默认内容
│   │   ├── content-single.php # 文章内容
│   │   ├── content-page.php  # 页面内容
│   │   └── content-none.php  # 无内容
│   │
│   ├── header/              # 头部部件
│   │   ├── site-branding.php # 站点标识
│   │   ├── navigation.php    # 导航菜单
│   │   └── search-form.php   # 搜索表单
│   │
│   ├── footer/              # 底部部件
│   │   ├── site-info.php    # 站点信息
│   │   └── social-links.php # 社交链接
│   │
│   └── sidebar/             # 侧边栏部件
│       ├── sidebar-posts.php # 文章侧边栏
│       └── sidebar-pages.php # 页面侧边栏
│
└── languages/               # 语言文件目录
├── centlight.pot       # 翻译模板
├── zh_CN.po           # 简体中文翻译
└── zh_CN.mo           # 简体中文编译文件
## 5\. 主题选项
### 5.1 基础设置
1\. 站点标识
- LOGO上传
- Favicon设置
- 站点标题显示方式
2\. 布局设置
- 内容宽度
- 侧边栏位置
- 文章列表样式
3\. 颜色设置
- 主题色
- 文字颜色
- 链接颜色
- 背景色
### 5.2 SEO设置
1\. 基础SEO
- 首页标题格式
- 首页描述
- 首页关键词
2\. 文章SEO
- 标题格式
- 自动描述
- 关键词提取
3\. 高级设置
- Schema开关
- Sitemap配置
- Robots.txt设置
## 6\. 开发步骤
### 阶段一：基础框架搭建
#### 步骤1：创建基础主题文件
1\. 创建主题目录结构
2\. 创建必要的主题文件：
- style.css（主题信息）
- index.php（主页模板）
- functions.php（功能文件）
- header.php（头部模板）
- footer.php（底部模板）
3\. 编写基本的主题信息
4\. 测试主题是否可以在WordPress后台识别并启用
#### 步骤2：设置主题基础功能
1\. 在functions.php中添加主题支持
- 特色图片
- 自定义菜单
- HTML5支持
- 标题标签
2\. 注册主导航菜单
3\. 添加基础的主题设置
4\. 测试基础功能是否正常工作
#### 步骤3：构建基础页面结构
1\. 完善header.php
- DOCTYPE声明
- meta标签
- 主导航菜单位置
2\. 完善footer.php
- 版权信息
- wp_footer()调用
3\. 创建基础的index.php循环
4\. 测试页面结构是否完整
#### 步骤4：添加基础样式
1\. 创建assets目录结构
2\. 编写基础CSS样式
- 重置样式
- 排版样式
- 网格系统
3\. 正确加载样式文件
4\. 测试样式是否正确应用
### 阶段二：核心功能实现
#### 步骤5：实现文章列表
1\. 创建content.php模板
2\. 实现文章列表基本布局
3\. 添加文章meta信息显示
4\. 测试文章列表显示效果
#### 步骤6：实现文章详情页
1\. 创建single.php和content-single.php
2\. 实现文章详情页布局
3\. 添加文章导航
4\. 测试文章详情页功能
#### 步骤7：实现侧边栏
1\. 创建sidebar.php
2\. 注册侧边栏
3\. 添加默认小工具
4\. 测试侧边栏功能
#### 步骤8：实现评论系统
1\. 创建comments.php
2\. 设计评论表单
3\. 实现评论列表样式
4\. 测试评论功能
### 阶段三：响应式设计
#### 步骤9：添加响应式支持
1\. 添加viewport meta标签
2\. 创建响应式断点
3\. 实现移动端菜单
4\. 测试各种设备上的显示效果
#### 步骤10：优化移动端体验
1\. 调整移动端排版
2\. 优化触摸区域
3\. 实现移动端特定功能
4\. 测试移动端用户体验
### 阶段四：SEO优化
#### 步骤11：基础SEO实现
1\. 优化meta标签
2\. 实现面包屑导航
3\. 添加文章Schema标记
4\. 测试SEO基础功能
#### 步骤12：高级SEO功能
1\. 实现自定义标题结构
2\. 添加Open Graph标签
3\. 实现自动内部链接
4\. 测试SEO效果
### 阶段五：性能优化
#### 步骤13：基础性能优化
1\. 实现样式和脚本的按需加载
2\. 添加图片懒加载
3\. 优化资源加载顺序
4\. 测试加载性能
#### 步骤14：进阶性能优化
1\. 实现关键CSS内联
2\. 添加资源预加载
3\. 优化字体加载
4\. 测试优化效果
### 阶段六：功能完善
#### 步骤15：添加主题设置
1\. 实现主题自定义选项
2\. 添加颜色选择器
3\. 实现布局选项
4\. 测试主题设置功能
#### 步骤16：添加交互功能
1\. 实现文章点赞
2\. 添加分享功能
3\. 实现阅读量统计
4\. 测试交互功能
### 阶段七：最终优化
#### 步骤17：代码优化
1\. 检查并优化PHP代码
2\. 优化JavaScript代码
3\. 精简CSS代码
4\. 测试整体性能
#### 步骤18：兼容性测试
1\. 测试不同WordPress版本
2\. 测试不同PHP版本
3\. 测试主流浏览器
4\. 修复兼容性问题
## 7\. 性能指标要求
1\. 页面加载
- 首屏加载时间 < 2s
- 完全加载时间 < 3s
- 页面大小 < 1MB
2\. Google评分
- Mobile: > 90
- Desktop: > 95
3\. 核心指标
- FCP < 1.8s
- LCP < 2.5s
- CLS < 0.1
- FID < 100ms
```
项目一开始，我们就在本地机器或服务器上把 WordPress 环境搭好，专门在主题目录 theme 下新建一个独立的主题文件夹，随后用 Cursor 把这个文件夹打开。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4b2fcfab461a05c4848168f31c316302.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_576e99c9662aa3359d70edbc957e6fe9.png>
有了这一切就绪后，就依据产品经理梳理完成的 PRD 文档，让 Composer 领着做开发。Composer 的执行效率很高，严格按照清单逐项产出主题代码：
*   实现步骤1创建基础主题文件：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5a6d1f3340c3a275a671ca25913795a9.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7c4e5034669a28f0a8e8b648414d8243.png>
*   实现步骤2设置主题基础功能：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d8b7d12b844b00f84cfad15ebc7dac5a.png>
每完成一个开发节点，我们都会立刻切回 WordPress 前台做验证。起初 Composer 还没完全进入节奏，在生成完基础文件并启用主题后直接报错。
这份报错本可以直接丢给 Composer 让它自行排查修复。但我们这次换了个思路，调用擅长代码评审的 Chat 来做诊断和修复：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_093b76090beda586030e787bced8f806.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c384076e41b91edb8ebbd18550138f79.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6a11e7707a5300b57480081ec8dd3ee4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f1f8072cfbb9dd1dde89e076e8023a73.png>
没过多久，Chat 就把问题修好了。我们把修复结果同步给 Composer，示意它接着推进下一步：
*   实现步骤3构建基础页面结构：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9d4399987e09413e1b63a28b29a3c4a4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cb73593340fffc18824f3b6e683b2747.png>
从这里开始，Composer 明显进入了高效状态，一口气把后续多个功能点都实现了，且自测阶段未出现明显问题：
*   实现步骤4添加基础样式：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7d79dade05ca71a0401969fb2a71a653.png>
*   实现步骤5实现文章列表：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c6bdd017c40625700c16c4c73194e581.png>
*   实现步骤6实现文章详情页：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ce3bb4df9ea307ec0d2cf87dfd33819a.png>
*   实现步骤7实现侧边栏：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_980575117b4739a2f82fa5ce87497e4b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f372221ddc17323b22fb2c1d034ca9ce.png>
*   实现步骤8实现评论系统：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1dc89b4b923426d3fd2e5c68d07c8ee8.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b10639bcd3ff4e6a88c02f41b8b64846.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4ba8ea295afa312ef11a626e10df1ef2.png>
*   实现步骤9添加响应式支持和步骤10优化移动端体验：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3e40f798b698778db7098ac248f58184.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcf6393e991a45f09484dd4fca3f4e04.png>
这套WordPress主题模板，是我让多个AI角色合力“打磨”出来的。最开始，Composer根据需求把主题的基础模块搭了起来；不过走到第十个步骤时，新的麻烦又出现了。按照惯例，我还是把这些问题丢给Chat去处理：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e830b1a08793fa0e8d3aaa9c57d3344c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ff5b7cfb5d4b8af60d3361168934197b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_41677630263b352582ed4286bf72eb80.png>
结果这一回，Chat改完之后并没有收干净，反而又冒出了别的报错：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2eefc2ed27dd0f6570dd679f5cffdcaf.png>
可问题还得继续解决，于是我把最新提示复制下来，再次交给Chat：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2fbff21a43999c5229b9e1c2906d090e.png>
就这样和这位“代码审查专家”来回拉扯了好几轮，问题才算彻底消除，主题雏形也终于立住了：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dc87f9c9486fcef2931c8b4d6cb39169.png>
之后，我把Chat修复后的代码结果同步给了Composer：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_725112be0907ecff79fbd6587a33071d.png>
接着让Composer核对一下当前进度：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_079b67841569bb36c2ecabd680106d21.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5c3647bccbcfcc5414e601df13cbe0f1.png>
再往后，Composer继续照着需求文档的开发步骤生成代码，一旦遇到报错或功能异常，依然由Chat负责审查和修复。必须说，这趟旅程并没有想象中那么丝滑，Cursor也远没有部分博主吹得那么神。当项目代码量持续增加，我绝大部分精力都花在跟Chat反复交底、同步思路、定位问题上，这种感觉几乎和我日常用ChatGPT写代码如出一辙。期间，前面总结的几个思路也被反复拿出来用，尤其是“思路二：引导调试并自检问题”“思路五：指定代码并限定范围”和“思路六：做好备份并适时回退”。
到这一步，主题的核心功能算是基本齐了。布局有列表、网格、大图三种；侧边栏覆盖默认、左侧、右侧、无侧边栏、宽屏五种；文章阅读进度条、一键返回顶部、图片懒加载、网站明暗色切换、SEO标题设置等也都一一落地：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7b56a12a811bbc86e2e387daf08c0d30.png>
此时，我动了优化UI的念头，自然要请出UI设计专家：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3260980d16ccbb2895f5dda2e349f361.png>
偏偏主题的样式主文件 main.css 已膨胀到近2000行，让UI设计专家直接在这么大的文件里做全局改动，确实有些施展不开。后来我只好先用ChatGPT的o1把main.css整体合并整理了一遍，压缩了几百行冗余代码，给后续优化腾出空间。这件事也让我实实在在体会到“思路九：配合其它AI工具辅助Cursor编程”的价值——有些活儿Cursor做起来别扭，不妨交给更偏底层的ChatGPT或Claude，处理完之后再把代码拿回Cursor项目里。等到障碍扫清，UI设计专家重新上手优化样式：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cdd637c20cf1551e8f92d89332d8b480.png>
另外，角色分工真的不必太死板。这套主题中有不少样式代码，其实是由“代码审查专家”Chat生成的；同样，遇到代码问题也别一股脑全丢给Chat，适当分一些给Composer反而效果更好，毕竟Composer手头就有相关上下文，有时能更直接地定位问题。当然，如果问题需要多轮对话才能掰扯清楚，那还是“代码审查专家”Chat更合适。
### 多AI协作，怎样给项目做迭代？
目前Composer按需求文档产出的模板还比较朴素，功能覆盖也不算全。比如JustNews可以给每个分类或标签单独设置布局，我也想在自己的模板里加上类似能力。这样的迭代该怎么做？我选择先把“产品经理”Chat请回来，听听它的建议：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7e978488753fbb15acc45a44b89160a4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8b884b463b5b471605a2f00cfacd4f66.png>
顺着实际需要，我和这位产品经理反复讨论，最终敲定要增补的需求清单，并请它把新增需求和对应开发步骤写回根目录的 readme.md 需求文档里：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_46e27032f86bb906ffaf44e5c691fc1a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3369fea6b93b53df95806b276dffff43.png>
接下来，Composer重新投入工作。我先让它对照最新版需求文档检查当前进度：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bc89f53955ccb679a1c8f1e2f6030969.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a7bbf0a401b84bbb622d6087eac9da20.png>
再让它着手生成新增功能的代码：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_145ca1f63b8a0fffed2b8c8ef451537c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_46446a96bc065ded6660dbf41ca83f39.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b3887195ddba8786c4a913d33c624e4e.png>
代码生成后，照旧到WordPress网站端做实测；发现异常，就再让Chat以代码审查专家身份介入修复：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_14a4685c31a31c2f41356efc2dd7c097.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e3ca0a4a8b46403e6178413f8f0c1009.png>
老实说，整个迭代过程并不算顺。因为从始至终我基本不细看Cursor生成的代码，完全把自己当成一个编程小白，所以在开发中不得不反复回退代码、反复指定涉及的文件，最后才换来Cursor把问题搞定。
核心功能就绪后，我试着搭了一个测试网站。装好并启用模板后，还需要配合Kadence Blocks这个Gutenberg插件来定制页面内容和框架。这个灵感来自我使用过的轻量级主题Air Light：这类主题通常更专注SEO，代码和功能尽量精简，因此页面层面的定制就交给第三方插件去完成。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_69170290360998b9baa4a502d9639e07.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2b6d72948cf31caa914ff36a316b78bd.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c6626a1dfa5fd9882fbaf2495d439a3c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_02cc2e8e544e61e20d80ed8f83b785ad.png>
眼下的模板离“完善”还有不小距离：字体样式需要支持灵活设置，菜单要多层级，最好还能预置几套不同风格；这些后续都会继续交给Cursor迭代。
### 九条Cursor编程心得
回顾这次实战，我把最常用的经验浓缩成九条思路：
*   思路一：预设方案并分步输出。先把需求拆解成足够小的步骤，并准备好对应的开发方案，存到项目根目录，再让Cursor按这个脚本慢慢推进。入口越小、步骤越细，越不容易跑偏。
*   思路二：引导调试并自检问题。程序报错时，把现象和提示原样交给Cursor；若几轮对话都不能解决，就让它加一些跟踪日志，把运行结果或调试信息再反馈过去，引导它自行定位并修复。
*   思路三：细化功能并分步输出。复杂功能别指望一次成型。先和AI把方案聊透，再拆细成多个小步骤，每一次只生成一小段代码。如果每步都能测试并反馈，最终效果会靠谱很多。
*   思路四：善用经验并做明确引导。如果你懂项目逻辑，就应该由你给Cursor指方向，而不是被动等它带你走。项目越复杂，上下文限制对Cursor的约束越明显，这时引导Cursor做编程，而不是被Cursor带着走，才更有利于项目推进。
*   思路五：指定代码并限定范围。让Composer或Chat动手前，尽量把相关代码完整贴过去，限定它只在你圈定的范围内修改，这样能最大限度减少上下文干扰。
*   思路六：做好备份并适时回退。没有版本管理，就在每个关键节点手动备份。一个问题聊了很多轮仍无解时，继续硬聊大概率会在错误方向上越走越远；不如退回上一个正常版本，在原有对话位置重新编辑提问，按已经确认的思路重新引导。
*   思路七：先沟通清楚再做开发。写不出预期代码，往往不是AI能力不行，而是我们没说清。这也是为什么对需求敏感的产品经理和逻辑清晰程序员，在AI时代反而更有优势——他们知道怎么把问题描述到位。与其急着让它出码，不如先就功能目标和会涉及到的文件、代码聊清楚，等共识达成后再让它登场。
*   思路八：多个AI相互协作结伴编程。通过Composer和Chat提前布置好多个角色，各管一摊，从不同视角交叉验证、互相补位，很多单点难题会被拆解成协作问题。
*   思路九：配合其它AI工具辅助Cursor编程。遇到Cursor搞不定的场景，可以求助更原生的ChatGPT或Claude，处理完再把代码收回项目中。随着模型能力的提升，这类联动也会越来越高效。
### 写在最后
从2022年底ChatGPT第一次站到大众面前起，就有朋友为技术人员的前途忧虑。我起初并不以为然，但也没有真的掉以轻心，而是试着把它当成自己的搭档，做出了一些以前很难独立完成的小产品。Cursor出现后，编程门槛被进一步降低，连不少非技术背景的圈友也开始用它写产品。
但亲身试过以后，我越来越确信：用Cursor去做一个有一定复杂度、一定代码量的项目，你还是要有编程的基本常识，并通过合理思路和既有经验去引导它，而不是全程躺平。航海在即，很期待继续和各位圈友一起探索Cursor编程，把我们脑海里的产品一个个造出来。祝大家长风破浪，龙哥盟。
### 附录
**附录I：通过ChatGPT整理时间块小程序的需求文档和开发步骤**
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_19a465a9c4902c355ecfc4691614bc4a.png>
**附录II：Cursor的产品经理(Chat)整理WordPress主题模板的需求文档和开发步骤**
1、让Cursor的Chat扮演产品经理，整理需求文档、开发步骤和文件结构：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e1a57aee30b3e7550434853c3b6a9b4a.png>
2、联网学习JustNews主题模板的功能：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2a1fec4cf36ebfc036ae7247dd3532ce.png>
3、罗列JustNews主题模板的功能列表：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7c1ccf0598ddde17fd880d0d44c826b5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dc3e886ad49d41a4ac20b1e3c23acca0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0a1a10ea8168e4beb179fb45e9dc376f.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f98b09076e94596c2bb6163e252b4eb1.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a23c5c33354b2aaff8f4927aa2f1d3be.png>
4、提取JustNews主题模板的核心功能：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d585a563e55965376a88b1877c4c592f.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4af56064bd08d668e8e30700094ee985.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e3904394f23f80c64e2b9ba9bbc824bf.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7e102536a23b4c9eb29bf35d6978783c.png>
5、把提取的核心功能整理成需求文档：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9f4ffe90af5f2c48b3ebfcb13c2474f6.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4f3e3615852a35e8381ca8cf791a1813.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4f9cc17f40b7cdb852b8b7a794eb5298.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b0aedd56a9d36105a1a5a44af8cbf865.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1133b6ab1885aa4837bf1e62f87d4459.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ee77326e2c0b463fe5759a97f2cb149a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ff81241d6d873c1acad3fe53fc5fea9c.png>
6、把需求文档保存到项目根目录：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1fe186e36c08c1910b307d7da49a4f27.png>
7、细化需求文档中的开发步骤：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4e2291f1ee99d8ab159c11302498a988.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1e4b366d490e06a5483490025b415457.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_84578344b88228b1c57e314dd8fac87b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_517f49a68c44b7867cb02f5f0d112d36.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_40ff65c1e7567bb1d4aadb900c6d5b1c.png>
8、更新细化的开发步骤到需求文档：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_44f9fb05f795ab317bb0cd6373b8f0f4.png>
9、重新梳理项目的文件结构：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_51785ec61873b455cd70b6181a971a4e.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d5abce17dd47cb8d3fbcfad4697c98e.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_03dd3f6b8d8fe6912edb1b523ef00921.png>
10、更新最新的文件结构到需求文档：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c92e5c4b526274b8cf4549923acd81e6.png>
**附录III：和Cursor一起探讨Composer和Chat的编程能力**
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b6bb5b7e6bd77391b0898381026565f3.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bdbf14d2903acbe987bdbb25ab1f9865.png>