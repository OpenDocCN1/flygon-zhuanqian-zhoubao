# n8n 实战：从零搭建 AI 写稿 + 一键推送公众号的自动化流水线



## 写在前面

提醒一下，这篇教程拆得很细，内容量比较大，跟着搭也需要不少时间。动手前最好先确认自己有整块的空闲，精力跟得上。没空的话建议先收藏，挑个安静的时间再开干。

微信公众号自动发布的思路其实不算新鲜，Coze 上也能见到类似插件。这次选 n8n 重新实现，是因为整个链路很典型，几乎把新手刚上手后会用到的核心功能都串起来了，很适合作为进阶练习。

把下面这套流程跑通后，你能掌握：

1、如何安装社区节点
2、大模型节点的接入方式
3、节点之间的数据如何传递
4、如何让模型结构化输出多个字段
5、凭证的创建与配置方法
6、把网络图片 URL 转成可上传的文件

## 一、开工前的准备

### 先装上公众号节点

需要用到一个基于微信开放文档开发的公众号节点，接口覆盖很全，能直接完成图文的自动推送。点进节点介绍页，复制安装指令：

```
npm i n8n-nodes-wechat-offiaccount
```

https://www.npmjs.com/package/n8n-nodes-wechat-offiaccount?activeTab=dependencies

![](img/fef5abfe2ee752b7f07276de1eb3b039.png)

复制好后打开 n8n，点击左下角设置

![](img/52ef96476e835d4a265f1bdfc25e8a61.png)

进入社区节点，选择“安装社区节点”

![](img/53d229c7fdf7f34a1bcc37ee20cb8703.png)

把刚才的命令粘贴进去，勾选风险提示，点击安装

![](img/e6cc12acec214a387f3ffda1dced8bda.png)

安装完成后，节点列表里就能看到它了

![](img/760fbbbfa4a185c469f35773b876235d.png)

### 准备能调用的外网大模型 API

n8n 本身没有内置大模型，需要自行接入。这里用 OpenRouter，国内可直连且提供免费模型，调试很方便。

官网：https://openrouter.ai/

注册登录后进入 API Key 页面

![](img/7292ade6230adce04f0b8b004a047a74.png)

点“创建 API Key”

![](img/a77225ace311567074d3be5f80c0abc6.png)

生成后立刻复制保存，只显示一次，丢了只能重新创建

![](img/86addcc64fa64a553db3a6b91cf20f5c.png)

### 准备一个免费的图像生成模型

公众号发文封面图是必填项，这里用阿里云百炼的通义万相。活动期间新用户有大量免费额度。

进入 https://bailian.console.aliyun.com/ 注册登录后，新建一个 API Key 并保存

![](img/c7b83a1bd3a546350643b7122022d32f.png)

## 二、在 n8n 上搭建自动写稿 + 自动发布的工作流

### 1、起步：触发节点

工作流的第一步是触发。n8n 触发方式很多，为了方便调试，这里用 Chat Message 节点，直接在聊天框输入指令就能跑通

![](img/9e466133417e13f7a7368375b95c3436.png)

### 2、接入大模型

在触发节点后加一个 AI Agent 节点

![](img/c003795825c24069240373e63527439e.png)

节点会提示大模型未配置，点击 Chat Model 旁的“+”，搜索 open，选择 OpenRouter

![](img/b94641768bc0d2e5dbb200ab8f40d9a4.png)

双击 OpenRouter 进入配置，需要先创建凭证

![](img/4d4114ab1f40a1b3e852ef6e410f22c8.png)

进入凭证创建界面，只需要填入 API KEY

![](img/839d8b40578071a587a40b98b2dd6fc1.png)

把准备阶段申请的 OpenRouter Key 填入并保存

![](img/d0826d2048b1b36e70efb4ebee28fd4c.png)

返回 OpenRouter 配置页，选择刚才的凭证，在 Model 中搜索“free”挑选免费模型。正式用建议换付费模型，免费模型有频控限制。

![](img/79b4f10bd94bd14e965a7f17ecaf9997.png)

选好模型点左上角返回画布

![](img/e02ef888bbf3db549dd4758aceb5de6a.png)

### 3、给大模型下指令

双击 AI Agent，设置参数和系统提示词。因为是用聊天触发，可以直接选 Connected Chat Trigger Node，参数会自动关联。

点击 Add Option，选择 System Message 填入系统角色设定

![](img/a1a82b1c63fa9ddcb7341e9ea5af971d.png)

输入简单的提示词即可

![](img/f58f7d0c9c4acf87f4f1a57bd755f070.png)

保存后在左下角聊天框输入内容测试，返回正常说明配置成功

![](img/199001dae219b31c6001758640628f49.png)

### 4、让输出结构化【重点】

目前只是简单对话，后续发布需要标题、正文、配图提示词等多字段。要让模型按格式输出，先打开 AI Agent 的结构化输出开关

![](img/d1b71e8bc53ee2675bf156a019ca22d1.png)

打开后会多出一个结构化输出节点，点击添加

![](img/069e94bae2635a7541fe33c0a378d5a4.png)

按示例配置输出结构，给模型一个清晰的格式模板

![](img/e5c775b2f919efb3b15243819ce1e35c.png)

