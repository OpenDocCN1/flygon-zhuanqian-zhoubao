# 手把手教你：用手机一键把小红书商品抓进飞书多维表格



更新：现在能抓取小红书商品的最新销量数据
更新：新增手机端小红书笔记采集方案
更新：补充电脑端笔记采集方法
更新：在小红书笔记采集流程里加入视频抓取
更新：常见问题-扣子工作流执行时报 “code”: 6039 的处理
更新：扣子平台持续迭代，遇到新状况可在文档下方留言

# 开篇说明

本文核心思路是借助手机快捷指令类工具，配合扣子工作流做抓取，最后把结果写入飞书多维表格。步骤写得比较细，零基础也能跟着跑。虽然赶工完成，如果实操卡住，直接来问我就行。

小红书 App 刷商品很顺手，看到想存的就分享复制链接，通过快捷指令一键推送到飞书多维表格，对标商品收集也能省不少人工。(![](img/a9c293981c89d0aa21e9a2fd3262b341.png))

![](img/e15af93c728352d9fe7e852c0765fff8.png)

![](img/986b4d9f5a03d39619167dc7980af8a2.png)

![](img/556ffdcb0cd939f1712f0ee73ad1de9c.png)

流程总览示意

# 飞书侧准备

*   先注册登录

飞书官网：https://www.feishu.cn/

## 新建飞书多维表格

流程示意

### 方案一：快速套用

#### 使用现成模板

点开链接直接套用，表格会自动存到你的飞书空间

![](img/90fe419d1566bfd2e23001a475486c17.png)

#### 调整表格分享权限

*   修改权限设置

![](img/a9fdae715f1c29c633844157dede201b.png)

#### 核对多维表格链接

*   你的飞书多维表格链接

![](img/5459f44acec452c4273c30e0c86404ca.png)

*   确认链接里的 token 是否为 base 类型

![](img/acefb83b0973c89b3d457f45f032d0f1.png)

*   若是 base 类型可直接跳过。若不是，建议把表格搬到【我的空间】或云盘下

![](img/8553650c962f794a540494f6c0277dc2.png)

![](img/d388fd592ca6604ef001135205097dba.png)

*   说明

![](img/abdf4a0dc84a2a0ac7a492d9f58c303c.png)

#### 提取 token 与 table_id

红色字为飞书多维表格的 app_token，绿色字为 table_id

![](img/2f69bfb209859de6c5aa3e2ea70b6757.png)

记得记下自己的 token 与 table_id，后续扣子里飞书插件会用到

飞书多维表格 app_token=A27xbnXHXaDpnrsLft9c7N6An4g

飞书多维表格 table_id=tbljfQRh9edYZLp7

### 方案二：手动搭建

#### 手动新建多维表格

![](img/156e655bc16e54fca971daa0ec5f0bc0.png)

#### 清理多余行列

![](img/e1ddc9f3f874cc34602ce3170e36a1ea.png)

#### 按需添加字段

![](img/9560bec020eb103fcec0ade592e456cb.png)

#### 调整【图片】字段

链接无法直接渲染为图片，需借助字段捷径【链接转附件】实现展示

![](img/a538a6dd8f91fb0da72d307d9fa64229.png)

#### 调整【图片链接处理】字段

字段捷径【链接转附件】对超过五张图会失效，还需用字段捷径【信息提取】做二次处理

![](img/b7fe77e0ca6b663dab71d8e6fdfbf8f4.png)

#### 修改表格链接权限

![](img/8dd42eb5053683637b0d279c7417085b.png)

1.  获取表格的 token 与 table_id

红色字为飞书多维表格 token，绿色字为 table_id

![](img/3402977c266b7b2f83e30506c95e9bc2.png)

请把自己的 token 与 table_id 记录下来，扣子工作流里飞书多维表格插件需要用到

飞书多维表格 app_token=A27xbnXHXaDpnrsLft9c7N6An4g

飞书多维表格 table_id=tbljfQRh9edYZLp7

# Coze 扣子侧配置

## 注册登录账号

扣子官网：https://www.coze.cn/

![](img/40442ec207a8c2aaf0eecec751a86550.png)

## 工作流搭建

### 小红书商品采集流程

*   流程逻辑

![](img/5db7ec8e6a5be89ebeba253288914241.png)

#### 新建工作流

![](img/22d18c29442927d85e312860f4afd876.png)

*   工作流命名

