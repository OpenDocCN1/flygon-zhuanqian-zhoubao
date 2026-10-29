# Creem 收款接入指南：从注册审核到支付上线，一次讲清楚

做独立站、SaaS 或数字产品出海，流量和产品只是前半程，真正让业务闭环的，是如何把海外用户支付的美元安全、顺畅地收回来。

如果选择 Stripe，通常要面对海外银行卡、严格风控等问题；PayPal 虽然在电商领域使用广泛，但个人开发者往往会被公司主体要求卡住。Creem 的吸引力在于：面向国内开发者相对友好，提现可以走支付宝，而且接入门槛没有想象中高。

听上去很理想，但“注册完成”和“真正跑通”完全是两回事。

我最初是在一篇海外收款平台注册文章中了解到 Creem 的：

![](img/85e849c9c572ed7be48206c0d3f958ff.png)

文章里说，整个流程大约二十分钟。我实际体验下来，注册和初审确实很快，真正耗时间的是后续配置。作为零基础用户，我前后折腾了两周，三月底完成了大部分支付接入，直到五月中旬才算彻底跑通。

因此，这篇内容不只讲后台按钮怎么点，也会把容易踩坑的地方一起说明白。

全文分为四个阶段：

1. 创建 Creem 用户并完成收款资料
2. 分别准备开发环境与线上环境的参数
3. 按需配置 Webhook 和 ngrok
4. 将支付流程接入网站

---

# 一、先完成注册与收款资料

## 1. 创建账户

进入 Creem 后，可以使用 Google 账户登录，也可以通过邮箱注册。完成后会进入后台首页：

![](img/c66360fa20ca3c8fded1df28da9cd5c8.png)

![](img/b131c648d35ecb73fbec1b3f1a50eda8.png)

## 2. 设置提现账户

### 2.1 新增收款档案

打开 **Balance → Payout Account**，新建一个提现账户，地区选择 **China**。

![](img/e38794ac2a89f803006834c513650afe.png)

### 2.2 填写业务背景

平台会要求你说明个人基本情况，以及当前销售的产品或服务内容。

![](img/391524bba55d44e0b46c7bebef0353a4.png)

建议按照真实业务填写，产品描述不必写得过于复杂，重点让审核人员看懂你提供的是什么。

### 2.3 完成身份认证

按照页面提示提交大陆身份证正反面，并使用电脑摄像头完成拍摄。认证资料最终会归档到 Sumsub 的身份验证系统中。

![](img/c54ae08be31c74078c04d1f80e546368.png)

![](img/a4c576a831b61ff7e4a8b2e7f9d3ab06.png)

提交后可能会出现等待审核的页面：

![](img/d59b5809fdc36f78cec241d9f8e47812.png)

![](img/33d88964acf8f5f1801031ab44667dda.png)

这一步不用重复提交，也不要频繁修改资料，耐心等待即可。通常约一天左右会收到邮件结果，也有人能够直接通过：

![](img/eb45ff5d3a55022ede5681b297b93738.png)

![](img/b769313d5c5ab2c8cc5eefd15d96f102.png)

### 2.4 补充提现方式

进入 **Payout Details → Manage Payout Account**，继续设置到账信息。

![](img/9cdde8b259401153407c2fca9e088a7c.png)

具体填写方式如下：

- 地区：China
- 结算货币：CNY
- 收款渠道：Alipay
- 支付宝账户：填写实际收款账号
- 邮箱：填写常用邮箱
- 姓名：填写真实中文姓名

![](img/91d3be050bd1c2353d2450d60984f647.png)

家庭住址按照实际情况填写即可。保存后，身份资料和提现资料就基本完整了。

![](img/f9976e17b67c7152ff28da55cb13f6a0.png)

### 2.5 等待最终结果

最后只需等待平台审核。顺利的话，几个小时到一天左右就会有结果。

![](img/039aa4e2a8cc3e2ab172b13d52cfe780.png)

---

# 二、开发环境和线上环境必须分别配置

这里是非常容易忽略的一点：Creem 的测试状态与正式状态并不是共用配置。

也就是说，以下内容都要分别准备两份：

- 测试环境
- 正式环境

产品、密钥、Webhook 等资料，只要处于不同模式，就不能混用。

![](img/e9a9574e12ceb972023dcf2c51a7a80c.png)

## 1. 新建产品

进入 **Product → Add Product**，开始创建商品。

![](img/924afac9cd86e2e794d9712359d947d7.png)

### 1.1 基础资料

![](img/a691fd084e3f1ed719707535256318c3.png)

页面中常见字段可以这样理解：

- **Name**：商品名称
- **Return URL**：付款结束后返回的地址
- **Description**：商品或服务说明
- **Status**：选择 active，使商品处于可用状态
- **Image Preview**：商品封面，可按需上传

### 1.2 付款参数

