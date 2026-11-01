# Coze/扣子零代码搭MVP：让公众号自动提炼要点并定时送达微信，附8000字实操手记



各位好，我是拔刀刘，Coze提效大航海的带队教练。

现在手上带了两千三百多名同行者，依旧在路上。这次拿自己的一次尝试，给技术门槛高的朋友一点信心：在大模型时代，借助现成工具，即便不写一行代码，也能把想法迅速变成可用原型。

![](img/0bc51b70a17b9dd49a2d3ea9036ca608.png)

## 一、缘起与需求

这个点子纯粹来自个人痛点。订阅的公众号越来越多，打开信息就变成一种负担。心里总惦记着“别漏了”，可真去逐篇点开又太耗时。理想的形态是：有个小助手先把我关注号的最新内容抓回来、浓缩成要点，发到微信里让我扫一眼，觉得值得再去看原文。

如果再进一步，把播客、微博、X、知识星球、群聊等信息源也一并汇集，定期汇总推送，体验会更完整。以前靠RSS把各种源统一起来，但RSS只能给原文，没有提炼，总差一口气。所以决定先用Coze造一个Bot，从公众号入手，把主干流程跑通。

![](img/d865331bae5f140f4461e1d4e14c3a79.png)

## 二、最终呈现

文章篇幅较长，先把成果效果放前面，给大家一个继续看下去的理由。感兴趣怎么做的，下面有八千余字和六十余张图的逐条拆解；不想自己搭的，我会把完整流程和提示词开源，获取方式在文末。

请忽略我的年老字体和暗色主题[捂脸][捂脸][捂脸]

## 三、流程拆解思路

工作流的本质，是把高频重复的工序固化，提升效率。比如你想把一条抖音文案转成文字，流程是复制链接、打开小程序、粘贴链接、等待识别、复制结果、粘到文档，中间还可能弹出广告。做一次就这一套动作，重复做就是消耗。工作流就是把这条动作链变成自动化的路径。

从复制链接到文案落地文档这一段，本质上就是一条“入口-处理-出口”的链路，跟“把大象装进冰箱分几步”是同一类问题。

![](img/dfdf7e36381fa26b935ca4435c9ddc49.png)

### 1、主线拆解

把“自动提炼公众号内容并定时推送微信”拆开，核心就三段：

1、获取公众号的文章
2、把文章做提炼
3、汇总后按时推送到微信

### 2、要素拆解

每一段里需要什么？

1、获取公众号文章：
先在Coze里找现成插件。可惜目前能读公众号的插件都停更了，用不了。

![](img/b865a25621c114ba603a992518fc069f.png)

没有即插即用的插件，就剩下两条路：自建抓取，或调用已有服务。回想RSS折腾时用过「瓦斯阅读」，抓公众号比较稳定，试了一下，成功拉到龙哥盟的最新内容。

![](img/ac58c132a46722e10fdd772cbd5863fd.png)

可很快发现收录不全，十个里七个找不到。像Coze官方号直接无记录。

![](img/41c77fb57cd38bd4eaea66f6dfbff457.png)

继续找替代方案。GitHub上有一个开源工具WeWe RSS，它借助微信读书的订阅机制去订阅公众号，看起来可行且优雅。

![](img/c4f9119ecb6959c1a40cc41824549309.png)

2、内容提炼：
这块基本是模型的强项，总结类任务大模型很在行，字节豆包就能胜任。难点在于批量：一个号多篇文章、多个号加起来量不小，所以要用到批处理能力，细节后面展开。

![](img/9e1191b46ed0bb4d1093eef678610392.png)

3、定时推微信：
分两件事：定时触发，Coze自带触发器可以搞定；微信推送，Coze没有现成模块，需要第三方服务桥接。

![](img/8ac1d473ffc299a662f59fffecc3ef3d.png)

之前用过「server酱」，它能用服务号模板消息把自定义文本推送到个人微信，做MVP阶段的免费额度完全够用。

![](img/067b2bd2b92a4a2435ce86e72c4e4725.png)