![](img/7c958283e7128b3e3859eba6416464bb.png)

#### 节点-开始

把变量名改为 “url”

![](img/50f178a9b02734e4f90654ce7714d6c3.png)

#### 节点-插件-小红书-xhs_goods_detail

新增插件节点

![](img/56bda7c8ea07f3000d81eb1acca0ea1a.png)

搜索小红书，添加 xhs_goods_detail 插件

![](img/0b8e36a1c76c6ae629646c1f257657b3.png)

节点间连线方式

![](img/de4f59ac1490fb43242dc0942a5348ae.png)

选择变量值

![](img/8c10381fa436697a64c30e6deba42522.png)

#### 节点-插件-链接读取-LinkReaderPlugin

新增插件节点

![](img/3a1ffcc4b6a4e01e2b95caa585c1e64e.png)

添加 链接读取 下的 LinkReaderPlugin 插件

![](img/bdab3f2e751327ff59b9c73aafd2ad46.png)

选择变量值

![](img/9521266204d52dc9fc89b72ee9d65002.png)

#### 节点-代码

新增代码节点

![](img/56b585a9febd67fd340ccc3e1aa55427.png)

选择变量值

![](img/9fb8871c57f84b4e82e6f39bf734017d.png)

填入代码

![](img/b2cf70a0190e3dee78823b5c647cd65c.png)

代码内容：

需复制请打开：

```
async function main({ params }: Args): Promise {
    const input = params.input || ''; 
    const regex = /已售\S+/; 
    const matchResult = input.match(regex);

    const ret = {
        "key0": matchResult ? matchResult[0] : "" 
    };
    return ret;
}
```

#### 节点-代码1

再新增一个代码节点

![](img/7a5025a459933c32730f7edacfca0151.png)

![](img/4ac0cd4566b753f6f1abb4540b0db780.png)

新增变量，变量名请参照下图修改

![](img/6688070dc14e699dce359b5b0f4c395c.png)

具体变量值请对照下图选择，xhs_goods_detail 输出对应的变量名如下：

![](img/35db3e7bbb29aef56b04a7a7c1d96667.png)

![](img/b4f74785b1f2b45d9bbb5d93740483d2.png)

变量名 sales 对应的值

![](img/7a4b708151f03bcdb2cfc81df3535419.png)

变量名 url 对应的值

![](img/aef59d93bc557af569be2459667ae69c.png)

*   填入代码

![](img/325aa7860edebcd8604939bbd491df38.png)

代码内容：

需复制请打开：

代码中文字需与飞书多维表格字段标题一致，如需改动请保持对应

```
async function main({ params }: Args): Promise {
    // 构建输出对象
    const list = [
        {
            "title": params.title,
            "name": params.name,
            "fans_amount": params.fans_amount,
            "seller_score": params.seller_score,
            "price": params.price,
            "deal_price": params.deal_price || '',
            "images": params.images,
            "sales": params.sales,
            "url": params.url
        }
    ];
    let records = [];
    for (let item of list) {
        let record = { "fields": "{}" };
        let fields = {};
        fields.商品名称 = item.title;
        fields.店铺名称 = item.name;
        fields.粉丝数 = item.fans_amount;
        fields.店铺评分 = item.seller_score;
        fields.销量 = item.sales;
        fields.售价 = String(item.price);
        fields.到手价 = String(item.deal_price);
        fields.图片链接 = item.images.join(','); 
        fields.商品链接 = item.url;
        record.fields = JSON.stringify(fields);
        records.push(record);
    }
    const ret = {
        info: records
    };
    return ret;
}
```

#### 节点-插件-飞书多维表格-add_records

*   添加插件

![](img/0c1098425c04e289398eb363b5c69c06.png)

*   搜索飞书多维表格，添加 add_records 插件

![](img/6383416b311a727df585d896ac3006a2.png)

*   填入自己的飞书多维表格 token 与 table_id

![](img/4cb3134372318f10d39e200832c9807a.png)

*   变量名 records 对应的值

![](img/58e81331e091f31f0c4f4d9f2dde589d.png)

#### 节点-结束

*   结束节点仅用于收尾，对变量名和选择值无要求，前一步已完成写入

注意

新手建议按下图选择变量值，便于排查问题

![](img/0f5b089cde3ab6580796f6bbc22c1304.png)

#### 工作流测试

*   试运行，粘贴商品链接测试（商品链接获取：小红书 App-分享-复制链接）

