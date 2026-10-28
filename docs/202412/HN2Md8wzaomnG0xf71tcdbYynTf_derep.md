# 闲鱼网页新消息提醒插件实战制作记录

> 来源：[https://w63nbfedzw.feishu.cn/docx/HN2Md8wzaomnG0xf71tcdbYynTf](https://w63nbfedzw.feishu.cn/docx/HN2Md8wzaomnG0xf71tcdbYynTf)

# 开头

## 起因

在闲鱼做二手买卖，最怕的就是错过买家的私信。之前我分享过闲鱼网页版也能回复消息，有朋友吐槽说没有提示音很抓狂。我当时以为是浏览器通知没开，让对方确认后也以为是偶发bug就没深究。后来有段时间无论手机还是电脑都收不到提醒，几十分钟才发现客户已经连发几条消息，这才决定自己动手做一个提醒方案。先试了油猴脚本，没达到预期，可能手法不对就放弃了。

直到2024年11月26日那天咨询量暴增，一位客户在网页上密集发言，我盯着电脑干等，索性下定决心用 Chrome 插件的方式实现有声提醒。看不懂开发细节的读者可以直接跳到文末附录下载成品并参考第六章安装方法。

## 为何选用 Chrome 插件

Chrome 插件能更底层地干预网页交互，提示音文件可以直接打包进插件包里，比外链更稳定。之前油猴子的方案体验一般，所以这次换个思路，从零做一个自带的 Chrome 提醒插件。

# 前期准备

## 实现思路

1、闲鱼网页版出现新私信时，标签页标题会变成以“[新消息]”开头，于是判断新消息就看标题里有没有“[新消息]”。

2、插件只在闲鱼相关域名生效，网页版域名是“https://www.goofish.com/”，消息页是“https://www.goofish.com/im”开头，匹配到这些地址才启动。

3、本地播放音频需要提供 mp3 提示音素材。

4、插件需要图标，我让 CurSor 直接生成了矢量稿。

## 开发所需工具与资源

*   CurSor 编程环境
*   Chrome 浏览器用于开发调试
*   SVG 转 PNG 在线工具，CurSor 给的是：https://svgtopng.com/
*   配音制作工具，我用的是微配音

![](img/a29b420d52677f9141453d12d05e65f4.png)

# Chrome 插件基础框架

## 核心构成

一个典型的 Chrome 插件一般包含：

*   manifest.json：配置插件信息、权限、版本号等元数据。
*   background.js：后台脚本，负责监听事件和处理逻辑。
*   content.js：在页面上下文运行的脚本，用于读取或操作页面内容。
*   popup.html：如需用户交互，则提供弹窗界面，通常搭配 popup.js。
*   图标文件：常见尺寸 16x16、48x48、128x128 的 PNG，命名一般为 icon48.png、icon64.png、icon128.png。
*   其他资源：样式表、脚本等。

# 提示音 mp3 的制作

1、在微信 PC 端打开【微配音】小程序，输入提示文案，点击【更多】挑选配音主播，我选的是【智虹】：

你有新的闲鱼消息，请注意查看~

![](img/61ff2148b79c4d2d22828345ba3ab598.png)

文字选好后可用【短句试听】先确认语气是否合适。

2、纯语音略显单调，下方有【音效库】可搭配提示音效：

![](img/e143513568552cbacec229a8d5f16a24.png)

3、音效复制到主文案上方，点击【语音合成】开始合成：

‖●音效zhongling/11.mp3‖你有新的闲鱼消息，请注意查看~

![](img/16a156c5de24255f47781f7209254a65.png)

![](img/dbdbb5aa8b7ad033afb39c8da58087c1.png)

4、合成完成后可预览，不满意点左上角【<】返回调整：

![](img/95d2551862f51e141b9db01fdf21b912.png)

确认无误后点击【下载】保存配音。

5、进入下载页，点击【复制下载链接】用 Chrome 浏览器打开：

![](img/5f72f90bab64a4583190dbded0609571.png)

![](img/d9276c529b168bb8d0ddb4cdeb35614f.png)

随后点击【下载音频文件】完成获取。

# 插件编码

## 提示词撰写

思路是让 AI 充当 Chrome 插件工程师，把需求拆清楚：

假设 AI 是 Chrome 插件编程专家，帮我写一个 xxx 插件，要求如下：

1、仅在网址包含 xxx 时激活
2、具体行为，比如当 xxx 网页的标签标题包含 xxx 时执行 xxx

需求写得差不多即可，不必一开始就面面俱到。

我最终给出的闲鱼提醒插件需求是：

你是一个Chrome插件编程专家，请帮我编写一个闲鱼信息提醒插件，需求如下：

1、网址包含@https://www.goofish.com/ 、@https://www.goofish.com/im* 时启用插件

2、后台监测包含@https://www.goofish.com/im* 的网址标签页的标签页banner包含“[新消息]”的给我播放提醒mp3

## 用 CurSor 完成代码

建好项目文件夹并用 CurSor 打开后，直接在 Composer 模式里输入上述提示词，Composer 会自动创建文件结构：

![](img/3631b412be6bca127341a1cede95cdd3.png)

![](img/392a4acef0c10c45ad088b962f98617e.png)

2、为了文件管理更清晰，我让 CurSor 额外建一个存放 mp3 的目录，口吻很随意：

增加一个mp3文件存储文件夹

![](img/f7f3e5947ec9a1b485e5eeca87bd1dc5.png)

![](img/698d7bf5d52e9979d455061f6421766f.png)

Composer 大部分时候会自动建目录，但偶尔失灵，我就手动新建了【audio】文件夹。

3、文件结构里已有 icon48.png、icon128.png 和 notification.mp3，先让 CurSor 生成图标：

给我生成icon图标

![](img/f0279b34574d0e2a34f57e005ad1bc77.png)

![](img/92d7e631f79c407dd8cfbfeb87f32bdc.png)

CurSor 输出了 icon.svg，并给出 svg 转 png 的网站。

4、把转换好的文件下载回项目根目录，复制一份分别重命名为 icon48.png、icon128.png：

![](img/61741acec3b27543c26d50af6b1a9053.png)

![](img/f79053451b45c8fce626afd1408383ea.png)

命名完成后可在 Chrome 中加载测试，具体安装见 Chrome插件安装章节。

5、第一次加载报 Service worker registration failed. Status code: 15，迭代太多不好回滚，直接把报错丢给 CurSor 修：

![](img/cc1b28a150f18aa612e375a55f6a8bfa.png)

![](img/9864595add85a54b35cf795cb3412cdb.png)

![](img/5722ad54fe9d77da486db173202302ca.png)

6、修复后出现 Uncaught (in promise) ReferenceError: Audio is not defined，又让 CurSor 处理：

![](img/a2381c6ad5a8f168b1c00790f103ca37.png)

![](img/bc13997f69f7e4c2947bae820cad0ade.png)

这次被改成了 Chrome 原生通知音【铛铛铛】，辨识度低，无法判断是不是闲鱼消息。

7、希望图标能显示未读数，于是要求修改：

有新消息的时候插件图标增加数量

![](img/09c3df1bad3c3dc50bb7ae5c223c0af9.png)

![](img/f69dbb7093a98ca72f1ca6cbba6b6927.png)

改完后图标上确实出现数字，但始终是1，因为标签页标题并不会显示具体条数。

8、原生通知音不理想，改回本地音：

还是更改为使用本地声音提醒比较好

![](img/ef29236597d54f7cf8ab08709ec57157.png)

![](img/b493b22e2dc1fe7c596daba86dd52d2b.png)

```
主要更改说明：
移除了通知相关代码，改用音频提醒
添加了 content script 来处理音频播放
使用消息传递机制在 background 和 content script 之间通信
保留了图标上的未读消息计数功能
添加了必要的权限和资源配置
这样实现的好处：
可以正常播放本地音频文件
保留了未读消息计数功能
避免了系统通知可能被屏蔽的问题
提供了更好的用户体验
```

9、随后进入反复修 bug 阶段，把报错信息直接丢给 CurSor 修改：

发送消息失败: Error: Could not establish connection. Receiving end does not exist.：

console.error('发送消息失败:', error);

![](img/f8677a0bdc1318b5fcae8523ae27dc29.png)

![](img/310966976f9d5bd0f2c9dc36dd5a741f.png)

![](img/bd652daa00aa83b2351c39d9df0238a2.png)

```
主要修改说明：
在 background.js 中添加了脚本注入逻辑
添加了 scripting 权限以支持动态注入脚本
在 content.js 中添加了初始化确认机制
使用 setTimeout 确保有足够时间让 content script 加载
添加了错误处理和日志记录
这些修改应该能解决消息发送失败的问题。主要通过以下方式解决：
确保 content script 已经正确加载
动态注入脚本以确保代码执行顺序
添加延时以等待脚本加载完成
增加错误处理机制
如果还遇到问题，可以检查：
插件权限是否正确设置
音频文件是否存在且路径正确
Chrome 控制台是否有其他错误信息
```

没有看到调用本地notification.mp3文件播放

这个错误是因为代码里没引用 notification.mp3，所以让 CurSor 补上。

![](img/2cce66f95b729e663a8abec9ee6d4ab6.png)

![](img/e3ffbfdec2c4bc463c165d55aa801e04.png)

```
主要修改说明：
在 background.js 中直接创建和播放音频
如果直接播放失败，再尝试通过 content script 播放
在 manifest.json 中明确指定了音频文件路径
添加了 到 matches 以确保 background script 也能访问音频文件
请确保：
在插件目录下创建 audio 文件夹
将 notification.mp3 文件放在 audio 文件夹中
音频文件格式正确且可以播放
文件结构应该是：
插件根目录/
  ├── manifest.json
  ├── background.js
  ├── content.js
  ├── icon48.png
  ├── icon128.png
  └── audio/
      └── notification.mp3
这样应该能确保音频文件能够正确播放了。如果还有问题，可以检查 Chrome 开发者工具的控制台是否有错误信息。
background.js 
```

发送消息失败: Error: Could not establish connection. Receiving end does not exist.

Context

background.js

Stack Trace

background.js:9 (anonymous function)

// 存储未读消息数量

let unreadCount = 0;

// 播放提醒音频

async function playNotification(tabId) {

try {

// 创建本地音频对象

const audio = new Audio(chrome.runtime.getURL('audio/notification.mp3'));

// 直接播放音频

await audio.play();

} catch (error) {

console.error('播放音频失败:', error);

// 如果直接播放失败，尝试通过content script播放

try {

await chrome.tabs.sendMessage(tabId, { action: 'playNotification' });

} catch (error) {

console.error('通过content script播放失败:', error);

}

}

}

// 更新扩展图标上的未读数量

function updateBadge(count) {

if (count > 0) {

chrome.action.setBadgeText({ text: count.toString() });

chrome.action.setBadgeBackgroundColor({ color: '#FF0000' });

} else {

chrome.action.setBadgeText({ text: '' });

}

}

// 检查标签页标题的函数

function checkTitle(tabId, changeInfo, tab) {

// 只检查闲鱼相关的页面

if (tab.url && tab.url.includes('goofish.com/im')) {

// 检查标题是否包含[新消息]

if (tab.title && tab.title.includes('[新消息]')) {

// 更新未读消息数量

unreadCount++;

// 更新图标

updateBadge(unreadCount);

// 播放提醒音频

playNotification(tabId);

} else {

// 如果标题不包含[新消息]，说明消息已读

if (unreadCount > 0) {

unreadCount = 0;

updateBadge(unreadCount);

}

}

}

}

// 监听标签页更新事件

chrome.tabs.onUpdated.addListener(checkTitle);

// 监听标签页关闭事件

chrome.tabs.onRemoved.addListener((tabId) => {

// 重置未读消息计数

unreadCount = 0;

updateBadge(unreadCount);

});

播放音频失败: ReferenceError: Audio is not defined

通过content script播放失败: Error: Could not establish connection. Receiving end does not exist.

![](img/6067530bfc35e946e2b2b9bdbe35ac0b.png)

![](img/4521f425f43727d71a132d0169f57794.png)

```
主要修改：
移除了 content.js 和相关配置
使用 chrome.scripting.executeScript 直接在页面中执行音频播放代码
简化了错误处理逻辑
保留了必要的权限和资源配置
这样应该能解决音频播放的问题。关键改动是：
不再依赖 content script
直接在页面上下文中执行音频播放
使用 scripting API 注入代码
请确保：
audio 文件夹中有 notification.mp3 文件
音频文件格式正确
文件路径正确
```

再次迭代后仍提示播放音频失败: ReferenceError: Audio is not defined，继续交由 CurSor 调整：

播放音频失败: ReferenceError: Audio is not defined

![](img/6af8bc1a3efd27ab8e69ac140b2b3a5d.png)

![](img/cc4a316386f2dbd35e7e2ec02a5c1ebe.png)

```
主要修改说明：
创建了单独的音频播放脚本
使用 document.createElement('audio') 替代 new Audio()
通过 executeScript 注入整个文件而不是函数
文件结构：
插件根目录/
  ├── manifest.json
  ├── background.js
  ├── play-audio.js
  ├── icon48.png
  ├── icon128.png
  └── audio/
      └── notification.mp3
这样应该能解决 Audio 未定义的问题，因为我们现在是在页面上下文中创建音频元素。
```

这次新增了一个 `play-audio.js` 文件，但加载后立即出现了报错：

`Uncaught SyntaxError: Identifier 'audio' has already been declared`

Context：

https://www.goofish.com/im?spm=a21ybx.home.sidebar.1.

Stack Trace：

`play-audio.js:1 (anonymous function)`

![](img/3bd13f28b924705e7a7e2b1dc40b3bd7.png)

```
主要改动：
使用立即执行函数(IIFE)创建独立作用域
给音频元素添加唯一ID
检查是否已存在音频元素，避免重复创建
隐藏音频元素
将音频元素添加到文档中
这样可以：
避免变量命名冲突
重用已存在的音频元素
保持DOM结构整洁
确保音频元素正确加载和播放
```

随后又遇到了音频播放失败的问题：

`播放失败: [object DOMException]`

Context：

https://www.goofish.com/im?spm=a21ybx.home.sidebar.1.

Stack Trace：

`play-audio.js:16 (anonymous function)`

![](img/f7571e8a3db634eefa51a667db1bae7f.png)

![](img/7754afd51d91c0fb1a5f47abd2b1db06.png)

经过调整后，新消息已经可以触发MP3提醒音了。不过新的问题也随之出现：声音不会在播放一次后停止，而是不断重复，并且多次音频还会叠加播放。

原本应该只听到一次【Duang】，实际效果却变成了【Duang、Duang、Duang、Duang】，而且声音彼此重叠。

因此继续让CurSor修改逻辑：当检测到多条新消息时，提醒音应该按照设定的时间间隔依次播放，而不是在检测期间持续叠加播放。

![](img/4380fb395a614db61245643fcd4f87bf.png)

```
主要修改说明：
添加了 lastPlayTime 变量记录上次播放时间
添加了 PLAY_INTERVAL 常量定义播放间隔（3秒）
在播放前检查时间间隔
只有超过间隔时间才播放音频
这样可以避免频繁播放提示音，提供更好的用户体验。你可以根据需要调整 PLAY_INTERVAL 的值来改变播放间隔。
```

之后又发现，浏览器插件图标右上角的消息数量并没有变化，于是再次让CurSor协助处理：

插件图标上的消息数量没有增加。

![](img/6f342298832f2dd7b9b7dece02cfe579.png)

![](img/d89c9f3178e22854d2235dfd41f0cdd4.png)

修改后数量依旧没有显示。考虑到标签页本身也没有展示新消息总数，最后就没有继续在这个功能上反复调整。

### 效果视频

## 使用popup.html设置提醒间隔

之前视频里采用固定3秒间隔进行提醒，使用起来比较频繁，也不够灵活。因此增加一个 `popup.html` 配置页面，让用户可以自行设置声音提醒的间隔时长。

发给CurSor的修改要求是：

增加popup.html用户界面，通过用户界面设置播放间隔时间。

![](img/31db56e4a2880291c50274a0ae8c885a.png)

![](img/2301805ac808ea5f2978f50a351add59.png)

![](img/7142d2859f2dae2f8e022c255d99a3e9.png)

![](img/3a40bf1899cd667879bf67559421f99e.png)

```
主要更改说明：
添加了设置界面，可以调整播放间隔时间
使用 chrome.storage.sync 保存设置，支持跨设备同步
添加了实时设置更新功能
增加了输入验证和保存成功提示
界面设计简洁直观
使用方法：
点击插件图标打开设置界面
输入想要的播放间隔时间（1-3600秒）
点击保存按钮应用设置
设置会立即生效并保存
```

修改完成后，需要重新加载插件：

![](img/8fa8708e600de4beece57ca51114779a.png)

![](img/65b82ad17b88bb265ecd6c06de7b873c.png)

默认的10秒间隔仍然觉得有些密集，于是我把它改成了20秒。

### 效果视频

设置提醒间隔之后，整体体验改善了不少，声音不会再过于频繁地响起。只是这部分操作当时没有录制下来，之后有机会再补充，不过功能本身已经可以正常使用。

# Chrome插件安装

## 在本地加载插件

打开Chrome浏览器，在地址栏输入 `chrome://extensions/` 进入扩展程序管理页面。接着开启右上角的“开发者模式”，点击“加载已解压的扩展程序”，选择保存插件源码的文件夹即可完成安装。

![](img/c90564b1b1cd0135dcaa0738a06881f7.png)

![](img/eeb0ab18fa9578a28df8e80a3f1ac3ae.png)

![](img/23b55f6333bb01268214fdce3a14e95d.png)

![](img/d81e1cd5068248879172d2f2703fc2ae.png)

安装完成后，别忘了点击插件旁边的Pin图标，将它固定到浏览器工具栏中，后续使用会更加方便。

# 结语

整个插件的代码编写大约用了40分钟，整理和撰写文档则花了两个多小时，中间还抽出了一些时间帮别人下载视频。

这次开发过程中，我真正亲自参与的部分并不算多，主要包括创建audio文件、把SVG转换成PNG、调整icon文件名，以及制作提醒音MP3。其余大量时间，基本都用在让CurSor协助排查和修复Bug上。

相比传统的开发方式，和CurSor沟通的过程非常轻松，像是在和朋友讨论问题一样，一边描述需求，一边根据反馈继续调整，最后就把整个插件完成了。如果换成我自己从头编写，类似的工具可能需要半天到一天时间，而借助CurSor，效率确实提升了很多。

即使没有编程基础，只要能够清楚表达自己的需求，也可以借助CurSor完成一些实用工具的制作。这种开发体验，确实非常方便。

# 附录

## v1.0版本

插件下载地址：

## v1.1版本

更新内容：新增标题关键词配置、定时检测功能，以及提醒音频播放间隔设置。

解压密码：JiaoYang12345

# 异常处理

## 比特浏览器没有声音

![](img/009e78ec9d59e2932cfaac6ac0e01500.png)

在比特浏览器中安装插件后，如果始终没有声音提醒，可以按照下面的方法进行设置：

![](img/83129375c65e2a79a28bd02c0dc4578a.png)

进入“指纹设置”，找到“启动参数”，添加以下内容，然后点击确定保存：

`--autoplay-policy=no-user-gesture-required`

![](img/0e9842c3c7723c531a645f012595d40c.png)

保存配置后，重新打开对应的浏览器窗口，插件就可以正常播放声音了。

现在应该能够听到提醒音。

参考：

Autoplay policy in Chrome

## 2024年12月4日 没有提醒声音

晚上使用时突然没有声音提醒，起初以为是插件出现了问题。后来检查发现，标题关键词被改成了【[您有新消息]】，与实际页面标题内容不一致。

将关键词修改回来即可：

![](img/dc9839ce6d04827eea3820c49677efcb.png)

![](img/579e6502d660bf258190456cf5b5f0e7.png)