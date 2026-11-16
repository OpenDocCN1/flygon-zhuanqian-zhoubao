# Claude Code 指挥 n8n：我把小红书做成了一座像素农场
作者：龙哥

> 转自飞书笔记

志辉，十年数据架构背景，现在一头扎进 AI 编码这件事里。

我想在这条路上带更多人把脑中的点子变成现实，也盼着同路人多一些思想碰撞。

最近 Claude Code 在我手里几乎是万能的，主业副业都绕不开它。

用它折腾出过不少半成品，也有几个项目真的跑通了。我同时也在摸索 AI 开发的最优解法。

Agent 概念正热，但我之前搭过一个“抓 X 推文→自动写稿”的流水线，过程相当折磨。

当时就想：能不能换个思路，由 Claude Code 直接负责 n8n 的流程设计？

试了一轮，效果惊艳。它写出来的流程比我手动配的更靠谱。

所以有了这篇帖子。我坚信 Claude Code 与 n8n 组合起来，后面能量会更大。

# 先感受一下

上视频，直接体验这套组合的魔力。

想给账号做对标、定时发文、持续追踪某类达人动态的话，这套方案能给你巨大的想象空间。

它不止能服务小红书，任何“采集→加工→输出”的场景都可以往里套，灵活、快速。

目前闭环里已经能实现这些事：

1、一键抓取同类目达人号的全部笔记和个人资料，之后想怎么用都有空间。

2、n8n 流水线自动接手，清洗数据、写入数据库，同时调用 AI 为达人生成专属分析报告。

3、像素土豆系统把数据重新可视化，任意形态展示，我选了像素风；还能模仿达人写文，以及配图生成。

# 整体架构

![](img/zhuanqian_8d70e923771ce6f67cc3c8dccf09bd01.png)

整个方案其实只有三大块：

1. Chrome 扩展：嵌在 Chrome 内的采集端，负责抓取达人昵称、IP 属地、关注数、收藏/点赞数，以及每篇笔记的标题、描述、喜欢数、收藏数和评论。

2. n8n 流程：云端中转站，收到扩展推送的数据后先做清洗，再按表写入数据库，同时调用大模型产出达人档案。

3. 像素土豆系统：展示端，读取库中数据做任意可视化，我这里做成了像素风格，还支持仿写和生图。

接下来逐个拆解，讲讲它们是怎么落地的。

# 名词扫盲

这三个概念如果熟，可以跳过这一段直接看后面。

### Claude Code

AI 写代码目前的 S 级选手，我至今没见过能打的。

它已经变成我工作和生活里的标配。终端足够轻，很多场景都能直接用；对各种编程语言、IDE 的兼容性也很好，能顺畅嵌入现有开发方式。

它的 tool 调用能力很强，靠这一点，大项目也能放心改。

再加上 Claude 大模型本身的文字功底，我写稿、写周报也常找它帮忙。

一句话：一套工具走天下。

### n8n

玩过 Coze 和 Dify 的朋友应该不陌生，它们是可视化流程编排平台，也支持私有化部署。

n8n 和它们放在一起，我的感受是：开放程度更高，接海外服务尤其顺手。

比如我以前搭过一条 X 数据自动采集 + 按文风推送热点稿的链路。

![](img/zhuanqian_2fcf1b8b982ac2de793eed75b5fa568d.png)

再配上 Claude Code 辅助，学习成本立刻降下来。

由 Claude Code 先把需求拆清楚，再生成流程，n8n 的搭建速度快很多。

### 爬虫采集

老话重提。

先说合规：一定严格遵循 robots.txt 规则。

所谓爬虫，核心就是从页面里取数据，要么解析 HTML 源码，要么拿到后端接口返回的内容。

实现手段非常多：RPA、现成采集工具、用 XPath 或 CSS 直接抓元素，都能做。

我这次选择 XPath，理由是浏览器开发者工具能直接展示元素位置，快速定位非常方便。

```
//div[@class="user-name"]/text()
```

![](img/zhuanqian_bf92b6f5c8d692b262ceec1b95ff484a.png)

而且现在 AI 工具演进很快，Playwright MCP 这类浏览器控制方案也能承担抓取工作。

这块讲得有点干，不看也不影响后面的主线。有兴趣可以回头再啃。

# 我的三线作战姿势

因为要同时开发三块，我直接采用终端多屏模式。

macOS 用户很幸福：cmd+d 竖切、cmd+shift+d 横切，几乎所有终端都支持。

我当前用的是 Ghostty，轻、快、不碍事。

Windows 用户可以试试 Warp，否则就老实开多个终端窗口。

布局如下：

*   左：Chrome 扩展开发

*   中：n8n 流程开发——注意，这套流程是 Claude Code 写出来的，我这种小白只是把要求写清楚

*   右：像素土豆系统开发

![](img/zhuanqian_5bc1dcb8e138a628e58c265116a2249b.png)

单枪匹马按住三台 AI“牛马”，成就感直接拉满，我也算当上老板和监工了。

![](img/zhuanqian_62cb1c854c635e191b68998ab3279efd.png)

放张图应景，图中这位是作者自己。

1、2、3 就位，开工。

等到一天结束，烧掉 200 多美金，三台 AI 真把整套系统给我蹬出来了。

