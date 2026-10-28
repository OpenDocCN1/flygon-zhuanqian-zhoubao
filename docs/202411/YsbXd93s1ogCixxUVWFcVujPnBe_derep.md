# 用 Automa 把海螺AI图生视频做成自动流水线

> 来源：[https://ktnwm6ohjn.feishu.cn/docx/YsbXd93s1ogCixxUVWFcVujPnBe](https://ktnwm6ohjn.feishu.cn/docx/YsbXd93s1ogCixxUVWFcVujPnBe)

大家好，我是土豆君，混迹代码圈的小程序员。

自从亦仁老大抛出AI视频的风向标之后，圈子里的人都在轮番上阵试工具，Runaway、Canva AI、海螺AI都在榜上。

我自己实操海螺AI时，最大的痛点就是出片太慢、要一直盯着点。于是花了几天把流程做成RPA自动化，下面这套思路你拿去也能复用到别的AI视频平台。

前提是已有海螺AI的会员，或有一批便宜的批量邮箱号来注册帐号，1个谷歌邮箱大约1-3元。国内版每天有免费额度，国际版前三天免费，用这套流就能做到持续批量生产。

![](img/82e0ff9b4bc9480713a6d72f47e57693.png)

先说工具选型。RPA很多人第一反应是影刀，我一开始也一样。后来在研究比特浏览器多开指纹环境 https://www.bitbrowser.cn/ 的过程中，发现它自带了 Automa 开源扩展，才开始深入。

跟影刀相比，Automa的优势是插件形态，能装在任何浏览器里。配合指纹浏览器就能做到十几个窗口同时跑，影刀就做不到这种量级。比特浏览器已经内置了 Automa，工作流可以随意复制迁移，代价是上手门槛比影刀高一点。

官方地址：https://www.automa.site/
中文学习资料：https://automa.wiki ，建议结合B站教程一起看，单靠文档会比较吃力。

下面先说怎么用，以及我为什么这么设计。

## 流程总览

整个工作流的核心思路很简单：用一个固定提示词，批量读取指定文件夹里的图片，循环上传到海螺AI生成视频。如果用比特浏览器多开，每个窗口都是一条独立生产线，效率直接翻倍。

## 演示

![](img/6cd944da6018e7d1ca79eefc01846534.png)

Automa 页面截图：

![](img/295c1a6585a0a7cdcd1cc6276b67fc71.png)

点一下 ▶ 就开始执行，运行中会在扩展图标上显示一个 1️⃣ 的小角标。

![](img/f43c549a86e006ab8694cbd2e51736ab.png)

如果没看到 1️⃣ ，大概率是执行出错了，去日志里排查。查看日志入口：Tips - 查看日志

![](img/625213dc431dca9bf523d319061986eb.png)

运行效果大概是这样：

## 成片展示

## 设计原理

了解原理可以更好定制，需要直接上手可以直接跳过。

在海螺官网实现自动图生视频，难点在于自动上传图片，按钮点击相对简单。

#### 图片预处理

上传需要图片路径清单。我用 Cursor 写了个小工具，把指定文件夹下的图片转成路径列表。

![](img/afa4f74ef533febf5e6a07c93d1b68c0.png)

输出格式是这样的 JSON：

![](img/c7dc33eb1a5d38b12693c9cb13d1a6e5.png)

#### 执行逻辑

开头放触发器，然后通过切换标签页匹配目标网址。

![](img/dcb7f6e5301a73bdd0f1300e6e4dd53c.png)

接着是循环读取数据，用来遍历图片列表，跑完一张回到开头取下一张。

![](img/9526e1207800b58f873e6a6631a29ec0.png)

循环结束靠循环断点判断。

![](img/dcd688feec679d65e183104bcaa739c6.png)

中间加了一段排队检测：判断当前页面是否有3个或5个视频在排队，如果满了就等3分钟再检查一次。

![](img/4491e2d4e4452cb5e6acee09a7c1db7f.png)

随后是写入提示词、上传图片。

![](img/e41ba59156a7bf99098d3553e58e5a09.png)

上传后会空等5秒确认是否成功，失败则重新点一次上传。

![](img/af67cde69a780740137c6feee5bb9780.png)

最后点击生成，并附带是否上传成功、是否进入生成状态的判断。

![](img/45d8daf9840d73606f3a59ef74e4f8de.png)

#### 基础操作说明

以提示词为例，表单元素负责填入内容，右侧的定位📍图标可以吸取页面元素，✔图标用来校验选择器是否有效。

![](img/931eedefd49568c382394288a9d04c16.png)

选元素支持自动框选识别，可用 CSS 选择器或 Xpath。

![](img/602e342e4e7cc4d256cde906252cb15e.png)

![](img/99beb79a680e9fd630a22e36f8aad7f1.png)

在文本框里填入你要固定的提示词到对应位置。

![](img/f66fbf738bc543b0ab87e78213770404.png)

## 使用步骤

#### 1 生成图片列表

文末有附件。解压后先运行：图片处理工具V1.0.exe

![](img/23786e77bf5f7c7fbfaa397d9f149a0d.png)

点“选择图片文件夹”或直接拖拽文件夹进去

![](img/99602092cacd30e3b0f5686604eab45f.png)

也有网页版，操作更简便：

https://imgtool.tudoujunha.parts/

![](img/003f65c1dc859a8d419c7dfca1e4b2e9.png)

注意路径别放太深，否则容易上传失败。建议把文件夹放到根目录或桌面。

点生成后会在同目录下生成一个 image_list_时间.json ，生成完就可以关闭工具。

![](img/1d98db66d72e84a6f56e632517479c1f.png)

#### 2 安装 Automa

Chrome/Edge 用户可通过此链接安装

https://chromewebstore.google.com/detail/automa/infppggnoaenmfagbfknfkancpbljcca

![](img/5206c269f78f90eeadedc0d9149bfbc1.png)

打不开商店就用比特浏览器，在扩展中心直接添加。

![](img/6e7428a68b94fbbd83e2e7426b4edcd1.png)

需要中文界面在这里切换

![](img/b57a92a6f4f9dd2dcd5f6a3b31844841.png)

#### 3 开启文件访问权限

Chrome/Edge 使用时记得给 Automa 开启文件访问权限，比特浏览器测试过默认已开。

把下面链接粘到地址栏打开设置：

```
chrome://extensions/?id=infppggnoaenmfagbfknfkancpbljcca
```

或者去扩展管理里找到 Automa：

![](img/b10668ed74adce1c4602363da689ea0e.png)

![](img/992904fed41230faa6493105f356dbc0.png)

把“允许访问文件URLs”打开

![](img/016575f7dde62c095e473d7af6309fb3.png)

没开会提示：Automa 无权访问文件

![](img/bc274891ba60c28e473af63e7880edf1.png)

#### 4 切换语言

进设置改语言为中文。

![](img/0189e34891975dce56dc81f814c62411.png)

#### 5 导入工作流

打开后导入 RPA 文件：hailuo_auto.automa.json

![](img/2018711110e5cf09aed967d50f387a6c.png)

默认是海螺国际版，国内版用户看下面的 Tips 切换。

#### 6 设置提示词

双击 Forms 卡片填入固定提示词。

![](img/36aff9b08af7fa6e2844f7b22f508826.png)

最新版里填的是 {{variables.prompt_text}}，如果你只用一个提示词，直接删掉变量填自己的词就行。变量的作用是支持多提示词，看 Tips - 使用多个提示词。

![](img/440da230054e6be6f06b67268ef6a6e2.png)

不需要提示词就清空内容或关闭开关，运行时会跳过。

![](img/f5fdbac21056ac0ae7c6835ac8b43337.png)

#### 7 导入图片列表

导入后点工作流卡片打开，找到 Loop data 图片列表，双击或点右上角✏：

![](img/3245d0cf39f5a59962effe78808c52db.png)

左侧显示 Loop Data 详情，点击 Insert data：

![](img/d049232fe59fb2732d352355a470c9e5.png)

点 Import file 选择 image_list.json：

![](img/ebf04ac52ad9c36207ccfca770f94e23.png)

导入成功后点右上角❎关闭

![](img/7f46a9303522c7cad4867a78b2165183.png)

最后一定要点 Save 保存才生效

![](img/420f29c2a3246f676b24853bbbda1bc8.png)

打开 https://hailuoai.com/video 点 ▶ 测试一下。

注意：
1. 运行期间不要操作当前浏览器，可以最小化但不能切标签或开新页，否则会报错。可新建 Chrome 用户或用指纹浏览器多开隔离。
2. 演示基于国内版，国际版基本流程一致，网址需要改一下见 Tips - 切换国际版。

### Tips

#### 多窗口并发

在比特浏览器流程设计里可配置 RPA 任务，会自动打开浏览器和 Automa。

![](img/06f1f5cb00bf3c8aa2ea5364bf5724c4.png)

复制 Automa 工作流的 ID

![](img/e9512086a6a5536aa7af4190831218ee.png)

在 RPA 自动化页面新建任务填入 ID，就能多窗口同时跑。

![](img/aff84df33854499a6160f64f90dc772f.png)

![](img/9aed6491017d3f66d2f6fc309a1e76f1.png)

如果不想改配置，也可直接多开窗口各自装 Automa，按需启用。

![](img/af57628f4b51701dc76912377ffd0f47.png)

#### 调整检测间隔

默认每3分钟检测一次生成位是否空闲，单位是毫秒，可自行改。

![](img/1f70c6ef672a8bbf5f469c9a06739d57.png)

#### 日志查看

点日志可看到当前工作流运行记录，选 hailuo_auto 能看到详细报错，右侧显示运行状态，可停止。

![](img/0d365059074ba11d215b16cd960dcad6.png)

点 Stop 停止正在运行的任务

![](img/5e0830dd4f1d02d962b751c89ea48fc6.png)

点标题展开详细日志

![](img/a80b1044a1b5d57b76dcfc7ce02574e5.png)

#### 国内/国际版切换

国内版：https://hailuoai.com/video/create
国际版：https://hailuoai.video/create

切换时把标签页的链接改掉即可。

示例：国内 https://hailuoai.com/video/create 改为国际 https://hailuoai.video/create

![](img/8f932cf2133dc2549fd38ea48081d8fe.png)

![](img/9985bca6fe35d8e8b11fc7135cb09e19.png)

运行前记得把网页切到 Image to Video

![](img/133e73bd4a4182cc15776ef088da512b.png)

#### 用 F12 看进度

在运行页面按 F12 打开控制台，可看到打印日志，比如 loop-index: 0 image_xxx_0.png，代表当前是第几张图。错误信息可忽略。

![](img/67079ea31a71f38a57016fb90f791c0a.png)

#### 上传失败处理

如果生成视频尺寸不对，说明是文生而非图生，大概率上传失败。若偶发，可把工作流里两个5秒延迟改成10秒。

![](img/5f98fd7e2203959a6c019240674fd059.png)

![](img/1387f3e33d862ac4a9ca4ccc62ff0cef.png)

#### 多提示词方案

现在支持按图片序号自动换提示词。例如前99张用提示词A，100-299张用提示词B，以此类推。

找到 JavaScript 块双击

![](img/6e4a1e707ce91683b59f9368d02d3817.png)

点进代码区

![](img/1b8507c9a3ac897e16e7daa970e49661.png)

按格式填入自己的提示词，注意保留引号。

```
automaSetVariable("prompt_text", 
  loopData.$index < 100 ? "第一个提示词" : 
  loopData.$index < 300 ? "第二个提示词" :
  loopData.$index < 450 ? "第三个提示词" :
  loopData.$index < 500 ? "第四个提示词" :
  "超过500的提示词"  // 当索引大于等于500时使用的默认值
)
```

代码逻辑：0-99用第一个，100-299用第二个，500+用最后一个。

![](img/c39a4d7d8b02c8987357b0e438e41737.png)

然后在 prompt 表单里填变量 {{variables.prompt_text}}

![](img/23e571c0a56eadc21f033f4482195f0d.png)

## 附件

#### 海螺AI工作流

下载：https://gitee.com/tudoujunha/rpa-gpt/releases/download/v1.0/hailuo_auto.automa_v1.0.json

#### 图片处理工具 Web 版

imgtool.tudoujunha.parts

![](img/33ed5fe7b8ee5afa1681bda4812330b9.png)

#### 图片处理工具 Windows 版

Win 版 exe 下载

![](img/27733476d828004b480a9f8fb554bc60.png)

Win版图片处理工具下载🔗

#### 图片处理工具 Mac 版

Mac 版打包下载：

Mac版图片处理工具下载🔗

#### 源码

Python 源码：

![](img/711d6f930549cd1da04ac88237cd15e2.png)

运行命令：

```
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Mac/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 然后安装依赖
pip install pillow

# 运行脚本
python filepath2json.py

# 打包命令
#### Windows
pip install pyinstaller
pyinstaller --onefile --windowed filepath2json.py

#### MacOS
pip install py2app
py2applet --make-setup filepath2json.py
python setup.py py2app
```

今天逛Gitee的时候发现一个挺实用的小工具，来自rpa-gpt这个项目，是一个叫filepath2json.py的脚本文件。

这个脚本挺有意思的，从名字就能看出来，是处理文件路径和JSON之间转换的。在自动化流程或者数据处理的时候，经常需要把文件路径整理成结构化格式，手动搞又麻烦又容易出错，这种现成的小脚本就派上用场了。

想直接拿代码去用的朋友，我把传送门放在下面了：

https://gitee.com/tudoujunha/rpa-gpt/blob/master/filepath2json.py

有需要的话可以看看，对这种小工具感兴趣的朋友可以收藏一波。

#效率工具 #Python #自动化 #实用脚本