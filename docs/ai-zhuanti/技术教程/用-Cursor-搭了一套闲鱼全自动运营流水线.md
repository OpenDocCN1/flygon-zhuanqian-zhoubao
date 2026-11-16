# 用 Cursor 搭了一套闲鱼全自动运营流水线

# 写在前面

最近收到鱼丸的私信，问我还在不在研究 AI 编程方向。刚好这段时间我用 Cursor 把闲鱼的自动化工具跑通了，索性整理一下实操路径，跟大家一起交流借鉴。

先上整体架构图，方便快速理解工具在干嘛：

![](img/zhuanqian_17bc78d4e8d5c46a4841feb4ca52d782.png)

整套方案拆成三层来做：

1. 前端层

技术选型：vue + element-ui

作用：直观地浏览、筛选和维护数据库里的闲鱼数据

2. 后端层

技术选型：nodejs + mysql

作用：统一收口和调度闲鱼相关数据的存储与管理

3. 脚本层

技术选型：python

作用：负责数据的抓取采集和商品的上架发布

下面就按这三个区块，聊聊我是如何借助 Cursor 完成落地的。

# 一、脚本层【核心】

## 跑起来是什么样

先看整体动效。我录了两段演示，一个是采集，一个是发布。

采集脚本演示：会自动找出状态为未采集的关键词，跑完关键词列表后，再去把对应商品的详情补齐。

发布脚本演示：演示从类目选择、图片上传、标题填充到 SKU 设置的完整流程。

## 脚本具体能做什么

1. 采集脚本

对接比特浏览器的接口，使用其 API 文档完成环境调用。

基础配置项：

数据库连接配置

采集参数配置：并发数、重试次数、间隔等待等

过滤规则配置：想要数等筛选条件

Coze 配置：API Key、bot_id 等

采集关键词下的商品列表

需要入库的字段包括商品 ID、标题、描述文案、主图链接、价格、库存、状态、关联关键词、采集时间、采集状态、想要数、卖家 ID 等，用于后续检索和使用。

采集商品详情页

需要入库的字段包括商品全部图片、SKU 详情、浏览量等。

2. 标题文案脚本

调用 Coze 生成标题文案，参考 Coze API 文档。

3. 上传脚本

基于 webdriver 启动浏览器进入指定页

判断当前是否需要登录

进入商品发布页

选择预设类目和目标闲鱼店铺

上传图片、填入标题文案

识别 SKU 结构：单 SKU / 单组 SKU / 双组 SKU，并配置对应库存与价格

设置发布选项：是否立即发布、是否擦亮等，最后提交

## 开发思路

脚本体量较大，这里统一以采集脚本为例讲解。

对于偏简单的脚本，其实不用太多对话，Composer 就能搞定。整体节奏是先把需求说清、输出开发文档，再进入编码。

![](img/zhuanqian_2efd3c96aee6e93e5f44fb0567774ddd.png)

![](img/zhuanqian_5530279813516bd20f82f6d027e2a7c5.png)

![](img/zhuanqian_10d1d6dd1cb9918f3e6c7b951b5793e0.png)

![](img/zhuanqian_f0532b5d1a8daaf0626a5c1292e7fe94.png)

![](img/zhuanqian_56457b3bdab39640ac70084c2befa4d1.png)

![](img/zhuanqian_15b8953ad7059f0146cc7ad539945af8.png)

![](img/zhuanqian_27f32f191b08d4a2bb2193a095ac88ca.png)

![](img/zhuanqian_a2d30c9594895b95ff67d1398cca6b9b.png)

![](img/zhuanqian_90c760defaa2bf87abee8b0c70a880bc.png)

![](img/zhuanqian_2b4ec2890735cdce76167599291c1c62.png)

![](img/zhuanqian_0e882e9cbc182917e12bceced043b621.png)

![](img/zhuanqian_f6418d5f0723657fe21dedf889a4bd2e.png)

# 二、后端层【核心】

## 功能拆解

我习惯采用模块化方式推进。

模块化本质是把复杂系统拆成多个独立可复用的单元，以此提升效率、复用率、可维护性和扩展性。

