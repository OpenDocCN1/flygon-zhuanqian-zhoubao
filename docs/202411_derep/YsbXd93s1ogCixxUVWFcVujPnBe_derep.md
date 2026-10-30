# 海螺AI图生视频太慢？我用RPA做了一键批量生成的工作流

大家好，我是土豆君，一个程序员。

自从亦仁老大放了颗AI视频风向标，圈子里的小伙伴都在玩各种视频生成工具，比如Runway、可灵、海螺AI。我自己试海螺AI的时候，发现它出片速度真心有点慢，于是琢磨着能不能让它全自动跑。折腾了几天，写了套RPA工作流，今天就分享给大家。如果你手上正好有海螺AI会员，或者买了一批谷歌邮箱（一个才一两块钱）用来注册海螺AI，那这套流程就能让你实现“无限生成”——国内版一天免费，国际版三天免费，账号够多就等于无限。

![](img/82e0ff9b4bc9480713a6d72f47e57693.png)

先解释下为什么用Automa而不是影刀。大家应该都很熟影刀，但Automa可能有点陌生。其实我开始也是在研究比特浏览器（一款能多开的指纹浏览器）的时候，发现它居然支持RPA，才去深入的。Automa和影刀最大的不同在于，它就是个浏览器插件，任何浏览器都能挂上去。配合指纹浏览器，你甚至能开10个窗口同时跑自动化，影刀可做不到。比特浏览器里面直接集成了Automa这个开源扩展，多窗口控制很顺手。开源的好处是工作流随便复制，缺点是上手门槛比影刀高那么一丢丢。

Automa官网：https://www.automa.site/
中文文档：https://automa.wiki （光啃文档有点难，建议再搜点视频教程）

这套工作流的逻辑非常直接：固定一个提示词，循环读取某个文件夹里的图片，一张张传到海螺AI，自动点生成。如果配合比特浏览器多开，每个窗口各跑各的，效率直接×10。

## 效果演示

![](img/6cd944da6018e7d1ca79eefc01846534.png)

Automa里看到的工作流长这样：

![](img/295c1a6585a0a7cdcd1cc6276b67fc71.png)

按一下 ▶ 按钮就开始跑，运行的时候扩展图标上会出现一个 1️⃣ 的小角标。

![](img/f43c549a86e006ab8694cbd2e51736ab.png)

要是没看到 1️⃣ ，大概率是出错了，去日志里看看（方法见Tips）。

![](img/625213dc431dca9bf523d319061986eb.png)

下面是实际跑起来的效果。

## 原理拆解

这部分聊聊工作流是怎么实现的，要是只想用，可以跳过。

自动化的难点在于上传图片，点击之类的好解决。为此我写了个小工具，用Cursor做了个图片路径转换器。把图片文件夹或单张图片丢进去，它就能生成一个路径列表，长这样：

![](img/afa4f74ef533febf5e6a07c93d1b68c0.png)

输出的是json格式，大概是这样：

![](img/c7dc33eb1a5d38b12693c9cb13d1a6e5.png)

工作流本身的运行机制是这样的：一开始是触发器，然后要找到目标页面，这里用切换标签页去匹配网址。之后是循环数据，把上一轮生成的多条路径按顺序读取，跑完一条又绕回来。

![](img/dcb7f6e5301a73bdd0f1300e6e4dd53c.png)

![](img/9526e1207800b58f873e6a6631a29ec0.png)

循环什么时候停？靠的是循环断点。

![](img/dcd688feec679d65e183104bcaa739c6.png)

中间这段会去检测页面UI，看看是不是已经有3个或5个视频在排队。如果满了，就等3分钟再查。

![](img/4491e2d4e4452cb5e6acee09a7c1db7f.png)

接着是填提示词、上传图片。

![](img/e41ba59156a7bf99098d3553e58e5a09.png)

上传后等5秒，检查有没有传上去，失败就重新点一次上传。

![](img/af67cde69a780740137c6feee5bb9780.png)

最后点上传按钮，再根据反馈判断是否上传成功、生成是否真的启动了。

![](img/45d8daf9840d73606f3a59ef74e4f8de.png)

### 简单认识一下关键元素

以提示词输入为例。表单元素可以直接写入内容，CSS选择器右侧有个定位📍图标，点它能直接选中页面上的某个元素，✔图标则是用来验证你的选择器有没有写对。

![](img/931eedefd49568c382394288a9d04c16.png)

选择元素时，工具会自动框选，也支持手动填CSS选择器或XPath。

![](img/602e342e4e7cc4d256cde906252cb15e.png)

![](img/99beb79a680e9fd630a22e36f8aad7f1.png)

然后你就能在文本域里填入想自动输入的提示词了。

