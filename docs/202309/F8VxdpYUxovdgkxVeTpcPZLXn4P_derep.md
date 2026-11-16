# 零基础用 GPT 搭出爬虫，代码都不用自己敲
作者：龙哥



大家好，我是亮仔

## 开场白

之前分享过一个基于 selenium 的抓取方案，可环境配置那块真的劝退。装 chromedriver、配 Chrome 版本、处理各种插件冲突，折腾半天才跑起来。

执行力重要，性价比也重要。有没有一种打法，是不折腾浏览器、不手写代码，直接让 GPT 生成可直接用的爬虫脚本？【注：Python 运行环境仍然需要】

思路是有的，今天就带你整一套更省心的做法。

声明：本方法理论上可适配绝大多数网站，下面的示例仅作演示。实际使用时只需更换目标网站和提示词，不像某些教程那样只能爬特定平台。仅供学习参考，请勿用于违法违规用途。

## 全流程拆解

### 1，先把网页本体存下来
这一步看起来笨，其实很关键。网页结构的小白看不懂，专业名词也听不进去。直接把整页源码保存下来，让 GPT 自己去读结构最省事。

按 Ctrl+S 把目标页面完整保存到本地，路径最好固定在 C 盘或 D 盘，方便后面上传找文件。

![](img/68215eff039a5ea2d01d8efe82b08d40.png)

### 2，把文件丢给 GPT 并喂好指令
#### ① 文件上传
上传的文件格式必须是 html。

![](img/647725bbe4820682ba607923bfa829fc.png)

![](img/33a5b3cd8fd743aa05f9fcb567d88e47.png)

#### ② 提示词怎么给
大括号里的内容要按你的需求替换，这里以 AIGC 为例，后面有完整版可直接抄。

我通过访问如下链接：{目标链接复制过来} 得到了我需要的关键词{aigc}的网页，其内容如文件

我希望你能够通过案例知道爬取的内容结构 并制作一个针对该网页的分页的python爬虫脚本，可以自定义搜索内容，并最终生成一个我给你的例子格式的表格

例子如下：

其中我以第二条内容为例，

标题：{AIGC:我不是元宇宙的附庸品}

链接：{这里直接右键有个复制链接}



时间：{2022-11-17}

要求：

1.使用python和request

2.网站URL:weixin.sogou.com

3.输入关键字 [AIGC]

4.爬取标题、链接、来源，时间

5.抓取前2页的内容

6.爬取的结果输出到Excel文件中

7.你只需要返回如上要求的代码即可

8.记得通过使用该文件的html内容测试一下

![](img/aa560bfb97da37c3bfb753fb9d039134.png)

上面这段话可以直接在目标页复制，字段要自己命名，灵活性很高。比如再加摘要、作者等都行。

理想的输出样式是这样：

![](img/31bb305e5a1dabfb20f8c6e80d48b53c.png)

跑一次后我建议再加两个控制项：一是明确爬取页数，避免无限跑；二是每爬完一页休眠几秒，降低被反爬的风险。这两点可以直接追加到指令里。如果你想要更稳，可以再加：11.增加适量的伪装以应对反爬虫

9.初始爬取页数为3

10.爬取完一页后休眠5秒

#### ③ 可直接复制的完整提示词
【所有 {} 内的内容请自行替换，替换完后删除大括号】

```
我通过访问如下链接：{目标链接复制过来} 得到了我需要的关键词aigc的网页，其内容如文件，我希望通过该案例制作一个该内容的爬虫
我希望你能够通过案例知道爬取的内容结构 并制作一个针对该网页的分页（前两页即可）的python爬虫脚本，可以自定义搜索内容，并最终生成一个我给你的例子格式的表格
例子如下：
    其中我以第二条内容为例，
    标题：{AIGC:我不是元宇宙的附庸品}
    链接：{这里直接右键有个复制链接}
    来源：{雷峰网}
    时间：{2022-11-17}
要求：
    1.使用python和request
    2.网站URL:{weixin.sogou.com}
    3.关键字为AIGC,该关键字在程序中为一个变量
    4.爬取{标题、链接、来源，时间}
    5.抓取前{2}页的内容
    6.爬取的结果输出到Excel文件中
    7.你只需要返回如上要求的代码即可
    8.记得通过使用该文件的html内容测试一下
    9.爬取完一页后休眠5秒
    10.增加适量的伪装以应对反爬虫
```

