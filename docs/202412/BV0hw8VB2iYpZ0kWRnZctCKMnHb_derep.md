# 不懂代码也能搞定！用Cursor从零打造B站视频下载工具，还顺手部署上线

> 赚钱圈友大家好，我是红哥Frank。干了多年项目经理，写代码这件事对我而言完全是盲区，但我特别迷AI编程。11月刚成了赚钱传术师，又赶上【Cursor-零基础做软件应用】12月航海，以志愿者身份混在队伍里，见识了不少船员在实操中踩坑。海伦领队让我出来做个分享，给零基础的朋友打打气——我都能做出来，你们肯定也行。于是就有了这篇全程手把手、细节拉满的实操记录。

先看成果：下面这个界面，就是我用Cursor做出来的B站视频下载工具。它具备这些能力：

1. 输入B站视频链接，点击【解析视频】，就能把视频的基础信息抓出来，比如发布时间、UP主、点赞数、投币数、收藏数等，一览无余。
2. 可自由选择想下载的清晰度。
3. 点【下载视频】按钮，就能把视频存到本地。
4. 历史下载记录也会被好好保存下来。

![](img/356693a6c7dda73b6de7572e0475e4be.png)

---

## 第一步：建项目文件夹

在电脑上随便找个地方，新建一个空目录，名字就叫 `bilibili-download`。以后所有代码都会在这个文件夹里生成。

## 第二步：用Cursor打开文件夹

启动Cursor，点“Open a folder”，选中刚才建好的那个目录，然后点【打开】。

![](img/2bd957896622d8ce152945feeb9a5be0.png)

![](img/5e4c01ea416dbb018dcfccc05763abd8.png)

![](img/1728bf38c4286da415da1150f015a4cf.png)

看到左上角只有一个大写的 `BILIBILI-DOWNLOAD` 就对了，现在里面空空如也，一切从零开始。

## 第三步：把需求讲清楚

用Cursor做应用，最核心的功夫就是“说人话”。下面这份是我当时写的需求描述，你可以直接参考，也可以按自己的喜好改。

> 我想做一个在线的B站视频下载工具网站，主要功能如下：
>

>
> 2. 用户要能选下载清晰度，所以需要一个下拉列表，列出所有可用的清晰度。
>
> 3. 【解析视频】成功后，用户点【下载视频】按钮，系统开始下载到本地。下载过程中要有实时进度条，下载完成后提示“下载成功”。另外，要展示历史下载记录。
>
> 4. 网页标题命名为：红哥的视频下载器。
>
> 5. 页脚footer显示一行字：© 2024 红哥的视频下载器，仅供学习使用，联系人：红哥，邮箱：hong420802#gmail.com
>
> 6. 整个页面做成响应式，适配各种屏幕尺寸，前端框架用Bootstrap。
>
> 7. 我是0基础用户，从没写过代码，用Mac电脑。希望你先把我的需求吃透，规划好技术架构，给我一些建议，并把方案输出到 `bilibili-download` 文件夹下的 `Readme.md` 文件中。

## 第四步：在Chat里聊需求

把上面这段需求复制下来，扔进Cursor的Chat窗口，让它帮你完善并生成 `Readme.md` 文档。

![](img/5216b3d115ebc482609ffa830bf58955.png)

![](img/1476674975c45228c65a38b4d0af03b3.png)

Cursor会输出一份详细的Readme，介绍项目并推荐技术栈。如果它没有自动在项目文件夹里创建文件，就手动新建一个 `Readme.md`，把内容粘进去保存即可。

![](img/a1b77e449c88dbad52e881428f1b4130.png)

![](img/a6ce44f4a4fee6c21c5d63e062e22d6a.png)

![](img/815b1fa7a9e0f86b3377467516b00dc9.png)

## 第五步：在Compose模式里写代码

### 5.1 让AI生成框架和代码

在Cursor右侧切换到Compose模式，输入：

> @ Readme @ Codebase 这是我的B站视频下载的需求说明书Readme.md，请你理解我的需求，并帮我实现。

回车后稍等片刻，Cursor就会自动生成代码、自动创建文件。右下角出现【Accept all】时，点击接受所有修改。

![](img/167a61a093d11bdcee34824c04ac3ced.png)

接着，Cursor会给出运行项目的步骤说明。照着操作，就能把项目跑起来。

![](img/1ee043ab97bb8d9bd3a3caaa8b5aab8b.png)

```
确保已安装所有依赖：
pip install flask yt-dlp requests
```

![](img/f007cc70ac60a8c1faa887d380fd0308.png)