![](img/578855e25ebdad8c5f7d2ebc0ae4ac3a.png)

*   首次运行会提示授权失败，请复制链接到浏览器完成授权

![](img/3d72ea58fded648480ff52aadc4cfe58.png)

![](img/b4095ac3781ada9e0a6ec465b9423fce.png)

*   授权成功后，多维表格会同步更新数据。测试通过后发布工作流

![](img/0d8b6b439dbcdaaf162f544d23ab9f53.png)

*   记录工作流的 workflow_id

![](img/72e8476347d30c192231ca6085843505.png)

红色标记处即为 workflow_id，请保存

workflow_id=7492048120039358483

## 生成个人访问令牌

1.  新建令牌，用于手机端调用扣子工作流

![](img/f753dd1bee98816909f6daaf48b23bee.png)

1.  有效期建议不超过 30 天，权限选工作流，空间选个人空间

![](img/8c5e0357afc9d3dac69f8626684eea98.png)

令牌只显示一次，未保存请重新生成

![](img/edf7f252bc5b6dbe0db60dc2c543dae2.png)

红色标记为 token，请妥善保存

token=pat_iOgnznoTzJUJCUTSpmzWXjzGXRczmOacFuQBdE6uoEKSsiayVrpajpjWKKSSLSMT

## 验证扣子 API 执行

1.  在扣子 API 中选择执行工作流，验证 token 与 workflow_id 是否可用

![](img/7250e907fd5b11ed7847aca640f68f03.png)

1.  填入个人访问令牌、workflow_id 及 parameters 参数

![](img/920db0870d36328ecc1c6ac7ed64f2eb.png)

Parameters 格式示例

*   url 为开始节点的变量名

```
{"url":"填入小红书商品链接"}
```

注意

出现飞书未授权的情况，请复制括号内网址进行授权，如下图

![](img/a0c01c0daf5af8ecbc0c1e547cb1ba8f.png)

# 手机端采集实操

## iPhone 用户

iPhone 可用自带快捷指令实现一键采集

### 快捷指令配置

指令已整理好，通过浏览器打开即可获取

https://www.icloud.com/shortcuts/c4ef07994b7649c1b97fe68bb209f7ac

1.  获取捷径并导入快捷指令，调整设置

![](img/89076d55d21ac85226af859996f04ac6.png)

1.  修改小红书商品采集相关设置

![](img/e2bb8aa5cfdadaf31d413174d0d3edd6.png)

1.  只需改动 Authorization 与 workflow_id 两个位置

![](img/b674ab445b009ea3422dbfa8b9cf100f.png)

红色部分替换成自己的 token 与 workflow_id，注意格式

```
Authorization=Bearer pat_iOgnznoTzJUJCUTSpmzWXjzGXRczmOacFuQBdE6uoEKSsiayVrpajpjWKKSSLSMT

workflow_id=7492048120039358483
```

### 触发方式设置

1.  打开辅助触控

![](img/cec455a2689537eaf9f1ada4440b263e.png)

![](img/6c8f98c11aaaddcba9dc2c6693a52ed1.png)

![](img/a4110d4e188ed8996af50ca37ac4e0e7.png)

1.  选择喜欢的触发方式

![](img/36aa75446ee7e52c7d6485152af0c9c7.png)

1.  例如轻点两下

![](img/657f2b0b58a02ccd72cbd5aefee5c041.png)

1.  例如小圆点顶层菜单

![](img/387b6d8281185e55946bbf1853457311.png)

1.  iPhone 8 及以上可设置轻点背面

![](img/dcaec566cc117091af05d1d0eafe21a4.png)

![](img/4543ef4c0439723aaf2bb1b7e48262a5.png)

### 一键采集演示

在小红书商品页，点击分享-复制链接-触发快捷指令

![](img/d1fde8b286e167e95605184a772d4eb0.png)

![](img/1a06d36075bfb80fb61be999d79f83b3.png)

![](img/49fab793ee760b8210ce4d90d3491cc1.png)

## 安卓用户

安卓可借助第三方自动化工具 Macrodroid 实现一键采集

MacroDroid 是一款基于宏任务的手机自动化工具，操作界面干净简洁，上手门槛很低。引导式的配置流程让你一步步完成设置，宏列表会清晰显示总数，点击即可查看详情并进行删除、复制等常规编辑。当你新建宏时，系统已内置多种开关操作可供直接调用，也支持从零自建。

