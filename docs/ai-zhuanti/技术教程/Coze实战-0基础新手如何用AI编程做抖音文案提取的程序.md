# Coze实战|0基础新手如何用AI编程做抖音文案提取的程序
作者：龙哥

大家好，我是龙哥。做过六年程序员，现在自由职业，主要做 RPA 定制和小红书运营，同时也是赚钱 RPA 航海教练，偶尔教大家怎么用 AI 写代码。最近 Coze 在字节系生态里热度很高，像抖音评论区自动回复、飞书表格这类用法，已经被很多人当成提效工具。今天这篇内容，就是来聊聊：一个完全没写过代码的人，如何借助 AI 写代码，配合 Coze，做出一个属于自己的小工具。如果不想看文字，文末有视频教程；效果展示：

![](img/zhuanqian_a9e945826473d6168156383c4bdf48e5.png)

![](img/zhuanqian_560efa4069b434fe79b279f1818a9130.png)

先说说 Coze 到底是什么。字节官方的定义是：一站式 AI Bot 开发平台，无论有没有编程经验，都能在上面快速搭建基于 AI 模型的问答机器人，既能处理简单问题，也能应对复杂对话；做完之后还能发布到各类社交平台和通讯软件，跟用户互动。这段描述有点绕，我的理解是：你相当于拥有一个“数字助理”，这个助理拥有你想要的大模型能力。Coze 有国内版和海外版，国内版入口是 coze.cn，官方文档在 coze.cn/docs/guides/welcome；海外版是 coze.com。我们这次用国内版就足够了。

接下来做第一个 Bot，让它扮演大厨，教你做各种菜。流程非常简单：打开 Coze 网站注册，然后依次执行“创建 Bot -> 选择工作空间 -> 填写 Bot 名称 -> 确认”。

![](img/zhuanqian_05f1f18fcaa69f9096ebd8613f8ad33e.png)

进入编辑页面后你会发现，这个小助理的所有能力，都写在“指令”里。你写一次指令，它的功能就定型了。

![](img/zhuanqian_1fb2646afd7d26f190172d1c50de153c.png)

编辑页面分成三个区域：配置区、扩展区、预览区。配置区用来描述你想要的功能，比如先写一句“扮演一个厨师，能够提供各种菜的做法”，然后点“优化”，系统会自动补全一段更完整的指令。

![](img/zhuanqian_198d666a8710185dc8582b1b5082e226.png)

![](img/zhuanqian_dcee94fe3ebc2c58963202f4aa3b8e55.png)

扩展区是为了高级场景准备的，例如图片处理、调用别人写好的模块，这时就需要在配置区的描述中加入对应的代码；但我们的第一个 Bot 用不到扩展区，直接跟大模型聊天就够了。预览区用于验证，输入“牛肉的制作方式”发出去，机器人就会给出答案。

![](img/zhuanqian_7bf6bce460fda2de484972d1c8b60097.png)

验证完成后，记得保存，并把 Bot 的名字改成“一泽的大厨师”。

![](img/zhuanqian_5e8cdea2256b1fc363242baa687a43c2.png)

![](img/zhuanqian_7b41b64c71ef8de75f74c66ce3746713.png)

![](img/zhuanqian_cfa9147a70b5ec72816c119499ad488b.png)

改完名之后，点右上角的“发布”，等系统自动生成介绍，再点“确认”。

![](img/zhuanqian_9a7bcf6d91bc021c6bac20ffd848478e.png)

![](img/zhuanqian_5ea51ccb2f59bcf4e147ff00c1a91746.png)

发布之后去哪儿找呢？如果是“扣子 Bot 商店”，用户搜索“一泽的大厨师”就能找到；也可以放到抖音评论区，用户评论想知道某道菜怎么做时自动触发；还有“Bot as API”模式，允许我们自己写一个 exe 程序，不依赖 Coze 网页，甚至可以拿去商用。因为我们的目标是让 Python 能调用这个大厨，而官方界面不直接支持，所以发布时务必勾选“Bot as API”，再点发布才有意义。

![](img/zhuanqian_062f77a67e05a6a8014f98e26a4948c6.png)

接下来解决一个问题：怎么让 Pycharm 和 Coze 连接起来？答案是通过 API 传消息。Coze 官方提供了一份 API 文档，链接在 https://www.coze.cn/docs/developer_guides/coze_api_overview ，但里面全是专业术语，看得人头疼。