![](img/8e2d18f096ff4bbc53e3bdd0c1777f01.png)

![](img/5ae4cf628599c84c25ad7a76cd4e02cf.png)

![](img/4fd0bce843502f8a713d15f429f33e7b.png)

![](img/e4911701a50893ac961b0b0920f5aacf.png)

![](img/9264d350ad8f2a6e3f2a82d795e84815.png)

![](img/38fe69c663f5edc808147f9910278a51.png)

![](img/4ea5482448a935eed60a8f139a9b7745.png)

在浏览器里访问 `http://127.0.0.1:5000/`，就能看到界面了：

![](img/8efe62c8f005a3b27d41adfc678822bc.png)

```
创建项目目录结构：
mkdir -p bilibili-download/{static/{css,js,img},templates,database}
```

### 5.2 测试并让AI修Bug

我随便找了个B站视频，输入链接，点解析，结果报错了。把报错信息直接发给Compose窗口，然后点Accept all。

> ERROR: [BiliBili] BV1L1zJYHET3: Requested format is not available. Use --list-formats for a list of available formats

![](img/a99dd42e5bec96baa443329da034b614.png)

![](img/cbfb724df41c29c071bdb907afa86c6d.png)

刷新页面，再试一次。我常用的测试链接是这个（后续修Bug一直用它，方便对比效果）：

`https://www.bilibili.com/video/BV1L1zJYHET3/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=9b4215a6fed2d68ee59316b639bf92d2`

![](img/b474e36db2d199651b5c443770c21729.png)

又发现几个小毛病：

1. 封面图没显示出来。
2. 解析出来的字段太少，只有“播放”和“点赞”，我想要的那些字段（封面大图、标题、描述、上传时间、Up主、分辨率、文件大小、播放量、点赞数、收藏数、投币数、转发数、弹幕数等）大部分缺了。

先不管这些，优先测核心功能——下载。点击下载，片刻后提示下载成功，历史记录也完整记下了。

![](img/486a42a7b70d545a6f6e8b5391f493df.png)

![](img/30fc18449248ff3297420ed8dd2757e1.png)

![](img/736787ab083ff61c7ad8b4f670264674.png)

下载和历史记录一次通过。接下来回头优化刚才的小问题。把页面截图粘贴到聊天窗口，再附上问题描述发给Cursor。

![](img/5b6a30e808bb8f4a752bf98e556d288a.png)

![](img/6219742e0ca8e42161ddda8a5aa3e9e0.png)

等Cursor改完，点Accept all，再次测试。结果倒好，页面直接打不开了，后端日志一直刷：`"GET /static/img/default-thumbnail.png HTTP/1.1" 404 -`。继续丢给AI。

![](img/d85473519deda344d57567048a3fb2fc.png)

点Accept all。但发现Cursor没自动创建img目录，于是自己动手新建 `img` 目录，并创建 `create_default_thumbnail.py` 文件，把内容复制进去保存。

![](img/8624e9ed42989cca9978e564cc4cedc3.png)

再把Compose里没自动执行的命令手动跑一遍。

![](img/72e1aec61b949005b16c4db8788a5f97.png)

继续测试，又报错了：`'<' not supported between instances of 'NoneType' and 'int'`。继续发给Cursor，等它处理完，Accept all。

![](img/351b6146b92a1650a3ff43b06ba3e1a2.png)

再测，字段比之前多了，但有些字段没取到值，封面还是没出来。

![](img/49dcfff8cb8ed57dbc57d94597488cee.png)

继续找AI解决：



![](img/9532a270e4cb01209dea7d5d0fa1dd9e.png)

测试后发现，字段解析正常了，但封面图还是不行。

![](img/b7b002cf2decb67e1306a5aa1c900ed1.png)

继续追问AI：



![](img/a1fbc2205c5bdeac6f7cd0ddcfa38ff5.png)

这次Cursor说用了代理接口来获取和显示图片，应该没问题了。刷新页面，输入URL，点解析——成了！封面图终于显示出来。

![](img/49c651ef03e19a58be42d980a36be500.png)

再整体测一遍完整流程：选择下载清晰度时，发现文件大小没有显示，继续让AI修。

![](img/ad63118ce1a1fa9831c19dcc1452c2d0.png)

![](img/159abc94375ad14afec62a6a9433c027.png)

再次测试：解析参数正常、封面正常、清晰度下拉正常、文件大小显示正常。点下载，下载成功，历史记录也完美。

![](img/c0451474436ef4b588487f3a706d17fd.png)