这里可能有人会问：这些工具平时根本想不起来怎么办？现阶段AI搜索太方便了，搜一下就能定位到可用方案。做事难不难，关键看愿不愿意查。

![](img/8c765b2317d35fd22bc86e477dc2f59f.png)

![](img/544684e2e9a11eb4166f21c491d93d53.png)

![](img/89ae4a95121ad1efcfee1611082d1ab5.png)

到这里，整条链路的各个环节都有可落地的方案，理论上可行。下面就进入搭建环节。

## 四、工作流搭建

### 1、整体蓝图

双击画布可看高清图，建议结合后续细节反复对照。

### 2、起始节点

开始节点需要用户提供两项输入：server酱的sendkey 和 rss清单。

* key：server酱的sendkey，获取方法见「相关资源」
* rss_list：RSS清单，没有的话可用我提供的测试数据先跑通

复制代码、提示词：

```
https://qnmlgb.tech/v2/rss?i=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRob3JfaWQiOiI1YjY5ODkzNzI0NGQ0ZTQwODg0ZWVhNjMiLCJ1c2VyX2lkIjoiNjE1NWNiY2NiZGRjZGI2OTYwZTkzMTBjIn0.ifLJz8mnwJOeq5dEhUAuCa_U9ovEPJQzYuymzZ7ZuYw
https://qnmlgb.tech/v2/rss?i=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRob3JfaWQiOiI1YmE1Yzg4NzI0NGQ0ZTJkMDJkMjVhYjIiLCJ1c2VyX2lkIjoiNjE1NWNiY2NiZGRjZGI2OTYwZTkzMTBjIn0.3hMRodTsvFCLPYoRTHY2syPQROuHq6_h_OGoSzz1oj4
```

![](img/b90e59e5ecda710dd75059f2329f34e0.png)

### 3、RSS清单切分

用「文本处理」节点把输入的清单拆成逐行，输出为数组，方便后续批量处理。

![](img/25831e2d676af1781cf0d8e4628e383b.png)

### 4、拉取RSS内容

使用插件里的“链接读取”节点读取清单里的内容。

![](img/790b764d0a09e56533d606c5d30bc200.png)

配置要点：

* 启用批处理
* 批处理输入选「分割RSS列表」的output
* 下面url参数填当前节点中的item1

![](img/a409bcf5d648685508ee082bbf3cf167.png)

### 5、汇总文章列表

上一步每个订阅源会返回最近几篇文章，包含作者、标题、链接。这里把所有结果收拢并格式化。

一般一个公众号每天不超过三篇，所以代码只保留各源最近三篇，提升运行速度。

使用「代码」节点，左侧选代码，输入项选上一步的outputList。打开IDE选Python，粘入如下代码：

复制代码、提示词：

```
import xml.etree.ElementTree as ET

async def main(args: Args) -> Output:
    params = args.params
    content_urls = params.get("content_urls", [])

    # 存储最终的结果集合
    unique_results = set()

    for item in content_urls:
        pdf_content = item.get("pdf_content")
        if pdf_content:
            try:
                # 解析 XML
                root = ET.fromstring(pdf_content)

                # 提取 channel 的标题作为 author
                channel_title = root.find('.//channel/title')
                author = channel_title.text if channel_title is not None else ""

                # 提取前3个 item
                item_count = 0  # 初始化计数器
                for item_element in root.findall('.//item'):
                    if item_count >= 3:  # 如果已经提取了3个，停止循环
                        break

                    item_title_element = item_element.find('title')
                    link_element = item_element.find('link')

                    item_title = item_title_element.text if item_title_element is not None else ""
                    url = link_element.text if link_element is not None else ""

                    # 验证和剔除无效链接
                    if url and not url.startswith("http://purl.org/rss/1.0/modules/content/") and not url.startswith("http://"):
                        # 拼接 author, title 和 url
                        combined = f"{author}@{item_title}@{url}"
                        unique_results.add(combined)
                        print(f"Added: {combined}")  # Debug information
                    else:
                        print(f"Filtered out URL: {url}")  # Debug information

                    item_count += 1  # 增加计数器

            except ET.ParseError as e:
                print(f"XML parsing error: {e}")  # Debug information

    # 去重并转换为字典数组
    result_list = []
    for entry in unique_results:
        author, title, url = entry.split('@', 2)  # 修改分割为三部分
        result_list.append({"author": author, "title": title, "url": url})

    ret: Output = {
        "content_urls": result_list
    }

    # 如果结果为空，输出调试信息
    if not ret["content_urls"]:
        print("No valid content URLs found.")  # Debug information

    return ret
```