重新执行，模型就会按设定好的字段返回内容了

![](img/7fd7ab4b628691d4e840050e71adcb4e.png)

### 5、加上图像生成

回到阿里云百炼，找到模型广场筛选图片生成模型，选择指定模型并打开 API 参考

![](img/f7ff8dd62c76569c25032d38abbb5d9e.png)

复制页面里的 curl 示例

![](img/42c242c07295308636278531484aaf9f.png)

把代码里的 $DASHSCOPE_API_KEY 换成之前创建的百炼 Key，保存。注意 Bearer 和 Key 之间保留空格

![](img/99ee0f8eb32a8b6957034df4ce95c633.png)

在 n8n 的大模型节点后新增一个 HTTP Request 节点

![](img/030e0bece3cc0ef22f1f3c6121ad3ca0.png)

双击节点，选择导入 curl，把准备好的代码导入

![](img/190eaa98a61e45d12ed50d73e59cc67a.png)

导入后找到 JSON 参数，把前面节点生成的图像提示词拖拽到 Prompt 字段，完成文生图调用

![](img/847a7561f9654c81abe6dacc8401b197.png)

执行测试，图片生成成功

![](img/dbc58aed9dcc1ca7545c8b9811278a1a.png)

### 6、配置公众号调用凭证

发文需要授权，先创建凭证。点击左上角“+”，选择创建凭证

![](img/5d73758375021c12dc5c183e303749aa.png)

搜索 wechat，选择公众号节点的凭证类型

![](img/9c9ac3d16cd64128159aa73a9d18a172.png)

到公众号后台找到开发者设置，如未开启秘钥先启用

![](img/6c5b411d438b4b75482451335641bf58.png)

把 AppID 和 AppSecret 填入 n8n 凭证并保存

![](img/613a645718e414378c621a64fe39ba34.png)

记得在公众号后台添加 IP 白名单，即 n8n 所在服务器的公网 IP。本地部署需注意 IP 变动问题

需要云部署教程可参考：

![](img/ff50d8c390c35442eac1f7409986b291.png)

### 7、把 URL 图片转为可上传文件

公众号上传需要 file 格式，而模型生成的是 URL。新增一个 HTTP Request 节点下载图片并转为文件

![](img/771f14d1c8dcc9593bb857dffe989f1e.png)

双击配置，把上一步生成的图片 URL 填入请求 URL，新增 Response 选项

![](img/027b2d0c541bab4201db920eb081209d.png)

在 Response Format 中选择 File，表示把下载内容转为二进制文件，供后续上传使用

![](img/8b931107a3e99fe2c20892063fc5d7e7.png)

运行后出现文件信息即下载成功

![](img/db1159b6f0342c41400c63b80552da2e.png)

### 8、上传封面到素材库

在下载节点后添加“其他类型永久素材”节点，用于把图片上传到公众号素材库

![](img/4ccdcf8d78ac9c4346769dfd017eedfc.png)

配置时确认凭证是否使用第 6 步创建的公众号凭证

![](img/358d3f179ff8d6bac7ba0c211d648c10.png)

试运行成功后会返回 media_id

![](img/ae6b7d50480c6cb17f6a6ec2cf3773b1.png)

### 9、创建草稿

最后加一个新建草稿节点，放在图片上传之后

![](img/52167d8a59eaa6c573fc7310c5fbeea3.png)

双击配置，把 AI 生成的标题、正文和上一步的 media_id 分别映射到对应参数。内容较多可点击右下角放大编辑

![](img/f19f375f9992f543168f633858ba0fce.png)

放大后界面

![](img/a0336f68ccae69cd2c48f78328f6b484.png)

注意点：正文中可能含双引号，会破坏 JSON 格式，所以变量后需加上 .toJsonString()。示例代码如下

```
[
    {
        "article_type":"news",
        "title":"{{ $('AI Agent').item.json.output.title.toJsonString() }}",
        "author":"AI助手",
        "content":"{{ $('AI Agent').item.json.output.content.toJsonString() }}",
        "thumb_media_id":"{{ $json.media_id }}",
        "show_cover_pic":1,
        "need_open_comment":1,
        "only_fans_can_comment":0,
        "auto_publish":false,
        "publish_time":"immediate"
    }
] 
```

参数说明：

article_type: 文章类型，news 表示图文
title: 标题，需 toJsonString
author: 作者
content: 正文，需 toJsonString 处理特殊字符
thumb_media_id: 封面媒体 ID
show_cover_pic: 是否显示封面 1/0
need_open_comment: 是否开启评论 1/0
only_fans_can_comment: 评论权限 1/0
auto_publish: 是否自动发布 false 为草稿
publish_time: 发布时间

整体执行一次，草稿创建成功

![](img/3df8d1fdbfbbc86f21c340440271b17a.png)

到公众号草稿箱查看，文章已入库

![](img/6431553772bea3901c23a985a78b7f38.png)

想直接发布可在草稿节点后接发布草稿节点，建议先入库人工复核，AI 输出不稳定。

需要完整工作流可联系获取。

懒得自己搭的，可以试试我集成的自动化工具：https://auto.kanglan.vip

在工具里生成完素材后，一键选择账号即可推送到指定公众号

![](img/63d651a0b83fdc8636288b0a3f278060.png)