*   先安装 MacroDroid 应用

整个自动化都依赖宏的设定，下面提供两种搭建思路：一种是直接导入已搭好的宏模板，只需改动关键参数即可使用；另一种是完全手动从零配置，一步步完成触发与动作的设定。

### 方法一（导入现成宏）

1.  导入宏文件

宏文件如下 ：

![](img/d54af03f21eb29bbf9f31b99eafe0674.png)

![](img/4e4be6788a6061b04aa74654b8b0b2f8.png)

1.  开启权限

运行期间会提示需要授予“显示在其他应用上层”的权限，请同意授权

![](img/6eb8bb563881c2fca8c7dc11edfe7d14.png)

1.  进入 HTTP 请求并打开配置界面

![](img/fb8cf409953c8ac2fdf567d28bc70f15.png)

![](img/5bfe50011638a47bd4e2792ce6f8f47e.png)

1.  编辑请求正文

![](img/77da3c51fc1342173c837a31af70acd8.png)

正文代码如下：

```
{
  "parameters": {
    "url": "{v=商品链接}"
  },
  "workflow_id": "7492048120039358483"
}
```

1.  修改请求头信息

把 Authorization 替换成你自己的扣子 token

![](img/5d9339208d4ba2cdb744b7ea347f26cf.png)

Authorization 写法示例，请将红色部分换成自己的扣子 token

```
参数名称：
Authorization
值（红色部分换成自己扣子的token）：
Bearer pat_iOgnznoTzJUJCUTSpmzWXjzGXRczmOacFuQBdE6uoEKSsiayVrpajpjWKKSSLSMT
```

设置完成后别忘了保存

1.  进行测试

![](img/ff39be9a9c9f36bb800b28c1adfae613.png)

![](img/64a21a5eef40a66a86348db6cd3935b2.png)

到此结束

### 方法二（手搓宏）

*   流程概览图

#### 新建宏

![](img/201bfacf17137483a020e3cec0c89307.png)

#### 配置触发器

![](img/76eac6ac4838b3a97c1c68e41f86c869.png)

![](img/ba80b0b20600cfdd5b6f1da852196977.png)

![](img/bef469506ec313b9633b25b5cc3aadff.png)

![](img/45fe00dcac835e937182a56b744e24bc.png)

![](img/12d7831c6bd045797e918cd773900ad4.png)

添加动作

#### 添加动作-刷新剪贴板

![](img/d2f64fc0820d75495ebffd7a75667b09.png)

![](img/99bda913aca9d58311b1b69e9942bd8d.png)

#### 添加动作-设定变量

*   将剪贴板里的内容保存为商品链接变量

![](img/3a0bc5b8b98d3050ef6d103bd24aa79a.png)

![](img/af5ead98654328546f49d6ee16d2f402.png)

![](img/df6b86675721d66731d1af87fecff844.png)

![](img/896d63e17ae90246f1349e9bcc34520c.png)

![](img/d5d010deef2a12d7c763c4e334b275b5.png)

![](img/231cb00ebb8ca276ed9a698e982f4d35.png)

#### 添加动作-条件判断

*   判断剪贴板内容是否包含小红书商品链接

![](img/7a9831e1cb439cf472ae3024a09e68a5.png)

![](img/8778e250bc32d75d2a9fed982247f742.png)

![](img/41fddc81f909c978a1eeb050e2faeaf0.png)

![](img/9b6c1f15c39a7956ef650316551bc161.png)

![](img/636f769735c0e7b85434e3ffc0625d1b.png)

![](img/86cc514c56bc68b9591974b1f9c90bca.png)

![](img/62e4e51380a7709664441e0f0f15eb21.png)

![](img/a0b9cfba4eaf5341cc3ff5cebc8048b2.png)

![](img/467d121afb62a172ca20bd8bffd2f672.png)

#### 为【如果】添加子动作

*   新增 HTTP 请求，按要求填入各项参数

![](img/a7104111decb9c1831d29e16e3824428.png)

![](img/f09edcbe5107de53d8a91bd850f32159.png)

![](img/6446e0945a215f8cf49a7c12aab7b167.png)

![](img/b3848640e657aa972af7d63c6166b544.png)

![](img/969ab6249bf3ac613abd15d40cd424da.png)

![](img/615c29810a06f717488abe115a7220aa.png)

![](img/ab4d6d1f0f985034e1b409b9afce6cc6.png)