模块的基本构成：

接口：对外服务入口，是模块间通信的桥梁

功能：模块承载的具体业务逻辑

逻辑：内部实现细节，如算法与数据结构

状态：模块运行时的状态及转换关系

模块化的好处：

开发效率更高：系统拆分后可并行推进，周期缩短

代码复用更好：通用模块封装后可在多项目复用

维护成本更低：接口隔离降低耦合，改动局部不影响整体

扩展性更强：新增功能可通过增模块或改接口实现，无需重构

在动工前，先想清楚需要哪些数据、基于这些数据要做什么操作、数据库里要保留哪些核心字段、哪些是次要字段。再据此梳理后端必须支撑的功能点。如果要打通从采集到发布的闭环，后端需要的数据流如下图所示。

![](img/zhuanqian_0698be99f35ed80f731b89193138fc1f.png)

## 落地方案

需求明确后，我会在 Cursor 里给角色分工：Chat 担任产品经理、Chat 担任代码审查、Composer 担任程序员。

先和产品经理对齐整体流程并输出开发文档。

![](img/zhuanqian_3ee5ffa03bd492d0cdabe1cdb6d5d0ac.png)

![](img/zhuanqian_6ce6f5613a73a475c6544c01a16f0e56.png)

这是第一版文档，后续可以继续迭代。

![](img/zhuanqian_304280b7c0b44ef2b9f4187a36ca2904.png)

![](img/zhuanqian_e3118d57945dbfd8a392e0d7e0d033ea.png)

![](img/zhuanqian_a140d42e7c0914d7fd333901c9f89837.png)

让 Cursor 在原文档基础上迭代，我们可以把不需要的过度设计砍掉，比如库存预警、安全日志之类的。

![](img/zhuanqian_d02caa27b90ef2eabf72822af5cdc4d8.png)

![](img/zhuanqian_1c396564fd7053d6c45bd479964890e5.png)

这是经过初步调整后的文档，可以按需继续填充。

再与程序员对齐需求并开始编码。这里我坚持模块化，保证后续好扩展和接手。

![](img/zhuanqian_02e97a3e8da475e78c326980813ab43d.png)

![](img/zhuanqian_6a010dbb6c8f91d5462a50904db489c9.png)

![](img/zhuanqian_542ca945692ab90592007785adaf8470.png)

随后让代码审查角色做一次全面检查，输出修改建议。我们筛选出必要的问题，形成正式的审查报告，再把报告丢给 Composer 执行修改。

![](img/zhuanqian_1e54d2a930298474a689cc9d4e3e79c5.png)

![](img/zhuanqian_05ee971d7f19799940e69ed8fbd0c9c9.png)

![](img/zhuanqian_360f3b8ec8e9f7b631943319f5bedfd3.png)

![](img/zhuanqian_fc2c3bd70684bb13a9c7d6f0bfcf17b5.png)