![](img/zhuanqian_9188f8ce7387939e94da73b214dc6777.png)

点开“发起对话”页面，依然是一堆复杂参数。

![](img/zhuanqian_f609fb95b9f1c7f452286b6669d43432.png)

我的办法是：把这部分内容复制下来，丢给 Kimi，让它帮忙分析，顺便生成一段能与 Coze 通信的 Python 代码。

![](img/zhuanqian_a44acf104d856824c1b426434f33b036.png)

![](img/zhuanqian_7e0effee233c5abc68166f1c5594f381.png)

Kimi 返回的代码大致如下：

```
import requests
import json
# 配置 Coze API 接口信息
api_url = 'https://api.coze.cn/open_api/v2/chat'
headers = {
'Authorization': 'Bearer YOUR_PERSONAL_ACCESS_TOKEN',  # 替换为你的个人访问令牌
'Content-Type': 'application/json',
'Connection': 'keep-alive',
'Accept': '*/*'
}
# 配置请求体
data = {
'bot_id': 'YOUR_BOT_ID',  # 替换为你的 Bot ID
'user': 'user_example',
'query': '你好，Coze!', # 替换为你的问题
'stream': False
}
def coze_chat():
# 发起对话请求
response = requests.post(api_url, headers=headers, json=data)
# 检查响应状态码
if response.status_code == 200:
# 解析响应内容
response_data = response.json()
print("Response from Coze:")
print(json.dumps(response_data, indent=2, ensure_ascii=False))
else:
print("Failed to connect to Coze API:", response.status_code)
# 调用函数
coze_chat()
```

简单看了一下，它需要我们在代码里填两个关键信息：一个是私人令牌，另一个是机器人编号。

![](img/zhuanqian_a8932a626cc7d2026c18fb22d13ed1f1.png)

这两个东西是什么、从哪来？打个比方：男生和女生要通过介绍认识，至少得知道对方的学校和学号吧？不然就只能靠漂流瓶了。对照 API 文档就能明白：令牌代表“这个应用是谁开发的”，机器人编号则表示“这是第几个机器人”。

![](img/zhuanqian_9fe94d7a0243659ea2810ed3b7153f4c.png)

令牌在创建空间的时候就已经存在了，那是你在这个平台上的合法身份。机器人编号其实就是机器人页面网址末尾的一串数字，在这个项目里是 7385099152600121363。

![](img/zhuanqian_a0c4c762251a43aaddabd42decefe7f3.png)

同时，代码里还有一个 query 字段，把它改成你要问的菜名即可。

![](img/zhuanqian_aac956ede393b3919d08cadc57fd49ba.png)

对话结果如下：

![](img/zhuanqian_e7c0d6399f1b9bfcd9a8495ec68a3003.png)

现在目标很明确：使用 AI 写代码 + Pycharm，做出一个能脱离 Coze 网页独立运行的 exe 程序。

![](img/zhuanqian_f1942e8e8d3ff452e90c91f0d516f517.png)

先放下 Coze 的事。要做成可执行程序，让别人用起来顺手，必须有操作界面。这个界面需要四样东西：第一，采用 Pyside6 框架（其他能生成界面的框架也可以）；第二，一个日志展示区域；第三，一个文本输入区，里边要有提示文字“请输入你想要吃的菜”；第四，一个确认按钮。

![](img/zhuanqian_d4b2c4452717ca2c7aebdce1d3ee96db.png)

操作界面同样可以交给 AI。打开任意大模型对话框，比如 GPT 或 Kimi，输入这么一句：“帮我写一个 pyside6 的代码，要有一个 log 日志输出框，一个文本输入框（有提示词：请输入你想要的菜的做法），一个确定按钮。”简单直接，AI 就会给出代码。

![](img/zhuanqian_57fcc14ec01e1b279fac735c7f62ebed.png)

生成的界面代码是这样：

