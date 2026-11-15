# n8n实战：打造AI一键排版，公众号美化全自动
上一期我带大家搭好了AI写稿并自动推送到公众号的整套流，现在内容能出稿了，但都是裸文本，样式全无，看起来很糙。
这一期我们来补齐最后一块短板：用n8n做一个AI自动排版的子工作流。讲清楚了之后，这个排版模块既可以独立跑，也可以无缝挂到上期的生成发布流程后面一起用。两套叠加，写作+排版+发布全流程闭环。
实操完你能掌握这几个n8n核心技巧：
1、子工作流的封装与调用方式
2、IF分支的判断与流转逻辑
3、不同分支数据的合并技巧
# 开始搭建
## 1、子工作流触发节点
第一步先建一个可被复用的子工作流。新建画布后，在节点搜索栏输入 “sub” 找到 Execute Sub-workflow 节点并拖入。
![](img/zhuanqian_01c23e55831c17ab0c005ee63ec73f1f.png)
点进去后把触发器加进来。
![](img/zhuanqian_fa1c5bc3cff3c4982ca03ac032768954.png)
这个节点的作用是什么？
它是子工作流的入口。子工作流是把常用功能独立封装起来，多个主流程可以共用，避免重复造轮子。子工作流必须以这个触发器开头，用来接收来自父流程的参数。父流程则通过 Execute A Sub workflow 节点来调用它，后面会演示。
![](img/zhuanqian_82fc65e12415e9bf998ab251e1f1e902.png)
接下来给触发器定义入参。双击节点，点击 Add field，添加我们需要的字段，比如：
content：需要做排版的正文内容
url：作为排版参考的公众号文章链接
![](img/zhuanqian_5e1c868aec9a327f742182a08e47bd47.png)
## 2、获取参考HTML
拿到入参后，要先拿到排版参考的HTML。为了让流程更健壮，我设计成：url为空或抓取失败时就回退到一份默认模板，后续还能把模板换成不同风格，相当于一套排版皮肤库。
所以先加一个 IF 节点。
![](img/zhuanqian_ce9f435cf81ccb20d5aa42659abaa3fc.png)
判断逻辑是 url 是否为空，为空走默认模板分支，不为空就去抓取目标文章的HTML。
![](img/zhuanqian_cf2ca2d0bc4cc3cda44b97a8e2c57384.png)
在 url 为空的分支上加一个 Set 节点，节点类型搜 “set” 即可。现在的画布结构大致如下。
![](img/zhuanqian_b5bdc5a8e15b7505ba178c6494859144.png)
先准备默认参考代码。很多人问代码从哪来，很简单：找一个公众号排版编辑器，比如96编辑器这类工具，打开任意一套免费模板，点击 “微信复制” 复制到自己的公众号编辑器。
![](img/zhuanqian_8f80e5c55e5a7bfb72d9c145adc00d8a.png)
在公众号编辑页面按 F12 或右键审查元素，找到文章主体区域的HTML，用鼠标框选整篇文章后右键复制元素。我们要的就是这段结构代码。
![](img/zhuanqian_1f830cf935133bced53edc44455c536d.png)
把这段代码填到 Set 节点里，作为默认排版模板。
![](img/zhuanqian_caff23ba532e6c488e3fffa92f72744d.png)
如果 url 不为空，就需要调用接口去抓取指定文章的HTML。我用的是 https://auto.kanglan.vip/ 这个服务，先注册账号，进入个人资料获取 token。
![](img/zhuanqian_5d11e99eb84ec1c0cd616de739e6bd67.png)
复制下面这段 curl，注意把 {token} 换成自己的 token。
```
curl --request POST \
--url https://auto.kanglan.vip/cozeapi/html/getHtmlBySelector \
--header 'Accept: */*' \
--header 'Accept-Encoding: gzip, deflate, br' \
--header 'Connection: keep-alive' \
--header 'User-Agent: PostmanRuntime-ApipostRuntime/1.1.0' \
--data 'url=你的url' \
--data 'selector=#js_content' \
--data 'token={token}'
```
在 url 不为空的分支上新增一个 HTTP Request 节点，调用刚才的接口。
![](img/zhuanqian_ef37766b0b43f4d8e0a6c82425d3a6ae.png)
进入节点设置，选择 Curl 导入，把上面的代码粘贴后导入，记得先替换 token。
![](img/zhuanqian_a86d8339de5a4ba0b59f7f373fac16c3.png)
把上游传来的 url 变量填进请求参数里。这里有个小坑：子工作流触发器默认没有测试数据，导致分支拿不到参数。
![](img/zhuanqian_534638d7c5f4fae510ae2dd66d66d0f8.png)
为了方便调试，我们先给触发器固定一组测试数据。双击触发器，点击固定输出按钮。
![](img/zhuanqian_bac10a286fc2191fa43b8e9a61366cc0.png)
填入一组假数据，保存。
![](img/zhuanqian_33966af3fcbab84531a6b53ceea730eb.png)
回到画布执行一次工作流，重新拉取数据。注意不要单独执行触发器节点，否则会把固定数据清空。
![](img/zhuanqian_cd8ce58df5aa385e70f270de1b60e931.png)
执行成功后能正常进入 HTTP 请求分支，接着把 url 正确映射给接口。
![](img/zhuanqian_37aecdd9bc020f9fb47f3fdb1f3fc120.png)
点 “执行步骤” 看到返回成功，说明节点配置没问题。
![](img/zhuanqian_a59f63078ef7562a277efa427f0ac340.png)
## 3、合并HTML结果
现在有两个分支的输出，一个是抓取到的HTML，一个是默认模板。我们需要合并成一个统一的 html 字段供后面AI使用。继续用 Set 节点把两个分支汇聚。
![](img/zhuanqian_c483aba3239971f8a4de4e19a4d8f92b.png)
和之前一样，先给触发器设置两种测试场景：url 为空和 url 不为空，分别拖入对应的 html 字段。
![](img/zhuanqian_0b2bb03d2530a888cf784b635a8eb9a8.png)
画布上现在有两路数据：$json.data.html 是接口返回的，$json.html 是默认模板返回的。用下面这个表达式做 fallback，哪个有值就用哪个。
```
{{  $json?.data?.html || $json?.html }}
```
## 4、接入大模型做排版
参考HTML准备好后，就能让AI来排版了。搜索 Agent 节点加入画布。
![](img/zhuanqian_0e3297029e6fa2762ff8306d40933038.png)
Agent 节点需要搭配模型节点使用，再搜索 “open router” 加在 Agent 下方。
![](img/zhuanqian_74669a584e64a90056cad007f0bbf8d0.png)
OpenRouter 节点用于调用 OpenRouter 平台的大模型接口，可以免费试用国内外多个模型。
## 5、申请 OpenRouter API Key
打开 https://openrouter.ai/ 注册登录后，找到 API Key 管理区。
![](img/zhuanqian_5ef8b53e250499552c5596a46ca4df94.png)
点击 “创建API key”。
![](img/zhuanqian_1bca2a46a307fd91d4999c2fe6e3c118.png)
创建成功后立即复制保存，只显示一次，丢了只能重新创建。
![](img/zhuanqian_160ff73f327ac6665e83520b8f1b2429.png)
## 6、配置 OpenRouter 节点
回到 n8n，双击 OpenRouter 节点，需要先创建凭证。
![](img/zhuanqian_d31cd8968368967a830c29a0c4f55a05.png)
凭证里只需要填入 API KEY，保存即可。
![](img/zhuanqian_55485bc82da3b515146a6d24ba29f334.png)
返回节点配置，选择刚创建的凭证，Model 栏可搜索模型。我这里搜 “free” 用免费模型，生产环境建议用付费模型，免费的有限流，1分钟一次。
![](img/zhuanqian_b1bd263be70acb6e4711db5bfa7c1269.png)
## 7、设置模型提示词
进入 Agent 节点，把 User Prompt 来源设为 Define below，再添加 System Prompt 选项。
![](img/zhuanqian_554020e7bb5c12144ab07996b9e99b5e.png)
把系统提示词和用户提示词填入。系统提示词比较长，我已放到公众号，关键词 “AI排版提示词” 自取。填入后记得把占位符替换成需要排版的内容和参考 html。
![](img/zhuanqian_8db65768d96bb0f591781c59ac15fda3.png)
全部节点就绪后整体执行一次，能生成排版后的代码。
![](img/zhuanqian_c69474b7ffa4a7ce8f4e0d7f41050817.png)
实测发现模型输出有点乱，HTML不干净，不利于直接使用。再加一个格式化输出。
在 Agent 节点打开输出格式化开关。
![](img/zhuanqian_1f95a3d8a1fb5ba5ec3885fd9d771ec4.png)
在产生的分支上加一个格式化节点。
![](img/zhuanqian_eac3f05e87d22e4ccda99c468ef081f1.png)
按示例给大模型一个干净的输出范式。
![](img/zhuanqian_e1255e49d820cbf33be6afa4dd48db65.png)
再次执行，输出就很干净了，后续直接取 html 字段就能用。
![](img/zhuanqian_6c49105abbc476f59f2cf19886de58ce.png)
## 8、挂到之前的生成发布流程
如果你已经有上期的自动生成并发布工作流，现在只要在生成内容节点后面接入这个排版子工作流即可。
在大模型生成节点后点击添加。
![](img/zhuanqian_22789b875cc7e3fed4588ed53e7e9f08.png)
加入 Execute A Sub workflow 节点。
![](img/zhuanqian_7a672d3530274b7dad9dacfa87c3d4e6.png)
双击节点，选择刚建好的排版子工作流，并把上游生成的内容传入。
![](img/zhuanqian_18e6e1336df911e96c5fb03e064703d9.png)
最后修改 “添加草稿” 节点，把内容源换成排版子工作流的输出。
![](img/zhuanqian_661ce4b94f55c2221a8b62b3509024df.png)
节点改完后重新跑一遍全流程，检查公众号里是否已经是一篇排版完整的文章了。排版效果有波动，取决于参考模板的稳定性，多试几套模板，挑最稳定的那一套固定下来用。
![](img/zhuanqian_6f11308423cce792531e8a09ae145e3e.png)
附件：