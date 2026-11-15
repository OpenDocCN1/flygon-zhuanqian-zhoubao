# 3分钟，用mac搭建了每日自动打开网页领取积分的RPA
我是龙哥，一个典型的“没工具就难受”患者。这次分享的是怎么用 Mac 原生能力搭建一个小自动化，让我每天自动去指定网站签到领积分。
先看效果：每天早上 10 点，即使电脑在熄屏状态，Mac 也会悄悄打开网站完成领取。要是当时没连网，等下次解锁时页面正好停在通义听悟，手动刷新一下就成功了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a59586c9905ef159059504f020f9805c.png>
下面说具体折腾过程。
## 为什么会想做这个
最近我重度依赖通义听悟，免费时长消耗得飞快。每天手动登录领积分？太麻烦了。我想着：我的 Mac 已经长大了，该自己打工了。于是，我决定让 AI 帮我写个自动化流程，用苹果自带的 RPA 小工具来实现。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_10ecf6b6704cc79dbfdd68d32e36cec3.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ccc34d660971a0bb04cf8264de2f74f7.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1049d278dd93d1c8431a3fbebd97c8df.png>
## 直接问 AI，别想太复杂
我没有写任何角色设定，直接把需求抛给了 AI：用 Mac，每天上午 10 点自动打开指定网页，告诉我怎么实现。有时候只要需求够具体，直接问就行。
```
我用的是mac电脑，我想实现，每天10点的时候 打开某一个网站，可以有什么实现方式吗？
```
结果它给了我三种方案。我选了第一种，理由是 Automator 之前听过，第二种要碰代码，第三种还得额外装软件，太麻烦。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1e9d583719951ba3cf4f9eb8d6d62cb4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4963403bad2e97c01a5cea43bf4f5eb9.png>
## 跟着指导一步步做
选定方案后，我让它把操作步骤细化。由于我是英文系统，我请它用英文再讲一遍，方便我对照着找按钮。
### 第一步：打开 Automator，新建一个“程序”
按 `Command + 空格` 打开搜索，输入 `Automator`。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_eb9b4ab352fa28580b086e68978c0568.png>
启动后，选择第二个选项“应用程序”，然后点“选择”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7619b56e5034ccf002abdbec3acc73bd.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_81b4bcc0789bcb32cf5dd004bb7d59fc.png>
进来后就是这样的工作区。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_49bc81713f5ecc1d74233480f8f93f0a.png>
### 第二步：添加“运行 AppleScript”动作
在左侧搜索栏输入 `AppleScript`，把右边的“运行 AppleScript”拖到右侧空白区域。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_73be1d9743029b155768e6a9a85f34af.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5b4c678619ca0c959c973d5e664b0376.png>
拖过去之后长这样。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c7435bde62ffa85b3ab40a5813246be4.png>
把默认代码换成适合 Chrome 的版本（截图如下）：
```
tell application "Google Chrome"
activate
open location "https://tingwu.aliyun.com/home"
end tell
```
Safari 对应的是另外一段，其他浏览器也可以照着改。网址部分随你填，想打开哪个网站就填哪个。
```
tell application "Safari"
activate
open location "https://tingwu.aliyun.com/home"
end tell
```
### 第三步：测试一下
点右上角的“运行”，我这边直接就弹出 Chrome 打开了通义听悟。第一次记得先手动登录，后面就不用再登录了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9b94d3d1fb66528dc0f7083cb4d86790.png>
### 第四步：保存成程序
点屏幕顶部的“文件”->“保存”，改好名字和位置，再点“保存”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_93fc02c8e235840e38cc8af22175d442.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c3d25db4dfc5e1c399541c817685d039.png>
保存完，桌面上就出现这个 App 了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7b76744f1298b2837490ae12dfa7c4e5.png>
### 第五步：设置日历提醒，让它每天定时打开
打开“日历”应用，在某个日期上右键，选择“新建事件”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0115fbd336421d15a1c76aa8898954b5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_00ae601f3582a20a8591a39b068b779f.png>
在左侧给它起个名字。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0e2078e27262e21c9d615b6ce4431a5a.png>
再点右边那个“添加提醒，重复...”的选项。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_615bba0227aeb9f57b1ff553ba81f939.png>
接着按下面的方式设置：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ec8ab901ea8360ddd126fe60990e1c0c.png>
- 开始时间：10:00
- 结束时间：10:00
- 重复：每天
- 提醒：选择“自定义”——“打开文件”——“其他”——选中刚才保存的 App
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2454741f5acb8da09a042de459582492.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4c12bd40f2044e3ecd8b26b51db49a28.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3744560753e0dcd49242c6d2684abafa.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_383b8da166b59e3aad697d93496220fb.png>
最后把提醒时间调整为“事件发生时间”，点“确定”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7144c54d4e76eacee2bf598d6d9497b7.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ae6735259ebc0cbde34e3aaea7daf19e.png>
这时候再看日历，那一排排的重复事件，是不是挺壮观？
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f42dc255b30102621d23c4b8154c8fa1.png>
到这里，整个自动化流程就完工了。Mac 真的可以很强！
## 最后一点碎碎念
我常觉得，了解一个工具的价值，是让你知道自己的能力边界。我的代码水平很菜，但我清楚“能实现”和“怎么实现”是两回事——前者靠自己认知，后者交给 AI 或者更专业的工具就行。
每一个接触过 AI 的人，都可以试着去想象边界在哪里。说不定哪天做出来的东西，会把自己都吓一跳。
看不懂英文系统？我也用了五年英文界面，习惯了就好，别吐槽我啦。
如果觉得这篇内容有用，欢迎去原帖点个赞。爱你们！