输出配置：类型选「Array」，新增字段分别输出title、url、author。

![](img/249ad5bb8cfcfbb1f81fd034aed82cf6.png)

### 6、循环校验是否已推送

左侧工具栏选「循环」节点。循环节点负责决定次数，循环体负责处理每一项。输入是数组时，次数等于数组长度，逻辑类似for循环。

我们的目标是：对上一步的每篇文章在数据库里检索一次。找到说明之前已推送，本次跳过；找不到则是新内容，继续往后走。

![](img/67e53cfd01ec2b5d2adfbde7da64d7bd.png)

![](img/3c90bcb0007f656189630f709f45f23c.png)

循环输入项选上一步输出的全部文章。

![](img/deb6a15836f29727bdc0b97176449448.png)

进入循环体，逐个节点说明。

![](img/f94b79994cb6bf00457eb5629e61ac44.png)

循环体内——数据库查询

用数据库节点判断该文章是否已推送过。输入为当前文章url 和 起始节点的key，这里我把它重命名为suid。

设计之初就考虑多用户共用：不同人订阅的号不同，微信也不同，所以用server酱的sendkey作为用户唯一标识。

因此查询条件是url + suid。SQL由模型生成，直接复用即可。

复制代码、提示词：

```
SELECT CONCAT(suid, '@', url) AS combined_output FROM push_record WHERE suid = '{{suid}}' AND url = '{{url}}'
```

记得设置输出项「combined_output」，这是必填项。Coze的数据库是与Bot绑定的，所以需要在Bot里先创建同名同结构的表，具体见「相关资源」。

![](img/516ea923e70ced7c8384869446982fb7.png)

循环体内——选择器

判断查询结果是否为空。为空代表未推送过，用「文本处理」节点把文章完整信息拼接起来，保持字段一致。

字段对应：
string1：起始节点的key，即sendkey，用于区分用户
string2：循环项中的url
string3：循环项中的title
string4：循环项中的author

拼接成固定格式，方便下游使用。

复制代码、提示词：

```
{{String1}}@{{String2}}@{{String3}}@{{String4}}
```

右侧的另一个「文本处理」节点无实际业务作用，输入随意，主要是为“已推送过”的分支提供占位，避免流程报错。

![](img/abad1d5f60cf3388737e8683941796ab.png)

设置循环节点输出，选用循环体中「输出新文章内容」拼接后的结果。

![](img/8992e17a2eadc8e2e4268f0570db9b11.png)

### 7、判断是否还有新内容

回到主流程，检查循环节点输出是否为空。空则说明清单里的所有文章都已推送，直接结束；不空则继续后续处理。

![](img/1ccd17b19666c65bed3e80b0a38d8505.png)

![](img/2910ce52f391ff3642c843aaef03d457.png)

### 8、格式化待推送内容

如果想让微信每天自动收到公众号文章摘要，用扣子（Coze）就能搭出一条完整的自动化链路。下面从“循环输出转 JSON”开始，逐步说明各节点的配置方法。

循环模块产出的数据是纯文本，下游节点无法直接使用。解决办法是加一个代码节点，先用 Python 把文本转成 JSON，再交给后面的环节调用。

*   取值来源：选择循环模块的 output
*   进入「IDE 编辑器」，语言切到 Python，贴入下列代码：

