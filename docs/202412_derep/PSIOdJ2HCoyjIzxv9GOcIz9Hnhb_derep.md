# ('利用AI工具copycoder + bolt 三句话复制想要复制的网站', (2, 37))

AI复制网站如此简单？CopyCoder + Bolt 三句话搞定！

大家好，我是那个总在赚钱圈子里默默潜水、偷偷学习的小透明——路过蜻蜓。今天鼓起勇气，来跟大家分享一个最近玩得特别上头的骚操作：如何借助 CopyCoder 和 Bolt 这两个 AI 工具，几乎零成本地把一个网站“复制”下来。你没听错，三句话就够。

先给大家看看我最终做出来的成品效果：https://exquisite-donut-20454b.netlify.app

![](img/ef076a0857ca89324625a27000337fcc.png)
![](img/7ae5c5bf422e16d470c4c003a37093c4.png)
![](img/24595bc14ed9484724263866365f7f19.png)
![](img/8d9ef1eddcbaff545363774a70d90905.png)

从截图能看出来，还原度相当高，甚至连多个子页面都完整保留了下来。

那这个 CopyCoder 到底是个啥？前几天刷 X 的时候偶然发现了一个新工具：https://copycoder.ai

![](img/bb75d1791c6102e54ab477a5e87f74fc.png)

出于好奇，我第一时间跑去问了 ChatGPT 这网站是干什么的。

![](img/2adc193b7e7fbc04f9d9bf312cdb1cab.png)

得到的答案是这样的：CopyCoder 是一款基于 AI 的辅助开发工具，你只需要上传应用截图、UI 模型或设计图，它就能自动分析并生成对应的详细编码提示词。这些提示词可以直接用于 Cursor、Bolt、v0 等主流前端开发环境，能大大提升开发效率。简单来说，你给它一张图，它帮你把代码思路和结构都规划好。

换句话说，我只要把目标网站的截图或设计稿丢进去，就能获得一份可以生成该页面的提示词。光说不练假把式，直接上手试试。

![](img/9981e68a20ccc07c64beae58bd64ec4b.png)

我当时正好在研究 Suno AI 音乐，就拿 Suno 官网开了刀。打开 https://suno.com，复制首页地址，截个图，然后上传到 CopyCoder。

![](img/f4be51f6ea635740b68c3406bc835448.png)

点一下“Generate prompt”按钮，提示词就出来了。

![](img/c4561d9b1f1bfaa9b4a4b11fe8b28c5f.png)

第一步操作完成，提示词就在页面下方展示着。

![](img/064902e1f3e9dd496c293d8f4c8db3a9.png)

官方说明显示，目前生成的提示词支持 V0、Bolt、Cursor 这三款工具。点击对应教程，还能看到如何用 Cursor 创建项目的方法。

![](img/62f5bc64c7a3fad5e7b6e5f4fe11c5d7.png)
![](img/811d3285f2a2275a587da1b0414ee9ca.png)

不过我这次没选 Cursor，而是用了 Bolt。直接打开 https://bolt.new

![](img/0261ecd002edc95b6206a3f13e001826.png)

把第一步生成的提示词复制粘贴到输入框里，Bolt 就会自动开始干活，帮你把网站搭出来。

![](img/eca33c7ea0ab9d355c9766e6bd855f60.png)
![](img/884cf46531a87fceb57d59f1f1a6d124.png)

这个工具最大的特色就是能一边和 AI 对话聊天，一边实时看到网站生成的效果。可惜我当时的试用次数已经用完了，没法展示动态效果。

![](img/f27b1496a7750375bf6f419a17668a9c.png)

接下来，我让 AI 把网站里的文字全部替换成简体中文。

![](img/b86f2823126df86a8cc319eadec37019.png)

然后回到 CopyCoder，点击“Generate Page Structure”按钮，拿到第二步所需的提示词。

![](img/c659d4dcbdc7a7e018a5f19be76df9e8.png)
![](img/8cfb9aa282e294e5004a91563319d3ef.png)
![](img/5ec5342bb4c066a683ab31cea5bacbd7.png)

把新提示词提交给 Bolt 后，我发现首页显示有点小问题，就让 AI 顺手修复了一下，接着直接部署上线。

![](img/4584dc4142cbe25e91b7dfe70f4ae7d4.png)
![](img/19d59cced8c35e66d016b1e02db1509b.png)

你看，整个过程中我前后只跟 AI 对话了三四句，一个完整的网站就这么诞生了。我的提示词内容和操作都放在下方，大家也可以照着试试。

