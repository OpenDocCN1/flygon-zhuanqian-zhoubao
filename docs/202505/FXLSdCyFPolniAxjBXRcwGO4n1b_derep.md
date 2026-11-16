# 注册美国公司、开通Mercury并申请Stripe：从零到首笔收款的完整经验分享

大家好，我是龙哥。

如果你正在做海外产品，支付系统几乎是绕不开的一环。常见的选择包括：

- Stripe：https://stripe.com/
- Paddle：https://www.paddle.com/
- PayPal：https://www.paypal.com/
- Creem：https://www.creem.io/

其中，Stripe在独立站、SaaS和各类出海产品中使用非常广泛。本文分享一条我实际跑通的路径：

1. 通过Stripe Atlas注册美国公司；
2. 使用公司资料申请Mercury商业银行账户；
3. 将美国公司和Mercury账户绑定到Stripe；
4. 完成收款配置，并成功获得第一笔Stripe收入。

全文主要介绍申请流程，后半部分再分享实际使用中的一些经验。

# 一、通过Stripe Atlas注册美国公司

注册美国公司有不少渠道，例如：

- 通过第三方服务平台办理；
- 使用Firstbase：https://www.firstbase.io/
- 使用Stripe Atlas：https://stripe.com/zh-us/atlas

我当时选择的是Stripe Atlas。下面按照实际操作顺序说明。

## 1. 注册费用

在Atlas官网直接申请，费用通常是500美元：

https://stripe.com/zh-us/atlas

![](img/6bcdefb21b562bf0c3c9f39058c05d2b.png)

如果通过Stable合作页面进入，价格是300美元：

https://stripe.com/zh-sg/atlas/stable

也就是说，可以直接节省200美元。Stable与Atlas存在合作关系，这个页面属于Stable的专属入口，购买Atlas注册公司服务时会有优惠。

Stable主要提供美国商业地址和邮件处理服务。注册美国公司时需要填写公司地址，Atlas页面也会推荐Stable，不过这项服务并非绝对强制。

![](img/93de95f0546f3cdc1887a7a264ef65ef.png)

此外，公司成立后的第二年开始，还会产生每年100美元的管理费用，具体说明可以查看：

https://support.stripe.com/questions/managing-your-registered-agent-subscription

## 2. 提交注册申请

打开以下网址：

https://stripe.com/zh-sg/atlas/stable

点击“立即注册公司”，然后按照页面提示填写资料。

![](img/0b9b2673ffe94ef7524bb26b6bc7fbe0.png)

先录入个人基本信息。

![](img/80dccacd5c31823710de1056228b3c04.png)

提交后，前往邮箱完成验证。

![](img/c5ca46200f60c3e3a31cd6bfc6ee87bf.png)

## 3. 填写公司资料

验证邮箱后，进入公司申请页面，点击“Let's go”继续。

![](img/b3e9f828da72cc0d314bfea084af60c7.png)

### 公司组织形式

选择LLC，也就是有限责任公司。

![](img/62398c875f2a3c621329fd814b375637.png)

### 公司名称

准备一个英文公司名称，并确认名称符合注册要求。

![](img/23936e9abce835178a936b3664e8c39c.png)

### 公司业务信息

填写公司简介以及网站地址。我当时填写的是一个已经上线的AI图片网站。

![](img/05d25572fbea87c9c77da03eddd6e6f4.png)

### 个人身份信息

个人资料必须按照真实情况填写，尤其注意姓名顺序：

- First name代表名；
- Last name代表姓；
- Your home address填写目前实际居住的国内地址。

![](img/cda566b7673e046e765ee59e398fc8af.png)

确认股权信息后，点击Next。

![](img/3fc1173063e98df41a3a13dc83dbea6e.png)

公司管理人选择自己。

![](img/cee27a4de0ac4f182c4869fc856ce41a.png)

之后进入公司税号，也就是Company Tax相关页面。

![](img/64956a5e33f3eaee107b6a4690d8eb51.png)