```
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, \
QPushButton, QTextEdit, QLineEdit, QLabel
class MainWindow(QWidget):
def __init__(self):
super().__init__()
self.initUI()
def initUI(self):
# 设置窗口标题和初始大小
self.setWindowTitle("PySide6 应用示例")
self.setGeometry(100, 100, 400, 300)
# 创建布局
layout = QVBoxLayout()
# 创建日志输出框
self.log_edit = QTextEdit()
self.log_edit.setReadOnly(True)
layout.addWidget(self.log_edit)
# 创建输入框和提示词
self.input_edit = QLineEdit()
self.input_edit.setPlaceholderText("请输入你想要的菜的做法")
layout.addWidget(self.input_edit)
# 创建确定按钮
self.confirm_button = QPushButton("确定")
self.confirm_button.clicked.connect(self.on_confirm_clicked)
layout.addWidget(self.confirm_button)
# 将布局添加到窗口
self.setLayout(layout)
def on_confirm_clicked(self):
# 当点击确定按钮时，将输入框的内容添加到日志框
text = self.input_edit.text()
self.log_edit.append(text)
if __name__ == '__main__':
app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec())
```

把它放进 Pycharm，缺库就自己 pip install。界面效果如下：

![](img/zhuanqian_5a9185c5d4a75dcb7fde50d69e9b0e24.png)

然后，把之前替换好令牌和机器人编号的两个 Python 文件一起交给 AI，请它优化，并实现这样的功能：按下确定键后，把输入框内容发送给 Coze，并分析返回结果。

![](img/zhuanqian_de31a76816121565546df3d1c5af3df5.png)

把 AI 优化后的代码复制回 Pycharm 运行，可能会发现之前的操作界面被改动了，但不影响功能。全部代码就放在文末。

```
import sys
import requests
import json
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, \
QPushButton, QTextEdit, QLineEdit, QLabel
class MainWindow(QWidget):
def __init__(self):
super().__init__()
self.initUI()
def initUI(self):
# 设置窗口标题和初始大小
self.setWindowTitle("Coze Chat Interface")
self.setGeometry(100, 100, 400, 300)
# 创建日志输出框
self.log_edit = QTextEdit()
self.log_edit.setReadOnly(True)
self.log_edit.setPlaceholderText("Coze 的回复将显示在这里")
# 创建输入框和提示词
self.input_edit = QLineEdit()
self.input_edit.setPlaceholderText("请输入你的问题")
# 创建确定按钮
self.confirm_button = QPushButton("确定")
self.confirm_button.clicked.connect(self.on_confirm_clicked)
# 创建布局并添加控件
layout = QVBoxLayout()
layout.addWidget(self.input_edit)
layout.addWidget(self.confirm_button)
layout.addWidget(self.log_edit)
self.setLayout(layout)
def on_confirm_clicked(self):
# 获取用户输入
user_input = self.input_edit.text()
if not user_input:
self.log_edit.append("请输入问题")
return
# 发送请求到 Coze API
self.send_to_coze(user_input)
def send_to_coze(self, query):
api_url = 'https://api.coze.cn/open_api/v2/chat'
headers = {
'Authorization': 'Bearer 456',  # 替换为你的个人访问令牌
'Content-Type': 'application/json',
'Connection': 'keep-alive',
'Accept': '*/*'
}
data = {
'bot_id': '123',  # 替换为你的 Bot ID
'user': 'user_example',
'query': query,
'stream': False  # 根据 Coze API 的要求设置
}
try:
response = requests.post(api_url, headers=headers, json=data)
response.raise_for_status()  # 如果响应状态不是 200，将抛出异常
response_data = response.json()
# 显示 Coze 的回复
self.display_response(response_data)
except requests.exceptions.RequestException as e:
self.log_edit.append(f"请求 Coze API 时发生错误: {e}")
def display_response(self, response_data):
# 这里我们假设 Coze API 返回的是非流式响应
if 'messages' in response_data:
for message in response_data['messages']:
if message['role'] == 'assistant' and message['type'] == 'answer':
self.log_edit.append(message['content'])
if __name__ == '__main__':
app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec())
```

运行后，输入【菜名】，然后点击【确定】。

一个小提醒：因为 Coze 的交互本身需要一定时间，点击确认之后，程序可能会卡住 5 到 10 秒，看起来像“无响应”，别担心，稍等片刻就好。

![](img/zhuanqian_85b2aa0cab475a18deaa52a4a9ef96be.png)

## 4.7 打包成 exe 可执行文件

如果希望脱离 PyCharm，让程序能在别的电脑上直接跑，该怎么做？

1. 在 PyCharm 底部或左下角，打开你的【Terminal】终端。

2. 输入这行命令：pyinstaller -F -w 大厨.py

3. 等它执行完，在对应路径下会生成一个 dist 文件夹，里面的 exe 文件就是打包好的可执行程序。

小贴士：pyinstaller 打包命令说明

