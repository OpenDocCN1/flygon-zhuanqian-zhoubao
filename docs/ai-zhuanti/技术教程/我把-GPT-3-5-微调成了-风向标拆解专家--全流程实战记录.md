# 我把 GPT-3.5 微调成了“风向标拆解专家”：全流程实战记录
8 月底，OpenAI 终于开放了 GPT-3.5 的微调（fine-tuning）接口，官方文档也同步发布。我第一时间上手试了试，目标很明确：把一个专门拆解商业风向标的模型训练出来。今天就把我的真实体验和操作流程完整分享给大家。
如果你还没看过我之前用 ChatGPT 拆解风向标的帖子，可以先补一下背景：
## 先说几句大实话：什么时候才值得微调？
这两天折腾下来，我最大的感受是下面这几点：
1. 当你希望模型输出格式更稳定的时候，比如固定生成 JSON，微调会很有效。
2. 当你希望模型学会某一种特定风格，或者专注完成某一类任务时，微调能派上大用场。
3. 微调有机会减少每次请求时 prompt 的长度，但注意：它不一定更省钱，因为微调模型的调用单价往往更高。
4. 它还能在一定程度上抵抗 prompt 逆向——也就是说，别人不容易通过套话把你的“专属提示词”挖走。
## 微调模型 vs 原版模型：效果对比赛
下面每组图里，上面是微调后的模型，下面是原版 GPT-3.5。
第一组：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_21f3276542d98fa70491a30d9e9205b4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7242b760532bf2baa9903ffe21c931ad.png>
第二组：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_025890a4e70afc3f9526ca8845eb92a6.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f4b7e9a451cdc5b7d5bf94274050d4a4.png>
第三组：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_83bc674301825b395f59184f149a2608.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b1844fd9e0314e7e39e03c319a6353e3.png>
说实话，如果你逐条细看，可能不会觉得微调模型全面碾压原版。因为有些分析，原版 3.5 本身就已经做得很好了。
而且我的训练数据是拿 GPT-3.5 生成的，数据质量未必算高，这也会影响最终效果。模型决定性能的下限，数据质量才决定性能的上限。
不过，如果不纠结内容，只看结构，你会发现一个很有意思的现象：微调后的模型输出风格特别稳定，格式感很强，但我们明明没有在 prompt 里强调输出格式。这就是微调的价值——它能学习特定格式、特定风格，同时也在一定程度上防御 prompt 逆向。
下图是我用来生成微调数据的原始 prompt。每次调用 API 之前，我都要带上这一大段指令，而微调之后，这些都可以省掉，只需要很短的 prompt 就能完成同样的任务。
## 微调到底是什么？
按照官方文档的解释，微调是一种让预训练模型适配特定任务的机器学习技术。
举个例子：如果你运营一个电商网站，想用聊天机器人回答退货政策问题，微调可以让模型针对这类问题回答得更准，而不是泛泛而谈。
说得更直白一点：如果大语言模型是一个刚入职的运营实习生，那微调后的模型就是一个有三年经验的运营熟手。微调能让模型显得更“专业”。
下面这张对比表，可以帮你看清普通提示词（Prompting）和微调（Fine-tuning）的核心差异：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ef122ab6784d364e3738b954b2fc9419.png>
再举两个例子：
- 你只是想让模型算个“2+2”这种基础题，用普通 prompt 就够了。
- 但如果你需要模型做复杂的金融分析或预测，微调会更合适，因为你可以用特定金融数据集去训练它。
## 有哪些模型支持微调？
OpenAI 目前开放了下面几款：
1. GPT-3.5-turbo（最推荐，综合性能强，性价比高）
2. Babbage-002
3. Davinci-002
如果你的旧项目本来就在用后两者，或者有特殊迁移需求，可以继续选择它们。GPT-4 的微调支持也在路上了，官方预计不久的将来会推出。
## 什么情况适合用微调？
微调在以下场景里特别有效：
- 需要模型保持特定语气或风格，比如正式、幽默。
- 在医疗、法律等高风险场景里，需要更可靠、稳定的输出。
- 任务包含大量复杂子指令或边缘情况。
- 需要模型完成某项非常具体的能力，比如生成代码、做垂直领域问答。
不过在决定微调之前，建议你先试试 prompt engineering 或函数调用，因为它们的反馈循环更快。
粗略区分：
- 提示词工程：通过优化 prompt 提升效果，但处理不了太复杂或太特定的任务。
- 函数调用：适合做简单计算类任务，但无法理解深层语义。
- 微调：能搞定高度特定且复杂的任务，但更花时间和资源。
## 实战开始：准备数据集
微调第一步，是准备符合 OpenAI 要求的数据集。
数据格式大体长这样：
```json
{"messages":[{"role":"system","content":"你是一个有用的助手。"},{"role":"user","content":"如何学习编程？"},{"role":"assistant","content":"学习编程需要投入时间和精力，并且需要大量练习。"}]}
```
简单说，就是一组 messages，里面按顺序放 system、user、assistant 的消息。
在做风向标拆解时，我的每一条数据都是一轮对话，内容大概是这样：
```json
{"messages":[{"role":"system","content":"你是一个 AI 商业风向标拆解助手，请你帮助用户拆解分析风向标。"},{"role":"user","content":"我想要你帮忙分析的风向标是：快手官方上线电话号卡分销功能"},{"role":"assistant","content":"Q：你今天关注的风向标是哪一个？A：快手官方上线电话号卡分销功能。\nQ：请给出这条风向标的 1-3 个知识点？A：...\nQ：请说出它的商业模型是什么？A：...\nQ：请判断它的盈利状况，如有可能，请说出月盈利预期。A：...\nQ：请判断为什么它是机会/为什么它不是机会？A：...\nQ：如果你要来做这个项目，它的最小 MVP 是什么？你会怎么开展工作？A：..."}]}
```
这里的 assistant 回答，固定包含“关注的风向标、知识点、商业模型、盈利状况、机会判断、最小 MVP”六个部分，结构感很强。
有几个注意事项需要记牢：
1. 每个示例要和你真实使用场景高度相关。
2. 每个示例不能超过 4096 个 Token。
3. 至少需要 10 个示例，才算达到最低训练门槛。
4. 一般建议准备 50 到 100 个示例，效果才会比较明显。
5. 如果初步效果不错，可以继续加数据，数据量每翻一倍，性能通常也会跟着提升，但不会永远线性增长。
## 原始数据是怎么生成的？
我的原始数据是通过调用 GPT-3.5 API 生成的，用的就是上面那个很长的拆解 prompt。这个模板最早来源于刀姐的风向标作业。
如果你不会写代码，也没关系，直接把 prompt 扔进 ChatGPT，然后手动复制结果就行。在代码解释器里可以这样操作：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5a2c4503085543f46f2379b923c4bc32.png>
这样每跑一次，就能得到一条训练数据。
重复十来次，一份最小可用的数据集就出来了。
如果要更高效一点，代码解释器还有进阶玩法。
先把任务定义清楚，让它批量干活：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0b3b821bced220799ac571dd4df102b9.png>
然后 ChatGPT 就会自动生成内容，并帮我们保存下来：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7de52a96258d736a4a3a2af369b7a406.png>
接下来不用停，继续让它生成就行：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c38878cefd770afbe1019285fc36b5f1.png>
要是中途出现问题，只需要把问题说清楚，再让 ChatGPT 自己修改。
这样就能拿到一份完整可用的训练数据：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_408031d83f62b3bc17cfb32b6af0a3f3.png>
不过生成出来的数据还要微调一下，因为 system prompt 太长，我们需要精简：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a43b17bffe34faa244af0841c63d642b.png>
## 上传文件：用现成工具就能搞定
为了把数据集传到 OpenAI，推荐大家直接用这个开源工具：
https://github.com/anchen1011/chatgpt-finetune-ui
懂技术的朋友可以自己拉下来部署，不想折腾的可以直接用作者提供的在线版本：
http://system2.space:8001
注意：用在线版一定要记得，操作完立刻删除你的 API Key，安全第一。
第一步，在输入框填入你的 OpenAI API Key，然后按回车：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_58633c6d7958a4fab82623fc5213cced.png>
我自己用的是魔改版，和原版基本没差，只是改成了自己的环境，用起来更安心：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ab0df850147058de6ea04e6a4fb67aea.png>
接下来，把刚才生成的数据集上传上去：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1ef4b99932d3991c2b1c277af3b5c230.png>
我的魔改版里加了个费用预估功能。可以看到，微调这 10 条数据预计要花 0.13 美元，并不算便宜。
## 开始微调
我的版本需要手动把文件上传到 OpenAI，原版工具会更省事，直接从本地上传就行。
上传后，OpenAI 会先做文件校验。校验没问题后，文件状态会变成 processed。这时候就可以创建 fine-tuning job 了：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f803e6741d6c54c33ce69e4a5f2cf138.png>
等训练跑完，一个专属于你的微调模型就诞生了。
如果你也想做类似的垂直场景尝试，不妨从 10 条数据开始，先跑通流程，再慢慢优化数据质量。毕竟微调这件事，真正拉开差距的，不是模型，而是你喂给它的数据。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a849581272febd3a558cc29dc957b94c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3e948af7dfd865650ebca149fafee0be.png>
提交训练任务后，不用一直盯着看。根据数据集的大小，等个几分钟到几小时，再打开“Get Fine-Tuning Job Detail”查看进度。只要状态栏显示为“succeed”，就意味着模型已经训练完成，接下来就能到Playground里亲自试效果了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e57d05e0d4d10c5d5fcb7219fd6f0eca.png>
# **实测微调性能**
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_389c1f21243e560a649fb079bc196cf0.png>
这样一来，一个专属的风向标分析模型就到手了，是不是很带感？心动的话直接上手试试，成本也就两美元上下，还能顺便点亮【微调GPT-3.5模型】这个新技能点。最后，想认识有海外数据资源的大佬一起搞点合作，有意向的欢迎评论区聊聊~
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e57d05e0d4d10c5d5fcb7219fd6f0eca.png>
评论区：
暂无评论
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1c37d505930596d12a88ab23e11aa07a.png>