# 2024年12月 使用 Cursor 航海时踩过的坑以及解决办法汇总

> 来源：[https://ggoff9gymx.feishu.cn/docx/OuWgdGxyZoE9zgx7FbCcTlExnXc](https://ggoff9gymx.feishu.cn/docx/OuWgdGxyZoE9zgx7FbCcTlExnXc)

希望这篇记录能给同样在航海的伙伴们一些参考

### 问题1：报错 pyinstaller : 无法将“pyinstaller”项识别为 cmdlet、函数、脚本文件或可运行程序的名称

当你想把 Python 脚本打包成 exe，并且 pyinstaller 已经装了，运行时却可能跳出这个报错：

[PRE0]

把错误信息直接复制粘贴给 Cursor，它会给出排查方向，如下图：

[PRE1]

[PRE2]

Cursor 通常会提到 Python Scripts 目录，但如果你是从微软商店安装的 Python，就找不到那个常规路径。

实际的有效路径大概是：

C:\Users\[你的用户名]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts

用户名每个人不同，后面的版本号段也可能有差异，按这个规律找到自己的路径后复制，照着 Cursor 的步骤加入环境变量即可。

[PRE3]

配置完成后别忘了重启 Cursor，不然修改不会生效。

### 问题2：按手册做图像压缩网站时，Cursor 没有自动生成 index.html、css、js 等文件

[PRE4]

[PRE5]

不用手动点 apply 应用代码，直接问 Cursor 为什么没有自动生成，它通常就能自己补上。

出现这种情况，多半是 .cursorrules 也就是角色设定文件写得不够完整。我当时也是在 Cursor 提醒后才意识到是角色设定没配好。

另外在迭代需求时，代码里偶尔会留下冗余部分，也可以让 Cursor 自动清理。

让 Cursor 根据当前需求优化一下 .cursorrules，下次就能避免重复发生。

[PRE6]

[PRE7]

[PRE8]

下面是我当时让它更新后的规则示例，原提示词不记得了，不同人生成的内容会不一样：

[PRE9]

### 问题3：git 到底是什么？怎么装？用来做什么？

Git 读作 /gɪt/，是一款开源的分布式版本控制系统，无论是小型项目还是超大规模项目都能高效管理版本。 [1] 它最初由 Linus Torvalds 为 Linux 内核开发而创建。[来源百度百科]

[PRE10]

官方下载地址：https://git-scm.com/downloads/win

如果概念不清楚，先简单理解为一个存放本地代码的在线仓库就行。手册要求把本地代码通过 git 推到 GitHub，但光装好 git 还不够，需要先把本地 git 和你注册的 GitHub 账号建立起可验证的关联。

[PRE11]

假设你已经在 GitHub 新建好仓库，那就继续往下看。

### 问题4：第一次提交或关联远程仓库时出现 error: src refspec main does not match any / error: failed to push some refs to 'github.com:xxxxxx/tupianyasuo.git'

问 Cursor，它一般会给出如下解释：

[PRE12]

实际上核心问题是本地还没有生成 SSH 密钥并添加到 GitHub。

[PRE13]

### 问题5：ssh 密钥要怎么复制？

看不懂上图的提示也没关系，按图中路径找到对应目录，用记事本打开：

[PRE14]

[PRE15]

打开后全选复制即可。

### 问题6：测试 SSH 连接时弹出 The authenticity of host 'github.com (20.205.243.166)' can't be established.

问 Cursor 就能知道原因：

[PRE16]

按提示点蓝色文字，把红框里的内容复制下来

[PRE17]

然后到 .ssh 目录下新建一个名为 known_hosts 的文件，注意不要带 .txt .exe 等后缀，就是一个纯文件名。

[PRE18]

不会看文件扩展名可以参考下图：

[PRE19]

新建完成后用记事本打开，把刚才复制的内容粘贴进去保存。

到这一步你可能仍连不上，继续看下一个问题。

### 问题7：报错 Cannot stat C:\\Users\\Alber/.ssh/known_hosts: No such file or directory

问 Cursor 会得到类似下图的建议，这里重点看红框。默认情况下 .ssh 目录是只读的，需要取消只读属性。

[PRE20]

[PRE21]

取消只读并应用后，我这边测试连接就成功了，虽然目录属性看起来又变回只读了，但实际文件已生效，不影响使用。

### 问题8：提示 Author identity unknown *** Please tell me who you are.

这是因为没有配置提交者身份，也就是 GitHub 账号信息，这项本该在安装 git 后就完成。

[PRE22]

配置好后就能正常提交，并把本地代码推送到 GitHub。推送完后按手册要求，还有一个更麻烦的点。

### 问题9：🔥 怎么注册 Vercel？用 GitHub 登录时提示 Your account requires further verification. Please contact registration@vercel.com to complete your registration.

[PRE23]

我当时在网上找到一个可行的办法，https://blog.csdn.net/weixin_52164430/article/details/143060297

核心就是给官方发一封申请邮件

邮件模板如下，自行修改后发送，记得删掉备注部分：

[PRE24]

邮件发出后官方通常会秒回，表示已收到并进入审核。等待不到 24 小时就会收到通过通知，成功率基本是 100%。

[PRE25]

### 问题10：Cursor 怎么汉化？

直接参考下文里的中文插件配置，建议安装插件时把梯子打开，不然速度会很慢。