![](img/zhuanqian_517860f6375622b5c9f49811af571b66.png)

复盘一句话：编码全靠 Claude Code 干，我只负责提要求。

方案：我的是官方 200 美金套餐，偶尔也用多人合租、镜像代理、API 调用。

我不喜欢做选择，能用的方式全掺一脚。

# 这套方案强在哪

市面上一堆内容平台抓取工具，为什么我要自己搞一套？

1、采集层可插拔：扩展现在用 XPath，兼顾速度与合规，也预留了反爬策略调整空间，它只专心抓数据。

2、流程层负责脏活：数据清洗入库，生成 AI 分析结论，目前库用的 Supabase。

3、展示层够灵活：这个平台里的数据怎么呈现都随你，仿写文章、生成图片都能干。

一句话总结：让每个工具干自己最擅长的事。

- 替换成本低：数据躺在自己库里，哪天看腻了像素土豆，随时可以另做一个前端。

- 生产效率高：XPath 精准捞数据 → n8n 直接落库 → AI 节点即插即用，整条链路非常顺。

- 业务适配强：完全定制化，能顶住各种复杂业务需求。

不吹了，直接上干货。

# 模块一：数据抓取（小红书）

这部分其实就是 Chrome 扩展怎么落地。

要完成的活有三件：

1. 梳理小红书页面里合适的 XPath。

2. 写出 Chrome 扩展。

3. 让扩展与 n8n 完成对接。

## Step 1：准备环境

### 1、找一套脚手架

开发扩展时我直接用了成熟模板，免得 Claude Code 完全自由发挥，这样能减少幻觉。

模板选了 GitHub 上一个知名的开源方案，React + Vite 技术栈。

克隆到本地后重命名，当作新项目起点。

```
git clone https://github.com/Jonghakseo/chrome-extension-boilerplate-react-vite xiaohongshu-n8n-chrome-extension
```

### 2、初始化项目记忆

敲一下 init 指令，生成第一版记忆文件。提示词如下：

```
/init 使用中文，ultrathink
```

![](img/zhuanqian_7d9806676b6b8cb89f84e5ceb1b6f040.png)

执行完，项目根目录会多一个 CLAUDE.md。

![](img/zhuanqian_da858a0852486d36a4c005a770881419.png)

它的价值在于：后续 Claude Code 每次开工，都能快速明白“这是什么项目、什么架构、代码写在哪、如何运行和打包”，不至于瞎猜。

## Step 2：抓取小技巧

### 1、XPath 怎么写

想弄懂 XPath，先得知道一点 HTML。

网页里看到的信息，最终都来自 HTML 结构。比如：

```
文章标题
这是正文内容
点击查看更多
# 爬虫入门
作者：龙哥
2025-08-21
[阅读全文](/detail/123)
```

浏览器渲染出来是这样的：

![](img/zhuanqian_8ad2cd4ccfa053acbd14ec675543721a.png)

XPath 是一种路径语言，在 HTML 当中查找元素，就跟用文件夹路径找文件一样。

我想取「Python 爬虫课」「作者：龙哥」「2025-08-21」「/detail/123」，直接这样写：

```
标题：//div[@class="article"]/h1/text() → 爬虫入门
作者：//p[@class="author"]/text() → 作者：龙哥
时间：//p[@class="time"]/text() → 2025-08-21
链接：//div[@class="article"]/a/@href → /detail/123
```

XPath 算是爬虫圈的老手艺，以前我能背出各种语法，现在基本忘光，全靠 AI 帮我捡回来。

![](img/zhuanqian_d6d4d9ce3acc74c4396b21ee672cf2b0.png)

做法很简单：把 HTML 贴给 GPT，问“这个值怎么取”，它就把表达式吐出来了。

### 2、在浏览器中验证 XPath

表达式写好后，不用急着写代码。

打开 Chrome 开发者工具（F12），切到 Elements 标签，用搜索框直接搜 XPath，就能确认结果。

这是当时验证达人名称的截图：

![](img/zhuanqian_447c06ab7a73cad904fceaabf5cd4ee5.png)

![](img/zhuanqian_0abfff89ccea2dc4a0839078acdb7792.png)

![](img/zhuanqian_a4ed9f09a95788d834e9d253e097da50.png)

文章列表的验证也类似，让 GPT 帮我推表达式，一次搜出 16 个节点。

![](img/zhuanqian_6b685eaec19758fe1176cadee531df94.png)

![](img/zhuanqian_3d85198c00b62e8cf307d7d09a5d4bf1.png)

## Step 3：写需求文档

XPath 理清后，就能把需求文档整理出来。

我事先把需要用到的 XPath 都写进了文档，这次只是重新梳理、补全功能点。

![](img/zhuanqian_36c02ec82e87bc2552c34486d337e47c.png)

PRD 文件放在项目的 docs 文件夹下。

文档也公开出来：

```
docs/prd.md
```

![](img/zhuanqian_8cb345301a9981b8d60a7146e0293e1b.png)

## Step 4：出实施方案

这一步进入真正的设计环节。

打开 Claude Code，切到规划模式（plan）：shift+tab 按两下；Windows 用户可能需要 alt+m。

