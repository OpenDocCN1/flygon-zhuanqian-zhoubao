# 【Coze保姆级教程】一键生成爆款视频
作者：龙哥

不藏了！用扣子（Coze）批量产出爆款视频，手把手全流程指南

诸位好，本人富百。平时做油管视频，也帮人搭自动流水线，挂了个“youtube深海圈教练”的牌子。前些日子被约去线下做了场小范围分享，主题就是用扣子（Coze）把视频制作全流程自动化。我从下午2点一路讲到晚上7点多，五六个小时的干货，20位圈友全程没走，也没有人提前离场——这就是最让我开心的反馈。还要感谢子安的邀约，让我对扣子更熟稔，也认识了一帮爱钻研的伙伴。

![](img/64a6c90a00a30f6c5dcb8a78004ea8e9.png)

与此同时，龙哥前两天给n8n发了个重磅标签，结果n8n的航海报名人数直接破了2000，扣子这边只有500人。好在两个生态我都玩过，想给刚入行的朋友指个方向：什么样的人适合n8n，什么样的人适合扣子。

我的判断标准，一共七条：

一、先看业务。做海外市场的，闭眼选n8n——它对外网服务的接口覆盖极全。内容沾了擦边嫌疑的，也选n8n，因为扣子对内容审核更紧。在国内做正规业务，那就用扣子，上手容易，搭建还省钱。

二、看学习成本。我当初刚摸到这两个平台时，明显感觉n8n要花的时间大约是扣子的两到三倍，这还是在我已经理解自动原理的情况下。换作零基础小白，n8n的难度可能要乘以五。

三、看操作界面。n8n整个面板都是英文，风格偏老派，像是给懂代码的人准备的。扣子的操作面板则清爽直观，一眼能看明白，也更符合普通人的使用直觉。n8n的界面是这样的：

![](img/9dfb40701aceb749cd7b80ff8ba17fe9.png)
![](img/73f1818e28055c6788bfad12d079c9df.png)

扣子长这样：

![](img/56789b43c9d18e4fce229e5ef4f6f3c4.png)
![](img/62d3369f9dc4a0b03a4574ecc616827e.png)

四、看真实需求。多数人的用途就是调调语言模型、生成图像，这类流程扣子处理起来很轻松。它还有个画布工具，做📕图文尤其顺手，而n8n反倒没有这个能力，即便要模仿，也折腾得很。

![](img/c2061e9e8a73f9ab54c13f0f12784f8f.png)

五、看预算。扣子和即梦同属一个生态，在扣子平台内调用即梦的图像生成模型，单价只要0.025元；而走即梦的API，一张是0.2元，差了8倍。因此扣子特别适合做图文向、图片导向的视频流水线，成本差了一个量级。举个例子，用即梦图做的视频，放扣子只要8块，搬到n8n就变成40块。

![](img/8550f74882ab2df330f6cec56dbfddf6.png)
![](img/7f0a141ba349d6e647b0fc49c2c570a0.png)

六、看插件。速推这家公司已经把剪映工程相关的接口封装成插件，这让扣子在视频流程上格外省事。我接下来分享的流程，正是靠这套插件跑通的。而这个插件在n8n那边暂时是空白。

七、看模型兼容。扣子也能接国外LLM，借助中转服务就行。比如下面就是用某个中转渠道接入的Claude模型，书虫自己搭的渠道也可以。

![](img/6ef246f0ca215b302fc8491511efacfa.png)

总之，先盘清楚自己的业务，再对照这七条选平台，别把时间浪费在不合适的工具上，最后拿不到想要的结果。

接下来，把线下分享的精华内容也同步给你。

扣子平台的核心能力大体有三块：

1）流程编排：能产出文字、图片、视频等AIGC内容，也能做日报汇总、数据追踪，以及从非标文本里抓取关键信息。常见用法有：快速产出📕图文笔记、批量出不同风格的视频、按标签给客户分组推送节日关怀并定点投送。

2）Agent：把若干流程包装成对话式助手，根据用户的意图调用对应流程，体验很自然。适合搭建公司知识库，帮助售前售后、销售团队快速检索与答复；也能做自动应答机器人、出策划方案、设计行程等。

3）API：把流程或Agent接进外部系统，解锁更多玩法。

视频流程案例拆解：

![](img/0ae5aad5bc1f4c6933454962e12c8804.png)
![](img/7cf65ac8a47f1b7f91218895df97d543.png)
![](img/31dcfa60c3aee1e21ce76145a6bf8e58.png)
![](img/fd8368a978564c5c1a0b78a45657b7d9.png)

- 解说历史名人生平：https://v.douyin.com/zUpjbRnAi9k（图一）
- 火柴棍小人心理动画：https://v.douyin.com/y88c6TbaJxU/（图二）
- 油管英文叙事账号：https://www.youtube.com/@HopeStories-us/videos（图三）
- 油管英文叙事账号：https://www.youtube.com/@BlackThreadYT（图四）

上面四条视频都是由流程自动做成的。前两条来自抖音，后两条是油管的英文叙事账号。可见机器产出的视频同样能爆，而且并不罕见。图三与图四还用了同一套模板——前面两幅图先做动态效果，后面直接放静态图轮播。

抖音、视频号、B站、油管上，大量“纯图短视频”和“简易AI动效+图”那类内容，都能用流程做批量产出，形成矩阵。它们之间的差异只在文案质量和赛道选择，换一条新赛道，同类内容还能再火一回。翻翻圈友帖子，不少视频号、抖音上的荐书号就是这么玩的。

接下来是实操：以历史题材为例，手把手跑通一条自动视频流程。

先看全貌流程图：

![](img/94ced8999313d4055f322cc464535c3c.png)

整个环节分三大段：第一段让LLM产出文案与绘图prompt；第二段负责准备图片与音频素材；第三段把这些素材合成剪映工程文件。看起来复杂，但掌握这套方法后，几乎所有以图片为基础的流程你都能自己复现和微调。所以别急，一步步来。

具体操作：

第0步：新建流程。

![](img/a50a4a3fe3d167a702036efb3eaee1d9.png)

在弹出的界面点“确认”，即完成创建。

第1步：配置入口节点。

![](img/5a218b1ab60550e212bbf700c45f73f1.png)

把参数名改成 `zhuti`。

第2步：配置文案生成节点。

![](img/2ecae69f6d54c677e8d4ce697f1ecc22.png)
![](img/b0ffdc484c54aaed7fe9e39a058de1a4.png)

模型可以选 DeepSeek 的 V3-0324 版本；参数 zhuti 对应好入口处的 zhuti 就成。另外记得给节点起个清晰的名字，后续引用变量时全靠名称来区分哪些数据该接哪，名称不乱，流程再大也好认。

![](img/5b06c8cd5bb555fbf4a43bd755f07bd4.png)

系统指令就填下面这段：

