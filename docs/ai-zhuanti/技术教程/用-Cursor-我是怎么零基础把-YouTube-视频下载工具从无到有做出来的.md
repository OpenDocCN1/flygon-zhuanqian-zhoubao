# 用 Cursor 我是怎么零基础把 YouTube 视频下载工具从无到有做出来的
大家好，我是龙哥 Frank，在赚钱混了快两年了。工作一直很忙，参与感不高。最近抽了几天时间上手 Cursor，意外做出了两个小东西：一个是贪吃蛇，一个是 YouTube 在线视频下载器。写下这篇是想把从零到一的完整路径复盘出来，给同样想学 Cursor 的赚钱伙伴一点实操信心。我能搞定，你也能。
先看看成品效果。
# 一、起因
最近 Cursor 特别火。星球里、志愿者群里经常有人在聊。2024 年 11 月 14 日，志愿者群里一篇《如何让吴佳文学会用 cursor 完成一个复杂项目》的帖子点醒了我。我跟着流程体验了一把，当天就用 Cursor 搭出了贪吃蛇游戏，编译打包后部署到 Github Pages，还绑了自定义域名，全程不到 4 小时，体验感拉满。
![](img/zhuanqian_2c2ca30acc04b2d439334d8947cf9191.png)
(贪吃蛇是直接用 Cursor 实现的，编译打包后上线到 Github Pages，cname 到自己的域名，可直接访问)
周末玩了两天后，11 月 18 日周一，我又用 Cursor 在两三个小时内撸出了第一个 YouTube 网页下载工具，中间踩了一些坑但最终跑通了。下面是当时的界面截图，功能很朴素：
这一版技术栈是 React + Node.js。
![](img/zhuanqian_213def8acfe4386cb0df7edf6e480cab.png)
![](img/zhuanqian_12ec52ec5ac88e1de65ffa2ba7967b0a.png)
![](img/zhuanqian_8d537b39af11afb36eee09f6a22d31d8.png)
![](img/zhuanqian_a9b70fecfbfb1f986c5ad570fb3db2fd.png)
第一次做就成功了，在罗卜等圈友的鼓励下，我决定重做一版并做记录。第二次选用了 Bootstrap + js + python + flask，界面大概长这样：
![](img/zhuanqian_5a5a4c885c2641e86e65d3144ad63e3f.png)
![](img/zhuanqian_de8540f6d5adefc6a346d3acc7eba8e7.png)
# 二、为什么要做这个工具
最近我太太暂时失业，在家里研究视频搬运，需要我帮忙下 YouTube 原片，她自己再剪辑发布。我工作忙基本没空搭理，之前的做法是她把链接发我，我去 Google 找靠谱的下载站，运气好几分钟搞定，运气差要反复试好几个站点，算上找工具和传文件常常要半小时以上。
想到刚体验完 Cursor，就琢磨能不能直接做一个自己的下载器，把视频直接下下来。12 月正好有航海活动，主题里就有 Cursor 项目，提前练手也算为航海做准备。想让更多零基础的圈友看到，借助 AI 工具也能做出能用的应用。
# 三、找对标
前期调研很关键，直接影响需求的清晰度。
我的做法很简单：Google 搜“在线 youtube 视频下载工具”，点进一个能正常解析下载的站点，看看它怎么做的。参考站点的交互是输入 YouTube 链接 -> 解析 -> 显示信息 -> 点击下载。只模仿核心下载流程，其他功能不做。为避免广告嫌疑，这里不贴网址，按关键词自己搜即可。
![](img/zhuanqian_e0f273148fd2761b410615745eaf45d3.png)
下面是我用 Cursor 从零实现的全过程，也希望你能跟着试一次，做出东西后那种掌控感真的很上头。
# 四、实现路径拆解
## 第 0 步：明确人机分工
我画了个简易流程图：
![](img/zhuanqian_bcdd2403717d720aad164d0ae66b0941.png)
梳理下来分工如下：
我，扮演产品经理：
* 有一个点子
* 用文字把需求说清楚
* 在 Cursor 给出的技术方案里做选择
* 搭建完环境、功能落地后负责验收测试
Cursor，扮演开发：
* 理解需求并输出需求设计文档
* 推荐可行的技术栈
* 给出开发环境搭建步骤和代码
* 按设计文档分模块实现功能
* 修复我反馈的问题
使用者只需要把想法说清楚，后续是需求验收和迭代。没有手写代码环节，工作方式和真实的产研协作几乎一致。
## 第一步：把需求写清楚
这是最关键的一步。AI 再强，也需要清晰的目标。
我的核心想法是做一个在线 YouTube 下载站点，于是把需求整理成文字：
1、核心功能：打开网站后输入 youtube.com 的视频 URL，点击【解析视频】后展示封面大图、标题、描述、上传日期、文件大小等信息。字段名和值分开展示，最好用表格形式。【解析视频】成功后出现【下载视频】按钮，点击后开始下载到本地，下载时有进度条，完成后有成功提示，并记录下载历史。
2、页面 title 命名为：红哥YouTube视频下载
3、页脚显示：© 2024 红哥的YouTube视频下载器，仅供学习使用，联系人：红哥，邮箱：hong420802#gmail.com
4、页面需响应式，自适应各种屏幕
5、我在 Mac 桌面建了 youtube-download 文件夹，所有文件和代码都放这里。我是零基础，希望先基于此生成技术架构建议和《需求设计文档.md》放到该文件夹
写需求耗时约 5～10 分钟，前提是自己先想清楚要什么。
## 第二步：让 Cursor 生成需求设计文档
打开 Cursor，点击右上角【Togger AI Pane】，新建会话，把上面需求粘进去。
![](img/zhuanqian_0194f5fbe0fbcf3dc7fb35a8c8eafb4a.png)
![](img/zhuanqian_da42d668f445bf36ab13dcab94741609.png)
回车后会得到一份需求说明，用 txt / md / word 保存即可，便于后续对照。
![](img/zhuanqian_d6ff549629382021a6dd11c790b9b36c.png)
AI 给出的 YouTube 下载工具需求设计文档就是这个阶段的产出。
耗时约 5 分钟。
## 第三步：搭建开发环境
在聊天框输入：按这个方案落地，先手把手教我搭建开发环境，我零基础。
![](img/zhuanqian_f1eafa90f5f0be767b3181d949362223.png)
按步骤执行，遇到问题直接抛给 AI 解决，不需要额外搜百度或问朋友。
例如创建虚拟环境时遇到权限报错：
![](img/zhuanqian_0c830e1213faf76ea448ba1f64e96f08.png)
![](img/zhuanqian_fdbab2d401cbfe7fae8d7033c0840ea2.png)
![](img/zhuanqian_977e7bd029090b9a12c63325a1bbb65b.png)
![](img/zhuanqian_cf63da0984c9296c678b92549680ebeb.png)
类似问题直接问 Cursor，给出方案后尝试即可。解决后在框里输入“OK，解决了，继续下一步”，AI 会顺着上下文给出下一步指导，避免翻找历史记录。
![](img/zhuanqian_9514cf8198c6d08684ebbc2f71ca34f0.png)
### 1、安装 Python
![](img/zhuanqian_3d664c9948d3ef93dafdcbb4bef570eb.png)
操作截图：
![](img/zhuanqian_6a0d00bd1deef7515b6415129f427249.png)
看版本号就 OK，没装按提示装。
### 2、创建项目虚拟环境
![](img/zhuanqian_5861a3608af0f5c2e7758f89f034f71f.png)
操作截图：
![](img/zhuanqian_bd6fce8c5113ebc9b6ebfdebaa945812.png)
![](img/zhuanqian_ac91711f36456b2750b2ab5bb02f9d05.png)
![](img/zhuanqian_55784ca0699399a7c31e07fb2a81a90f.png)
### 3、安装依赖包
![](img/zhuanqian_6900b148d66cda9c93d26991897ca016.png)
![](img/zhuanqian_92b336f09401b7e409b7aaea7d4feb5c.png)
### 4、创建基本项目结构
![](img/zhuanqian_3cdcd741cd2fc798d0b9552dd64516f6.png)
![](img/zhuanqian_db19c4d3151681444e5b7fc7c48189bb.png)
### 5、验证安装
![](img/zhuanqian_da82554b34149438ee30e1a70f6910ee.png)
![](img/zhuanqian_fad83f56c471faaf3cd8527999f9a9f1.png)
![](img/zhuanqian_82f19486d4b80693ee9cdf670121a0aa.png)
![](img/zhuanqian_0601c879d0307586f134fc5fa2ae41e0.png)
![](img/zhuanqian_d44f0a3fbf3380eb2950903e1fecd4e7.png)
![](img/zhuanqian_8175f5ab391cbb9ccf5e9c025f0f9d26.png)
![](img/zhuanqian_7a274f34507724f8efb15065e5796eba.png)
![](img/zhuanqian_dca39828a16ce94b18d0c8cb449bee25.png)
到这里环境搭建完成，算是一半成功。
耗时约 15～30 分钟。
接着提示：环境搭建完成，浏览器访问 http://127.0.0.1:5000 输出正常，请指导下一步。
![](img/zhuanqian_fc74476aef6341eef441ad7a1707cdf1.png)
## 第四步：创建网站基础界面
### 4.1 准备工作
打开项目目录让 Cursor 感知上下文：
![](img/zhuanqian_f90a7a976f8074f4bf8cd2a7d2a356b1.png)
打开后历史聊天会消失，没关系，把需求再给一遍即可。
![](img/zhuanqian_4e8c521d3d51577f56ccdea0a193f33d.png)
![](img/zhuanqian_044c87ba9c9dad529ede2fb445fbec82.png)
找历史记录：文件 -> 新建窗口 -> AI 聊天 -> 历史记录
![](img/zhuanqian_c28a949317457580113a0931265da760.png)
用 Cursor 打开目录的目的是让 AI 的右侧 Apply 能生效，点 Apply -> Continue -> Accept，代码会自动写入项目，大幅提升效率。
### 4.2 生成基础界面
在 AI 聊天窗口点【Apply】等待几秒后再次点击：
![](img/zhuanqian_d77d8ed8263415dd050e482924a37411.png)
![](img/zhuanqian_937d911df146554fdab6df43ee111474.png)
Apply 后记得 Ctrl+S 保存。
![](img/zhuanqian_c9d4bf4d0fd22ac906d9afe32d8c25f0.png)
按 AI 提示依次 Apply -> Accept，把代码应用完并保存。
![](img/zhuanqian_84e02d8d1447a5b90972662711715bc4.png)
### 4.3 运行应用
![](img/zhuanqian_f876360a9dd3228e858f8b993afe3fba.png)
### 4.4 测试与排错
AI 提示在 http://127.0.0.1:5000 查看页面，包含响应式布局、输入框、信息展示区、下载按钮、进度条、页脚。
实际出现的是 Hello,YouTube Downloader！
![](img/zhuanqian_ee2279dce04a2fb2ec96a00d062900db.png)
不会排错就问 AI。
![](img/zhuanqian_ee7f008b1b5b81841132a9b5183b0b64.png)
![](img/zhuanqian_c4ab4f91edb7e500297e4a56f386b3c8.png)
排查后发现 5000 端口被占用，改成 5001，重启服务后页面正常。
![](img/zhuanqian_73cd15383cfa33003b86870ab964dabc.png)
![](img/zhuanqian_cd34ad5a062d25c568b697900e67ed28.png)
#### 4.5 结果说明
最终确认，这一步的目标功能已经落地，跑测结果正常。
#### 4.6 用时统计
把开发、验证和排错全算上，前后加起来大约 30 分钟。
## 第五步：把视频解析能力做出来
继续推进，我和助手说：目前首页和样式都正常，请我们进入下一个功能吧。
![](img/zhuanqian_577df0c9f10699e1fb8fefc166f5210d.png)
#### 5.1 实现与验证
先新建一个 JS 文件，用来处理前端交互。这个环节跟着助手的引导操作就行。
这里有一个小细节：应用代码时，有时会出现两个选项，一个是“应用到当前已有文件”，另一个是“新建一个文件”。如果工程目录里已经有目标文件，而且内容是空的，就选前者；如果文件还不存在，就选后者。
![](img/zhuanqian_0e61a8dc86aeaf811b57c0240d347424.png)
按助手提示操作完之后，它建议这样自测：
把 YouTube 链接粘贴到输入框，点击“解析视频”按钮，等待页面展示视频信息。
实际测试时，粘贴链接后点解析并没有反应，过了好一阵子才弹出一条报错。
![](img/zhuanqian_5fe3e1e088ce1e3278bc1dcf14bb792c.png)
我马上把报错发给助手。
![](img/zhuanqian_4b762282f71e45e370d09d6dbc1f1123.png)
按它的建议修改之后，依然有问题，于是继续追问。
![](img/zhuanqian_5ee8c20037e4b16e569bb7396be7ef19.png)
这次排查下来，还是没有输出。接着问助手，它给了检查方向：确认 /parse 路由是否存在。
![](img/zhuanqian_770d0759407c28670138d5630a7b8a34.png)
![](img/zhuanqian_b75cadf437a66ce0be1e93d0b75655c7.png)
检查方式是进入 python3，导入应用并打印路由表。结果终端里什么都没有输出。再用 pip list 过滤 flask-cors，发现这个扩展并没有装上，于是重新执行安装命令，装好后再把上面的验证流程走一遍。
![](img/zhuanqian_fad94973762abbd67d10a5203ea97206.png)
这次终于正常了，路由表里出现了 index 和 parse_video。
![](img/zhuanqian_fe405976451cd1c31ae8ba028716d513.png)
回到前端页面，输入链接并点击解析，又冒出一个新错误。
![](img/zhuanqian_90cfb309a29a1f3888f465dad3a11ced.png)
![](img/zhuanqian_4868d320375a8f7d6586212c152ffdd2.png)
再重新测一次，解析总算成功，距离目标又近了一步。
不过这时界面看起来不太美观。
![](img/zhuanqian_820ed1c7993a2ec9e57b154200288d90.png)
我向助手描述了样式问题，请它帮忙调整。
![](img/zhuanqian_23364c7c3501c089b6fa36f6f17fb77e.png)
![](img/zhuanqian_9ea9f7b8407d43883ccb681e591af0cc.png)
#### 5.2 用时统计
从开发到测试再到修问题，整体约 1 到 1.5 小时。
## 第六步：把下载能力做出来
继续向助手提问，让它推进下一个功能。它给出的代码，应用到工程后点接受，再重启服务，就可以开始测了。
#### 6.1 下载功能的实现
这个功能没有太多额外动作：按照助手的提示，应用代码并接受即可。
![](img/zhuanqian_ef2afb2b4061e260b78da8833d335cf3.png)
#### 6.2 下载功能验证
操作方式是：输入链接并解析视频，然后拉到页面底部，按下“下载视频”按钮，观察文件能否保存到本地电脑。
验证结果：
![](img/zhuanqian_0d3eabd7ddc17e600ed894cd9450c527.png)
第一次下载失败，我把情况告诉助手，它帮忙调整了代码：
- 加上 User-Agent 请求头
- 关闭证书校验
- 开启详细输出，方便排查
- 补上一些必要的下载选项
再次测试，结果依然失败。yt-dlp 报错说无法提取播放器响应，并建议升级到最新版本。
![](img/zhuanqian_5fe48b9170880d39139d58f7fec47729.png)
![](img/zhuanqian_f4735c4efcd05070e0bc246dc78889bc.png)
继续测，问题仍然存在。
![](img/zhuanqian_23ae7216652da92779b6940fb5bd6728.png)
于是再把问题抛给助手，这次它让我安装 ffmpeg。装完之后重新测试。
![](img/zhuanqian_5d1b12fc5216880d93b4b3d228340d2f.png)
这次终于成功了。
![](img/zhuanqian_13aa306c7469503bb9fcbe2e49a425c8.png)
这是服务端的日志，下载进度到 100%，Merger 也把文件合并到了本地。
![](img/zhuanqian_dd95f7df047b28400065667776255aad.png)
随后我换了一个 39 分钟的 YouTube 视频来验证，文件大小 346MB，下载花了大约 10 多分钟。
![](img/zhuanqian_a791891bc310e59068beafa2cb02fd58.png)
![](img/zhuanqian_7f45af685d9d689c2038d8d1b358df8a.png)
#### 6.3 验证结论
我的结论是：通过。基础下载链路没问题。
如果觉得速度不够快，可以继续请助手做优化；它会给建议，我们要做的就是把代码应用进去，然后反复测试。这个部分以体验流程为主，不必在某个优化点上死磕，以后熟悉了再回来弄也行。
![](img/zhuanqian_529aa7a087c56652ac09e81fe7145be6.png)
后续的优化过程我就不逐个展开讲了，套路都一样：把问题丢给助手，应用它给的代码，再遇到问题就继续问，直到解决。
我的优化效果：
![](img/zhuanqian_bd660fb72454a6cd2740afeede2273f8.png)
![](img/zhuanqian_80f35683f4946563990a44abbb57bd9a.png)
同样是 346MB 的视频，最终 4 分钟就下载完成，提升很明显。
#### 6.4 用时统计
实现、测试和修 Bug 加起来，大约 1 小时。
## 第七步：加上下载进度条
第六步做完以后，下载的核心能力已经具备了。
第七步是做一个进度条，让用户点击下载后能实时看到进度变化。这个功能属于体验优化，不做也不影响主流程；如果大家动手练习，可以跳过这一节。
#### 7.1 进度条的实现
我给助手的指令是：先做下载进度的实时显示。它给出了代码层面的修改建议。
![](img/zhuanqian_f6e4c174a29c463c104a38230e2d9136.png)
#### 7.2 功能验证
测试时用的视频链接是：https://www.youtube.com/watch?v=u8suB4La7oE ，大小只有 2.4MB，方便观察进度条效果。
实测没问题：进度条能正常展示，下载完成后，整个进度区域会自动隐藏。
![](img/zhuanqian_2d7e5b5c0bcb02a64f407309e43c3ab5.png)
![](img/zhuanqian_c9804bef16f6cce9ba3394129862ea9e.png)
有时候，助手在合并代码时会引入新问题，导致之前修好的内容又重新出现。解决办法还是继续问它，让它做修复。最好让它给出完整的修改方案，再把代码整体替换掉。
下面是我这次遇到的问题：
进度条看起来正常了，但解析结果里的“文件大小”字段又变成了“未知大小”。这个问题之前已经修过，现在再次出现，请帮忙处理。
![](img/zhuanqian_ecaffc42e659ea24433f8a68e2b088c6.png)
![](img/zhuanqian_9389ce49f6cf400e63ea7ea4dcefcbf9.png)
实现进度条之后，还发现了两个新问题：
1. 文件原本应该保存到 youtube-download/downloads 目录，现在却跑到了桌面。
2. 下载后的文件名之前没有处理过，我重新提需求，请助手帮忙改名。
下面是发给助手的问题：
![](img/zhuanqian_78f8334c0f11af966b70195ee510851c.png)
![](img/zhuanqian_1cbbed856b1174782253aa31114ce5d6.png)
应用修改之后，结果符合预期。
![](img/zhuanqian_d481885ec981207df0bb91fc1817a05c.png)
文件回到了 downloads 目录，文件名也改成了对应的视频标题，查找起来很方便。
![](img/zhuanqian_7c63142dde402d58839453748dc5615a.png)
#### 7.3 验证结论
功能已经实现，整个验证过程正常。
#### 7.4 用时统计
从实现到测试再到修问题，整体不到 30 分钟。
## 第八步：支持视频质量选择
#### 8.1 实现清晰度选择能力
我让助手继续对照需求文档，把还没做的功能列出来。它会生成一个待办清单，并建议优先做那些优先级高、改动简单的项。
我选择先做“视频质量选择”。
![](img/zhuanqian_f8a18e3479e2c50e190cf1d1296be2f5.png)
![](img/zhuanqian_6b22284563797e9d67f8abcd8b9b765e.png)
#### 8.2 选择功能验证
中间遇到一些小问题，都通过问助手解决了。最终效果如下：
![](img/zhuanqian_b9a810bbbadf8de01bee614af8e4d90c.png)
下载功能和进度条功能也都正常。
![](img/zhuanqian_ffa7dc0d1e086925355b9bb03f70bbba.png)
#### 8.3 验证结论
这个功能实现正常，本次验证以及之前的功能回归也都正常。
#### 8.4 用时统计
实现、测试和修 Bug 加起来，不到 1 小时。
## 第九步：查看下载历史记录
这个功能不是必须项。我主要是想演示一下：从冒出“下载历史记录”这个念头，到用 Cursor 把它做出来，整个过程是怎样的，希望能给大家一点启发。
实际做项目时，建议把精力放在更核心的地方。比如这个下载工具，重点就是解析视频和下载视频，其他功能都属于锦上添花。
“历史记录”这个想法，我没有专门去调研市面上的同类工具有没有，纯粹是自己临时起意。我想验证一下：一个不会写代码的人，通过 Cursor 到底能不能把这样的想法实现出来？如果真做成了，还挺有成就感的。
继续往下看吧。
#### 9.1 历史记录前端页面
![](img/zhuanqian_7eded1a773b4958c397452d0c1997931.png)
助手给出的方案很清晰，照做就行：在右侧窗口点击应用，接受修改，完成后直接开始验证。
第一步，安装必要的依赖：
```
pip install flask-sqlalchemy
```
第二步，修改 app.py，加入数据库支持：
```
# 在文件开头添加导入
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# 在创建 Flask app 后添加数据库配置
app = Flask(__name__)
CORS(app)
# 配置 SQLite 数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///downloads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# 定义下载历史模型
class DownloadHistory(db.Model):
id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(500))
url = db.Column(db.String(500))
format = db.Column(db.String(50))
quality = db.Column(db.String(50))
filesize = db.Column(db.String(50))
download_date = db.Column(db.DateTime, default=datetime.now)
status = db.Column(db.String(20))  # success, failed
error_message = db.Column(db.Text, nullable=True)
file_path = db.Column(db.String(500))
# 创建数据库表
with app.app_context():
db.create_all()
```
第三步，修改 templates/index.html，增加历史记录页面：
```
##### 下载历史
标题 |
质量 |
大小 |
下载时间 |
状态 |
操作 |
```
下面是我实际操作时的截图：
![](img/zhuanqian_ef0b92c1c3e6e26252e8761b6e4f8854.png)
前端页面展示效果如下，一切正常。
![](img/zhuanqian_ee0ee3452c66ac20cd9085a2e340cbc5.png)
#### 9.2 记录下载日志
这个功能的意思是：用户每完成一次下载，就往历史记录里插入一条数据，把这次下载留个底。
接着让助手提供对应的前端 JS 和后端接口代码。具体操作跟着它的引导一步步问就行，这里没办法把所有截图都贴出来，太费精力了。
![](img/zhuanqian_1785865a63e87c827f68f7ad57f20191.png)
我先加了“获取历史记录”的接口，结果下载视频又失败了。
![](img/zhuanqian_4b1338e8dc334c0f2e0e5999da7f6bd3.png)
老办法，把问题丢给助手，等它给出方案后，在右侧点应用，再点接受。前面已经反复提过，直接操作就好。最后啰嗦一句：接受修改后，记得按保存快捷键把文件存一下，这一步很容易漏。
![](img/zhuanqian_fbd1cb4257ae0f5bf9a8d5557a27e58d.png)
保存后重启服务，又遇到了新状况，继续问助手。
![](img/zhuanqian_c11629d7f17359fb352ab4ee5d95c309.png)
再次按它给的方案执行。
![](img/zhuanqian_522d560be9e1431872cae3b6af9cca58.png)
这次下载成功了，历史记录里也出现了数据。
![](img/zhuanqian_5012efa85cbde502e7ac47c4ebaae4b0.png)
再换一个视频链接试一次，历史记录同样能正常显示。
![](img/zhuanqian_0c115759b82d50edd122889c2bcfbc1d.png)
![](img/zhuanqian_7932042537c798acb7ac50630693e2e2.png)
#### 9.3 从历史记录重新下载
这个功能的入口在历史记录列表里：每一条记录的右侧都有一个“下载”按钮，点击后可以重新下载对应文件。
![](img/zhuanqian_f4025f51d7a6a6fb7434f8f6b1504c96.png)
# 不会写代码，靠AI做帮手，我7小时搞出一个能用的视频下载应用
以前我总觉得，做应用是程序员才能碰的事。但这次，我从零开始，把一台电脑用成了“带编程序”的助手：只要把需求讲清楚，AI负责写代码，我负责验收。整个过程下来，最深的感受是：不会编程，照样能做出来能跑的工具应用。
这篇就把我的完整操作过程、踩过的坑和一些实用心得写下来，给同样零基础的朋友参考。
## 我最初想要什么
起初的需求不复杂：粘贴一段YouTube链接，能自动识别出封面、标题、简介、文件大小、上传时间；点一下按钮，能把视频保存到本地；还要能查看历史获取过的内容，并支持从历史里再次获取。这些功能，最后都通过Cursor逐一实现了。
## 七个多小时花在了哪里
整个项目从开工到收尾，累计约七个小时。其中约一半时间花在边做边写文档、截图留档上，真正用于开发和调错的时间，大约两三个小时。各环节大致用时如下：
- 把想法整理清楚：三五分钟
- 请AI起草需求说明：三五分钟
- 搭好开发环境：十五到三十分钟
- 制作基础页面：半小时上下
- 实现视频信息解析：一个半小时左右
- 打通文件保存流程：约一小时
- 增加进度显示：不足一小时
- 加入清晰度选择：半小时以内
- 历史留档与再次获取：约一小时
- 细节打磨与外观调整：约一小时
只要把大任务拆成小步骤，每个节点都不会让人卡住。最常用的做法就是：把报错信息原样交给AI，等它给出修改方向，再动手验证。
## 一次典型的排错过程
开发过程中摔跤是常事。我记得有一次，从历史记录里再次获取视频时，页面弹出了 `Cannot read properties of undefined (reading 'target')`。那时候我完全看不懂是什么意思，就把这行提示原封不动发给了AI。![](img/zhuanqian_a493a537c6910f4f10f3005e9a0d8cea.png)
补丁应用之后呢，又遇到了新问题，如下：![](img/zhuanqian_f2943a32a4f4dd09225029899517ecda.png)
于是又把提示丢给AI，照着它给的方案来弄：![](img/zhuanqian_1e02667834796afdbd40af51fed78c38.png)
![](img/zhuanqian_09551819ccf77e049ae35fd3c90a04ce.png)
![](img/zhuanqian_28ccf8c9c4a4509ba371dafb7f9b8db8.png)
重新下载了一次，结果还是提示 Cannot read properties of undefined (reading 'target')，只能继续向AI求助。![](img/zhuanqian_470cd7c07c1e8c896b4e1b5f7f0ef248.png)
按AI的版本改完之后，我刷新前端页面，进入下载历史，再重新下载，实际走了一遍：![](img/zhuanqian_c492ba175ba6e75f2a103905b695e87b.png)
这次顺利通过。![](img/zhuanqian_fe0c059294d8bf1b816c1bde1ccee29e.png)
这里要说明一下：每次在终端执行过其他命令之后，都需要先激活虚拟环境，具体命令如下。```
在终端命令行执行：
cd /Users/Frank02/youtube-download   //进入到项目的目录
source venv/bin/activate   // 激活虚拟环境
python app.py     // 启动Flask服务器
```
![](img/zhuanqian_532ddf1d67ff11be405fc0adf5657c4b.png)
因为我是边写功能边顺手验证的，所以详细的测试过程就不在这里展开了。
验证结果：下载历史记录可以正常查看，重新下载也能正常工作，这一块从开发、测试到修复Bug，整体加起来不到1个小时。
## 最后的细节优化
主功能完成以后，我又提出了一些小调整，都是逐条和AI对话完成的：
1. “下载视频”“下载历史”这两个标签，希望距离顶部10px，怎么写代码？
2. 这两个标签需要加粗显示，怎么操作？
3. 解析出的视频信息里，想再增加几个字段：上传人、视频时长、观看数、点赞数。
4. 视频质量的默认值，希望改成 720p (HD) (mp4)。
这些需求一律交给AI处理，每次对话的过程都截图留存了。
顺便提醒一句：每次做新优化或改动功能点，都有可能出现新的意外，甚至把已经好用的部分弄坏。这是很正常的事。此时最好的态度是保持耐心，多向AI请教，请它继续排查解决，而不是抱怨它水平不行，又搞出了之前解决过的问题。![](img/zhuanqian_01d885e1002199c09a753d4ffd8a1293.png)
![](img/zhuanqian_d5cfa0d06975eadab35f423293f94cc1.png)
![](img/zhuanqian_b211f54b4a502b5e0e5b933561fd64c4.png)
![](img/zhuanqian_1df925475f9690a9bb52a504e9b5dcbf.png)
最终优化完成后的效果如下：![](img/zhuanqian_3a6c9d4d1f42a215cdc84806720a277f.png)
## 给新手的几点叮嘱
1. 每次开始开发前，记得先激活虚拟环境：```
cd /Users/Frank02/youtube-download   //进入到项目的目录
source venv/bin/activate   // 激活虚拟环境
python app.py     // 启动Flask服务器
```
2. 只要改过 app.py 文件，在功能验证之前，都需要重新启动 Flask 服务器。
3. 开发结束后，可以输入 deactivate 退出虚拟环境。
4. 遇到权限类的报错，可以考虑在命令前加 sudo，例如 sudo brew install python3。
5. 碰到稀奇古怪的问题也不必慌。把具体的现象和报错信息，通过AI对话窗口发给Cursor，让它给出解决方案，多试几次总能解决。
6. 在AI对话窗口中点了 Apply 并 Accept 之后，一定要记得把代码保存下来。否则测试时代码没有真正生效，Bug会一直亮在那里。
7. 接收代码补丁时，要留意修改的文件名和所在路径是否正确，别把 app.py 的代码误用或复制到 index.html 里去，导致无谓的报错。
8. 每完成一个新能力，建议把项目代码文件夹整体手工备份到别的地方。因为AI改代码时可能一通操作，导致旧功能全废、新功能也没加上；如果有上一个可用版本的备份，就可以直接从那儿接着改，效率会高不少。如果熟悉git，用版本管理工具会更方便。![](img/zhuanqian_f2abe3c5c11daab62667ae72eca44968.png)
9. 和AI对话偶尔会失败，多半是网络连接问题。因此最好准备一个稳定的外部网络工具，否则会影响整体开发效率。
## 最后的话
回头看，我最开始的需求描述——输入YouTube视频链接，解析出封面图、标题、描述、文件大小、上传日期，然后点击下载视频，并保留下载历史、支持重新下载——这些全部通过Cursor实现了落地。
我自己没有编程背景，也没有写过代码，整个过程都靠AI协助，最后出来的功能是真实可用的。这说明，零基础并不妨碍做出工具类的小应用。
全程耗时大概七个小时，每大步的用时明细见上面的清单。如果撇开写文档的时间，单纯做这个工具只需要两三个小时。整个流程可以概括为：有了想法→写下来→AI辅助完善需求→AI搭建开发环境→AI实现功能→测试→完成。
没有编程经验的人，一样能借助Cursor做出应用软件。我已经从头到尾走通了一遍，相信你也可以。
最后，祝各位圈友一起赚钱、一起进步。马上有个Cursor的实操活动要开始了，感兴趣的朋友抓紧报名，一起学习中。