页面大意是：Atlas会向美国国税局IRS申请EIN。这个税号今后用于企业报税、雇佣员工以及相关身份识别。为了帮助更快获得EIN，系统会要求提供美国公司地址、美国电话号码和美国社会安全号码等资料。

实际填写时：

- 公司地址：可以使用Stable提供的美国商业地址；
- 美国电话号码：填写自己准备好的美国号码；
- SSN：如果没有美国社会安全号码，可以留空。

Stable与Atlas有合作，通过对应入口购买地址服务时，通常可以享受前三个月免费，之后一年按五折计算。原价每月49美元，优惠后约为每月24.5美元，一年后恢复原价。我当时使用的就是Stable提供的地址。

![](img/835b1b2d9eb132072613c3f0088b0fc3.png)

另一种选择是尝试填写自己的国内住址。页面中有“Use my home address”选项，据了解，也有人使用国内地址完成了注册。

完成后，检查公司资料是否准确。发现错误要及时返回修改。

![](img/28ee020e460c8e9c378dd8c6db796482.png)

确认无误后，进入付款环节。

![](img/8536487b9eaf61bec720f3f42cc40107.png)

## 4. 激活Stripe收款功能

Atlas的办理速度相对较快，通常一到两个工作日就能完成公司注册。注册成功后，邮箱会收到通知，点击邮件中的“Accept US card payments”即可开始激活Stripe。

也可以登录Atlas后台操作，系统会自动带入之前填写过的资料。

![](img/b6a090128738e4501311892bc32339dc.png)

如果公司注册完成后迟迟没有激活，Stripe可能会继续发邮件提醒。这个步骤最好及时完成，否则后续登录Stripe网页端时可能遇到问题。

我当时就曾经无法正常登录网页版，联系支持团队也没有立即解决。后来尝试使用Stripe手机App，反而成功登录，并顺利完成激活。

![](img/4dc17f1f1489f0b6d52a5e153ae910c7.png)

![](img/40ca745e09be4715ca4bb8cdf52ac092.png)

完成这一步后，实际上已经可以在网站中接入Stripe并开始收款。

Atlas是Stripe官方提供的美国公司注册服务。通过Atlas注册公司后，即使暂时还没有获得EIN，也没有海外银行账户，Stripe通常也允许先接受付款。不过，在EIN和银行账户准备好之前，账户余额无法正常提现。

相关说明可以搜索Stripe官方文档：Accepting payments before receiving your EIN。

## 5. 等待EIN税号

接下来就是等待美国国税局下发EIN。这个过程通常需要几周时间。

EIN全称是Employer Identification Number，即雇主识别号。它由美国国税局IRS发放，是企业用于报税、身份确认和银行业务的重要税务编号，一般由9位数字组成，例如：12-3456789。

在Atlas后台，可以查看公司申请进度。通常到了这一步，剩余事项主要就是等待EIN。

![](img/7935d0d3fa310976e2985b8f8dee285f.png)

## 6. 申请过程遇到问题怎么办

### 英文阅读有困难

可以在浏览器中安装“沉浸式翻译”等翻译插件，将页面内容转换为中文。

### 不确定如何填写

建议每完成一步就截图询问AI，尤其是公司结构、地址、税务和身份信息等部分。填写前确认清楚，可以减少因为理解偏差造成的错误。

### 查看官方帮助文档

Atlas相关帮助页面：

https://support.stripe.com/topics/atlas

### 联系客服

如果遇到无法自行处理的问题，可以发送邮件至：

support@stripe.com

尽量把问题描述清楚，并附上必要截图。根据我的体验，客服回复速度不错，态度也比较友好。

我在最后付款时曾遇到信用卡被拒的问题，连续尝试几次都没有成功。后来直接邮件联系Stripe客服，经过几轮沟通后，他们帮助我开放了支付权限，最终顺利完成付款。

![](img/d314e263d04e5a52b53fea477238f346.png)

![](img/f0a48fb26b411b3e13ae8fb6add802d5.png)

