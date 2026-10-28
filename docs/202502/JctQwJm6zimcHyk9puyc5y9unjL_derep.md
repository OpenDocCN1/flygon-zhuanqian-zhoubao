# 排队无望时用这 9 个免费入口，让 DeepSeek R1 直接开聊

> 来源：[https://zzi7a49xoa.feishu.cn/docx/RQFNdiFGfoPH8nxlzfacuaPIn2b](https://zzi7a49xoa.feishu.cn/docx/RQFNdiFGfoPH8nxlzfacuaPIn2b)

“DeepSeek 又挂了！”
最近在各个 AI 讨论群里，这句话出现的频率有点高。

眼看同行已经用 R1 跑出产出，自己却只能盯着“服务繁忙”。

![](img/800f40f51ed1b2af2fc7315010388641.png)

别慌。

过去几天我挨个去试，用脚投票挑出几类现在还算稳定、并且能白嫖的 R1 渠道整理给你。

有纯网页对话，也有能免费调用 API 的，方便你把能力塞进自己的工作流程。

最后我也会把 本地搭建 DeepSeek 个人知识库 的完整思路讲清楚。

提醒一句：流量高峰期站点会偶发宕机，挂了就换下一家，总有一家能用。

## 一、硅基流动

华为云和硅基流动联手上线的满血 DeepSeek R1，注册即送 2000 万 Token 起步。

![](img/90223055c4f569a2adc4b1151557e408.png)

Token 究竟是什么？简单说它可以是词、标点、汉字，模型处理时靠它把文本拆成最小单元。

2000 万 Token 量级有多大？

粗略估算：一本普通小说每页约 300 字/词，2000 万 Token 相当于 6.6 万页。按 300 页一本算，约 220 多本，差不多一个大书架的量。

上手三步：

1、注册：https://cloud.siliconflow.cn/i/TAAOvaXg
2、进模型市场找到 R1。
3、输入指令开始对话。

![](img/d4ef63a3f37add71040c147532db28f5.png)

需要调用接口的话，在模型页就能找到文档，按步骤接入即可。

小技巧：借助 Cursor 或 Trae 这类 AI IDE 直接拉取示例代码，几分钟就能连通。

![](img/f1953f762c8a18310777c412fd8d5309.png)

## 二、秘塔

硅基、Lambda 等通道普遍缺少实时联网检索。

目前只有官方生态支持较稳，Lambda 与硅基的资料我测下来基本停留在去年。

![](img/de937ecf6aa5b3d855a30cc6c66314fc.png)

打开秘塔，开启长思考模式试试。

地址：https://metaso.cn/

![](img/1e5641160a8250ff4dc5197b06107609.png)

答案立马是当下的——今年暑期全网刷屏的电影《哪吒》！

口碑不错，剧情完整，就是得坐两个半小时，腰有点受不了……😆

![](img/73e76007e22fe281b832423a8db39e1c.png)

## 三、国家超算互联网

国家队已开放 DeepSeek 全民入口。地址：https://chat.scnet.cn/

网络上传闻有 32B、14B、7B，我实测在线的只有 DeepSeek-R1-Distill-Qwen-7B。

参数偏小，可作为保底：当其他站点都不可用、又不想折腾本地时再用。

![](img/17c5e8a07f8b64184f422cd9be9a4f29.png)

## 四、Lambda.chat

有科学上网条件的用户想求聊天极速，直上 Lambda.chat。

无需看参数面板，也不用写代码，点开即用。

地址：https://lambda.chat/

![](img/3acf8edc041e71aecf17811435d3228f.png)

除 671B 满血版 R1，还能挑选大量不同量级的 Llama 模型。

![](img/646e6ae455af225728f7dff19224e08a.png)

## 五、英伟达

DeepSeek-R1 让英伟达市值蒸发近 6000 亿刀，但英伟达很快拥抱了它——打不过就加入 😆

NVIDIA 用 HGX H200 部署满血 R1，推理速度拉到 3,872 Token/s！🚀

对比 GPT-4 的 150 Token/s、Claude-3 的 200-300 Token/s，差距明显。

使用门槛很低：一个邮箱注册即可，我还测过免登录直接用。

地址： https://build.nvidia.com/deepseek-ai/deepseek-r1
右侧直接给出 API 接入代码。

![](img/9d128535796981780e5902afd64dc2b9.png)

## 六、Poe

国内重度 AI 用户的常用工具 Poe 也接入了 R1。

官方版上下文窗口 164K，输出上限 33K。

![](img/6221b31f0dea3d016d89bec2b5152095.png)

![](img/f4e6e4c1798aa58d287c46649b94a005.png)

若需要在同一问题下生成超长文本，比如长文档或大段代码，可以试 DeepSeek-R1-FW。

它保持 164k 输入，同时支持 164k 输出。

日常问答用标准 R1 足够。

![](img/acb2598d803e5a280b41e269a0990e36.png)

## 七、Groq

除了满血 R1，若想体验大参数蒸馏版比如 70B，Groq 也是选项。

登录后左上角找到 Deepseek-R1-Distill-Llama-70b 即可使用。

![](img/fbb508004caa5f06776668acaee0aec5.png)

## 八、阿里云百炼平台

需梯子的备用池，有少量免费额度。

地址：https://api.together.ai/playground/chat/deepseek-ai/DeepSeek-R1

![](img/9ef4091d712d51731b250a9c3f476bb3.png)

## 九、潞晨

面向开发者的 API 接入平台，普通用户可跳过。

潞晨云为 DeepSeek-R1 系列提供从 671B 满血到轻量蒸馏的多样选择，重点是 API 目前限时无限量免费体验。

地址：https://cloud.luchentech.com/maas/modelMarket

能持续多久未知，先用先得。

![](img/632020f495de81f11e1c14e9a07df61b.png)

使用步骤：

1、生成密钥。

![](img/e9040cdcd266089c99c637d37b1f37b1.png)

2、进入 API 文档找代码样例，比如 curl 示例。

![](img/7fa6ca5cd2a2c324ac287428e572257f.png)

导入 curl 到在线工具 ApiFox 测试连通性：https://app.apifox.com

![](img/7bf0028d9821dc94e9c7863db3d41902.png)

3、粘贴从官网复制的密钥。

![](img/e5ccf980f99746449e28b224fecbb33f.png)

4、发送测试，OK 即可。

![](img/4d146fbf007a0b6e258a92048bb7fb2c.png)

后续如何集成，有技术背景的自行搞定。无技术背景可参考我之前的 AI 编程文章，用 Cursor 辅助开发。

## 十、本地部署搭建个人知识库

常有人问：如何本地部署 DeepSeek 搭建个人知识库。

![](img/24adba709c80bdd4d03eccbca718c485.png)

坦白说，除非做技术研究或数据必须离线，我不建议普通人折腾。

目前 Ollama 上 1.5B~70B 均为 R1 能力蒸馏到 Qwen/Llama 的学生模型，性能提升但与原版 671B 仍有差距。

官方满血 671B 的算力成本对个人较高。

不过我找到了折中方案：能用上 R1 本体，还能拿到免费额度。下面分三部分讲。

本章收获：

1. 满血 DeepSeek R1 API 搭建个人知识库
2. 本地部署 DeepSeek R1 搭建个人知识库

### 一）个人知识库实测效果

看几个案例：借助知识库做外脑，用方法论指导提问。

DeepSeek 很强，前提是会问。

不会提问，再强的模型也白搭。除了自学提示词，最快的方式是把提问指南放进知识库，让 AI 教你怎么问。

![](img/b9eca90a925b6d70ba3576b02f4a65ff.png)

AI 结合知识库里的 DeepSeek 指导手册，会预判你可能的问题并给出标准提示词格式。

从结果看，回答来自知识库而非模型自带语料。

![](img/2a350c47f23f3101487b05342d1b7b99.png)

当然也能直接检索库内原始信息，秒查。

![](img/d5d3f21501452d1e96a7100608a026a0.png)

### 二）用 API 搭建知识库

数据不涉密、追求最佳体验，直接上满血 R1 671B。

1、先安装 Cherry Studio。

地址： https://cherry-ai.com/download

![](img/61ae7de226082183cc26efde5f323052.png)

2、登录硅基流动，新用户送 2000 万 Token。

地址：https://cloud.siliconflow.cn/i/TAAOvaXg

![](img/465f590a0eb7242f498ad03e97752b84.png)

3、在 API 密钥页创建或复制已有密钥。

![](img/afa763773a74bcb329e134b607531ee7.png)

4、在 Cherry Studio 配置 API Key。

![](img/ba90130faec724e992d8984036a0604b.png)

5、模型广场前两名是硅基+华为云联合发布的 DeepSeek R1/V3。需要推理能力就选 R1，并复制模型名。

![](img/843ed86675f7a7390f989d2ce411a3f8.png)

6、在硅基流动服务下添加 R1 模型。

![](img/042dbe556931d31a6504ac4bccf68f84.png)

7、点检查测试连通。

![](img/799b3e74b7c14f8702cd89fd18a50ef4.png)

8、还需要一个嵌入模型。嵌入模型负责把本地文件转成向量存入数据库，提问时通过 RAG 召回相似内容。

配 BAAI/bge-m3，追求精度选 Pro/BAAI/bge-m3。

![](img/fc7467c24ceadb947a27c870a7d532e5.png)

同样方式配进 Cherry Studio，无需检查。

![](img/9198cf091f6ed94bfca25dd5cecfda58.png)

9、在 Cherry Studio 新建知识库，选择刚才的嵌入模型，自动向量化。

![](img/1bef25494b85f20b411a280647db04c2.png)

10、上传本地文件。

注意：扫描件、手写件、复杂表格或公式 PDF 解析效果差，建议先转结构化文档再上传。

推荐 Doc2x：https://doc2x.noedgeai.com?inviteCode=4A6KOD
或 Textin：https://www.textin.com/market/detail/pdf_to_markdown

上传成功后图标显示向量化完成。

![](img/46597aa07e07e4336791dc1f65634e99.png)

11、测试使用，添加助手并选满血 R1。

![](img/71bbaf58b7811e2ef13e61e41d5419c2.png)

不想每次都选，可设为默认模型。

![](img/a9540ede74faa3df3520f0a636104f14.png)

测试，DeepSeek 已开始深度思考。

![](img/7c5fd82ad638ba06dc9858c8846374b1.png)

AI 回复与原文一致。

![](img/d1e8ba66772c826e1e270920d75282ea.png)

原文内容：

![](img/aaf33e0d0ff7376bfcb4a28c06a7ee51.png)

### 三）本地部署建知识库

想简单体验或保护数据，可用本地方案。

1、去 Ollama 官网下载：https://ollama.com/download，建议装最新版。旧版装 R1 可能用不了。

![](img/e5e4ab4c647d5270458ce843d4b27e1a.png)

2、运行 Ollama 后，用命令行拉取模型：https://ollama.com/library/deepseek-r1

![](img/322eb9051eaa96cb80fdfba58e3e7101.png)

无 GPU 建议 1.5B 起步。4G 显存勉强跑 8B，但慢。RTX 4090 跑 32B 效果不错，按需挑选。

![](img/a6c59514f826e44b907b4f769f423b77.png)

也能用 Cherry Studio 做本地模型的 UI。

打开配置选 Ollama，管理里选本地部署的模型，找不到就手动添加，密钥随意。

![](img/343be680abb309aea8c2e8b2bdcc2b09.png)

点检查测试连通，成功即可。

![](img/4b25a4391e5d2e6c5051defb9ee04314.png)

之后在添加助手时选本地 R1 模型即可使用。

![](img/4e1dbf3247a17e9954745cc8aa63cec9.png)

测试结果与原文一致，搞定。

![](img/2513f3f17d728b16f4f7ccd4c93015d0.png)

我用的是 Mac，没测 Windows，但流程基本一致，自行尝试。

## 十一、总结

以上平台各有侧重。

国内用户首选秘塔、硅基流动；国外可试 Lambda、Poe、英伟达。

硬件充足就本地部署，数据最安全。

技术迭代永远在上演，一个入口卡了，下一个马上补位。这就是科技的魅力——总有备选，总有希望。

最后想说的不仅是工具，更是如何在变化中持续找到好方案。

真正让人心头一热的，不是又一个榜单刷新，而是一个来自中国的团队，把大模型做到了世界级水准——它需要用“+86”才能注册。

作为亲历这场技术跃迁的人，我们确实足够幸运，能在自己的土地上，见证属于中国的 AI 时刻。

必须说，领先从来都不是终点，它更像是一个逗号，而不是句号。

但 DeepSeek 真正触动我们的，是那种“原来中国也可以”的底气，是它把“可能”两个字，重新放回了我们心里。

这份底气，才是我们真正愿意去守护的东西，也是值得被寄予厚望的火种。

最后，也谢谢各大平台一路以来的支持，祝大家玩得尽兴！

我是 🐼 熊猫 Jay，我们下次再见～