```
请根据用户提供的【主题】，按照以下结构生成一段历史类短视频口播文案：

1\. **悬念开场**：以“【朝代/场景】+ 反常识疑问/断言”开篇，激发观众兴趣（例：“古代【某职业】真的比【对比对象】更【形容词】吗？”）。
2\. **身份代入**：用第二人称“你”描述主角身份、时代背景及面临的致命危机（需包含具体官职/处境/对手）， 不要出现“想象一下”等过渡词，直接进入主题。
3\. **冲突升级**：
   - 第一层：外部压力（如敌军压境、上级压迫、天灾降临）
   - 第二层：内部瓦解（如下属背叛、资源短缺、疾病蔓延）
   - 第三层：道德困境（如忠义两难、屠城抉择、政斗站队）
4\. **破局细节**：主角采取3个递进动作，包含：
   - 震慑手段（当众处决/焚毁证据）
   - 心理博弈（离间计/匿名信）
   - 终极底牌（隐藏密件/借势压人）
5\. **主题收尾**：通过主角结局（惨胜/悲壮失败）引出金句，揭示历史规律（如“权力本质/战争真相/人性弱点”）。

参考文案：
参考文案1：
在古代，当一个七品县令真的比做皇帝还爽吗？你是一个七品县令，听着像是芝麻官，实际上却管着一线生杀。你到任第一天，文案积压，吏园散漫，商人压税，盗匪频繁，所有人都在盯着你，想看看你这个读书人究竟能撑几日。于是，你命人将城中四大银行、三大米商召来，说了一句话，自今日起，税从清征，人从严制，谁敢藏奸瞒骗，先抄家，再杀头。众人皆笑，你却不恼，只是冷冷记下每人姓名，派人查账。三日后，你当街砍了一个米商账房，把人头挂在城门口。不久，其余几家主动上门认错，乖乖交税送礼，百姓自此称你为顾青天。你从不自称清官，但你知道，在这地方，拳头和律法并重才叫威望。一个月后，你已经在县城里站稳了脚跟。天还未亮，衙门门口已跪满人。左边是乡绅土豪求你叛帝，右边是盐商粮商给你送礼，你打了个哈欠。走出卧房后堂，十几名婢女簇拥着为你更衣梳发。你才刚坐下，茶就端来了，不是普通茶，是百里外送来的贡品。龙井三千银子一斤，一口下去，香气绕喉。你懒洋洋的抬眼看着堂下跪着的众人，手一挥，先问田地安，其余让他们在外等着。话音未落，师爷立刻应声，堂上传来惊堂木声，升堂在云阳县，穷人看你是神，富人把你当祖宗，就连知府大人来视察，都得先送一船好酒，再送一个歌妓，才敢上门拜访。你笑着收下他来视茶，你派人抬着软轿出城，五里相迎，不是给她面子，而是要让他知道，你虽然是七品，但这云阳县早已是你的天下。你升任第三年的秋天，县衙后库突发火灾，你亲自查探火因，结果意外发现一批私盐帐簿署名竟是你手下最信任的书立李记。你震怒，立即将其缉拿，却在其家中搜出一封未寄出的密信，写明这批私言背后勾结知州卢大人，牵连州府多名官员。你这才意识到，你触碰了这片土地上最不能动的那条线。延说，第二天你才刚出堂，就有人呈上一封匿名举报信，连你的私房收礼记录都一应俱全。你第一次感到这不是污蔑，这是操盘已久的杀局。知州大人紧急来访，私下告诫你有人要动，你背后牵的是京城兵部与阎道衙门，你得自己找活路。你立刻封锁案卷，亲自入库查账，发现那些伪账本竟源自你手下最信任的书立。你将其关入大牢，一审才知他的妻儿被人挟持，只得从命栽赃你，你这才意识到，自己就是那块要被剃掉的棋子。第二日，你还未来得及申辩，便接到了停职审查的诏书。知州亲率提其封了你的书房后堂暗牍，你如过街老鼠，众人避之。你低头无语，却没有认输，跟你早有后手。你连夜写密折命心腹快马送至京中清流大臣门下，可三日后却传来噩耗，送信之人马踏山崖，尸骨无存。此刻，你彻底陷入死局，这时钦差已入陷，兵部主事钦来查办，你被软禁在后堂，你以为你的结局将与前任三位县令无异，都死于意外。正当你思索破局之法时，昔日曾受你父亲庇护的朝中高官命书立偷偷送来一封信，信里竟藏着一张对账残页，印有兵部大员亲笔落款与黑岩交易详情。你明白了？他们大意了。栽赃太快，忘了悔证。7日后，钦差升堂审你。你披发跪堂，血衣染袍，众人以为你彻底崩溃了，你却突然从怀中掏出那张残页，当众高喊，我顾怀珍，问心无愧。今日一命换一局，看天子信谁。钦差当场变色，百姓哗然。而你早已让人将密政副本藏匿。一旦你死，城门口便贴文告公示。这一次，他们不敢动你。钦差低头退堂，3日后急返京城，再五日，圣旨亲临。顾怀贞未曾贪墨，实为中职之臣，留任云阳县专责清查南沿岸。你身披旧袍，眼中血丝未退，但腰杆挺直如初。你看着天轻声念叨我顾怀珍，就算是七品芝麻官，也能让权臣避让百官低头。那些试图吞下你的权贵，一个个被抄家砍头，这回你虽然没有升官，但却赢得了天下最难赢的那一局。

参考文案2：
一个汉朝使者竟在敌国当众砍了国王的人头，却没人敢多说一句话。今天我们讲大汉最狂使者班超，你是一名大汉边疆的普通士兵，略懂一些西域语言。这天长官班超突然发话，你准备一下，后天随我出使西域。你心头一紧，西域远在万里，危险重重，去过的使者几乎全都被砍了。可班超的眼神告诉你，这个任务不容你拒绝，行进的路程异常艰难，漫天风沙遮蔽了天际。一路上，你多次冒出逃跑的念头，可李智告诉你，脱离了大部队也是死路一条。三个月后，你们终于抵达了第一站楼兰。你早已听说过这里的危险，楼兰国王血腥手段让无数使者丧命于此。大殿内，楼兰国王坐在王座上冷眼看着你们周围的侍卫目露凶光，气氛紧张的让你几乎无法呼吸。你担心班超要是说错话会连累大伙被处死，不料他毫不畏惧的走上前，直指国王的鼻子，怒骂道，你这背信弃义的狗东西竟敢欺骗盟友匈奴使团从你这经过，竟然不告诉老子怎么是不是翅膀硬了？说完，班超看向你，冷声道，翻译给他听。你心头猛然一惊，差点喷出一口老血，但还是战战兢兢的翻译给国王听。国王怒吼道，你信不信我现在就砍了你。然而令你意想不到的是，班超不但没有害怕，反而把脖子凑了上去，挑衅道，来来来，朝这里砍不砍你是我孙子。此话一出，你被惊得愣在了原地，冷汗浸湿了三层衣袍，只听班超继续说道，南越杀我汉使，九郡被夷为平地，大碗杀我汉室，国王的脑袋被挂在城门上。今日你若杀我，明日汉军便会举国而出，屠径你楼兰数辈，而我的子孙会受到封赏，我也会名留青史，老子求之不得。你站在旁边心跳如雷鼓，仿佛下一刻就会被拖出去斩首，但令人惊讶的是，楼兰国王非但没有下令砍了你们，竟然还低头认错，表示愿意重新恢复大汉。一时间你被震惊的愣在了原地，我大汉朝啥时候那么硬气了？在别人的地盘上训斥他们的国王，如同老子训斥儿子一样。但更令你惊掉下巴的事还在后头，你们继续前行，来到了善善国。国王的礼遇让你觉得这一次可能是个顺利的任务。然而随着几天的相处，你渐渐察觉到不对劲，善善国王的态度开始变得冷淡，班超肯定也察觉到了这一点，过了几天，他把善善王的亲信叫了过来，语气平静却像刀匈奴的使者来了吧，打算待几天。一句话把对方吓得脸色发白，哆嗦着回道，五六日，你惊愕的看着班超，他没有直接询问匈奴使者是否到来，而是问得极其巧妙，仿佛早已知道一切。你心里发凉，36个人被困异国，如果善善国王决定投靠匈奴，你们所有人都将命丧于此，成为他的投名状。夜晚寒风凛冽，班超召集弟兄们喝酒。酒过三巡，他忽的一拍桌子，兄弟们，我们被困异国，国王已变脸，说不定哪天就把我们绑了送给匈奴。我们死在这，不会有墓碑，不会有人记得。如今这局面，你们说该怎么办？有人先喊了一句，无论是死是生，我们都听你的。接着你们36人齐声应下班超点头，冷静的不像是要杀人的将军，更像个写好了剧本的导演。我去匈奴营上放火，你们埋伏在出口，火势一起，谁跑出来就砍谁，谁敢逃就射谁。深夜风大如刀，班超点燃火把扔进匈奴使者的驻地。火光腾起那一刻，你心跳几乎停了，敌人惊慌出逃，你们早已守在四周，一刀一个。惨叫声4起，匈奴使节头颅飞溅，愚者被活活烧死。次日一早，班超提着一颗焦黑的脑袋，亲自去见善善国王。你跟在他身后，手还在发抖，只见他将人头扔在国王前，冷声道，既然你犹犹豫豫，那老子就替你做个决断，投靠谁国，自己看着办。国王脸色煞白，当即俯首称臣。不久后，单善国归附，震动西域。你实在忍不住轻声问他，我们这样是不是太霸道了？班超没回头，只是眉头一皱。他们弱却不谦卑，贪却不识相。你给他们脸，他们觉得你好欺负。你不拔刀，他们就敢骑在你头上拉屎。接下来的日子里，班超带你们在西域各国大闹一通后，还是不满意，因为这些国家只是迫于压力，表面沉浮。日后一有机会，他们还是会反水。于是他主动向霍光大将军请命，说要干一票大的。霍光大将军听了只淡淡一笑，不错，可以先拿楼兰国王来练练手。你听到这话，整个人僵在原地。练手？你们才多少人？三十几人而已，要去杀一个国王，颠覆一个政权，这不是练手，是送命啊。但你看看班超，他脸上没有一丝犹豫，你开始害怕，甚至比第一次跟他出使还要紧张。但你心里也清楚，一旦你们失败，大汉铁骑必定杀回来，到时候敌国血流成河，而你将作为烈士。这一次，你们带了满车金银，说是天子赏赐，与楼兰国君重修就好。小小楼兰国王见到这些宝物，两眼都直了，笑得比狗还谄媚，酒也越喝越猛，话也越说越飘。班超看向你只是一个眼神，你立刻明白，你悄悄带着另一个兄弟绕到屏风后等候。他走到国王耳边低语，天子密令，需要私下传话。楼兰王晃晃悠悠站起，毫无防备的走向你们。你屏住呼吸，手紧握剑柄，他刚一露头，班超眼中寒光一闪，剑刃贯穿心口。楼兰王连叫都没叫出声，瞪着一双死不瞑目的眼瘫软倒地。屏风外的文武百官当场傻眼，气氛一瞬间炸裂，有人握住了刀柄，有人咬牙低吼，啪板朝一声怒喝，酒被应声砸碎，谁若敢动，老子灭了你楼兰。小波一字一句像从地狱里拉出的声音，你也不知道他们到底怕了谁，怕班超，怕你们，还是怕背后那个庞然大物大汉。总之，他们全傻了，一个个低着头，连呼吸都小心翼翼。你们就这么砍下国王头颅，从人群中走出去，没有人拦，没有人动，你仿佛看见了卫青的铠甲，霍去病的战马，汉武帝的目光，还有那压在整个西域上空的大汉铁骑。你走得越来越稳，步子越来越大，头颅越抬越高，体梁越挺越直。这一刻你真切的为自己身为一个大汉子民而骄傲。

参考文案3：
古代战场上的瘟疫真的比敌人的刀剑更可怕吗？你是一名普通的宋朝士兵，此刻正坚守着一座即将被金军攻破的城池。就在敌军将要爬上城楼之际，你冒死将一架攻程梯狠狠推翻，鲜血混杂着汗水滴落在你的盔甲上，数日的厮杀抵抗使你浑身疼痛，但你依旧拼尽全力。终于熬到了半夜，敌军的攻势退去，你扶着刀柄浑身颤抖。原以为熬过了这一波攻势便能稍作喘息，却不知更可怕的敌人早已悄然逼近。午时3刻，你正趴在墙角休息，突然一具尸体从空中坠落，重重的砸在你脚边，顿时间血浆4溅。只见城外敌军竟然将死去士兵的尸体绑在投石车上，纷纷投入你们驻守的城中。尸体在半空中划过一道诡异的弧线，砸落在城内的街道上，散发出阵阵恶臭。你站在城墙上满心疑惑的看着这一幕，城中士兵甚至好奇的凑近尸体观察，却未料到一场灾难正在悄悄蔓延。夜幕降临，营地里弥漫着诡异的寂静。你窝在狭窄潮湿的帐篷里，伤口隐隐作痛，身边战友低声咳嗽着。你递给他一口水袋，却看到她的额头上渗满细密的汗珠，脸色惨白如纸。兄弟，你没事吧？他摇摇头，勉强挤出一个虚弱的笑容，没事，睡一觉就好了。你安慰自己，或许只是一场风寒罢了。次日清晨，你被惊叫声惊醒。掀开帐篷，映入眼帘的是令人毛骨悚然的一幕。营帐外躺满了奄奄一息的士兵，个个面色青黑，口唇干裂，有人甚至瘫倒在地，挣扎着向前爬动，眼神里充满了绝望。军医惊恐的喊道，不好，是瘟疫。你的心猛然一沉，汗毛倒竖。将军急忙下令隔离病患，但帐篷早已塞满了呻吟的病人，军中恐慌迅速蔓延，没人知道下一个倒下的会不会就是自己。几日之内，军队士气瓦解，敌方的探子传来消息，宋军染棘，已无战力，敌军趁势攻来。你们这些幸存者仓促应战，但手中的刀剑却仿佛重于千金。你看着一个个面容憔悴的战友倒在自己身边，敌人的刀还未靠近，他们便已因疾病虚脱而倒下。城破那日，你被敌人俘虏，眼睁睁看着自己驻守多年的城池被付之一炬。被俘的路上，你听敌兵闲聊，多亏了这一场瘟疫，否则城池哪能这么轻松的攻破，你心中一阵苦涩。押解途中，你与其他战俘被关进一处偏僻村落等待处理。夜晚守卫，昏昏欲睡，你趁机挣脱绳索逃出，却发现逃亡之路更加艰难，一路上尽是荒村野尸，家家闭户并漂遍野。你踩着尸骸踉跄前行，所到之处如同人间地狱。你明白，瘟疫比战争更无情，它不分敌我，只留下一片焦土和尸骨。几经挣扎，你终于逃回故乡，却发现村庄早已空无一人，唯有乌鸦的哀鸣在回响。你失魂落魄的走进家门，地上躺着父母冰冷僵硬的尸体，桌上还有未曾吃完的晚饭。你跪倒在地无声的痛哭。就在此时，你感到身体传来一阵剧痛，低头一看，手臂上赫然出现了与战友一样的黑斑，你颤抖着手摸向额头，已示滚烫如炭火。此刻，你才惊恐的意识到，自己也早已成为瘟疫的牺牲品，只是一直苦苦挣扎，不愿面对。耳边依稀响起昔日战友的叹息，原来我们才是这场战争真正的失败者。临死之际，你终于明白，战争胜负的背后，瘟疫才是真正的主宰。

**要求**：
- 每段不超过3句话，多用短句制造紧张节奏
- 加入至少2处历史专业术语
- 在关键转折点使用感官描写（气味/触感/视觉冲击）
- 结尾以“这一刻你终于明白…”句式点题
- 生成1000字左右口播文案
- 文案由长短句构成，遇到长句会用逗号分隔成短句，每个短句不能超过19个汉字

**输出要求**： 只输出口播字幕文案，不要输出其他任何额外内容，不输出分段说明
```