另外，申请期间Atlas会发送不少邮件，一定要经常查看邮箱，避免错过验证、补充材料或激活提醒。

## 7. 别忘了使用合作优惠

Atlas后台有一个专属优惠页面：

https://dashboard.stripe.com/atlas/perks

里面汇集了不少海外产品和服务的折扣，种类很多。对于正在做出海项目的人来说，购买服务器、工具或其他服务时，可以先看看是否有可用优惠。

![](img/bf978735237e2ffdf232f322428fd1a9.png)

Stable也有合作伙伴优惠页面：

https://usestableaddresses.notion.site/572353dfaad54a758bb780a428e8544b?v=74e63ef1e844495b9d2e49c7fd350651

其中就包括通过Stable购买Atlas服务可节省200美元的优惠。

![](img/ecd0031a368f062d83cbfb69638ae017.png)

此外，ElevenLabs近期也推出了合作伙伴优惠：

https://www.aiengineerpack.com/

如果你的项目会用到相关工具，可以比较一下优惠价格。

![](img/834be11be0e8fa94c274f06061a7ed76.png)

平时在购买海外服务时，只要页面提供优惠码输入框，就可以先让AI使用DeepSearch寻找折扣码。比如我之前购买Hostinger的VPS，就让Grok帮忙搜索可用优惠码，最后确实找到了能用的折扣。

![](img/23eef938d0c9a6f2d4a10fde8f146fd4.png)

![](img/9097a2f38141bef96b1b56e0dd5fe358.png)

# 二、Stripe账号的使用方式

通过Atlas完成美国公司注册后，Stripe账户基本已经具备使用条件。Atlas会为公司创建一个默认商户，之后可以在代码中接入Stripe支付。

如果后台提示需要补充资料，直接按照实际情况完成即可。Stripe可能会同时在网页端和手机App中提醒。例如，Mercury银行账户申请成功后，就需要回到Stripe后台补充银行卡信息。

![](img/dbf54abcf2cf5a053eabd357660343ea.png)

## 风险控制：建议一个网站对应一个商户

实际使用Stripe时，最好不要让多个业务网站共用同一个商户，建议采用“一站点一商户”的方式进行风险隔离。

Atlas默认生成的商户名称通常是公司名称，也可以自行修改。如果之后有新的独立网站需要接入支付，可以在Stripe后台左上角点击当前商户名称，在下拉菜单中选择创建账户。

![](img/32ce70b42495a59b0ba4b37108ca3a83.png)

![](img/ec643c4111783570bac91f31a3fec8c7.png)

![](img/57f8fe71379899ed6731842521c0a002.png)

新商户创建后，需要单独完成激活。

![](img/991b34a59b9e4e16a207da340a11a107.png)

填写过程中，公司资料继续使用之前注册的美国公司信息。

![](img/700223dc4a08a30a0884757002712fb6.png)

身份验证环节，如果没有SSN，可以根据页面提示改用护照等身份证件完成验证。

![](img/d107250cab9092099af71d5f2b1e2547.png)

银行账户部分选择Mercury账户。

![](img/a8c5a9856d6aa185e1136e9117654603.png)

审核通过后，Stripe会发送邮件通知，之后就可以开始收款。

![](img/4277f294dfc41356a9e12a506a98a513.png)

# 三、申请Mercury商业银行账户

Mercury是一家面向创业公司、互联网企业和电商团队的数字银行服务商，成立于2017年。它支持在线申请，也接受非美国居民通过美国公司申请商业账户，常用于绑定Stripe、PayPal等收款平台。

需要注意的是，Mercury目前不提供个人账户，必须以美国公司为主体申请。

通常来说，银行开户需要企业已经拥有EIN。不过，由于Mercury与Stripe Atlas存在合作关系，即使EIN还没有下来，也可以先提交申请。

## 申请入口

Mercury官网：

https://mercury.com/

但如果你是通过Atlas注册的公司，建议不要直接从官网开始，而是进入Atlas后台提供的专属入口。这样可以自动带入一部分公司信息，减少重复填写。

