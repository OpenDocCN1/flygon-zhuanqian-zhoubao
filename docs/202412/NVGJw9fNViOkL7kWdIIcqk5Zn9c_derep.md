# 用 Cursor 搞定浏览器插件开发
作者：龙哥



# 1、环境准备

## 1.1 Node.js 是什么

Node.js 是一个开源的 JavaScript 运行环境，核心作用是让 JavaScript 跑在服务器端。

通俗讲，它让同一门语言能同时写前端和后端，从而省去来回切换语言的成本。

它的底层采用事件驱动、非阻塞 I/O 设计，因而特别适合构建可扩展的网络服务，比如 Web 服务和 API。

对新手而言，可以把 Node.js 理解为一个像浏览器一样执行 JS 代码的容器，只是运行位置在服务器上。通过它可以开发后端服务、命令行工具，甚至桌面应用。

总体来说，Node.js 提供了高效灵活的 JS 运行平台，显著提升了开发效率与可玩性。

## 1.2 NVM

### 1.2.1 简介

NVM 全称 Node Version Manager，是专门管理 Node.js 版本的工具，和 Node.js 配合使用。

简单理解：

* Node.js 负责提供 JS 运行环境；
* NVM 负责在同一台电脑上装多个 Node 版本并自由切换。

NVM 的价值在于：

1. 在一台机器上同时维护多个 Node.js 版本，适配不同项目的版本需求。
2. 一键在不同版本间切换，无需反复手动卸载重装。
3. 保证项目运行的 Node 版本和项目要求一致，避免兼容性问题。

总之，NVM 能让版本管理更省心，开发更顺畅。

### 1.2.2 安装步骤

#### 1 下载
下载地址：Releases · coreybutler/nvm-windows

![](img/43b274dfd4d0219e1844b8faa4a3d4d6.png)

点选下载安装包。

![](img/c2f427ae30ca358432fb194b66b41a43.png)

下载完成后双击运行即可。

#### 2 安装
不建议装在 C 盘，除非 C 盘空间充足。

![](img/e24fc444b0f1673fca3e3a2b7c4d222b.png)

![](img/0701e83143350aa737ef88f1531ef135.png)

点 Install 后确认安装。

![](img/fbc5235aeb8d8045c0104dd1aa3800d6.png)

#### 3 验证
安装完成后打开终端输入 nvm -v，如果能显示版本号就代表成功。

![](img/0a4890146f66622b7e205db7072fe82f.png)

![](img/1dba9d8f9ea6246a2c950e4ccaef8581.png)

#### 4 换源配置
安装成功后进入 NVM 安装目录，找到 settings.txt 文件。

![](img/e1873b0ac1aa00888ca4e025deacb32e.png)

```
node_mirror: https://npmmirror.com/mirrors/node/
npm_mirror: https://npmmirror.com/mirrors/npm/
```

#### 5 环境变量配置
右键此电脑打开属性

![](img/b97cc267d9379dd7cba7107a2cfa4d62.png)

进入高级系统设置

![](img/769c569f259201c693da46756d3cd9dc.png)

打开环境变量

![](img/0a96e5212c3c16ebd640d6461c9a4565.png)

在系统变量里找到

NVM_HOME

NVM_SYMLINK

没有的话可以新建。

随后把这两个变量加入到 Path 中。

![](img/78c9da04e4f8916d4ac557708117937b.png)

选中后点编辑。

%NVM_HOME%

%NVM_SYMLINK%

### 1.2.3 用 NVM 装 Node.js

在终端执行 nvm list available，可查看可安装的版本列表。

```
nvm list available
```

![](img/29e5aabcca0da43dc6e713226f3bde24.png)

执行 nvm install xx.xx.x 安装指定版本，例如

```
nvm install 18.20.5
```

![](img/96ecf88460d694d5e6b8148bddc2b1ab.png)

查看已装版本，带 * 的是当前激活版本。

```
nvm list
```

![](img/3773361bfa72bf56142de0c3596594cb.png)

切换版本用：

```
nvm use 18.20.5
```

![](img/24e28cf995fdebe25f9a7ea2a0b49489.png)

NVM 常用命令一览：

# 2、脚手架初始化项目

## 2.1 为什么要用脚手架

开发伊始，很少有人会完全从零手写代码。脚手架能给开发流程划定边界，防止 Cursor 完全自由发挥，按自己的“标准答案”生成代码导致一堆坑。

个人踩坑经历：以前按教程让 Cursor 从零建浏览器插件，它喜欢用链接方式引入依赖，结果链接失效，模型又没及时感知，直接卡死。

现在前端依赖管理主流是 npm、pnpm，靠链接拉依赖的做法已经过时且不稳定。

这次用的脚手架是 AI 推荐的 chrome-ext，实际体验下来还挺顺手。