```
@docs/prd.md 这个是小红书数据采集的浏览器插件的详细需求，仔细阅读，并给出详细的规划方案，ultrathink
```

![](img/zhuanqian_c4f7d3ebd6899a9b78f4591dd4f638d3.png)

![](img/zhuanqian_ccc8e07f5e2e97a642880f5422b006a1.png)

Claude Code 给出的方案，我会另存为 Markdown，方便后续审阅。

```
保存到@docs/目录下，文件名称格式是PLAN_20250819_001.md格式。
```

![](img/zhuanqian_038e4972abbcbac8b19b2946975dda21.png)

看完初稿，我觉得有些地方还不够，就继续在规划模式里和它磨细节。

```
@docs/prd.md 我后面加了“反爬虫“的要求，再重新阅读下需求和现在的方案，另外就是爬取数据的准确性上再看看，ultrathink
```

![](img/zhuanqian_58de2414b57a6215ca29d9bfb9b2b08a.png)

让它把方案刷新一下，文档版本升到 2.0。

![](img/zhuanqian_84b9b1c22dff2d0401b9502e354b7fe9.png)

实施方案全文如下：

## Step 5：放手执行

如果前面聊得足够细，这一步基本就是看着它跑。

我先用规划模式把执行计划定下来，然后开启跳过权限检查的免打扰模式，让它一口气往前冲。

```
@docs/ 根据这个目录下的文档，开始写这个项目，ultrathink
```

![](img/zhuanqian_81975d37342456335590ece5c9ce663b.png)

## Step 6：修 bug

跑得快，问题也会跟着来。这很正常，关键是带着 Claude Code 一起分析、解决。

下面是我实战中遇到的几个典型问题，当作排查思路分享。

### 坑 1：抓取类任务被判定为敏感操作

界面飘红，还给了策略提示。我猜是 Anthropic 对这类抓取任务有限制。

![](img/zhuanqian_0077caf94a8c694abd906fe3eb485a33.png)

解决方式很简单：换一种话术描述目标，让 AI 从一个合规的角度去实现；一次不行，后面多试几次。

### 坑 2：取不到数据

```
页面检测结果: {isValid: false, url: 'https://www.xiaohongshu.com/user/profile/68497faa0…7HFRUObas-vCl_PSLHKnTLshQwak=&xsec_source=pc_feed', userId:   null, message: '请访问小红书个人主页（格式：https://www.xiaohongshu.com/user/profile/xxx）'}，页面已经检测倒是 https://www.xiaohongshu.com/user/profile/ 开头的格式，但是还是“页面不可采集“的术语，并且布局不太合理，[Image #1]
```

![](img/zhuanqian_5af5d8986e2158123bc675bcb04d1bcd.png)

### 坑 3：popup 界面布局乱了

![](img/zhuanqian_99686d320a5c005616a45a861d350944.png)

### 坑 4：侧栏弹不出来

![](img/zhuanqian_7815af741db15f264a41670255916418.png)

### 坑 5：抓到的信息缺字段

![](img/zhuanqian_f0d91a3bc53e10ee528250b0270ece92.png)

### ✅ 成果：达人数据成功入表

![](img/zhuanqian_273db148111b2724f42ce5240ba6fed7.png)

### 坑 6：笔记抓取不完整

```
采集文章的数据，需要点击每个打开后才能采集到标题、正文这些元素的。ultrathink
```

中途改了很多策略，最终整个流程才算跑顺。

```
采集策略，先不滚动页面，等采集完用户数据后才开始采集文章数据，默认进来就会有一些文章，先采集已经在页面上的文章数据，需要有鼠标点击打开文章的操作，然后再采集文章的要素，比如标题、正文、评论等，ultrathink，补充信息，正常人点击的是 class="note-item" 下的class="cover" 的a标签
```

![](img/zhuanqian_f7ca39a004f13054a5ecb24c94cfef9c.png)

### 结果查看：数据终于跑出来了

![](img/zhuanqian_9b643aea0f09a6b1b34a5da1609547a9.png)

抓取到的完整数据一览：

![](img/zhuanqian_91507bcde6496655e96a0c33a5d4c1f1.png)

支持一键导出 json 格式

## 步骤七：把 n8n 的配置同步过来

要走到这一步，前提是 n8n 的工作流已经搭好。

为了方便验证接口，我先用 APIFox 来调试前面抓到的那些数据。

https://apifox.com/

这是一款 http 接口调试工具，对新手来说门槛有点高。

可以让 AI 来解释：http 到底是什么，接口又是什么？我是个小白，别人用 APIFox 一般做什么？

![](img/zhuanqian_95133dab3de68004684066147c0b86d9.png)

等接口调试通了，就能把代码拷贝出来，让 claude code 知道请求参数长什么样、响应体长什么样。

这样就不会因为参数对不上而反复返工。

当然也可以整理一份接口文档，但这里只有一个接口，我就直接把内容粘到对话框的提示词里了。

```
同步n8n接口数据的参考代码为：{粘贴刚刚复制的 APIfox 代码}
```

![](img/zhuanqian_c479fe7314789d6f5c18c6c3501679ed.png)

返回数据的格式示例：

