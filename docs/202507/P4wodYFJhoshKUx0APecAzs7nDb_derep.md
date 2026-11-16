# 一键搬运对标号！用 Coze + 飞书多维表格自动抓取📕作者和笔记全数据



大家好，我是龙哥，这次分享的是我正在深耕的 AI 效率提升与私域获客方向的第 3 篇实战笔记：《AI 工作流实战 | Coze 联动飞书多维表格，批量采集📕博主账号与笔记数据》。

只要做过运营，就明白拆解标杆账号的价值。站在前人的肩膀上借力，省去大量试错成本。

可问题是，盯着一个对标主页刷笔记，刷着刷着前面看过的就忘了。想手动保存下来，又得一篇篇复制粘贴，手指都快僵了，找起来一样抓瞎。

这篇教程就是来帮你卸重的。跟着做就能实现：只输入📕作者主页地址，账号画像和全部笔记信息自动同步进飞书多维表格。之后做选题拆解、内容框架提炼、表达方式复盘、互动玩法模仿乃至仿写，都能在表格里一站式完成。省下来的时间，摸鱼打游戏都行~

整体运行逻辑如下：

![](img/d0b9a0e0d244ea048ebf77ff68c472d8.png)

运行效果展示：

账号信息结果：

![](img/22c456e2189690eb299c0fc987f9cf63.png)

笔记信息结果：

![](img/98697e46e63b694b6cce98c2ca6cb3a4.png)

内容分为四个模块：

1.  思路拆解
2.  操作详解
3.  源码与使用说明，想直接用的直接跳这里
4.  复盘总结

## 1 思路拆解

1.  先在飞书多维表格里建两张表，一张存博主主页信息，一张存笔记详情
2.  准备好📕作者主页链接、📕 Cookie、飞书两张表的链接
3.  用代码把抓取到的结果处理成表格可写入的格式
4.  抓取📕作者主页资料，写入飞书账号表
5.  抓取该作者全部笔记资料，写入飞书笔记表

## 2 实操步骤

### 2.1 新建飞书多维表格

1、打开飞书官网=》新建=》多维表格=》新建空白表格

![](img/603f9847f5499596a147958d88a500a6.png)

![](img/fa08211cb1f946a5ee02e46b50c0a723.png)

2、通过右键新建数据表即可。表名可直接修改。

![](img/e82c41dc07fa626ffb720ac39742e6a1.png)

3、本次用到两张表，“账号数据”记录博主信息，“笔记数据”记录每条笔记信息。

![](img/8fef9b91874d007e849f5fb97fb9bd28.png)

4、“账号数据”表：选中后右键删除多余列

![](img/d7e47cb0937ece5abd6bc4d352b1aada.png)

5、修改列名。鼠标右键选择“编辑字段和列”。第一行按以下顺序设置，注意字段名称要与后续代码完全一致，否则无法写入。数据类型都选文本。

![](img/84feab24bd6901df97d47e1a82c3fe22.png)

![](img/4ff8fa410361e08b2fb37668aaf62897.png)

6、点左上角全选，删除已有记录，方便从第一行开始写入。

![](img/417612fe712b13426ad9d199c3cd1b9a.png)

7、设置表格权限：

![](img/c7c11b4449767fc23f7926f6e75a5853.png)

8、复制出来的链接即为后续开始节点要用到的 FeishuToken

![](img/63623dc8882a14a21eb59c25cb9b3a85.png)

9、“笔记数据”表的字段设置如下，绿色框内为文本类型，黄色框为链接转附件类型，可将链接转成图片展示，搜索框里直接找即可：

![](img/58851ac5fab03c0005710e8ace6dbc61.png)

![](img/f8437aef699862d1de7f81cb0f192b32.png)

![](img/cae2a8a22c85e7cf0a4fc9f8b6e9b779.png)

![](img/b656701027af5d5d7a940189c8f156ab.png)

![](img/2a9bc387d6f3fef5fa44aea00c736b1f.png)

### 2.2 新建工作流

登录 Coze 官网=》开发平台=》快速开始=》左侧工作空间=》资源库=》右上角 + 资源=》工作流=》填写名称和描述

![](img/419a684c2fba08601ec85e2c44fe962c.png)

![](img/8e9f0679c228b6b5073267e12f8bf8fb.png)

这里我把工作流命名为：XHSAuthCrawlerCookie

描述填为：

:::warning

输入📕作者主页链接、📕 Cookie、飞书多维表格链接，批量抓取博主笔记数据

:::

![](img/14f4cdd9e372803e0592ce753b1a4b8d.png)

### 2.3 节点如何添加

1、添加节点=》插件

![](img/72678358e6c95ae5e9b6cf3d1dbf204c.png)

2、搜索插件名称，通常会得到一个合集。以📕插件合集为例：

![](img/ce3fd4cdc6ff664489d9a23715fe0477.png)

3、收藏后点击添加节点，后续就能直接调用，无需重复搜索

![](img/cfedf399c2993ad91dc9adad9a5351e7.png)

![](img/3c689b55537f55a859c63c59211c2fc7.png)

### 2.4 开始节点配置

设置如下：

![](img/ad394ad24a2a7c6379c46aec8bc681eb.png)

1.  RedBookAuthUrl：📕作者主页地址
2.  RedBookCookie：📕 Cookie
3.  FeishuAccountToken：飞书“账号数据”表 token
4.  FeishuNoteToken：飞书“笔记数据”表 token

### 2.5 📕作者数据抓取插件配置

设置如下：

![](img/59f249f2dd7edf7f14893201cf3ee93c.png)

1、cookieStr：

![](img/4e181b75879a2dba09c869441acfe0f0.png)

2、userProfileUrl

![](img/7725f44cf66c555849e755c10bb69903.png)

### 2.6 代码节点配置

设置如下：

![](img/ee0eb00e3a724442b1424e0bc513dcb9.png)

输入：input

![](img/eddae84ec863a2e5824621cee9fdcfb1.png)

输出：info

![](img/69338506242f8f36298309c0cd9bafb4.png)

代码如下：切换到 python

![](img/ed9a57177ab295e8dc379aac567b6b0a.png)

```
async def main(args: Args) -> Output:
    params = args.params
    params = params['input']

    # 构建输出对象
    records = []

    fields = {
        "博主昵称": params["nick_name"],
        "头像链接": params["avatar"],
        "简介": params["desc"],
        "粉丝数": params["fans"],
        "关注数": params["follows"],
        "赞藏数": params["interaction"],
        "IP地址": params["ip_location"],
        "博主id": params["red_id"],
        "主页链接": params["user_link_url"]
    }

    # 将 fields 转换为 JSON 格式的字符串
    record = {"fields": json.dumps(fields, ensure_ascii=False)}
    records.append(record)

    # 构建最终返回的输出对象
    ret = {
        "info": records
    }

    return ret
```

### 2.7 多维表格添加数据节点

添加插件：

![](img/c11487949412e07f36542f48e86b9c0d.png)

设置如下：

![](img/1bb87aae5aacb3315b06ad047487e06e.png)

1、app_token

![](img/0f1235e134fdc8f8247d18a3ee523309.png)

2、records

![](img/2107fa7ea8061e4935c511170c396c6c.png)

### 2.8 循环节点配置

设置如下：

![](img/9aa588a5bfd334c2dcb8487251263c32.png)

1、循环模式：数组循环
2、循环数组：input

![](img/5efd9bd62f3989747b7b38754ba814c4.png)

3、输出变量：output

![](img/3510d74faadf305b6a7b4547cc7ae064.png)

#### 2.8.1 📕笔记抓取插件

设置如下：

![](img/78ec8fef174b9ef8b433219c099a7b81.png)

1、cookieStr

![](img/3c5e2294870d54e33a653b79097b638d.png)

2、noteUrl

![](img/1211382a02863495a2569f8e696b6041.png)

#### 2.8.2 代码节点 1

设置如下：

![](img/7c0d723421bb5bc7033d9d28a2784e05.png)

输入：input

![](img/da178f4410923bdc4fc43105756a0d76.png)

输出：info

![](img/d781f1e3437dfdb94bab37ceecc5c90e.png)

代码如下：python

```
async def main(args: Args) -> Output:
    params = args.params
    params = params["input"]
    # 构建输出对象
    records = []

    fields = {
            "标题": params["note_display_title"],
            "创建时间": params["note_create_time"],
            "封面图片链接": params["note_image_list"][0],
            "博主昵称": params["auther_nick_name"],
            "文案": params["note_desc"],
            "标签": "||".join(params["note_tags"]),
            "类型": params["note_card_type"],
            "收藏数": int(params["collected_count"]),
            "点赞数": int(params["note_liked_count"]),
            "分享数": int(params["share_count"]),
            "评论数": int(params["comment_count"]),
            "视频链接": params["video_h264_url"],
            "笔记链接": params["note_url"],
            "图片列表": "||".join(params["note_image_list"])
        }

    # 将 fields 转换为 JSON 格式的字符串
    record = {"fields": json.dumps(fields, ensure_ascii=False)}
    records.append(record)

    # 构建最终返回的输出对象
    ret = {
        "info": records
    }

    return ret
```

#### 2.8.3 多维表格添加数据节点

设置如下：

![](img/f7e38dcbc3d3a956fd6d20fea97c6d4f.png)

1、app_token

