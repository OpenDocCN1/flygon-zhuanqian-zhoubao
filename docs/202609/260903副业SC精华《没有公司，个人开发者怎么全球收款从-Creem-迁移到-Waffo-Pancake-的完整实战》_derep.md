# Creem 被风控后，我把收款切到 Waffo Pancake 的实操全记录
作者：龙哥



![](img/67c37faeb967b1478183a189236a069f_0_0.png)

> 小懒判断 | 遇到 Creem 封号导致收款中断的出海个人开发者可以直接照做，还没上线站点的先收藏备用，审核核心在于你能否提供真实可访问的产品站点。最有参考价值的是那张费率清单：国际信用卡 3.9% 加 0.5 美元，2.99 美元的低价包因固定手续费占比接近两成，定价前务必先算清楚。最易翻车的点是 AIGC 合规评审，法律页面表述空泛、AUP 未覆盖六大禁止类型或缺少举报邮箱，首次提交基本会被驳回。

各位好，我是龙哥。赚钱社区六年老成员。

小排老师第二期 AI 编程深海圈学员，深海圈千刀户认证。

从去年起我把重心放在 AI 产品出海上，受主业限制一直未注册境外公司，也没有港卡，付费收款环节一直受限。

此前支付一直用 Creem，今年 5 月起 Creem 大规模风控，我的账号也中招，多次申诉失败，期间收入受损。具体情况可参考小排老师的《Creem 之后，AI 产品收款用这两家-刘小排》。

目前我已完成从 Creem 到 Waffo Pancake 的迁移落地。

我实现的效果如下，和我情况相近的可参考：

- 无海外公司、无营业执照；
- 仅凭中国大陆身份证完成个人身份验证；
- 通过 Waffo Pancake 的正式生产审核；
- 一次性积分包、月付、年付订阅均已上线并完成收款；
- 已绑定个人支付宝及国内银行卡实现出金；

本文发布于 2026 年 8 月 31 日。费率、覆盖国家、出金渠道与审核规则存在变动风险，文中数据均为我申请时官网、后台及客服的口径，实操前请再次核对官网。

我还在持续迭代，如有偏差欢迎指正，避免误导。

## 一、先把两条产品线区分清楚

第一次踩坑就是选错入口。很多人听说 Waffo 可收款，就去主通道申请，看到要公司主体就退缩。

Waffo 市场经理邮件里解释过两条路线：

| 路线 | 适合对象 | 主体要求 | 典型用途 |

| :--- | :--- | :--- | :--- |

| Waffo 主通道 | 已公司化运营的商户 | 香港、新加坡、日本、美国等公司主体 | 企业收单、多支付方式、对公结算 |

| Waffo Pancake | 独立开发者、初创、AI/SaaS 小团队 | 可无海外公司，以个人身份申请 | MoR 全球收款、订阅、积分包、个人提款 |

没有公司的个人开发者，正确入口不是企业 Sandbox，而是：

https://pancake.waffo.ai

官方文档地址：

https://docs.waffo.ai

官方给我的说法是：Pancake 专为 AI 个人开发者和初创设计，不强制公司主体；只要品类不在禁限清单内即可提交店铺审核，由风控后续判断。AIGC 类目审查更细，周期也更长。

![](img/67c37faeb967b1478183a189236a069f_2_0.png)

### Waffo Pancake 到底是什么

先说背景。Waffo 总部在香港，是全球支付与商业化平台，Waffo Pancake 是其面向开发者与数字产品的 MoR 方案。按 Waffo 2026 年 1 月公告，公司累计融资 3000 万美元，投资方包括 Illuminate Financial、高榕资本、HSBC、BAI Capital；官网同时披露香港 MSO 牌照与 PCI DSS 认证。

Pancake 并非普通支付网关，而是 Merchant of Record，简称 MoR。

传统通道商只负责资金流转。税务、发票、退款、拒付及各国销售税的法律责任仍在商户方。

MoR 的逻辑是：

用户向 Waffo Pancake 付款 → Waffo 作为法律销售方收款并处理税务 → 扣除费用后结算给你。

官方说明其会统一处理全球税费计算与缴纳、开票、支付、退款、拒付与争议。你只需对产品本身、内容合规、交付与客服负责，无需自行研究各国 VAT、GST、Sales Tax。

### 费率、退款、拒付、出金成本

按 2026 年 8 月 30 日官方费率页整理。

## 1. 成功交易