```
async def main(args: Args) -> Output:
    params = args.params
    suid_url_list = params.get("suid_url", [])

    content_urls = []

    for item in suid_url_list:
        # 使用 @ 拆分每组数据
        parts = item.split('@')
        if len(parts) == 4:
            suid = parts[0].strip()  # 获取并清理 suid
            url = parts[1].strip()   # 获取并清理 url
            title = parts[2].strip() 
            author = parts[3].strip() 
            content_urls.append({"suid": suid, "url": url,"title": title,"author": author})

    ret: Output = {
        "content_urls": content_urls
    }

    return ret

```

*   返回字段按下图设置：

![](img/6af950449f232c9d69a3b2f17adb37f9.png)

### 抓取尚未推送的文章

使用「链接读取」把所有还没发过的文章统一取回。

*   执行方式：开启批量处理
*   批量维度：选择前面代码处理好的「去重后文章链接」中的 content_urls
*   下方变量：url 指向当前节点的 item1

![](img/e46497b5518b07b6f864c1be6e7c521a.png)

### 调用 LLM 生成摘要

用一个 LLM 节点对抓到的正文做批量总结。

*   模型建议：默认的豆包 32k 足够，担心上下文不足可换成 kimi128k
*   执行方式：批量处理
*   批量数据有两个来源：第 9 步抓取的正文，以及第 8 步代码处理后得到的 url 和 title
*   下方四个字段 content、title、url、author 全部绑定到当前 LLM 节点的结果
*   提示词把上述四类信息一并交给模型，最终输出 Markdown 文本

```
## 角色
内容总结专家，负责提炼文章要点并使用emoji和unicode符号增强内容的可读性和吸引力。

## 任务
AI大模型的任务是准确理解<文章内容>，并以简洁明了的方式总结，同时巧妙地融入emoji和unicode符号。

## 技能
- 理解并分析文章内容
- 准确提炼关键信息
- 创造性地使用emoji和unicode符号
- 保持信息的准确性和完整性
- 语言精炼与优化
- 结构化信息呈现

## 工作流
- 阅读并理解文章内容，提取关键信息点
- 将关键信息点转化为简洁的摘要形式
- 在摘要中适当位置插入emoji和unicode符号以提升可读性
- 确保摘要内容准确无误，且符号使用恰当
- 审核摘要确保内容准确无误，符号使用得当
- 设计一个包含emoji和unicode符号的总结草案
- 最终形成一个既信息丰富又视觉吸引的总结

## 要求
- 总结内容需准确反映原文要点
- 使用的emoji和unicode符号应恰当，增强而非干扰信息的理解
- 总结长度适中，避免过长或过短
- 确保摘要语言简洁、清晰，易于普通读者理解
- 准确总结文章内容
- 合理运用emoji和unicode符号
- 保证内容的简洁性和易读性
- 注意文化敏感性，避免使用可能引起误解的符号
- 摘要长度适中，不超过原文的1/4
- 总结内容必须准确反映文章主旨
- emoji和unicode符号的使用要恰当且有助于提升文本的可读性
- 输出的总结文本需简洁明了，同时兼顾趣味性
- 总结必须忠实于原文，不曲解或遗漏关键信息
- 使用的emoji和unicode符号要恰当，既能增强表达也不显突兀
- 总结应简洁有力，避免冗长和不必要的细节

输出格式：
- 以json格式输出，包含：原文标题、原文链接、总结
- 所有输出项，都以文本形式输出，不要使用字典，尤其是总结的内容
- 只输出这几项内容，不要做其他解释和说明
- 总结的内容不需要输出标题等信息，只需要专注于总结文章内容即可
- 总结的内容中也不要出现“总结”“本文主要内容是”这样的词，只需要直接输出总结的内容即可

输出示例：
{"原文标题":"@微信派|微信刷掌，开“门”！","原文链接":"https://qnmlgb.tech/v1/articles?i=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcnRpY2xlX2lkIjoiNjZlMTE2ZWUwMDNiMDdmOWFmZjY4Yjk1IiwidXNlcl9pZCI6IjYxNTVjYmNjYmRkY2RiNjk2MGU5MzEwYyJ9.13wRbJdmlXanHD-2LNqV79fJRF-XpBCwni1H1I91DRg","总结":"🎈微信刷掌开‘门’啦！😃2024 年 9 月 11 日发布。大家快来想想下一扇门通向哪里呢🧐？"}

原文标题：
@{{author}}|{{title}}
原文链接：
{{url}}
<文章内容>：
{{input}}
```