登录：

https://dashboard.stripe.com/atlas

找到“Open a business bank account”，在Mercury项目旁点击Apply。

![](img/e0595e7e0dbaaf85aafec7254589d458.png)

接下来创建Mercury账号，并回答一些基础问题。

![](img/ef7f8fef71204b4efd9950477eb0adfa.png)

完成邮箱验证。

![](img/532b5553473191ace18b2f68215c9085.png)

填写公司名称。

![](img/133ec544c04a7159d53f0b1018f899f3.png)

### 设置Mercury callsign

Callsign可以理解为账户标识，我当时直接填写了公司名称。

它主要用于生成个性化的账户信息，例如专属转账邮箱、推荐链接等。这个标识类似用户名，需要具有唯一性，不能与其他用户重复。

例如，系统可能生成类似：

yourcallsign@mercury.com

这样的地址，用于收款或处理相关银行事务。

![](img/9c3cfdb808714fd6fde82734512a87fc.png)

### 公司类型选择

当系统询问公司是否属于列出的特定类型时，如果都不符合，可以选择“None of the Above”。

![](img/98ee5defb659d21e0b07e7da56148d47.png)

### 账户功能选择

系统会询问你对哪些银行功能感兴趣，我当时选择了前四项。

![](img/4d150765bbfef36d6173d495c921ffc2.png)

### 员工情况

如果目前没有相关员工，选择“None of the Above”。

![](img/33faf62b41078f9c0edd5109258f8052.png)

### 融资计划

如果近期没有融资计划，可以选择：

“No. I have no immediate plans to raise capital.”

![](img/8aeb11b0aef50c858b5b9c7097d7bade.png)

完成基础问题后，会跳转到正式的公司资料页面。

## 1. 补充公司信息

主要包括：

- Legal business name：公司法定名称；
- Country of incorporation：选择美国；
- Phone number：填写美国电话号码；
- Company website：可以根据实际情况填写，没有也可以暂时不填；
- Company type：选择LLC；
- Industry：按照实际业务选择；
- Company description：如实说明公司经营内容；
- Major investors：没有则留空。

![](img/341df3d617ec39a1b329fc3b63b6a97f.png)

## 2. 填写公司地址

这里通常会区分两种地址：

- 公司法定地址；
- 实际办公地址。

![](img/ca766a2eb0cec08d8645db0213c2d84e.png)

如果是从Stripe Atlas跳转申请，部分资料会自动填充。

若没有自动带入，可以这样处理：

- Legal address：填写Atlas后台提供的注册代理地址，可在以下页面查看：

https://dashboard.stripe.com/atlas/company

![](img/c6b626076e7250a696698e6b3edf58db.png)

- Office address：可以填写目前在国内的实际居住地址，使用英文格式即可。Mercury允许填写国际地址。

![](img/878047ba0277f4fb0d0e1e50f21154d1.png)

## 3. 完成个人身份验证

接下来需要提交实际控制人的资料，包括：

- 个人手机号；
- 出生日期；
- 当前居住地址；
- 护照照片；
- 自拍照。

自拍验证通常会调用电脑摄像头，按照页面提示直接拍摄即可。

![](img/c975eea8c74a3834e2e9bea13384c616.png)

此外还需要提交地址证明。我当时上传的是招商银行信用卡账单PDF。

![](img/224c1c8fa0a994d1bcf4fe1b3e9886dd.png)

招行App里埋着一个很少人知道的入口：查账 → 更多 → 补发历史账单。进去之后有两个落点可选——直接推送到邮箱，还是下载到手机。勾选“加盖印章”，圈定好月份，提交即可。这边有个小坑：如果账单上的通讯地址和Mercury那边预留的对不上，先去App里把地址改成两处一致的状态，招行是秒级生效，然后再重新生成一份PDF账单。

![](img/105845320ea974049ca93af7f07d3fb0.png)

所有必填项确认完成后，页面上会冒出绿色的“Complete”提示。

![](img/45b34816025788c420b5ec7da0de8bd8.png)

