# 零基础实操：用 n8n + RSS + 飞书搭一个跨平台热点选题库

前几期我已经手把手带大家把 n8n 部署好、把公众号自动发布的流程搭起来、甚至连自动排版都配完了。没跟上的同学可以翻回之前的长文，都是上千字的实操拆解，建议先收藏再慢慢练。

发文的自动化有了，下一个痛点就来了：到底写什么？

我自己的选题习惯就是每天刷各大平台热搜、再看看行业新资讯，看有没有能用的角度。但一个个平台点开查太费时间。

能不能把不同平台的热搜、自己关注的资讯全部聚合到一个地方？答案是可以。今天就用 n8n + RSS 给你建一个专属的选题池。我已经把它集成到自己的工具里了，现在直接在软件里搜关键词就能找到素材，一键生成文章。

因为大多数朋友没有自己的网站，这次我就把最终结果直接沉淀到飞书里。

![](img/zhuanqian_d108c563b3bd5549498473c448b2161d.png)

开始搭建！

## 一、先放一个定时触发器

今天的起点是定时触发节点。点【添加节点】搜索 schedule，选择它。这个节点负责按固定时间唤醒工作流，测试阶段可以随便定一个时间点。

![](img/zhuanqian_e4726fa7c0c3ffa6159d134971751e51.png)

## 二、接入 RSS 源

接下来加 RSS 节点。虽然它能直接订阅支持 RSS 的网站，但国内很多站点并不开放 RSS 订阅。可以去找别人搭建好的 RSS 地址来用，条件允许的话也可以自己做，但那又是另一套技术了。

文末我放了一个开源的 RSS 地址合集，大家可以自行挑选。

演示就用两个源：

![](img/zhuanqian_31a0025fcda5f2672e19d15ecf9e6262.png)

点进节点配置订阅地址。

一个是百度热搜：https://rss.aishort.top/?type=baidu

一个是微信最新文章：https://rss.aishort.top/?type=wasi

需要更多内容就多加几个 RSS 节点，多配几条地址就行。

![](img/zhuanqian_eba8c5e2decb3826edd1fed785f26faf.png)

跑一下测试，能看到成功拉取到数据，一个返回 100 条，另一个返回 10 条：

![](img/zhuanqian_42f28c2c213bef49c6efbeae8b828e6c.png)

## 三、给数据打上来源标签

为什么要预处理？因为直接拉回来的数据结构可能不统一，字段也不全。比如现在两个节点的输出长这样，如果直接丢进飞书，后续根本分不清这条是哪个平台来的，节点一多就更乱了。

![](img/zhuanqian_7f5c615e234d648132c10eefb45cbc6a.png)

所以我加了两个 Code 节点做清洗。

![](img/zhuanqian_4ab1f34efe120aa69a78a2823c68dd76.png)

在代码里给每条数据额外加一个 Source 字段，用来标记来源。代码逻辑就是遍历返回内容，给每条都加上来源标识。

![](img/zhuanqian_dd27296774e34699920e475d9e9b3059.png)

执行后就能看到数据里多了一个来源标注，后续每个订阅分支都用不同来源区分，清晰很多。

![](img/zhuanqian_52f7bb2b33ef04bdb705629fcc5e298f.png)

## 四、把多条分支合并起来

多个 RSS 拉回来的数据要统一处理，得先合并。用 Merge 节点即可，把不同分支的输出都连进来。

![](img/zhuanqian_5943da0c6366f17787af84f9fa9e82f5.png)

设置里选择模式为 Append，下方的数字代表要合并的分支数。订阅源越多，这个数字就要相应调大。

![](img/zhuanqian_98c460e964cfe1c0343a73adcbdd04ce.png)

执行后可以看到所有项目被聚合成了一条流。

![](img/zhuanqian_3779e8c0c5d6d1d5b7f93d50ab2d913e.png)

## 五、做时间过滤

数据量大了就需要筛选。比如只保留 1 天内的新鲜内容。合并节点后接一个 IF 过滤节点。

![](img/zhuanqian_06f3cc7bd48d8fabe266887e6831d1d7.png)

过滤条件可以这样写：

![](img/zhuanqian_38785adcd4bb68ed125b097c47b70436.png)

其中 `new Date(Date.now() - 1 * 24 * 60 * 60 * 1000)` 代表 24 小时前的时间点。不太会写的话直接让 AI 生成条件即可。设置完再跑，就能把旧数据筛掉。

![](img/zhuanqian_c085ba37fc40e43dd846ce73becfc27b.png)

## 六、聚合为单条项目

重点来了。批量获取后，如果项目数量是上百条，n8n 会对后续节点做批量循环执行，一次跑一百次，很容易触发频率限制。我之前就踩过坑，把 HTTP 请求放在后面，结果被限流了，明明没循环却一直报错。

如果不需要逐条处理，像我们这种要把所有内容打包成一个 JSON 一次性写入飞书表格的场景，就要先聚合。