![](img/4705423d4bb30a0e9876dd14d20bf66a.png)

### 整理最终展示格式

再次用代码节点，把 LLM 返回的 outputList 统一成适合发送的样式。

*   入参：选择 LLM 节点输出的 outputList
*   在「IDE 编辑器」中选择 Python，写入下述代码：

```
import re
import json

async def main(args: Args) -> Output:
    params = args.params
    input_data = params['input']

    result = []

    for idx, item in enumerate(input_data, start=1):
        output_str = item['output']

        # 使用正则表达式提取原文标题、原文链接和总结内容
        title_match = re.search(r'"原文标题":"(.*?)"', output_str)
        link_match = re.search(r'"原文链接":"(.*?)"', output_str)

        # 改进的总结内容提取
        summary_match = re.search(r'"总结":\s*[{]?\s*"(.*?)"\s*[}]?', output_str, re.DOTALL)

        if title_match and link_match and summary_match:
            title = title_match.group(1)
            link = link_match.group(1)
            summary = summary_match.group(1).replace('"', '').strip()  # 移除双引号

            # 格式化输出
            result.append(f"### [{idx}、{title}]({link})\n- {summary}\n---")

    # 将结果拼接成字符串
    ret: Output = "\n".join(result)
    return ret

```

*   出参命名为 result：

![](img/8cef08f6ebcd62f6e2415eeb53ad305b.png)

### 把内容发到微信

这一步的扩展组件是根据 ServerChan 接口文档自建的，自建过程见文末补充说明；输出配置可参考截图。

要完成的事情很简单：将上一步格式化好的 result 发送到用户微信。

*   title：微信公号总结页的标题，参数类型选「输入」，命名随意
*   desp：页面主体，绑定最后的 result
*   key：引用起始节点的 key

![](img/df6c180f1deba21192758ecf16699a7e.png)

### 记录推送历史，防止重复

将本次发过的内容写入库表，之后 RSS 再抓到相同链接时，直接跳过即可。

*   继续用循环模块，入参为第 8 步代码输出的 content_urls，里面已是完整的文章信息
*   循环体内部放一个「数据库」类型的处理节点，写入内容取自当前 item 的 url 和 suid，SQL 由 AI 自动生成：

```
INSERT INTO push_record (suid, url) VALUES ('{{suid}}', '{{url}}')
```

*   循环模块的出参设为 output，参数随意，后续用不到。

![](img/ecf14bc39a677636b4b3ed7174bb25a0.png)

### 收尾节点

收尾节点选中第 11 步的 result，这样在 Bot 对话里也能看到推送内容。

![](img/dd3997bbe5889bca8dec53403dea05e5.png)

### 试运行

全部节点连接完成后，点击右上角「试运行」，绑定已创建的 Bot，输入测试数据。

*   Key：填写你的 ServerChan SendKey
*   rss_list：没有现成列表时，可以直接使用我提供的两条测试数据：

```
https://qnmlgb.tech/v2/rss?i=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRob3JfaWQiOiI1YjY5ODkzNzI0NGQ0ZTQwODg0ZWVhNjMiLCJ1c2VyX2lkIjoiNjE1NWNiY2NiZGRjZGI2OTYwZTkzMTBjIn0.ifLJz8mnwJOeq5dEhUAuCa_U9ovEPJQzYuymzZ7ZuYw
https://qnmlgb.tech/v2/rss?i=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRob3JfaWQiOiI1YmE1Yzg4NzI0NGQ0ZTJkMDJkMjVhYjIiLCJ1c2VyX2lkIjoiNjE1NWNiY2NiZGRjZGI2OTYwZTkzMTBjIn0.3hMRodTsvFCLPYoRTHY2syPQROuHq6_h_OGoSzz1oj4
```