```
{
"success": true,
"message": "✅ 数据保存成功",
"errors": [],
"details": {
"authorSaved": true,
"notesSaved": 114,
"totalProcessed": 115
},
"timestamp": "2025-08-20T09:30:24.997Z"
}
```

![](img/zhuanqian_526317053d383bf14fe4d65714a8f6f4.png)

接下来继续校对返回接口的数据结构：

![](img/zhuanqian_771f70fbc363356863b5fdd15f8bdac5.png)

![](img/zhuanqian_71f8483b989d8591f339bd7777e96511.png)

## 步骤八：交互体验的修复与同步优化

这一块主要是在采集数据的同步上做体验增强和优化。

```
[Image #1]，每次采集都会新增一个记录，我理解是不是只同步每次最新的那个就行，还是说每个采集的记录都可以有同步的按钮操作，深度思考下这个交互怎么好做。ultrathink
```

![](img/zhuanqian_68c9ce41324ba522b08584418474674c.png)

## 步骤九：界面原型开发时遇到的坑

下面这张图说的是一个界面排版的问题。

这个问题我其实折腾了很久，反复改了好几次。

![](img/zhuanqian_45ad36c5e0d48633f2e0e7073a011ee1.png)

```
[Image #1]，看这个布局，使用ascii复现给我画出来，我好确认你已经知道我的问题
```

这里有个小技巧可以避开纯布局上的纠结，让 claude code 直接用 ascii 画出来。

一方面能确认它是否真的理解你的需求，另一方面也能验证它是否找到了可行解。

![](img/zhuanqian_91e29c7e03fa555a33a93f9d1ffdc07c.png)

要是没解决，就继续

加上 ultrathink

```
实际“采集数据“，“查看已采集数据“ 两个按钮还是太长，看是否可以做成自动适应父容器的，离父容器有个padding的距离。ultrathink
```

![](img/zhuanqian_a3d2c3b168b95599f00c930354ea1df1.png)

## 步骤十：插件调试实操

打开 Chrome 浏览器

![](img/zhuanqian_1b2552225cf750d6d17e2293f9778db8.png)

一定要开启开发者模式

![](img/zhuanqian_cd1139690978ad0d0c02d94fe1487346.png)

打开后左侧会出现三个控制按钮

![](img/zhuanqian_488d76dc2ec07e13e17509f8e4b42e1b.png)

选择加载目录。

通常在项目目录的 dist 文件夹下。

![](img/zhuanqian_5370a517e39426781df2f6aa2e5c974a.png)

记得把浏览器插件置顶，就能看到了。

![](img/zhuanqian_0d6b2ffbd6db2eb993af23200c98c4ea.png)

调试思路：

![](img/zhuanqian_f00aeb3f7b09f3e55d0b44aee266fa7e.png)

想看网络请求的话，切到 network 面板

![](img/zhuanqian_e45a60066cd5f6b52f92d1b481ec1515.png)

## 最后的小结

到这里浏览器端的开发基本就收尾了

过程里确实需要一些基础储备，比如 xpath 表达式、http 接口、F12 调试面板。

还有一个办法，如果自己搞不定，就找个能搞定的来帮忙。

# 第二部分：n8n agent 的开发

这里开始才是重头戏，也是整篇文章最精彩的部分。

建议泡壶茶，慢慢看。

整体就围绕这几个核心

1、n8n 的全部工作流都是靠 claude code 生成的，我一个没手动配过

2、接入大模型，自动生成个性化的博主分析报告

3、所有数据最终落库到 supabase 数据库里

## 步骤一：先准备建表

数据要落库，就得先建表。

这一步对小白不太友好，涉及后端数据库的概念和建表语法。

不懂就问 AI，现在最关键的能力就是学习能力。

### 1、建表的具体需求

提示词如下：

![](img/zhuanqian_8e8a97861eb054884026ac1dabcdac57.png)

核心是把 json 的数据结构，文章相关的和博主相关的都贴进提示词里。

这样 claude code 才能精准推导出建表语句。

```
{这里粘贴 json 的数据格式数据}
上面的数据是小红书的笔记和作者的数据，我希望有2个 supabase 的表来存储，分别是作者列表，以及笔记列表。
其他要求如下：
- 笔记列表就是保存对应的笔记数据，同时需要有一个作者id的字段能够联系起来。
- 作者表需要额外添加一个 report 字段
- 表不需要外键约束
- 暂时不需要 RLS 策略
请你给到我在supabase中创建这两个表的SQL语句，保存到 @supabase.sql 文件中
```

### 2、在 supabase 里创建存储表

这一步就是让 claude code 输出 sql 建表语句。

```
@prd_ddl.md 根据文件中的描述，生成所需要的sql内容
```

![](img/zhuanqian_497efa6399c7b5a9eb023eccfb9b28cd.png)

生成了 sql 文件

![](img/zhuanqian_f144744b1ddd95402d15f06b12b31caa.png)

在 supabase 中执行 sql

![](img/zhuanqian_afacbc4bb27ce2a8ea981dbb3bda0979.png)

这里涉及到 supabase 的概念。

简单说它就是一套云数据库，功能集成度很高。

现在做站基本都离不开 supabase 了。

它也是本系统里最核心的组件之一。

