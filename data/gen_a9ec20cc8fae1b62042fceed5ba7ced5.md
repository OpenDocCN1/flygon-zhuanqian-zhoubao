先说选品。

我现在判断一个品值不值得做，不会只看单一指标，而是看三种证据能不能交叉验证。

第一，市场证据：这个商品有人买，而且最近依然在稳定出单；第二，内容证据：平台上有人持续发相关笔记，并且这些笔记能拿到长期流量；第三，能力证据：我自己既能把产品做出来，又能稳定产出内容。

只有当这三样同时成立，我才会认真投入。

如果只有销量，却没有内容入口，商品很可能不适合小红书；如果笔记有热度，但成交很惨，说明大家只是看个热闹，并不真的想买；如果只是自己擅长，却没经过市场验证，最后很可能做出一份无人问津的资料。

所以我会用公式把“市场证据”算得更清楚，而“内容证据”和“能力证据”则需要靠人工判断来补充。此外，我在这款软件里也加入了MCP功能，让AI能直接读取选品库中正在监控的商品，再结合你的个人特点和擅长领域，帮你做分析和选品，效果往往比我手动看更好。

说到“销量监控软件”，很多人第一反应就是：我不会写代码，这跟我没关系。

但实际上，AI编程已经把“能不能写出来”这个门槛压得非常低。现在更难的事情变成了：你能不能把自己的思路说清楚。

如果你只丢给AI一句“帮我做一个小红书销量监控软件”，它很可能直接告诉你：未经允许，我拿不到小红书的数据。就算它继续开发下去，最后给你的可能只是一个有界面、但数据口径完全不可信的演示品。

所以，动工之前自己心里得有底。至少要知道：商品信息从哪来、要记录哪些字段、隔多久记一次、怎么根据前后两次累计销量算出增量，以及采集失败、商品下架、跨日的时候分别怎么处理。

我之前用的是另一套程序，基于MySQL数据库。那版基本是自用，很多规则没花心思写成别人看得懂的文档。上一篇帖子收到的投锚不少，也有圈友私信问实现方式，所以我又重新写了一版，把自己实际遇到的各种问题和解法都整理进了提示词，也算是对大家投锚的回馈。

这份提示词覆盖的内容包括：技术栈、商品输入、字段读取、定时采集、异常处理、销量计算、竞品看板、店铺分析、企业微信通知、只读MCP服务，还有Windows EXE打包。

里面不少内容都是我在使用中一点一点补进去的。举个例子：软件在09:35启动，不能把09:35当成正式整点，而是应该等到10:00再记录第一份完整快照；21:00的采集如果拖到22:00还没跑完，也不能让旧任务一直堆积；读取失败时不能存一个假0；新读到的累计销量低于历史高水位时，更不能硬生生造出负销量。

现在我已经把完整开发提示词整理好了。使用方法非常粗暴：Ctrl+C、Ctrl+V，把后面的提示词直接交给会写代码的AI就行。

注意是Ctrl+C，不是Command+C，因为我目前没有做Mac版。Mac圈友有需要的话，可以基于这份需求让AI自己改造。

当然，这份提示词不一定完美。我只能在遇到问题时解决一个问题，不可能提前预见每个人电脑上的特殊情况。它大概率也不会一次就生成一个完整可用的软件，你还是要会看报错、会调试，让AI继续修补。如果对界面、数据库、采集方式或某个功能不满意，也可以直接提要求，让AI在现有项目上继续改。

我不知道你运行时具体会撞上什么问题，但解决路径始终不变：把真实现象和完整报错交给AI，让它定位、修改，然后重新跑。千万别看到AI吐出一堆代码，就以为软件已经做完了。

说到底，AI编程并不是一句话许愿，而是先把思路讲清楚，再在一遍遍使用中不断修改。

有了这套完整提示词，AI要做的不再是回答一份产品方案，而是实打实地创建一套完整项目。

理想的交付物包括：Python源码、本地SQLite数据库、Windows图形界面、定时采集、错误重试、企业微信通知、只读MCP服务、说明文档、打包脚本、PyInstaller配置，以及可以双击运行的单文件EXE。

最终的使用流程也特别直白：

1. 把商品分享口令、短链、完整链接或24位商品ID加入软件；
2. 让它跑在一台能24小时开机的Windows电脑上；
3. 程序会按自然时间边界，每隔一小时记录一次累计已售和价格；
4. 用相邻快照计算每小时、今日、昨日和历史销量；
5. 用爆品值和商品价值给候选商品排序；
6. 把真正值得研究的商品加入重点监控，再结合店铺和内容做人工判断。

提示词里也特意要求提供只读MCP服务。这样一来，以后支持MCP的AI就能直接查询本地数据，回答像“今天哪些商品增长最快”“哪些店铺销售额最高”“某个商品最近七天是不是在加速”这类问题。

[PRE0]

你最后做出来的成品也许长这样，也许不是，那就得看各位用的是哪款模型了。

## 红薯雷达完整开发提示词

下面是我重新整理后的完整提示词，可直接复制使用。

### 红薯雷达完整开发提示词

### 完整提示词

[PRE1]sql

```sql
CREATE TABLE products (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    shop_name TEXT,
    shop_id TEXT,
    cover TEXT,
    active INTEGER DEFAULT 1,
    created_at TEXT,
    last_error TEXT,
    delisted_at TEXT,
    delisted_reason TEXT
);

CREATE TABLE snapshots (
    product_id TEXT,
    captured_at TEXT,
    sold INTEGER,
    shop_sold INTEGER,
    price REAL,
    fans INTEGER,
    stock_status INTEGER,
    deliverable INTEGER,
    PRIMARY KEY (product_id, captured_at)
);

CREATE INDEX idx_snapshots_product_time ON snapshots (product_id, captured_at);

CREATE TABLE settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    level TEXT,
    source TEXT,
    product_id TEXT,
    product_title TEXT,
    message TEXT,
    error_details TEXT
);

CREATE INDEX idx_logs_time ON logs (timestamp);

CREATE TABLE deleted_products (
    product_id TEXT PRIMARY KEY,
    deleted_at TEXT
);
```