![](img/b4bf687eb58e7b9b907d64074423fde9.png)

2、records

![](img/c522aba20529cdf5de1872b8ca51cd99.png)

### 2.9 结束节点配置

设置如下：

![](img/fe74092b72bcd405784ce038445feb52.png)

output：

![](img/2f58ed85add83dfaf0aa52e190b2f46a.png)

### 2.10 📕 Cookie 获取方式

![](img/132b6d337cc53a4685a8aeb7cf31735e.png)

2、随便找个内容搜索一下

![](img/22053823a27c63a65121e5c655292aab.png)

3、鼠标右键点检查，或直接按 F12

![](img/3b8bb3859c9265b9690a02c7a58504f1.png)

4、切换到 Network

![](img/5aef0295308eba9cbeb3627b971fef83.png)

5、在左侧找📕瀑布流笔记区域，一直往下滚，名称会出现 notes，点击后在 Headers 里找到 cookie 直接复制

4、unread_count 也可以用

![](img/c61b09eba13c7733d8816fee6a3d75f5.png)

注意：Cookie 会过期，失效了就重新抓取一次。

### 2.11 测试运行

1、点击“试运行”

![](img/9f24410baf48534f83ff82220618fbcd.png)

2、FeishuAccountToken

![](img/97465c732fcce345906ce6bfe6e9fcd7.png)

3、FeishuNoteToken

![](img/dae983e09133bc9281e88d3a562326ee.png)

4、RedBookAuthUrl，填写作者主页链接

![](img/f56f7cb9c801c2271b8af0c8240bd494.png)

5、RedBookCookie

![](img/b801d6ecac4f5db8c3be87ce0648942e.png)

6、把开始节点的变量全部填好

![](img/38f270d35883e0a0918f7b43c54f39f8.png)

## 3 源码与使用教程