相当于电脑的硬盘，存放着从小红书采集回来的全部数据。

后续系统的数据读取也都从这里来。

它是整个系统的粮仓，绝对不能出问题。

supabase 上手很快，注册后新建一个项目就能用。

## 步骤二：n8n 工作流 json 的开发

！！！重点！！！重点！！！重点！！！

来了来了。

这里讲怎么用 claude code 开发 n8n 工作流，主要有两种做法

方式一：直接生成 n8n 的 json 配置

方式二：用 n8n mcp 来修改工作流配置

少废话，直接上。

### 1、搭建 n8n mcp 环境

很简单，启动 mcp 服务即可

参考：https://github.com/czlonkowski/n8n-mcp

前提是装好 nodejs。

```
npx n8n-mcp
```

然后在项目根目录新建 .mcp.json 文件，配置如下

```
{
"mcpServers": {
"n8n-mcp": {
"command": "npx",
"args": ["n8n-mcp"],
"env": {
"MCP_MODE": "stdio",
"LOG_LEVEL": "error",
"DISABLE_CONSOLE_OUTPUT": "true",
"N8N_API_URL": "你的n8n 地址",
"N8N_API_KEY": "你的 n8n key 配置"
}
}
}
}
```

N8N_API_URL：你的 n8n 地址，例如：https://xxx.xxx.xxx/。就是你访问 n8n 的地址。

N8N_API_KEY：你的 n8n API Key。

在 n8n 设置页的「n8n API」菜单里可以生成。

其实不填这两个参数也能生成 json 工作流文件，配置主要是为了

![](img/zhuanqian_66664eb5b7ed971fe1eb0af79768ca00.png)

补充一下 n8n 的部署方式有很多。

大部分人本地用 docker 跑，我看过龙哥的文档，写的很细。

我自己有云服务器，用的是 zeabur 的模板部署，环境几分钟就起来了。

## 步骤三：写需求文档

又回到写文档这一步，所以现在的开发流程并没有变简单，对个人的要求反而更高了。

我发现自己写代码越来越顺，写需求文档的时间却越来越多。

### 1、n8n 工作流的需求文档

![](img/zhuanqian_3e98f7900cedd998bba1f330e51bc645.png)

关键点总结：

1、输出的是 n8n json 文件

2、触发方式用 webhook

3、调用大模型生成博主的个性化报告

4、把结果保存到数据库

```
帮我编写一个n8n的agent的对应的json文件，这个agent的要求如下：
1\. 能够以webhook的方式触发，POST请求，接受的数据的结构示例如下，这其实是一份小红书中获取到的创作者的相关数据，包含作者信息和笔记信息，@data.json
2\. AI Agent接收到这个数据之后，能够根据数据中的信息，分析出这个用户的一些特征，并生成一个创作者的分析报告，报告要包含以下的主题：数据概览、赛道分析、标题风格分析、笔记风格分析、热门笔记分析。把分析的报告保存到`report`字段中
3\. AI Agent分析完成后，需要解析对应的数据，并且分别把数据保存到对应的表中，分别有两个表，`xiaohongshu_authors` 表和 `xiaohongshu_notes` 表，分别对应作者列表和笔记列表，结构见文件 @supabase.sql
4\. 2个数据保存成功后，能够返回一个true，如果保存失败，返回false
其他要求：
1\. ChatModel 选择 OpenRouter，模型使用 deepseek
2\. 报告应该体现专业性
3\. AI Agent 的 prompt 要求能够完成我们上述的要求
```

这份需求文档参考了 yihui 大佬的做法，在此感谢。

### 2、用 claude code 开发 json 工作流

直接 @ 需求文档，让 claude code 开始干活。

```
@prd_n8n.md 根据这个文档的需求，并使用 n8n-mcp 生成对应的n8n的配置json文件，ultrathink
```

注意：前期我都用 plan 模式，并且加了 ultrathink。

![](img/zhuanqian_bbbf4edb78e838ea69114285b73fde05.png)

得到执行计划

![](img/zhuanqian_533bd7f066bb35381e26db3b99741f8e.png)

能看到每个节点都列出来了。

生成时每个节点都会通过 n8n mcp 拉取详细配置。

这样 claude code 就清楚每个节点该怎么写配置。

尤其是涉及数据处理的地方，会用代码节点，而写代码正是 claude code 的强项。

开发完后成功生成了 json 配置文件

![](img/zhuanqian_8d5b45e66a7431813701e24a04b538bd.png)

说实话我当时还有点怀疑，这个 json 到底能不能用？

那就试试看

### 3、把 json 导入到 n8n 工作流

新建一个 n8n 项目。

点右上角三个点，选择导入文件。

![](img/zhuanqian_b4ddcceb191db2f4597721c80f558d93.png)

选我们刚生成的 json 文件即可。

### 4、配置 AI KEY 和相关信息

可以看到导入后的界面。当时我挺惊讶的，我什么都没手动配，光写了个需求文档，导入后居然长得像模像样。

目前已经能证明 claude code + n8n 的组合是可行的。

![](img/zhuanqian_3c39ccd40deb3506fbe442a52b0c9547.png)

不过有几个节点显示红色叉叉，正常，是需要补充 openrouter 和 supabase 的配置。

