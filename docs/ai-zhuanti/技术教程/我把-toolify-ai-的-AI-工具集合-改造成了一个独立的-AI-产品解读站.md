# 我把 toolify.ai 的 AI 工具集合，改造成了一个独立的 AI 产品解读站
先看一下最终呈现的效果：https://toolify-insights.online/
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_35072b06137519ca511150a817c12d08.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5261690c5129fd906598aa06d8a8f167.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b2d0a6c71c9bd376f6c1d074affd1674.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_493794c84994afb26b671376054d827e.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e8fb9f04feab605fca29bbf8339ed530.png>
上面展示的就是我搭建的一个 Demo 解析页。这个站点的底子，是借鉴了圈友 @小学生 之前开源的项目，在此先感谢 @小学生 的分享。
我个人对需求来源的理解，正在慢慢拓宽。教练教的方法固然重要，但我发现日常里绝大多数可行的站点灵感，其实都来自赚钱圈的真实讨论。赚钱在聊什么，市场可能就在要什么。
这次动手做完，有几点收获印象特别深：
1. 把零散的文件拆分开单独管理，后续的迭代、修改和下架会轻松很多。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fe5816f2e4e5cabe56864a325f830688.png>
2. 之前做本地调试时，总是绕不开要搭服务器，这件事一直让我很头疼。这次直接用 Cloudflare Pages 就整个搞定了，体验确实顺滑。至于什么时候用 Workers、什么时候用 Pages，我也让 AI 帮我梳理了一遍思路：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_863bd4754245c48317570a137fa8e07b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_88e6b83a2d751d2c20b43da2d50b4261.png>
3. 借着 @小学生 分享的开源思路，我学会了怎么调用 API 做 AI 产品解析，感觉打开了新大陆。后来我又从 toolify.ai 重新拉了一份数据跑了一遍，原项目生成的 md 文件里产品链接是指向 toolify 的，我把链接改成了可以直达官方站点。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_df90dc15647c5d70177a0c2c35199ee5.png>
目前站点还有几个想继续打磨的地方：
1. 增加英文版的产品解析界面，翻译这块还没完全迁移过来
2. 在每个产品卡片上加上回源网站的直达链接
3. 持续补充更多 AI 工具的解读内容
4. 加入打赏入口
5. 考虑接入支付功能
如果你对这个网站有什么想法或建议，欢迎直接留言交流！