![](img/d5e486099c2ca39eef5a0dfe9e77a0e0.png)

![](img/f607343fccf9235d91db3a32aadaf67e.png)

#### 为【如果】添加子动作

*   新增 JSON 解析，用来判断返回内容

![](img/e08a2b9807ca7a860923b78be0e87e98.png)

![](img/335d06ddedbf5a2b637d6fe3d701bd37.png)

![](img/c3ad2b40f5de71ed4b23f31ca6554c31.png)

![](img/1af1986ea4e5e4afe6f8b5e700368419.png)

![](img/1e4a86d6c82f98ca43c7da79b023e755.png)

![](img/6751a044839fc644d13adc9060884bc0.png)

#### 为【如果】添加子动作

*   再包一层判断，校验扣子返回结果

![](img/211836592a38266b7b80c4b978ec0252.png)

![](img/e96556d135354a290dede2d28ad48064.png)

![](img/a412f737f5e4826e4b4fdd53d0a48c70.png)

![](img/ea33e714aecb896d98f57bd64be24c3d.png)

![](img/0274c2dcd486a7c40e3140828da0f9d6.png)

![](img/330cc1220fd84c46387ef2d00779a608.png)

![](img/0d7acb58d4ca83daafa4106d2abe7505.png)

![](img/80cf02b089f66c4df49fca4ec4a14890.png)

![](img/4e84d00bc6bb6f153f5240884efab58e.png)

![](img/dc7eb241645f30e1bee6dd37b1e50bfb.png)

#### 为【如果】-【如果】添加子动作

*   条件满足时弹出“保存成功”提示

![](img/1f00db4fb8fb151c0c29a4a30480f483.png)

![](img/bdc3d3997b0a3e12677b60358a25ef79.png)

![](img/9792a63bcb2d11c218489b590b895eba.png)

![](img/dfd29813ce2a6f8ae23321bfe7cf72d2.png)

#### 为【如果】-【如果】添加【否则】分支

*   新增否则分支

![](img/c71d9987431b76f896f472b1cdaeb931.png)

![](img/6be4aee658e29412a8e69386db1490b8.png)

#### 为【如果】-【如果】-【否则】添加子动作

*   条件不满足时弹出“保存失败”提示

![](img/628bfc4a57cc2fe2b5af25029a739f32.png)

![](img/2ef04357f06b8af8492ea261bce1022f.png)

![](img/32fa1d0b40d2b06dcf7d0c99d85174be.png)

![](img/c42867e295c6ae37b845dacc427b9ee9.png)

#### 为【如果】添加【否则】分支

*   新增否则分支

![](img/f86d3c0f04988f48ba6c4f724289c63f.png)

![](img/518c4aa7052e192b5051f82ceae84989.png)

#### 为【如果】-【否则】添加子动作

*   当链接无效时弹出提示

![](img/2d31e58181033a40d15f4e684d55f4bf.png)

![](img/eaf0ea2ebee07d80cbecf40445105ad8.png)

![](img/f55f5761b05dd8b88c4eb815cc89407b.png)

![](img/0971c6f749b1ff6c19f029c71fc6167f.png)

![](img/5d72b3f51a7f7a4a7610292f1817cc8f.png)

# 更新日志

## 获取小红书商品的实时销量

在原有商品信息抓取的基础上，加入新增销量追踪。首次采集的销量会固定，后续可通过新增字段去抓取实时销量，两次采集的差值即为销量增长量。

采集完商品信息后，若仍想用之前的飞书多维表格记录销量变化，可新建一个智能体并发布为飞书字段捷径，在表格中挂载该捷径获取最新销量，再用两次时间点的数据算出增量。注意部分商品可能无法获取销量。

![](img/e1b84541b179dbb185436c89a89e6822.png)

### 创建字段捷径

#### 新建扣子智能体

*   打开扣子平台

![](img/12e5c553415f19604ba77d952812d682.png)

*   给智能体命名

![](img/8e0ed53f5d8ad888f808fdaf96c0f9e9.png)

#### 新建对话流

*   选择对话流模式

![](img/2986fb85f3d209ef0f8b14487e54533b.png)

*   添加对话流

![](img/47faff33d4bc70b88b07406dc8479e29.png)

*   生成对话流

![](img/da7a5e523cc68fcb9db5af2ab109aa7c.png)

#### 添加节点-链接读取-LinkReaderPlugin

*   新增节点插件

![](img/144584b07bcbe9f82c3b0b465fb4d924.png)