关于用户指令的配置方式，说明如下：

```
主题：{{zhuti}}
```

重要提醒：
最终结果应当以 JSON 结构返回。字段 content 需要声明为 String 类型，用来存放待分镜的视频脚本正文。

## 3）分镜生成节点

![](img/1cfd99988d2f484ac3e3ec6c404de6ee.png)

节点配置如下：
- 选用的 model 为 DeepSeek-V3-0324。
- 上游数据取自“按主题起草脚本”节点的 content 字段（String）。
- 把当前节点改名为“LLM_分镜”。
- 系统指令填写下方区域：

```
# 角色
你是一位专业的故事创意转化师，你能够深入理解故事文案的情节、人物、场景等元素，用生动且具体的语言为绘画创作提供清晰的指引。

## 技能
### 技能1： 生成分镜字幕
1\. 当用户提供故事文案时，仔细分析文案中的关键情节、人物形象、场景特点等要素。
2\. 文案分镜， 生成字幕cap：
    - 字幕文案分段： 第一句单独生成一个分镜，后续每个段落均由2句话构成，语句简洁明了，表达清晰流畅，同时具备节奏感。
    - 分割文案后特别注意前后文的关联性与一致性，必须与用户提供的原文完全一致，不得进行任何修改、删减。字幕文案必须严格按照用户给的文案拆分，不能修改提供的内容更不能删除内容

===回复示例===
[{
          "cap":"字幕文案"
}]
===示例结束===

## 限制:
- 只围绕用户提供的故事文案进行分镜绘画提示词生成和主题提炼，拒绝回答与该任务无关的话题。
- 所输出的内容必须条理清晰，分镜绘画提示词要尽可能详细描述画面，主题必须为2个字。 
- 视频文案及分镜描述必须保持一致。
- 输出内容必须严格按照给定的 JSON 格式进行组织，不得偏离框架要求。
- 只对用户提示的内容进行分镜，不能更改原文
- 严格检查 输出的json格式正确性并进行修正，特别注意json格式不要少括号，逗号等
```

