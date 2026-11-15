# Creem 收款实操手册：一个新手是怎么把跨境收款接通的
做跨境工具和独立站的朋友，最在意的一件事大概就是“怎么把钱稳妥地收回来”。尤其是做数字商品，卖一次货款和按月扣费订阅，都必须依赖可靠的收款服务商，不然产品做得再好，流水进不来也是白搭。
我第一个尝试的是 Stripe。可是它要求开通境外银行卡，风控规则也很严厉，对没什么经验的人来说，动不动就遇到账户被限制的风险。PayPal 在海外电商场景里很常见，但它基本面向企业用户，个人开发者想申请并不容易。后来看到了 Creem，它标榜的三个点对我来说简直太合适了：对国内身份友好、结算能够直达支付宝、接入门槛很低。光是这三点，已经让我有动力去试试了。
最早知道 Creem 是从一篇介绍它接入方式的文章：<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_85e849c9c572ed7be48206c0d3f958ff.png>
那篇文章给出的信号是“二十分钟内完成”。在开户环节，这句话确实没错，但后续流程才是真正折磨人的地方。没有开发背景的我，在后续配置时彻底懵了，整整折腾了两周，才把整个流程弄通。三月底支付链路已经能正常工作，可惜这篇复盘拖到了五月中旬才收尾。今天就从我的实际体验出发，把每个关键动作都还原出来。
接下来分四个部分展开：
1. 开账户、过认证、绑定回款方式
2. 把测试和正式两套参数一起准备好
3. 搞定平台回调与本地隧道路由
4. 用 Cursor 写代码把全部参数串起来
## 一、账户开通与回款资料
### 1. 开户
在 Creem 官网选 Google 账户一键授权，或者用邮箱创建账号，进入后就是后台主页：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c66360fa20ca3c8fded1df28da9cd5c8.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b131c648d35ecb73fbec1b3f1a50eda8.png>
### 2. 设立回款账户
在 Balance 菜单的 Payout Account 区域，选择新增回款账户，国家选 China：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e38794ac2a89f803006834c513650afe.png>
### 3. 填写业务背景
把自己基本资料和业务类型录入详细，对方审核时需要参考：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_391524bba55d44e0b46c7bebef0353a4.png>
### 4. 身份核验
按页面指引上传大陆身份证正反面，然后打开电脑摄像头做一次人脸拍照。这些材料会统一记到 Sumsub ID 下：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c54ae08be31c74078c04d1f80e546368.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a4c576a831b61ff7e4a8b2e7f9d3ab06.png>
提交以后，可能看到的是等待人工复核的页面：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d59b5809fdc36f78cec241d9f8e47812.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_33d88964acf8f5f1801031ab44667dda.png>
不用着急，通常二十四小时内会收到结果邮件，也有人是立刻通过的：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_eb45ff5d3a55022ede5681b297b93738.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b769313d5c5ab2c8cc5eefd15d96f102.png>
### 5. 绑定支付宝
在 Payout Details 下进入 Manage Payout Account，把回款信息补齐。国家还是 China，币种 CNY，转账方式支付宝；再录入支付宝账号、邮箱地址和你的中文全名：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9cdde8b259401153407c2fca9e088a7c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_91d3be050bd1c2353d2450d60984f647.png>
最后补上家庭住址，如实填写即可。保存之后，身份认证和回款信息就都齐了：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f9976e17b67c7152ff28da55cb13f6a0.png>
### 6. 等候复核结果
进度快的话半天到一天就有消息：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_039aa4e2a8cc3e2ab172b13d52cfe780.png>
## 二、测试与生产环境：两套参数都不能少
要提醒所有新手：Creem 的 test mode 开关一旦打开，展示和使用的参数完全换了一套。当时我就是没注意到这个细节，和同伴在这里绕了很久。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e9a9574e12ceb972023dcf2c51a7a80c.png>
所以从下面的操作开始，每一步都要在对应模式下做两遍。
### 1. 新增商品
在 Product 菜单点击 add product 开始建一个：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_924afac9cd86e2e794d9712359d947d7.png>
#### 1.1 商品基本资料
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a691fd084e3f1ed719707535256318c3.png>
- name：商品名字
- return url：付款完成后应跳转的页面地址
- description：卖点说明（也可以交给 AI 代笔）
- status：记得选 active，商品才会正常售卖
- image preview：商品封面，非必填
#### 1.2 价格与收费类型
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e868b37f5a85d262a9d0f43256dbf63d.png>
- 计费模式：买断制（single payment）或者订阅制（subscription）
- currency：结算货币
- price：你想定多少钱
- tax category：数字商品一般选 “digital goods or service”
- tax behaviour：是否把税计入标价，按需处理
#### 1.3 补充素材
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_acb25ed2fdf8c8f79bf5ec481cdff039.png>
图片、特性说明和附加介绍，都能交给 AI 快速生成。全部填好以后点 create product。
#### 1.4 拿到商品标识
在商品列表右侧有三个点按钮，点开后即可复制该商品的 product id：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_24fb3cd676374ed19d2f8c3ca0f405ab.png>
### 2. 生成接口密钥
在右上角 developer 入口建立 API Key。测试环境和正式环境的 Key 是两回事，一定要各建一套：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_22e70cc2144918a03bd8e830cf6b2da7.png>
## 三、平台回调与本地隧道
### 3.1 先搞懂回调
回调（Webhook）就像是平台派出的信使，不要求你反复盯着后台问“有结果了吗”，而是主动跑过来说一声：这笔支付已经处理完了。
拿快递来打比方，一种是隔几分钟就打开物流 App 刷新一次状态，这是轮询；另一种是快递员到了楼下电话通知你，这就是 Webhook。
### 3.2 哪些情况下需要它
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3cc3751436867f1dba123bc2170bf7e4.png>
出现下面的场景，通常会考虑加装 Webhook：
1. 实时性要求高
- 买家一下单，商家马上收到提醒
- 博客有人留言，博主立刻看到通知
2. 业务要自动流转
- 付款成功后台自动发货
- 预约表格提交后自动回一封确认邮件
3. 多系统同步
- 代码仓库一更新就触发线上部署
- 订单系统与库存系统时刻畅通
如果这些都不是你的业务重点，那暂时不配也无妨。
### 3.3 创建 Webhook
还记得刚才那个 developer 页面吗？API Key 旁边就有 webhooks 入口：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f6eae7c2a25c4437edd16289fa9a4fd9.png>
点 add webhook 后只涉及两个必填项：
- webhook name：给这个信使取个名字，说明它的用途
- webhook url：Creem 通知送达的具体接口地址
### 3.4 正式环境：回调地址怎么定
让 Cursor 帮你定位负责接收通知的路由，然后使用“域名 + 路由”拼出完整地址即可：
```
www.XXXX.com/payment/result
```
### 3.5 沙箱模式：为什么还要借助隧道
照理说，测试环境也可以把地址填成上面那样：
```
http://localhost:3000/payment/result
```
可实际上，Creem 并不接收本机回环地址。你需要一个公网 URL 来接收通知，这时候就得用 ngrok 这个工具，把本地开发端口变成一个临时公网入口：
```
https://8733-191-204-177-89.sa.ngrok.io/payment/result
```
### 3.6 保存回调参数
Webhook 建好以后，会得到一组回调专属 URL：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a61279eee9f1d9d7523a7522de2f2c7c.png>
再往下翻，把它的 secret 也一并复制下来：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3df020153856a9d7217038d08a5f9bf8.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3b0dab96944ea88cac5af9251b10c690.png>
### 3.7 ngrok 操作全流程
#### 3.7.1 获取 Token
ngrok 也支持 Google 快速授权。登录以后进入菜单里的 “your authtoken”，把个人令牌复制出来：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8df2ea4dff4c75e93c40ced08ffbac2b.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d829824ad6c4d0535acc0238896b82ff.png>
#### 3.7.2 安装与绑定
直接到官网下载对应芯片的安装包：
```
brew install ngrok
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_03f15c4d730c03272a1b3f24421a7dc5.png>
或者在终端运行官方提供的命令行，把 authtoken 写入本机配置：
```
ngrok config add-authtoken 你的token
```
#### 3.7.3 跑起来
先把本地项目服务正常启动：
```
npm start
```
然后启动 ngrok，默认开在 3000 端口；如果你改过端口，记得一并调整：
```
ngrok http 3000
```
成功后会看到类似下面的输出，里面那条以 https 开头的地址就是公网地址：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b8a3b174de83b8f9246ab5422a1e15c3.png>
接着把你自己的业务路径附上去，例如：
```
localhost:3000/payment/result
```
所以最终的 Public URL 是：
```
https://08f7-115-196-182-99.ngrok-free.app/payment/result
```
### 3.8 免费版注意事项
ngrok 免费版本的公网地址不固定，每次运行都会重新分配一个。一旦你关了终端，下次启动就会拿到新地址，请务必回到 Creem 后台，把对应模式的回调地址同步修正。
## 四、全部串起来，完成联调
### 4.1 最后清点
走完上面流程，你应该已经拿到这么几项内容：
环境变量文件
```
CREEM_API_KEY=
CREEM_PRODUCT_ID=
CREEM_API_URL=https://api.creem.io
CREEM_SUCCESS_URL=
```
接口密钥
```
CREEM_API_KEY=
CREEM_API_KEY_TEST=
```
商品标识
```
CREEM_PRODUCT_ID=
CREEM_PRODUCT_ID_TEST=
```
API 地址
```
CREEM_API_URL=https://api.creem.io
CREEM_API_URL_TEST=https://test-api.creem.io
```
回调参数
```
CREEM_WEBHOOK_URL_test=
CREEM_WEBHOOK_URL=
CREEM_WEBHOOK_secret_test=
CREEM_WEBHOOK_secret=
```
支付完成后的回跳路由
```
CREEM_SUCCESS_URL=
CREEM_SUCCESS_URL_TEST=
```
### 4.2 让 Cursor 帮你写代码
#### 4.2.1 逻辑到底是什么
我尝试过让 AI 画流程图，结果画面复杂到更像一张电路图。其实把各方角色拆开看，流程并不难理解：
- 买家所见的表面流程：点击购买 → 进入收银台 → 付款成功 → 回到站点 / 触发权益到账
- 系统内部的实际流程：后端请求 Creem 的结算接口 → Creem 返回支付链接 → 后端把链接交给买家 → 买家完成付款 → Creem 回调通知后端 → 后端核验并更新订单状态
支付模式也就是买断和订阅两种。下面就以买断来代码演示。
#### 4.2.2 买断制接入要点
核心方法论可以压缩为一句话：把配置信息、官方文档和预计达成的效果交给 Cursor，让它替你完成代码。
“配置信息”已经备齐，“接口文档”也在手边，剩下就是明确“期望效果”。
这里先定一下目标：
⚠️ 当前案例不涉及账号注册/登录，因此不复杂。即便后续要增加登录体系，也可以直接用第三方身份服务，不用过分担心。
这个环节需要关注 `success_url` 和签名核验两个参数，官方的说明如下：
1. 每个 checkout_session 都允许自定义 success_url，它会覆盖商品默认设置的回跳地址。这样便能在每一次付款后按需把买家带到指定落地页。
2. 支付完成后的回跳和重定向 URL 中带有 Creem 签名的关键信息，利用它可以核验支付和买家身份。
一句话总结：付款后重定向、附带签名、用于验证。
买断制支付需要依次访问 3 个接口：创建 checkout → 生成签名 → 校验签名。
##### 接口一：创建结算会话
```
const redirectUrl = await axios.post(
`https://api.creem.io/v1/checkouts`,
{
"success_url": "https://example.com",
"product_id": "prod_your-product-id",
},
{
headers: { "x-api-key": `creem_123456789` },
},
);
```
请求看起来很长，实际上只关心四个地方：
1. `https://api.creem.io/v1/checkouts`：固定的结算接口，测试与生产各一套
2. `"success_url": "https://example.com"`：付款成功后的跳转地址
3. `"product_id": "prod_your-product-id"`：传入你自己的商品标识
4. `"x-api-key": "creem_123456789"`：改成你的 API Key，注意区分环境
最后附上我本地的 env 配置：
```
import axios from 'axios';
export interface CreateCheckoutParams {
productId: string;
requestId?: string;
successUrl?: string;
}
export interface CreateCheckoutResponse {
checkout_url: string;
[key: string]: any;
}
/**
* 创建Creem结账会话
* @param params 结账参数
* @returns 包含结账URL的响应
*/
export async function createCheckout(params: CreateCheckoutParams): Promise {
try {
const API_URL = process.env.CREEM_API_URL || 'https://test-api.creem.io';
const API_KEY = process.env.CREEM_API_KEY || 'creem_test_3sioDtbY5ADbmoODbQnNiW';
// 获取格式化的API基础URL（确保没有尾部斜杠）
const baseUrl = API_URL.endsWith('/') ? API_URL.slice(0, -1) : API_URL;
const apiUrl = `${baseUrl}/v1/checkouts`;
const response = await axios.post(
apiUrl,
{
product_id: params.productId,
request_id: params.requestId,
success_url: params.successUrl,
},
{
headers: { 'x-api-key': API_KEY },
}
);
if (!response.data || !response.data.checkout_url) {
throw new Error('API response does not contain checkout_url');
}
return response.data;
} catch (error) {
console.error('Error creating checkout session:', error);
if (axios.isAxiosError(error) && error.response) {
console.error('API error response:', error.response.data);
}
throw error;
}
}
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1d5835f203e6bcace0c2a79f86e242e6.png>
（这段解读来自GPT，你甚至可以复制给任意AI，看看它眼中的你到底是什么样子）
### API2：生成签名（signature）
```
import crypto from 'crypto';
/**
* 生成Creem签名
* @param params 参数对象
* @param apiKey API密钥
* @returns 生成的签名
*/
export function generateSignature(params: Record, apiKey: string): string {
// 创建格式为 "key1=value1|key2=value2|...|salt=apiKey" 的数据字符串
// 重要：不要对键进行排序 - 按照提供的顺序使用
const data = Object.entries(params)
.map(([key, value]) => `${key}=${value}`)
.concat(`salt=${apiKey}`)
.join('|');
// 使用SHA-256哈希算法生成签名
const hash = crypto.createHash('sha256').update(data).digest('hex');
return hash;
}
```
### API3：校验签名（signature）
```
import { generateSignature } from './signatureUtils';
export interface RedirectParams {
request_id?: string | null;
checkout_id?: string | null;
order_id?: string | null;
customer_id?: string | null;
subscription_id?: string | null;
product_id?: string | null;
}
/**
* 验证Creem签名
* @param params 重定向参数
* @param signature 要验证的签名
* @returns 签名是否有效
*/
export function verifySignature(params: Record, signature: string): boolean {
try {
const API_KEY = process.env.CREEM_API_KEY || 'creem_test_3sioDtbY5ADbmoODbQnNiW';
// 过滤掉null/undefined值，并移除signature参数（如果存在）
const filteredParams: Record <string string="">= {};
Object.entries(params).forEach(([key, value]) => {
if (value !== null && value !== undefined && key !== 'signature') {
filteredParams[key] = value;
}
});
// 使用Creem提供的方法生成签名
const computedSignature = generateSignature(filteredParams, API_KEY);
// 比较计算的签名与接收到的签名
return computedSignature === signature;
} catch (error) {
console.error('Error verifying signature:', error);
return false;
}
}</string>
```
## 支付测试环节
### 3.1 先用测试模式跑一遍
进入测试环境时，直接使用提供的测试信用卡即可。
卡号：```
4242 4242 4242 4242
```
其余信息无需纠结，随便填都能通过。
### 3.2 切换真实支付前，请务必看完（血泪教训，40美元就这么没了）
当你把测试环境全部跑通，准备切到生产环境来一笔真实交易验证时，下面三件事一定要记牢，否则钱包真的会抗议！
#### 💶那1000元，其实是欧元不是美元！
注意看，那个1000的货币单位，不是USD，而是EUR！我和彩笺当初都没看出来，傻乎乎地在商品设置里选了美元，自己给自己付了一笔9.9美元，结果发现被扣了手续费。再回去仔细一看，那个符号越看越不对劲——这分明是欧元啊！
#### 🎫Discount 折扣：菜单里的大彩蛋
在菜单页面，有一个非常显眼的discount选项，点进去就能自己创建优惠券，最高支持100%折扣，也就是完全免费！
没错，完全免费！
我之前傻傻地给自己刷了5笔9.9美元测试费，直到大哥提醒，才发现这么个神操作。起初我还只敢设个90%，结果大哥自己测试时直接拉满100%（我直接愣住）。更爽的是，设置好折扣码后，支付时连银行卡都不用填，只要输入这个discount的code，页面直接显示FREE！
#### 💰Refund 退款：那个隐藏在角落里的按钮
也是在大哥的提醒下，我随手点进了我的payment页面，心里想着：能不能把之前测试扣的钱退回来？结果还真让我找到了！点开订单最右侧的三个点，里面赫然躺着一个"refund"按钮，点了之后2分钟内退款到账。
（但如果是刚支付完立刻退款，银行那边可能还没入账。比如我写这篇文章的时候，几天前那4笔9.9美元到现在还没退回。）
## 五、实操演示走一遍
说明：这里的实战只聚焦怎么把支付API接进来，"登录"、"数据库"这些部分不在本次范围（后面我准备单独写一篇关于支付接入的文章）。
### 5.1 最终效果长什么样
点击支付按钮 → 触发支付流程 → 完成支付 → 跳转到指定的成功页面 → 进Creem后台确认收款。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7523576f3c2520ea0c2180ce17571a46.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_df5e331647922ae17672b09fd361b37c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8809e1d1ed3278ea41b8a669f48efa8a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c94f7c9236caa2f8ae6e5312fd789e7d.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6e8d99e3ec339e94d604e491d3c1f009.png>
### 5.2 代码文件结构一览
为了少消耗cursor的次数，我这次选择用augment来做演示（还没用过augment的朋友，可以看我之前写的那篇augment介绍，现在入手还能薅羊毛，越早用越划算）！
```
支付流程
├── 1\. 用户点击支付按钮 (app/page.tsx)
│   └── 生成唯一requestId
│
├── 2\. 前端调用API (app/api/create-checkout/route.ts)
│   └── 调用createCheckout服务
│       └── services/creem/createCheckout.ts
│           ├── 使用环境变量获取API配置
│           ├── 调用Creem API创建结账会话
│           └── 返回checkout_url
│
├── 3\. 用户被重定向到Creem支付页面
│
├── 4\. 支付完成后，Creem重定向回success页面
│   ├── URL包含支付结果参数和签名
│   └── app/success/page.tsx (服务端组件)
│       └── app/success/client.tsx (客户端包装器)
│           └── components/SuccessContent.tsx
│               ├── 从URL获取参数
│               ├── 调用verifySignature验证签名
│               │   └── services/creem/verifySignature.ts
│               │       ├── 过滤参数
│               │       └── 调用generateSignature生成签名
│               │           └── services/creem/signatureUtils.ts
│               │               ├── 按照Creem规则格式化参数
│               │               ├── 添加API密钥作为salt
│               │               └── 使用SHA-256生成哈希
│               └── 根据验证结果显示成功或失败页面
```
### 各文件的职责说明
1.  signatureUtils.ts：
*   主要作用：按照Creem规范生成签名。
*   工作逻辑：把参数按`key1=value1|key2=value2|...|salt=apiKey`拼接起来，再用SHA-256哈希算法算出签名。
*   被verifySignature.ts调用来完成签名校验。
2.  verifySignature.ts：
*   主要作用：校验Creem重定向回来的URL里带的签名。
*   工作逻辑：先过滤掉signature参数，然后调用generateSignature重新生成签名，再和URL中的签名做比对。
*   被SuccessContent.tsx组件调用，用来确认支付结果是不是真的成功。
3.  createCheckout.ts：
*   主要作用：调用Creem API来创建结账会话。
*   工作逻辑：使用axios向Creem API发送POST请求，拿到包含checkout_url的响应。
*   被app/api/create-checkout/route.ts调用。
4.  app/api/create-checkout/route.ts：
*   主要作用：处理后端的支付请求。
*   工作逻辑：接收前端请求，校验参数，调用createCheckout服务，然后返回结果。
*   被app/page.tsx里的支付按钮点击事件触发调用。
### 5.3 和AI协作的过程
```
我需要接入creem，在service下面，帮我封装creem的api接口，api一共有3个，分别是 “createCheckout”、“signatureUtils”、“verifySignature”
关于这三个的参考文件我已经放到readme里面，你可以参考学习，环境变量我已经准备好了
代码写完以后 请测试最后的验证signature，成功以后处理首页按钮的调用
```
把md文件写好，丢给AI，它就开始自动干活了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4109520b2afebecabeed0a23c3537c65.png>
如果遇到 verify 失败的情况，就像下面这样：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_866988c9178a08895a91dfef7502ee2d.png>
这时候就让AI去对比verify代码和参考代码的差异，严格要求它按参考代码来修正：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_eae5d4856dfc42ca1b451ad87d23e0a5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a3511b062aa1949ff9235e4aac4b19db.png>
## 六、碎碎念
一开始不懂，实在太正常了。不懂就硬着头皮上！崩溃个100次之后，自然就进入下一个阶段了。
支付和登录，真的就像两座大山压在面前。这篇内容其实3月底就已经写好了，一直想补一个实操演练，结果拖到了现在。面对这个一直让自己发怵的东西，终于把支付怎么接、api和service之间到底是什么关系，一点一点啃明白了。似懂非懂等于不懂，只有完全搞懂、彻底掌握，才算真正翻过了这座山。借老师的一句话：今天，我终于把这颗"支付"的珠子给丢掉了！
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f48edbed8b0d68a92b4e0790848910d9.png>
希望这篇能帮到每一个正在捣鼓支付接入的你。如果成功接上了，欢迎回来留个言告诉我喔！