# 别再卡在灰豚/考古类数据站了，这套思路直接上手

> 来源：[https://bc8fd5oefm.feishu.cn/docx/SrOXdYezPogfRnx4wnAcb3w8nVR](https://bc8fd5oefm.feishu.cn/docx/SrOXdYezPogfRnx4wnAcb3w8nVR)

本文共拆成三块来看，
第一块，干嘛要去爬这类数据中转站
第二块，为啥常规爬虫在这类站点上会失效
第三块，具体怎么把数据拿下来

### 一、为什么要盯上它

自己动手去扒淘宝这种头部站点，体验基本就是被反爬教育。验证码、风控、动态指纹，折腾到最后怀疑人生。

但换个角度想，如果有人已经把这些难啃的骨头啃完了，并把结果整理到自家的数据平台上呢？你只需要对准这个“二道贩子”站点下手就行了，成本直接降下来。

像灰豚这类的数据聚合平台，本质就是把源站的数据收敛、整理后重新分发。它对外的反爬强度普遍远低于源站，或许是会开锁的不一定会造锁。花点会员费，别人帮你把重活脏活做了，你直接拿现成结果。

当然，平台也不会把所有东西都敞开给你，付费看板、深度分析、交叉报表这些增值内容，往往就需要自己动手补充采集。

### 二、为什么老办法不好使

上次有朋友吐槽，用 ChatGPT 生成爬虫脚本很爽，碰到灰豚这种数据站就傻眼了。

原因很简单，这类站点的数据加载方式变了。数据量大不可能一次性塞进 HTML 里，页面会半天打不开。所以现在主流的做法是先把页面骨架扔出来给用户看，数据通过后台异步请求再填充进去，这就是典型的 Ajax 加载。

数据不在源码里裸奔，而是藏在接口返回的 JSON 里。想要拿到，就得先找到它发请求的地址，再去解析 JSON 结构。

好消息是，GPT 在分析接口和拆结构上很在行，能把工作量砍掉一大半。

### 三、怎么爬

核心就两个问题：数据在哪，拿到数据的正确姿势是什么。

#### 1. 数据在哪

实操环节开始了。

**先打开目标页面**
先想清楚你要什么。比如下文以灰豚的小红书近30天笔记为例，用一个普通账号做演示。

打开网页后按 F12，很多人看到开发者工具就退缩了，其实没那么玄乎，多点几次就熟了。

**第一步，切换到 Fetch/XHR**
![](img/ae4267c54e9cc0256a6e72b999b6d528.png)

**第二步，找到对应的接口**
这类请求基本都是 Ajax 产生的，一长串列表里挑哪个？

有两个判断方法：
方案一：看名字。开发写接口名时通常会照顾可读性，直接从命名就能猜个八九不离十。比如 currentUser、detail、noteOverview、notes10，分别对应当前用户、详情、笔记概览、近10条笔记。点进去对照页面内容就能确认，响应里是否包含你想要的字段，挑一个或多个都行。
方案二：直接搜索。点进任意一个请求后用 Ctrl+F 搜索关键词，比如用户名、笔记数。
![](img/af42423238bad6b48bf55998e4ed7528.png)

**第三步，读懂结构**
基本都能定位到数据所在的接口。数据长这样：{x:x}，这是标准的 JSON。双击后会用 JSONView 插件打开，结构一目了然。请求头里可以看到完整的请求 URL，这就是数据接口的入口，后面写代码要用¹

[图中为jsonview插件显示结果，默认为直接平铺了]
![](img/d026c1c8d8df4bbe0bfe864c643089c2.png)
![](img/eb298b7bb59779fb4275e645732ad454.png)

搞清楚 URL 规律就好办了。每个用户对应一个 id，这个 id 就能拼进请求地址里。所以批量采集的思路很清晰：把目标用户 id 整理到 Excel，每天跑一次定时拉取，就能监控对标账号动态。当然也可以用定时爬虫，只是频率越低越安全。

![](img/cd4d40570c30f7ac24cedb6e10e87592.png)

#### 2. 数据怎么拿

路径清楚了，怎么带着合法的身份去请求呢？

小白也能用 GPT 代劳，熟手也一样，写脚本太耗时间。

把接口地址和目标内容丢给 GPT，如果数据体量大，就截取一小部分做样本，让它基于局部推全。关键点在于登录态。

登录后服务器会给你一个身份凭证，通常就是 Cookie，里面包含了手机号密码组合加密后的 token。后面请求时要带上它。

打开目标页，在请求头里找到 Cookie，提炼出核心几个字段交给 GPT 放在请求头里，优先保证 Cookie 有效。

![](img/dbdcac5f335f1562d7ee1e4f0e9465f3.png)

如果跑起来拿不到数据，就重新抓一次请求头给 GPT，让它重写。要注意 token 长度限制。

提示词参考：
![](img/42dd9f51a7908787bb9cb258f41ea0d3.png)

运行效果如下：
![](img/df794dc6647bb6f52a6a6f29922fe850.png)

一次就通了，主要是 Ajax 返回的数据 pandas 能直接识别，灰豚的反爬也不算严，所以整体工作量很小。
![](img/6f7503cdd2bd9cc1c72a48b72223992b.png)

#### 3、收尾

这个案例具备通用性。灰豚绝大多数数据都是 Ajax 方式下发。

对普通人来说门槛在于第一次打开开发者工具。但跨过去之后，市场上的数据基本就两种形态：直接写在页面的静态数据，和通过 Ajax 请求的动态数据。配合我之前的两篇实战思路，https://t.zsxq.com/13k6dgddP，基本在 GPT 辅助下都能搞定。

GPT 生成的示例代码片段如下：

"""
为了从给定的 JSON 数据中提取 extData 并将其转换为表格，你可以使用 Python 的 requests 库获取数据，然后使用 pandas 库将数据转换为表格。下面是一段示例代码：

```
pythonCopy code
import requests
import pandas as pd
import json

# 定义请求的 URL 和 headers
url = "https://xhsapi.huitun.com/anchor/detail/notes10?_t=1698647452631&anchorId=5fb23b21000000000100bee3"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Cookie": "填写你的cookie即可"
}

# 发送 GET 请求
response = requests.get(url, headers=headers)

# 检查响应状态if response.status_code == 200:
    # 解析 JSON 数据
    data = json.loads(response.text)

    # 提取 extData
    ext_data = data.get("extData", [])

    # 转换为 DataFrame
    df = pd.DataFrame(ext_data)

    # 保存为 CSV 文件（或其他格式）
    df.to_csv("extData.csv", index=False)
```

请注意：

*   你需要将 your_user_agent_here 替换为实际的 User-Agent 字符串。

*   由于我无法访问外部网络，因此无法运行该代码进行测试。

这样，你就能得到一个名为 extData.csv 的 CSV 文件，其中包含 extData 中的所有数据。

如果你还没有安装 requests 和 pandas，你可以使用以下命令进行安装：

```
bashCopy code
pip install requests pandas
```

这只是一个基础示例，你可以根据自己的需求进行相应的调整。希望这能帮助你！

"""