![](img/e868b37f5a85d262a9d0f43256dbf63d.png)

这里主要设置：

- 计费类型：单次购买或周期订阅
- 结算币种
- 商品金额
- 税务类别：数字商品或数字服务通常选择对应的虚拟产品分类
- 税费规则：根据你的业务和定价方式决定是否含税

### 1.3 补充展示内容

![](img/acb25ed2fdf8c8f79bf5ec481cdff039.png)

商品图片、功能亮点和补充说明都可以继续填写。文案部分可以先让 AI 协助生成，再根据实际产品调整。

确认无误后，点击 **Create Product**。

### 1.4 保存商品编号

回到产品列表，找到刚刚建立的商品，打开右侧操作菜单，复制对应的商品 ID。

![](img/24fb3cd676374ed19d2f8c3ca0f405ab.png)

后面创建付款会话时会用到它，建议及时保存。

## 2. 生成访问密钥

![](img/22e70cc2144918a03bd8e830cf6b2da7.png)

打开右上角的 **Developer** 页面，创建 API Key。

测试状态和正式状态要分别生成密钥，不能拿其中一组去调用另一套环境。

---

# 三、Webhook 与 ngrok：不是人人都要配置

## 1. Webhook 到底做什么

Webhook 可以理解为“事件发生后，平台主动向你的服务器发消息”。

举个简单例子：

- 轮询：你隔几分钟主动打开物流软件查询一次
- Webhook：快递状态变化后，系统主动通知你

支付场景中，它常用于告诉网站：“某笔订单已经完成付款”。

## 2. 哪些场景值得使用

![](img/3cc3751436867f1dba123bc2170bf7e4.png)

如果你有以下需求，就应该考虑接入 Webhook：

### 需要即时提醒

- 新订单产生后通知管理员
- 用户留言后马上触发提醒

### 需要自动执行任务

- 付款完成后自动发放内容
- 表单提交后自动发送确认邮件

### 需要多个系统协同

- 代码仓库更新后自动部署
- 订单状态变化时同步库存

如果网站只需要在付款后跳转到一个结果页面，并没有发货、积分、订单同步等后续动作，那么可以暂时不接 Webhook。

## 3. 在 Creem 中建立 Webhook

创建访问密钥的页面附近，就能看到 Webhooks 入口：

![](img/f6eae7c2a25c4437edd16289fa9a4fd9.png)

点击新增按钮后，主要填写以下两项：

- **Webhook Name**：用于标记这条通知规则
- **Webhook URL**：Creem 发送支付事件的目标地址

### 3.1 正式环境

正式环境可以填写线上网站的域名，再拼接负责接收事件的接口地址。这个接口具体叫什么，可以让 Cursor 根据你的项目结构判断。

```
www.XXXX.com/payment/result
```

### 3.2 测试环境

```
http://localhost:3000/payment/result
```

测试时，如果接口只运行在本机，Creem 无法访问 `localhost`。平台要求目标地址能够从公网访问，因此需要借助 ngrok 把本地服务临时映射出去。

映射完成后，本地接口会获得一个公开访问地址：

```
https://8733-191-204-177-89.sa.ngrok.io/payment/result
```

### 3.3 保存 Webhook 地址

完成创建后，复制后台生成的 Webhook 地址备用。

![](img/a61279eee9f1d9d7523a7522de2f2c7c.png)

### 3.4 保存密钥

随后找到该 Webhook 对应的 Secret，并一并记录。

![](img/3df020153856a9d7217038d08a5f9bf8.png)

![](img/3b0dab96944ea88cac5af9251b10c690.png)

这个 Secret 后续用于校验平台推送的事件是否可信。

---

## 4. 用 ngrok 暴露本地服务

ngrok 的作用，是给本机开发服务临时分配一个公网入口，方便第三方平台访问你的本地接口。

### 4.1 创建 ngrok 账户

打开 ngrok 官网，可以使用 Google 登录。进入菜单中的 **Your Authtoken**，复制账户令牌。

![](img/8df2ea4dff4c75e93c40ced08ffbac2b.png)

![](img/d829824ad6c4d0535acc0238896b82ff.png)

### 4.2 安装程序

#### 4.2.1 获取客户端

```
brew install ngrok
```

也可以点击下载入口，根据电脑处理器选择对应版本。

![](img/03f15c4d730c03272a1b3f24421a7dc5.png)

#### 4.2.2 写入授权令牌

安装完成后，在终端执行页面提供的授权命令，把刚才复制的 token 写入本机。

```
ngrok config add-authtoken 你的token
```

### 4.3 启动映射

先启动你的网站开发服务：

```
npm start
```

然后启动 ngrok。很多项目默认使用 3000 端口，如果你的项目监听的是其他端口，就替换成实际端口号。

```
ngrok http 3000
```