1、openrouter 很简单，填 API KEY 就行

2、supabase 的信息

![](img/zhuanqian_41754920990cccb1d3aad4dc31c31ed1.png)

第一个是 host 地址：

![](img/zhuanqian_67b986f43c1f83abb908832500654ba0.png)

第二个是 Service role secret

![](img/zhuanqian_142394103b9472874179d7e8f1e42037.png)

填完后红色叉叉就消失了。

### 5、整体测试 n8n 工作流

下一步是测试。

点击工作流下方的「Execute workflow」进入测试模式。

![](img/zhuanqian_c9e2ee7ee2c97291d326f6eb508b97e0.png)

能看到整个工作流进入待执行状态，特别是第一个节点提示正在等待你的请求。

![](img/zhuanqian_dc8e8e674a5d293419f610e49e2b29c4.png)

点开第一个 webhook 节点

就能看到「Test URL」下的一个 http 地址。

![](img/zhuanqian_e7981bc5fc2581b8547d5fb6309e2aed.png)

复制这个地址，用前面提到的 APIFox 来发请求。

![](img/zhuanqian_8b9ef805e65ab32f4e0a9ac9fae8c968.png)

按下 APIFox 的「发送」后，工作流就跑起来了。

![](img/zhuanqian_f86cc9f41a6ed3a845286429631b80f6.png)

### 6、修复运行中的节点报错

运行过程中会出现节点报错

![](img/zhuanqian_7cff13692ba1c1273967e28480f339bc.png)

点开具体节点就能看到错误详情：

![](img/zhuanqian_b17f37179144c52ad219510eef00099f.png)

原因是数据量过大。

回头看浏览器插件采集的数据，前期采集了评论但没有做清洗。为了省事，先不处理评论数据。

```
接收到的数据里面有noteCommentsHtml评论数据，比较大，看是否可以先过滤掉，加一个过滤节点
```

![](img/zhuanqian_939f4852a3a3a8a3bc5f258eabd92b4a.png)

### 7、修复数据库唯一键冲突

还有一个问题，如果数据库里已有数据，再次执行就会报错。

可以看到是唯一键冲突，这是数据库的正常机制。

我想让它支持 upsert 逻辑：没有就新增，有就更新。

唯一键相当于身份证号，一张表里一条记录唯一。

![](img/zhuanqian_216647bb09a410bed226fb1c6a4edaff.png)

所以要改成 upsert 模式。

这里我直接更新工作流，n8n mcp 也支持这个操作，调用的是 n8n_update_partial_workflow 方法。

![](img/zhuanqian_d486d47a7efe886b079ae5e912359a6d.png)

我开启了 ultrathink 模式，让它更谨慎地修复错误。

![](img/zhuanqian_cc4299f81b0c83cb0c323f0f4b9c8d40.png)

最后发现改完还是报错

![](img/zhuanqian_52af930428ab92a6b5c4e1d2ce766ee0.png)

继续改：

![](img/zhuanqian_41fc302c8231b76f5b94c8ae23b8b9cf.png)

因为我装了 supabase 的 MCP，可以直接查 supabase 的文档，确认 upsert 该怎么写。

![](img/zhuanqian_e2b9871424ee875c3e81c13c2e9f68e0.png)

![](img/zhuanqian_7dc59bf5d244e786bcf462a6935f8b9e.png)

最终方案走的是自定义路线，是查阅 supbase 官方文档后才拿到的可行方法。

从 n8n mcp 反馈的信息来看，原生的 supbase 节点并不支持 upsert 行为。

于是让 claude code 直接生成了一个 http 节点，填入了 supabse 的鉴权信息，这样就能完成 supbase 的 upsert 了。

问题算是彻底解决。

![](img/zhuanqian_c34fd60344007a1d61e386fa7ebdb2ef.png)

### 8、这里藏着一个挺麻烦的点

笔记数据和博主数据存完后共用同一套判断逻辑，结果就会出现误报。

举个例子，笔记数据检查通过了，博主数据反而被判定为异常，其实两边数据都正常。

接着继续排查原因

```
"检查保存状态"这个节点，因为检测的是“作者“和“笔记“的前置两
个节点，检测代码写的是通用的，运行的时候只会满足一个情况，
比如检测作者数据的时候，就会返回[
{
"success": false,
"message": "数据保存失败",
"errors": [
"笔记数据保存失败"
],
"authorSaved": true,
"notesSaved": 0,
"timestamp": "2025-08-20T09:00:42.892Z"
}
]，检查笔记数据的时候，就会返回[
{
"success": false,
"message": "数据保存失败",
"errors": [
"作者数据保存失败"
],
"authorSaved": false,
"notesSaved": 114,
"timestamp": "2025-08-20T09:00:42.934Z"
}
]，帮我重新想下这个方案如何设计好，ultrathink
```

![](img/zhuanqian_f648fc077b4f6b13793fd3474b77fd5b.png)

让 claude code 帮忙给出解决思路：

解决问题：

![](img/zhuanqian_697d07f52402cc14c24e12b362223a1e.png)

## 最后的总结

说到这里你可能要意识到，我整套流程里根本没在 n8n 的页面上手工搭建过任何工作流。