![](img/bc1fac15140c4ea2ccdb10a09407075e.png)

![](img/24501980e01d8572bd0f1c2575433b2f.png)

整个流程走下来，功能完全正常。回顾一下：AI一次性生成代码后，启动遇到3个问题，修封面、补字段、加文件大小，总共对话10多次，大约半小时搞定。

---

## 第三部分：用Git管理代码

Git是代码版本管理工具，相当于给项目做备份。万一本地代码环境出问题，随时可以还原。怎么用Git？直接问AI。

> 我现在需要把代码同步到Github，我要怎么做，请一步一步教我

![](img/0049de637fc7991ab5948ed2308dc00d.png)

下面就是跟着AI教程一步步实操的完整过程。

### 3.1 把代码同步到Github

#### 3.1.1 注册Github账号

打开 https://github.com/ ，没账号就注册一个，步骤很简单，不啰嗦。

#### 3.1.2 新建仓库

登录后，点右上角“+”号，选“New repository”，填好仓库名，选Private，保存即可。

![](img/3ea575103913b0d390a75111d1ce7b25.png)

![](img/f4861c681604d572b8865c285deeb39c.png)

看到这个界面，就说明GitHub仓库建好了。

![](img/f164854e7440ae23c7e898d306564dff.png)

注意：
- 如果你不想让所有网友看到你的仓库，选 **Private**。
- 如果你想公开，选 **Public**。

#### 3.1.3 本地初始化仓库

在项目根目录打开终端，运行下面的命令来初始化Git仓库（如果还没初始化的话）：

```bash
git init
```

```
git init
```

截图如下：

![](img/60051b79b1b2031f60e110fd86fdcea9.png)

#### 3.1.4 添加远程仓库

把刚刚在GitHub上创建的仓库，添加为本地项目的远程地址。我的用户名是 `frank202020`，仓库名 `bilibili-download`，所以命令是：

```bash
git remote add origin https://github.com/frank202020/bilibili-download.git
```

```
# 添加远程仓库（将 YOUR-USERNAME 替换为你的 Github 用户名）
git remote add origin https://github.com/YOUR-USERNAME/bilibili-download.git
```

![](img/3f754d88520e2a776f4a48d4ce3b71ed.png)

#### 3.1.5 添加文件到Git

把所有文件加入到版本控制中：

```bash
git add .
```

```
git add .     // 意思是把本地代码放入到暂存区
```

![](img/630a3d3d9df12c9ed4160aee59b239c9.png)

#### 3.1.6 提交修改

运行：

```bash
git commit -m "第一次提交，实现B站视频解析与下载"
```

引号里的内容可以根据你实际实现的功能来写。

![](img/3f891a66388e534f942872153412df7f.png)

#### 3.1.7 推送到Github

把本地代码推送到GitHub仓库：

```bash
git push -u origin main
```

![](img/d6bc547f92deefc1ad7fa9d4f9f99699.png)

到这里，代码就顺利备份到GitHub了。整个过程对我来说没什么难度，你照着做，也一样能搞定。

希望这篇实操分享，能给想学Cursor的圈友带来信心。你能做出来这个应用，就能做出来更多应用。

打开 Github 看一下，目标仓库 bilibili-download 已经在上面了，代码、提交记录都齐全，直接搞定。

![](img/c8f344f3aa1c6380491d7b194174ee9a.png)

## 3.2 本地把 Github 代码拉下来

执行克隆命令：
git clone https://github.com/用户名/仓库名.git

例如克隆我的 bilibili-download： 
git clone https://github.com/frank202020/bilibili-download.git

## 3.3 在本地新建分支并推到 Github

```
git branch -a   // 查看所有分支
git checkout -b 分支名称
git push -u origin 分支名称
```

下面给出一个实操案例，供你参考。

![](img/62a0a2cdb823f8312cf45bcdc5f947d1.png)

![](img/624f4093cf084e774c3e3e005221c1f8.png)

## 3.4 移除已关联的远程仓库

有时需要把本地项目换到另一个远程仓库，就要先把之前的远程源删掉。

具体操作如下：

```
查看当前远程仓库：
git remote -v

移除远程仓库：
git remote rm origin

添加新的远仓库：
git remote add origin 新仓库地址

验证是否移除成功：
git remote -v  # 如果没有输出，说明已经成功移除
```

## 3.5 强制让本地覆盖远程代码

我之前就遇到过这种情况：希望以本地为准，把远程强制更新成本地版本。借助 Cursor 给的教程整理了流程，有类似需求可以直接照做。