命令执行成功后，终端会显示一个公网地址，它对应的就是本机服务入口。

![](img/b8a3b174de83b8f9246ab5422a1e15c3.png)

如果你的接口并不在根目录，还要在域名后继续拼上实际接口路径：

```
localhost:3000/payment/result
```

最终提交到 Creem 的，就是完整的公网接口地址：

```
https://08f7-115-196-182-99.ngrok-free.app/payment/result
```

### 4.4 使用免费版时要留意

ngrok 免费方案通常会在每次重新启动时分配新的随机域名。

因此，关闭终端后再次运行，之前保存的地址很可能已经失效。重新启动后，需要回到 Creem 对应的测试或正式模式，更新 Webhook 地址。

---

# 四、开始接入网站付款

## 1. 上线前先整理参数

完成前面的准备后，建议把关键值集中放进项目的环境变量中：

```
CREEM_API_KEY=
CREEM_PRODUCT_ID=
CREEM_API_URL=https://api.creem.io
CREEM_SUCCESS_URL=
```

通常需要准备：

### 访问密钥

```
CREEM_API_KEY=
CREEM_API_KEY_TEST=
```

### 商品编号

```
CREEM_PRODUCT_ID=
CREEM_PRODUCT_ID_TEST=
```

### API 服务地址

```
CREEM_API_URL=https://api.creem.io
CREEM_API_URL_TEST=https://test-api.creem.io
```

### Webhook 配置

```
CREEM_WEBHOOK_URL_test=
CREEM_WEBHOOK_URL=
CREEM_WEBHOOK_secret_test=
CREEM_WEBHOOK_secret=
```

### 付款成功后的落地页

```
CREEM_SUCCESS_URL=
CREEM_SUCCESS_URL_TEST=
```

测试模式和正式模式的值要分开管理，避免测试订单误用线上密钥，或者线上请求误打到测试商品。

## 2. 让 Cursor 协助完成代码接入

### 2.1 先理解完整链路

从访客角度看，流程很简单：

1. 点击购买
2. 进入收银页面
3. 填写付款信息
4. 完成支付
5. 回到结果页，或获得对应权益

但网站后台实际上会经历另一条链路：

1. 后端向 Creem 发起创建付款请求
2. Creem 返回一个结账地址
3. 后端把该地址交给前端
4. 用户完成付款
5. Creem 产生支付事件
6. 平台将事件推送给网站
7. 网站根据结果更新订单或发放权益

付款模式主要分为单次购买和订阅。下面先以单次商品为例。

配置规则文档直达

### 2.2 单次购买与 Return URL

向 Cursor 描述需求时，最好同时提供三类内容：

- 当前项目已经准备好的参数
- Creem 官方要求的调用规则
- 你希望用户完成付款后看到的结果

本例不涉及用户注册和登录，所以实现相对直接。后续即使要加入账户体系，也可以结合第三方登录服务完成。

这里有两个重点：

- 通过 `success_url` 指定支付完成后的落地位置
- 通过签名校验确认回传数据没有被篡改

官方规则可以概括为：

1. 每次创建 checkout session 时，都可以传入自己的 `success_url`，它能够覆盖商品默认设置的返回地址。这样，不同用户或不同订单可以进入不同页面。
2. 支付完成后的返回地址中会带有 Creem 生成的签名信息，网站可以利用这些字段判断付款信息及用户信息是否可信。

对于单次购买，通常需要完成三件事：

1. 创建 checkout
2. 生成签名
3. 校验签名

#### API 1：创建付款会话

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

这段请求看起来内容不少，但真正要替换的核心值主要有四项：

1. `https://api.creem.io/v1/checkouts`  
   Creem 的 checkout 接口地址。测试与正式环境使用不同的服务地址。

2. `"success_url": "https://example.com"`  
   用户付款完成后要前往的页面地址，换成你项目中的真实页面。

3. `"product_id": "prod_your-product-id"`  
   替换为前面保存的商品编号。

4. `"x-api-key": "creem_123456789"`  
   替换为当前环境对应的访问密钥。

我的文件如下：

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

![](img/1d5835f203e6bcace0c2a79f86e242e6.png)

（下面这段是GPT对接口的解读，你也可以原样丢给任何AI，让它告诉你这到底在讲什么）

#### API2：如何生成 signature

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

#### API3：如何校验 signature

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

### 3.1 先跑通测试支付

做测试支付的时候，直接用测试信用卡就行。

卡号

```
4242 4242 4242 4242
```

其余字段随便填，没有硬性要求。

### 3.2 正式扣款前必读（血泪教训，40 刀就这么没了）

前面所有步骤都走完、测试模式也顺利通过之后，你大概准备去生产环境验证真实支付了。动手之前，下面这几件事务必先做，否则钱包真的会疼！

#### 💶 所谓“1000 元免手续费”，单位其实是欧元