-F：将所有内容打包成单个文件

-w：不显示调试窗口

大厨.py：你的 Python 代码文件

如果还没装 pyinstaller，可先执行下面这行安装命令：

pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple

![](img/zhuanqian_35aabfe1f18b7c7d4c4ab22e86b2e37f.png)

![](img/zhuanqian_7fa244be24ddff7edce37ca3cfc681a7.png)

![](img/zhuanqian_4d296f8d43e3f0aa1777ec3daaadc105.png)

![](img/zhuanqian_c68473e875e689a036b9cc21fd5cc248.png)

# 5. 用 AI 编程搞定抖音文案采集

## 5.1 抖音文案需求

现在进入大家最熟悉的场景：【抖音文案采集 & 仿写】

那要怎么在现有【大厨】机器人的基础上，改造成支持抖音文案采集呢？

老套路，先看 UI：

![](img/zhuanqian_58a5cda9cd8b9870ee75528712d31b66.png)

这个 UI 框架和【大厨】机器人基本一致。

真正的核心改动，就在 Coze 的功能配置上。

## 5.2 修改文案功能

需要调整功能区里的描述：

把用户提交的抖音链接传给工作流，并输出工作流返回的文档。

当然，还要经过【优化】这一步。

![](img/zhuanqian_a10f8396163d025474178b47bf8abf5f.png)

## 5.3 调整插件部分

除了功能区要改，现在还缺一个“干活的主力”——把视频内容转成文案，所以我们需要一个【工作流】来承担这项工作。

### 5.3.1 方案一：直接用现成的插件

去【工作流市场】里搜一搜，看看有没有人已经开发好了“抖音视频转文案”的插件。

![](img/zhuanqian_b2edfca531f30d27aa145fad77ff1799.png)

![](img/zhuanqian_987781003313fd57d6456cd7705bb8fb.png)

![](img/zhuanqian_40fd3e6a8c1e2101fba62b7293ef1887.png)

一搜就能找到不少，挑一个功能符合你需求的，然后点【复制并添加】。

如果搜不到，可以试试这个关键词：【douyin_video_to_text_summary】

![](img/zhuanqian_c3628d0f2f838485216e6b8eb7ffb4db.png)

### 5.3.2 方案二：自己动手写

![](img/zhuanqian_9acd32a0a82b0f2835ff84a2af9fdb66.png)

![](img/zhuanqian_d94280c7a471f93392339dda4c5ba69c.png)

进入编辑界面后，能看到两个模块：【开始】和【结束】。

中间的区域，就是我们要操作的地方。

要实现抖音文案的提取与改写，需要按下面的流程走：

插件流程图：

【开始】- 设置输入：抖音链接

![](img/zhuanqian_d0d743f33ae7080962ca9e2e7c39a474.png)

搜索插件【LinkReaderPlugin】

![](img/zhuanqian_5f1998c726c35af98a74283e4aeb4193.png)

【提取抖音视频文本】 - 依赖插件：【LinkReaderPlugin】，让 url 参数指向【开始】的输入

![](img/zhuanqian_f050af23a0ef684991a65437250c3501.png)

【输出】

把输出内容设为提取模块返回的【content】

![](img/zhuanqian_67ac3f3468fbed0e9361f63ebe61fff4.png)

## 5.4 PyCharm 代码调整

代码的逻辑部分不需要动，只要回到原来的 UI 界面，把输入改成抖音链接，让程序帮我们生成文案就行。

![](img/zhuanqian_bcc9cf36f19e8e81b9b012e9c6d8dac5.png)

等它跑完，结果长这样：

![](img/zhuanqian_45a7f45e1e8674f8741785b444603583.png)

## 5.5 生成可执行文件

方法见 4.7。

## 5.6 还能怎么优化

### 5.6.1 解决卡顿

从程序角度来说，点击【确定】后，程序会一直阻塞，出现【无响应】——其实是在等 Coze 返回结果。

怎么解决呢？

—— 招个“幕后打工人”：前台 UI 继续等着你点击，后台的“打工人”在默默干活。

用专业话说，就是：开一个线程。

### 5.6.2 提示词优化

程序员也不只是工具人，在对话框里加一些更友好、更人性化的提示词和过程反馈，体验会好很多：

![](img/zhuanqian_c46f8ad79bf826f16697b002ccb4b0e2.png)

### 5.6.3 优化后的完整代码