## 4、公司资料
系统会把已有信息自动回填，几乎不用动手，直接点“继续”往下走。

![](img/7b290295665fcd782d8fa4174836d63b.png)

## 5、预期业务
“账户会不会发生跨境收支？”——选Yes。

![](img/c4935ede18111841b7b10232054ac1ce.png)

## 6、问题清单
这一节是一连串的问答题：

![](img/7891d2e7bd0f099ee5e47c6ba7fb0fde.png)

第一道：Do you currently have employees, investors, customers, suppliers or locations in the US? / 你在美国目前有无团队成员、出资人、客户、供应链渠道或线下场所？我勾的是“No, but I plan to in the next 6 months”。

![](img/5c52036e2be9d9878d14ad9b1e35cbdd.png)

第二道：Where will your first deposits come from? / 你的首笔入金将来自哪里？这里如果选self，就要上传银行账单凭证；

![](img/366107ab1e075e7cfa9089180b0cd8d9.png)

其实还可以挑Revenue（营业收入），这样银行流水就不需要交了。

![](img/285166751a7668d55f5b3e8e2ee16b3f.png)

第三道是地址核验，我传的同样是招行信用卡的账单PDF。

![](img/7682ae7cf0b27dd9484aa49a34e616dd.png)

还有两题比较开放：Who are your target customers/clients?（目标客群是谁？）和 How do you usually receive payments and what other types of transactions do you expect to flow through this account?（平时靠什么方式收款？计划让这个账户跑哪些业务？）。写不出漂亮回答的话，截个图丢给AI润色就行。

![](img/9aaf6e35e0e8c128a8b2b4bebebd21b1.png)

再往后会问“你的账户将来会不会涉及以下行为”，我一律填了None of the above。

![](img/3af75ff7ca136f619c7e6eb15067018a.png)

提交。

![](img/bb0c387de30f5222c01748ad45c77d1f.png)

几个钟头之后，邮件如约而至：Mercury银行开户成功。

![](img/2feea5291ed382c53b8a0dbc67173171.png)

接着还会有一封卡片已准备就绪的通知。此刻跑进 https://app.mercury.com/dashboard 看，满屏功能键都按不了，只剩一串账户数字孤零零挂在页面上——这是因为它要求账户先进一笔钱来激活。眼下不急着入金，先拿着卡号也没事。把水星的收款信息录进Stripe控制台，等生意来了再提款过去，一切顺理成章。

![](img/a47727b72c90e23283e667583de2a131.png)

## 7、EIN佐证文件
IRS把EIN批下来一般要等上数周，我的倒是快，两周就收到了。随后Atlas也会来信提醒，并指引你去完善公司档案。

从Atlas控制台进入更新页：https://dashboard.stripe.com/atlas

![](img/9c58c975644caf5bdfe62779ec1411c5.png)

![](img/3dee2304c7170e5d46c347eaef896bd3.png)

紧接着需要上传一份EIN获批凭证，下载入口在 https://dashboard.stripe.com/atlas/documents，我直接用官方给的147c Letter/Approved SS-4文件。其他问题照着事实填就好。

![](img/be7f0ca3aae54e5b419a8899dc7d0abf.png)

至此，水星开户的整个流程就算通关了。最后别漏掉Stripe那边的银行绑定，等Stripe有余额后拨一笔到水星，账户功能就会自动全部打开。

![](img/29319a17cb7ac2bc8674e31d3f279344.png)

## 8、把Mercury接到Stripe
入口：在“设置”的“商户”菜单下找到“银行账户和货币”，直达 https://dashboard.stripe.com/settings/payouts，图片里就是我已经绑完的样子。

![](img/408abfa5da7c9dbdb4c8f58844982cf0.png)

## 9、把Stripe的钱拨给Mercury
有收益后，去资金页面点“提现”按钮：https://dashboard.stripe.com/balance/overview，也可以让它每天自动转出。通常一个工作日就能落账，碰上周六日或节假日就要顺延。