```
如果你确定要用本地版本覆盖远程版本，可以强制推送（谨慎使用）
git push -f origin main
```

建议的完整步骤如下：

```
# 1\. 先获取远程更新
git fetch origin

# 2\. 合并远程分支
git pull origin main --allow-unrelated-histories

# 3\. 解决冲突（如果有的话）
# 编辑冲突文件...

# 4\. 提交更改
git add .
git commit -m "Merge remote changes"

# 5\. 推送到远程
git push -u origin main
```

## 3.6 把本地恢复成 Github 上的最新版

这种情况常见于：本地用 Cursor 改着改着，把之前能用的功能改坏了，修不回来。这时可以拉取仓库最新代码做重制，让本地回到 Github 提交的状态，再在此基础上继续开发新功能。

```
git fetch origin # 获取远程仓库的最新内容
git reset --hard origin/main   # 执行重置操作
```

重点提醒：

本地的功能一旦完成，一定要及时 push 到 Github 备份。以后才有回滚的可能。

# 四、部署到自有云服务器

想自己管服务器的话，可以用宝塔面板，上手很友好，Cursor 教练也推荐过。

## 4.1 安装宝塔面板

我买的是腾讯云服务器，购买完成后宝塔面板已预装好。

如果你的服务器没有预装，可以直接问 Cursor：我的服务器要装宝塔面板，请一步步教我。

安装过程就不贴图了，自己动手即可。

## 4.2 登录宝塔面板

![](img/f0d5471429c367d8a407c79fa0e0d91c.png)

## 4.3 新建项目目录

在根目录 www/wwwroot 下新建一个文件夹，命名为 bilibili-download，和本地项目名保持一致。

![](img/0fad144054f47f80b6e16431cac34af2.png)

## 4.4 把本地代码上传到服务器项目目录

![](img/df81cfca66ceb6d0bdda7ea84c0bb49f.png)

![](img/4753b34261e1f82bb0ea0f447a6715db.png)

解压完成后，这个 bilibili-download 文件夹就是上传上来的项目代码。

![](img/c821c55530c0fb57d0be4b681b1d0d60.png)

## 4.5 添加网站

项目是 Python 项目。进入宝塔面板左侧菜单：网站 -> Python 项目 -> 添加 Python 项目。

![](img/793c973f261df4999e74d0b67dfb1e56.png)

在添加页面的配置项注意填写完整，第一次操作可参照我截图的配置。

![](img/b6a2a7435e6c40f3f79428024ec891da.png)

如果项目未启动，可以手动点一下启动。

![](img/7494e0ce627aad1c7aa4fae9da9e61ac.png)

![](img/c5eb4e4cc139d823ccf2162c58268ccb.png)

## 4.6 在宝塔配置端口映射

应用运行端口是 5000，需要放通，外部用户才能访问。

![](img/1b701bdfc86fa9c2de2352c3991460ca.png)

![](img/6e9e39a6ea88771747ea1ab54555f7f2.png)

## 4.7 云服务器安全组放行端口

下面是腾讯云后台的截图。其他云厂商的操作逻辑类似，有问题可以问 Cursor。

![](img/3288d0f4d61c8ec80e40ecd2f9854b45.png)

![](img/9442b995597405326e40181284e352bb.png)

## 4.8 为网站添加域名

宝塔面板中，网站 -> 点项目名称 -> 域名管理 -> 添加域名。

![](img/21ab3b9005872387bd543c2d8049a2ad.png)

## 4.9 解析域名到服务器 IP

登录域名注册商后台，进入域名管理，找到对应域名。

添加记录，创建两条 A 记录：
主机记录：@   记录值：你的服务器 IP
主机记录：www 记录值：你的服务器 IP

这样域名就解析到服务器了。

下面是我在阿里云域名管理里的配置截图，仅作参考，其他厂商操作基本一致。

![](img/cd5a06b972932b7d97eff80bdf4b9bb3.png)

![](img/7f2a88fb1a56aa532249d00e92311739.png)

到这里就结束了，测试一下 域名:端口 能否访问项目。

访问成功，功能也正常。 注：我的腾讯云服务器正在备案中，域名解析被要求暂停，只能先用 IP 临时访问。

![](img/7dd1081e2ad75a7cf725f083e4f77c8b.png)

# 五、在 Vercel 部署

不想买服务器或者想做 MVP 验证，可以把本地应用部署到 vercel.com，零服务器成本。

## 5.1 前置准备：完善配置

本地开发完成后，先提交到 Github 备份。要发布到 Vercel，可以问 Cursor 还需要做什么，它会一步步告诉你。