节点长什么样、用来做什么、参数怎么配，我全都不知道。

都是 claude code 生成完之后，我才回头去看这个节点的作用。

这里提炼的关键点有：

1、对 claude code 把需求讲清楚，比如要它输出 n8n 的 json 文件

2、提前配置好 n8n mcp 工具，让它能拉取真实的 n8n 节点文档作为依据

3、做好工作流备份，点一下右上角的三个点就能导出 json 文件就行。

想多说的其实是学习能力与解决问题的能力。

这正是 AI 时代每个人都要刻意训练的能力。

# 第三部分：像素红薯开发

偷偷剧透一下，这个模块的难度是先难后易，这部分是最轻松的了。

第三阶段终于来了，可以稍微喘口气了。

进入休闲模式，也是人人都能拿下的环节。

本阶段的核心任务如下：

1、做一个 web 系统，从数据库读取小红书数据，直接展示出来即可

2、模仿对标写文章，也就是调用 AI 接口实现

3、文生图，依据参数生成小红书配图，调用 AI 文生图接口就行。

## 步骤一：生成项目骨架

最省时的开发方式，就是基于现成模板起步，环境基本一次到位。

直接让 claude code 按业务需求开干。

用模板代码快速生成项目

你不懂也没关系，这个模板里的源码我也没细看。

```
pnpm create next-app --example https://github.com/vercel/examples/tree/main/storage/postgres-drizzle
```

接下来填一下自己的项目名称就好

```
xiaohongshu-n8n-web
```

## 步骤二：写好需求文档

![](img/zhuanqian_8d42ec90d89675fbcf5de21766b84ceb.png)

核心其实是把你要的功能理清楚。

以及数据交互的具体流程。

这里要感谢 yihui 大佬的提示词给了灵感，真的很强。

```
网站名称叫做：像素红薯。
网站功能如下：
1\. 首页是从 xiaohongshu_authors 表中获取对应的数据，然后以卡片方式渲染，响应式一行最多渲染2个，移动端渲染1个卡片，点击作者名称能够新窗口打开链接 profile_url。同时卡片中有一个报告的icon，右侧出现报告渲染report 字段，report 字段为markdown格式，要求使用markdown的渲染库实现渲染。
2\. 点击作者卡片后，能够进入到作者的详情页面，顶部显示 xiaohongshu_authors 中的相关数据，同时请求notes表的数据，获取对应 author_id 的笔记数据情况并渲染。同样是以卡片渲染。卡片展示所有文案，不要多行省略。
3.在作者详情页面需要有一个AI小红书笔记仿写的的功能，使用对应的icon，点击后能够弹出一个几乎全屏的弹框。左侧是配置页面，在配置页面用户能够配置是否添加emoji表情，有一个多行文本框，这个多行文本框允许用户输入主题和想要创作的内容，同时又一个【仿写】按钮，点击后请求后端接口，开始实现仿写功能。右侧是AI仿写的小红书笔记的生成区域，使用流式输出实现AI给出对应的笔记
4\. AI功能使用智普大模型，使用OpenAI SDK，base_url:https://open.bigmodel.cn/api/paas/v4/, api_key为环境变量中的 ZAI_API_KEY，使用 process.env.ZAI_API_KEY。务必使用流式输出，模型使用：glm-4.5
5\. 你需要编写对应的系统提示词和用户提示词，提示词中你还需要携带上改作者的notes这张表的数据，用于更好的参考原先的内容实现仿写
6\. 网站使用 tailwindcss + shadcn/ui，要求UI样式魂斗罗的像素风格，有一定的微动画效果，颜色主要以🍠颜色为主题色。
7\. xiaohongshu_authors 表和 xiaohongshu_notes 表结构见 @docs/supabase.sql，集成Drizzle ORM
```

重点强调一下，到这里会发现，这三部分的的需求文档会花掉不少时间。

1、把功能想透，越细越好，细到某个 icon 都要说明

2、使用的技术栈，最好明确指定

3、涉及的数据，指定表名，以及交互组件

4、整体的站点风格。

5、把需要用到的 sql 文件和接口文档也指定好。

## 步骤三：根据需求文档进行开发

到这里流程还是一样，让 claude code 依据需求文档来开发。

```
@docs/prd.md 根据需求文档，开发这个网站，ultrathink
```

依旧在 plan 模式下，加开 ultrathink 深度思考。

![](img/zhuanqian_609beb24435487451ff6061e737aab35.png)

开始执行计划

![](img/zhuanqian_3da5106b6120eacc39c01bdc3096abaf.png)

到这里可以先放松一下。

![](img/zhuanqian_b6b472d23525d1281f09994be947b549.png)

等待它跑完就行。

## 收菜验收

喝了杯下午茶就去验收成果

进首页，第一眼还行，像素风，🍠配色，哈哈哈，icon 也一模一样。

![](img/zhuanqian_f59f529c2098f5dc2921a07bda21ddfd.png)

但是。。。。就报错了

## 步骤四：修复错误

### 1、”查看报告“的时候错误

![](img/zhuanqian_695a65c19c9740d1f617fe90fbce01b4.png)

直接点页面上的复制按钮

把内容粘贴到 CC 的对话框里