![](img/f575f8ff4ba78cdaecbc5ebbcd4a3113.png)

![](img/ae25f3ff06fc54fe1fd1104bfbe5ed52.png)

# 四、Mercury里面的钱怎么处理

## 1、线上直接刷卡
水星会派发一张虚拟卡（Debit Card），卡面对应着一组完整的卡号、到期日和CVC码。像是域名注册、云主机、ChatGPT订阅这些都能刷。国内卡经常被海外AI订阅拒之门外，但水星的虚拟卡基本没遇到过障碍。

![](img/ec456314f995db6cf69910987885321c.png)

## 2、电汇到香港卡
走跨境电汇渠道，就能把钱从水星转到香港的银行账户。

![](img/0faa3f5811f49839f9ac4293cb3cea09.png)

头一回操作要先新增一个收款对象（Create recipient）。

![](img/028b3b813074d3147b27ff9cdc143a54.png)

这个对象创建好后，系统会让你填对方的银行资料，信息都能在目标银行的App内翻到。付款方式那一栏，我挑了“International wire - USD”。

![](img/fc2ba9e47af86da59346bdbe373c4bb8.png)

实测了一笔：汇100美元到众安银行（香港），真正到账80美元，中间的损耗不小。

![](img/000c48cec6366c911b58af491d4d492e.png)

## 3、回内地银行卡
从水星直接汇进内地卡是行不通的。可行的路径是：水星 → 香港汇丰/众安 → 中国银行（香港） → 内地同名的中国银行借记卡。这条链路我因为收入还少并没有真正走通过。想抄作业的话可以上📕搜类似笔记，比如这篇：

https://www.xiaohongshu.com/explore/680a22d0000000000d0146f6?xsec_token=ABRRl7rDUVEErRTZqPQbUPLvTweCsa73pzuA_nUMY1lmo=&xsec_source=pc_user

![](img/81bf31d9d9f5efc645bec4a26a0f962b.png)

## 4、一些补充
中国银行（香港）的卡可以绑定到WeChat Pay上，这样在国内线下也能直接刷，币种是港币。我自己前两天吃饭时亲测了一回，确实能付。具体做法：先开通WeChat Pay HK，🛰️里搜“🛰️支付香港”即可自助操作；然后把钱包地区切成香港，注意只有完成开通才会出现这个切换入口；最后把中国银行（香港）的卡绑定进去。但要留意，这个钱包目前仅兼容中国银行（香港）卡，众安、汇丰等其他港卡都绑不了，因为需要有香港身份认证。

![](img/92a6108d60f5c2611c4c1d2c95f02398.png)

![](img/f9c813e3c1788c72d590391f4695be67.png)

![](img/35e9238624326d3ff4d70b41fb09f811.png)

# 五、Stripe的第一笔收入

## 1、看到需求
四月第二周，GPT-4o的生图能力彻底火了，特别是那种吉卜力动画质感的图片在社交平台霸屏，网上冒出一大批范例，还有人整理成了项目合集：https://github.com/jamez-bondos/awesome-gpt4o-images

4月6日，我在X上刷到一个博主把宠物照片处理成人物写真的案例。先用Google Trends瞄了一眼，热度指数不算火爆，走势也不惊人，就没当回事。谁知道几个小时后，群里的哥飞又丢过来一条即刻链接，歸藏也在讨论宠物转人像的应用，看来大家都嗅到了味儿。

![](img/d0956d599adbd32fa6f3d79892944891.png)

尝鲜成本这么低，不试白不试，我决定下场。前后花了四个钟头拼出一个AI图片站，功能很聚焦：用户传一张宠物照，后台调用GPT-4o生成人像，但要尽量不破坏原始的表情、动作与构图。关键词敲定pet to human，SEO的主攻方向也锁定这个短语。

站点地址：https://pettohuman.com/

![](img/b9211a34d8e6b22bf4f00a73dbe4847d.png)

![](img/b5fec28e471efa40b57729c3f7cf9dd1.png)

![](img/7d41ac59389d04f0d845e5e267ac4cdb.png)

