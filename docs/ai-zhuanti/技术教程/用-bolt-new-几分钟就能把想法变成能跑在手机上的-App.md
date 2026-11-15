# 用 bolt.new，几分钟就能把想法变成能跑在手机上的 App
## (49 赞)5 分钟做个 app bolt 教程
作者： 龙哥
日期：2025-02-13
我不喜欢在标题里放“炸裂”这种哄点击的词，除非当下真的觉得惊讶到不行。
至于“5 分钟做个 App”这个说法，则是受小排老师关于 bolt 的那篇文章启发，强烈建议去读一下：
**正文：**
今天本想拿 deepseek 和 bolt.new 比一比前端代码生成的差距，结果刚进 bolt.new，就看到了这个功能：
![](img/2f203424dbd34c4f07e3049159419afa.png "None")
AI 已经进化到可以直接出一款 App 了？那对三月要做的 iOS 出海项目来说，简直是好消息。
下面拆成两块来讲：
App 的一键生成实操
bolt.new 的快速上手要点
## 先了解一下基本信息
官网：bolt.new
登录：左上角 sign in，我习惯用 GitHub 账号，一键搞定
预览用的客户端：Expo Go，本次测试机型是国内 App Store 的 iPhone
费用：免费额度内的代码量足够日常尝试，体验感没问题
## 怎么出 prompt
![](img/39c25651314bbe08a2584c7a9eb73d5e.png "None")
先用最简单的一句话试水，让它帮我做一个壁纸分享类的 App，然后就等着看结果。
![](img/9a87780b59bbc026b7a43451202f1fbc.png "None")
预览在哪？别急，按它的提示再往下走一步就行。
手机上装好 Expo Go 后，App 本身没有扫码入口，需要用系统相机扫页面上的二维码，扫完后会弹出在 Expo Go 中打开的选项：
![](img/4fb0008f6508d2e732db15b9d08e6fb9.png "None")
打开成功后等一会儿，就能在真机上看到效果了
![235ebf2e25747b54cc7a74041410c75.jpg](img/article-) images.zsxq.com/Fht4fbuEseEqVnrIdhXwye19KIOb)
![aed4af3a61b6dc51be06974530732ba.jpg](img/article-) images.zsxq.com/Fs1iv4dR2Qs49tTXgDqu7OFBju5p)
整体完成度挺高的，部分图标在深色背景下显示不佳，可以改成浅色背景，或在支持的 IDE 里查看细节：
![](img/b571a7593acf73c6ac81388e368d1f60.png "None")
惊讶吗？
更复杂的诉求和代码产出就不再展开了，bolt 的代码能力基本不会因为语言或产品形态不同而有明显落差。
## bolt.new 使用速览
### 页面布局
![](img/8a61918760b61bc99a97c67c2db1b55b.png "None")
**左侧 1** 的大块文字区，是 bolt 在生成代码时的过程日志，相当于记录了做了哪些操作、生成了哪些文件、执行了哪些命令，和 Cursor 的回复面板类似。
**左侧 2** 是继续和 AI 对话的输入区。
**右侧 3** 是在线 IDE，主要干两件事：
代码查看与修改（Code）
实时效果查看（Preview）
边改边看，改完立刻生效。
**右侧 4** 区域的功能：
**导出代码：** 生成完后点左上角 Export，有两个选择，一个是 download 直接下载到本地；另一个是 Open in StackBlitz，这是一个在线开发环境，我通常直接在这里把项目推到自己的 GitHub 仓库。
![](img/43af5f7b15bea52e19a4604e95ddf3be.png "None")
上图就是 Open in StackBlitz 的界面，你可以把已有项目导入进来，也可以在 bolt.new 里生成完后点“Create a repository”，它会自动帮你建一个 GitHub 仓库。
在线 IDE 甚至能预览手机 App 的页面（上图右侧）。
**数据库连接：** Connect to Supabase，可把项目接入 Supabase 数据库。
**部署：** deploy 包含 deploy to web 和 deploy to App Store 两个方向。
前者会把网站或项目部署到 Netlify，并给你一个可用子域名。
后者是把 App 提交到应用商店，点开后有官方教程指引：
[`docs.expo.dev/deploy/submit-to-app-stores/`](https://docs.expo.dev/deploy/submit-to-app-stores/)
我的个人工作流：
一般先在 bolt.new 里把项目的雏形、基础样式和简单组件跑出来，然后导出到 GitHub，再在本地用 Cursor 做更精细的功能迭代和打磨。
* * *
评论区：
书虫 : 真的快
嘉应岛主 : 真是炸裂
辛亥 : 立马学习了
一兮｜小缨 : 感谢分享！晚点实践一下