| 支付方式 | 费用 |

| :--- | :--- |

| 国际卡、数字钱包 | 3.9% + $0.50/笔 |

| 🛰️支付 | 3.9%，无 $0.50 固定费 |

| 月费、接入费 | 0 |

固定 $0.50 对低客单影响很大。以 $2.99 体验包为例，刷国际卡手续费约：

$2.99 × 3.9% + $0.50 = $0.6166，占比约 20.6%。走🛰️支付仅约 $0.1166 的比例成本。

定价时必须把支付成本、模型 API 成本、退款与获客成本一起纳入考量。

## 2. 失败交易

卡支付进入 3DS 后失败，部分类型会收取 $0.30/次。未进入 3DS 即流失则不收费。

高风险流量不仅转化差，还会产生失败交易成本。

## 3. 退款

- 每笔退款处理费：$1；
- 原交易 3.9% + $0.50 不退；
- 全额或部分退款规则一致。

## 4. 出金

- 最低出金金额：$20；
- 手续费：1%，单笔最低 $10；
- 销售后约 10 个工作日进入可出金余额；
- 发起后 1 至 3 个工作日到账；
- 目前中国大陆支持人民币结算到银行卡或支付宝。

因单笔最低 $10，小额商户不宜频繁出金。比如提 $500，1% 仅 $5，仍按最低 $10 收；提 $2000 才按 1% 收 $20。

客服给的额度口径：

- 支付宝：单笔不超过 5 万元人民币，年累计不超过 30 万元；
- 银行卡：单笔/单日 50 万元，月累计 200 万元；
- 美元出金计划 9 月上线，支持 Wise 与香港汇丰。

以上为当时邮件截图，政策在更新，申请时请再确认。

5. 个人申请准备：目前公司与个人审核流程一致，后续需对公出金时才收集公司信息。建议提前准备：① 申请时填写真实产品域名，审核通过后不支持随意更换；② 客服邮箱最好使用与站点同后缀的。审核时长一般 1-3 个工作日，可先提交。

6. 国内银行卡出金补充：目前支持人民币转入国内银行卡与支付宝。结算周期 T+10 个工作日，以香港节假日为准，结算后发起出金，到账 1-3 个工作日。手续费 1%，最低 $10。限额：支付宝单笔 5 万人民币、年 30 万；银行卡单笔 50 万人民币、月 200 万。美元出金 9 月上线，支持 Wise 与香港汇丰。

## 二、个人申请与过审要点

Pancake 个人身份认证需要：

- First name：名的拼音/拉丁字符；
- Last name：姓的拼音/拉丁字符；
- Legal full name：身份证上的中文法定姓名；
- Country/Region：CN；
- ID Type：大陆居民身份证或护照；
- ID Number：18 位身份证号，或符合规则的护照号；
- 可收验证码的客服邮箱；
- 产品域名的控制权；
- 与法定姓名一致的银行卡或支付宝账户。

注意英文栏填拼音，法定姓名栏填身份证中文。法定姓名后续作为出金户名，空格、标点、顺序不一致可能导致打款失败。

团队建议使用与网站同域的邮箱，更易证明归属，减少邮箱不一致问题。

### 如何提高通过率

Waffo 对 AIGC 审查较严。AIGC 属于限制类，非默认禁止。官方至少要求：

- 不侵犯第三方知识产权；
- 明确披露内容由 AI 生成；
- 自有品牌，不冒充模型官方；
- 如实披露底层模型；
- 对提示词与生成结果做内容审核；
- 发布公开 AUP；
- 提供真实违规举报渠道；
- 保留审核与处置记录。

合规文档要求 AUP 至少明确禁止六类内容：色情与 NSFW；暴力血腥；仇恨言论；儿童不安全内容；Deepfake、未经授权冒充他人；侵犯版权或商标。

平台会检查是否逐项列出、是否有举报邮箱、举报后处理流程、账号限制或封禁规则、代码是否真正实现审核。

我首次提交后未被永久拒绝，而是得到 needs_info / awaiting_information，并点名若干功能不合规。合规团队认为按 Visa/Mastercard 口径涉及 Deepfake 或高风险人物内容，给出两选一：

### 方案一：下线高风险功能
整改后重新申请全渠道：国际卡、钱包、本地支付。

### 方案二：保留高风险功能
仅能申请🛰️支付，无法开通国际卡。

我的用户在海外，选择方案一。我下线四项高风险工具，保留核心产品与 SEO 资产。

