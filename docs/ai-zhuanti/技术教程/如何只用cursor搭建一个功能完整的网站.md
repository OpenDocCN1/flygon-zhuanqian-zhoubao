# 如何只用cursor搭建一个功能完整的网站
只用Cursor，真的能做出一个功能完整的网站吗？
我的答案是：能，而且没有想象中那么难。这篇文章不是空谈，而是我在《Cursor-零基础做软件应用》航海后整理的一份实战复盘，里面既写了怎么一步步把网站搭起来，也记录了不少我自己踩过的坑。顺便说一句，这次航海里有很多产品案例，完全可以整合到同一个网站里，日常用起来会方便很多。
我其实是在Cursor火了大半个月之后才正式上手的。最开始挺惊艳，用着用着又觉得“就这？”，直到真正涉足复杂项目，才发现这玩意儿简直是个神器。现在我几乎每天都会打开它。以前遇到代码问题，我的第一反应是打开百度搜；现在的第一反应，是打开Cursor问。说白了，就是从“面向百度编程”切换成了“面向Cursor编程”。
## 为什么我最终认定了Cursor
好用的人工智能编程工具其实很多，我选Cursor的一个重要原因是：它有免费额度，而且正常情况下完全够用。再加上下面这几个优点：
- 多文件并行修改：它的Composer模式可以按你的指令，一次性在多个文件里生成或修改代码，特别适合大范围重构。
- 智能补全：它能读懂代码上下文，补全建议比较靠谱，能省下不少敲键盘的时间。
- 质量提升：可以自动发现代码里的隐藏问题，并给出优化建议。
- 个性化：VSCode的扩展、主题、设置和快捷键都能直接导入，几乎零成本切换。
不过，新手用它时也容易翻车。最常见的情况是：本来想修一个bug或加个小功能，点下Accept之后，程序直接不能用了，还退不回去。
## 免费使用Cursor的几种“野路子”
想继续白嫖，可以试试这几个方法。
第一个是“销号重开”：去Cursor设置页（https://www.cursor.com/settings）拉到最底部，找到Delete删除账户，然后用同一个邮箱重新注册一个新账号。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a29eb5c4a8f315a93b281fac3751c7db.png>
第二个是换邮箱：直接买一个新邮箱来注册，买好之后重新登录就行。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9b30cfa5faad220a9315f9392344a8c4.png>
第三个是处理次数限制。现在免费额度已经从原来的500次缩水到了250次，而且一台机器也不能无限制地来回切免费账号。我试过靠谱的办法是：去扩展市场搜一个名字带 fake 的插件，装好后重启Cursor，一般就能继续用了。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_31d735e26bac196d37795d73eda7fd4e.png>
第四个是绑定自己的API Key。愿意用自己的API成本来换无限消息量，那就彻底不受免费次数束缚了。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1a459f7218c55d8e1cdc4f26586be486.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_264bbb2e921d6a8e7560cbce26b585f5.png>
## 开发前，先把这些工具备好
工欲善其事，必先利其器。下面几样东西都是傻瓜式安装，下载完双击就好。
- Cursor本体：直接去官网下载就行。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b49044d0a1ae5542cd607602a813ac33.png>
- Git：这是代码版本管理工具，装完之后右键菜单里就会出现相关入口，下面这些是常用命令。 ```
## 初始化和克隆
- `git init`：初始化一个新的 Git 仓库。
- `git clone [url]`：克隆一个远程仓库到本地。
## 检查当前状态
- `git status`：查看当前工作目录和暂存区的状态。
## 跟踪和暂存更改
- `git add [file]`：将文件添加到暂存区。
- `git add .`：将所有更改添加到暂存区。
## 提交更改
- `git commit -m "[commit message]"`：将暂存区的内容提交到本地仓库。
## 查看提交历史
- `git log`：查看提交历史。
- `git log --oneline`：以单行格式查看提交历史。
## 分支操作
- `git branch`：列出所有分支。
- `git branch [branch-name]`：创建新分支。
- `git checkout [branch-name]`：切换到指定分支。
- `git checkout -b [branch-name]`：创建并切换到新分支。
- `git branch -d [branch-name]`：删除分支。
## 合并分支
- `git merge [branch-name]`：将指定分支合并到当前分支。
## 拉取和推送更改
- `git pull`：从远程仓库拉取最新的更改。
- `git push`：将本地更改推送到远程仓库。
- `git push -u origin [branch-name]`：将新分支推送到远程仓库并设置上游分支。
```<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_849f1cf4379c881421ebfbe649a8178d.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4e29cd4a31acee6db6cc6ff01dd22bcb.png>
- Node.js：一定要装，装好之后才有npm命令。<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c68a3ddac96e1b6563b38eaeca79517f.png>
另外还有一些更好用但需要花钱的工具，也一并推荐：比如大模型Claude、GPT-4o；Windsurf是Cursor的直接竞品；Replit可以把AI工具整合到一起用；v0和bolt.new都是前端AI生成工具；Devin被称为“AI软件开发人员”；CopyCoder则非常适合复刻前端页面，上传截图或UI设计图，就能自动生成编码提示词。插件方面，还有GitHub Copilot、FittenAI、灵码和豆包编码助手可以试试。
## 完整开发流程：我是怎么从零搭出网站的
先说一下目标：做一个相对完整的网页Demo，包含登录认证、前端后端、SQLite数据库，以及AI聊天界面。做完之后的效果大概长这样。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_042e4e2b0894e5b801914394b11989d1.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1a00045ce5ac27b31c3e50f4e092ccde.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_92361d874522db623ab75dcb96b9749a.png>
### 第一步：明确需求，和Cursor达成共识
不要上来就让它写代码，先像聊天一样把需求问清楚。如果它给的回答不符合预期，就换一种问法重新问，直到双方对齐为止。
需求确认以后，新建一个README.md，把要点写进去。比如我的项目，技术栈用Next.js，数据库选sqlite，核心功能是登录和学生信息的增删查改，本质上是一个学生信息后台管理系统。提示词可以写成下面这种格式。 ```
回答我的问题，先不要生成代码, 以下是我的需求
```
项目作用：学生信息后台管理系统；项目功能：登录、学生信息增删查改；后端数据库：sqlite；技术栈：next.js。 ```
请你帮我设计项目的前端、后端、数据库、api
```<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7e679046742f0ea44e14c88ff637f509.png>
### 第二步：让Cursor帮忙初始化项目
这里有个很重要的经验：不要自己去跑脚手架命令。虽然像Next.js这类框架都有自带的项目初始化工具，但手动执行命令对新手来说又麻烦又容易出错，而且会生成一堆用不到的文件。文件一多，你看着烦，Cursor也容易看花眼。正确做法是让Cursor直接生成项目结构。 ```
，现在请帮我初始化一个next,js项目，不要告诉我命令，直接在当前目录下生成必须的代码文件
```
这一步容易遇到两个坑：
第一个坑：它不生成文件，只是把代码给你，让你自己动手建。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bb4429db83df21efce0e06e9f6565ac4.png>
第二个坑：它会新建一个目录，而不是在根目录生成文件。目录一多，Cursor可能就找不到正确位置，然后反复在当前目录生成重复文件。我的解决办法是：新开一个Composer窗口，然后把需求重新强调一遍。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_66d0ffe312036d9ca0f9ed743eafc323.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_69f8cb8c27fec51ff0dcdf75d118a2f2.png>
另外，如果你手动调整过文件或目录结构，一定要记得告诉Cursor：“@codebase，我调整了代码结构，请刷新缓存，后续不要生成重复的代码，不要生成多余的目录和文件。” <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3b9d83b21f5f2b5c55beb2c596f89442.png> 或者去设置里手动刷新一下缓存。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3fa050b1c2e2da27f5962d48d54dc103.png>
### 第三步：让程序先跑起来
项目初始化之后，先别急着做业务功能，第一件事是运行程序。哪怕只是一个最简单的页面，只要它能跑起来，就说明环境没问题。不要攒一大坨代码再运行，那样出了问题很难排查。 ```
代码生成好了，我要如何才能在浏览器上访问到
```
当你看到hello world，其实就已经成功一半了。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2548936a0dcfa0db329559e10f1d0337.png>
如果执行npm install特别慢，可以把npm源切换成国内镜像，命令是：
npm config set registry https://registry.npmmirror.com <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ecd25ffbc27daccf1fb9472160ee3d42.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f67e37cb35fc25505fafed737c734ca4.png>
### 第四步：开发登录页
登录页的提示词我写得很明确：先开发登录页，账号密码可以先写死在代码里；所有页面都必须登录才能访问，如果没登录，就自动跳转到登录页。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c89c3860a874c3616c5d879325a82024.png>
第一版做出来之后，界面通常比较丑，甚至还会出现乱码。这时候有两种优化思路：一种是反复跟Cursor说“好看一点，好看一点”，让它自己不断调；另一种是去网上找一张自己心仪的界面截图或链接发给它，让它照着做，这样能省不少沟通次数。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0d942b7867ee2294e711c06460387ef2.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f8a885db1599bdab99aeb337dbd65bb1.png>
页面出来以后，可能会发现没居中、不美观等问题 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_255dfff466d6e959498e707a44bc0970.png>，没关系，继续提优化要求就行。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0ef59ec15ddaab19e779058f21ea2095.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f0bc3e579c3a157ec78121e0aebeb92a.png>
每做完一个小功能，都要养成验证的习惯。比如确认登录后能不能正常跳转到首页。如果要做谷歌认证，去看谷歌官方文档。反正只要代码一报错，最省事的方法就是把错误信息直接复制给Cursor。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b903cca32d4efc0a169bf617e320a47f.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fe634ee154a3302bbded34984aec493a.png>
### 第五步：开发网站布局
细心的话会发现，绝大多数网站的不同页面，其实共用一套统一布局。所以布局最好优先于业务功能开发，先把骨架搭好，后面只需要专注填内容。
如果想复刻一个网站的布局，有三种方法：
1. 直接把目标网站链接发给Cursor，让它解析结构。
2. 截图，让Cursor根据图片生成代码。
3. 如果目标网站需要登录，可以打开F12，把页面代码复制到本地文件，然后通过@文件的方式让Cursor分析。
我演示了第三种方式：比如想复刻这个界面。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_459b05d86bf9f0327091353d0e982e41.png>
因为页面需要登录，所以先在F12里把代码复制到本地。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0d33c35b51fc33802b6595c177897b62.png>
然后给出提示词：帮我复刻一个如文件所示的界面布局。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7194c33bb83c3f23123fd6621b4414a6.png>
第一版往往不完美，但没关系，可以继续微调。比如：把顶部导航栏换成指定背景色、高度设为32px，并加上一个能展开/收缩侧边菜单栏的图标；侧边菜单栏背景保持不变，增加一个logo；底部footer背景改为白色，高度设为32px。其实只要知道顶部叫导航栏、左侧叫菜单栏、底部叫footer，就能按位置精准指挥Cursor了。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_64cd3ed2bb1be2301bea88b4b49e6980.png>
### 第六步：开发学生信息系统
从这里开始，才终于进入真正的业务开发。数据流大致是：
前端登录 → 前端展示页面 → 前端向后端发API请求 → 后端逻辑处理 → 数据库
我习惯把这三层理解成一个比喻：前端是销售，后端是产品线，数据库是仓库。销售给客户看产品图，吸引用户下单；后端再按单把产品生产出来；生产出来的东西和原材料，全都放在仓库里。
后台管理系统最常见的操作就是增删查改，也就是搜索、增加、删除、修改。这时候只需要对着README.md里的需求，让Cursor按部就班地开发就好。 ```
结合 @README.md 系统设计及以下需求，帮我生成用户管理系统:
1.当我点击学生管理的时候，内容区会显示对应内容
2.使用sqlite数据库存储学生数据
3.需要有搜索、增加、删除、修改功能
4.初始化的时候，如果数据库的学生表是空的，则插入10条示例数据
```
注意，一次性给的需求太多，特别容易翻车。报错也不用怕，老办法：把错误信息丢回给Cursor。我还会在提示词里加一句：把用到的依赖都写入package.json。这样它就不会只给你一条命令；否则当前环境下能跑，换个环境就容易缺包报错。 ```
代码报错了，报错信息: """报错信息"""
如果是因为缺少依赖包，你应该把依赖包写到package.json文件中
```<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_94f25ae82a1b62be313381976d9ec926.png>
把报错修掉之后，界面基本就出来了。我验证了一下功能，除了界面丑了点，功能完全没问题。运气好的时候确实能一次过，但大部分时候还是会有小bug需要慢慢磨。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e2f8b771eea4fe4fe025dd15583fad6a.png>
接下来，我按自己的审美写了新的优化提示词：
1. 删除文字“添加学生”，也删掉姓名、年龄、班级输入框。
2. 把搜索框移到添加按钮左边。
3. 添加和编辑学生信息时，改成侧边栏表单，让用户填写数据并发送请求。
4. 编辑学生信息时，要把已有学生数据自动填充到表单里。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7677d4f4030051f5e9132d79f5b6499f.png>
如果你看不懂这类需求、不知道怎么表达，也有两个办法。办法一：直接问AI，让它帮你重新描述。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_873ce1f83e1bc129a2eca4bbcc9962c8.png> 办法二：去官方组件库找术语，比如Element Plus官网 [https://element-plus.org/zh-CN/component/overview.html](https://element-plus.org/zh-CN/component/overview.html)，官方表达最权威，Cursor也一定听得懂。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_804c1cc9e6aebf5d5be71a4ba6285ad6.png>
另外，有时候想找好看的特效但没灵感，可以试试几个CSS灵感网站，基本都能直接复制粘贴代码：CodePen [https://codepen.io/](https://codepen.io/)、Animista [https://animista.net/](https://animista.net/)、Phuoc Nguyen [https://phuoc.ng/](https://phuoc.ng/)。 <https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8bc7714ed472818a5b2c528af77844ba.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ae2f9b027632f42e67b0102deedb4cce.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c599688d4c477fdbdc0571347788fa66.png>
### 第七步：开发AI聊天界面
最后一个模块是AI聊天界面。我想复刻的是Kimi的聊天界面，所以很多描述都按Kimi的样子来。由于这是我第一次写这类界面，我先把自己的需求发给Cursor，让它重新表述一遍，确认我的表达是否准确。 ```
我想增加一个功能，需求如下：
```
我的需求大致是：
1. 把“班级”改成“Kimi”，链接也改成Kimi。
2. 我要复刻Kimi网站，做一个用来和大模型聊天的网站。
3. 内容区拆成两部分：
- 底部是输入组件，一个简单的输入框，用来接收用户输入；
- 输入框之上是信息显示区，用户输入后，大模型返回的数据要以流式文字的方式显示。 ```
你先重新表达我的需求，达成共识后，再进行代码生成
```
以上就是我使用Cursor搭建一个相对完整网站的完整复盘。Cursor并不是万能的，但只要方法对，普通人也能用它独立做出一个能跑、能用、看起来也不差的网站。希望这份避坑指南，能帮你在AI编程路上少走一些弯路。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a54a60d460f99b0f4532c70db952ee32.png>
最近在折腾 Cursor，发现一个特别实用的技巧：让 AI 写代码时，如果能附上现成的示例，效果会好很多。比如我写一个调用大模型的 demo，代码就是直接从 API 文档里复制过来的。
提示词 2
```
很好，现在听我指挥，
1\. 在根目录下创建一个config/index.js文件，用于保存大模型的apiKey
2\. 调用大模型的demo代码是：
```
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
```
你要改成适合我需求的代码，apiKey从config/index.js文件引入
3\. 开始生成网站代码
```
就这么简单的两条提示词，一个能直接对话的聊天界面就搭出来了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d0e29825bb8bdf6c80b86b4b5d3f8a52.png>
整个过程只花了不到十分钟，界面还很粗糙，功能也谈不上完善。但这都不是事儿——你想让它怎么改，直接跟 Cursor 提，它就能慢慢帮你优化。后面有新想法，也可以很方便地往站点里加。
代码我已经传 github 了：https://github.com/leyonglin/cursor-demo.git
clone 下来之后，只需要把 config/index.js 里的 apiKey 改掉，就能直接用。
说完这些，再分享几个 Cursor 的提速技巧。
```
# Role:
Python专家
## Constraints:
- 专注于Python编程相关问题。
- 提供准确、安全且高效的编程解决方案。
- 避免提供与Python编程无关的信息。
## Background:
- Python专家是一个专门设计来解决Python编程问题的智能体。它具备深厚的Python语言知识，能够理解并解决各种编程难题。
## Goals:
- **问题解答**: 提供针对Python编程问题的准确答案。
- **代码优化**: 帮助用户优化Python代码，提高代码效率。
- **学习指导**: 引导用户学习Python编程的最佳实践。
## Skills:
- **编程知识**: 精通Python语言的语法和特性。
- **问题解决**: 能够快速定位问题并提供解决方案。
- **代码审查**: 能够审查代码并提出改进建议。
## Workflow:
- **问题接收**: 接收用户提出的Python相关问题。
- **问题分析**: 分析问题的具体内容和需求。
- **解决方案提供**: 根据问题分析结果提供解决方案或代码示例。
- **反馈循环**: 根据用户的反馈进行方案调整。
## OutPutFormat:
{解释用户的问题}
{解释问题的使用场景}
{知识点如何使用}
## Initialization:
- 简单介绍自己，提醒用户输入问题。
```
**Cursor 建议**
Tab：接受整段 AI 代码建议
Esc：拒绝当前的建议
Ctrl + →：只接受建议中的某一部分
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_459588a1da6420a1f787bd894789a85a.png>
**Chat 聊天**
Ctrl + K：调出内联编辑工具
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fa978003375e509a1057186dd06bd5a5.png>
Ctrl + L：打开 AI 聊天窗口，选中的代码会自动发送过去
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fef4baf43d6357f24dca67fb90147dad.png>
Ctrl + I：打开 Composer 工具窗口
Ctrl + Shift + I：全屏模式打开 Composer
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b07329c62264d1fbda2dc3e704590784.png>
**@ 符号命令**
Files：把某个文件加进来作引用
Folders：把某个目录加进来作引用
Codebase：引用整个代码库
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fd5c8d47c1153196eef77f433aba7673.png>
**通用快捷键**
Ctrl + Shift + P：呼出命令面板，所有命令都在这
Ctrl + , ：打开编辑器设置
Ctrl + B：显示/隐藏侧边栏
Ctrl + `：显示/隐藏集成终端
Ctrl + N：新建文件
Ctrl + S：保存文件
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f3a1dbb89d7c7830460339f19b7b4955.png>
这里专门说说 .cursorrules 规则文件。很多人搞混它和 README.md，但在 Cursor 眼里这俩完全不是一个级别：README 和普通文件没区别，.cursorrules 却是相当于规则/提示词的存在。
```
# Cursor 项目规则示例
# 文件名: .cursorrules
## 代码风格
- 使用 TypeScript 严格模式
- 优先使用函数式组件和 Hooks
- 遵循 ESLint 和 Prettier 配置
## 命名规范
- 组件使用 PascalCase
- 函数和变量使用 camelCase
- 常量使用 UPPER_SNAKE_CASE
- 类型和接口使用 PascalCase
## 文件组织
- 按功能模块组织文件
- 组件放在 components 目录
- 工具函数放在 utils 目录
- 类型定义放在 types 目录
## 测试规范
- 使用 Jest 和 React Testing Library
- 测试文件使用 .test.ts(x) 后缀
- 测试覆盖率要求 > 80%
## 文档要求
- 所有函数必须有 JSDoc 注释
- 复杂组件需要添加使用示例
- README 需包含安装和使用说明
## Git 提交规范
- 使用约定式提交信息
- 每个提交只做一件事
- 提交前进行代码审查
```
.cursorrules 同样是 markdown 格式写的。更多现成的规则可以从 GitHub 上扒：
https://github.com/PatrickJS/awesome-cursorrules/tree/main/rules
再聊一个有意思的案例。龙哥在 Cursor、v0、Claude 上花了 217 个小时，现在 4~7 天就能独立完成一个完整的 Web 应用，前端、后端、登录页、着陆页全都不在话下。
这其实说明了两件事：一是 AI 编程的入门成本极低，学习周期被压缩得很短；二是整个开发周期也大幅缩短。对普通人来说，花一点时间去折腾，绝对不亏。
而且资料也特别好找：菜鸟教程、w3schools、B站、X、YouTube，应有尽有。更奢侈的是，你可以随时随地直接问 AI。
**普通人学编程，到底图什么？**
最本质的作用，就是 AI 编程能让你把脑子里那些创意，真正变成产品。在赚钱这边，学以致用是基本操作——不管学编程还是学 AI 编程，核心就两个字：用起来。学不是为了当摆设，是为了解决问题，是为了赚钱。
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