![](img/zhuanqian_64b0b52f5248cf23466b1fe235d59591.png)

回车就搞定了。

解决后就能看到个人页面：

![](img/zhuanqian_64c8a4e40417eab2eb1ea862d9ff7476.png)

### 2、笔记列表为 0 的情况

能看到笔记列表显示为 0，于是直接告诉 claude cod。

![](img/zhuanqian_f5bb14b559793b81a4ebfc6e1d4152e2.png)

从 claude code 的反馈看，可能是关联字段写错了。

![](img/zhuanqian_29acfbd5e4fdf4824d5aab198319a25a.png)

最后顺利修复了，还贴心地帮我们删掉了调试日志。

![](img/zhuanqian_23a922674a9001ffe3b41479647118cc.png)

### 3、仿写功能异常

到仿写功能时也出现了异常

我们把错误信息粘贴上去，再加一点提示。

```
仿写的时候报错：ai-rewrite-modal.tsx:90 生成失败: Error: 生成失败at handleGenerate (ai-rewrite-modal.tsx:55:15)
```

![](img/zhuanqian_22e062d7d3be6112bbff380f4de506e3.png)

还有个小插曲，发现我的 glm 账号余额不足。

![](img/zhuanqian_d63f1b9ebefa9de203d44ce47a9a4730.png)

查了一下余额确实没了，先充值一下继续。

最后记得

```
commit push
```

![](img/zhuanqian_0b8b4ca459d59e64e695baecaaa09fd4.png)

效果如下：

![](img/zhuanqian_b3d908110d9eb8cb4b4dd47ad24c6cbd.png)

这里用的是 glm 的模型

这一点在需求文档里写得很明白。

```
4\. AI功能使用智普大模型，使用OpenAI SDK，base_url:https://open.bigmodel.cn/api/paas/v4/, api_key为环境变量中的 ZAI_API_KEY，使用 process.env.ZAI_API_KEY。务必使用流式输出，模型使用：glm-4.5
```

其实最稳妥的做法是把接口文档保存到本地的 api-glm.md 文件里，这样 claude code 读取更准。

避免它读不到链接里的内容。

## 步骤五：接入文生图的模型

只用最近很火的 qwen 的生图模型

https://www.modelscope.cn/models/Qwen/Qwen-Image/summary

不过我先让 claude code 讨论下这个模型怎么用

```
https://www.modelscope.cn/models/Qwen/Qwen-Image/summary
这个生图的模型怎么使用了？
```

![](img/zhuanqian_0275390b0425ad43450485f7ee065a4d.png)

后来我决定让 claude code 直接读取这个链接的文档

结果开发后一直不对

![](img/zhuanqian_79418d7f1d6931bf80d2d400c2f81303.png)

没办法，只能手动把文档粘贴上来。

我还特意把文档里的示例代码贴上了，虽然是 python 的，但 claude code 完全能理解。

```
@docs/api-modelscope.md 这个是modelscope的api文档，这个是文生图的示例代码：
```

![](img/zhuanqian_fd3856f981868962a519c642e9dc14bd.png)

### 错误：绑定阿里巴巴账号

这里有个坑是要绑定阿里巴巴账号

一开始我也不知道，就继续和 claude code 聊错误。

它会根据接口返回的信息帮你排查，并给出提示。

![](img/zhuanqian_fa0998388bd1d0c599b2d385d861c12e.png)

### 错误：自动修复尺寸符号问题

继续测试接口

发现尺寸符号应该用 x 而不是*号的问题。

![](img/zhuanqian_b9d17e6643e85f2e93087047ba073f26.png)

最后完美修复

![](img/zhuanqian_fffdc1e02df0f354948a1b7b607ebac6.png)

![](img/zhuanqian_6123973f0794465944b4d75d0cbb3381.png)

## 步骤六：提交代码

这是最后一次提交代码的说明

基本每完成一个小功能或解决一个问题，我都会提交一次

养成频繁提交代码的好习惯是整个过程中要培养的。

```
commit push
```

![](img/zhuanqian_b8b866c20a54eaa8af8ffdb19a2ec3d3.png)

# 总结

到这里基本就结束了。感觉体验如何

还是按惯例做个总结。

AI智能体+AI 编程绝对是今年最火的方向。

价值体现在哪里？

我觉得就是 claude code + n8n 的组合。

一个是编程圈的扛把子

一个是智能体领域的后起之秀

再加上出海赛道火爆。

这就是 claude code + n8n 的魅力所在。

那么具体怎么落地

1、把 AI 工具学好用好，我这里直接推荐 Claude Code + n8n，跟 AI 一起学，或者跟大佬一起学。

2、把你的需求痛点找准，把需求文档写清楚，越细越好，务必人工审核确认。

3、干中学！干中学！干中学！

4、做个垃圾！做个垃圾！做个垃圾！

5、复盘！复盘！复盘！

重要的话说三遍，其实就这么简单。

提升学习能力与问题处理能力

把需求搞懂

剩下的就是干就完了。

如果你有任何问题，欢迎来找我交流，欢迎跟志辉一起讨论！

最后感谢赚钱！跟很多大佬一起学习，也在积极反哺社区，跟大家一起在这个时代打造属于自己的天地。