![](img/e893b9f6c378e94d9359cc1b00267e73.png)

![](img/1302ec00fc835ef7d81c7ae1f713e714.png)

![](img/b309301b55c30d866d1367bf05d3657d.png)

第一版很粗糙，不设登录，不接支付，打开就能玩。先跑几天观察数据，如果流量能起来再付费也不急。

## 2、补齐账号与付费
4月7日正式对外开放，当时每天只有几十个人访问。结果4月8日一下子涌进来1000多位访客，API成本当天接近200块人民币。我立刻决定：该上支付了。

![](img/71388ba2ab5d07637a0ed71766ad3600.png)

Stripe是头一回碰，踩了一路坑，一直到4月9日天快亮时才把付款链路调通。产品策略也随之确定：每个账号登录后可白嫖一张图，想继续用就得买点数。上线当天居然就开张了，成交额1.9美元——不多，但也称得上有纪念意义。流量最高峰时，每天要生成2000多张图，下单付款的基本稳定在30到40人。

![](img/45168503518b3777f05fd17bb077eb3f.png)

![](img/5fecc21ad8d199e8b1e078d785f7e0e5.png)

## 3、流量一路下滑，怎么办
好景不长，从4月14日起，访客数据就开始一天不如一天。起初我还安慰自己只是正常波动，直到4月18日眼睁睁看着日活滑到100出头，才不得不承认出问题了。

![](img/80dcac49e303ff353b51f78875671058.png)

### 原因拆解
先看Google Trends：红线是GPTs的热度，蓝线是我做的那组关键词。蓝线在4月14日见顶，之后就头也不回地往下走——外面的搜索需求正在收缩。

![](img/adde8e247caece325228680adaf46617.png)

再翻开Search Console，站点的平均名次在4月15日附近开始连续跳水，最差掉到45到50名，位次越靠后，点击自然越少。回想刚上线时，我们的平均排名还在前二；后来猜测是同类站点扎堆出现，内卷加剧，加上我又没怎么做过外链，域名权重太低。

![](img/99b61669a7ecab31112ce56be598fafc.png)

### 补救一：铺外链
热度高低左右不了，那就用外链把排名顶上去。我一共撒出去六十多条友链，类型覆盖网址导航、博文投稿和留言区。当然不可能全被收录，用Ahrefs查下来，真正被记录的来源域名只有20个。好在外链的回报还算快，排名肉眼可见地慢慢回来了。

![](img/b568ad89afe31ee14bf2aef47f88467e.png)

![](img/372ff315339871afe75a5161c18ba108.png)

### 补救二：做视频
然后又拍了些短片发去YouTube和TikTok，简介栏里挂着站点链接，盼着能导点流。YouTube的成绩偶尔不错，有一两个视频播放过万；

![](img/e3141dfce474c3f7874ef59119db02cc.png)

TikTok就相当惨淡了。

![](img/6f0f5c0ca2ccd477a784df257033a13f.png)

Instagram和Facebook也都同步发了，几乎没什么人看。至于这些视频到底带去了多少访客，没法精确统计，只能看到网站每天还是100多人，没见增长。再加上关键词本身的Google热度一天比一天低，基本可以断定这是一波短期热词，来得快去得也快。我4月的Stripe入账曲线，就是这种“大起大落”的写照。

![](img/c69818e331589925779362b8c1ebd71b.png)

## 4、广告分成尝试
上线次日恰好撞上1000多位访客的高光时刻，我顺手递交了Google AdSense的申请。结果审核耗了20多天，等它批下来时，流量已经凉得差不多了，广告分成一天也就几毛钱。

![](img/a76c5ffbe19345b7c6bd411f8ad9532f.png)

后来才知道，不只有AdSense一条路，Adsterra、Monetag也都挺方便，且没有AdSense那种严格审核。我在等待期间顺势注册了Adsterra，一会儿就批了下来。

* Adsterra：https://adsterra.com/
* Monetag：https://monetag.com/

