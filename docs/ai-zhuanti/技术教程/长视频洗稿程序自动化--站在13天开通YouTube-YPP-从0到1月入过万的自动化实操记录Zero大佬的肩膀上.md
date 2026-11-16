# 长视频洗稿程序自动化——站在13天开通YouTube YPP，从0到1月入过万的自动化实操记录Zero大佬的肩膀上
作者：龙哥

## 长视频洗稿自动化：借Zero大佬的力，13天开通YouTube YPP，从0到1月入过万

先感谢Zero大佬的无私分享。这帖子在我心里就是2025年度最佳，没有之一。船要灯塔引航，人要贵人指路，Zero大佬就是那个在YouTube自动化赛道上给我们点灯的人。

![](img/zhuanqian_0fb686475d8ecd7fc945fe4b31d20d4d.png)

Zero大佬的原帖发布于2025年4月3号，我是在5月12号才看到的。当时看完立刻去评论区做了回应，顺便补出了“剪辑自动化”这一块的原始出处。

![](img/zhuanqian_5d10bbc9ce36b2e09dc8dc3b84c18253.png)

![](img/zhuanqian_14074238c557f356c65e7b42e42c985f.png)

![](img/zhuanqian_8a71e39c4ed2bc158769fa752b576aec.png)

因为我本身就是写代码的，对这种自动化工具特别敏感。顺着线索摸到GitHub，还真让我找到一个不臃肿、很灵活、上手也快的Python项目——pyJianYingDraft。简单说，这玩意儿就是用来生成和导出剪映草稿的，能直接帮你搭建全自动化的视频剪辑/混剪流水线。CapCut版本也在另一个仓库开发中，地址是 https://github.com/GuanYixuan/pyCapCut ，主项目地址是 https://github.com/GuanYixuan/pyJianYingDraft 。

既然是开源免费的，那就直接开干。我拿这个项目做了第一款软件——「视频自动化剪辑.exe」。

下载链接：https://pan.baidu.com/s/1PbZc8RFD4dmL221O9wUgSw?pwd=assq 提取码：assq

说实话，这个软件不算“开发”，因为github上有现成源码。但Zero大佬虽然分享了代码，对小白来说根本用不起来——光有代码，不懂运行环境，跑都跑不了。所以我就把它封装成了开箱即用的exe。

软件我确实留了一手（毕竟辛苦开发），但同样有私心：免费给赚钱圈友授权一年。5个软件的机器码都是同一个，直接填问卷就能领：赚钱圈友机器码专用问卷

![](img/zhuanqian_17125211a360147bb6403aaddd3e98a6.png)

![](img/zhuanqian_2be5e4fafb07d0c66d1e20899c839173.png)

授权时长统一365天，最大使用次数填-1就是不限制使用，如下图所示：

![](img/zhuanqian_7dbef7c251456424667eae12b4b5a5a1.png)

操作视频也录好了，跟着点一遍就会。

长视频这块搞定后，接着是「YouTube AI助手.exe」。

下载链接：https://pan.baidu.com/s/1a52CLPfH7tNfD6esPry6PQ?pwd=fx6i 提取码：fx6i

操作视频同样备好了。

接下来是长视频洗稿环节的三件套：

### 1. 智能伪原创工具.exe

下载链接：https://pan.baidu.com/s/1_xpcWjeqOgK-cXkMKP2AcQ?pwd=w4eb 提取码：w4eb

这工具需要买ChatGPT的API Key，点蓝色链接就能到购买页，模型默认选 `gpt-4o-mini`，统一走OpenAI接口。不过我得提醒一句：别完全依赖工具，建议人工介入——对原文或者洗稿后的文章先改一轮，再丢进去伪原创一遍，效果才稳。

![](img/zhuanqian_0b7b8a41329c2e2c26346ad34cf0524c.png)

![](img/zhuanqian_28c8ece1aae78eef29778bc8cc69fd9d.png)

Zero大佬原帖用的是Finetune Model，我没整明白，就直接用 `gpt-4o-mini` 来处理，完全够用。

![](img/zhuanqian_05f4eb75683bb5059869498f4a5e68f8.png)

### 2. 配音自动化.exe

下载链接：https://pan.baidu.com/s/1c_kMw8xp7KEqXGtR1f02Xw?pwd=9s4v 提取码：9s4v

配音这块直接借鉴思路，用的是 minimaxi.com 来处理。图片里已经有提示，点链接进去就行。核心原则不复杂，其实就是调官方接口。

![](img/zhuanqian_c5e5b1a88e9893f9cc179571879a40d7.png)

![](img/zhuanqian_fb3584756271a1b2540f24e87aae6944.png)

![](img/zhuanqian_3ff00ad7fd5c879898308aacec69ae83.png)

照着官方文档调API，配音模块就完成了。

![](img/zhuanqian_812deab31a2dbb7a18d8c404163a0294.png)

![](img/zhuanqian_8d81e04131632177d485e621ace8f83e.png)

### 3. AI图片生成器.exe

下载链接：https://pan.baidu.com/s/1ZTJnRVSUAK57DqBz82RMXw?pwd=2t2k 提取码：2t2k

图片生成需要去 https://my.runware.ai/login 注册账号并充值，消耗的是API Key的钱。至于OpenAI API Key去哪买，前面已经说过了。

![](img/zhuanqian_7c4635e07da5fc41547c5e514ceccac9.png)

出图跟配音一样，也是调API接口就行。

![](img/zhuanqian_25a08d9189f83076af80c16d2f958467.png)

付费这一块，实测用风向标那张卡是可以正常付款的。

![](img/zhuanqian_97dc5e56580faf04f4303e35fc8604fd.png)

我放一个示例出来，后面这工具还得继续迭代优化。

![](img/zhuanqian_245f807ee1c7255eebe47df2a92f3d15.png)

![](img/zhuanqian_6923c407324aadc704bded64d030ec94.png)

![](img/zhuanqian_1de7c7ba5bf2961c0133f6d8bf8b0c4b.png)

![](img/zhuanqian_4d3828e12296b0daee83ba85176672bc.png)