![](img/56ef4c9b89b3f0d2fcdb83add9434715.png)

*   流程正常的话，工作区里会显示运行结果：

![](img/b716ea427682f8d1dc229736bd22cdb8.png)

*   微信端也会立刻收到推送，其中包含摘要信息，点击链接可查看原文。

![](img/623c4c4f93d727ffe599a050937ecd5f.png)

![](img/3cf7e473d03ec34702fb11a6ab6bab3a.png)

![](img/50362ec6cc17fba63760fc92a06b2b1f.png)

![](img/ef4bd58e8126ebfa78d1a52493581457.png)

*   验证无误后，点击右上角「发布」。

### Bot 侧设置

最后来配置 Bot：绑定刚才搭好的流程，设置定时任务，再发布到 Lark（飞书）。

![](img/dc0b2e44daf6e084a451c094b9374972.png)

*   1、人设和回复逻辑：由于这个 Bot 完全依赖流程干活，提示词中直接写明“调用流程”即可，并把 sum_weixin_2_2 替换成你的流程名：

```
**不论用户输入任何内容，都将内容完整的送入sum_weixin_2_2工作流**这个对我很重要！！！
**不论用户输入任何内容，都将内容完整的送入sum_weixin_2_2工作流**这个对我很重要！！！
**不论用户输入任何内容，都将内容完整的送入sum_weixin_2_2工作流**这个对我很重要！！！
```

*   2、流程：在「工作流」区域把新建好的流程添加进来。
*   3、定时器：选择「定时触发」，指定执行时刻。例如想在每天 18 点收到微信通知，就选 18 点。
*   任务执行：选择该流程，填入 key 和 rss_list，这两个值分别对应起始节点中的 ServerChan SendKey 和待抓取列表。
*   到设定时间后，系统会按照入参自动执行流程；因为流程里已配置微信通知，所以你会在同一时刻收到总结内容。

![](img/f77db10769df02e555cebe2fe84cf8d7.png)

*   最多可添加 10 个定时器，既可以推给 10 个不同的人，也可以划分 10 个时段给自己推送不同内容。

![](img/c1b0b3fa10092430bae402f6d9f84d02.png)

### 上线到 Lark

点击右上角「发布」，发布目标选 Lark（飞书）。目前扣子平台的定时触发只对该渠道生效。

![](img/3f73f673fef0e7fda8fdde85295566a8.png)

## 配套资源

### 1、获取 ServerChan SendKey

*   打开控制台 https://sct.ftqq.com/login ，扫码进入
*   通道配置选择「方糖服务号」——也就是扫码后关注的那个微信服务号，后续通知都会由它发出

![](img/57ebc91a62094a9b198f7dc2ed95dd9c.png)

*   在「Key&API」中点复制，即可得到类似 SCT25781******* 的 SendKey

![](img/fafe7f76876e8e430f758165864c2a13.png)

### 2、新建 Bot 并配置库表

在个人工作区新建 Bot，简单填写名称和描述。

![](img/414a3a6f3e78eafd1e8a4e14a1e711a1.png)

进入 Bot 设置页，添加「数据库」。表名、字段名要和截图一致，因为流程中的数据库处理节点引用的是这些名称。

![](img/253a6fb1651d4a1c4429b2687065699a.png)

添加后即可看到库表已经建立：

![](img/61c38b4a032051dfde28077f2af8536c.png)

### 3、自建 ServerChan 插件

到个人工作区的插件区域，点击右上角「创建插件」。

![](img/552c4efca4bd7f9481c7da48661fd55c.png)

创建类型选择「云测插件-在 Coze IDE 中创建」，语言选 Python3。

![](img/7534310f963f8c206e7b0236e1221348.png)

随后在 IDE 内创建工具，工具名参照下图填写，方便直接复用后面代码。