![](img/f66fbf738bc543b0ab87e78213770404.png)

## 详细操作指南

#### 1. 生成图片列表

附件里有工具。解压后先打开“图片处理工具V1.0.exe”。

![](img/23786e77bf5f7c7fbfaa397d9f149a0d.png)

点“选择图片文件夹”，或者直接把文件夹拖进窗口。

![](img/99602092cacd30e3b0f5686604eab45f.png)

顺手说一下，我还做了个网页版，在线直接用：
https://imgtool.tudoujunha.parts/

![](img/003f65c1dc859a8d419c7dfca1e4b2e9.png)

注意：图片路径别放得太深，最好放在桌面或磁盘根目录，不然容易上传失败。然后点“生成图片列表”，当前目录下会生成一个叫`image_list_时间.json`的文件，此时工具就可以关掉了。

![](img/1d98db66d72e84a6f56e632517479c1f.png)

#### 2. 安装Automa

Chrome或Edge用户点这个链接安装：
https://chromewebstore.google.com/detail/automa/infppggnoaenmfagbfknfkancpbljcca

![](img/5206c269f78f90eeadedc0d9149bfbc1.png)

如果访问不了Chrome商店，那就直接用比特浏览器，扩展中心里能一键添加。

![](img/6e7428a68b94fbbd83e2e7426b4edcd1.png)

想用中文的话，在扩展设置里改语言就行。

![](img/b57a92a6f4f9dd2dcd5f6a3b31844841.png)

#### 3. 开启文件访问权限

Chrome/Edge用户别忘了打开Automa的“允许访问文件URLs”开关（比特浏览器默认开启）。复制下面这串链接到地址栏，直接进入配置页：

```
chrome://extensions/?id=infppggnoaenmfagbfknfkancpbljcca
```

或者在扩展管理里找到Automa，像这样操作：

![](img/b10668ed74adce1c4602363da689ea0e.png)

![](img/992904fed41230faa6493105f356dbc0.png)

把“允许访问文件URLs”打开。

![](img/016575f7dde62c095e473d7af6309fb3.png)

不开的话，运行时会提示“Automa 无权访问文件”。

![](img/bc274891ba60c28e473af63e7880edf1.png)

#### 4. 把界面改成中文

进设置，改语言为中文。

![](img/0189e34891975dce56dc81f814c62411.png)

#### 5. 导入工作流

打开Automa后，导入`hailuo_auto.automa.json`。

![](img/2018711110e5cf09aed967d50f387a6c.png)

默认工作流对应海螺国际版，国内版请参考后面Tips的切换方法。

#### 6. 设置提示词

双击“Forms”卡片，在里面填写你想要的固定提示词。

![](img/36aff9b08af7fa6e2844f7b22f508826.png)

最新工作流的默认值是`{{variables.prompt_text}}`。如果你只需要一个固定提示词，直接删掉这个变量，填你自己的文字就行。（这个变量是为多提示词准备的，详见Tips）

![](img/440da230054e6be6f06b67268ef6a6e2.png)

完全不需要提示词的话，删掉文字或者关掉这个开关，运行时会自动跳过。

![](img/f5fdbac21056ac0ae7c6835ac8b43337.png)

#### 7. 导入图片列表

导入工作流后，点进工作流卡片，找到“Loop data”图片列表。双击卡片或点右上角的✏图标：

![](img/3245d0cf39f5a59962effe78808c52db.png)

左侧会弹出Loop Data详情，点“Insert data”：

![](img/d049232fe59fb2732d352355a470c9e5.png)

然后点“Import file”，选上刚才生成的`image_list.json`：

![](img/ebf04ac52ad9c36207ccfca770f94e23.png)

导入之后就是这样，点右上角的❎关掉。

![](img/7f46a9303522c7cad4867a78b2165183.png)

最后别忘点一下“Save”，不然不生效。

![](img/420f29c2a3246f676b24853bbbda1bc8.png)

接下来打开 https://hailuoai.com/video ，点▶就能试了。

注意事项：
1. RPA运行期间，请不要操作那个浏览器。可以缩小窗口，但别打开新页面，也别激活其他标签页，否则会报错。当然，你可以用Chrome开一个独立用户，或者用指纹浏览器开10个窗口，这样就没影响了。
2. 以上演示基于国内版，国际版步骤基本一样，但需要改一处设置，见Tips。

### Tips

#### 让RPA多窗口同时跑

在比特浏览器里进入“流程设计”，可以配置RPA任务。它会自动打开浏览器和Automa扩展，你可以在这里设计工作流。

![](img/06f1f5cb00bf3c8aa2ea5364bf5724c4.png)

