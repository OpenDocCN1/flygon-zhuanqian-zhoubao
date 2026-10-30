# 我把 DeepSeek 接上网了：基于 Coze 的在线满血版实操记录

> 原文出处：[`www.yuque.com/for_lazy/zhoubao/aaf5tvntmyiv7ffr`](https://www.yuque.com/for_lazy/zhoubao/aaf5tvntmyiv7ffr)

##  DeepSeek 联网玩法：用 Coze 打造可联网的完整版

作者：熊猫 Jay  
发布：2025-02-07

最近两天，关于 DeepSeek 如何联网的问题，我几乎被问到麻木了。可以说，这已经成了大家最关心的痛点。折腾了好一阵子后，我摸到了一套目前来看比较稳的联网实现方式。整个流程我整理在了飞书文档里，感兴趣可以直接看详情：

如果这篇思路对你有帮助，麻烦点个赞支持一下，谢谢！[`zzi7a49xoa.feishu.cn/wiki/JJMgw7MBAiCHxfkavcVcCsgvnnh?from=from_copylink&reRdXZ;=1`](https://zzi7a49xoa.feishu.cn/wiki/JJMgw7MBAiCHxfkavcVcCsgvnnh?from=from_copylink&reRdXZ;=1)

* * *

读者互动：

程序员飞飞：所以本质上是付费调用火山引擎部署的 DeepSeek R1 服务对吧？

熊猫 Jay：没错。

Erik：输出时怎么才能看到推理过程？

珊瑚虫：Coze 的创业版收费会不会很贵？

Monk：我用豆包做关键词提取，结果总是答非所问，是什么原因？[抱拳]

熊猫 Jay：是我截图时漏掉了这一步，已经补上了，关键是要去设置用户提示词。

熊猫 Jay：费用方面还算可以接受。

熊猫 Jay：这个配置入口我暂时还没找到。