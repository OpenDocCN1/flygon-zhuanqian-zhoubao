# 喂饭级教程 | Coze 小程序第三弹：存数据、看历史、发上线
前两期，咱们已经把首页和海报生成功能搞定了。这一期接着往下走，把剩下的“我的”页面补齐，顺便带你把做好的小程序发布到微信上。还没看过前两篇的朋友，建议先去补课，不然直接看这期可能会掉队。
先分析一下“我的”页面到底要做什么。说白了，这里就是用来展示历史生成记录的，方便用户回看之前做过的海报。但现在的问题很现实：记录从哪儿来？答案是——目前还没有。所以必须先给小程序加上数据库能力，每次生成完海报，就顺手把内容存进去，之后“我的”页面才能把记录调出来展示。
![](img/zhuanqian_a04cc629f680bdff76877692a802f642.png)
## 一、新建数据库，把生成记录存下来
第一步，先建一张数据表。在 Coze 左侧找到“数据”，点击旁边的“+”，选择数据库，接着给表起个名字。
![](img/zhuanqian_8140489ed3d00ccf378b57a3134a0882.png)
表名确定后，再按截图里的配置把字段设计出来，主要就是 name（名称）、datetime（时间）、image（图片）这几个字段。
![](img/zhuanqian_44531e1e0c4ff51f0ee435a8c82e4a9d.png)
![](img/zhuanqian_a120220c0589c3ef39231424202aa0f3.png)
表建好之后，还要回头改造一下之前的生成工作流。打开 haibao_make 工作流，在“生成海报”节点和“结束”节点之间，点一下连线上的“+”，选择数据库节点加进去。
![](img/zhuanqian_0ccd285ec1f32ec1e97d874675827e19.png)
接着配置这个数据库节点。先要把刚才建好的表添加进来，然后设置数据库的输入，也就是把生成好的内容传进去，让节点知道该存什么。
![](img/zhuanqian_8aa37e5be11b542b5fd6e85fe305aaab.png)
![](img/zhuanqian_3e75e22765f6d59b0b6d648be757bb63.png)
接下来这一步，没写过代码的朋友可能会觉得有点卡，因为要写 SQL 插入语句。不过别慌，Coze 自带 AI 辅助写 SQL 的工具，直接让 AI 帮你搞定就行，遇到不懂的地方问一问 AI，学习成本真的不高。
先点一下“AI 辅助写 SQL”这个工具，然后在弹出的查询目标里写：往数据表插入 name、datetime 和 image，让 AI 自动把语句生成出来。
![](img/zhuanqian_4cddaa9086a30f2c573e8742dd813273.png)
![](img/zhuanqian_42bd94a5f2df8e7dc5665dff78bbc94f.png)
AI 给出的语句是这样的：
INSERT INTO haibao_history (name, datetime, image) VALUES ('', '', '')
这句话的意思是：往 haibao_history 表里插入一条数据，VALUES 里的内容要和前面括号里的字段一一对应。但仔细看，现在里面全是空字符串，显然不对，因为存进去的应该是工作流里拿到的真实数据。所以要把节点接收到的变量填进去，改完之后就成了：
INSERT INTO haibao_history (name, datetime, image) VALUES ('{{name}}', '{{datetime}}', '{{image}}')
![](img/zhuanqian_49a6918494afe846163ced4e876cc9a4.png)
## 二、新建一个读取记录的工作流
数据存进去之后，还得能读出来。新建工作流的具体步骤之前都讲过了，这里就不啰嗦，直接看搭好的结构就行。开始节点里加了一个 num 参数，作用就是设定总共要读取几条记录。
![](img/zhuanqian_3b08388a196bb8f7dcf4d769f4492de8.png)
读取数据的 SQL 语句如下：
SELECT name,datetime,image FROM haibao_history order by id desc LIMIT {{num}}
## 三、把页面逻辑绑上去
历史记录应该一进“我的”页面就自动显示出来，所以要先把页面加载事件绑定好，让页面一进来就去调用读取工作流。
![](img/zhuanqian_5fc799bb1135a6c9a5e6ac33efc760eb.png)
拿到返回的数据后，再把数据绑定到列表组件上。
![](img/zhuanqian_bb1f7f82e06a12edba7a95fa6f1e9dcc.png)
接着是列表里的细项，分别点击 name、datetime、image 这三个位置，设置对应的绑定数据。绑定格式固定为 {{item.??}}，?? 就是工作流返回的字段名。
![](img/zhuanqian_3864241ac50376be58774a911cb9459e.png)
![](img/zhuanqian_fea1b0b41d66499ddbed9ceca80ed684.png)
到这儿，整个小程序功能就算全部完成了。先点预览看看实际效果，确认没问题就可以准备发布。
![](img/zhuanqian_e151b0d0947a9a8b84daa02fd814b794.png)
## 四、发布到微信小程序
发布之前，记得先确认微信小程序已经完成基本配置，而且要确保备案已经通过。确认无误后，点击右上角的“发布”，进入发布页面。
![](img/zhuanqian_0ea54218aa1d038ae0fe37dde879fdc0.png)
第一次发布的话，需要先点“配置”，然后把微信小程序的 APPID 填进去完成绑定。
![](img/zhuanqian_24d21b10a225ae5755cd95cf3fe6e28f.png)
绑定完成后，就可以正式发布了。到这里，这个用 Coze 做的小程序就全部搞定，赶紧去试试吧！