```
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
import requests
import re
import json
import threading
class LogApp(QWidget):
def __init__(self):
super().__init__()
self.initUI()
self.headers=''
self.payload=''
self.captureStat = 0
def initParam(self,link):
personal_access_token = 'YOUR_PERSONAL_ACCESS_TOKEN'
# 替换为你的Bot ID
bot_id = 'YOUR_BOT_ID'
# 构造请求头
headers = {
'Authorization': f'Bearer {personal_access_token}',
'Content-Type': 'application/json',
'Accept': '*/*',
# 'Host': 'api.coze.cn',
'Connection': 'keep-alive'
}
# 构造请求体
payload = {
"bot_id": bot_id,
"user": "29032201862555",
"query": link,
"stream": False,
}
self.payload = payload
self.headers = headers
def initUI(self):
# 创建布局
layout = QVBoxLayout()
# 创建文本编辑框，用于显示日志
self.logTextEdit = QTextEdit()
self.logTextEdit.setReadOnly(True)  # 设置为只读
layout.addWidget(self.logTextEdit)
# 创建文本输入框
self.inputLineEdit = QLineEdit()
self.inputLineEdit.setPlaceholderText('请输入抖音链接')
layout.addWidget(self.inputLineEdit)
# 创建确定按钮
self.confirmButton = QPushButton('确定')
self.confirmButton.clicked.connect(self.on_confirm_click)
layout.addWidget(self.confirmButton)
# 设置布局
self.setLayout(layout)
self.setWindowTitle('一泽的抖音文案提取大师')  # 设置窗口标题
self.setGeometry(300, 300, 400, 300)  # 设置窗口位置和大小
def log(self, message):
"""将消息添加到日志文本框"""
self.logTextEdit.append(message)
def is_douyin_link(self,url):
# 定义抖音链接的正则表达式
pattern = r'https://www\.douyin\.com/[a-zA-Z0-9]+'
# 使用正则表达式匹配链接
if re.match(pattern, url):
return True
else:
return False
def on_confirm_click(self):
"""确定按钮点击事件处理"""
if self.captureStat == 0:
self.captureStat = 1
self.log(f'一泽的coze采集大师...')
self.log(f'让我瞅瞅怎么个事...')
process_thread = threading.Thread(target=self.capture)
# 启动线程
process_thread.start()
else:
self.log(f'别催了别催了，在看了')
def capture(self):
link = self.inputLineEdit.text()
stat = self.is_douyin_link(link)
if stat == False:
self.log(f'手欠，链接输入错了')
self.captureStat = 0
return 0
self.initParam(link)
# 发送POST请求
response = requests.post(
'https://api.coze.cn/open_api/v2/chat',
headers=self.headers,
json=self.payload  # 注意这里使用的是json参数而不是data
)
# 打印响应内容
if response.ok:
print('请求成功，返回数据：')
# print(response.json())
self.log(f'\n等久了吧，我来了\n')
response_data = response.json()
print(response_data)
if 'messages' in response_data:
for message in response_data['messages']:
if message['role'] == 'assistant' and message['type'] == 'answer':
self.log(message['content'])
else:
print('请求失败，状态码：', response.status_code)
print('错误信息：', response.text)
self.captureStat = 0
user_input = self.inputLineEdit.text()
# self.log(f'用户输入: {user_input}')
def main():
app = QApplication(sys.argv)
ex = LogApp()
ex.show()
sys.exit(app.exec())
if __name__ == '__main__':
main()
```

### 5.6.4 流式输出代码（边生成边输出）

本节聚焦于让代码结果不再等待完整生成后再呈现，而是采用逐块推送的实时展现方式。整个过程是边计算边返回、边返回边渲染，使用户能够第一时间看到正在成型的代码片段，并在生成过程中即时跟进和交互。

![](img/zhuanqian_d15c3f2a215f0e3b667c504db78bdf59.png)