*   插入 LinkReaderPlugin 插件

![](img/f64db564255559ac90c59bd1907c6333.png)

*   指定变量

![](img/ec2cf4988b1c9c293cf5c1ac5a859623.png)

#### 代码节点

*   新增代码节点

![](img/9200bb0683f52d226b8ed0305590d633.png)

*   指定变量

![](img/506b62b5fdd30f3731fb1ca5300820ed.png)

*   粘贴代码

![](img/b8ab72d3802b78c6e7e6935ad0cadbf1.png)

代码如下：

复制请打开：

```
async function main({ params }: Args): Promise {
    const input = params.input || ''; 
    const regex = /已售\S+/; 
    const matchResult = input.match(regex);

    const ret = {
        "key0": matchResult ? matchResult[0] : "" 
    };
    return ret;
}
```

#### 结束节点

选择变量输出

![](img/cfa7ae7736dfccc9fe7d9e9ca0d6675b.png)

#### 试运行

![](img/b5557430ae0e4cf96fc662e6350dec11.png)

*   输入商品链接进行测试

![](img/2262c587602463ac3e8ac4a3602e32f0.png)

#### 发布对话流

*   点击发布按钮

![](img/f4313529d8efd81ed3532ea81a1aab4d.png)

*   加入到智能体

![](img/3d02ecb8033f350f757e7dd29a80c790.png)

#### 发布智能体

*   点击发布

![](img/9d8b97dbac65a63d79a62fc64cfe1aa2.png)

*   跳过开场白

![](img/949087b1c082a22c07a45d99f7407c7c.png)

*   选择发布平台

![](img/9d65ecfb3d9e839121549af65b79664d.png)

*   授权并配置多维表格

![](img/0f01ec8e7903cb0eaf9f44e2b77f32bd.png)

*   填写捷径信息

![](img/26cc3ec4260d5086ae9e217e710e5024.png)

*   提交审核

![](img/7ffbae3b37988b3a563da3c3456d8a0d.png)

*   确认发布

![](img/f36f27351d7738b16ea0c349ce903685.png)

![](img/0426444be6278b303a4171f3c347140a.png)

智能体审核需要等待一段时间

### 修改多维表格

#### 方法一（套用模板）

可以直接套用模板，但模板中【最新销量】字段里的捷径需替换成你自己发布的智能体。操作细节可参考方法二。

![](img/b9b4d2e4f2c81b84cc661ec3d7ab3263.png)

#### 方法二（手动调整）

##### 新建字段-采集时间

*   记录首次数据生成的时间

![](img/82b8e7413c475e5d946d38560e0049ba.png)

##### 新建字段-最后更新时间

*   记录最近一次更新的时间

![](img/7c943a4ccc9e160696afed41d53ea5aa.png)

##### 新建字段-最新销量

*   用于获取最新的销量数值

![](img/625a6cd7072b51a8124e8e44ed558f36.png)

##### 新建字段-处理销量

*   提取销量中的数字便于计算

![](img/5c33b8c8b64fa916fd191a4adec29cb7.png)

##### 新建字段-处理最新销量

*   提取最新销量的数字便于计算

![](img/ce6e002a97533837573933749bb54614.png)

##### 新建字段-增加的销量

*   计算销量增量

![](img/cc031a8818ade524d1e723c333aca952.png)

##### 调整顺序与隐藏

*   为了界面整洁，可调整字段顺序并隐藏不常用的字段

![](img/cb185644542cd6a09bc13b68f27b539a.png)

### 测试

*   用之前的手机快捷指令进行测试

## 小红书笔记采集

![](img/7440e79e64dd867381ecf2fe5094a860.png)

### 飞书多维表格

#### 新建多维表格

直接套用现成模板即可

打开链接后模板会保存到你的飞书空间

![](img/dcaaa656f61f6c4216dd7d044967816f.png)

#### 修改多维表格分享权限

*   调整权限设置

![](img/c2074bfeb2561f80f2ab5576ed679f91.png)

#### 核对飞书多维表格链接

*   多维表格链接

![](img/032250911c23b9246a9c8cb50307685f.png)

*   检查链接中的 token 是否为 base 类型

![](img/7932bd7cd04cc919f7842789fcca574e.png)

*   若为 base 类型可直接使用；否则请将表格移至“我的空间”或云盘

*   补充说明

![](img/4ad76de04bdd8191a9c00fa92e67bf4c.png)