这个 1000 的货币单位是欧元，不是美元。我和彩笺都栽在这儿：产品一开始按美元配置，自己给自己付了 9.9，结果发现被扣了手续费。后来再细看，越看越不对——那个符号分明就是欧元符号！

#### 🎫 Discount 折扣券

菜单页里有个很显眼的 discount 按钮，可以自己建优惠券，折扣最高能设到 100%，也就是完全免费。

完全免费！

林悦己前后给自己的支付测试充了 5 次 9.9 美元，后来经大哥提醒才发现并用上这个功能。起初我只敢设 90%，结果大哥自己测试时直接拉到 100%（我：？）。

有了折扣券，付款时连银行卡信息都不用填，只要输入 discount code，页面就会显示 FREE！

#### 💰 Refund 退款

还是大哥提醒的，我顺手点进了 payment 页面，想着能不能退款，还真找到了：点开 order 最右边那三个点，里面有个“refund”按钮，两分钟内就能完成退款。

（如果是刚支付、信用卡还没入账的情况——写这篇帖子时，我有 4 笔 9.9 是几天前付的，还没退回来。）

# 五、实战操作演示

前提：这次实战只聚焦“怎么接支付 API”，“登录”“数据库”这些部分不展开（后面我打算另写一篇专门讲接支付）。

## 5.1 最终效果

点按钮 → 触发支付 → 支付完成 → 跳回指定成功页 → 去 creem 后台确认钱是否到账。

![](img/7523576f3c2520ea0c2180ce17571a46.png)

![](img/df5e331647922ae17672b09fd361b37c.png)

![](img/8809e1d1ed3278ea41b8a669f48efa8a.png)

![](img/c94f7c9236caa2f8ae6e5312fd789e7d.png)

![](img/6e8d99e3ec339e94d604e491d3c1f009.png)

## 5.2 代码结构

为了省着点用 cursor 的次数，演示我用 augment 来做（还没上车 augment 的朋友可以翻我之前那篇，现在还能薅羊毛，越早越好）！

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

### 各文件职责拆解

1.  signatureUtils.ts：

*   核心职责：产出符合 Creem 规范的签名

*   实现方式：把参数拼成 key1=value1|key2=value2|...|salt=apiKey 的形式，再用 SHA-256 哈希算出签名

*   由 verifySignature.ts 调用，用于校验签名

1.  verifySignature.ts：

*   核心职责：校验 Creem 重定向回来的 URL 里的签名

*   实现方式：过滤参数、剔除 signature 参数，调用 generateSignature 生成签名，再跟 URL 里的签名做比对

*   由 SuccessContent.tsx 组件调用，用来确认支付结果

1.  createCheckout.ts：

*   核心职责：调用 Creem API 创建结账会话

*   实现方式：用 axios 向 Creem API 发 POST 请求，返回带 checkout_url 的响应

*   由 app/api/create-checkout/route.ts 调用

1.  app/api/create-checkout/route.ts：

*   核心职责：处理前端发来的支付请求

*   实现方式：接收请求、校验参数、调用 createCheckout 服务，最后把结果返回

*   由 app/page.tsx 里支付按钮的点击事件触发

## 5.3 和 AI 协作的经过

```
我需要接入creem，在service下面，帮我封装creem的api接口，api一共有3个，分别是 “createCheckout”、“signatureUtils”、“verifySignature”
关于这三个的参考文件我已经放到readme里面，你可以参考学习，环境变量我已经准备好了
代码写完以后 请测试最后的验证signature，成功以后处理首页按钮的调用
```

先把 md 文件写好，发出 prompt，它就开始自己干活了。

![](img/4109520b2afebecabeed0a23c3537c65.png)

如果你遇到 verify 失败，也就是下面这种情况——

![](img/866988c9178a08895a91dfef7502ee2d.png)

那就让 AI 对比一下 verify 代码和参考代码的差异，严格照着参考代码改：

![](img/eae5d4856dfc42ca1b451ad87d23e0a5.png)

![](img/a3511b062aa1949ff9235e4aac4b19db.png)

# 六、一点碎碎念

一开始搞不懂太正常了，不懂就硬着头皮上！崩溃一百次之后，自然就进入下一个阶段了。

支付和登录确实是两座吓人的大山。这篇内容其实三月底就写好了，一直想补个实操演练，结果拖到了现在。

面对自己发怵的东西，把支付到底怎么接、api 和 service 之间是什么关系彻底弄明白——似懂非懂等于不懂，只有完全懂、完全明白、完全掌握，才算真正翻过这座山。借用老师那句话：今天，我终于把支付这颗珠子给扔掉了！

![](img/f48edbed8b0d68a92b4e0790848910d9.png)

希望这篇内容能帮到正在接支付的你。如果接入成功，欢迎回来留言！