成品网站：https://exquisite-donut-20454b.netlify.app

![](img/46c58724ef07c3b196c7870e284c9057.png)

这里有个重要提醒：目前 CopyCoder 只能生成网站，不过据官方说法，后续应该会开放手机端等其他类型。

![](img/10a617d47af0fbf0c8123376beae1556.png)

另外，如果你需要翻译页面内容，推荐使用浏览器插件“沉浸式翻译”，还能接入 AI 进行辅助翻译，非常方便。

![](img/34a384b2d0ff1e4bf4a30575420d0bb8.png)

最后附上我用的第一步提示词（用于生成组件结构）：

```
Create detailed components with these requirements:
1\. Use 'use client' directive for client-side components
2\. Style with Tailwind CSS utility classes for responsive design
3\. Use Lucide React for icons (from lucide-react package). Do NOT use other UI libraries unless requested
4\. Use stock photos from picsum.photos where appropriate, only valid URLs you know exist
5\. Configure next.config.js image remotePatterns to enable stock photos from picsum.photos
6\. Avoid duplicate components
7\. Automatically source and display logos from a CDN in design placeholders
8\. Follow proper import practices:
   - Use @/ path aliases
   - Keep component imports organized
   - Update current src/app/page.tsx with new comprehensive code
   - Don't forget root route (page.tsx) handling
   - You MUST complete the entire prompt before stopping

Music Creation Platform Dashboard with Featured and Trending Tracks

 1\. Navigation Elements:
- Left sidebar with: Home, Create, Library, Explore, Search
- Secondary navigation: Credits counter, Subscribe button, What's New, Notifications
- Social media links at bottom: X, Instagram, TikTok, Discord

2\. Layout Components:
- Header banner: 100% width, ~60px height
- Main content area: ~80% width
- Card grid layout: 5x2 grid for featured content
- Cards dimensions: ~200px x ~280px

3\. Content Sections:
- Top banner announcement for v4 features
- "Fresh from v4" featured section
- "Global Trending" section
- Track cards with: Duration, Title, Artist, Play count, Likes
- Right sidebar promotional content

4\. Interactive Controls:
- Play buttons on track cards
- Like counters with interaction
- More options (three dots) menu on cards
- Global/Now filter dropdowns
- Navigation hover states

5\. Colors:
- Primary dark theme: #000000 (background)
- Accent blue: #1E90FF (v4 badge)
- Text white: #FFFFFF
- Secondary gray: #808080
- Gradient overlays on track artwork

6\. Grid/Layout Structure:
- Main container: 1440px max-width
- Card grid: 20px gap
- Sidebar: 240px fixed width
- Responsive collapse points at 1200px, 768px 

 1\. Project Structure:
```

然后是状态管理相关结构：

```

2\. Key Features:
- Audio playback system
- Track information display
- Like/interaction system
- User authentication
- Track upload/management

3\. State Management:
```

路由定义：

```

4\. Routes:
```

响应式断点样式：

```

5\. Component Architecture:
- TrackCard (reusable component)
- AudioPlayer (global component)
- NavigationBar (fixed component)
- FilterControls (shared component)

6\. Responsive Breakpoints:
```

到这里，步骤一的提示词就完整了。

``` 
```

接着是步骤二的提示词内容：

```
Create me a complete route structure for the Next.js app router, implementing layouts for each page. Ensure the structure is focused on page generation and navigation flow. Each route should have a corresponding page.tsx with comprehensive component structure. Avoid creating parallel routes.
```

如果觉得一步一步操作麻烦，也可以直接复制我建好的项目模板继续创作：https://bolt.new/~/sb1-x4derj

![](img/857b2fdf9978e0477707f3307d430887.png)

再稍微延伸一下，这个思路不仅能复制网页，还能用来写别的工具。我自己就用 Cursor 和 Windsurf 做过不少小项目。比如因为报名了赚钱的 YouTube 航海，顺便做了一个带登录注册功能的网站：http://www.maotools.org

![](img/57099b70d0d7e8653cc1d1a61aa0fba0.png)
![](img/e9c29603ed162b20ee7bb8287926e292.png)

还开发了一款 macOS 下的 YouTube 下载工具。这些全都是靠 AI 工具完成的。以后有时间，我再专门写一篇聊聊我是怎么从零把网站做完并成功上线的，包括用到的具体技术。

总结一下：现在真的是 AI 创意的时代，只要你有想法、有点子，再借助合适的工具，几乎什么都能实现。赶紧动手试试吧！