#### 多维表格的 token 与 table_id

先看飞书的 Base 控制台（也就是多维表格），其中有两条关键信息需要记住：文字标红的是访问令牌（app_token），文字标绿的是数据表ID（table_id）。动工之前，务必把这两项保存到自己的备忘里，后续接入 Coze 时几乎处处要用。

![](img/80e622cce03ed1529483782392967536.png)

这里把两个值单独列出来，方便对照：app_token 那串为 L9eLbhW46aH1SRs0vLtcAPxJn2b；table_id 那串为 tblyv2CsIXIl9CsG。

### 模块一：Coze 流程搭建

**第一步：新建流程**

登录 Coze 工作台，从首页创建一个全新的流程项目，并填写你喜欢的任务名。

![](img/0d68f12bb70b4cfa2aad9c4e8e15ea07.png)
![](img/32e28d2a1f21bdad7ace9a24039eff93.png)

**第二步：调整入口参数**

把起始步骤的参数改名为 url。这个参数将承载外部传入的笔记地址。

![](img/269dee006c6464c2c3be02d58cc54240.png)

**第三步：接入链接解析扩展**

在扩展组件列表里找到 get_url，引入后它会自动从分享文本中还原出可访问的页面地址。为了让它知道该处理什么，把 url 指定为它的输入源。

![](img/7042a345f6ab341d4657470cfd591bfa.png)
![](img/788f97f0628fe7d2ace5b69a9985c28f.png)
![](img/f853e36cf459e7fdce975d2952b8ee20.png)

**第四步：接入详情解析扩展**

再装入一个 get_note_detail，这一步负责将该笔记的标题、正文、图片等结构化信息整体抽取出来。它的输入源同样选 url。

![](img/dda76b3a14fd295db333dafc5ca287d8.png)
![](img/15bd630b951bdc76d450499d9e1c90f9.png)
![](img/f668ba07fc7c30b998f673a6e6cc871a.png)

**第五步：插入自定义脚本步骤**

在画布上加一个脚本块，作用是格式化前面的输出，使结果符合表格写入的预期格式。先声明接收数据的变量，再把下方脚本贴进执行区。

![](img/7da3c434955e9c35f309154840a5fe37.png)
![](img/3f5dfb09c5caec2677c7300773ab70f5.png)
![](img/dc10dc52af143de4317a907eaab00d68.png)

```
async function main({ params }: Args): Promise {
    // 构建输出对象
    const list = [
        {
            "title": params.title,
            "author": params.author,
            "content": params.content,
            "publish_time": params.publish_time,
            "location": params.location,
            "like_count": params.like_count,
            "collect_count": params.collect_count,
            "comment_count": params.comment_count,
            "share_count": params.share_count,
            "author_page": params.author_page,
            "url": params.url,
            "images": params.images
        }
    ];
    let records = [];
    for (let item of list) {
        let record = { "fields": "{}" };
        let fields = {};
        fields.笔记标题 = item.title;
        fields.博主 = item.author;
        fields.文案 = item.content;
        fields.发布时间 = item.publish_time;
        fields.地点 = item.location;
        fields.赞 = item.like_count;
        fields.收藏 = item.collect_count;
        fields.评论 = item.comment_count;
        fields.分享 = item.share_count;
        fields.博主主页 = item.author_page;
        fields.笔记链接 = item.url;
        fields.图片链接 = item.images.join(','); 
        record.fields = JSON.stringify(fields);
        records.push(record);
    }
    const ret = {
        key0: records
    };
    return ret;
}
```

**第六步：连接到 Base 数据表**

在集成市场中以“多维”为关键词搜索，即可定位到飞书官方的 Base 插件，随后调用 add_records 能力。将第一步记录的两项凭据填入相应配置项，并把记录来源设为脚本块输出的 key0。

![](img/f2376c222dbed2193be909558f1ba3b2.png)
![](img/31a168dbb795b42144dc8c56d6984839.png)
![](img/1192274c5f2620891ecd87fbed29b42b.png)

**第七步：配置收尾动作**

在流程末端挂一个结果节点，用于返回运行信息；这一步没有什么特殊要求，按自己习惯选择即可。

![](img/9645ee9c77f9e7ab98c0983630286895.png)

**第八步：试跑并上线**

先点“试跑”，在 App 的分享面板里复制出笔记的公开地址，将它贴到入口处跑一遍全链路。