合规整改不是全站 SEO 自杀，应只下线高风险能力，而非把正常业务一起砍掉。

提交前务必自查，官方店铺审核清单很实用。我结合两次自检整理出最低要求：

| 项目 | 最低要求 |

| :--- | :--- |

| 产品 | 公开可访问，非 Coming Soon，也非登录后才可理解 |

| 定价 | 进入收银前可见价格、周期、权益 |

| Terms | 说明服务、计费、取消、退款、点数有效期、禁止用途 |

| Privacy | 说明收集数据、用途、第三方服务商、跨境处理、保留与删除 |

| AUP | 对 AIGC 六类禁止内容、审核、举报、处置逐项说明 |

| 客服 | 全站页脚直显有效邮箱，最好同域名后缀 |

| 退款 | 与收银台、Terms 规则一致 |

| 品牌 | 不冒充模型官方，不蹭商标 |

| 营销信息 | 不写虚假用户数、评价与无法证明的能力 |

| 模型披露 | 如实列出底层模型或在生成界面展示模型选项 |

我首次自检失败原因：

- 未写清个人经营主体与 MoR 关系；
- 未区分一次性点数包、月订、年订；
- 未写点数有效期、取消与退款；
- 未列出真实数据处理商；
- AUP 缺少用户举报渠道；
- 页脚未直接展示客服邮箱。

整改后，我在 AUP 中补充：用户可向客服邮箱发送 Content Report，附链接、截图、账号或订单；平台将做分级、自动审核与人工复核，必要时删除内容、限制功能或封禁账号。

同时把支持邮箱放到全站页脚，无需进入 Contact 页面即可联系。

## 三、个人申请完整步骤

按我实际操作顺序：

### 第 1 步：先做品类自查
查看官方禁止与限制品类：

https://docs.waffo.ai/zh/mor/prohibited-products

涉及 Deepfake、未经授权人脸/声音克隆、NSFW、侵权、赌博、破解软件、刷量等高风险业务，先改产品再申请。

### 第 2 步：注册 Pancake
打开：

https://pancake.waffo.ai

我的填写：身份个人；国家中国；产品类目 SaaS；计费模式订阅制。

![](img/67c37faeb967b1478183a189236a069f_10_0.png)

务必按实际情况填写。团队明确提醒，审核对象是该产品网站，通过后不支持换成完全不同站点。

### 第 3 步：创建商店与首个商品
商店名正常填写。起初不必建全套套餐，我先建最低价体验包：一次性购买 $2.99。

![](img/67c37faeb967b1478183a189236a069f_11_0.png)

先用一个真实低价商品跑通测试支付、Webhook 与点数发放，再补其他套餐，排错更简单。

![](img/67c37faeb967b1478183a189236a069f_12_0.png)

随后进入 Dashboard 配置 API 密钥与代码接入，其他设置可后续完善。

### 第 4 步：按指引完成 Dashboard 设置
Dashboard 右下角有新手指南，共 9 步。我习惯每一步截图给 Codex，让 AI 核对网站实际情况后再操作。

![](img/67c37faeb967b1478183a189236a069f_12_1.png)

审核填写部分，我简单列出我的做法供对照。

![](img/67c37faeb967b1478183a189236a069f_13_0.png)

业务类型选个人。

![](img/67c37faeb967b1478183a189236a069f_13_1.png)

地区选中国，协议全部同意。

![](img/67c37faeb967b1478183a189236a069f_13_2.png)

业务详情选“已准备好”。

![](img/67c37faeb967b1478183a189236a069f_14_0.png)

有无付费用户如实选择。

![](img/67c37faeb967b1478183a189236a069f_14_1.png)

姓名用全拼，如张三写 Zhang San。

![](img/67c37faeb967b1478183a189236a069f_14_2.png)

店铺名沿用之前默认值，固定一个名字，不要随意修改。

![](img/67c37faeb967b1478183a189236a069f_14_3.png)

联系邮箱用网站域名邮箱，需验证，必须准确。

![](img/67c37faeb967b1478183a189236a069f_15_0.png)

填写完整域名。

![](img/67c37faeb967b1478183a189236a069f_15_1.png)

![](img/67c37faeb967b1478183a189236a069f_15_2.png)

![](img/67c37faeb967b1478183a189236a069f_16_0.png)

Pancake 会询问现有客户、商家名称、业务介绍、产品详情、目标用户、定价与网站链接等。可让 AI 结合产品撰写，重点是让审核员快速看懂五件事：