先把Automa工作流的ID复制下来：

![](img/e9512086a6a5536aa7af4190831218ee.png)

然后在RPA自动化页面，新建任务，粘贴这个ID，就能实现多窗口自动运行了。

![](img/aff84df33854499a6160f64f90dc772f.png)

![](img/9aed6491017d3f66d2f6fc309a1e76f1.png)

如果自动运行的方式不利于修改配置，也可以多开几个窗口，分别在各窗口的Automa扩展里配置工作流，想哪些窗口跑就用哪些窗口。

![](img/af57628f4b51701dc76912377ffd0f47.png)

#### 调整检测间隔

默认是3分钟检测一次“生成”按钮是否可点（延时卡片以毫秒为单位）。一旦可点，就自动上传图片并点击。

![](img/1f70c6ef672a8bbf5f469c9a06739d57.png)

#### 查看日志

点“日志”图标，能看到当前工作流的日志。点`hailuo_auto`会显示详细运行日志或错误。日志右侧会显示运行状态，运行中想停也可以直接停。

![](img/0d365059074ba11d215b16cd960dcad6.png)

点“Stop”就能停止工作流。

![](img/5e0830dd4f1d02d962b751c89ea48fc6.png)

点标题能看详细内容。

![](img/a80b1044a1b5d57b76dcfc7ce02574e5.png)

#### 切换国内/国际版

国内版地址：https://hailuoai.com/video/create
国际版地址：https://hailuoai.video/create

切换时只需要把标签页链接改掉。下面演示的是从国内版切到国际版，注意新版链接要带/create：

![](img/8f932cf2133dc2549fd38ea48081d8fe.png)

把 https://hailuoai.com/video/create 改成 https://hailuoai.video/create

![](img/9985bca6fe35d8e8b11fc7135cb09e19.png)

改完后，记得等网页标签切到“Image to Video”再运行。

![](img/133e73bd4a4182cc15776ef088da512b.png)

#### 用F12看进度

在海螺AI的运行页面上按F12打开开发者工具，切到“控制台”，就能看到输出的日志。那些报错可以无视，只看最下面类似这样的行：

`loop-index: 0 image_xxx_0.png`

`loop-index: 0`表示当前是第几张图（从0开始），后面是图片名。

![](img/67079ea31a71f38a57016fb90f791c0a.png)

#### 图片传不上去

如果生成的视频尺寸跟上传的图片对不上，那说明走了文生视频。

![](img/5f98fd7e2203959a6c019240674fd059.png)

这大概率是图片上传失败了。要是真碰到了（概率不高），可以试试把工作流里两处5秒延迟改成10秒。

![](img/1387f3e33d862ac4a9ca4ccc62ff0cef.png)

#### 想用多个提示词？

目前工作流默认是一个提示词跑到底。不过新版支持多个提示词，比如前99张图用第一个，第100到299张用第二个，以此类推。

先定位到“JavaScript”卡片，双击打开：

![](img/6e4a1e707ce91683b59f9368d02d3817.png)

点一下里面那个代码块：

![](img/1b8507c9a3ac897e16e7daa970e49661.png)

然后把你准备的提示词依次填进去，注意别把双引号删了。

```
automaSetVariable("prompt_text", 
  loopData.$index < 100 ? "第一个提示词" : 
  loopData.$index < 300 ? "第二个提示词" :
  loopData.$index < 450 ? "第三个提示词" :
  loopData.$index < 500 ? "第四个提示词" :
  "超过500的提示词"  // 当索引大于等于500时使用的默认值
)
```

这段代码的意思是：第0-99张图用第一个提示词，第100-299张用第二个，第300-499用第三个，大于等于500用第五个。

![](img/c39a4d7d8b02c8987357b0e438e41737.png)

最后在提示词表单里填这个变量：`{{variables.prompt_text}}`

![](img/23e571c0a56eadc21f033f4482195f0d.png)

## 附件

#### 工作流文件

下载：https://gitee.com/tudoujunha/rpa-gpt/releases/download/v1.0/hailuo_auto.automa_v1.0.json

#### 图片处理工具（网页版）

网页版更方便，直接访问：
imgtool.tudoujunha.parts

![](img/33ed5fe7b8ee5afa1681bda4812330b9.png)

#### 图片处理工具（Windows版）

下载地址，目前只打包了exe。需要Mac版可以留言，我抽空更新。

![](img/27733476d828004b480a9f8fb554bc60.png)

Win版图片处理工具下载链接

#### 图片处理工具（Mac版）

Mac上不方便直接打包，所以先放出源码。不过Mac版现在已经打包好了，可以直接下：

Mac版图片处理工具下载链接

#### 源码

Python源码：

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