用 Aggregate 节点把前面多条记录合并成一个变量。

![](img/zhuanqian_f80306f658f5914cc1e9a9fbaf089831.png)

按示例配置后执行，画布上就只剩一个项目，所有内容都集中在 data 字段里。

![](img/zhuanqian_1087b6b8eab9bc587599756e9864e796.png)

## 七、写入飞书表格

### 1、装飞书社区节点

写入飞书需要社区版的飞书节点，功能覆盖飞书大部分操作。节点地址：

https://www.npmjs.com/package/n8n-nodes-feishu-lite

复制安装命令后在 n8n 设置里的社区节点安装即可。

![](img/zhuanqian_23310ac094873663d8ef638fdf693e94.png)

![](img/zhuanqian_ddd76073e9769cfeabb84bffb7a24016.png)

### 2、配置飞书凭证

安装完要创建飞书凭证

![](img/zhuanqian_acf6a366831d1184abd0f7c5f130f201.png)

![](img/zhuanqian_1c16b30aa7908fa63ecf2965bbd32109.png)

需要填入飞书的 AppID 和 App Secret。不会获取的同学可以看我之前的飞书教程，页面可能更新了但流程一致，拿到后保存即可。

![](img/zhuanqian_c166c75d3f7bf218669fe492c286e113.png)

为了让 n8n 能自由创建和编辑表格，还需要给应用分配文件夹权限，具体操作见官方文档：


### 3、创建每日表格

准备工作完成后，添加创建电子表格节点。为什么不直接写表？因为我想让工作流每天自动生成一张新表，按日期存档。

搜索 feishu 添加创建表格节点

![](img/zhuanqian_dc4705c98298a578039125f4ab44f6cb.png)

表格标题可以用今天的日期，代码示例：

```
{{ ((d) => `${d.getFullYear()}年${(d.getMonth()+1).toString().padStart(2,'0')}月${d.getDate().toString().padStart(2,'0')}日`)(new Date()) }}
```

File Token 就是前面授权后的文件夹打开对应的 token。

![](img/zhuanqian_f77b2bb0564be39e991ab7a75c34324d.png)

执行成功会有创建成功的返回。

![](img/zhuanqian_18778b5cb91bd652ea4e8ed1d097f7ae.png)

### 4、写入数据

最后一步是写数据。先加一个获取工作表节点的节点，因为一个表格里可能有多个表单，需要先拿到当前表单的 ID。

![](img/zhuanqian_2a112319308e14891adab8ab4eb3ad7e.png)

![](img/zhuanqian_a8daf00c5a5df6de5a740e35264f7bd4.png)

飞书对数据格式要求比较严格，需要用 Code 节点把 JSON 重组为它能识别的格式。

![](img/zhuanqian_e79a780593e6b6864b7b35a1601a5158.png)

代码示例：

```
// 转换函数
function convertToTableData(data) {
// 表头（固定）
const headers = ["标题", "链接", "发布时间", "内容", "摘要", "来源"];
// 数据行
const rows = data.map(item => [
item.title || "",             // 标题
item.link || "",              // 链接
item.pubDate || "",           // 发布时间
item.content || "",           // 内容
item.contentSnippet || "",    // 摘要
item.source || ""             // 来源
]);
// 返回：表头 + 数据行
return [headers, ...rows];
}
// Add a new field called 'myNewField' to the JSON of the item
// 原始数据
const inputData = $('Aggregate').item.json.data;
console.log(inputData)
// 执行转换
const tableData = convertToTableData(inputData);
// 打印结果（可在控制台查看）
console.log(tableData);
$input.item.json.tableData = tableData;
return $input.item;
```

最后加一个写入表格节点，把处理好的数据和表单 ID 传入，保存运行即可。

注意！第一次演示数据字段写错了，正确的数据引用应该是 {{ JSON.stringify($json.tableData) }}，大家以这个为准。

![](img/zhuanqian_ad88e34026ba132d5b69131a555742d6.png)

![](img/zhuanqian_22f7039105c29585098dced20e971da5.png)

看一下最终效果：

![](img/zhuanqian_a71637ccc6435d397aa17a8614523cd7.png)

调试没问题后，记得把定时触发器打开，让工作流正式跑起来。

![](img/zhuanqian_494259e77be9337568ebd53690965567.png)

完整的工作流我已经打包放到我的自动化工具站，需要的自取。

另外为了方便大家系统学习 AI + 自动化，我把 Coze 工作流、RPA、n8n 系列教程都整理到星球里了。进星球能拿到完整工作流和后续进阶玩法。星球刚开设，公众号有优惠券可以领取。

## 资源汇总

自动化工具站：https://auto.kanglan.vip

n8n 飞书社区节点：https://www.npmjs.com/package/n8n-nodes-feishu-lite

RSS 地址库：https://github.com/weekend-project-space/top-rss-list