- 用户指令填写下方区域：

```
故事原文内容：
{{content}}
```

- 返回字段 scenes 使用 Array<objets> 类型，并在该结构中附加 cap 下级字段。

![](img/d8401d45cabb51fdace4390870aa4b18.png)

### 理解 Array<objets> 结构
- Array 的意思是数组，即一组有序项。
- 数组中各项均为对象（object）。
- 对象通过 key-value 组合来定义，写法示例：{ "k1": "v1", "k2": 18 }

![](img/f654941e65be1587ad33aa2d8620beec.png)

## 4）图片 prompt 生成节点

![](img/d86f86ecec13ed11c7d048c56e063292.png)

节点配置：
- 把节点改名为“LLM_图片 prompt”。
- model 选用豆包的 1.5 Pro 版本。
- 上游数据来自“LLM_分镜”节点的 scenes。
- 系统指令如下：

```
# 角色
根据分镜字幕cap生成绘画提示词desc_prompt。

## 技能
### 技能 1:  生成绘画提示
1\. 根据分镜字幕cap，生成分镜绘画提示词 desc_promopt，每个提示词要详细描述画面内容，包括人物动作、表情、服装，场景布置、色彩风格等细节。
  - 风格要求：古代惊悚插画风格，颜色很深，黑暗中，黄昏，氛围凝重，庄严肃穆，构建出紧张氛围，古代服饰，古装，线条粗狂 ，清晰、人物特写，粗狂手笔，高清，高对比度，色彩低饱和，浅景深
  - 第一个分镜画面中不要出现人物，只需要一个画面背景

===回复示例===
[
  {
    "cap": "字幕文案",
    "desc_promopt": "分镜图像提示词"
  }
]
===示例结束===

## 限制:
- 只对用户提供的json内容补充desc_prompt字段，不能更改原文
- 严格检查输出的 json 格式正确性并进行修正，特别注意 json 格式不要少括号，逗号等
```

- 用户指令如下：

```
故事分镜字幕信息：{{scenes}}
```

- 返回字段配置：

![](img/311b7dbf8cb792dc0378c2d5fafb372a.png)

## 5）批量处理环节

![](img/8be4d38fceb92774bcccac13d8dbd9e4.png)

![](img/f821811efcd54519401cb661878961bb.png)

![](img/3ba1673c70358d5d717aa28542798b8e.png)

本环节负责接收上游数据并输出结果。

### 5.1）图片生成

![](img/98ef5345074deb8b3bb2add2c49f89b6.png)

![](img/422e0b100e84b09dbdf591e8c5b5f3f2.png)

将 model 切到 Pro 通用档位
画面比例设为 4:3
把质量档位调到最高
prompt（正向）：复古恐怖美术样式：{{desc_prompt}}

### 5.2）条件分支器

它类似开发时的分支逻辑（if-else）。当上游数据发生变化，需要切换不同工具时，就交给它来分流。
运作逻辑：上游数据 → 规则匹配 / 手动指定 → 触发对应流程。

![](img/83cf5de2c0ba26b6abeb9af6d224bd1d.png)

![](img/35086fa084a5afafd676a6927e256b6a.png)

### 5.3）自动润色与重绘

自动润色 prompt 并重绘画面，主要是为了避免某些词触发拦截。系统会在后台自动修正 prompt，从而让整个流程更稳定、更健壮。

![](img/2741ca0b81b68d0f8e08a138d9bf9549.png)

![](img/e8b6aa4c4430ed673e37e581f72e9025.png)

### 5.4）再次图像生成

![](img/eec9d5d1d17872d282302bfb5ac6ead8.png)

![](img/639654529dfa67226b23f14f511e657d.png)

### 5.5）变量聚合

变量聚合本质上是一个容错兜底机制。当主图的生成环节因为违禁词被拦截，导致返回值为空时，系统会自动取用图像生成_1的产出作为替代。换句话说，该节点可以串联多条分支，按先后顺序寻找第一个非空结果作为最终交付。

举一个例子，准备 output1、output2、output3 三个出口按顺序合并到 Group1。判定逻辑是：先看 output1 是否有内容，有则直接赋给 Group1；若 output1 为空，就去读取 output2 的内容，以此类推，直到命中第一个可用值。