![](img/8ed276ab15ab965dd9740b82e19e0b75.png)

Adsterra前前后后给我贡献了5美元。

![](img/cfaac71696922f8b8b1329eee771f3d5.png)

## 5、换关键词挖坑记
顺着GPT-4o画图这条线，我又试了好几个题材，结果没有一个跑出来。放在这里当反例。

### 人像变动物
既然“宠物变人”能行，那人变动物呢？于是照葫芦画瓢做了个站：上传人像照片，AI在保留表情、穿搭、姿势的前提下生成对应的动物形象。

![](img/37ffe3d7afb80086d2e32408f3602f05.png)

![](img/d24eda8a024a5d6ba12f3d1d2ec4e605.png)

![](img/7ecd4bf157ee1d01ca61c97b4396b2c0.png)

![](img/f23d3da3bd78bda9475a8ffce322aaaf.png)

![](img/958fc4a5be3d2140d543fe9c5ca4decb.png)

需要说明的是，这些示例图中没有一张是真实人像，均为AI合成。整个站没花多少功夫就上线了——https://humantopet.org/——可惜流量十分低迷。

![](img/26bd181133a7dc1658de48d04f893115.png)

### 宠物换装
接下来又冒出一个自以为聪明的点子：人买衣服要试穿，宠物买衣服是不是也该试穿？那就做个宠物试衣间——用户传上宠物照片和衣服照片，AI帮你合成宠物穿好衣服的效果，出图会包含正面视角和侧面视角。

![](img/1927cac36c7157e31878ae874976007b.png)

![](img/616035aeeeb7fe3b4d2b4ac3907f2b6f.png)

![](img/42f070f5678dfe9f21451cfb8c9694f2.png)

![](img/69bb525aebe92e99c109e1845aa5567c.png)

![](img/ace237f6eae74f0a0e60101432acdecf.png)

![](img/66a2fd377fbc285f0d1d348cd63aba9d.png)

这类需求到底真不真，我也和AI讨论过一阵，记录在：https://grok.com/share/bGVnYWN5_46dc23aa-adb1-4c02-baa3-c2096c247b2b

![](img/98f091d613057b7b10ca2b930e6c2c2f.png)

![](img/42834d9cac676b3dff044867b966f853.png)

![](img/444508b011a491a21dd51e0c79cd9b83.png)

AI直接判定这是一个机会，于是我立刻动手，几小时之内就把功能搭好发布上线：https://pettryon.com/，上线后访问量却寥寥无几

![](img/35dd39b614f58521c4f8b4f63af0e7b9.png)

### X光风格转换

随后我又碰到一个挺有意思的功能，能把人或宠物的普通照片渲染成X光透视效果。

![](img/0384dac316f2dce10fd95ed0d118f0f5.png)

我跟AI聊了聊，它觉得这玩意儿大概率没人会用。但我心里还是存着侥幸，总觉得这么好玩、这么吸睛的效果放上社交媒体肯定能爆。

于是照旧开工，利用几个小时快速把站点做出来：https://xrayify.com/，结果依然是流量平平

![](img/fba8d974f9aa525247ef39cd8f9c2193.png)

### 掉进的坑：靠想象硬造需求

其实以上这三个AI绘画相关网站的灵感，全都源自我自己的脑补。

开发前我也查过相关关键词在Google Trends上的表现，热度不高，搜索需求也很弱，但我选择性忽略了数据，固执地认为这个点子太酷了，肯定有人要。于是直接开造。最后的反馈也很公平：访问量差到让人难受。

这件事让我重新想起 @刘小排 老师写过的一篇关于如何获取产品灵感的文章：https://t.zsxq.com/eiQtm，里面就讲过“凭空捏造的idea”成功概率非常低。文章我早看过，但没真正入心，亲手踩坑后才彻底记住了。

![](img/911d526228aa7b4814ac08a3ea5f3f68.png)

![](img/5d6a8c3a38d483dc1ad834ea9cf16330.png)
End.

最后祝各位出海创业都能多赚美金！