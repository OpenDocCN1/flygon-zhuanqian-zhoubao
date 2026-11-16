# 用美区 Apple ID 搞定 ChatGPT 注册与 Plus 充值全流程

# 先说难点

目前 OpenAI 已经对大陆、香港、澳门、韩国、俄罗斯、台湾等地区做了访问限制，用这些地区的支付工具基本都无法完成扣款，包括 PayPal、VISA、Mastercard 等。

OpenAI 允许开通的区域不包含中国大陆，会通过网络环境和 IP 地址来判断你的所在地，一旦识别到在国内，连登录注册都会受阻。因此在动工之前，先把 IP 调到美国，可以通过 https://ip.cn/ 来核验当前节点。🪜违法，请自行注意合规风险。

ChatGPT Plus 的结算走的是 Stripe Checkout。理论上 Stripe 能受理大部分银行卡，包含大陆的 Visa/万事达乃至银联，但 OpenAI 在 Stripe 端对发卡国家做了白名单限制。

我先后测试了十几张以上的实体卡和虚拟卡，涵盖国内实体卡、香港虚拟卡、美国虚拟卡，还有全球付的香港虚拟信用卡以及万里汇的香港虚拟信用卡，均无法绑定成功。

综合测试结果，暂时能用的卡段大致如下：

=531993 DePay，需用 USDT 充值

556766 NobePay

=489683 Qbit Visa，存疑

= Payoneer 的信用卡 529366 可绑定 OpenAI/ChatGPT Plus

= QBIT 虚拟信用卡 489683

540524 卡段实测可成功绑定 Plus

556150 卡段实测可成功绑定 Plus

明确不行的卡：

* 国内招商银行 VISA/MASTERCARD、全币卡

* 全球付香港虚拟卡

* 万里汇香港虚拟卡

我们持续在观察 AI 的演进，半年时间过去，ChatGPT 已具备多模态能力，工作水准已接近全球顶尖名校毕业生的量级。但这些强能力集中在 4.0 上，而 4.0 必须依赖 Plus 会员才能使用。

![](img/zhuanqian_b480c9fd43cf5a98b77afd623e5636d8.png)

在这种情况下，身为国内用户，没有美国手机号和信用卡，充值成功率极低；对非跨境公司而言难度更高。可与此同时，这也催生了代注册、代充的生意空间。

# 本篇要解决什么

本篇聚焦在如何顺利注册账号、避免被封，以及如何完成 Plus 充值。至于后面怎么用、怎么学，可以参考圈内其他人的分享，黄小刀在实操层面就很专业。文中 ChatGPT 统一简写为 CT。

# 方法来源与验证时间

本方案源自龙哥盟航海家群的分享，我在 2023.10.19 两天内实测了两个账号，从注册到充值全部成功，现整理出来供参考。

核心思路：用苹果手机登录美区 Apple ID，下载 CT 客户端，给美区 Apple ID 充值，然后在 CT App 内完成订阅。

# CT 账号注册

最稳的做法是用微软账号直登，因为 OpenAI 与微软深度绑定。微软的 Outlook 邮箱免费可注册，无额外成本。

1. 打开浏览器无痕窗口，减少设备指纹关联。

![](img/zhuanqian_c2015db69cbd17c351efc28c3dae60d7.png)

1. 进入 https://www.microsoft.com/en/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook ，注册一个 Outlook 邮箱。

![](img/zhuanqian_581b5bbf3f653213b2d8728d000201fe.png)

![](img/zhuanqian_76e4b38ce393bade144e11b72aa6cdb8.png)

![](img/zhuanqian_40bb039d1671800014d38b20cdbb3a15.png)

![](img/zhuanqian_fbe04af9f17ed3a915909f2345d62c69.png)

![](img/zhuanqian_e89456f21fedbd74e5e2206a67af73b4.png)

![](img/zhuanqian_18d317e41d3b4e9b4701d3b207d7d236.png)

![](img/zhuanqian_3ac573b5e7f3f3834404e6c17863ef0f.png)

1. 登录 https://chat.openai.com/auth/login

![](img/zhuanqian_b57209400eb3aa68fb75431ee3c29265.png)

![](img/zhuanqian_4638115114aabffc713cb4c752ba74d6.png)

![](img/zhuanqian_a58cb1a1fe927c8a5126f2cd4c8753b4.png)

![](img/zhuanqian_536d5c642b7f8d2d351a1244e35db457.png)

![](img/zhuanqian_0f6c391bd9481ab0f73570458873f790.png)

https://mp.weixin.qq.com/s/P6mOqTihAkun49q7rGB5IQ

不会用接码平台的小伙伴可以看上面的链接，教程依然可用。

完成以上步骤，账号就算注册成功了。

# 注册美区 Apple ID 的注意事项

这一环节坑最多，网络环境和 IP 必须保持在美国，否则注册失败。

1、直接参考这篇教程注册美区账号

如何注册美区苹果账号

重点提醒：

1、国家与地区必须选择美国，手机号可以用中国大陆的正常手机号。千万不要用虚拟号码，我之前就因为用虚拟号导致连续挂掉 3 个账号。Apple ID 后续验证场景很多，虚拟号不稳定很容易被封。

2、用电脑注册经常收不到短信验证码，后来改用手机注册，手机网络环境调成美国、语言调成英语，成功率大幅提升。

3、Apple ID 注册完成后，付款时需要填写账单地址，一定要选美国免税州，邮编要对应。美国免税州地址、邮编汇总可参考 Usitrip 走四方旅游网。我之前几号扣款失败，主要原因就是填了非免税州，导致后续只能用美国信用卡修改账单地址。

# Plus 充值实操

支付环节大概率会触发 Apple 风控。这时可以拨打 Apple 官方客服电话申请人工处理，通常 10 分钟左右可解决。

一个 Apple ID 最多只能对应一个 CT 的 Plus 账号。如果要批量操作，就需要多注册几个 Apple ID。目前我用一台手机已注册 5 个 Apple ID 未出现异常。流程上建议：新注册 Apple ID 后，重新下载 CT App 再进行订阅，避免信息残留。

这里面存在明显的差价空间。市场价上，注册一个号在 50-100 元之间，代充一个 Plus 会员约 180 元人民币，自付成本约 19.99 美元，折合人民币不到 150 元。熟练后，注册+充值一条龙大约 20 分钟，时薪可达一两百元。

祝大家龙哥盟。