![](img/bb151b22211cee38e028f47f3aabc556.png)

![](img/e4d3c5ce47365560a84cb4a71c776dec.png)

### 5.6）音色与文本合成音频

![](img/042716fee4dc9f4535c1890a39559695.png)

![](img/7b98f6063a85ea26b46ac8fcacd1e1dc.png)

进入音色面板后即可浏览内置的预设声线，支持试听对比，挑出最符合人设的配音。

![](img/3e39efd8fb5391cb893641d967899809.png)

![](img/75978860f7dd193fd1e9e7e0231df6fb.png)

音色总表

https://www.coze.cn/open/docs/dev_how_to_guides/sys_voice

### 5.7）get_audio_duration

https://www.coze.cn/store/plugin/7457837529027493922

https://www.coze.cn/store/plugin/7475816084453654580

打开上述两个地址把插件加入收藏夹，后续在节点库里就能直接看到已收藏的组件，调用更顺手。

![](img/b0cea59a25e6646c15c08a8f28180828.png)

![](img/f320aa022f9cedfc7699a3ed2a06556f.png)

![](img/3b558efee33aec08f1e54e51c702ccc6.png)

用途：统计每段音频的实际时长，为后面拼装剪映草稿提供时间参数。

![](img/afe7fd607ef9c13bda52e7304a1cfa3c.png)

![](img/a376cf8c5ccc01cca798feecec2d4434.png)

## 6）大模型_主题生成

![](img/29748f65792473cc266c45b8ec4b96e0.png)

![](img/c1fd97173d93e434fe5b1210a6610a7f.png)

系统提示词请填写以下内容

```
# 角色
能够深入理解故事文案的情节、人物、场景, 根据故事内容提炼出简洁精准的2个字故事主题素。

## 技能
### 技能1：生成2个字的主题
1\. 从故事文案中提炼出能够精准概括故事核心内容的2个字故事主题

## 限制:
- 只围绕用户提供的故事文案进行分镜绘画提示词生成和主题提炼，拒绝回答与该任务无关的话题。
- 主题必须为2个字。 
- 直接输出主题，不要回复其他额外内容
```

用户提示词请填写以下内容

```
故事原文内容：
{{content}}
```

输出字段

titie:String格式

![](img/22ebc1a718b187a0b87b5abb583bb9e8.png)

## 7)大模型_主角首图

![](img/46174ff08ef88af093bdbe62a1e88cae.png)

![](img/a923acab631c9b05fc5eaeb78cc7342b.png)

系统提示词请填写以下内容

```
# 角色
根据故事信息生成故事主角开场绘画提示词desc_prompt。

## 技能
### 技能 1:  生成绘画提示
1\. 根据故事信息，生成主角任务绘画提示词 desc_promopt，详细描述人物动作、表情、服装，色彩风格等细节。
  - 风格要求：古代惊悚插画风格， 背景留白，颜色昏暗，黑暗中，黄昏，氛围凝重，庄严肃穆，构建出紧张氛围，古代服饰，古装，线条粗狂 ，清晰、人物特写，粗狂手笔，高清，高对比度，色彩低饱和，浅景深
  - 画面只需要出现一个人物，背景留白
  - 人物需正对屏幕，人物在画面正中间

# 限制
1\. 只输出绘画提示词，不要输出其他额外内容
```

用户提示词请填写以下内容

```
故事信息：{{content}}
```

输出字段

desc_prompt:String格式

![](img/b5e77c4cb67f45d947add79f0d6db56e.png)

## 8)图像生成_主角首图

![](img/410c457d426f791c9db403cd176695c1.png)

![](img/faf1d8833173f79f352fea13c300fd36.png)

正向提示词

```
{{desc_prompt}}
```

9)cutout_智能抠图

在节点库里检索“抠图”关键词即可定位到该工具

![](img/9497203f892ff89b8437ff5d17ac784d.png)

![](img/9c3472fc3348446c5e7e4ad5ac9411ed.png)

## 10）剪映草稿模块

![](img/2d664b9b109705e2e519a6069d3f0600.png)

剪映草稿本质上是一段可被识别的结构化脚本，本流程要做的工作就是把素材整理成剪映能读懂的格式。

一条成片通常由音频、画面、字幕三大部分构成，同时还可能涉及音效、文字层、背景乐以及关键帧等可选元素。

第11部分聚焦音频、画面、字幕这三项必备要素，
第12部分介绍音效、背景乐、文字层这几类可选要素，
第13部分则讲解关键帧操作。

先行创建一个空草稿。

### 10.1）创建剪映草稿

![](img/1a41ce40344b67994ecbd6a418f4425f.png)

![](img/5710168f77a93294f621d0c94ca9b687.png)

1.新增节点---2.视频合成_剪映小助手---3.create_draft

## 11）音频，图片，字幕模块

### 11.1）构造音频时间轴

![](img/debc509ebe6be84f2f4aded99bfff5d2.png)

![](img/1f5142f788b85afbdf13cb5d8d36a230.png)

1.新增节点---2.剪映小助手数据生成器---3.audio_timelines

接入参数：批处理的link_list

### 11.2）构造音频数据

![](img/7f320ca261d9c4fc2234a7d75e26cdd0.png)

![](img/e26ac206da309b6dd53d012ae2ba7719.png)

1.新增节点---2.剪映小助手数据生成器---3.audio_infos

### 11.3）添加音频

![](img/9c902779826299f1e98fb7ff0e8c8ddb.png)

![](img/43c95767775bc5dccc4bf5ce825addad.png)

1.新增节点---2.视频合成-剪映小助手---3.add_audios

### 11.4）构造图片数据

![](img/cd176a1a9c739ec461d4165c10ae1f9c.png)

![](img/6988ec89e5abb8dbfcfc1f3f1ea47c48.png)

1.新增节点---2.剪映小助手数据生成器---3.imgs_infos

### 11.5）添加图片

![](img/d4e48f3a4aa84805c598161f084b56c7.png)

![](img/fa94b8a4845cd78ba02dc761dab46b27.png)

1.新增节点---2.视频合成_剪映小助手---3.add_images

### 11.6）代码_调整字幕

![](img/d7b80fc47622048f3b2749ed6cc0210f.png)

![](img/5addca7a3cd86ea2969ee45c2b117fd7.png)

1.新增节点---2.代码 然后再IDE编辑器中粘贴下面代码

涉及代码块的节点请把语言切换为python，不要保留默认的JavaScript

![](img/dd3ca646d870f0deeb7608d128448216.png)

粘贴下面内容

```
import re
from typing import List, Dict, Tuple, Any

# --- 辅助函数部分保持不变 ---
SUB_CONFIG = {
    "MAX_LINE_LENGTH": 25,
    "SPLIT_PRIORITY": ['。', '！', '？', '，', ',', '：', ':', '、', '；', ';', ' ']
}

CHINESE_CHAR_REGEX = re.compile(r'[\u4e00-\u9fa5]')
CLEAN_REGEX = re.compile(r'[\u3000\u3002-\u303f\uff00-\uffef\u2000-\u206f!"#$%&\'()*+\-./<=>?@\\^_`{|}~]')