1. 你是谁；
2. 产品做什么；
3. 用户如何使用；
4. 如何收费；
5. 如何控制风险。

合规检查全部同意。填写好产品域名、Terms、Privacy 后运行网站自检。AIGC 产品还需核对 AUP、客服邮箱、模型披露与内容审核。

AIGC 审核接口：

https://docs.waffo.ai/zh/api-reference/endpoints/content-safety/scan-prompt

自检通过不等于人工一定通过，这是基本门槛。

![](img/67c37faeb967b1478183a189236a069f_16_1.png)

最后确认手续费即可提交审核。

![](img/67c37faeb967b1478183a189236a069f_17_0.png)

我的审核约半天回复。务必留意邮箱，首次被退回概率很大，修改后继续申请。

![](img/67c37faeb967b1478183a189236a069f_17_1.png)

## 四、审核通过后的代码接入

别忘了，支付还未完全接入。Waffo 对 AI 友好，接入只需对 AI 说一句话。

```
Read https://docs.waffo.ai/llms-full.txt, load the official Waffo Pancake skill from https://docs.waffo.ai/zh/integrate/skill, and integrate Waffo Pancake payments into the current project.
```

![](img/67c37faeb967b1478183a189236a069f_18_0.png)

很快接入成功。

### 创建并映射商品
将网站付费产品加入，包括一次性与订阅类型。

![](img/67c37faeb967b1478183a189236a069f_18_1.png)

以上就是我的迁移全过程。若你正面临同样问题，希望能少走弯路。最后再次强调：支付政策、费率、出金通道会变，请以官方最新口径为准。祝收款顺利，出海赚钱！

Creem 毫无征兆地关停，让一大批开发者被迫紧急迁移收款方案，我也是其中一员。最终在 Waffo 上把整套收款流程重新拉通，这篇复盘按步骤记录关键操作，希望能帮你避坑。

第一步是商品配置。Waffo 要求每件商品都建立独立的 Product ID，价格不能作为判定依据，Product ID 也不该出现在前端。正确做法是在后端维护一张映射表，让自家套餐编号对应 Waffo 商品 ID，前端只认套餐编号。

第二步，创建 Checkout 的动作要在服务端完成。Waffo 提供了一套 TypeScript SDK，将 Merchant ID 与 Private Key 都留在服务端发起请求，拿到托管收银台 URL 后再抛给前端跳转。Private Key 的存放没有第二种选择：只能放在服务端的 Secret 区域，客户端一律禁止持有。

第三步，配置 Webhook。进入 Pancake Dashboard，切到 设置 → Webhooks → Production，Payload 格式选 Raw。一次性积分包至少要捕获 order.completed 事件。订阅模式建议把以下事件全部挂上：subscription.canceled、subscription.canceling、subscription.uncanceled、subscription.past_due、subscription.payment_succeeded、subscription.updated、subscription.activated。退款场景再加退款类事件。

第四步，配置提款账户。先看示意图。

![](img/67c37faeb967b1478183a189236a069f_20_0.png)

需要提交的信息包括：姓名拼音、中文姓名、身份证号码、所在国家/地区。

![](img/67c37faeb967b1478183a189236a069f_20_1.png)

收款方式二选一：支付宝或银行卡。

填完信息后先做支付验证，可以拿自己的🛰️扫码下一单。海外银行卡也可用，Waffo 在邮件中的说法是覆盖 160+ 国家；而 MoR 说明文档里目前的数字是 173。这类数值会持续变化，以提交申请那天的 Dashboard 上真实开放的支付国家和方式为准。

正式上线前，将右上角的开关拨到生产模式。

![](img/67c37faeb967b1478183a189236a069f_20_2.png)

随后进入 API & 开发模块，创建生产级 key 即可。如果对 key 配置没有把握，同样可以让 AI 代劳，官方连提示词都备好了。

整套流程到这就结束了。从 Creem 关停开始，到 Waffo 上收到第一笔真实款项，希望这篇手记能帮你避掉那些最典型的坑。祝早日审核通过、稳定出金！作者：独孤风。有问题来评论区聊，想私下交流可以找鱼丸。

![](img/67c37faeb967b1478183a189236a069f_21_0.png)

附录：官方入口与文档索引全集

以下仅保留 Waffo 的官方渠道信息。如果文中的说法和后台界面不一致，请以申请当天 Dashboard 的展示、官方说明文档以及客服的书面答复为准。

