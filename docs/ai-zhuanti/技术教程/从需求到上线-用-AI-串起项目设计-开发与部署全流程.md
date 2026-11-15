# 从需求到上线：用 AI 串起项目设计、开发与部署全流程
如今，AI 不只是用来聊天和生成代码，它已经能够参与到一个项目从需求梳理、数据库设计，到接口规划、代码开发，再到云端部署的完整链路中。
这套流程主要使用：
- **DeepSeek**：负责需求分析、数据库设计和接口规划
- **Cursor**：负责前后端代码开发
- **DevBox**：提供隔离、统一的开发环境
- **Sealos**：完成数据库创建、项目部署和公网访问
简单来说，就是先让 AI 帮我们完成设计，再借助 Cursor 编写代码，最后通过 DevBox 和 Sealos 将项目部署上线。
## 一、整体流程概览
一个完整项目大致可以拆分为三个阶段。
### 1. 项目设计
根据产品原型和需求文档，分析业务内容，设计数据库表结构、表之间的关联关系以及系统接口，最终整理出一份完整的接口文档。
### 2. 项目开发
有了数据库和接口设计之后，就可以进入代码开发阶段。前端与后端都按照接口文档实施，开发过程中只需要通过自然语言向 AI 描述需求，Cursor 就能协助生成和修改代码。
### 3. 项目部署
项目开发完成后，借助 DevBox 和 Sealos 可以快速完成发布。最终项目会获得一个公网访问地址，其他人无需进入本地环境，也能直接访问系统。
# 二、开始之前需要准备什么
## 1. DeepSeek
拿到页面原型和产品需求文档后，第一步通常是设计数据库。
这部分工作可以交给 DeepSeek 完成。当然，Cursor 或 Claude 同样能够承担这类任务，但如果更关注使用成本，DeepSeek 已经足以满足大部分基础设计需求。
使用前需要先注册 DeepSeek 账号。
## 2. DevBox
开发项目时，后端可能需要 JDK、Maven 等环境，前端则需要 Node.js。传统做法是先在电脑上逐项安装，之后测试环境、生产环境还要再次配置。
这种方式不仅耗时，还容易出现环境差异：
- 本地可以运行，测试环境无法启动
- 测试环境没有问题，上线后却出现异常
- 不同开发人员的环境不一致
- 依赖版本不统一，排查问题困难
DevBox 的作用，就是帮助我们快速创建一个独立、干净且与其他环境隔离的开发空间。
项目地址：
https://sealos.run/
Sealos 是以 Kubernetes 为基础构建的云操作系统，可以帮助用户快速部署、管理和扩展应用。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4fc10c0423e83ffe884a184dc79017a2.png>
注册 Sealos 后，如果需要数据库，可以直接在平台内创建；如果需要开发环境，也可以通过「DevBox」一键生成。系统会自动准备项目所需的运行依赖，我们不必再手动安装各种环境。
另外，Sealos 新用户注册后会赠送 10 元额度，可以用于体验相关服务。
## 3. Cursor
代码开发离不开合适的工具，这里选择 Cursor。
Cursor 可以理解为一款集成 AI 能力的开发工具。开发过程中，我们不一定要自己逐行编写代码，只需要把需求、修改目标和预期效果描述清楚，就可以让 AI 协助完成代码生成、调整和排错。
# 三、数据库设计：先让 AI 做分析，再由开发人员确认
拿到产品原型和需求说明后，不建议直接开始写代码。数据库结构是否合理，会直接影响后续接口设计和系统开发。
通常可以按照下面四个步骤进行：
1. 结合原型和需求，判断业务涉及哪些数据实体，也就是需要创建多少张表。
2. 分析不同表之间的关联关系，确定是一对一、一对多还是多对多。
3. 明确每张表需要哪些字段，并确定字段类型、默认值和约束条件。
4. 整理出完整的表结构，生成建库、建表脚本。
前面三项工作都可以交给 AI 协助完成，但 AI 的结果不能直接照搬。开发人员仍然需要结合原型、需求和实际业务进行检查、修正与完善。
## 1. 判断需要创建多少张表
以部门管理为例，可以将页面原型和需求说明交给 AI，让它分析该模块涉及的数据表。
部门管理模块提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2e854f3cbcb29c51617725ab62c0ca77.png>
分析结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f9d9d60bdfbb7de87af7cf569d7368fb.png>
AI 判断部门管理只需要一张表。此时应当对照产品原型进行复核，确认页面中的数据是否都可以由部门表承载。经过检查后，可以确认这个判断是合理的。
接着分析员工管理模块。
员工管理模块提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_654019e93d140fc7147e6771e270d8ac.png>
分析结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_644ba722bf02b0b79f49a98896b9d74e.png>
AI 表面上给出的结论是一张表，但从它的分析过程可以看出，它已经注意到了员工工作经历这一类数据，只是认为可以将工作经历直接作为员工表中的一个字段保存。
这时就需要结合实际业务做判断。
如果一个员工可能拥有多段工作经历，那么将所有经历塞进员工表显然不够合理。因此，更合适的设计是拆分为：
- 员工表
- 员工工作经历表
综合部门管理和员工管理两个模块，最终需要三张表：
- 部门表
- 员工表
- 员工工作经历表
## 2. 分析表与表之间的关系
确定表数量之后，还要继续判断这些表之间如何关联。
可以继续向 AI 提问：
> 部门管理和员工管理两个模块一共涉及三张表，分别是员工表、工作经历表和部门表，请分析这三张表之间的关系。
分析结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8ee3d82135a5e1c0e9d7f6047e7b7398.png>
经过核对后，可以确认这三张表的关系符合业务逻辑。
一般来说：
- 一个部门可以对应多名员工
- 一名员工通常只归属于一个部门
- 一名员工可以拥有多条工作经历
- 每条工作经历只属于一名员工
通过这一步，我们就明确了数据表数量以及彼此之间的关联关系。
## 3. 确定具体表结构
接下来要继续确定每张表的字段、数据类型和约束。
本次涉及三张表：
- 部门表
- 员工表
- 员工工作经历表
可以把产品需求文档直接提供给 AI，让它结合业务要求输出初版表结构。
### 3.1 部门表
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_330c4ac695182ebbe1e42e7774f34049.png>
初步结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_933ded75544abccdd67f1b535352705e.png>
AI 给出的结构通常需要进一步优化。我们可以先梳理自己的设计思路，再重新补充要求，让 AI 按照更明确的规则进行调整。
优化提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_13e3dd104106af9dc85c3aff9e2aa2aa.png>
将整理好的提示词复制给 AI 后，可以得到优化后的建表 SQL：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0504a6b992e7329bd4b2a0a26ec3a5a1.png>
部门表建表语句：
```
CREATE TABLE `dept` (
`id` int(11) NOT NULL AUTO_INCREMENT COMMENT '部门ID',
`name` varchar(10) NOT NULL COMMENT '部门名称（唯一，2-10字符）',
`update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后操作时间',
`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
PRIMARY KEY (`id`),
UNIQUE KEY `name_unique` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='部门管理数据表';
```
### 3.2 员工表与工作经历表
部门表确定后，再按照同样的方式设计员工相关表。
员工表设计提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_494f2a78da6df11b2eddc22042bb272a.png>
AI 输出结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1199e19e570791bd1b536e5aebc58df1.png>
接下来要结合原型和需求文档逐项检查，例如：
- 页面中是否出现了所有必要字段
- 字段名称是否统一
- 数据类型是否合适
- 是否需要非空、唯一等约束
- 员工与部门之间的关联是否正确
- 工作经历是否应该独立成表
确认问题后，再向 AI 发出优化要求。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_843c9e1eca4bfbcc9713ef133b7bcea3.png>
优化后的员工表建表语句：
```
CREATE TABLE emp (
id INT PRIMARY KEY AUTO_INCREMENT COMMENT '员工ID',
username VARCHAR(20) NOT NULL UNIQUE COMMENT '用户名（2-20字符）',
name VARCHAR(10) NOT NULL COMMENT '姓名（2-10字符）',
gender TINYINT NOT NULL COMMENT '性别，1：男，2：女',
phone CHAR(11) NOT NULL UNIQUE COMMENT '手机号',
position TINYINT COMMENT '职位，1：班主任，2：讲师，3：学工主管，4：教研主管，5：咨询师',
salary DECIMAL(10,2) COMMENT '薪资',
head_image VARCHAR(255) COMMENT '头像存储路径',
join_date DATE COMMENT '入职日期',
dept_id INT COMMENT '所属部门ID（逻辑关联dept.id）',
create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
update_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后操作时间',
password VARCHAR(64) NOT NULL DEFAULT '123456' COMMENT '登录密码'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='员工信息表';
```
优化后的员工工作经历表建表语句：
```
CREATE TABLE emp_expr (
id INT PRIMARY KEY AUTO_INCREMENT COMMENT '经历ID',
emp_id INT NOT NULL COMMENT '员工ID（逻辑关联emp.id）',
company VARCHAR(50) COMMENT '公司名称',
job_position VARCHAR(50) COMMENT '职位名称',
start_date DATE COMMENT '开始日期',
end_date DATE COMMENT '结束日期'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='员工工作经历表';
```
到这里，三张表的结构就基本确定完成了。
## 4. 让 AI 生成测试数据
有了建表语句之后，还需要准备一些数据，方便后续开发和接口测试。
可以把三张表的结构统一提供给 AI，并要求它生成符合关联关系的测试数据。
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_edc24fa530e994e4eff491eb5ed79376.png>
AI 输出结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7778d7abcec37974914def43bb4b046e.png>
这样，数据库表结构和初始化测试数据就都准备好了。
不过需要特别注意：AI 生成的数据库方案很难一次性做到完全符合实际业务。开发人员仍然需要结合页面原型和产品文档进行人工检查，确认结果能够真正支撑后续开发。
# 四、在云端创建数据库
数据库不一定要安装在自己的电脑上，也可以直接使用 Sealos 创建云数据库。
平台地址：
https://sealos.run/
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_031a418d1aaf64f736476a24e2ed59f3.png>
进入平台后，点击「数据库」。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f520cb58a62ef0bd0b5043b0252ac665.png>
然后点击「新建」，创建数据库实例。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7f640658027ab97966aca13df8c700da.png>
配置时需要注意：
- 数据库类型选择 MySQL
- 版本可以根据项目需求选择
- 名称是 MySQL 应用实例的名称，不是数据库名
- CPU 和内存按照项目实际情况分配，配置越高费用越高
- 实例数量选择 1 即可
- 磁盘空间暂时使用 2GB 基本够用
- 当前不需要备份时，可以先关闭备份功能
配置结束后，点击部署。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_86cb6fd73a91f0bb345a11f763ee1525.png>
部署完成后，平台会提供数据库连接信息，包括连接地址、用户名和密码。借助这些信息，就可以从本地工具连接到云端数据库。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_efc56f762d4bea53accb6440632a853c.png>
数据库实例准备好后，将前面生成并确认过的 SQL 语句复制出来，直接在数据库管理工具中执行。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2f53aae8bc7af2ef463f452191d49142.png>
执行成功后，三张业务表和对应的测试数据就会被创建出来。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ea18eaad47c424d230b1f28902a57c63.png>
# 五、设计前后端接口
数据库完成之后，下一步是规划前端与后端之间如何通信。
接口设计的作用是把功能、请求方式、参数、返回结果和异常情况统一记录下来。这样前端和后端就可以围绕同一份接口文档并行开发，减少沟通成本。
设计接口时，需要根据：
- 页面原型
- 产品需求
- 数据库表结构
判断系统需要哪些功能，再为每项功能规划对应接口。
同样可以让 AI 辅助完成。
比较推荐的做法是，将页面原型、数据库表结构和接口文档模板一次性提供给 AI，让它按照指定模板生成接口文档。
## 1. 部门管理接口
首先准备一份接口文档模板。
模板的意义在于告诉 AI：
- 接口应该采用什么格式
- 请求参数如何描述
- 返回数据如何组织
- 接口说明应该包含哪些内容
然后要求 AI 结合部门管理页面和数据库设计生成接口文档。
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a714da139d1d98e449d586734e5ae69d.png>
只要模板约束清晰，AI 输出的结果通常会与模板保持一致。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6b89c0b3d4ee6b45832afab9305ee813.png>
接口生成完成后，将内容复制到在线文档、Markdown 文件或团队知识库中保存，方便后续开发使用。
## 2. 员工管理接口
员工管理通常比部门管理复杂，涉及员工信息、部门关联和工作经历等多个页面及功能。
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_399a60f2df194010c452a207748707b2.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_730fc649f1d7989b3432eddfe4caa3c6.png>
如果一次性上传全部页面原型，AI 可能无法完整识别其中的内容，导致分析遗漏或结构混乱。
解决方式是：
- 将页面原型拆分成多张图片
- 分批上传给 AI
- 分别说明每张图片对应的功能
- 最后让 AI 汇总生成完整接口文档
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_566902ef429e50c18fa47db51513cff4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dab8fed83962c168c27a0ec6da43f27d.png>
这一阶段同样需要把 AI 生成的结果保存到云文档或 Markdown 文件中。
最后，将部门管理和员工管理的接口文档统一整理，就可以得到完整的接口设计方案。
接口文档完成之后，前后端开发就有了明确依据。
# 六、开始开发项目
## 1. 服务端技术选型
本项目服务端采用：
- Spring Boot
- MyBatis
开发过程中要严格遵循前面确定的接口文档，避免实际代码与接口设计出现偏差。
传统方式是先在本地创建 Spring Boot 项目，再安装 JDK、Maven 等环境。这里则可以直接使用 Sealos 提供的 DevBox 创建项目。
## 2. 使用 DevBox 创建 Spring Boot 项目
进入 Sealos 后，点击「DevBox」。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c85d37983d2db915412c2cf3b2687d5a.png>
然后选择新建项目。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0d4d58953f3eaf195d1a6f97e568677f.png>
由于服务端采用 Spring Boot，因此直接选择对应的项目模板。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3a89fec96259e3849c019ec1bf3f4f2c.png>
接着配置项目的公网访问端口和访问地址。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b94282e204cd28e5f32173a8e1e0d330.png>
确认配置无误后，点击右上角的创建按钮。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f30e9a807464b0f6d5c6bea7661991d3.png>
这样，一个 Spring Boot 项目就会在云端 DevBox 中创建完成。
## 3. 使用 Cursor 连接云端项目
项目虽然创建在云端，但我们仍然可以通过 Cursor 进行开发。
在 Cursor 中打开这个云端项目。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_11fcb446e51ffbca7a89534a77d81283.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6ef0c8aa9d322e98b62f843b9b81171e.png>
连接成功后，项目内容会显示在 Cursor 中。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_767207154a73d41bc0ba2c6d98d6bd3f.png>
这里要注意：代码和项目文件并没有真正保存到本地电脑，而是继续存放在云端 DevBox 内。Cursor 只是通过远程方式连接到这个环境，我们可以使用 Cursor 查看、修改和生成代码，实际开发过程仍然发生在云端。
因此，不需要在本地重新安装整套开发环境，也不必担心本地配置与云端不一致。
## 4. 第一次启动 Spring Boot 项目
项目创建完成后，建议先进行一次启动验证，确认 DevBox 创建的项目结构正常，服务可以成功运行。
如果不清楚 Spring Boot 项目的启动方式，也可以直接询问 AI。
例如可以描述：
> 请告诉我如何在当前 DevBox 环境中启动这个 Spring Boot 项目，并说明需要执行哪些命令、如何确认启动成功，以及常见错误应该如何处理。
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_508b3e0ec8ee940b033792c59f6751bc.png>
AI 给出的结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8c91dae96f26fe2ddd5accd4ff2f6542.png>
项目跑起来之后，我们就看到服务正常启动了
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_68f7040ea0bc513ad12a290e039e23dd.png>
紧接着我们让 AI 帮我们写一个简单的测试接口，验证一下能不能正常访问
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7516c19db9daa2d2d4ed8889197f35c0.png>
我们访问地址：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_051105c635e0e727dda0757421b88463.png>
返回结果和接口预期完全一致，到此初始化流程就算走通了。注意这里的访问地址必须用公网地址，localhost 是不行的，因为代码是在云端运行的。公网地址可以在 DevBox 里面找到
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d70366454db167f2a02820d505a40683.png>
#### 5.1.2 功能接口开发
部门管理接口开发：
前面我们已经根据原型图和需求文档，和 AI 确认好了接口文档，现在后端服务也启动正常了，接下来就按接口文档开工
我们用 cursor 来写服务端的接口，先把提示词整理好写在记事本里，再一次性复制进去。提示词里要明确 4 点：① 当前用的开发框架是什么 ② 需要操作的数据库表结构 ③ 数据库连接信息 ④ 完整的接口文档
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b385df8aac59e580928d73f28c11e4df.png>
AI 会按照提示词的要求去生成代码，代码检查没问题后就直接 Accept ALL。然后重启项目，跑一下接口看看能不能用
如果不会测，也可以继续问 AI 要测试方法
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e8836a29804d5df4ac383159a5b2fc10.png>
AI 给出的接口测试方案：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d8340b64bfd6e58d672032b0919c3ee8.png>
我们用 postman 去测了一下，结果报错了
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3b6f0b2b6833c13eb4d402c727a86888.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0c37be392142ceffd3882aec89416519.png>
把错误截图直接丢给 AI，AI 马上帮我们定位原因
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3c2dd32bd8e3c80f749198571c82a7c6.png>
原来是数据库名称写错了，改过来之后接口就通了
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7f07fd8d79a304315593b589775ba279.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_80ee8c861db9d8fe16a0ed592323ef68.png>
剩下的接口，AI 也都给出了对应的测试步骤，直接复制到 postman 里就能跑
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2768f1e45e8a1ee5c194ada1643b31f3.png>
部门管理的接口都验证没问题后，就可以进入员工管理的接口开发了
员工管理接口开发：
提示词：
这次给 AI 的提示主要包含三部分：① 员工管理模块的表结构 ② 员工管理的接口文档 ③ 员工管理的页面原型与需求文档
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cec619fc8366808f1336a84e08d75a7c.png>
把提示词发过去后，AI 就开始写代码了。写完后 Accept ALL，然后去验证接口是否可用，同样可以让 AI 教我们怎么测
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3e3758080edec5a61db8afaed526b7f1.png>
AI 给出的结果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3042a5e106caeadd804a37b9f84fd776.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2808916cdf6a6bc5abe8f495f2d59219.png>
把 AI 给的测试用例导入 postman 跑一遍，全部通过就说明接口可用
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b360082e174057953b244b6c5db60564.png>
头像上传接口开发：
这个接口涉及到文件上传，要考虑文件存哪、前端该返回什么，所以单独说一下。
头像上传成功后，需要给前端一个可访问的路径，前端拿着这个路径就能直接展示图片。
文件存储有两种思路，自己搭文件系统，或者用第三方云存储比如阿里云 OSS。现在我们用的是 Sealos 云操作系统，它自带对象存储
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_792f75b92908ea5a0c48c740e8d22cd4.png>
我们先创建一个存储桶
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5238d0474ff3199f5b1317ae177d5d42.png>
后续上传的文件都会落到这个桶里
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4ed3b56dec797042622c19de021af164.png>
建好桶后需要上传凭证才能操作，点击访问秘钥就能拿到
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_206a971addc3eccdab67f1692abf0f7a.png>
访问秘钥里公钥、私钥、内外网地址都写得很清楚
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ea3e9530093763f54df1dd5a2d5c191b.png>
存储准备好了，那代码里怎么去访问并上传呢？
这个时候就要看官方文档了
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5b02babaab89a3ae70cd6fd1959c6a8b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3449b17b107ac45cac073dae5db88b7c.png>
看完文档就能写提示词去和 AI 交互了
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0dc68ffad23c7a2ac424dc309d459391.png>
AI 帮我调整了头像上传后的返回结果，并给了测试用例：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c1c1f7ce98b69a102e0bbedd1e4a4e75.png>
把测试用例导入 postman，接口调用成功，返回了头像地址，云端存储桶里也能看到刚上传的图片
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_649de053d721724357800fe3e47d1647.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ea5094772b0b157b94af0bac6454df12.png>
到这里服务端的功能就全部开发完了，接下来开始做前端
### 5.2 前端开发
前端的开发方式和后端类似，也是在 DevBox 云端做
#### 5.2.1 创建 Vue 项目
在 DevBox 里新建一个项目
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ee385690733b7d5a80e95b4e043db99c.png>
选择 Vue 前端模板
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5299610760e7de443bd6eaab039ec717.png>
点击创建项目
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_171983ea8de9b15fe63ad7886d8e732e.png>
前端项目就创建好了
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_372e0cad10f3b14167fcd188a3edef9a.png>
然后用 cursor 打开项目
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3093e7af0a710841c6b3a06b34be0043.png>
问 AI 项目该怎么启动
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7a04ab9dac0f6e38b3b9eb89103bdf2c.png>
能看到 Vue 官方欢迎页就说明启动成功了
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3f8c245e1ae2a53f10a2d062e0532525.png>
#### 5.2.2 页面布局开发
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1a06e2735cede1a39dd7c752e9c58ad1.png>
从原型图来看，页面分为顶栏、侧边菜单和主内容区三大部分
接下来写提示词让 AI 帮我们搭好整体布局
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_05b87aa9b6cb9ed4e9d3a341298a6df1.png>
AI 生成完代码后启动项目，界面就出来了
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f18bafb99e229ff46fe8e5e68fe0edb5.png>
页面骨架到这里就算搭好了
#### 5.2.3 部门管理前端开发
部门管理前端需要从服务端取数，所以要严格按之前约定的接口文档来做。提示词需要包含：① 页面原型，让 AI 知道要做什么样的页面 ② 部门管理的接口文档，让 AI 能正确把数据展示出来 ③ 前端页面要调用的服务端地址
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_50d98915bca741986111f2cc7306d3b1.png>
不出意外 AI 会把页面写好，并且把后端数据正常呈现到前端
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ee0ed1fed1574b2b6d9bddfd96f6e5a0.png>
#### 5.2.4 员工管理前端开发
员工管理前端也需要结合原型图开发。写提示词前先梳理原型涉及哪些接口，并在提示词里全部喂给 AI
所以要告诉 AI：① 页面原型，确定样式 ② 接口文档，确定和后端的交互
提示词：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e0b6c61370a934ac4be3170151ef17df.png>
AI 完成后页面效果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d1e3e4a0bca1e67110a0de6207d41bba.png>
## 6、项目发版上线
因为全部都在 DevBox 上开发，所以上线非常简单，不用自己准备服务器、配置环境、买域名、配负载均衡
只要两步就能搞定
### 6.1 编写启动脚本
前端和后端项目都需要一个启动脚本，发版时会调用它来启动项目
#### 6.1.1 服务端启动脚本
确保文件存在，并且里面是正确的启动命令
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0553b13dd476d53ca506012aecc8db0a.png>
#### 6.1.2 前端启动脚本
前端也要有这个文件，启动时就是执行里面的命令
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_038ce91da71958afd3260213e83e7849.png>
### 6.2 项目发版上线
#### 6.2.1 后端项目发版
在 Sealos 里打开 DevBox
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_42a1cbf7a23b6bd306f3eb9039ca3ca2.png>
找到后端项目，点击右侧三点，选择发版
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dc8d7c408e2d44891677c174c2f6f187.png>
填上版本号和版本描述
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7d1a646977cc4a9539dc13146f6ead71.png>
十几秒后显示发版成功
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e029ab02619b714bee0288f0c39ceb74.png>
#### 6.2.2 后端项目上线
发版成功后点击上线。发版是确定最终给用户用的版本，上线才是部署到生产环境。点击上线
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9c1c03cb6a356a2e3d60603b67aea116.png>
可以根据需求选择 CPU 和内存，上线后 DevBox 会分配一个公网域名
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_43170f5c3c092605ac5c01b89100ea3b.png>
点击部署应用，DevBox 会自动起一个 docker 容器来跑项目
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c69e27d3029c0d924d535101ad4f4966.png>
上线完成后会拿到内网地址和外网地址
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5b751198880b66073d0dba5b0f4eaea7.png>
#### 6.2.3 前端项目发版上线
流程和后端基本一样，有一点要注意：后端上线后会有一个生产环境的地址，前端项目里要改成生产地址，不然前端还会调开发环境的后端
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8054df36e4c3e82c79a3a9f296b8528b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a6d92b8e9540ff9ee57faed4a9384f4a.png>
## 总结
暂时还没学用 claude 直接画页面原型，所以先网上找了个管理系统原型。有了原型后，如何用 AI 辅助完成前端和后端开发，重点是把这套 AI 协作流程完整跑通一次
后续会学怎么用 AI 画原型图，这样从原型图到前端页面再到后端服务就能全链路打通，一个人就能完成项目全流程。