最后把所有数据表的完整字段清单导出来，方便脚本层调用时对齐表结构。示例：

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
mysql> SHOW TABLES;
+-------------------------+
| Tables_in_xianyu_manage |
+-------------------------+
| t_keyword               |
| t_log_operation         |
| t_prod_category         |
| t_prod_image            |
| t_prod_info             |
| t_prod_keyword          |
| t_prod_operation_log    |
| t_prod_shop             |
| t_seller_info           |
| t_shop_info             |
| t_shop_item             |
| t_stat_daily            |
| t_sys_config            |
| t_sys_user              |
| t_task_collection       |
| t_task_execution        |
| v_shop_collect_stats    |
+-------------------------+
19 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_collect_log;
+------------+----------+------+-----+-------------------+-------------------+
| Field      | Type     | Null | Key | Default           | Extra             |
+------------+----------+------+-----+-------------------+-------------------+
| id         | bigint   | NO   | PRI | NULL              | auto_increment    |
| task_id    | bigint   | NO   | MUL | NULL              |                   |
| log_type   | tinyint  | NO   |     | NULL              |                   |
| content    | text     | NO   |     | NULL              |                   |
| created_at | datetime | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+----------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_keyword;
+----------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field          | Type         | Null | Key | Default           | Extra                                         |
+----------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id             | bigint       | NO   | PRI | NULL              | auto_increment                                |
| name           | varchar(100) | NO   | UNI | NULL              |                                               |
| collect_status | tinyint      | NO   | MUL | 0                 |                                               |
| collect_time   | datetime     | YES  | MUL | NULL              |                                               |
| created_at     | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at     | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+----------------+--------------+------+-----+-------------------+-----------------------------------------------+
6 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_prod_image;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | bigint       | NO   | PRI | NULL              | auto_increment    |
| product_id | bigint       | NO   | MUL | NULL              |                   |
| url        | varchar(500) | NO   |     | NULL              |                   |
| sort       | int          | NO   |     | 0                 |                   |
| is_main    | tinyint      | NO   |     | 0                 |                   |
| status     | tinyint      | NO   | MUL | 1                 |                   |
| file_size  | int          | YES  |     | NULL              |                   |
| dimensions | varchar(20)  | YES  |     | NULL              |                   |
| created_at | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
9 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_prod_info;
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| Field             | Type          | Null | Key | Default           | Extra                                         |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| id                | bigint        | NO   | PRI | NULL              | auto_increment                                |
| name              | varchar(255)  | NO   |     | NULL              |                                               |
| title             | varchar(255)  | NO   |     | NULL              |                                               |
| code              | varchar(50)   | NO   | MUL | NULL              |                                               |
| category_id       | bigint        | NO   | MUL | NULL              |                                               |
| price             | decimal(10,2) | NO   |     | 0.00              |                                               |
| stock             | int           | NO   |     | 0                 |                                               |
| sales             | int           | NO   |     | 0                 |                                               |
| status            | tinyint       | NO   | MUL | 0                 |                                               |
| source_url        | varchar(500)  | YES  |     | NULL              |                                               |
| description       | text          | YES  |     | NULL              |                                               |
| keywords          | varchar(500)  | YES  | MUL | NULL              |                                               |
| shop_id           | bigint        | NO   | MUL | NULL              |                                               |
| collect_time      | datetime      | YES  | MUL | NULL              |                                               |
| publish_time      | datetime      | YES  |     | NULL              |                                               |
| rewrite_status    | tinyint       | NO   | MUL | 0                 |                                               |
| publish_status    | tinyint       | NO   | MUL | 0                 |                                               |
| created_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| deleted_at        | datetime      | YES  |     | NULL              |                                               |
| collect_status    | tinyint       | NO   | MUL | 0                 |                                               |
| collect_error     | varchar(500)  | YES  |     | NULL              |                                               |
| collect_count     | int           | NO   |     | 0                 |                                               |
| last_collect_time | datetime      | YES  |     | NULL              |                                               |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
24 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_seller_info;
+------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field            | Type         | Null | Key | Default           | Extra                                         |
+------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id               | bigint       | NO   | PRI | NULL              | auto_increment                                |
| shop_id          | varchar(255) | NO   |     | NULL              |                                               |
| seller_id        | varchar(50)  | NO   | UNI | NULL              |                                               |
| nickname         | varchar(100) | YES  |     | NULL              |                                               |
| rating           | decimal(3,1) | YES  | MUL | NULL              |                                               |
| total_items      | int          | NO   |     | 0                 |                                               |
| good_rating_rate | decimal(5,2) | YES  |     | NULL              |                                               |
| status           | tinyint      | NO   | MUL | 1                 |                                               |
| last_active_time | datetime     | YES  | MUL | NULL              |                                               |
| description      | text         | YES  |     | NULL              |                                               |
| location         | varchar(100) | YES  |     | NULL              |                                               |
| created_at       | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at       | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| deleted_at       | datetime     | YES  |     | NULL              |                                               |
+------------------+--------------+------+-----+-------------------+-----------------------------------------------+
14 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_shop_info;
+--------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field              | Type         | Null | Key | Default           | Extra                                         |
+--------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id                 | bigint       | NO   | PRI | NULL              | auto_increment                                |
| name               | varchar(100) | NO   |     | NULL              |                                               |
| platform           | varchar(50)  | NO   | MUL | NULL              |                                               |
| shop_url           | varchar(500) | YES  |     | NULL              |                                               |
| status             | tinyint      | NO   | MUL | 0                 |                                               |
| rating             | decimal(2,1) | YES  |     | 5.0               |                                               |
| created_at         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| total_products     | int          | NO   |     | 0                 |                                               |
| collected_products | int          | NO   |     | 0                 |                                               |
| last_collect_time  | datetime     | YES  |     | NULL              |                                               |
| collect_status     | tinyint      | NO   | MUL | 0                 |                                               |
+--------------------+--------------+------+-----+-------------------+-----------------------------------------------+
12 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_sys_config;
+--------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field        | Type         | Null | Key | Default           | Extra                                         |
+--------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id           | bigint       | NO   | PRI | NULL              | auto_increment                                |
| config_key   | varchar(50)  | NO   | UNI | NULL              |                                               |
| config_value | text         | YES  |     | NULL              |                                               |
| description  | varchar(200) | YES  |     | NULL              |                                               |
| created_at   | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at   | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+--------------+-------------
mysql> SHOW COLUMNS FROM t_shop_item;
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| Field             | Type          | Null | Key | Default           | Extra                                         |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| id                | bigint        | NO   | PRI | NULL              | auto_increment                                |
| seller_id         | bigint        | NO   | MUL | NULL              |                                               |
| item_id           | bigint        | NO   | MUL | NULL              |                                               |
| item_price        | decimal(10,2) | YES  |     | NULL              |                                               |
| item_image        | varchar(500)  | YES  |     | NULL              |                                               |
| collect_status    | tinyint       | NO   | MUL | 0                 |                                               |
| collect_count     | int           | NO   |     | 0                 |                                               |
| last_collect_time | datetime      | YES  |     | NULL              |                                               |
| created_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
10 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM cookies;
ERROR 2013 (HY000): Lost connection to MySQL server during query
No connection. Trying to reconnect...
Connection id:    117
Current database: xianyu_manage
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field         | Type         | Null | Key | Default           | Extra                                         |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id            | int          | NO   | PRI | NULL              | auto_increment                                |
| cookie        | text         | NO   |     | NULL              |                                               |
| token         | varchar(255) | NO   |     | NULL              |                                               |
| create_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| update_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| last_use      | datetime     | YES  |     | NULL              |                                               |
| is_valid      | tinyint(1)   | YES  |     | 1                 |                                               |
| fail_count    | int          | YES  |     | 0                 |                                               |
| success_count | int          | YES  |     | 0                 |                                               |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
9 rows in set (0.01 sec)
mysql> SHOW COLUMNS FROM proxies;
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field         | Type         | Null | Key | Default           | Extra                                         |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id            | int          | NO   | PRI | NULL              | auto_increment                                |
| ip            | varchar(255) | NO   |     | NULL              |                                               |
| port          | int          | NO   |     | NULL              |                                               |
| protocol      | varchar(10)  | YES  |     | http              |                                               |
| is_valid      | tinyint(1)   | YES  |     | 1                 |                                               |
| create_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| update_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| last_use      | datetime     | YES  |     | NULL              |                                               |
| fail_count    | int          | YES  |     | 0                 |                                               |
| success_count | int          | YES  |     | 0                 |                                               |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
10 rows in set (0.00 sec)
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
mysql> SHOW TABLES;
+-------------------------+
| Tables_in_xianyu_manage |
+-------------------------+
| t_keyword               |
| t_log_operation         |
| t_prod_category         |
| t_prod_image            |
| t_prod_info             |
| t_prod_keyword          |
| t_prod_operation_log    |
| t_prod_shop             |
| t_seller_info           |
| t_shop_info             |
| t_shop_item             |
| t_stat_daily            |
| t_sys_config            |
| t_sys_user              |
| t_task_collection       |
| t_task_execution        |
| v_shop_collect_stats    |
+-------------------------+
19 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_collect_log;
+------------+----------+------+-----+-------------------+-------------------+
| Field      | Type     | Null | Key | Default           | Extra             |
+------------+----------+------+-----+-------------------+-------------------+
| id         | bigint   | NO   | PRI | NULL              | auto_increment    |
| task_id    | bigint   | NO   | MUL | NULL              |                   |
| log_type   | tinyint  | NO   |     | NULL              |                   |
| content    | text     | NO   |     | NULL              |                   |
| created_at | datetime | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+----------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_keyword;
+----------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field          | Type         | Null | Key | Default           | Extra                                         |
+----------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id             | bigint       | NO   | PRI | NULL              | auto_increment                                |
| name           | varchar(100) | NO   | UNI | NULL              |                                               |
| collect_status | tinyint      | NO   | MUL | 0                 |                                               |
| collect_time   | datetime     | YES  | MUL | NULL              |                                               |
| created_at     | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at     | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+----------------+--------------+------+-----+-------------------+-----------------------------------------------+
6 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_prod_image;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | bigint       | NO   | PRI | NULL              | auto_increment    |
| product_id | bigint       | NO   | MUL | NULL              |                   |
| url        | varchar(500) | NO   |     | NULL              |                   |
| sort       | int          | NO   |     | 0                 |                   |
| is_main    | tinyint      | NO   |     | 0                 |                   |
| status     | tinyint      | NO   | MUL | 1                 |                   |
| file_size  | int          | YES  |     | NULL              |                   |
| dimensions | varchar(20)  | YES  |     | NULL              |                   |
| created_at | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
9 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_prod_info;
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| Field             | Type          | Null | Key | Default           | Extra                                         |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| id                | bigint        | NO   | PRI | NULL              | auto_increment                                |
| name              | varchar(255)  | NO   |     | NULL              |                                               |
| title             | varchar(255)  | NO   |     | NULL              |                                               |
| code              | varchar(50)   | NO   | MUL | NULL              |                                               |
| category_id       | bigint        | NO   | MUL | NULL              |                                               |
| price             | decimal(10,2) | NO   |     | 0.00              |                                               |
| stock             | int           | NO   |     | 0                 |                                               |
| sales             | int           | NO   |     | 0                 |                                               |
| status            | tinyint       | NO   | MUL | 0                 |                                               |
| source_url        | varchar(500)  | YES  |     | NULL              |                                               |
| description       | text          | YES  |     | NULL              |                                               |
| keywords          | varchar(500)  | YES  | MUL | NULL              |                                               |
| shop_id           | bigint        | NO   | MUL | NULL              |                                               |
| collect_time      | datetime      | YES  | MUL | NULL              |                                               |
| publish_time      | datetime      | YES  |     | NULL              |                                               |
| rewrite_status    | tinyint       | NO   | MUL | 0                 |                                               |
| publish_status    | tinyint       | NO   | MUL | 0                 |                                               |
| created_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| deleted_at        | datetime      | YES  |     | NULL              |                                               |
| collect_status    | tinyint       | NO   | MUL | 0                 |                                               |
| collect_error     | varchar(500)  | YES  |     | NULL              |                                               |
| collect_count     | int           | NO   |     | 0                 |                                               |
| last_collect_time | datetime      | YES  |     | NULL              |                                               |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
24 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_seller_info;
+------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field            | Type         | Null | Key | Default           | Extra                                         |
+------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id               | bigint       | NO   | PRI | NULL              | auto_increment                                |
| shop_id          | varchar(255) | NO   |     | NULL              |                                               |
| seller_id        | varchar(50)  | NO   | UNI | NULL              |                                               |
| nickname         | varchar(100) | YES  |     | NULL              |                                               |
| rating           | decimal(3,1) | YES  | MUL | NULL              |                                               |
| total_items      | int          | NO   |     | 0                 |                                               |
| good_rating_rate | decimal(5,2) | YES  |     | NULL              |                                               |
| status           | tinyint      | NO   | MUL | 1                 |                                               |
| last_active_time | datetime     | YES  | MUL | NULL              |                                               |
| description      | text         | YES  |     | NULL              |                                               |
| location         | varchar(100) | YES  |     | NULL              |                                               |
| created_at       | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at       | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| deleted_at       | datetime     | YES  |     | NULL              |                                               |
+------------------+--------------+------+-----+-------------------+-----------------------------------------------+
14 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_shop_info;
+--------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field              | Type         | Null | Key | Default           | Extra                                         |
+--------------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id                 | bigint       | NO   | PRI | NULL              | auto_increment                                |
| name               | varchar(100) | NO   |     | NULL              |                                               |
| platform           | varchar(50)  | NO   | MUL | NULL              |                                               |
| shop_url           | varchar(500) | YES  |     | NULL              |                                               |
| status             | tinyint      | NO   | MUL | 0                 |                                               |
| rating             | decimal(2,1) | YES  |     | 5.0               |                                               |
| created_at         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| total_products     | int          | NO   |     | 0                 |                                               |
| collected_products | int          | NO   |     | 0                 |                                               |
| last_collect_time  | datetime     | YES  |     | NULL              |                                               |
| collect_status     | tinyint      | NO   | MUL | 0                 |                                               |
+--------------------+--------------+------+-----+-------------------+-----------------------------------------------+
12 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM t_sys_config;
+--------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field        | Type         | Null | Key | Default           | Extra                                         |
+--------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id           | bigint       | NO   | PRI | NULL              | auto_increment                                |
| config_key   | varchar(50)  | NO   | UNI | NULL              |                                               |
| config_value | text         | YES  |     | NULL              |                                               |
| description  | varchar(200) | YES  |     | NULL              |                                               |
| created_at   | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at   | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+--------------+-------------
mysql> SHOW COLUMNS FROM t_shop_item;
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| Field             | Type          | Null | Key | Default           | Extra                                         |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
| id                | bigint        | NO   | PRI | NULL              | auto_increment                                |
| seller_id         | bigint        | NO   | MUL | NULL              |                                               |
| item_id           | bigint        | NO   | MUL | NULL              |                                               |
| item_price        | decimal(10,2) | YES  |     | NULL              |                                               |
| item_image        | varchar(500)  | YES  |     | NULL              |                                               |
| collect_status    | tinyint       | NO   | MUL | 0                 |                                               |
| collect_count     | int           | NO   |     | 0                 |                                               |
| last_collect_time | datetime      | YES  |     | NULL              |                                               |
| created_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| updated_at        | datetime      | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+-------------------+---------------+------+-----+-------------------+-----------------------------------------------+
10 rows in set (0.00 sec)
mysql> SHOW COLUMNS FROM cookies;
ERROR 2013 (HY000): Lost connection to MySQL server during query
No connection. Trying to reconnect...
Connection id:    117
Current database: xianyu_manage
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field         | Type         | Null | Key | Default           | Extra                                         |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id            | int          | NO   | PRI | NULL              | auto_increment                                |
| cookie        | text         | NO   |     | NULL              |                                               |
| token         | varchar(255) | NO   |     | NULL              |                                               |
| create_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| update_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| last_use      | datetime     | YES  |     | NULL              |                                               |
| is_valid      | tinyint(1)   | YES  |     | 1                 |                                               |
| fail_count    | int          | YES  |     | 0                 |                                               |
| success_count | int          | YES  |     | 0                 |                                               |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
9 rows in set (0.01 sec)
mysql> SHOW COLUMNS FROM proxies;
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| Field         | Type         | Null | Key | Default           | Extra                                         |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
| id            | int          | NO   | PRI | NULL              | auto_increment                                |
| ip            | varchar(255) | NO   |     | NULL              |                                               |
| port          | int          | NO   |     | NULL              |                                               |
| protocol      | varchar(10)  | YES  |     | http              |                                               |
| is_valid      | tinyint(1)   | YES  |     | 1                 |                                               |
| create_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
| update_time   | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
| last_use      | datetime     | YES  |     | NULL              |                                               |
| fail_count    | int          | YES  |     | 0                 |                                               |
| success_count | int          | YES  |     | 0                 |                                               |
+---------------+--------------+------+-----+-------------------+-----------------------------------------------+
10 rows in set (0.00 sec)
```。

接下来要做的，就是接住它，然后，把故事讲下去。

# 第三部分｜前端（辅助）

## 界面效果

![](img/zhuanqian_63fb56436a88162c50c36aa7cce8233c.png)

![](img/zhuanqian_df6c1479dbcd7d56054b74e6792cc369.png)

![](img/zhuanqian_426f9250424bef4eaa22fa4f17355eac.png)

![](img/zhuanqian_c3330914ee0e0ea8eb29d6306806d1b6.png)

![](img/zhuanqian_0c834aeb9a3332e574f7f86ef20c1311.png)

## 操作流程

1. 先把待抓取的搜索词维护进关键字清单。

![](img/zhuanqian_dcc1131e2816a94e6854c16b8ada29f3.png)

点一下「成批添加」

![](img/zhuanqian_17a0d61aa6baf8888f22e0792e0682f7.png)

成批添加

![](img/zhuanqian_709c6b273b26462b9ec310e514cf43ea.png)

添加完成

2. 运行抓取程序，程序运行时会把库里还没抓过的关键字捞出来，并把这些词的状态置为「抓取中」。

3. 逐个关键字抓取对应货品清单，对清单做筛选、去重、清洗，然后写回库中；单个关键字跑完后，状态转为「已抓完」。

4. 等所有关键字都处理完毕，程序会接着自动开启货品详情的抓取：找出仍处于「未抓取」状态的货品 ID，一个个拉取详情。

5. 拉回来的详情用于补齐基础货品表，成功抓到的货品，状态会自动更新。

6. 接着去前端做选品，挑中的货品直接进入发布环节。

7. 进入上架管理页，有两大块要处理：一是图片素材，二是标题内容。

8. 目前图片走的是软件批量处理，标题内容则交给 Coze 的接口生成，Coze 处理完后把结果写回数据存储。

9. 最后启动自动上架流程，正式发布。这里的核心难点在于 SKU 的粒度：单条 SKU、成组 SKU、批量 SKU 要分开处理。具体细节可参考操作录屏。

# 第四部分｜Cursor 避坑实录

1. 需求描述得太细，Cursor 反而会偷懒，给出的代码常常缺这缺那。

2. 需求给得太泛，它又会产出大量冗余代码，啰嗦又难维护。

3. 理解经常跑偏。比如我正在调整货品清单页，一旦切到其他标签页，它会把修改对象搞错。

![](img/zhuanqian_9376a86b488522afca37522ead844bf1.png)

当时我正在调整货品清单页

![](img/zhuanqian_4634d63bd19070026e19601e3c2a92ef.png)

结果它跑去了上架管理页，把这里的代码改错了

4. 改着改着，还可能误删原本正确的逻辑。

![](img/zhuanqian_754bc917941a406222c515958cf2becd.png)

![](img/zhuanqian_386f13c1a8d9dc23623aad703a4d17a3.png)

![](img/zhuanqian_d78b60090b5e6f5e39ffbe024b819eef.png)

![](img/zhuanqian_5deb0b73200cc4a6457966adb8f97465.png)

5. 增加新需求时，如果没有人工提醒，它会直接硬写一段新代码来完成，而不是先检查当前组件是不是已经具备类似能力。这一步必须人工介入。

6. 改动往往不闭环。比如让它接入一个新组件的用法，它会直接调用组件里的方法，却忘记引入这个组件，一运行就报错。

7. 对话聊得太久，上下文塞得太满，只能另开新会话。

![](img/zhuanqian_eeed37efd9f45f3997acc6f0a48d21aa.png)

# 五、写在最后

Cursor 的基础环境搭建，可以参考这些资料：

赚钱社区的 Cursor 专题内容，把初始设置和入门开发讲得很透，照着做基本不会错。

还有一篇圈友的文章，讲怎么借助 Cursor 搭建复杂系统、和 AI 结对开发，也很有启发性。

另外赚钱社区里关于 AI 实战的帖子不少，质量普遍不错。想继续深挖 Cursor，去 AI 实战板块刷一刷就对了。

如果今天的内容对你有帮助，记得去原文底下点赞，感谢支持！