def split_long_phrase(text: str, max_len: int) -> List[str]:
    if len(text) <= max_len:
        return [text]
    for delimiter in SUB_CONFIG["SPLIT_PRIORITY"]:
        pos = text.rfind(delimiter, 0, max_len)
        if pos > 0:
            split_pos = pos + 1
            return [text[:split_pos].strip()] + split_long_phrase(text[split_pos:].strip(), max_len)
    start_pos = min(max_len, len(text)) - 1
    for i in range(start_pos, 0, -1):
        if CHINESE_CHAR_REGEX.search(text[i]):
            split_pos = i + 1
            return [text[:split_pos].strip()] + split_long_phrase(text[split_pos:].strip(), max_len)
    split_pos = min(max_len, len(text))
    return [text[:split_pos].strip()] + split_long_phrase(text[split_pos:].strip(), max_len)

def process_subtitles(
    captions: List[str],
    subtitle_durations: List[int],
    start_time: int = 0
) -> Tuple[List[Dict[str, int]], List[str]]:
    processed_subtitles = []
    processed_subtitle_durations = []
    for text, total_duration in zip(captions, subtitle_durations):
        phrases = split_long_phrase(text, SUB_CONFIG["MAX_LINE_LENGTH"])
        phrases = [re.sub(CLEAN_REGEX, '', p).strip() for p in phrases]
        phrases = [p for p in phrases if p]
        if not phrases:
            processed_subtitles.append('[无内容]')
            processed_subtitle_durations.append(total_duration)
            continue
        total_chars = sum(len(p) for p in phrases)
        if total_chars == 0:
            continue
        accumulated_duration = 0
        for i, phrase in enumerate(phrases):
            ratio = len(phrase) / total_chars
            duration = (total_duration - accumulated_duration) if i == len(phrases) - 1 else round(total_duration * ratio)
            processed_subtitles.append(phrase)
            processed_subtitle_durations.append(duration)
            accumulated_duration += duration
    text_timelines = []
    current_time = start_time
    for duration in processed_subtitle_durations:
        end_time = current_time + duration
        text_timelines.append({"start": current_time, "end": end_time})
        current_time = end_time
    return text_timelines, processed_subtitles

# --- Coze 节点主函数，严格适配示例风格 ---
async def main(args: Args) -> Output:
    # 按示例，从 params 取 input 和 duration_list 
    params = args.params
    input_scenes = params.get('input', [])  # 对应示例里的 input 参数
    duration_list = params.get('duration_list', [])  # 对应示例里的 duration_list 参数

    # 提取字幕文本
    captions = [scene.get('cap', '') for scene in input_scenes]  

    # 处理字幕生成时间轴和结果
    text_timelines, text_captions = process_subtitles(
        captions=captions,
        subtitle_durations=duration_list,
        start_time=0
    )

    # 构造输出，和示例一样的结构风格
    ret: Output = {
        "text_captions": text_captions,
        "text_timelines": text_timelines
    }
    return ret
```

### 11.7）构造字幕数据

![](img/99cfb289050366f675961af90ba70121.png)

![](img/c0471a3f11bf4974be0302d76c361872.png)

1.新增节点---2.剪映小助手数据生成器---3.caption_infos

### 11.8）添加字幕

![](img/6aa7f64d2861b51c287cf2111fa91e0f.png)

![](img/0254c220faa414a75e518686671376e9.png)

1.新增节点---2.视频合成_剪映小助手---3.add_captions

## 12）首图，开头音效，背景音乐模块

### 12.1）代码_构造首图_开头音效_背景音乐数据

![](img/ce590f25a9b17ffb45755eb0d00728f6.png)

![](img/77e908b014f5d53c3c932f9d04ea9928.png)

max_duration 取 all_timelines 的结束节点

此次输出额外包含 kc_audio_info、bg_audio_info 两个字段，片头音效与背景乐均已上传至云端，脚本中直接引用云端链接

```
# 在这里，您可以通过 'args'  获取节点中的输入变量，并通过 'ret' 输出结果
# 'args' 已经被正确地注入到环境中
# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为'input'的值：
# params = args.params; 
# input = params['input'];
# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：
# ret: Output =  { "name": '小明', "hobbies": ["看书", "旅游"] };

async def main(args: Args) -> Output:
    params = args.params
    # 获取输入的image_url和duration_list
    image_url = params['image_url']
    duration_list = params['duration_list']
    kc_audio = "https://p9-bot-workflow-sign.byteimg.com/tos-cn-i-mdko3gqilj/c04e7b48586a48f1863e421be4b10cf1.MP3~tplv-mdko3gqilj-image.image?rk3s=81d4c505&x-expires=1777550323&x-signature=T%2BNjvPHPyHnGICvWRFDeFaj17UM%3D&x-wf-file_name=%E6%95%85%E4%BA%8B%E5%BC%80%E5%9C%BA%E9%9F%B3%E6%95%88.MP3"
    bg_audio = "https://p3-bot-workflow-sign.byteimg.com/tos-cn-i-mdko3gqilj/5603dc783a6c4b75a4bf4e1b44086ad5.MP3~tplv-mdko3gqilj-image.image?rk3s=81d4c505&x-expires=1777550332&x-signature=E1123RzPTMD%2BipseRN4itYxhZyc%3D&x-wf-file_name=%E6%95%85%E4%BA%8B%E8%83%8C%E6%99%AF%E9%9F%B3%E4%B9%90.MP3"
    max_duration=params['max_duration']   
    # 构建输出对象，只使用duration_list的第一个时间作为end值
    ret: Output = {
        "image_info": [
            {
                "image_url": image_url,
                "width": 1024,
                "height": 1024,
                "start": 0,
                "end": duration_list[0]  # 取第一个时间作为结束时间
            }
        ],
        # 新增开场音频信息部分
        "kc_audio_info": [
            {
                "audio_url": kc_audio,
                "duration": 4884897,
                "start": 0,
                "end": 4884897
            }
        ],
        # 新增背景音频信息部分
        "bg_audio_info": [
            {
                "audio_url": bg_audio,
                "duration": max_duration,
                "start": 0,
                "end": max_duration
            }
        ]

    }
    return ret
```

### 12.2）add_images_首图

![](img/3b0f2fba14099b8b02b7d7174c765ac8.png)

![](img/a61b50047ebb70a97fdbfdf295e1f791.png)

先新建一个节点，选用 视频合成_剪映小助手 里的 add_images 功能

### 12.3）add_audios_开头音效

![](img/4827b5a981e7934f6a6bc42a1dd4adb0.png)

![](img/57bc55966d144eca725271e4960a7098.png)

再新增一个节点，调用 视频合成_剪映小助手 的 add_audios 接口

### 12.4）add_audios_背景音乐

![](img/352ae2551851e21238770a8bb4ce989b.png)

![](img/6ce6cb27f770d3a3b1122b91c748cf27.png)

继续添加节点，接入 视频合成_剪映小助手 的 add_audios

### 12.5）代码_构造主题时间轴

![](img/0c183c365f182ffa1ceeae39b1c7de74.png)

![](img/809b3f6acf9e7db8c47b50191788d50d.png)

放置一个 代码 节点，随后在内置的 IDE 编辑区把下方代码复制进去

```
from typing import List, Dict, Any

