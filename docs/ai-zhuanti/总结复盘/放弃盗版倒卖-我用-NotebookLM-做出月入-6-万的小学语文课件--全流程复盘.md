# 放弃盗版倒卖，我用 NotebookLM 做出月入 6 万的小学语文课件——全流程复盘
260618 副业SC 精华
哈喽，我是龙哥。上过一年班，随后以自由职业身份探索了十年，现在一门心思做教育类虚拟商品。这篇复盘，讲我怎么把危险系数很高的资料搬运生意，切换成用 NotebookLM 生产小学语文课件的正规打法，并一路在小红书完成需求探测、内容引流、工具提速和团队协作。
目前这个项目由 NotebookLM 驱动，主要产出 PPT 课件。早年倒卖过盗版资源，所以对老师端的真实需求心里有数。眼下月流水稳定在 5w 上下，私域里沉淀了约一万名教师。全文不灌水，只聊真实踩过的坑、验证过的路径，以及普通人可以直接抄作业的细节。
这篇文章想清楚回答六个问题：
1. 为什么非要放弃搬运，投向智能创作？
2. 小红书怎么花小钱验证赛道？
3. Gemini + NotebookLM 怎样配合，才算做出了能卖的产品？
4. 放量的时候，哪条平台红线不能碰？
5. 靠工具和兼职，人效可以怎么突破？
6. 内容、流量、交付、变现四个环节怎么咬合成闭环？
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_0_0.png>
## 一、卸载盗版生意，装上新方向
过去两年，我一直混迹在虚拟资料倒卖的圈子，主要就是把小学语文的教辅、课件打包转手，前期确实跑得顺手，赚到了起步资金。
小学语文虚拟资料项目总结：从0 到100，3 个月团队快速盈利30w
但这条路的隐患随着时间浮出水面：各平台审核越收越紧，侵权投诉和诉讼随时可能砸到头上，天天折腾盗版既消耗心力，也看不到长期出路。权衡再三，我把盗版业务彻底断掉，并给自己立了规矩：两年之内绝不沾染任何相关灰色操作。
重启这个方向的契机，来自一次航海活动——我观察到有人正用 NotebookLM 批量制作课件，思路很有意思。感谢赚钱这个平台
结合过往的行业手感，我判断得很明确：中小学教师对优质课件、公开课 PPT 的需求长期稳固。于是新路线就此确定：借助智能工具批量产出高质量小学语文课件，做成可以放心售卖的商品，精准对接教师群体的刚需。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_1_0.png>
正式动手之前，我专门做了一轮低成本的赛道测试，阵地就选在小红书：高频搜索“小学语文公开课 PPT”“精品课件”“智能教学课件”等关键词；重点盯三个信号——有没有博主能稳定更新，评论区是不是常有人留言求资料、求课件，同行是否留下了清晰成交痕迹。综合看下来：需求扎实、流量不断、付费意愿明显，这个方向完全值得做。
## 二、先花一个月，把“能卖”的课件标准磨出来
方向确认后，我反而按住性子，没有大批量出货，也没急着变现，而是死磕一个关键命题：怎样打磨出老师看着顺眼、上课能用、心甘情愿掏钱购买的课件？这件事我花了一个月的时间来修炼。
初期的模型直出成品根本没法卖，主要有三个致命缺口：
- 视觉底子差：版式混乱、风格跳跃，和小学课堂偏好的简约、清新、国风调性相去甚远；
- 内容深度不足：基本是课文的简单摘抄，缺少清晰的教学推进逻辑；
- 场景不匹配：课堂引入、生字教学、朗读示范、课后巩固等核心环节统统缺失，老师拿到手上不了讲台，更不用说应付公开课和赛课。
那段时间我一直提醒自己别冒进：先把“老师愿意用、愿意买单”这层地基打牢，再谈别的。同时，我采用了“半成品抛砖引玉”的打法——把还没彻底完善的作品先发到小红书上试探反应。结果远超预期：12 月 13 日发出测试笔记，12 月 15 日就收到了第一笔订单，智能课件的商业价值当场得到验证。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_3_0.png>
反复调整若干轮之后，一套高效、稳定的制作 SOP 沉淀了下来，整个链路以模型为主力，人只做轻量收尾：
- 内容层：向 Gemini 输入定制好的指令，把课文拆解成可讲授的模块，明确页数范围、教学板块和知识点边界；
- 排版层：把梳理完毕的文字内容导入 NotebookLM，它能迅速排出版式统一的 PDF 版本；
- 精修层：PDF 原生格式不便直接改动，WPS 直接转 PPT 又乱码频发，所以我会借助 AI 消除、截图替换、Canva 智能拆版等手段逐一修正版式问题、统一视觉风格、补充教学细节，最终交付出干净、可再次编辑的 PPT。
这套打法把创作门槛砸得很低——哪怕没有设计功底，也不一定深谙语文教学法，普通人照样能独立完成课件生产。
具体步骤也一并贴出来：
第一步：PDF 下载好后，去闲鱼花一毛钱左右买一天的 WPS 会员；
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_4_0.png>
第二步：打开 PDF 文件，按我截图里的流程将它转成 PPT；
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_5_0.png>
第三步：WPS 转出来的 PPT 乱码往往很严重，用 AI 消除和截图替换来处理比较有效——但一定要先选中目标图片再点消除按钮，否则功能模块不响应。
再送一个 NotebookLM 去水印的地址：https://www.notebooklmwatermark.com/zh ，转 PPT 之前先把水印去掉会更省事；另外也有基于模型开发的本地批量去水印小工具可以挂在电脑上跑。
为了解决转格式时的乱码与版式错乱，我还摸索出一套可画国际版的拆版方案：
- 准备 Canva 国际版账号：https://www.canva.com/；
- 调出 Magic Layers 魔法图层功能（需要先设置一下才会显示），点一下就能把整张图的元素全部拆开，基本见不到乱码，缺点是要一张张上传图片。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_6_0.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_6_1.png>
把账号语言切换为美国英语，即可解锁 Magic Layers 魔法图层：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_7_0.png>
第一步：语言设置里选中美国英语；
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_7_1.png>
第二步：直接把图拖进可画国际版窗口；
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_8_0.png>
第三步：点选图片，再点 open in editor 按钮，进入编辑器；
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_8_1.png>
第四步：使用魔法图层，全部元素一键自动拆分；
拆分结束后各元素保持独立、无损，补上动画就完工。
最终效果相当理想，目前我就是逐页这样处理。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_9_0.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_9_1.png>
## 三、量产放大，遭遇产能天花板
制作流程跑通之后，我开始规模产出内容，持续往小红书发引流笔记，很快撞上了第一个硬瓶颈：根本做不过来。
一条笔记从零到发布，要经历 PPT 导出高清图、稿定设计里排版、拟定标题、写种草文案、挑选话题标签、再到账号发出，纯手工走完一轮至少 10 分钟，一天极限只能发 10 条左右，流量量变无从谈起。智能内容时代，项目要想放大就必须依赖稳定量产，手工操作的效率直接封死了增长上限。
为了赶速度，我一度动过歪脑筋——开发过小红书群发脚本，用程序去做机械化的批量发布。
结果相当惨烈：账号被打上限流标记甚至封禁，累积起来的全域流量瞬间归零，前期养出的账号权重全部作废。那次跌跟头也让我彻底看清楚了平台的底线：工具可以帮你提效，但机械化的机器人操作绝对踩雷。
此后我把运营规则全部推倒重来：任何脚本、群发工具统统扔掉，全部内容都回归真机手动发布。表面上是慢了一些，但账号权重稳得住，系统推荐也恢复正常，长期做下来反而更安全。
眼下这个项目运转两个月，累计营收突破 10w+，最强月份摸到过 6w。这个数字不是靠单个账号单打独斗实现的，而是由小红书三个关联账号的流量合力托起来的。
接下来我们还准备再开店铺做几个其他类目，初中语文、地理、生物、历史都已在测试，需求端都有反应。
多账号放量时也有痛点：模型批量产出的标题和文案，依然容易被小红书识别出来，给账号带来风险。解决办法不复杂——提示词要高频更换，同一套话术不能反复复用。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_12_0.png>
## 四、用工具重构流程，把时间抢回来
跨过平台规则这道坎后，我把全部工作流重新拆了一遍，最容易吃掉时间的环节就两个：一是课件文件的归整，二是小红书笔记图片的排版输出。
得益于在航海里学到的工程思维，我试着把复杂问题拆解成小块，再让 AI 辅助写代码，把开发门槛降得很低。最终借助 AI Studio 加 Python，我做出了几款轻量级的内部小工具，也把其中一些实用脚本开源给了同行：
- 小红书配图自动归整工具：PPT 导出的图片能够自动排序、裁切和排版，不用再手动一张张调；
- NotebookLM 批量下载脚本：绕开平台的限制和繁琐的单次下载，一键就能把全部 PDF 课件拉到本地，彻底解放双手。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_13_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_14_0.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_14_1.png><https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_14_2.png>
这里把 NotebookLM 一键下载 PDF 的方法同步给圈友：添加一个浏览器书签，再把书签地址替换为下面的代码，在页面里点一下书签就会自动触发下载：
javascript:(async function(){ /* 1. 寻找右侧面板中所有的“三个点(⋮)”按钮 */ let buttons = Array.from(document.querySelectorAll('button')); let moreButtons = buttons.filter(btn => { let rect = btn.getBoundingClientRect(); /* 筛选位于右侧列表的三个点按钮 */ return btn.innerHTML.includes('more_vert') && rect.left > window.innerWidth / 2 && rect.top > 100; }); if(moreButtons.length === 0) { alert('没有找到文档列表，请确认右侧面板已加载。'); return; } let count = 0; alert(`找到 ${moreButtons.length} 个文档，开始全自动排队下载...\n\n⚠️ 注意：浏览器可能会在顶部弹出【允许下载多个文件】的提示，请务必点击【允许】！`); /* 2. 使用循环，像机器人一样挨个点击 */ for(let i = 0; i < moreButtons.length; i++) { /* 点击当前的三个点 */ moreButtons[i].click(); /* 等待菜单弹出的动画时间 (0.5 秒) */ await new Promise(resolve => setTimeout(resolve, 500)); /* 寻找菜单里的“下载 PDF”按钮 */ let xpath = "//*[contains(text(), '下载 PDF')]"; let result = document.evaluate(xpath, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null); let found = false; for (let j = 0; j < result.snapshotLength; j++) { let node = result.snapshotItem(j); if (node.innerText && node.innerText.includes('下载 PDF')) { node.click(); /* 触发下载 */ found = true; count++; break; } } if (!found) { console.log(`第 ${i+1} 个文档没有找到 PDF 下载选项。`); } /* 点击空白处收起菜单 */ document.body.click(); /* ⚠️ 关键：等待 10 秒再下载下一个，防止被浏览器当作恶意连击拦截 */ await new Promise(resolve => setTimeout(resolve, 1500)); } alert(`✅ 批量下载指令发送完毕！\n 共触发了 ${count} 个 PDF 下载。`);})();
再送大家一个可以直接套用的小红书笔记模板，包含标题和正文的实操写法。
比如标题，我现在基本走这个路子：
《中国美食》带你解锁舌尖上的汉字魔法！??（对应文件：232.pdf）
正文可以这样组织：今天分享编号 232.pdf 的课件，把教室变成“美味食堂”，带孩子们在诱人的香气中认识中国饮食文化！????
第一站：舌尖上的生字精灵（导入识字）
欢迎来到美味小镇！想进食堂，先得捕获这些“生字精灵”：津、溜、腐、酱、粥、蛋。课件摆了一道“汉字魔法阵”，通过加一加、减一减、换偏旁（如“火+暴=爆”“草字头+姑=菇”）等多种玩法，让识字复习像点餐一样有趣！
第二站：火候里的偏旁密码（部首解析）
为什么美食总离不开“火”？课件聚焦三大偏旁，破解烹饪秘密：火字旁对应炒、烤、爆；四点底对应煎、蒸、煮；立刀旁对应切、剁。带着学生发现规律：带这些偏旁的字，大多与火候或烹饪方式脱不开关系！
第三站：金牌点餐员挑战（朗读指导）
怎么读出美食的诱人感觉？课件提供了“美食家读法”：红烧茄子、香煎豆腐——语调欢快，念出食物的色香味；水煮鱼、葱爆羊肉——读出烹饪时热气腾腾的画面。用“点餐大PK”的形式，让孩子在反复朗读中牢牢掌握各种美食的名称。
结尾带上与课文对应的话题标签，比如 #语文公开课 #二年级语文 #小学语文课件 #备课资源 #PPT课件。
按这个结构输出 PDF 内容，字数控制在 500 字以内，小红书标题和正文很快就能成形。
## 五、把兼职老师拉进生产线
工具把效率拉起来之后，下一个卡点立刻浮现：PDF 转 PPT、纠错排版、润色美化这类细活，人工占用太大了。如果全部自己碰，每天能交付的量有限，订单稍一多就会拖慢周期，客户的体验和复购都会受影响。
我在教育行业这么多年的积累里，正好握着一批精准的私域资源——一万名在职一线教师的微信，之前多数时间闲置着，这个项目把它们彻底激活了。
招人方法也很简单：发一条朋友圈，放出一个“课件整理兼职”的招募信息，很快就能筛到合适的人。
我在筛选时只盯几个硬指标：在职语文老师、能稳定拿出空闲时间、熟悉教学课件规范。
流程上做细致的分工：我仍然把控选题、内容初稿、引流、谈单和最终审校；兼职老师承接文件格式转换、排版修整、细节勘误这类重复动作。
结算采用计件模式：单价固定、验收标准明确，几乎不需要额外管理成本。
这一步让我把角色彻底切换过来——不再是没日没夜执行的一线劳工，而是统筹资源的操盘者，个人的时间不再构成项目的上限。
朋友圈文案其实就一句话：“招兼职，负责整理课件，有意私聊。”
消息发出去，来私信的老师就络绎不绝。刚开始我不了解每个人的水平，所以价格一律先砍一半试水——原本打算一课给 50 的活儿，我先报价 20 元一单，用很低的试错成本就把能干活的人挑出来了。后来课件规范逐渐成型，再招人就简单了：把标准文档直接发给面试者即可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_19_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_20_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_21_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_22_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_23_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_24_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_25_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_25_1.png>
## 六、体系跑通之后，再看向下一处空白
内容端由模型批量供给、持续产生新课件；流量端用多台真机每天规律更新，积少成多沉淀自然流量；交付端主打分工协同，订单再多也能接得住；变现端靠单品加套餐搭配，把客单价和回头率同时拉起来——这四大引擎各司其职，完整的商业系统就此跑通。
数字上：月度稳定有 3w+ 净入，旺季月份能冲到 6w，而且这种模式几乎不占库存、没有售后包袱，合规又可持续。
当前收益主要由小红书四个账号贡献，淡旺季感受很明显。收入数据放下面了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_26_0.png>
眼下这个盘子还能再往上走，最明显的空白是短视频板块。接下来我计划系统补齐 AI 视频制作的能力，把现在的课件产品延伸成动态演示课件、课堂重点片段预览，以及记录课件诞生过程的种草视频。
视频比图文更容易形成冲击力，也能更快建立信任感，对私信咨询的转化会有直接帮助；在此基础上还能顺带拉高客单价，衍生出定制课件、整套备课资源包等更高客单业务，收益空间还会再打开一截。
补充一句：小红书目前支持开虚拟店铺，通过第三方渠道就能搞定，办起来挺省事，交点服务费就行。
总结下来，这套打法最核心的启示是：普通人完全可以复制一条“轻投入、无库存、合规可持续”的智能变现路径——上游用模型做内容，中游用工具提效率，下游用协作破瓶颈，剩下的，就是持续迭代的耐心。
很多人第一眼看到这个AI语文课件项目，以为它只是卖卖资料的小买卖。但真正拉开差距的，是一整套可复制的商业化系统。对普通人来说，这套系统的门槛远比你想象中低，核心就藏在下面这五个维度里：
**一、用AI重构内容生产**
选准教师群体高频刚需的细分切口，让AI取代过去全靠人力的创作模式。内容产出的门槛被大幅拉低，同时还能稳定批量输出高质量资源，完全避开热门赛道的恶性竞争。
**二、让流量获取变得可预期**
不走赌爆款的捷径，老老实实深耕小红书这类垂直内容生态。坚持标准化输出，靠日更节奏和搜索流量一点点累积，最终沉淀出稳定且精准的引流管道。
**三、把运营效率交给工具**
凡是重复性、机械式的工作——排版、下载、文件整理——一律交给轻量工具、开源脚本或简单开发来解决。把人力从低效事务中解放出来，一个人也能撑起一条高效流水线。
**四、搭建可拆解的执行系统**
不搞大而全，而是把流程细化拆分。借助私域积累的协作资源，将低价值环节轻量化外包，自己牢牢抓住流量、成交和品控这几个决定成败的关键点。
**五、走一条能长期复利的赛道**
主动绕开盗版和灰产，专注合规的AI原创衍生内容。顺应平台规则与政策方向，让项目既能持续运营，也能不断放大，还能跨学科复制到更多领域。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_27_0.png>
## 十一、核心感悟
说实话，我就是一个普通创业者，技术谈不上顶尖，认知谈不上超前，资源谈不上雄厚。能做出结果，无非是死磕了一件事：找到一个小而美的刚需细分项目，把全流程拆到极致，打磨出标准动作，然后稳步推进、一点点放大。AI时代，普通人不需要什么都会，只要锁定一个真实需求，用AI提效、用工具赋能、用轻协作放大，就能跑出一条属于自己且稳定变现的路径。
————分割线————
看完这篇SOP，你可能觉得已经懂了。但现实是，90%的人实际操作时，连第一步都迈不出去。
工具和教程从来不是真正的门槛，真正的分水岭只有两个：能不能立刻动手，以及你处在什么样的信息圈层。
这里只聊商业闭环的拆解和AI效率的极致挖掘。系统已沉淀1000+验证过跑通的实战案例。
👉 查看圈子完整资源库与加入方式：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_856ecf8b7a3a18ca212cf3c8ae0e67a7_29_0.png>