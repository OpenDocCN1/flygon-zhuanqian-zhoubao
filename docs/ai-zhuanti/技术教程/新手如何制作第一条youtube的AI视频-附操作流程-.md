# 新手如何制作第一条youtube的AI视频（附操作流程）
从零到成片：我的第一条YouTube智能短片实操记录
说实话，开始之前我心里完全没底。没团队、没预算、没剪片经验，一个人对着电脑搜教程硬啃。但啃了几天之后，居然真的做出一条完整的短片。趁热打铁，把每一步怎么做的都记下来了，想入场的圈友可以参考，也欢迎一起探讨。
一、先定方向，再找参考
常用网站先列出来，后面都会用到：
YouTube主站：https://www.youtube.com/
变现查询：https://ytlarge.com/
海外社媒数据：https://socialblade.com
先说Shorts的变现门槛：广告分成需要加入YPP合作计划，两个条件满足其一即可：
1. 近90天内订阅人数到1000，Shorts公开播放量累计到1000万；
2. 近12个月内订阅人数到1000，长视频累计观看时长到4000小时。
我选参考账号的方法是：从自己喜欢的领域切入，筛选已经做出收益的号，观察他们的爆款作品，画面风格上还要找自己上手快的，之后才能逐步延伸创意。
翻数据文档时看到#cat标签下播放量和点赞量排在前面的账号，决定就从这里找灵感。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2e64e71d381a8d3146ef6d2944162eee.png>
点进#cat标签，内容大致两类：真人实拍宠物和智能生成的剧情短片。实拍的事我目前没条件做，于是锁定了后面这一类。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_eb303e773823f2dd38e46584fc7d7ed9.png>
我关注的部分账号和收益情况如下：
https://www.youtube.com/@DailyCuteMeow/shorts
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5140ef5aeb32c52de59d23a197e08660.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0353d5c17a0a0478f54f13b6874e044d.png>
https://www.youtube.com/@Cutecat.2814
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a83be784c0eac6afa9407e46ddb8fed2.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_387e6876aa3258e14161a9c93f910e59.png>
https://youtube.com/shorts/wxG86PG5z0I?si=NaFuHq3quNbdRhn6
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_73bbc807b3ffff1630d2dd4bf44c42f8.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6dec7464a69660547b85d358fa696855.png>
https://youtube.com/shorts/gOj-ObWKeBk?si=CwNSkzPIHSONNx4q
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e0fa56cfda982058a70c23ad1c955b1a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9f4a0a0a2a30e2ba761bf5c9d3a999f1.png>
https://www.youtube.com/@94cat7
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9f6348a5a147fc9839221ea12df09ca5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9d0034baa7e3f22121a1436d30886a8f.png>
选好目标后，我挑了一条热门的短片下载到本地，用到的下载器是这个：https://ytshorts.savetube.me/zh/29-youtube-video-downloader-1jeen2
二、完整制作流程
这次实操用到的工具都整理在下面：
- AI导航站：https://www.ai138.com/#term-13
- MJ中文版：https://www.mj888.net/mjDraw/career
- 即梦（新用户有积分赠送）：https://jimeng.jianying.com/ai-tool/home
- 海螺（图生视频，注册当天无限次）：https://hailuoai.com/video
- 国内免费GPT入口：https://www.chatopens.com/
- 浏览器AI扩展Sider（每天免费额度）：https://sider.ai/invited?c=1da1f41a71ac8544ddc8ae831b1014a0
- 豆包：https://www.doubao.com/
- 智谱清言：https://chatglm.cn/main/gdetail/65a232c082ff90a2ad2f15e2?lang=zh
1）复刻参考画面
链路是：拆帧→提取画面→拆解镜头→写清画面描述→文生图→图生视频→配乐配音→成片。
把下载好的短片放进剪辑工具，进度条拉大一些，方便选定要截取的帧。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_396897c80e618c575e1d7887c3eaaef5.png>
在目标位置上右键，通过“时间区域”→“以片段选定区域”→“静帧导出”，把画面存到本地。之后把这些静帧图发给大模型分析内容。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cdcd7081ecb23fe37a36eb1c7a2011eb.png>
这里有个坑：对话模型一次最多收10张图，所以得分批上传，最后再汇总结果。
下面是我从参考片里拆出来的故事线（以一条猫主题短片为例）：
开篇是晨间离别：客厅很亮堂，大门敞开，阳光洒入，屋外隐约看见白色栅栏。白猫妈妈穿着白色上衣和蓝色长裤，站在门口和幼猫们挥手告别，尾巴轻翘，笑意温柔又带点不舍。
然后是通勤画面：郊区公路开阔，道旁树影快速掠过，天色明净。画面切到她独自驾车，银色轿车行驶在郊野大道上，她目光平视前方，神情轻松从容，仿佛对这一天很有把握。
推进到室内：光线暗了几分，两只小猫坐在毯子上，面前放着点火器和一盒点火棒。橘色虎斑猫胆子大，抓起点火棒试着划火，旁边的小白猫瞪圆眼睛盯着。
火苗出现：橘猫手中的点火棒真的被点燃，他一脸兴奋地看着火，小白猫鼓掌叫好。毯子上的火星已经向外快速扩散。
火势失控：火焰席卷沙发、挂帘和地面织物，屋里到处是火光。两只小猫终于反应过来，害怕得直往后退，互相贴紧，尾巴夹着，身体缩成一团。
屋外视角：黑烟从窗缝和门缝不断涌出，屋顶已经烧起来，火光把窗户映得透亮，一眼就知道出事了。
救援出动：红色消防车闪着警示灯，在城市道路上疾驰，鸣笛声似乎能穿屏而出。夜色里，车灯与警灯交叠，张力拉满。
超市来电：她推着一辆购物小车，手机忽然响起，接起后脸色立刻变了。货品塞满小车，她的心思却已经飞回家里。
归途狂奔：银色轿车在路上飞驰，远处天边升起烟柱。她双手握住驾驶盘，表情严峻，一秒都不敢耽误。
目睹火场：站在自家屋前，大火映红了一切，黑烟翻卷。她双手抱头，弯下身子，眼里蓄满泪水，整个人写满了绝望。
场景和角色理顺后，让大模型据此生成一组绘图提示词。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_178d2fa7ef886da0d8aeb7d91135f54b.png>
拿到提示词后喂给绘图工具，实际效果需要反复调整。为了控制预算，我试了三种方案：国内版GPT、即梦、MJ。国内版GPT出图偶尔卡顿，二次改动也麻烦；垫图之后即梦和MJ的表现更优。MJ中文版我是先在淘宝买体验卡试的。
图生视频环节，我主要用即梦（每天60积分）和海螺（注册当天不限生成次数）。有一点建议：先把图全部做好，再找一个时间集中处理，把海螺的免费额度用满。
即梦：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_641f80f4fddff1231c15ea71f79f0256.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9e916e43ba8ac2d15af707f72c5f9150.png>
MJ：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c1651be44870a7145cbd76ff4011cc4c.png>
生成好的片段按故事顺序放进剪辑软件。背景音乐提取自YouTube上miaomiaomiao博主发布的视频，直接搜Bongo Cat也能找到：
https://www.youtube.com/results?search_query=Bongo+Cat
https://www.youtube.com/shorts/h1qQt-lZycU
具体做法是把参考片下载到本地，在剪辑软件里提取原BGM，再找合适的音效补上去。
还有个小问题：AI绘图导出的图片通常带着网站水印。我的土办法是拉近画面，让水印直接出画。如果有更高效的去水印工具，欢迎分享。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d7ea95cb114b0ee6918900d494dd0a9c.png>
最终成品就是这样：
2）后续如何延伸
照着别人的模板做，我自己也担心被判搬运。所以前期只用来熟悉流程，后续准备写原创故事。大概的思路是：先写故事脚本→再分镜头出图→把图片按顺序生成动态→配上音乐→导出成片。比如下面这组：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8c4081160f630c5c31a0743c3971d9ef.png>
即梦的出片效果：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0cad7eebeadb5f7184b77cd971a3fd71.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1f71c5abd737db527c27b34666aaff4e.png>
除了猫咪，我在#animals和#funny标签里还刷到其他动物类的智能生成内容，画风相似，也都很擅长讲家常故事或者抓人情绪的小片段。随手整理了几个：
狗狗剧情向：
https://youtube.com/shorts/DlS7aIsfQOU?si=1x9ziStMSYRbi7Mn
狗狗节奏向：
https://youtube.com/shorts/WaKu3cVIB2c?si=VWkQgMXZE4MKncXg
兔子剧情向：
https://youtube.com/shorts/7CRSVC8Qb_M?si=OAhE8uwUYht-F7_j
多动物账号：
https://www.youtube.com/@Todd_AI_Animal
多动物图片动效：
https://youtube.com/shorts/glGtEUD-hPA?si=jRfLQZ_wJ9hHmQkL
https://youtube.com/shorts/bP0cdPtNUZY?si=J845gLiNg0FbyJ7B
https://youtube.com/shorts/8K4mO16lqb4?si=Y24yWaRJvulDEAfs
热门动画IP混搭动物：
https://youtube.com/shorts/vxRM-Mil354?si=1Iiml_3KhutN9TET
我现在也还在学习阶段，很多玩法需要继续试。欢迎更多同路人来交流，一起把这些技巧打磨到位。
最近发现，AI宠物视频这个方向已经有不少创作者在做了，尤其是猫咪类内容，赛道明显有点挤。所以我在想，之后可以试着把提示词换成其他动物来生成视频，这样或许能避开同质化，做出点差异化。
再说说我目前遇到的问题和短板：
一是对YouTube平台和整个赛道的玩法还不够熟悉，得多刷多看，找找感觉和灵感；
二是平时用AI工具和剪视频的频率太低，很多时间都耗在摸索各种软件上，这块需要重点补课；
三是现在基本是在模仿对标视频的画面来制作，也担心内容太像会影响后续变现，所以希望在熟练操作之后，能慢慢尝试一些自己的风格。
近期的打算是这样的：
一方面，系统梳理赛道里的账号和爆款内容，明确选题方向；
另一方面，每天拆解一条AI短视频，从剧情、风格到剪辑手法都过一遍，同时认真学习AI工具的使用和剪辑技巧，比如怎么结构化地引导AI、如何写出更精准的提示词、怎样搭建自动化工作流等等，把创作效率提上去。
最后想说，愿我们都能在行动里找到适合自己的赚钱方法，做出让自己满意的作品！
感谢观看～