**① 入口与账号**
- https://waffo.ai（Pancake 官网）
- https://waffo.dev（开发者产品站）
- https://waffo.com（公司官网）
- https://pancake.waffo.ai（注册与登录）
- https://docs.waffo.ai/zh（中文文档）
- https://docs.waffo.ai/zh/quickstart（快速开始）
- https://docs.waffo.ai/zh/feature-list（功能总览）
- support@waffo.ai（客服邮箱）

**② 费率与区域**
- https://docs.waffo.ai/zh/mor/what-is-mor（MoR 定义）
- https://docs.waffo.ai/zh/mor/fees（交易费率）
- https://docs.waffo.ai/zh/mor/supported-countries（支持的国家与方式）
- https://docs.waffo.ai/zh/mor/prohibited-products（禁售品类）

**③ 审核与店铺**
- https://docs.waffo.ai/zh/mor/account-reviews（账号审核）
- https://docs.waffo.ai/zh/settings/business-details（企业资料 / KYB）
- https://docs.waffo.ai/zh/merchant/identity-kyc（个人 KYC）
- https://docs.waffo.ai/zh/settings/email-verification（邮箱校验）
- https://docs.waffo.ai/zh/settings/domain-verification（域名校验）
- https://docs.waffo.ai/zh/settings/store-settings（商店配置）
- https://docs.waffo.ai/zh/features/test-mode（沙盒模式）

**④ 合规与法务**
- https://docs.waffo.ai/zh/mor/account-reviews/aigc-compliance（生成式 AI 合规）
- https://docs.waffo.ai/zh/mor/account-reviews/tos（ToS 模板）
- https://docs.waffo.ai/zh/mor/account-reviews/privacy-policy（隐私条款模板）
- https://docs.waffo.ai/zh/mor/account-reviews/aup（AUP 模板）
- https://docs.waffo.ai/zh/api-reference/endpoints/content-safety/overview（内容安全 API 总览）
- https://docs.waffo.ai/zh/api-reference/endpoints/content-safety/scan-prompt（Prompt Sift 安全扫描）

**⑤ 商品与订阅**
- https://docs.waffo.ai/zh/features/products（商品说明）
- https://docs.waffo.ai/zh/guides/ai-billing（AI 用量计费）
- https://docs.waffo.ai/zh/guides/one-time-payments（单次收费）
- https://docs.waffo.ai/zh/guides/subscriptions（订阅收费模式）
- https://docs.waffo.ai/zh/features/subscriptions（订阅管理）
- https://docs.waffo.ai/zh/features/checkout（Checkout 说明）
- https://docs.waffo.ai/zh/checkout/checkout-flow（结算流程）
- https://docs.waffo.ai/zh/checkout/customization（收银台定制）
- https://docs.waffo.ai/zh/features/customer-portal（客户门户）

**⑥ 开发与 API**
- https://docs.waffo.ai/zh/integrate/skill（Skill 插件）
- https://docs.waffo.ai/zh/api-reference/authentication（接口鉴权）
- https://docs.waffo.ai/zh/api-reference/endpoints/orders/create-checkout-session（发起 Checkout 会话）
- https://docs.waffo.ai/zh/guides/webhooks（Webhook 指南）
- https://docs.waffo.ai/zh/api-reference/webhooks（事件验签与结构）
- https://docs.waffo.ai/zh/api-reference/endpoints/subscriptions/cancel-subscription（停止订阅）
- https://docs.waffo.ai/zh/guides/refunds（退款说明）
- https://docs.waffo.ai/zh/api-reference/payment-error-codes（错误码说明）

**⑦ 结算与迁移**
- https://docs.waffo.ai/zh/features/finance（资金与结算）
- https://docs.waffo.ai/zh/merchant/finance（商户资金账户）
- https://docs.waffo.ai/zh/merchant/payout-accounts（配置提款账户）
- https://docs.waffo.ai/zh/merchant/payout-flow（到账规则）
- https://docs.waffo.ai/zh/integrate/migrate（Stripe/Creem 迁移指南）

**⑧ AI 可读资料**
- https://docs.waffo.ai/llms.txt（官方索引）
- https://docs.waffo.ai/llms-full.txt（完整文档）

---


![](img/67c37faeb967b1478183a189236a069f_27_0.png)

![](img/67c37faeb967b1478183a189236a069f_27_1.png)
