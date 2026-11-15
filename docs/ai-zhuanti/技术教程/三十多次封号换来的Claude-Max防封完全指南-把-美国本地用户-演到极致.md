# 三十多次封号换来的Claude Max防封完全指南：把“美国本地用户”演到极致
文 / 懒人搜索精选
Opus 5.5发布之后，Claude在AI圈几乎是碾压级的存在。但再好的模型，号一封也白搭。从年初到现在，我前前后后因各种原因没了三十多个Claude账号（有些是帮同事开的）。苹果内购、Google Play、海外卡我全试过，市面上能踩的坑基本都踩了一遍。如今我手上有4个号在正常服役：3个Max 20x，1个Pro，其中有2个连七八月那两轮大封杀都扛过来了。
这篇文章把整套稳定不封号的细节全盘托出：从IP、注册、电脑和网络环境，到付款、Claude Code、升Max 20x和续费，甚至KYC处理都包了。为了照应不同读者，关键操作都配了示意图。内容较长，建议先收藏再按图索骥。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_0_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_0_1.png>
> 编辑划重点：如果你打算把Claude Code往重度用，这篇是必读。作者用三十多次封号换来的心得，浓缩成一句话就是——平台封不封你，只看你的“环境”像不像美国本地用户。正在用随便一架🪜免费白嫖的轻度用户，看完这句就可以划走了。最值得抄的两条：一是花60元左右买个美国静态住宅IP，只用于注册那几天，日常使用反而随便；二是Pro正常用5次、隔一天再升Max。另有最坑的雷区：Apple邮件验证链接千万别在日常浏览器点开，否则环境配得再好也白搭。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_1_0.png>
## 一、封号底层逻辑：Anthropic真正在乎的是什么
网上流传的防封方法大多跑偏。其实Anthropic在用户协议里已经把红线写清楚了，就三条：你是否在不支持的地区使用；你是否使用账号做模型蒸馏、高并发或接入了不受认可的第三方工具；你是否发布违规内容。对绝大多数人来说，后两种行为只要不主动作死就不会触发。所以剩下的核心变量，其实就是你想不想一个“受支持地区的正常用户”。
从注册、订阅到使用，我们要做的只有一件事：让平台觉得你就是一个它支持区域里的普通活人。后面的每个操作，都在回答同一道题：“一个地道的美国用户，会不会这么做？”
而注册是整条链路上最脆弱的一环。新号注册后的头几天，风控系统会评估你是不是高风险用户。它主要看你注册瞬间的状态：浏览器有没有暴露真实位置和IP、注册用的IP在不在海外、这个IP有没有被滥用过。风险高，付款时弹KYC；风险更高，直接封号。我遇到过的一注册就挂的号，几乎都是因为环境出卖了你。
反过来，注册时环境干净、行为正常、邮箱正经，这个号从出生起就自带清白，后面怎么造也不容易出问题。当然IP不是唯一因素——一个美国人在咖啡馆连着公共Wi-Fi注册，或者常年挂VPN上网，难道就不是正常用户了？所以关键是整体环境，不是某一个参数。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_2_0.png>
## 二、注册权重怎么提：单独买一个美国静态住宅IP
平时用的🪜节点，大多数是多人共享的“公共汽车”，你没法确定以前有多少人用它注册过、被封过多少个号。注册又是风控最严格的环节，因此值得单独配一个干净的IP。
没必要一上来就买几百块一个月的“真家宽”。几十块的静态住宅代理，完全撑得住。选购时看三点：
- 地区必须选美国。后面浏览器的时区和语言都要跟着IP城市走。
- 选静态，不选动态。静态IP出口固定，动态IP会按时间或连接轮换，正常人不可能刷新一次网页就换一个城市。
- 商家页面一般把“动态住宅”“静态住宅”“静态机房”分开卖，认准“静态住宅代理”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_4_0.png>
付款后你会收到一份连接信息，里面有四行核心数据：IP、端口、账号、密码。这四件套后面会用两次：一次在指纹浏览器里配置，一次在手机上用小火箭登录Claude App。先存到安全的地方。
购买渠道就不点名了，免得有广告嫌疑。去YouTube搜“美国静态IP”等关键词，多看几个教程和评论，挑一家口碑可以的下手。价格在60元/月以上通常没问题；有人贪便宜买了30元的所谓“住宅IP”，结果注册秒封，基本可以断定是机房IP冒充。
这里要注意节奏：注册、手机登录、订阅Pro、升级Max，尽量在这一周内全部干掉，之后这个IP就不需要续费了。日常使用Claude和Claude Code，用自己的普通🪜就够，哪怕是机房IP也没事。因为海外本来就有大量用户把Claude Code挂在机房服务器上7x24小时跑，这不稀奇。
## 三、指纹浏览器：把“美国用户”演到细节
一个真正的美国用户，浏览器环境的画像是什么？IP在当地，时区在当地，界面语言是英文。比特浏览器这类指纹浏览器可以帮你一键配齐，并且让整个窗口的流量强制走指定代理；代理一断，窗口立刻断网，不会偷偷使用你的真实网络。
步骤很简单：打开比特浏览器，点击左上角“创建窗口”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_6_0.png>
在弹出的设置面板里，先看代理区域。“代理方式”保持默认的“自定义代理”，“代理类型”选Socks5，然后把刚才的四件套分别填进“代理主机”“代理端口”“代理账号”“代理密码”。“刷新URL”空着。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_6_1.png>
继续往下翻，红框里那几项语言选项，统一改成英语。时区必须和IP所在城市一致：IP在加州就选America/Los_Angeles，在纽约就选America/New_York。WebRTC和地理位置，全部选“禁止”。旁边的“基于IP生成”开关建议全部关闭，手动选心里更有数。
为什么要禁WebRTC？因为这项技术用于浏览器实时音视频，它有可能绕过代理把真实IP直接交出去。禁用后网站能检测到“你关闭了WebRTC”，但这不可疑——海外很多在意隐私的人早就是这么配的。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_7_0.png>
硬件和设备指纹不用一项项调，点左下角“一键随机生成指纹配置”，然后保存。配置完成后先随便开个网页，能正常加载说明代理通了；再去ipinfo.io看看出口IP是不是在美国、城市能不能和时区对上。
接下来要准备一个海外邮箱。我最推荐Proton，原因非常简单：Anthropic发的邮件里带跟踪器，而Proton会自动拦截。比如我在Proton里打开一封Anthropic邮件，顶部直接显示“已屏蔽1个跟踪器”，来源是Sendgrid，展开后链接地址开头就是mail.anthropic.com。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_8_0.png>
这类跟踪器在邮件打开时会被加载，从而拿到你当时的IP。Proton负责拦，比特浏览器负责走代理，等于双重保险。
Proton有免费版，注册时直接选最左边那个Free就行，零成本。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_9_0.png>
注册时一般会要求绑定一个恢复邮箱来验证真人，用你现有的邮箱或Gmail都可以，千万别用来路不明的野鸡邮箱，那会拉低账号权重。
不管用哪个邮箱，都要守住一条原则：只在设置好的比特浏览器窗口里登录和收信。这样即使邮件里的追踪器加载，泄露出去也只是代理IP。
有些验证链接会发到你的日常邮箱，比如Proton发到恢复邮箱的那封验证信。千万不要用手边浏览器直接点开，像下图那样，在“Verify email”上右键，选择“复制链接地址”，再粘贴到比特浏览器里打开。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_10_0.png>
邮箱准备好，终于可以注册Claude了。在比特浏览器窗口打开claude.ai，忽略Google和Apple按钮，直接用输入框填邮箱，点击“Continue with email”。随后去Proton收信，点邮件里的黑色Sign in按钮，链接10分钟内有效。点回去以后，勾选同意条款，再点“Create account”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_10_1.png>
接着Claude会问你想选什么套餐。你的终点是Max 20x，但正常人不会注册第一分钟就掏200美元，所以正确操作是选最左边的“Use Claude for free”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_11_0.png>
随后它会不断引导你下载桌面客户端，忽略底部的“Skip”；职业也跳过；称呼随便填一个英文名；角色选择继续跳过，就可以进入主页了。进来后先像普通新用户一样随便聊几句，中文英文都行，因为海外本来就有大量用简体中文的华人和留学生，不必刻意装成英语母语者。
整个流程里最危险的动作，是在日常浏览器里点开Claude的邮件链接。前面环境做得再完美，一下就把真实IP暴露了。这一步的干净程度，直接决定付款时会不会弹KYC。如果真弹了，说明注册环境仍有瑕疵，常见原因无非是：IP地址曾被滥用；指纹浏览器参数不对，比如时区没对齐、WebRTC没关；邮箱被风控；或单纯赶上Claude风控升级。我的建议是直接放弃这个号，重开一个窗口、换新邮箱，按流程再走一遍。
## 四、电脑做好了，再把系统环境“洗”一遍
号注册好了，先别急着付钱。后面订阅和接Claude Code都要在自己电脑上操作，必须先把电脑收拾干净。
第一，把系统时区设为新加坡。它和北京同属UTC+8，改过去显示器上时间完全不变，但系统时区不再是中国。Claude Code存在本地运行，会读取系统时区，所以能少暴露就少暴露。方法很简单：跟你的Agent说一声“把系统时区改成Asia/Singapore”，它会自动查询、修改并确认生效，后续清理Skill里也会带这一步。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_12_0.png>
第二，清除本机残留的Claude记录。如果这台电脑之前被封过号，不用换机器，清掉残留就能恢复干净。我两台MacBook都封过号，清理后正常用。我写了一个开源的清理Skill，地址：https://github.com/suyuan2022/suyuan-skill/blob/main/claude-cleanup/SKILL.md
这个Skill只在macOS上验证过，Windows暂未测试。它的工作机制很保守：动手之前先把~/.claude完整备份一遍，Skills、Hooks、会话记录都在里面；然后自动清缓存和日志。像换本地ID、清钥匙串、清桌面端登录状态、改系统时区这些属于较大动作，会不会执行由你勾选。所有删除的文件都进一个带时间戳的废纸篓目录，不会永久删除；最后还得你亲自输入一次CONFIRM，它才开始动手。
需要注意，应该让Codex或普通终端来执行这个Skill，绝对不要让它清理正在运行中的Claude Code自己的目录。使用体验是这样的：把链接丢给Agent，说“执行这个skill帮我清理”，它会先做只读审计，列出缓存、备份的大小以及高风险操作，完全不会乱删。你决定清理哪些项目后，自己在终端里输入CONFIRM确认，它才会真正写入磁盘。
## 五、网络分流：让真实IP永远隐在幕后
电脑收拾干净，接下来处理网络。这一章只解决两件事：一是做好分流，二是🪜一断，Claude也跟着断。
先说分流。最容易暴露你的，往往是🪜没开全局。Claude在收集数据时不一定只访问claude.ai和anthropic.com，它可能调用第三方服务。你如果只给这两个域名配代理，其他连接还是走中国IP；而全局代理又让国内网页慢得没法用。所以我选择“反着配”：从GitHub拉一份国内域名和国内IP段白名单，名单内的直连，名单外的一切流量都走海外出口。Anthropic几乎不可能把数据存在中国服务器上，它要连的一定都在海外。只要非国内流量全部走海外，它怎么检查都是海外IP。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_15_0.png>
另外，Clash默认的“系统代理”模式，终端里的命令行程序不一定走，而Claude Code正是跑在终端里。所以务必开启TUN模式，让🪜接管所有程序的流量。
光有分流还不够，还得保证🪜掉线时，Claude也跟着网线“断开”。🪜总会遇到不靠谱的时候：节点挂了、Clash崩了、电脑睡眠唤醒还没重连。一旦流量在此时自动切回直连，Claude便会拿着你的真实国内IP去建立连接，而你根本察觉不到。所以原则是：宁可断网，绝不偷偷直连。具体做法是：打开TUN模式，把分流规则的兜底指向海外节点，代理组里不放“直连”。这样节点挂了，海外流量就是连不上，而不是绕回直连。
验证方式也直白：把海外节点在Clash中停掉，此时claude.ai应该无法访问，而国内站点依然秒开，这就达标了。
这些规则不用手写，直接把下面这段话发给你的Agent即可：
“帮我改Clash分流规则：国内域名和国内IP直连，其余所有流量走我指定的海外节点；节点断了宁可断网也不要回落直连。先找到当前Clash客户端和生效配置，完整备份并告诉我位置；保留原有订阅和局域网直连规则；加入国内域名和IP段规则集（域名来源：https://github.com/pfwf/china-domain-allowlist，IP来源：https://github.com/Loyalsoldier/clash-rules 的 cncidr）；兜底指向海外节点，代理组里不要放DIRECT；检查规则顺序和DNS设置，别让国外域名被国内DNS解析后走直连；最后开启TUN模式，确认终端命令行程序也走代理。”
以上这套流程，就是我三十多个号的“学费”换来的全部经验。照做之后，我目前的四个号一直很稳。祝你的Claude也活过每一次风控。
7. 调整完毕后请帮我做一下自检：国内的网站保持直连正常访问；claude.ai 必须走海外线路；在终端里查一下公网出口 IP 确认已经落在境外；随后把海外节点关掉，核对 claude.ai 已经无法打开而国内网站依然可用。
8. 完整告诉我如何一键恢复到修改前的网络配置。缺少的信息先向我确认，不要自行假设。
## 六、付费订阅 Claude 账号
电脑与网络环境整理完，接下来就是付款环节。
付款大致有两条路线，选哪条取决于你手上有什么资源：
### 网页直订 + 境外银行卡
需要条件：一张可以在国外支付的银行卡，我实测用的是 Starryblu，不过开卡通常需要护照资料。
Max 20x：每月 200 美元。被封无退款。操作难度：低。
### App Store 内购 + 美区礼品卡
需要条件：一部 iPhone、一个美区 Apple ID、美区礼品卡余额。
Max 20x：每月 249.99 美元。被封后退款走苹果通道。操作难度：高，升级 Max 时极大概率要联系苹果客服解除风控。
先讲网页路线。
我用的 Starryblu 近期在 X 上讨论度很高，用来订阅 Claude 实测不会被拒。
开卡阶段常会被卡在排队审核，可以联系客服说明你是要付费开户，请求加急，基本很快就能通过。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_18_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_18_1.png>
卡通过后需要充值，最顺畅的是用一张香港卡入账；没有的话也可以找可靠渠道代充。
付款前有一点比卡更关键：访问 IP、账单地址、银行卡这三者要相互匹配。比如 IP 显示在加州，账单地址就必须填加州的。
如果 IP 在加州，账单地址却填别的州，卡又是新加坡发行的，风险会明显上升。
手上如果有干净的新加坡 IP，也可以把整套信息换成新加坡：浏览器时区与语言调成新加坡，账单地址填新加坡地址。随后在 Claude 网页内选择 Pro，进入结算页。
左上角有两张方案卡，点蓝色那张「Pro monthly」，即月付，每月 20 美元。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_19_0.png>
旁边我标注红叉的那张「Pro annual」是年付，网页上 Pro 年付 200 美元一年，和 Max 的 200 美元一个月名字很像，点错就等于锁定一年 Pro。
支付时若弹出 KYC，按第三章结尾的处理方式：不要硬闯，直接注销重建一个新账号。
下面讲苹果 App Store 路线。
苹果的方案每月要多掏约 50 美元的「保护费」，好处是不需要境外银行卡，且被封后仍可尝试向苹果申请退款。
苹果美区条款写明「所有交易均为最终交易」，但实际提供了退款申请入口。
打开 reportaproblem.apple.com ，选择「申请退款」，勾选对应的订阅提交即可。
是否通过由苹果判定，条款也说明若认定存在欺诈或滥用可直接拒绝。
网页申请若不成功，后续退款流程和升级 Max 时找客服的流程一致。
我的经验是首次申请基本能过，第二次难度就大很多。
退款本身也有风险，**<u>我曾经申请退款后，苹果直接把我的 Apple ID 冻结了</u>**
所以如果条件允许，最好自己注册美区 Apple ID，万一被封至少账号成本不白花。
另外安卓的 Google Play 订阅也是 250 美金左右，我不建议走这条，风控非常严。
小米手机和谷歌安卓模拟器我都试过，账号刚注册、还没怎么使用就被封了。
走苹果路线，第一步得先准备好**<u>美区 Apple ID</u>**。
可以自行注册，YouTube 上搜「美区 Apple ID 注册」教程很多；也可以购买现成账号。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_20_0.png>
购买的话建议选价格稍贵的，**<u>到手立刻把登录手机号改成你自己的，避免卖家找回</u>**
买来的 Apple ID 只用于 App Store 登录。
**<u>不要登录 iCloud</u>**，也不要在系统设置里退出自己的 Apple ID 换号，有锁机风险。
账号有了，还需要美区礼品卡，美区账号只能充值美区卡。
最省事的做法是在支付宝内购买，人民币结算免去换汇。
打开支付宝首页，点击左上角城市入口，默认显示当前城市。
城市列表在下方：切换到上方的「国际/港澳台」，左侧选择「北美洲」，热门城市里点「旧金山」，美国任意城市皆可。
切换后首页变为国际版，向下滑动到「超值抢购」，点击第一张「大牌礼卡低至9折」下方的「立即抢」。
进入后是礼卡集合页，继续往下拉到底部「更多大牌 折扣礼卡」，点击左图圈出的 Pockyshop。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_21_0.png>
会跳转到 Pockyt Shop 小程序，选择地区为「美国」，右图圈出的「App Store & iTunes USA」和「Apple Gift Card US」两种都可用，充值后都会进入美区 Apple 账户余额。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_22_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_22_1.png>
进入后选择面额，用支付宝付款，付款完成后在底部「订单」里查看卡密。
由于支付宝渠道使用者众多，偶尔会出现缺货。若缺货，可在 SEAGM 平台购买，会产生少量手续费，但比找人代充便宜。
注册登录后，首页「热门游戏点卡」第一项即为箭头所指的「iTunes 礼品卡(美国)」。
同一行右侧的「Apple 礼品卡(美国)」也可以用；中间的土耳其区选项不要点错，区不对无法充值到美区。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_23_0.png>
点击后选择金额。
左侧两列中，显示灰色并带有红色「售罄」标签的就是无货状态，我截图当天 10、20、25 美元档都缺货，建议提前备货。
选择后查看右侧「总计」，即实际支付金额，例如 15 美元的卡需付 15.28 美元，确认无误后再用支付宝支付。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_23_1.png>
订单发货后点击「获取卡」即可拿到卡密。
此时需要输入的是 SEAGM 的登录密码，不是 Google 密码。
卡密先保存，等手机端登录好 Claude 再进行兑换。
手机上的代理节点要和注册时保持一致：在小火箭中添加对应的 SOCKS5 并开全局模式，这部分也可以让 Codex 帮你生成配置文件。
国区 App Store 搜不到 Claude，需要先切到美区账号。
打开 App Store，点击右上角头像，拉到最底下退出当前账号，再登录美区 Apple ID。
随后在 App Store 下载 Claude，使用邮箱登录。
手机填写完邮箱后，回到 Bit 浏览器查收 Claude 发来的登录邮件，即左图那封，点击中间黑色的 Sign in。
随后在 Bit 浏览器中会出现右图 6 位验证码，标题下方提示将它填到「最初发起登录的地方」，也就是手机端。
填回手机即可完成登录。
验证码下方那个「Sign in here instead」不要点，点以后会切换到电脑端登录。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_24_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_24_1.png>
登录成功后，**先充值 20 美元开通 Pro**。
充值在 iPhone 的 App Store 内操作，点击右上角头像，即下方第一张图我圈出的「兑换充值卡或代码」，输入 20 美元卡的卡密，确认余额到账。
先使用一段时间 Claude，再在 App 内订阅 Pro。
第二张为订阅页，左侧为月付 20 美元，右侧我打红叉的是年付 214.99 美元，**务必选择左侧月付**，别选错。
订阅成功后进入 Settings，即第三张图，Billing 行我画红圈处显示 Pro plan 即代表开通成功。
**苹果路线最容易翻车的是新号到手当天就充值 200 多美元礼品卡并立即订阅。**
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_25_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_25_1.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_25_2.png>
苹果的风控在此事上比 Claude 还严格，**大额充值紧接着大额订阅很容易触发购买限制。**
因此先充 20 美元开 Pro，等稳定后再上 200 多美元的 Max。
## 七、接入 Claude Code
Pro 激活后即可将 Claude Code 接入。
我推荐使用命令行 CLI 版，不建议桌面客户端。
其一客户端体验不佳，其二客户端权限更高，能获取更多本地信息。
安装无需手动敲命令，直接让 Codex 执行「帮我安装 Claude Code 命令行版」，它会按官网 code.claude.com 的指引完成部署。
安装完成后在终端运行 claude，按浏览器提示登录。
登录方式选择 Claude 账号，即你的 Pro 订阅。
浏览器授权步骤与邮件链接类似：将授权链接复制到 Bit 浏览器中打开，在已登录 Claude 的窗口里点击授权即可。
接入后日常使用要注意什么？
回到第一章的三条红线，后两条需要自律：
- 不要同时开启大量会话高并发运行；
- 不要把订阅反代成 API，也不要接入各类中转站点；
- 不要讨论违规内容。
## 八、从 Pro 升级 Max
何时升级？
建议 Pro 真正使用约五次左右，间隔一天后再升 Max 20x。想想一个正常用户会怎么做？
不会刚开 Pro 就立刻换成 200 美元的 Max，而是先用一段时间，觉得额度不够才加价。
这才是正常使用新软件的逻辑。
五次和一天仅作参考，无需卡得太死。
走苹果路线时，间隔一天能避免苹果账号在短时间内连续大额充值。
网页路线最简单，直接在网页订阅设置里升级 Max 20x 即可。
苹果路线步骤更多。
走苹果时，**先兑换 250 美元的礼品卡，确保余额充足再升级**。App 内找不到升级入口时，进入「管理你的订阅」，点击「查看所有方案」，找到 **Max 20x 月付 249.99 美元**。
注意名称和金额，不要选成 Max 5x。
余额一定要准备好，因为苹果升级是即时生效：**先全额扣除 249.99 美元，Pro 未使用完的天数再按比例退回原支付方式**。
并非只补差价。
准备好后点击升级，大概率会弹出「无法完成购买」的提示，提示联系 Apple 支持。
此例我未拍摄，下图为网络示例，弹窗样式相近。
此时：
**不要反复点击购买**。点多少次都没用，等待客服处理。
不要点弹窗或 App 内的 Apple 支持。手机 iCloud 登录的是你自己的 Apple ID，显示的是你本人的账号，不是这个美区号。要在 Bit 浏览器中打开苹果在线支持：[getsupport.apple.com](https://getsupport.apple.com)。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_28_0.png>
进入后为分类页，下半部分「Apps & Services」里箭头指向的就是 App Store。
进入后询问问题类型，选择左上角第一项「Subscriptions & Purchases」。
右侧紧邻的「Gift Card & Codes」不要点错。
在话题列表中选择左侧第三项「Unable to purchase」，即「无法购买」。
全程为英文。
若看不懂，可给 Bit 浏览器装沉浸式翻译插件，或用微信截图：框住页面后点击工具栏箭头所指的「翻译」按钮，整页即可译成中文。
接着系统会推荐几个解决方案，均可忽略，直接点击左下角「Get more help」。
弹出的「Contact Options」中只有「Live Chat」一个选项，点击即可进入苹果在线客服。
客服一般会先索要 Apple 账户邮箱，再要求报一个 Support PIN。
该 PIN 在 Apple 账户网页 account.apple.com 左侧导航最下方，即箭头所指的灰色小字「Support PIN」。
点击获取 PIN 后发给客服即可。
图中右侧可见，我该账号最终升级成功的订阅为「Claude Max 20x - Monthly」，249.99 美元每月。
接下来是如何与客服沟通。
我当时给客服的意思大致是：我就是正常在 App Store 购买订阅，不明白为何被拒；我用了多年苹果，每次发布会都熬夜看，结果连订阅都买不了，真的很失望。
英文不必自己写，我把意思丢给 ChatGPT 生成。
图示中我只说了一句「跟对方动之以情」，再补充自己买了很多苹果设备、每次熬夜看发布会，它就写出两段自然的英文，直接复制发送。
你也可以把自己的情况告诉 AI 生成话术。
客服大概率会回复：已提交审核，请等 72 小时。
这时不要听完「已在审核」就结束，务必追问一句：「So I understand that after 72 hours I will definitely be able to complete this purchase, right?」
让他给出明确答复。
多磨一下成功率会更高。
随后等待。
这 72 小时内什么都不要做，不要反复尝试购买。
时间满后，再从 Claude App 内升级。
多数情况下等待结束后即可购买。
但不要把 72 小时当成铁律，我曾连续等了四次仍无法购买。
下图是我当时把客服聊天记录丢给 ChatGPT 的截图。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_30_0.png>
客服的说法是：
> “我完全理解你的担忧，也非常感谢你的配合。相信我，这一次会成功的。”
意思是仍让你再等一次 72 小时，且他说 “Trust me this time it will work.”，相当于向你作出比较明确的保证。
我建议立刻把保证坐实，发一句：
> Okay, thank you. Just to confirm, after waiting another full 72 hours, I should be able to purchase the $250 plan successfully this time, correct?
让他明确回答 Yes。若 72 小时后仍失败，下次找客服可直接说明：上一位客服明确告知等待 72 小时后一定能购买，但仍失败。
没有进展就继续找客服，不要在 App 里一遍遍点击购买。
升级成功后，还需注意续费不断。
苹果订阅为自动续费。
每次扣费前 5 到 10 天，检查余额，提前购买并兑换礼品卡。
礼品卡偶尔缺货，不要等到扣款当天才处理。
网页路线同理，扣费前确保 Starryblu 余额充足，否则扣款失败订阅会中断。
## 最后
整套流程走下来大约一周，最耗时的就是等待苹果客服，其余步骤按图操作即可。
完成后你就能像我一样使用 Max 20x，Opus 5.5 随意调用。
回头看，这篇文章的每一步其实都在回答一个问题：
一个正常的美国用户会这样操作吗？以后遇到文中未提及的情况，也用这句话自问，基本就能判断怎么做。
> 分割线
看完这份 SOP，你可能觉得明白了。但 90% 的人在实操第一步就会卡住。
工具和教程只是初级壁垒，真正的壁垒是「立刻执行」和「圈层信息差」。
如果你想看到全网最新的变现玩法，并和一群执行力极强的极客一起落地拿结果，
我们不谈虚的，只做商业闭环拆解与 AI 效率压榨。体系内已沉淀 1000+ 跑通的套利实战案例。
- 查看圈子完整数字资产与入场门槛：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_32_0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bcfece54a310330e5a8cfb5ef0657559_32_1.png>