问法：
我的项目代码开发完成了,我想部署到vercel.com，我还需要做哪些工作，请一步一步详细的指导我完成

![](img/2d12d0efb47414f8e49c604b45d1fa71.png)

在项目根目录执行
pip freeze > requirements.txt
然后 Apply 创建 vercel.json

![](img/01fde54d1708fb17870a2d93cd92512d.png)

OK，重新同步代码到 Github。

![](img/61b01bf0bc4db466ec78a7cc2f6ea6bb.png)

## 5.2 在 Vercel 新建项目并部署

### 1、登录 Vercel.com
浏览器打开 www.vercel.com，登录账号。没有账号就注册，注册流程也可以问 Cursor 一步步教。

### 2、新建项目
进入 vercel 后点右侧 Add New -> Project

![](img/4c616b4b53af47ad00449aed07683b49.png)

### 3、处理 Vercel 权限
会弹出 Import Git Repository 的窗口。

输入项目名 bilibili-download 搜索，会弹出 Config Github App

![](img/4d414129f2a3a34746d1e8da611f96bd.png)

输入 Github 密码，授权 Vercel 访问你的 Github 仓库。

我选择的是 Only delect repositories，下拉选择前面新建的仓库名 bilibili-download，点击 Save 保存。

![](img/6c697e4b816330a796630abc109e5a90.png)

![](img/7b0103d6ef5f2055634f32544abe3976.png)

### 4、导入项目代码
点击仓库 bilibili-download 右侧的【Import】按钮导入。

![](img/81e0f316c5f94752111018b2595052c8.png)

### 5、部署项目
在这个页面无需修改，直接点 Deploy 即可。

![](img/4c169adc9ae93d8fa1d097c2ab45bf02.png)

等待片刻，Vercel 部署完成，Status 变绿，并给出分配的域名即可访问。

Status 为绿色且能看到网页预览图，就代表部署成功了。

![](img/cdb66c650f8cc86bbeb7f9e6f52a248c.png)

# 六、注意事项

1. 每次开始开发前，先激活虚拟环境。
否则会出现 python 命令不存在、版本不对等错误。实际上都已安装，只是要在虚拟环境中使用。
cd bilibili-download // 进入项目目录
source venv/bin/activate // 激活虚拟环境
python app.py // 启动 Flask 服务器

2. 学会用 Cursor 解决问题。
航海期间发现很多人本地问 Cursor 会，但部署到服务器后报错就不会了。
你可能会抱怨本地好好的，部署到 Vercel 或服务器总出奇怪问题。这很正常，别焦虑。我也遇到过，多半是环境和依赖问题。查看 Vercel 的 runtime log，再丢给本地 Cursor 分析即可。
有具体日志给 Cursor，它会给出针对性方案。
比如我部署服务器时遇到的 WSGI 和 requirements 依赖未装好。

![](img/417303126a5e874cb1afd8fd56bd13c6.png)

另外新手部署服务器常遇到 502 页面、Nginx 起不来、403 forbidden，这些基本都是 Nginx 配置问题。我部署时都碰过，排查很痛苦。但有 Cursor 帮忙，把相关日志反馈给它就能得到指导。

3. 做好 Git 备份。
本地做完应用，或完成一个页面、一个按钮、一次小优化，都要养成及时提交 Github 的习惯，就像写 Office 文档要习惯保存一样。避免 Cursor 改着改着把 Bug 搞得更糟。有备份就能拉回之前的提交版本。

总的来说，AI 编程遇到的 99% 问题，只要你学会提问，多半都能解决。
我用 Cursor 以来，99% 的问题都解决了，只是耗时长短不同。对新手来说，解决过程会比较折磨。
因此需要好心态和耐心。遇到问题别慌别放弃，勇敢面对。累了就休息，再回来攻克。

# 七、感谢

感谢本次 Cursor 航海，海伦领队，让我有机会写下这篇船员分享。

感谢航海的各位教练，尤其是大铭教练、michael 教练，从你们的领航、点评和分享中学到不少。最经典的观点是：要和 AI 协作，不要把 Cursor 当外包，要把它当同事，让它帮助我们生长代码，而不是生成代码。

也感谢阿紫教练，是我的 Cursor 启蒙老师，看了你的贪吃蛇教程后就爱上 Cursor。

最后祝大家龙哥盟，一起学 AI 编程，这个真的上瘾。
期待大家沉迷 Cursor，沉迷 AI 编程做应用，创造自己的产品，提升效率或实现商业变现。