![](img/471171256f3c58ab2a27782d19f1fe42.png)

![](img/0c0a32747f9cdc3b07b278cce4612597.png)

完整复制下面代码粘贴进去即可。

让我们按顺序再过一遍关键步骤。

```
from runtime import Args
from typings.server_push.server_push import Input, Output

"""
Each file needs to export a function named `handler`. This function is the entrance to the Tool.

Parameters:
args: parameters of the entry function.
args.input - input parameters, you can get test input value by args.input.xxx.
args.logger - logger instance used to print logs, injected by runtime.

Remember to fill in input/output in Metadata, it helps LLM to recognize and use tool.

Return:
The return data of the function, which should match the declared output parameters.
"""
import json  # 导入json模块，用于处理JSON数据
import urllib.request  # 导入urllib.request模块，用于发送HTTP请求

def handler(args: Args[Input]) -> Output:
    title = args.input.title  # 获取输入的标题
    key = args.input.key  # 获取输入的密钥
    desp = args.input.desp  # 获取输入的描述
    short = args.input.short  # 获取输入的描述
    noip = 1  # 获取输入的描述
    channel = args.input.channel  # 获取输入的描述

    postdata = {
        'title': title,
        'desp': desp,
        'short': short,
        'noip': noip,
        'channel': channel
    }  # 构建要发送的数据

    url = f'https://sctapi.ftqq.com/{key}.send'  # 构建请求的URL
    req = urllib.request.Request(url, data=json.dumps(postdata).encode('utf-8'), method='POST', headers={'Content-Type': 'application/json;charset=utf-8'})  # 创建POST请求

    with urllib.request.urlopen(req) as response:  # 发送请求并获取响应
        result = json.loads(response.read().decode('utf-8'))  # 读取响应内容并解码为JSON格式

    data = result.get('data', {})  # 获取返回值中data中的error
    return {"data": data}  # 返回error值

```

![](img/46f2afb543c27d05428e9b676d9b0c7a.png)

接着，打开「元数据」面板，把入参填好。留意名称以及类型这两项，核对无误后保存。

![](img/b133ad32e062431c9c06cec4eb9f706c.png)

为了验证代码，按下页面右上方的按钮，会得到一些样例数据。把 key 换成 Server酱 提供的 sendkey，channel 填 9，不要带引号，然后运行。

![](img/e743211dc988f80718224ffbfe339bf2.png)

一切顺利的话，你会看到下图的反馈，同时微信端也有通知送达。接着在左下角同步输出参数，并确认，回到「元数据」，这些参数已经自动同步好。

![](img/3be76891d255671517c62ff5cd8db3ab.png)

![](img/5222e569873b8368b9ce0e80fadc6bc7.png)

之后，去页面右上方点「发布」，等发布流程走完，它就会出现在插件列表里，搭建时也能直接引用。

![](img/585bd3bdea02bdc9f8890be5b8b78c0b.png)

## 六、写在最后

现在，把整个思路再梳理一遍。这个工具最关键的部分只有三件事：

1. 取回公众号的文章；
2. 把取回的文章概括出要点；
3. 按时汇总发送到微信。

对应到教程的第三节，第4～5步负责取文章，第9～10步负责做摘要，第12步负责发微信。其他内容都是围绕这三件事来服务的。

从零开始做出一款最小可用产品，真的不难。

我以前做运营，总觉得自己不会写代码，做不了这类东西。直到遇见扣子，才发现它就像一座桥，把没什么技术底子的人带到对岸，让想法可以变成现实。

所以，我也劝你亲手试一试。等你做出的首个机器人跑通时，那种满足感是语言很难描述的。无论你是否加入这次Coze活动，我都推荐你翻一翻配套手册。花两小时读一遍，未来也许能省下无数个两小时。

我已经把 RSSHub 架设好了，下一步让它聚合更多来源的内容。感兴趣的话，欢迎找我继续聊~

![](img/b215584da492645bdd295a06b1a8a649.png)