如果代码有报错，别怕，让它自己修。GPT 会根据报错信息迭代修复。

![](img/26b3074a32dc491f03e287a3e738d400.png)

### 3，拿代码跑起来
最终得到的脚本大概长这样：

```
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_articles(keyword, pages=2):
    base_url = "https://weixin.sogou.com/weixin"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_articles = []

    for page in range(1, pages + 1):
        params = {
            'type': '2',
            'query': keyword,
            'page': page
        }

        response = requests.get(base_url, params=params, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all("h3")

        for article in articles:
            title = article.a.text.strip()
            link = article.a['href']
            details_section = article.find_next_sibling('div')
            source = details_section.find('span', class_='all-time-y2').text.strip()
            time_text = details_section.find('span', class_='s2').text.strip()
            all_articles.append((title, link, source, time_text))

    return all_articles

def save_to_excel(data, filename="articles.xlsx"):
    df = pd.DataFrame(data, columns=["Title", "Link", "Source", "Time"])
    df.to_excel(filename, index=False)
    return filename

# Example usage:
# articles = fetch_articles("aigc", pages=2)
# save_to_excel(articles)

```

注意最后两行可能被注释掉了，记得取消注释。

在本地新建一个 main.py 文件，直接把代码粘进去。Win+R 打开 cmd，切换到文件所在盘，比如 D 盘，然后执行 python main.py 即可。

![](img/655714836f90ca4a47c1c26489fb38c3.png)

#### 第一次运行效果
执行后的控制台输出如下：

![](img/9821f7f200bb475bfe0f2875eb65f493.png)

#### 遇到的小 bug
这次时间字段没抓到，其他字段都正常了。让 GPT 针对时间解析做一次小调整就行。

![](img/c117d8f5eb3fe35447b999e7670d3090.png)

#### 最终结果
调整后跑通，表格导出效果如下：

![](img/84e59009325a3573c89ae45575774160.png)

![](img/552fd8a81a5cd665cb3ddcdd352a7f98.png)

如果不知道要装哪些依赖，怎么 pip install，也可以直接问 GPT4，它会给出清单。

### 完整脚本
最终可用的完整代码如下：

```
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import  datetime

def fetch_articles(keyword, pages=3):
    base_url = "https://weixin.sogou.com/weixin"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',

    }

    all_articles = []

    for page in range(1, pages + 1):
        params = {
            'type': '2',
            'query': keyword,
            'page': page
        }

        response = requests.get(base_url, params=params, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.find_all("h3")

        for article in articles:
            title = article.a.text.strip()
            link = article.a['href']
            details_section = article.find_next_sibling('div')
            source = details_section.find('span', class_='all-time-y2').text.strip()

            time_script = details_section.find('span', class_='s2').script.string
            timestamp_match = re.search(r"timeConvert\('(\d+)'\)", time_script)
            if timestamp_match:
                timestamp = int(timestamp_match.group(1))
                formatted_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            else:
                formatted_time = "N/A"

            all_articles.append((title, link, source, formatted_time))
        time.sleep(3)
    return all_articles

def save_to_excel(data, filename="articles1.xlsx"):
    df = pd.DataFrame(data, columns=["Title", "Link", "Source", "Time"])
    df.to_excel(filename, index=False)
    return filename

# To use the script:
results_path = save_to_excel(fetch_articles("AIGC"))
print(f"Results saved to: {results_path}")
```

#### 致谢
本文思路参考了圈友 @毅鸣 的分享，并在上做了补充优化，原链接如下

https://wx.zsxq.com/mweb/views/topicdetail/topicdetail.html?topic_id=188514455288512

有任何细节不明白的可以直接评论，我会针对性修改。

点赞破 50 的话考虑出一个面向 GPT3.5 的版本。

gpt 对话记录【可直接查看】

https://chat.openai.com/share/bcd80563-ee70-41e4-94e7-5223d0a5f489