async def main(args: Args) -> Output:
    params = args.params
    # 获取相关输入数据，假设 title 在 params 中，duration_list 也在 params 中
    title = params.get('title', '')
    duration_list = params.get('duration_list', [])
    # 取 duration_list 第一个时间点，若为空则设为 0（可根据实际情况调整默认值）
    first_duration = duration_list[0] if duration_list else 0  

    # 构造 title_list，这里简单处理为列表包含 title，可根据实际需求扩展
    title_list = [title]
    # 构造 title_timelines，假设起始时间为 0，结束时间为 first_duration
    title_timelines = [{"start": 0, "end": first_duration}]  

    # 构建输出对象
    ret: Output = {
        "title_list": title_list,
        "title_timelines": title_timelines
    }
    return ret
```

### 12.6）构造主题数据

![](img/c6fcc4556e7467412785259d9e9412d1.png)

![](img/421dc1f0e93b16a9140e3c0eaa4bb753.png)

新增节点，选择 剪映小助手数据生成器 的 caption_infos 输出

### 12.7）add_captions_主题

![](img/88d665406bb05e423cab56943338f8b9.png)

![](img/ec1dfbe5900e6d2705794548aea8ddf4.png)

添加节点，连接 视频合成_剪映小助手 中的 add_captions

## 13）添加关键帧模块

### 13.1）代码_图片关键帧

![](img/310ce21e70618b42fd33b374b5100f00.png)

![](img/3805897948d60c3d6b1edee75348862f.png)

插入 代码 节点，并在 IDE 里填入下面的脚本内容

```
# 在这里，您可以通过 'args'  获取节点中的输入变量，并通过 'ret' 输出结果
# 'args' 已经被正确地注入到环境中
# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为'input'的值：
# params = args.params; 
# input = params['input'];
# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：
# ret: Output =  { "name": '小明', "hobbies": ["看书", "旅游"] };

import json
from typing import Any

async def main(args: Args) -> Output:
    params = args.params
    segment_ids = params['segment_ids']  # 所有图片的ID列表
    times = params['duration_list']      # 对应每张图片的时长列表

    # 验证参数长度（确保一一对应）
    if len(segment_ids) != len(times):
        raise ValueError("segment_ids与times数组长度必须一致")

    keyframes = []  # 存储当前脚本生成的关键帧

    # 循环处理第2张及以后的图片（跳过索引0）
    for idx, seg_id in enumerate(segment_ids):
        if idx == 0:
            continue  # 跳过第一张，留给另一个脚本处理

        # 获取当前图片的音频时长（转换为整数微秒）
        audio_duration = int(float(times[idx]))

        # 根据索引奇偶性决定缩放方向（排除第一张后的循环索引）
        cycle_idx = idx - 1  # 从0开始重新计数（第2张对应cycle_idx=0）
        if cycle_idx % 2 == 0:
            start_scale = 1.0
            end_scale = 1.5
        else:
            start_scale = 1.5
            end_scale = 1.0

        # 添加起始关键帧（动画开始时的缩放值）
        keyframes.append({
            "offset": 0,
            "property": "UNIFORM_SCALE",
            "segment_id": seg_id,
            "value": start_scale,
            "easing": "linear"
        })

        # 添加结束关键帧（动画结束时的缩放值，与音频时长同步）
        keyframes.append({
            "offset": audio_duration,
            "property": "UNIFORM_SCALE",
            "segment_id": seg_id,
            "value": end_scale,
            "easing": "linear"
        })

    # 输出关键帧（序列化为JSON字符串）
    return {
        "keyFrames": json.dumps(keyframes)
    }
```

### 13.2）代码_首图关键帧

![](img/2f1bf58bb68ef4ada4e2d8d15b3aaa60.png)

![](img/d0816a1da881c0012d23de6b56356729.png)

再加一个 代码 节点，在编辑器中粘贴所给代码

```
# 在这里，您可以通过 'args'  获取节点中的输入变量，并通过 'ret' 输出结果
# 'args' 已经被正确地注入到环境中
# 下面是一个示例，首先获取节点的全部输入参数params，其次获取其中参数名为'input'的值：
# params = args.params; 
# input = params['input'];
# 下面是一个示例，输出一个包含多种数据类型的 'ret' 对象：
# ret: Output =  { "name": '小明', "hobbies": ["看书", "旅游"] };

import json
from typing import Any

async def main(args: Args) -> Output:
    params = args.params
    seg = params['segment_infos']  # 包含第一张图片信息的列表

    # 验证是否存在第一张图片信息
    if not seg or len(seg) < 1:
        raise ValueError("segment_infos中未找到第一张图片信息")

    first_seg_id = seg[0]['id']  # 第一张图片的ID
    # 计算第一张图片的总时长（结束时间 - 开始时间）
    first_duration = seg[0]['end'] - seg[0]['start']

    keyframes = []  # 存储当前脚本生成的关键帧

    # 第一张图片的起始关键帧（0秒时缩放值为2）
    keyframes.append({
        "offset": 0,
        "property": "UNIFORM_SCALE",
        "segment_id": first_seg_id,
        "value": 2,
        "easing": "linear"
    })

    # 第一张图片的中间关键帧（0.533秒时缩放值为1.2）
    keyframes.append({
        "offset": 533333,  # 固定时间点（单位：微秒）
        "property": "UNIFORM_SCALE",
        "segment_id": first_seg_id,
        "value": 1.2,
        "easing": "linear"
    })

    # 第一张图片的结束关键帧（总时长结束时缩放值为1.0）
    keyframes.append({
        "offset": first_duration,
        "property": "UNIFORM_SCALE",
        "segment_id": first_seg_id,
        "value": 1.0,
        "easing": "linear"
    })

    # 输出关键帧（序列化为JSON字符串）
    return {
        "keyFrames": json.dumps(keyframes)
    }