![](img/6ed5d00316f97bb3cedd70418767449d.png)

如果运行正常，Base 表格里应该会出现对应的新记录；确定没问题后，把流程发布出去。

![](img/9dd3b7a2dfc901d93101fe080cb0e597.png)

### 模块二：用浏览器扩展批量收录笔记

想在电脑上高频收录内容，可以给浏览器装上 Tampermonkey 扩展。它对主流浏览器的支持都比较完善，包括 Chrome、Edge、Safari、Opera Next 与 Firefox。

需要说明的是，很多人把 Tampermonkey 和 Greasemonkey 混着叫，其实后者是 Firefox 平台上一款单独的扩展，作用并不完全一样。手机端也有现成的捷径方案可以直接使用，这里主要展开电脑端的做法。

动手前请务必记住：先确保 Coze 流程能被 API 正常驱动，因为浏览器端也要借助 API 才能触发流程执行。

**第一步：装好 Tampermonkey**

打开浏览器的扩展商店，搜索 Tampermonkey 并安装到当前浏览器。

![](img/2e91331541a6842e05006d5c1a4f54b3.png)
![](img/d883327c97b6dd2f7f0278adcf987578.png)

**第二步：改两个参数**

进入 Tampermonkey 的脚本管理页，打开脚本源码，找到 workflow_id 和 Authorization 两处：前者替换成你自己的 Coze 流程ID，后者替换成你自己的 Coze 令牌。

```
workflow_id: '7499044907908628489'
'Authorization': 'Bearer pat_QhNwAtHQ1DC9m8o1MWDAp44t2JfV1ffmfBl6Bbz9Mi4Mn0goMYCAmThha01nS123'
```

**第三步：粘贴脚本**

新建一个用户脚本，把整段代码完整填入，保存后等待生效。

![](img/41c5d19416ec2e3f0c418df451060f47.png)
![](img/87630c84b3f30e44d9d0d79ce8160584.png)
![](img/1ae0bc52f02dbcc809386c590fac3050.png)

**第四步：抓一条试试**

找一条笔记做验证，确认能成功抓取到内容。

![](img/186511691e70b23449393e379e031d36.png)

### 模块三：给流程增加视频保存

若想把视频一并收下来，在原有的图文收录基础上扩展几步即可。

**第一步：挂视频扩展**

从扩展库中找到视频解析类组件并挂载到流程中。

![](img/d934ff7e9f85603ec352501a953d9160.png)
![](img/f8e5a06041f900ff744482bc27878819.png)

**第二步：设好扩展的入参**

把视频解析组件所需的参数与上游传下来的视频地址对应上。

![](img/b3e7e9c862a6228605006ad1f280721c.png)

**第三步：在脚本块里补输出**

找到脚本块，为其新增一个输出变量，专门存放视频的访问URL。

![](img/28fb892d1dfb47ac412dc0e8356af663.png)
![](img/4fe3d06988941c12bc9d1fd661208b91.png)

将脚本内容调整一下，让新变量随流程一起输出。

![](img/2be54fde14f7ca7a9e2278a800d19370.png)

**第四步：重新发布流程**

脚本调整完成后，对流程做一次重新发布。

![](img/94b26f76c0c2a1a29821107c1b1b750d.png)

**第五步：扩展 Base 表结构**

回到 Base 表格，新增一列字段，命名为“视频链接”字段，用来存抓取到的地址。

![](img/5a3740709e0231fec11904f20d9d7841.png)

再新增一个“视频”字段，这样表格里就能直接预览视频内容。

![](img/3eb19df5427f7e8f287c3abf526d6be0.png)

最后重跑一遍测试，看看视频能否正常保存。

![](img/691145e7aeadb172ee5b3add750297f1.png)

### 模块四：报错处理速查

遇到报错时，先对照以下常见情形：

- 入参缺失或命名不对，多半是参数没写对；
- 传入的数据结构和预期不一致，确认一下字符串和数组的用法；
- 提示授权验证未通过，多出现在用 API 调用的时候；
- 返回 “code”: 6039，建议直接查询官方错误码说明。

错误码查询入口：https://open.feishu.cn/document/home/index

![](img/0def0eda21a6bf87e3f26235bb8111d6.png)
![](img/b6cc57cd48d5105d510682c35637df17.png)
![](img/69a2268a540df3e90350055f661d4a3e.png)
![](img/3f80be2eadc9637be855c78047ca1c70.png)