下面是 Claude 的说明

![](img/fd2549bbc6ef2ffab9c9a726f2af5b14.png)

## 2.2 项目初始化

找一个空文件夹。

在地址栏输入 cmd 回车打开终端。

![](img/811e25a865d2b7b4c42cc366f246c00b.png)

执行初始化命令，输入项目名，建议用英文，减少不必要的编码问题。

```
npm create chrome-ext 项目名称
```

直接回车使用默认包名。

![](img/feefa989ea50268f66c78e189aebeb85.png)

选择技术栈，有前端基础的选自己熟悉的，我习惯 Vue，所以选了 Vue。

![](img/46f69f19635846c5a3a8d9032d055af4.png)

语言选 JS 或 TS 都行。

打开文件夹，就能看到初始化好的项目结构。

![](img/90c1b88bb19ace52506894ad47f0ad6e.png)

用 Cursor 打开项目。

# 3、开发流程

## 3.1 新建 .cursorrules 规则文件

我的习惯是开工前先建一个 .cursorrules 文件。

它相当于给 AI 的项目写作规范，规定代码风格、命名习惯等。

我的做法是从 Cursor Directory 里找对应的技术栈模板，复制出来让 Chat 帮我改写成适配当前项目的版本。

![](img/101d1d9fc48a0f241c1b123fd5ae8279.png)

![](img/0b3cb090dfb29d19d8fa8b29d107b6fe.png)

直接选第一个。

![](img/36281bad0e9ec85bf5a1cf97e1fd4187.png)

随便挑一个复制。

打开 Cursor 新建对话，把复制的内容粘贴进去。

![](img/53449b1a242ca9583f425264cacaba14.png)

回车后就能生成适配本项目的 .cursorrules 规则。

复制内容写入 .cursorrules 文件中。

![](img/5b1e1f0d870a636c8538b2e5a025ca46.png)

## 3.2 用 Chat 生成产品需求文档

刚开始脑子里往往只有一个模糊想法，具体交互和实现没头绪，这时我会让 AI 先出一个产品需求文档，拿来就能用。

同样在 Cursor 新建对话。

![](img/52cf5d882fc72c6fe447600491e7dda1.png)

生成后点击复制。

再把文档放到 NOTEPADS 方便后续引用。

![](img/bb55c3cd099be89272d1511a8728139e.png)

粘贴内容进去。

![](img/aa5163bff2df49f6f3e07cb467fe79f5.png)

重命名文档。

![](img/43215f6715cf04b1ef9b1b954ec4943e.png)

之后在对话里就能直接 @ 该文档调用。

![](img/6e676a2d465dabfc647a6890dc3d9a0c.png)

## 3.3 让 Cursor 按需求文档开发

把模式切到 COMPOSER，选择 agent 模式，模型用 Claude-3.5。

![](img/30469cede2b2a5008c5581a5be51abc2.png)

开始下指令，让 Cursor 执行开发任务。

随即你会看到它迅速创建并写入相关代码文件。

![](img/299fcfa6e8348d939b5b8dc9a83d6e9e.png)

任务完成后它还会提示安装和测试方法。

提醒一下，如果中间没自动执行打包，需要自己在终端手动执行。

![](img/abd5480cbea5b747b975a8fcaffffcd5.png)

# 4、测试与迭代

基础代码完成后进入测试迭代阶段。

心态放好，运气好一次通过，运气差就把报错贴给 Cursor 修复。

先打开 Chrome 扩展管理页：chrome://extensions/，并开启右上角开发者模式。

![](img/2f2d5c3303d17a640a55ae991839f0fb.png)

![](img/918c97b1716c22dfa9615b4d7bdb910a.png)

载入已打包的插件。

![](img/42336022eb9bded771330dfd1c2fd165.png)

打开任意网站验证效果：百度一下，你就知道

![](img/d00d77eb1910c17a4e9471de5f6e5520.png)

运气不错，直接成功了。

如果失败，把报错信息复制给 Cursor 即可修复。

![](img/8033d0358275b4dcf28e0bdb4f0e6c4d.png)

报错一般会显示，点击进去能看到详情。

![](img/e2d02d07f26e744b4b8bf38032672fa2.png)

把错误信息截图或复制给 Cursor 修复就行。

## 4.1 迭代

![](img/8db3e0c3cd7a05c07cdc284984dff7d3.png)

迭代前务必先用 Git 提交一次代码！不懂 Git 直接问 Cursor。

![](img/bc141b20d0284385110d383ee86e7bac.png)

如果 Cursor 没帮你执行构建命令，就手动在终端执行。

![](img/6cd1550fdb3e05a24dd07ba65c92554f.png)

看看最终效果。

感觉挺满意。

![](img/90a697d93edb7199baac8c367a5a3543.png)

## 4.2 插件安装

最后附上插件压缩包