```

### 13.3）add_keyframes_图片

![](img/238d2b0e16ce888a93a897cb4aa522c7.png)

![](img/a55d3cb444945f97d6f9a07afcf0b781.png)

新增节点，指向 视频合成_剪映小助手 的 add_keyframes

### 13.4）add_keyframes_首图

![](img/5df21781ddc00e7479f42757051d944f.png)

![](img/4d7fc61d562238d9b1f2cd141a4584e8.png)

新增节点，指向 视频合成_剪映小助手 的 add_audios

## 14）保存剪映草稿

![](img/557b792806bb8b01b3d5ee863dd3c4f1.png)

![](img/8eda53361ad9f40bbe43e6b8e3618cfc.png)

创建节点，调用 视频合成_剪映小助手 中的 save_draft

## 15）输出

![](img/f9607725e7cb26d461aeb95f4caaca7d.png)

## 16）下载文件

把以上所有步骤跑完，工作流会返回一个形如 https://ts.fyshark.com/#/cozeToJianyin?drafId=https://video-snot-12220.oss-cn-shanghai.aliyuncs.com/draft/dede1dcf-87c4-4f46-aee0-db96518eff00.json 的地址

剪映小助手下载入口

https://www.51aigc.cc/#/cozeToJianyin

将返回的地址粘贴到剪映小助手内即可拉取草稿

首次启动剪映小助手时会提示配置草稿目录，可进入剪映设置查看当前草稿保存路径，把该路径告知给小助手，这样导出的文件会落到与剪映一致的目录下，便于剪映识别

![](img/838763a657b67607006cba1efa170a67.png)

![](img/3aa7c315587b7729696573e5caf0af55.png)

![](img/aebebf1eb4b286b5b157c7ecb1784108.png)

![](img/71af65895390a43b06b4cea02dfc26c4.png)

# 案例举一反三

你有没有发现，所有图文类的创作流程，底层逻辑其实都是相通的？只要把文案大模型的提示词、生图大模型的提示词换一换，就能立刻切到另一个赛道——心理学科普、英语陪练、哄睡故事、励志鸡汤、书单推荐、带货种草，统统不在话下。

视频的画风也能随时切换：把关键帧、特效、音效、背景音乐换一套，整个片子就像重新做的一样，观众根本看不腻。再动一动节点，声音克隆、图片转视频、数字人直播也能直接接进来。如果前面挂一个专门抓取对标文案的插件，二次创作直接起飞。

# 延伸玩法

## 1. 智能体

每次都要打开工作流去调用，确实有点烦。那就干脆搭一个智能体，直接用对话的方式触发工作流。

### 1）新建智能体

![](img/6e1dca51aecb27e6151caa1e1e1b4b01.png)

### 2）智能体搭建页面

![](img/757209c990de4fcdd1a0a59d467b108b.png)

发布之后记得把链接复制保存好，分享给别人就能用。别人调用你的智能体，扣的是他自己的资源点，你不用担心成本。

### 3）智能体对话页面

我的智能体链接在这，可以看看效果：https://www.coze.cn/store/agent/7535489804445188136?bot_id=true

![](img/d261d1c1e6c16a24540e71690607c6e8.png)

收到回复后，把那个以json结尾的链接直接丢进剪映小工具，就能使用了。

![](img/71821d7ffe18fda462e25c3d94b273b4.png)

## 2. 包装成API

![](img/2f8d06081ef1fe88429ada645f1111c9.png)

### 1）点击授权

![](img/437097ebe44c5f83750133de22274e25.png)

![](img/9a8f7b5735bb1d5c712e5df4792f4995.png)

左边是没授权的样子，右边是授权完成后的状态。

![](img/364b0e2dbe64c35a11a3cfa242420fbb.png)

### 2）找到workflow_id和输入参数

在工作流页面的网址里，就能找到workflow_id。

![](img/c8ce4d252d4e8e8fa25886b14cd63aae.png)

![](img/80cbc46a1c05b8f8e561251995359d8f.png)

![](img/c4c9d0d05bcdebf9428b21fe4b9dcecb.png)

把workflow_id填到图里标1的位置。标2的位置填输入参数parameters。如果你的开始节点像左上图那样，就输入：

```
{"input":"古代粮食为何紧缺"}
```

如果开始节点像右上图那样有3个参数，就照葫芦画瓢写3个。

```
{
    "bg_audio": "https://p3-bot-workflow-sign.byteimg.com/tos-cn-i-mdko3gqilj/5603dc783a6c4b75a4bf4e1b44086ad5.MP3~tplv-mdko3gqilj-image.image?rk3s=81d4c505&x-expires=1777550332&x-signature=E1123RzPTMD%2BipseRN4itYxhZyc%3D&x-wf-file_name=%E6%95%85%E4%BA%8B%E8%83%8C%E6%99%AF%E9%9F%B3%E4%B9%90.MP3",
    "kc_audio": "https://p9-bot-workflow-sign.byteimg.com/tos-cn-i-mdko3gqilj/c04e7b48586a48f1863e421be4b10cf1.MP3~tplv-mdko3gqilj-image.image?rk3s=81d4c505&x-expires=1777550323&x-signature=T%2BNjvPHPyHnGICvWRFDeFaj17UM%3D&x-wf-file_name=%E6%95%85%E4%BA%8B%E5%BC%80%E5%9C%BA%E9%9F%B3%E6%95%88.MP3",
    "zhuti": "苏东坡"
}
```

### 3）测试API

接着点图里标3的按钮。

![](img/d8badf99edceabcc5fb23d6c2582add8.png)

测试通过后，把标3位置的代码块复制给AI，让它帮你把这个API接入到其他产品里，或者直接当网站后端服务来用，都没问题。

![](img/797b28feb2a9f39260ee7bc00d085875.png)

要是测试没过，就按返回结果调整。上图那种提示，说明是缺了参数，也就是输入写得不完整。

# 补充知识

## 1）什么是JSON格式

JSON是一种特别通用的数据格式，专门用来存数据、传数据。

- 最基础的结构是“对象”：用 `{}` 包起来，里面放多个键值对，键和值之间用 `:` 连接，每一对之间用 `,` 隔开。比如描述一个人：

```
{
  "name": "张三",    // 键是"name"，值是"张三"（字符串，用双引号）
  "age": 20,         // 键是"age"，值是20（数字，不用引号）
  "isStudent": true  // 键是"isStudent"，值是true（布尔值：true/false，不用引号）
}
```

- 如果要描述“一群人”，就用 `[]` 把多个对象包起来，这叫数组。比如描述两个人：

```
[
  {
    "name": "张三",
    "age": 20
  },
  {
    "name": "李四",
    "age": 22
  }
]
```

- 还可以嵌套：某个键的值再放一个对象或数组，形成复杂结构。比如描述一个人和他的宠物：

```
{
  "name": "张三",
  "pets": [  // 键"pets"的值是一个数组
    {
      "type": "猫",
      "name": "花花"
    },
    {
      "type": "狗",
      "name": "旺财"
    }
  ]
}
```

推荐一个JSON格式化网站：https://jsonhero.io/j/tGDhvzLOQem7 再乱的JSON丢进去，也会变得清清楚楚。左边是原始数据，右边是整理后的样子。

![](img/ccad4fb406ad58f24045611bf1f231c7.png)

![](img/c79ceb277ac58f867906f4f1765efdcb.png)

## 2）如何查看日志

日志在调试工作流时非常有用。你可以翻出以前运行过的数据，把它们复制下来，单独去测某个节点，不用把整个流程跑一遍。

![](img/11098ccbdf7eb3407906f4183c361076.png)

![](img/a823bb0d30de19c7b744fa0bdafafc2c.png)

左图是调出日志的方法。右图点1的位置，能看到历史日志记录；选中某一条，再点3的位置，就会跳转到当时运行现场。

![](img/bd299002af6217512c78605ffba09424.png)

这样一来，就能看到当时工作流的输入和输出，也不用每次都从头跑完整条流程，白白浪费资源点。

## 3）剪映草稿文件时间线生成方法

## 4）剪映草稿文件可用的字体列表

## 5）批处理的并行数量是有限制的

如果你的批处理节点里包含“图片生成”这种任务，最大并发数量只能设成4。

## 6）云端存储音频、图片、视频相关数据，方便调用

地址：https://console.volcengine.com/tos

![](img/53dbfd795db8a2c5224ff6779d900970.png)

点一下“桶名称”，就能进入存储空间。

![](img/76eb6a3d323d6343ccd0ec93d4511c61.png)

在这里能看到文件详情。

![](img/2bf2cb5808a4c93c9e2f5020846a572b.png)

点击“详情”再点“复制”，得到的链接就是全网都能访问的地址了。

# 最后

工作流再强大，也只是给效率加倍的放大器。真正值钱的，是业务本身。如果你还没跑通从0到1的那一步，建议先踏踏实实把业务打磨好。

觉得这次分享有收获的话，记得点赞投锚告诉我，我才知道下次该往哪个方向分享。如果你有工作流相关的需求，也欢迎找鱼丸咨询。感谢大家耐心看完。