### 3.1 源码

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
{"type":"coze-workflow-clipboard-data","source":{"workflowId":"7518229660888350760","flowMode":0,"spaceId":"7510842919100809242","isDouyin":false,"host":"www.coze.cn"},"json":{"nodes":[{"id":"177157","type":"4","meta":{"position":{"x":640,"y":13}},"data":{"nodeMeta":{"description":"‌获取用户【笔记列表】（xhs_auther_notes）‌\n‌功能描述‌： 根据提供的用户首页地址链接和📕cookie，抓取该用户的所有笔记列表。\n‌参数‌：\ncookieStr：📕的cookie字符串，用于身份验证。\nuserProfileUrl：用户首页的地址链接。\n","icon":"https://p26-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/b1898b6505b7472993ae37794313f9e7~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753068274&x-signature=6d%2B4%2Fu6fA8cHjXLPLRduAj8ZVOc%3D","subtitle":"📕:xhs_auther_notes","title":"xhs_auther_notes"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7425907757733330994","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"xhs_auther_notes","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7413268723496190002","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"📕","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"}],"inputParameters":[{"name":"cookieStr","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"RedBookCookie"},"rawMeta":{"type":1}}}},{"name":"userProfileUrl","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"RedBookAuthUrl"},"rawMeta":{"type":1}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"integer","name":"code","required":false},{"type":"object","name":"data","schema":[{"type":"string","name":"cursor","required":true},{"type":"boolean","name":"has_more","required":true},{"type":"list","name":"notes","schema":{"type":"object","schema":[{"type":"string","name":"auther_nick_name","required":false},{"type":"string","name":"note_cover_width","required":false},{"type":"string","name":"note_url","required":false},{"type":"string","name":"note_xsec_token","required":false},{"type":"string","name":"auther_avatar","required":false},{"type":"string","name":"auther_user_id","required":false},{"type":"string","name":"note_cover_url_pre","required":false},{"type":"string","name":"note_id","required":false},{"type":"string","name":"auther_home_page_url","required":false},{"type":"string","name":"note_display_title","required":false},{"type":"string","name":"note_liked_count","required":false},{"type":"boolean","name":"note_sticky","required":true},{"type":"string","name":"note_card_type","required":false},{"type":"string","name":"note_cover_height","required":false},{"type":"string","name":"note_cover_url_default","required":false},{"type":"boolean","name":"note_liked","required":false}]},"required":false},{"type":"object","name":"auther_info","schema":[{"type":"string","name":"gender","required":false},{"type":"string","name":"interaction","required":false},{"type":"string","name":"ip_location","required":false},{"type":"string","name":"nick_name","required":false},{"type":"string","name":"red_id","required":false},{"type":"string","name":"avatar","required":false},{"type":"string","name":"fans","required":false},{"type":"string","name":"follows","required":false},{"type":"string","name":"user_link_url","required":false},{"type":"string","name":"desc","required":false},{"type":"list","name":"tags","schema":{"type":"string"},"required":false},{"type":"string","name":"user_id","required":false}],"required":false}],"required":false},{"type":"string","name":"msg","required":false},{"type":"string","name":"tips","required":true}]},"_temp":{"bounds":{"x":460,"y":13,"width":360,"height":112},"externalData":{"icon":"https://lf6-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/517231610969187_1725264473893186047_CDXXehfYsy.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=lDH6TRceUKnCA3RPRubURsLPU5E%3D","apiName":"xhs_auther_notes","pluginID":"7413268723496190002","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7402935100184313883","inputs":[{"description":"📕 cookie","input":{},"name":"cookieStr","required":true,"type":"string"},{"description":"数据游标","input":{},"name":"cursor","required":false,"type":"string"},{"description":"用户首页地址链接","input":{},"name":"userProfileUrl","required":true,"type":"string"}],"outputs":[{"input":{},"name":"code","required":false,"type":"integer"},{"input":{},"name":"data","required":false,"schema":[{"input":{},"name":"notes","required":false,"schema":{"schema":[{"input":{},"name":"auther_avatar","required":false,"type":"string"},{"input":{},"name":"note_cover_url_default","required":false,"type":"string"},{"input":{},"name":"note_cover_url_pre","required":false,"type":"string"},{"input":{},"name":"note_cover_width","required":false,"type":"string"},{"input":{},"name":"note_display_title","required":false,"type":"string"},{"input":{},"name":"note_xsec_token","required":false,"type":"string"},{"input":{},"name":"auther_user_id","required":false,"type":"string"},{"input":{},"name":"note_card_type","required":false,"type":"string"},{"input":{},"name":"note_cover_height","required":false,"type":"string"},{"input":{},"name":"note_liked","required":false,"type":"boolean"},{"input":{},"name":"note_sticky","required":true,"type":"boolean"},{"input":{},"name":"note_url","required":false,"type":"string"},{"input":{},"name":"auther_home_page_url","required":false,"type":"string"},{"input":{},"name":"note_id","required":false,"type":"string"},{"input":{},"name":"note_liked_count","required":false,"type":"string"},{"input":{},"name":"auther_nick_name","required":false,"type":"string"}],"type":"object"},"type":"list"},{"input":{},"name":"auther_info","required":false,"schema":[{"input":{},"name":"gender","required":false,"type":"string"},{"input":{},"name":"tags","required":false,"schema":{"assistType":0,"type":"string"},"type":"list"},{"input":{},"name":"user_id","required":false,"type":"string"},{"input":{},"name":"user_link_url","required":false,"type":"string"},{"input":{},"name":"ip_location","required":false,"type":"string"},{"input":{},"name":"nick_name","required":false,"type":"string"},{"input":{},"name":"red_id","required":false,"type":"string"},{"input":{},"name":"avatar","required":false,"type":"string"},{"input":{},"name":"desc","required":false,"type":"string"},{"input":{},"name":"fans","required":false,"type":"string"},{"input":{},"name":"follows","required":false,"type":"string"},{"input":{},"name":"interaction","required":false,"type":"string"}],"type":"object"},{"input":{},"name":"cursor","required":true,"type":"string"},{"input":{},"name":"has_more","required":true,"type":"boolean"}],"type":"object"},{"input":{},"name":"msg","required":false,"type":"string"},{"input":{},"name":"tips","required":true,"type":"string"}],"updateTime":1752558364,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"‌获取用户【笔记列表】（xhs_auther_notes）‌\n‌功能描述‌： 根据提供的用户首页地址链接和📕cookie，抓取该用户的所有笔记列表。\n‌参数‌：\ncookieStr：📕的cookie字符串，用于身份验证。\nuserProfileUrl：用户首页的地址链接。\n","title":"xhs_auther_notes","mainColor":"#CA61FF"}}},{"id":"155154","type":"5","meta":{"position":{"x":1100,"y":13}},"data":{"nodeMeta":{"description":"编写代码，处理输入变量来生成返回值","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","mainColor":"#00B2B2","subTitle":"代码","title":"代码"},"inputs":{"inputParameters":[{"name":"input","input":{"type":"object","schema":[{"type":"string","name":"gender","required":false},{"type":"string","name":"interaction","required":false},{"type":"string","name":"ip_location","required":false},{"type":"string","name":"nick_name","required":false},{"type":"string","name":"red_id","required":false},{"type":"string","name":"avatar","required":false},{"type":"string","name":"fans","required":false},{"type":"string","name":"follows","required":false},{"type":"string","name":"user_link_url","required":false},{"type":"string","name":"desc","required":false},{"type":"list","name":"tags","schema":{"type":"string"},"required":false},{"type":"string","name":"user_id","required":false}],"value":{"type":"ref","content":{"source":"block-output","blockID":"177157","name":"data.auther_info"},"rawMeta":{"type":6}}}}],"code":"# 在这里，您可以通过 ‘args’  获取节点中的输入变量，并通过 'ret' 输出结果\n# 'args' 和 'ret' 已经被正确地注入到环境中\n# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为‘input’的值：\n# params = args.params; \n# input = params.input;\n# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：\n# ret: Output =  { \"name\": ‘小明’, \"hobbies\": [“看书”, “旅游”] };\n\nasync def main(args: Args) -> Output:\n    params = args.params\n    params = params['input']\n\n    # 构建输出对象\n    records = []\n\n    fields = {\n            \"博主昵称\": params[\"nick_name\"],\n            \"头像链接\": params[\"avatar\"],\n            \"简介\": params[\"desc\"],\n            \"粉丝数\": params[\"fans\"],\n            \"关注数\": params[\"follows\"],\n            \"赞藏数\": params[\"interaction\"],\n            \"IP地址\": params[\"ip_location\"],\n            \"博主id\": params[\"red_id\"],\n            \"主页链接\": params[\"user_link_url\"]\n        }\n\n    # 将 fields 转换为 JSON 格式的字符串\n    record = {\"fields\": json.dumps(fields, ensure_ascii=False)}\n    records.append(record)\n\n    # 构建最终返回的输出对象\n    ret = {\n        \"info\": records\n    }\n\n    return ret","language":3,"settingOnError":{"processType":1,"timeoutMs":60000,"retryTimes":0}},"outputs":[{"type":"list","name":"info","schema":{"type":"object","schema":[]}}]},"_temp":{"bounds":{"x":920,"y":13,"width":360,"height":112},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","description":"编写代码，处理输入变量来生成返回值","title":"代码","mainColor":"#00B2B2"}}},{"id":"161588","type":"4","meta":{"position":{"x":1560,"y":13}},"data":{"nodeMeta":{"description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","icon":"https://p6-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/dfc3d7f4eb004d0584aaf47a510beba2~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753069237&x-signature=Vp77knPs%2Bxpvy541HXnkdnxXj20%3D","subtitle":"飞书多维表格:add_records","title":"add_records_账号数据"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7395047759797288987","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"add_records","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7395047759797272603","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"飞书多维表格","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"},{"input":{"type":"integer","value":{"content":0,"type":"literal"}},"name":"pluginAuthMode"}],"inputParameters":[{"name":"app_token","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"FeishuAccountToken"},"rawMeta":{"type":1}}}},{"name":"records","input":{"type":"list","schema":{"type":"object","schema":[]},"value":{"type":"ref","content":{"source":"block-output","blockID":"155154","name":"info"},"rawMeta":{"type":103}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"float","name":"code","required":false,"description":"错误码，非 0 表示失败。"},{"type":"object","name":"data","schema":[{"type":"list","name":"records","schema":{"type":"object","schema":[{"type":"string","name":"fields","required":false,"description":"数据表的字段，即数据表的列，格式为 json 字符串。"},{"type":"string","name":"record_id","required":false,"description":"一条记录的唯一标识 id"}]},"required":false,"description":"本次请求新增的记录列表"}],"required":false,"description":"返回结果"},{"type":"string","name":"log_id","required":false,"description":"链路追踪 id"},{"type":"string","name":"msg","required":false,"description":"错误描述"}]},"_temp":{"bounds":{"x":1380,"y":13,"width":360,"height":112},"externalData":{"icon":"https://lf9-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/618387578815144_1720635554144262143_tbFVbqTqbp.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=kKr8JlRZVPPlIqTty2FdGqqx4bA%3D","apiName":"add_records","pluginID":"7395047759797272603","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7315016311652941851","inputs":[{"description":"多维表格数据表的唯一标识符","input":{},"name":"table_id","required":false,"type":"string"},{"description":"多维表格数据表的名称","input":{},"name":"table_name","required":false,"type":"string"},{"defaultValue":"open_id","description":"用户 ID 类型，可选值有 open_id、union_id、user_id，默认值为 open_id。, default value is open_id","input":{},"name":"user_id_type","required":false,"type":"string"},{"description":"多维表格的唯一标识符，支持输入文档 url。","input":{},"name":"app_token","required":true,"type":"string"},{"description":"本次请求将要新增的记录列表，格式为：[{\"fields\":{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}}]","input":{},"name":"records","required":true,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。例如：{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}","input":{},"name":"fields","required":true,"type":"string"}],"type":"object"},"type":"list"}],"outputs":[{"description":"错误码，非 0 表示失败。","input":{},"name":"code","required":false,"type":"float"},{"description":"返回结果","input":{},"name":"data","required":false,"schema":[{"description":"本次请求新增的记录列表","input":{},"name":"records","required":false,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。","input":{},"name":"fields","required":false,"type":"string"},{"description":"一条记录的唯一标识 id","input":{},"name":"record_id","required":false,"type":"string"}],"type":"object"},"type":"list"}],"type":"object"},{"description":"链路追踪 id","input":{},"name":"log_id","required":false,"type":"string"},{"description":"错误描述","input":{},"name":"msg","required":false,"type":"string"}],"updateTime":1752558245,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","title":"add_records","mainColor":"#CA61FF"}}},{"id":"148068","type":"21","meta":{"position":{"x":2580,"y":0},"canvasPosition":{"x":1940,"y":318}},"data":{"inputs":{"inputParameters":[{"name":"input","input":{"type":"list","schema":{"type":"object","schema":[{"type":"string","name":"auther_nick_name","required":false},{"type":"string","name":"note_cover_width","required":false},{"type":"string","name":"note_url","required":false},{"type":"string","name":"note_xsec_token","required":false},{"type":"string","name":"auther_avatar","required":false},{"type":"string","name":"auther_user_id","required":false},{"type":"string","name":"note_cover_url_pre","required":false},{"type":"string","name":"note_id","required":false},{"type":"string","name":"auther_home_page_url","required":false},{"type":"string","name":"note_display_title","required":false},{"type":"string","name":"note_liked_count","required":false},{"type":"boolean","name":"note_sticky","required":true},{"type":"string","name":"note_card_type","required":false},{"type":"string","name":"note_cover_height","required":false},{"type":"string","name":"note_cover_url_default","required":false},{"type":"boolean","name":"note_liked","required":false}]},"value":{"type":"ref","content":{"source":"block-output","blockID":"177157","name":"data.notes"},"rawMeta":{"type":103}}}}],"loopCount":{"type":"integer","value":{"type":"literal","content":"10"}},"loopType":"array","variableParameters":[]},"nodeMeta":{"description":"用于通过设定循环次数和逻辑，重复执行一系列任务","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Loop-v2.jpg","mainColor":"#00B2B2","subTitle":"循环","title":"循环"},"outputs":[{"name":"output","input":{"type":"list","schema":{"type":"string"},"value":{"type":"ref","content":{"source":"block-output","blockID":"154375","name":"msg"},"rawMeta":{"type":1}}}}]},"blocks":[{"id":"103111","type":"4","meta":{"position":{"x":180,"y":0}},"data":{"nodeMeta":{"description":"‌根据笔记链接获取【笔记详情】（xhs_note_detail）‌‌\n功能描述‌： 根据提供的笔记URL和cookie，抓取该笔记的详细信息。\n‌参数‌：\nnoteUrl：笔记的URL地址。\ncookieStr：📕的cookie字符串，用于身份验证。\n","icon":"https://p3-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/b1898b6505b7472993ae37794313f9e7~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753070075&x-signature=kO%2FyYdX2y7GXvb6Y6Fg6NHIwEQw%3D","subtitle":"📕:xhs_note_detail","title":"xhs_note_detail"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7425907757733347378","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"xhs_note_detail","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7413268723496190002","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"📕","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"}],"inputParameters":[{"name":"cookieStr","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"RedBookCookie"},"rawMeta":{"type":1}}}},{"name":"noteUrl","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"148068","name":"input.note_url"},"rawMeta":{"type":1}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"integer","name":"code","required":false},{"type":"object","name":"data","schema":[{"type":"object","name":"note","schema":[{"type":"string","name":"note_id","required":true,"description":"笔记编号"},{"type":"string","name":"auther_home_page_url","required":true,"description":"作者主页链接"},{"type":"string","name":"note_create_time","required":true,"description":"笔记创建时间"},{"type":"string","name":"note_url","required":true,"description":"笔记链接"},{"type":"string","name":"video_h265_url","required":true},{"type":"string","name":"auther_nick_name","required":true,"description":"作者昵称"},{"type":"string","name":"note_display_title","required":true,"description":"笔记标题"},{"type":"string","name":"note_last_update_time","required":true,"description":"笔记最后更新时间"},{"type":"string","name":"share_count","required":true,"description":"分享数"},{"type":"string","name":"video_a1_url","required":true},{"type":"string","name":"video_h264_url","required":true},{"type":"string","name":"video_h266_url","required":true},{"type":"string","name":"video_id","required":true},{"type":"string","name":"auther_user_id","required":true,"description":"作者ID"},{"type":"boolean","name":"collected","required":true,"description":"是否收藏"},{"type":"string","name":"collected_count","required":true,"description":"收藏数"},{"type":"string","name":"note_card_type","required":true,"description":"笔记类型"},{"type":"string","name":"note_desc","required":true,"description":"笔记描述"},{"type":"string","name":"note_duration","required":true},{"type":"string","name":"note_liked_count","required":true,"description":"点赞数"},{"type":"list","name":"note_tags","schema":{"type":"string"},"required":true,"description":"笔记标签列表"},{"type":"string","name":"auther_avatar","required":true,"description":"作者头像"},{"type":"string","name":"comment_count","required":true,"description":"评论数"},{"type":"list","name":"note_image_list","schema":{"type":"string"},"required":true,"description":"笔记封面"},{"type":"boolean","name":"note_liked","required":true,"description":"是否点赞"},{"type":"string","name":"note_model_type","required":true,"description":"笔记模型类型"}],"required":false,"description":"笔记信息"}],"required":false},{"type":"string","name":"msg","required":true},{"type":"string","name":"tips","required":true}]},"_temp":{"bounds":{"x":1940,"y":318,"width":360,"height":112},"externalData":{"icon":"https://lf26-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/517231610969187_1725264473893186047_CDXXehfYsy.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=x%2BTgrZut%2Fs6I8U6oK7pKeEC%2B4%2BY%3D","apiName":"xhs_note_detail","pluginID":"7413268723496190002","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7402935100184313883","inputs":[{"description":"cookie","input":{},"name":"cookieStr","required":true,"type":"string"},{"description":" 笔记链接","input":{},"name":"noteUrl","required":true,"type":"string"}],"outputs":[{"input":{},"name":"code","required":false,"type":"integer"},{"input":{},"name":"data","required":false,"schema":[{"description":"笔记信息","input":{},"name":"note","required":false,"schema":[{"description":"评论数","input":{},"name":"comment_count","required":true,"type":"string"},{"description":"笔记描述","input":{},"name":"note_desc","required":true,"type":"string"},{"description":"笔记最后更新时间","input":{},"name":"note_last_update_time","required":true,"type":"string"},{"description":"点赞数","input":{},"name":"note_liked_count","required":true,"type":"string"},{"description":"笔记链接","input":{},"name":"note_url","required":true,"type":"string"},{"description":"作者头像","input":{},"name":"auther_avatar","required":true,"type":"string"},{"description":"作者昵称","input":{},"name":"auther_nick_name","required":true,"type":"string"},{"description":"作者ID","input":{},"name":"auther_user_id","required":true,"type":"string"},{"input":{},"name":"video_h264_url","required":true,"type":"string"},{"description":"笔记封面","input":{},"name":"note_image_list","required":true,"schema":{"assistType":0,"type":"string"},"type":"list"},{"description":"笔记模型类型","input":{},"name":"note_model_type","required":true,"type":"string"},{"description":"分享数","input":{},"name":"share_count","required":true,"type":"string"},{"description":"是否点赞","input":{},"name":"note_liked","required":true,"type":"boolean"},{"input":{},"name":"video_a1_url","required":true,"type":"string"},{"input":{},"name":"video_id","required":true,"type":"string"},{"description":"是否收藏","input":{},"name":"collected","required":true,"type":"boolean"},{"description":"笔记创建时间","input":{},"name":"note_create_time","required":true,"type":"string"},{"input":{},"name":"note_duration","required":true,"type":"string"},{"description":"笔记标题","input":{},"name":"note_display_title","required":true,"type":"string"},{"description":"笔记编号","input":{},"name":"note_id","required":true,"type":"string"},{"description":"笔记标签列表","input":{},"name":"note_tags","required":true,"schema":{"assistType":0,"type":"string"},"type":"list"},{"input":{},"name":"video_h265_url","required":true,"type":"string"},{"input":{},"name":"video_h266_url","required":true,"type":"string"},{"description":"作者主页链接","input":{},"name":"auther_home_page_url","required":true,"type":"string"},{"description":"收藏数","input":{},"name":"collected_count","required":true,"type":"string"},{"description":"笔记类型","input":{},"name":"note_card_type","required":true,"type":"string"}],"type":"object"}],"type":"object"},{"input":{},"name":"msg","required":true,"type":"string"},{"input":{},"name":"tips","required":true,"type":"string"}],"updateTime":1752558364,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"‌根据笔记链接获取【笔记详情】（xhs_note_detail）‌‌\n功能描述‌： 根据提供的笔记URL和cookie，抓取该笔记的详细信息。\n‌参数‌：\nnoteUrl：笔记的URL地址。\ncookieStr：📕的cookie字符串，用于身份验证。\n","title":"xhs_note_detail","mainColor":"#CA61FF"}}},{"id":"121886","type":"5","meta":{"position":{"x":640,"y":0}},"data":{"nodeMeta":{"description":"编写代码，处理输入变量来生成返回值","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","mainColor":"#00B2B2","subTitle":"代码","title":"代码_1"},"inputs":{"inputParameters":[{"name":"input","input":{"type":"object","schema":[{"type":"string","name":"note_id","required":true,"description":"笔记编号"},{"type":"string","name":"auther_home_page_url","required":true,"description":"作者主页链接"},{"type":"string","name":"note_create_time","required":true,"description":"笔记创建时间"},{"type":"string","name":"note_url","required":true,"description":"笔记链接"},{"type":"string","name":"video_h265_url","required":true},{"type":"string","name":"auther_nick_name","required":true,"description":"作者昵称"},{"type":"string","name":"note_display_title","required":true,"description":"笔记标题"},{"type":"string","name":"note_last_update_time","required":true,"description":"笔记最后更新时间"},{"type":"string","name":"share_count","required":true,"description":"分享数"},{"type":"string","name":"video_a1_url","required":true},{"type":"string","name":"video_h264_url","required":true},{"type":"string","name":"video_h266_url","required":true},{"type":"string","name":"video_id","required":true},{"type":"string","name":"auther_user_id","required":true,"description":"作者ID"},{"type":"boolean","name":"collected","required":true,"description":"是否收藏"},{"type":"string","name":"collected_count","required":true,"description":"收藏数"},{"type":"string","name":"note_card_type","required":true,"description":"笔记类型"},{"type":"string","name":"note_desc","required":true,"description":"笔记描述"},{"type":"string","name":"note_duration","required":true},{"type":"string","name":"note_liked_count","required":true,"description":"点赞数"},{"type":"list","name":"note_tags","schema":{"type":"string"},"required":true,"description":"笔记标签列表"},{"type":"string","name":"auther_avatar","required":true,"description":"作者头像"},{"type":"string","name":"comment_count","required":true,"description":"评论数"},{"type":"list","name":"note_image_list","schema":{"type":"string"},"required":true,"description":"笔记封面"},{"type":"boolean","name":"note_liked","required":true,"description":"是否点赞"},{"type":"string","name":"note_model_type","required":true,"description":"笔记模型类型"}],"value":{"type":"ref","content":{"source":"block-output","blockID":"103111","name":"data.note"},"rawMeta":{"type":6}}}}],"code":"# 在这里，您可以通过 ‘args’  获取节点中的输入变量，并通过 'ret' 输出结果\n# 'args' 和 'ret' 已经被正确地注入到环境中\n# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为‘input’的值：\n# params = args.params; \n# input = params.input;\n# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：\n# ret: Output =  { \"name\": ‘小明’, \"hobbies\": [“看书”, “旅游”] };\n\nasync def main(args: Args) -> Output:\n    params = args.params\n    params = params[\"input\"]\n    # 构建输出对象\n    records = []\n\n    fields = {\n            \"标题\": params[\"note_display_title\"],\n            \"创建时间\": params[\"note_create_time\"],\n            \"封面图片链接\": params[\"note_image_list\"][0],\n            \"博主昵称\": params[\"auther_nick_name\"],\n            \"文案\": params[\"note_desc\"],\n            \"标签\": \"||\".join(params[\"note_tags\"]),\n            \"类型\": params[\"note_card_type\"],\n            \"收藏数\": int(params[\"collected_count\"]),\n            \"点赞数\": int(params[\"note_liked_count\"]),\n            \"分享数\": int(params[\"share_count\"]),\n            \"评论数\": int(params[\"comment_count\"]),\n            \"视频链接\": params[\"video_h264_url\"],\n            \"笔记链接\": params[\"note_url\"],\n            \"图片列表\": \"||\".join(params[\"note_image_list\"])\n        }\n\n    # 将 fields 转换为 JSON 格式的字符串\n    record = {\"fields\": json.dumps(fields, ensure_ascii=False)}\n    records.append(record)\n\n    # 构建最终返回的输出对象\n    ret = {\n        \"info\": records\n    }\n\n    return ret","language":3,"settingOnError":{"processType":1,"timeoutMs":60000,"retryTimes":0}},"outputs":[{"type":"list","name":"info","schema":{"type":"object","schema":[]}}]},"_temp":{"bounds":{"x":2400,"y":318,"width":360,"height":112},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","description":"编写代码，处理输入变量来生成返回值","title":"代码","mainColor":"#00B2B2"}}},{"id":"154375","type":"4","meta":{"position":{"x":1100,"y":0}},"data":{"nodeMeta":{"description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","icon":"https://p6-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/dfc3d7f4eb004d0584aaf47a510beba2~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753069237&x-signature=Vp77knPs%2Bxpvy541HXnkdnxXj20%3D","subtitle":"飞书多维表格:add_records","title":"add_records"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7395047759797288987","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"add_records","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7395047759797272603","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"飞书多维表格","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"},{"input":{"type":"integer","value":{"content":0,"type":"literal"}},"name":"pluginAuthMode"}],"inputParameters":[{"name":"app_token","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"FeishuNoteToken"},"rawMeta":{"type":1}}}},{"name":"records","input":{"type":"list","schema":{"type":"object","schema":[]},"value":{"type":"ref","content":{"source":"block-output","blockID":"121886","name":"info"},"rawMeta":{"type":103}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"float","name":"code","required":false,"description":"错误码，非 0 表示失败。"},{"type":"object","name":"data","schema":[{"type":"list","name":"records","schema":{"type":"object","schema":[{"type":"string","name":"fields","required":false,"description":"数据表的字段，即数据表的列，格式为 json 字符串。"},{"type":"string","name":"record_id","required":false,"description":"一条记录的唯一标识 id"}]},"required":false,"description":"本次请求新增的记录列表"}],"required":false,"description":"返回结果"},{"type":"string","name":"log_id","required":false,"description":"链路追踪 id"},{"type":"string","name":"msg","required":false,"description":"错误描述"}]},"_temp":{"bounds":{"x":2860,"y":318,"width":360,"height":112},"externalData":{"icon":"https://lf9-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/618387578815144_1720635554144262143_tbFVbqTqbp.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=kKr8JlRZVPPlIqTty2FdGqqx4bA%3D","apiName":"add_records","pluginID":"7395047759797272603","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7315016311652941851","inputs":[{"description":"多维表格数据表的唯一标识符","input":{},"name":"table_id","required":false,"type":"string"},{"description":"多维表格数据表的名称","input":{},"name":"table_name","required":false,"type":"string"},{"defaultValue":"open_id","description":"用户 ID 类型，可选值有 open_id、union_id、user_id，默认值为 open_id。, default value is open_id","input":{},"name":"user_id_type","required":false,"type":"string"},{"description":"多维表格的唯一标识符，支持输入文档 url。","input":{},"name":"app_token","required":true,"type":"string"},{"description":"本次请求将要新增的记录列表，格式为：[{\"fields\":{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}}]","input":{},"name":"records","required":true,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。例如：{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}","input":{},"name":"fields","required":true,"type":"string"}],"type":"object"},"type":"list"}],"outputs":[{"description":"错误码，非 0 表示失败。","input":{},"name":"code","required":false,"type":"float"},{"description":"返回结果","input":{},"name":"data","required":false,"schema":[{"description":"本次请求新增的记录列表","input":{},"name":"records","required":false,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。","input":{},"name":"fields","required":false,"type":"string"},{"description":"一条记录的唯一标识 id","input":{},"name":"record_id","required":false,"type":"string"}],"type":"object"},"type":"list"}],"type":"object"},{"description":"链路追踪 id","input":{},"name":"log_id","required":false,"type":"string"},{"description":"错误描述","input":{},"name":"msg","required":false,"type":"string"}],"updateTime":1752558245,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","title":"add_records","mainColor":"#CA61FF"}}}],"edges":[{"sourceNodeID":"148068","targetNodeID":"103111","sourcePortID":"loop-function-inline-output"},{"sourceNodeID":"103111","targetNodeID":"121886"},{"sourceNodeID":"121886","targetNodeID":"154375"},{"sourceNodeID":"154375","targetNodeID":"148068","targetPortID":"loop-function-inline-input"}],"_temp":{"bounds":{"x":2400,"y":0,"width":360,"height":138},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Loop-v2.jpg","description":"用于通过设定循环次数和逻辑，重复执行一系列任务","title":"循环","mainColor":"#00B2B2"}}}],"edges":[{"sourceNodeID":"177157","targetNodeID":"155154"},{"sourceNodeID":"155154","targetNodeID":"161588"},{"sourceNodeID":"161588","targetNodeID":"148068"}]},"bounds":{"x":460,"y":0,"width":2300,"height":138}}
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
{"type":"coze-workflow-clipboard-data","source":{"workflowId":"7518229660888350760","flowMode":0,"spaceId":"7510842919100809242","isDouyin":false,"host":"www.coze.cn"},"json":{"nodes":[{"id":"177157","type":"4","meta":{"position":{"x":640,"y":13}},"data":{"nodeMeta":{"description":"‌获取用户【笔记列表】（xhs_auther_notes）‌\n‌功能描述‌： 根据提供的用户首页地址链接和📕cookie，抓取该用户的所有笔记列表。\n‌参数‌：\ncookieStr：📕的cookie字符串，用于身份验证。\nuserProfileUrl：用户首页的地址链接。\n","icon":"https://p26-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/b1898b6505b7472993ae37794313f9e7~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753068274&x-signature=6d%2B4%2Fu6fA8cHjXLPLRduAj8ZVOc%3D","subtitle":"📕:xhs_auther_notes","title":"xhs_auther_notes"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7425907757733330994","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"xhs_auther_notes","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7413268723496190002","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"📕","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"}],"inputParameters":[{"name":"cookieStr","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"RedBookCookie"},"rawMeta":{"type":1}}}},{"name":"userProfileUrl","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"RedBookAuthUrl"},"rawMeta":{"type":1}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"integer","name":"code","required":false},{"type":"object","name":"data","schema":[{"type":"string","name":"cursor","required":true},{"type":"boolean","name":"has_more","required":true},{"type":"list","name":"notes","schema":{"type":"object","schema":[{"type":"string","name":"auther_nick_name","required":false},{"type":"string","name":"note_cover_width","required":false},{"type":"string","name":"note_url","required":false},{"type":"string","name":"note_xsec_token","required":false},{"type":"string","name":"auther_avatar","required":false},{"type":"string","name":"auther_user_id","required":false},{"type":"string","name":"note_cover_url_pre","required":false},{"type":"string","name":"note_id","required":false},{"type":"string","name":"auther_home_page_url","required":false},{"type":"string","name":"note_display_title","required":false},{"type":"string","name":"note_liked_count","required":false},{"type":"boolean","name":"note_sticky","required":true},{"type":"string","name":"note_card_type","required":false},{"type":"string","name":"note_cover_height","required":false},{"type":"string","name":"note_cover_url_default","required":false},{"type":"boolean","name":"note_liked","required":false}]},"required":false},{"type":"object","name":"auther_info","schema":[{"type":"string","name":"gender","required":false},{"type":"string","name":"interaction","required":false},{"type":"string","name":"ip_location","required":false},{"type":"string","name":"nick_name","required":false},{"type":"string","name":"red_id","required":false},{"type":"string","name":"avatar","required":false},{"type":"string","name":"fans","required":false},{"type":"string","name":"follows","required":false},{"type":"string","name":"user_link_url","required":false},{"type":"string","name":"desc","required":false},{"type":"list","name":"tags","schema":{"type":"string"},"required":false},{"type":"string","name":"user_id","required":false}],"required":false}],"required":false},{"type":"string","name":"msg","required":false},{"type":"string","name":"tips","required":true}]},"_temp":{"bounds":{"x":460,"y":13,"width":360,"height":112},"externalData":{"icon":"https://lf6-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/517231610969187_1725264473893186047_CDXXehfYsy.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=lDH6TRceUKnCA3RPRubURsLPU5E%3D","apiName":"xhs_auther_notes","pluginID":"7413268723496190002","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7402935100184313883","inputs":[{"description":"📕 cookie","input":{},"name":"cookieStr","required":true,"type":"string"},{"description":"数据游标","input":{},"name":"cursor","required":false,"type":"string"},{"description":"用户首页地址链接","input":{},"name":"userProfileUrl","required":true,"type":"string"}],"outputs":[{"input":{},"name":"code","required":false,"type":"integer"},{"input":{},"name":"data","required":false,"schema":[{"input":{},"name":"notes","required":false,"schema":{"schema":[{"input":{},"name":"auther_avatar","required":false,"type":"string"},{"input":{},"name":"note_cover_url_default","required":false,"type":"string"},{"input":{},"name":"note_cover_url_pre","required":false,"type":"string"},{"input":{},"name":"note_cover_width","required":false,"type":"string"},{"input":{},"name":"note_display_title","required":false,"type":"string"},{"input":{},"name":"note_xsec_token","required":false,"type":"string"},{"input":{},"name":"auther_user_id","required":false,"type":"string"},{"input":{},"name":"note_card_type","required":false,"type":"string"},{"input":{},"name":"note_cover_height","required":false,"type":"string"},{"input":{},"name":"note_liked","required":false,"type":"boolean"},{"input":{},"name":"note_sticky","required":true,"type":"boolean"},{"input":{},"name":"note_url","required":false,"type":"string"},{"input":{},"name":"auther_home_page_url","required":false,"type":"string"},{"input":{},"name":"note_id","required":false,"type":"string"},{"input":{},"name":"note_liked_count","required":false,"type":"string"},{"input":{},"name":"auther_nick_name","required":false,"type":"string"}],"type":"object"},"type":"list"},{"input":{},"name":"auther_info","required":false,"schema":[{"input":{},"name":"gender","required":false,"type":"string"},{"input":{},"name":"tags","required":false,"schema":{"assistType":0,"type":"string"},"type":"list"},{"input":{},"name":"user_id","required":false,"type":"string"},{"input":{},"name":"user_link_url","required":false,"type":"string"},{"input":{},"name":"ip_location","required":false,"type":"string"},{"input":{},"name":"nick_name","required":false,"type":"string"},{"input":{},"name":"red_id","required":false,"type":"string"},{"input":{},"name":"avatar","required":false,"type":"string"},{"input":{},"name":"desc","required":false,"type":"string"},{"input":{},"name":"fans","required":false,"type":"string"},{"input":{},"name":"follows","required":false,"type":"string"},{"input":{},"name":"interaction","required":false,"type":"string"}],"type":"object"},{"input":{},"name":"cursor","required":true,"type":"string"},{"input":{},"name":"has_more","required":true,"type":"boolean"}],"type":"object"},{"input":{},"name":"msg","required":false,"type":"string"},{"input":{},"name":"tips","required":true,"type":"string"}],"updateTime":1752558364,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"‌获取用户【笔记列表】（xhs_auther_notes）‌\n‌功能描述‌： 根据提供的用户首页地址链接和📕cookie，抓取该用户的所有笔记列表。\n‌参数‌：\ncookieStr：📕的cookie字符串，用于身份验证。\nuserProfileUrl：用户首页的地址链接。\n","title":"xhs_auther_notes","mainColor":"#CA61FF"}}},{"id":"155154","type":"5","meta":{"position":{"x":1100,"y":13}},"data":{"nodeMeta":{"description":"编写代码，处理输入变量来生成返回值","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","mainColor":"#00B2B2","subTitle":"代码","title":"代码"},"inputs":{"inputParameters":[{"name":"input","input":{"type":"object","schema":[{"type":"string","name":"gender","required":false},{"type":"string","name":"interaction","required":false},{"type":"string","name":"ip_location","required":false},{"type":"string","name":"nick_name","required":false},{"type":"string","name":"red_id","required":false},{"type":"string","name":"avatar","required":false},{"type":"string","name":"fans","required":false},{"type":"string","name":"follows","required":false},{"type":"string","name":"user_link_url","required":false},{"type":"string","name":"desc","required":false},{"type":"list","name":"tags","schema":{"type":"string"},"required":false},{"type":"string","name":"user_id","required":false}],"value":{"type":"ref","content":{"source":"block-output","blockID":"177157","name":"data.auther_info"},"rawMeta":{"type":6}}}}],"code":"# 在这里，您可以通过 ‘args’  获取节点中的输入变量，并通过 'ret' 输出结果\n# 'args' 和 'ret' 已经被正确地注入到环境中\n# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为‘input’的值：\n# params = args.params; \n# input = params.input;\n# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：\n# ret: Output =  { \"name\": ‘小明’, \"hobbies\": [“看书”, “旅游”] };\n\nasync def main(args: Args) -> Output:\n    params = args.params\n    params = params['input']\n\n    # 构建输出对象\n    records = []\n\n    fields = {\n            \"博主昵称\": params[\"nick_name\"],\n            \"头像链接\": params[\"avatar\"],\n            \"简介\": params[\"desc\"],\n            \"粉丝数\": params[\"fans\"],\n            \"关注数\": params[\"follows\"],\n            \"赞藏数\": params[\"interaction\"],\n            \"IP地址\": params[\"ip_location\"],\n            \"博主id\": params[\"red_id\"],\n            \"主页链接\": params[\"user_link_url\"]\n        }\n\n    # 将 fields 转换为 JSON 格式的字符串\n    record = {\"fields\": json.dumps(fields, ensure_ascii=False)}\n    records.append(record)\n\n    # 构建最终返回的输出对象\n    ret = {\n        \"info\": records\n    }\n\n    return ret","language":3,"settingOnError":{"processType":1,"timeoutMs":60000,"retryTimes":0}},"outputs":[{"type":"list","name":"info","schema":{"type":"object","schema":[]}}]},"_temp":{"bounds":{"x":920,"y":13,"width":360,"height":112},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","description":"编写代码，处理输入变量来生成返回值","title":"代码","mainColor":"#00B2B2"}}},{"id":"161588","type":"4","meta":{"position":{"x":1560,"y":13}},"data":{"nodeMeta":{"description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","icon":"https://p6-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/dfc3d7f4eb004d0584aaf47a510beba2~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753069237&x-signature=Vp77knPs%2Bxpvy541HXnkdnxXj20%3D","subtitle":"飞书多维表格:add_records","title":"add_records_账号数据"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7395047759797288987","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"add_records","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7395047759797272603","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"飞书多维表格","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"},{"input":{"type":"integer","value":{"content":0,"type":"literal"}},"name":"pluginAuthMode"}],"inputParameters":[{"name":"app_token","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"FeishuAccountToken"},"rawMeta":{"type":1}}}},{"name":"records","input":{"type":"list","schema":{"type":"object","schema":[]},"value":{"type":"ref","content":{"source":"block-output","blockID":"155154","name":"info"},"rawMeta":{"type":103}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"float","name":"code","required":false,"description":"错误码，非 0 表示失败。"},{"type":"object","name":"data","schema":[{"type":"list","name":"records","schema":{"type":"object","schema":[{"type":"string","name":"fields","required":false,"description":"数据表的字段，即数据表的列，格式为 json 字符串。"},{"type":"string","name":"record_id","required":false,"description":"一条记录的唯一标识 id"}]},"required":false,"description":"本次请求新增的记录列表"}],"required":false,"description":"返回结果"},{"type":"string","name":"log_id","required":false,"description":"链路追踪 id"},{"type":"string","name":"msg","required":false,"description":"错误描述"}]},"_temp":{"bounds":{"x":1380,"y":13,"width":360,"height":112},"externalData":{"icon":"https://lf9-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/618387578815144_1720635554144262143_tbFVbqTqbp.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=kKr8JlRZVPPlIqTty2FdGqqx4bA%3D","apiName":"add_records","pluginID":"7395047759797272603","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7315016311652941851","inputs":[{"description":"多维表格数据表的唯一标识符","input":{},"name":"table_id","required":false,"type":"string"},{"description":"多维表格数据表的名称","input":{},"name":"table_name","required":false,"type":"string"},{"defaultValue":"open_id","description":"用户 ID 类型，可选值有 open_id、union_id、user_id，默认值为 open_id。, default value is open_id","input":{},"name":"user_id_type","required":false,"type":"string"},{"description":"多维表格的唯一标识符，支持输入文档 url。","input":{},"name":"app_token","required":true,"type":"string"},{"description":"本次请求将要新增的记录列表，格式为：[{\"fields\":{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}}]","input":{},"name":"records","required":true,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。例如：{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}","input":{},"name":"fields","required":true,"type":"string"}],"type":"object"},"type":"list"}],"outputs":[{"description":"错误码，非 0 表示失败。","input":{},"name":"code","required":false,"type":"float"},{"description":"返回结果","input":{},"name":"data","required":false,"schema":[{"description":"本次请求新增的记录列表","input":{},"name":"records","required":false,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。","input":{},"name":"fields","required":false,"type":"string"},{"description":"一条记录的唯一标识 id","input":{},"name":"record_id","required":false,"type":"string"}],"type":"object"},"type":"list"}],"type":"object"},{"description":"链路追踪 id","input":{},"name":"log_id","required":false,"type":"string"},{"description":"错误描述","input":{},"name":"msg","required":false,"type":"string"}],"updateTime":1752558245,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","title":"add_records","mainColor":"#CA61FF"}}},{"id":"148068","type":"21","meta":{"position":{"x":2580,"y":0},"canvasPosition":{"x":1940,"y":318}},"data":{"inputs":{"inputParameters":[{"name":"input","input":{"type":"list","schema":{"type":"object","schema":[{"type":"string","name":"auther_nick_name","required":false},{"type":"string","name":"note_cover_width","required":false},{"type":"string","name":"note_url","required":false},{"type":"string","name":"note_xsec_token","required":false},{"type":"string","name":"auther_avatar","required":false},{"type":"string","name":"auther_user_id","required":false},{"type":"string","name":"note_cover_url_pre","required":false},{"type":"string","name":"note_id","required":false},{"type":"string","name":"auther_home_page_url","required":false},{"type":"string","name":"note_display_title","required":false},{"type":"string","name":"note_liked_count","required":false},{"type":"boolean","name":"note_sticky","required":true},{"type":"string","name":"note_card_type","required":false},{"type":"string","name":"note_cover_height","required":false},{"type":"string","name":"note_cover_url_default","required":false},{"type":"boolean","name":"note_liked","required":false}]},"value":{"type":"ref","content":{"source":"block-output","blockID":"177157","name":"data.notes"},"rawMeta":{"type":103}}}}],"loopCount":{"type":"integer","value":{"type":"literal","content":"10"}},"loopType":"array","variableParameters":[]},"nodeMeta":{"description":"用于通过设定循环次数和逻辑，重复执行一系列任务","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Loop-v2.jpg","mainColor":"#00B2B2","subTitle":"循环","title":"循环"},"outputs":[{"name":"output","input":{"type":"list","schema":{"type":"string"},"value":{"type":"ref","content":{"source":"block-output","blockID":"154375","name":"msg"},"rawMeta":{"type":1}}}}]},"blocks":[{"id":"103111","type":"4","meta":{"position":{"x":180,"y":0}},"data":{"nodeMeta":{"description":"‌根据笔记链接获取【笔记详情】（xhs_note_detail）‌‌\n功能描述‌： 根据提供的笔记URL和cookie，抓取该笔记的详细信息。\n‌参数‌：\nnoteUrl：笔记的URL地址。\ncookieStr：📕的cookie字符串，用于身份验证。\n","icon":"https://p3-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/b1898b6505b7472993ae37794313f9e7~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753070075&x-signature=kO%2FyYdX2y7GXvb6Y6Fg6NHIwEQw%3D","subtitle":"📕:xhs_note_detail","title":"xhs_note_detail"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7425907757733347378","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"xhs_note_detail","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7413268723496190002","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"📕","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"}],"inputParameters":[{"name":"cookieStr","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"RedBookCookie"},"rawMeta":{"type":1}}}},{"name":"noteUrl","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"148068","name":"input.note_url"},"rawMeta":{"type":1}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"integer","name":"code","required":false},{"type":"object","name":"data","schema":[{"type":"object","name":"note","schema":[{"type":"string","name":"note_id","required":true,"description":"笔记编号"},{"type":"string","name":"auther_home_page_url","required":true,"description":"作者主页链接"},{"type":"string","name":"note_create_time","required":true,"description":"笔记创建时间"},{"type":"string","name":"note_url","required":true,"description":"笔记链接"},{"type":"string","name":"video_h265_url","required":true},{"type":"string","name":"auther_nick_name","required":true,"description":"作者昵称"},{"type":"string","name":"note_display_title","required":true,"description":"笔记标题"},{"type":"string","name":"note_last_update_time","required":true,"description":"笔记最后更新时间"},{"type":"string","name":"share_count","required":true,"description":"分享数"},{"type":"string","name":"video_a1_url","required":true},{"type":"string","name":"video_h264_url","required":true},{"type":"string","name":"video_h266_url","required":true},{"type":"string","name":"video_id","required":true},{"type":"string","name":"auther_user_id","required":true,"description":"作者ID"},{"type":"boolean","name":"collected","required":true,"description":"是否收藏"},{"type":"string","name":"collected_count","required":true,"description":"收藏数"},{"type":"string","name":"note_card_type","required":true,"description":"笔记类型"},{"type":"string","name":"note_desc","required":true,"description":"笔记描述"},{"type":"string","name":"note_duration","required":true},{"type":"string","name":"note_liked_count","required":true,"description":"点赞数"},{"type":"list","name":"note_tags","schema":{"type":"string"},"required":true,"description":"笔记标签列表"},{"type":"string","name":"auther_avatar","required":true,"description":"作者头像"},{"type":"string","name":"comment_count","required":true,"description":"评论数"},{"type":"list","name":"note_image_list","schema":{"type":"string"},"required":true,"description":"笔记封面"},{"type":"boolean","name":"note_liked","required":true,"description":"是否点赞"},{"type":"string","name":"note_model_type","required":true,"description":"笔记模型类型"}],"required":false,"description":"笔记信息"}],"required":false},{"type":"string","name":"msg","required":true},{"type":"string","name":"tips","required":true}]},"_temp":{"bounds":{"x":1940,"y":318,"width":360,"height":112},"externalData":{"icon":"https://lf26-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/517231610969187_1725264473893186047_CDXXehfYsy.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=x%2BTgrZut%2Fs6I8U6oK7pKeEC%2B4%2BY%3D","apiName":"xhs_note_detail","pluginID":"7413268723496190002","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7402935100184313883","inputs":[{"description":"cookie","input":{},"name":"cookieStr","required":true,"type":"string"},{"description":" 笔记链接","input":{},"name":"noteUrl","required":true,"type":"string"}],"outputs":[{"input":{},"name":"code","required":false,"type":"integer"},{"input":{},"name":"data","required":false,"schema":[{"description":"笔记信息","input":{},"name":"note","required":false,"schema":[{"description":"评论数","input":{},"name":"comment_count","required":true,"type":"string"},{"description":"笔记描述","input":{},"name":"note_desc","required":true,"type":"string"},{"description":"笔记最后更新时间","input":{},"name":"note_last_update_time","required":true,"type":"string"},{"description":"点赞数","input":{},"name":"note_liked_count","required":true,"type":"string"},{"description":"笔记链接","input":{},"name":"note_url","required":true,"type":"string"},{"description":"作者头像","input":{},"name":"auther_avatar","required":true,"type":"string"},{"description":"作者昵称","input":{},"name":"auther_nick_name","required":true,"type":"string"},{"description":"作者ID","input":{},"name":"auther_user_id","required":true,"type":"string"},{"input":{},"name":"video_h264_url","required":true,"type":"string"},{"description":"笔记封面","input":{},"name":"note_image_list","required":true,"schema":{"assistType":0,"type":"string"},"type":"list"},{"description":"笔记模型类型","input":{},"name":"note_model_type","required":true,"type":"string"},{"description":"分享数","input":{},"name":"share_count","required":true,"type":"string"},{"description":"是否点赞","input":{},"name":"note_liked","required":true,"type":"boolean"},{"input":{},"name":"video_a1_url","required":true,"type":"string"},{"input":{},"name":"video_id","required":true,"type":"string"},{"description":"是否收藏","input":{},"name":"collected","required":true,"type":"boolean"},{"description":"笔记创建时间","input":{},"name":"note_create_time","required":true,"type":"string"},{"input":{},"name":"note_duration","required":true,"type":"string"},{"description":"笔记标题","input":{},"name":"note_display_title","required":true,"type":"string"},{"description":"笔记编号","input":{},"name":"note_id","required":true,"type":"string"},{"description":"笔记标签列表","input":{},"name":"note_tags","required":true,"schema":{"assistType":0,"type":"string"},"type":"list"},{"input":{},"name":"video_h265_url","required":true,"type":"string"},{"input":{},"name":"video_h266_url","required":true,"type":"string"},{"description":"作者主页链接","input":{},"name":"auther_home_page_url","required":true,"type":"string"},{"description":"收藏数","input":{},"name":"collected_count","required":true,"type":"string"},{"description":"笔记类型","input":{},"name":"note_card_type","required":true,"type":"string"}],"type":"object"}],"type":"object"},{"input":{},"name":"msg","required":true,"type":"string"},{"input":{},"name":"tips","required":true,"type":"string"}],"updateTime":1752558364,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"‌根据笔记链接获取【笔记详情】（xhs_note_detail）‌‌\n功能描述‌： 根据提供的笔记URL和cookie，抓取该笔记的详细信息。\n‌参数‌：\nnoteUrl：笔记的URL地址。\ncookieStr：📕的cookie字符串，用于身份验证。\n","title":"xhs_note_detail","mainColor":"#CA61FF"}}},{"id":"121886","type":"5","meta":{"position":{"x":640,"y":0}},"data":{"nodeMeta":{"description":"编写代码，处理输入变量来生成返回值","icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","mainColor":"#00B2B2","subTitle":"代码","title":"代码_1"},"inputs":{"inputParameters":[{"name":"input","input":{"type":"object","schema":[{"type":"string","name":"note_id","required":true,"description":"笔记编号"},{"type":"string","name":"auther_home_page_url","required":true,"description":"作者主页链接"},{"type":"string","name":"note_create_time","required":true,"description":"笔记创建时间"},{"type":"string","name":"note_url","required":true,"description":"笔记链接"},{"type":"string","name":"video_h265_url","required":true},{"type":"string","name":"auther_nick_name","required":true,"description":"作者昵称"},{"type":"string","name":"note_display_title","required":true,"description":"笔记标题"},{"type":"string","name":"note_last_update_time","required":true,"description":"笔记最后更新时间"},{"type":"string","name":"share_count","required":true,"description":"分享数"},{"type":"string","name":"video_a1_url","required":true},{"type":"string","name":"video_h264_url","required":true},{"type":"string","name":"video_h266_url","required":true},{"type":"string","name":"video_id","required":true},{"type":"string","name":"auther_user_id","required":true,"description":"作者ID"},{"type":"boolean","name":"collected","required":true,"description":"是否收藏"},{"type":"string","name":"collected_count","required":true,"description":"收藏数"},{"type":"string","name":"note_card_type","required":true,"description":"笔记类型"},{"type":"string","name":"note_desc","required":true,"description":"笔记描述"},{"type":"string","name":"note_duration","required":true},{"type":"string","name":"note_liked_count","required":true,"description":"点赞数"},{"type":"list","name":"note_tags","schema":{"type":"string"},"required":true,"description":"笔记标签列表"},{"type":"string","name":"auther_avatar","required":true,"description":"作者头像"},{"type":"string","name":"comment_count","required":true,"description":"评论数"},{"type":"list","name":"note_image_list","schema":{"type":"string"},"required":true,"description":"笔记封面"},{"type":"boolean","name":"note_liked","required":true,"description":"是否点赞"},{"type":"string","name":"note_model_type","required":true,"description":"笔记模型类型"}],"value":{"type":"ref","content":{"source":"block-output","blockID":"103111","name":"data.note"},"rawMeta":{"type":6}}}}],"code":"# 在这里，您可以通过 ‘args’  获取节点中的输入变量，并通过 'ret' 输出结果\n# 'args' 和 'ret' 已经被正确地注入到环境中\n# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为‘input’的值：\n# params = args.params; \n# input = params.input;\n# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：\n# ret: Output =  { \"name\": ‘小明’, \"hobbies\": [“看书”, “旅游”] };\n\nasync def main(args: Args) -> Output:\n    params = args.params\n    params = params[\"input\"]\n    # 构建输出对象\n    records = []\n\n    fields = {\n            \"标题\": params[\"note_display_title\"],\n            \"创建时间\": params[\"note_create_time\"],\n            \"封面图片链接\": params[\"note_image_list\"][0],\n            \"博主昵称\": params[\"auther_nick_name\"],\n            \"文案\": params[\"note_desc\"],\n            \"标签\": \"||\".join(params[\"note_tags\"]),\n            \"类型\": params[\"note_card_type\"],\n            \"收藏数\": int(params[\"collected_count\"]),\n            \"点赞数\": int(params[\"note_liked_count\"]),\n            \"分享数\": int(params[\"share_count\"]),\n            \"评论数\": int(params[\"comment_count\"]),\n            \"视频链接\": params[\"video_h264_url\"],\n            \"笔记链接\": params[\"note_url\"],\n            \"图片列表\": \"||\".join(params[\"note_image_list\"])\n        }\n\n    # 将 fields 转换为 JSON 格式的字符串\n    record = {\"fields\": json.dumps(fields, ensure_ascii=False)}\n    records.append(record)\n\n    # 构建最终返回的输出对象\n    ret = {\n        \"info\": records\n    }\n\n    return ret","language":3,"settingOnError":{"processType":1,"timeoutMs":60000,"retryTimes":0}},"outputs":[{"type":"list","name":"info","schema":{"type":"object","schema":[]}}]},"_temp":{"bounds":{"x":2400,"y":318,"width":360,"height":112},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Code-v2.jpg","description":"编写代码，处理输入变量来生成返回值","title":"代码","mainColor":"#00B2B2"}}},{"id":"154375","type":"4","meta":{"position":{"x":1100,"y":0}},"data":{"nodeMeta":{"description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","icon":"https://p6-flow-product-sign.byteimg.com/tos-cn-i-13w3uml6bg/dfc3d7f4eb004d0584aaf47a510beba2~tplv-13w3uml6bg-resize:128:128.image?rk3s=2e2596fd&x-expires=1753069237&x-signature=Vp77knPs%2Bxpvy541HXnkdnxXj20%3D","subtitle":"飞书多维表格:add_records","title":"add_records"},"inputs":{"apiParam":[{"input":{"type":"string","value":{"content":"7395047759797288987","rawMeta":{"type":1},"type":"literal"}},"name":"apiID"},{"input":{"type":"string","value":{"content":"add_records","rawMeta":{"type":1},"type":"literal"}},"name":"apiName"},{"input":{"type":"string","value":{"content":"7395047759797272603","rawMeta":{"type":1},"type":"literal"}},"name":"pluginID"},{"input":{"type":"string","value":{"content":"飞书多维表格","rawMeta":{"type":1},"type":"literal"}},"name":"pluginName"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"pluginVersion"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"tips"},{"input":{"type":"string","value":{"content":"","rawMeta":{"type":1},"type":"literal"}},"name":"outDocLink"},{"input":{"type":"integer","value":{"content":0,"type":"literal"}},"name":"pluginAuthMode"}],"inputParameters":[{"name":"app_token","input":{"type":"string","value":{"type":"ref","content":{"source":"block-output","blockID":"100001","name":"FeishuNoteToken"},"rawMeta":{"type":1}}}},{"name":"records","input":{"type":"list","schema":{"type":"object","schema":[]},"value":{"type":"ref","content":{"source":"block-output","blockID":"121886","name":"info"},"rawMeta":{"type":103}}}}],"settingOnError":{"processType":1,"timeoutMs":180000,"retryTimes":0}},"outputs":[{"type":"float","name":"code","required":false,"description":"错误码，非 0 表示失败。"},{"type":"object","name":"data","schema":[{"type":"list","name":"records","schema":{"type":"object","schema":[{"type":"string","name":"fields","required":false,"description":"数据表的字段，即数据表的列，格式为 json 字符串。"},{"type":"string","name":"record_id","required":false,"description":"一条记录的唯一标识 id"}]},"required":false,"description":"本次请求新增的记录列表"}],"required":false,"description":"返回结果"},{"type":"string","name":"log_id","required":false,"description":"链路追踪 id"},{"type":"string","name":"msg","required":false,"description":"错误描述"}]},"_temp":{"bounds":{"x":2860,"y":318,"width":360,"height":112},"externalData":{"icon":"https://lf9-appstore-sign.oceancloudapi.com/ocean-cloud-tos/plugin_icon/618387578815144_1720635554144262143_tbFVbqTqbp.png?lk3s=cd508e2b&x-expires=1755150634&x-signature=kKr8JlRZVPPlIqTty2FdGqqx4bA%3D","apiName":"add_records","pluginID":"7395047759797272603","pluginProductStatus":1,"pluginProductUnlistType":0,"pluginType":1,"spaceID":"7315016311652941851","inputs":[{"description":"多维表格数据表的唯一标识符","input":{},"name":"table_id","required":false,"type":"string"},{"description":"多维表格数据表的名称","input":{},"name":"table_name","required":false,"type":"string"},{"defaultValue":"open_id","description":"用户 ID 类型，可选值有 open_id、union_id、user_id，默认值为 open_id。, default value is open_id","input":{},"name":"user_id_type","required":false,"type":"string"},{"description":"多维表格的唯一标识符，支持输入文档 url。","input":{},"name":"app_token","required":true,"type":"string"},{"description":"本次请求将要新增的记录列表，格式为：[{\"fields\":{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}}]","input":{},"name":"records","required":true,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。例如：{\"文本\":\"文本内容\",\"单选\":\"选项 1\",\"日期\":1674206443000}","input":{},"name":"fields","required":true,"type":"string"}],"type":"object"},"type":"list"}],"outputs":[{"description":"错误码，非 0 表示失败。","input":{},"name":"code","required":false,"type":"float"},{"description":"返回结果","input":{},"name":"data","required":false,"schema":[{"description":"本次请求新增的记录列表","input":{},"name":"records","required":false,"schema":{"schema":[{"description":"数据表的字段，即数据表的列，格式为 json 字符串。","input":{},"name":"fields","required":false,"type":"string"},{"description":"一条记录的唯一标识 id","input":{},"name":"record_id","required":false,"type":"string"}],"type":"object"},"type":"list"}],"type":"object"},{"description":"链路追踪 id","input":{},"name":"log_id","required":false,"type":"string"},{"description":"错误描述","input":{},"name":"msg","required":false,"type":"string"}],"updateTime":1752558245,"channel_id":2,"latestVersionTs":"0","latestVersionName":"","versionName":"","description":"在多维表格数据表中新增多条记录，单次调用最多新增 500 条记录。","title":"add_records","mainColor":"#CA61FF"}}}],"edges":[{"sourceNodeID":"148068","targetNodeID":"103111","sourcePortID":"loop-function-inline-output"},{"sourceNodeID":"103111","targetNodeID":"121886"},{"sourceNodeID":"121886","targetNodeID":"154375"},{"sourceNodeID":"154375","targetNodeID":"148068","targetPortID":"loop-function-inline-input"}],"_temp":{"bounds":{"x":2400,"y":0,"width":360,"height":138},"externalData":{"icon":"https://lf3-static.bytednsdoc.com/obj/eden-cn/dvsmryvd_avi_dvsm/ljhwZthlaukjlkulzlp/icon/icon-Loop-v2.jpg","description":"用于通过设定循环次数和逻辑，重复执行一系列任务","title":"循环","mainColor":"#00B2B2"}}}],"edges":[{"sourceNodeID":"177157","targetNodeID":"155154"},{"sourceNodeID":"155154","targetNodeID":"161588"},{"sourceNodeID":"161588","targetNodeID":"148068"}]},"bounds":{"x":460,"y":0,"width":2300,"height":138}}
```。

接下来要做的，就是接住它，然后，把故事讲下去。

很多朋友在尝试复制工作流时总会卡壳，其实核心操作很简单：先把文件内容全部复制下来，然后到工作流页面直接粘贴，大功告成。不过这里有个小坑，粘贴之后，系统可能会因为缺少“开始”节点而报错，导致某些变量值显示为空。遇到这种情况别慌，只需对照文档第二部分的内容，手动补充一下节点信息即可。

接下来把时间花在刀刃上，聊聊我亲身踩坑后的复盘心得。

**关于效率的抉择**：我为这个任务分别打造了两套工作流，一套是循环写入，另一套则是批量写入。数据量是13条。结果很有意思：循环逐条写入飞书多维表格，全程大约耗时36秒，但它的优势在于完全不消耗Coze资源点和飞书Token；而批量写入虽然只需要8秒，看着快了好几倍，但在飞书那端需要额外配置信息提取环节，这个过程本身就要花时间，并且还得占用飞书的Token。至于具体消耗了多少，我手头还真没详细测算过。

**关于平台的底线**：抓数据这事儿，千万要克制。我一开始没掌握好节奏，一股脑地去抓取，结果发现一次性抓取10条左右比较稳妥。我那天断断续续测试了大约100多条笔记，马上就触发了📕的风控机制。好在平台还算留情，第二天我的账号访问就恢复正常了。所以听我一句劝，细水长流，别贪多，安全第一。

![](img/422310edd333a4fbb6809040a8938c4d.png)