```
import sys
import requests
import json
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit
from PySide6.QtCore import QThread, Signal
import threading
class CozeAPIThread(QThread):
response_signal = Signal(str)
def __init__(self, api_url, headers, data):
super().__init__()
self.api_url = api_url
self.headers = headers
self.data = data
self.active = True
def run(self):
try:
with requests.post(self.api_url, headers=self.headers, json=self.data, stream=True) as response:
response.raise_for_status()
for line in response.iter_lines():
if line:
self.response_signal.emit(line.decode('utf-8'))
finally:
self.active = False
def stop(self):
self.active = False
class MainWindow(QWidget):
def __init__(self):
super().__init__()
self.initUI()
self.querystat = 0
def initUI(self):
self.setWindowTitle("Coze Chat Interface")
self.setGeometry(100, 100, 400, 300)
self.log_edit = QTextEdit()
self.log_edit.setReadOnly(True)
self.log_edit.setPlaceholderText("Coze 的回复将显示在这里")
self.input_edit = QLineEdit()
self.input_edit.setPlaceholderText("请输入你的问题")
self.confirm_button = QPushButton("确定")
self.confirm_button.clicked.connect(self.on_confirm_clicked)
layout = QVBoxLayout()
layout.addWidget(self.log_edit)
layout.addWidget(self.input_edit)
layout.addWidget(self.confirm_button)
self.setLayout(layout)
self.api_thread = None
def on_confirm_clicked(self):
if self.querystat == 0:
self.querystat = 1
self.log_edit.append("开始处理")
process_thread = threading.Thread(target=self.capture)
process_thread.start()
else:
self.log_edit.append("在处理了")
def capture(self):
query = self.input_edit.text()
if query:
self.start_coze_api_thread(query)
def start_coze_api_thread(self, query):
api_url = 'https://api.coze.cn/open_api/v2/chat'
headers = {
'Authorization': 'Bearer YOUR_PERSONAL_ACCESS_TOKEN',  # 替换为你的个人访问令牌
'Content-Type': 'application/json',
'Connection': 'keep-alive',
'Accept': '*/*'
}
data = {
'bot_id': 'YOUR_BOT_ID',  # 替换为你的 Bot ID
'user': 'user_example',
'query': query,
'stream': True
}
if self.api_thread is not None and self.api_thread.isRunning():
self.api_thread.stop()
self.api_thread.wait()
self.api_thread = CozeAPIThread(api_url, headers, data)
self.api_thread.response_signal.connect(self.display_response)
self.api_thread.start()
def display_response(self, line):
# 检查是否包含 "data:" 前缀，并去除它以及随后的空格
if line.startswith("data:"):
# 去除 "data:" 和可能的空格，然后解析外部的 JSON 对象
line = line[5:].strip()
try:
# 解析 JSON 数据
data = json.loads(line)
event = data.get('event')
# 检查是否是消息事件
if event == 'message':
# 获取消息内容
message = data.get('message', {})
content = message.get('content', '')
content = content.replace('\\n', '\n').replace('\\', '')
# 打印 'content' 字段的内容
print(content)
self.log_edit.append(content)
elif event == 'done':
self.querystat = 0
self.log_edit.append("本次结束")
return
except json.JSONDecodeError as e:
# 如果解析 JSON 失败，记录错误信息
self.log_edit.append(f"解析 JSON 错误: {e} - 原始行: {line}")
else:
# 如果行格式未知，打印提示
self.log_edit.append(f"未知格式的行: {line}")
if __name__ == '__main__':
app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
sys.exit(app.exec())
```

# 6.使用过程中容易踩的坑

感谢圈友【大麦】把实操中遇到的卡点汇总整理，简化复盘如下：

1、依赖库安装耗时。首次部署需要执行 pip install PySide6，默认源下载速度偏慢，耗时可能超过半小时。建议切换到国内镜像源加速，例如使用清华源：pip install PySide6 -i https://pypi.tuna.tsinghua.edu.cn/simple

2、发布前先创建 API。若未提前新建接口，发布阶段将找不到【Bot as api】的选项，导致无法继续。

3、个人令牌仅展示一次。生成 Token 时务必立即复制保存，后续不会再显示。之前有同学因为没保存只能先删除再重新申请。

4、调用时注意头部格式。借用示例代码前，记得把自己的个人令牌和 Bot_id 填入，并要在令牌前缀加上 Bearer，这是 Bearer Token 的标准标识，补充后程序才能正常通信。

5、界面会短暂卡顿。输入关键词点击确认后，界面可能停顿数秒才返回结果。这是单线程运行导致的，程序在等待 Coze 回复期间无法响应 UI 操作。解决方法是另起一个线程去异步等待返回，已在 5.6.3 完整版中补充。

# 7.收尾

本次内容分享就先到这里。Coze 的玩法远不止于此，还有很多方向可以继续探索。

如果你有任何想法或改进建议，欢迎提出交流。

我是泽泽，有问题可以加 V：z8401483498