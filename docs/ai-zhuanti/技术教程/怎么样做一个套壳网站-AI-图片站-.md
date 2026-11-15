# 怎么样做一个套壳网站（AI 图片站）
今天咱们聊个挺有意思的事：AI图片站到底是怎么做出来的？很多人以为这背后技术门槛高，其实说白了，大部分AI绘画网站都是“套壳”——核心是把别人训练好的AI模型接口拿来用，再套个网页方便用户输入提示词。这篇文章就从零带你撸一个AI图片网站，哪怕你编程基础不深，照着一步步来也能跑通。
先认识一个利器：Replicate。它相当于一个“AI模型超市”，市面上很多开源模型（比如画图、写文本、生成视频和音乐）都已经被人部署好了，普通用户直接在网页上就能试玩，有些项目连登录都不用，免费就能体验。更棒的是，这些模型全都开放了API接口，你可以把它们接到自己的应用里。官方地址：https://replicate.com/
## 开工前要准备什么
**第一，GitHub账号。** Replicate的登录是走GitHub授权的，所以你肯定得先有一个GitHub账号。![](img/zhuanqian_488cdb243b033fe91d3e1e8bbdc98069.png) 有了账号后，输入用户名密码登录，或者提前登录好GitHub再授权Replicate也能进。![](img/zhuanqian_fb915e1308de7277ef21888c48a209db.png)
**第二，绑定支付方式。** 点右上角头像，进入“Account settings”，然后在“Billing”菜单里找到“Manage billing”。![](img/zhuanqian_e65711705e0fec11d48d79cdaf034872.png)![](img/zhuanqian_2c9c860968bb7a686e769d7bf56062e0.png) 添加信用卡时，卡号栏会提示支持的卡种。我用的是国内银行的Visa卡，可以正常添加。![](img/zhuanqian_a12e5b3ccfa4337e3f42c00c490ee92b.png) 为什么一开始就要绑卡？因为Replicate上的模型调用都是要花钱的，没绑定支付方式，接口就会调用失败。怕花超的话，可以在账单设置页面设定调用限额，以后按需调整就行。![](img/zhuanqian_9bd3450a785a7dd208cc249adf272863.png)
**第三，安装Node.js。** 下载地址：https://nodejs.org/zh-cn/download 下载完就是一路“下一步”的傻瓜安装，不会的话随手问问AI也能搞定。装好后，在命令行敲 `node -v`，能看到版本号就说明安装成功了。![](img/zhuanqian_e9013316d69ef018c5d6504a7950be71.png)
## 先快速见效：纯后端调用API
咱们先不着急做网站，先在本地感受一下怎么通过API生成一张AI图片。
**第一步，一行命令初始化项目。** 有个npm包叫 `create-replicate`，执行它后会自动帮你创建一个项目目录，并写入初始代码。```
npx create-replicate
``` 你先建好一个文件夹，进入该文件夹并打开命令行，执行这条命令。![](img/zhuanqian_1128c3e792db0f27f5abd568974a9a52.png) 命令跑起来后，它会要求你粘贴Replicate API token。你直接敲回车，它会自动打开浏览器，带你去获取token的界面。![](img/zhuanqian_f8c8b019e28b64366d1f50506c41ca22.png) 在页面上随意给token取个名字，点“Create token”。![](img/zhuanqian_54c7a561131806715cd03f8f9ac86d92.png) 然后把新生成的token复制回到命令行粘贴上。![](img/zhuanqian_e34a20db247c41683d6670c15424301a.png) 看到“初始化完成”提示后，你的目录下就多了一些项目文件。![](img/zhuanqian_41d008c94a7ab8d8e68b906605069b1f.png)![](img/zhuanqian_5388c2a685082f79cd8397b46f88bb13.png)
**第二步，用编辑器打开项目。** 用VSCode或Cursor都行，直接把整个项目文件夹拖进Cursor里。![](img/zhuanqian_839ccbf2ef248511f8d3aaa86c04653e.png)
**代码原理其实不难。** 刚才你填的那个token，就是后面调用API时用的凭证，代码里通常不会写死，而是放在 `.env` 环境变量文件中。![](img/zhuanqian_09f34e5282ea9c887d18c59b7c657c00.png)![](img/zhuanqian_32a0fa686b26189ab4d9ae798aef2b72.png) 接着你要指定想调用哪个图像模型，比如Replicate上的Stable Diffusion XL（SDXL），官方调用示例里会写明具体的模型名称。![](img/zhuanqian_9d93d48c95ac4bd91f6181a755ef5624.png) 调用时需要传参，最重要的就是 `prompt`，也就是你想生成的图像提示词。其他参数不用管，保持和官方示例一致就行。![](img/zhuanqian_fbc6c55ca2cf6772169b35df4bdd0a0e.png) Replicate上模型很多，每个模型都有官方示例，照着改即可。
**第三步，把生成的图片下载到本地。** 默认的初始化代码只会把生成图片的URL打印到控制台，看不方便。所以我们借Cursor改一下代码，让程序把图片下载到当前目录下的images文件夹里。![](img/zhuanqian_31bc20cc65cd165daab412c490524ff2.png) 改完按Cursor的提示安装必要依赖。![](img/zhuanqian_81ee73d5cb92a3778cc82202154ad632.png) 然后在控制台运行项目。```
node index.js
``` 跑完后，到根目录的images文件夹里就能看到AI生成的作品了。![](img/zhuanqian_c1be59eba5a8d3f102454c67bc8dc30d.png)![](img/zhuanqian_108bfad7d09bcb19b095144e3b626b39.png)
**小结一下：** 这是纯服务端代码调用Replicate图像模型API，直接在你电脑本地生成图片的方式。现在许多文生图网站本质就是这套逻辑，只不过外面套了一层网页：用户在前端输入提示词，后端把提示词传给模型API，生成完再返回页面展示给用户。
## 用Next.js搭建一个最简单的文生图网站
接下来咱们动真格：搭一个可访问的网站，部署到Vercel上，用户输入提示词就能生成图片。
### 前置条件
需要准备四样东西：
- Node.js环境（前面已介绍）
- Replicate账户（用来调用模型）
- GitHub账户（托管源代码）
- Vercel账户（部署网站）
### 搭建过程
**1. 创建项目并初始化。** 在本地新建一个文件夹，名字随意，比如 `demo-web`。在该目录下打开命令行，或者用 `cd` 命令进入这个目录，执行初始化项目的命令。```
npx create-next-app@latest --js --eslint
```![](img/zhuanqian_45e3907d9b9d2dae410cb09c97e3ecf4.png) 过程中会问你项目名称等选项，嫌麻烦直接一路回车用默认值就行。![](img/zhuanqian_de17027b3c4a344aa5c28157e4720d77.png) 初始化完成后，`demo-web` 文件夹里会多出一个 `my-app` 项目。把 `my-app` 文件夹拖进Cursor打开。![](img/zhuanqian_11fa854b70652fbfc0cee2a737f6ecce.png)![](img/zhuanqian_02285a7b13cff81ffb60ec6d21074cfb.png)
**2. 本地试运行。** 启动一下项目，确认初始页面能正常打开。```
cd my-app
npm run dev
```![](img/zhuanqian_9055a1c289b2c15f31f0ab287899f5e8.png) 启动成功后，访问控制台给的地址 http://localhost:3000 如果看到Next.js的欢迎页，就说明项目没问题。![](img/zhuanqian_09faf8fd33fe6eafd942d4c1b2981452.png)
**3. 配置环境变量。** 因为要调用Replicate的图像模型，必须把API Token放到环境变量文件里，项目启动后就能自动读取。在项目根目录中执行命令创建 `.env.local` 文件，Next.js会自动加载它。```
touch .env.local
``` 另外，不同后缀的环境变量文件对应不同环境，比如 `.env.production`、`.env.development`。![](img/zhuanqian_fe408fe3bbba0ee4c988d243b3ebca51.png) 创建完文件后，把你的Replicate API Token填进去。![](img/zhuanqian_def5fb4d27044380e7b4e54fa8e14d4b.png)![](img/zhuanqian_e46e2b6f02db6fc63be5378ae0496cc5.png)
**4. 编写后端代码。** 在 `src/app` 目录下新建 `api/predictions` 目录，用于存放业务代码。![](img/zhuanqian_32e1df5a9c56064e7e7c34381ab10182.png) 然后新建 `route.js` 文件，实现的功能是：接收POST请求，提取用户输入的提示词，调用Replicate API生成图片，并返回生成结果。```
import { NextResponse } from "next/server";
import Replicate from "replicate";
const replicate = new Replicate({
auth: process.env.REPLICATE_API_TOKEN,
});
// In production and preview deployments (on Vercel), the VERCEL_URL environment variable is set.
// In development (on your local machine), the NGROK_HOST environment variable is set.
const WEBHOOK_HOST = process.env.VERCEL_URL
? `https://${process.env.VERCEL_URL}`
: process.env.NGROK_HOST;
export async function POST(request) {
if (!process.env.REPLICATE_API_TOKEN) {
throw new Error(
'The REPLICATE_API_TOKEN environment variable is not set. See README.md for instructions on how to set it.'
);
}
const { prompt } = await request.json();
const options = {
model: 'black-forest-labs/flux-schnell',
input: { prompt }
}
if (WEBHOOK_HOST) {
options.webhook = `${WEBHOOK_HOST}/api/webhooks`
options.webhook_events_filter = ["start", "completed"]
}
// A prediction is the result you get when you run a model, including the input, output, and other details
const prediction = await replicate.predictions.create(options);
if (prediction?.error) {
return NextResponse.json({ detail: prediction.error }, { status: 500 });
}
return NextResponse.json(prediction, { status: 201 });
}
```
**5. Webhook回调说明。** 官方案例里有个 `WEBHOOK_HOST`，它的作用是让Replicate在模型运行过程中，通过Webhook把状态更新（开始、完成、错误）发送到你的应用。代码里是个三元表达式：生产环境用Vercel自动提供的 `VERCEL_URL`，开发环境则用 `NGROK_HOST`，也就是需要你用ngrok把本地服务器暴露到公网。![](img/zhuanqian_d254cc8547c088a2dac0daca4c737be4.png) 如果你只是为了跑通MVP，可以先不管这个变量，因为部署到Vercel后，它会自动帮你设置。但如果不配置，可能会遇到这些问题：收不到模型运行状态、生成请求可能失败、调试困难、依赖Webhook的功能无法正常工作。
**6. 动态路由获取生成结果。** 还需要新建一个 `[id]` 目录，并在里面新建 `route.js`。这里 `[id]` 是Next.js的动态路由规则。这个文件实现的功能是：通过Replicate API查询指定模型的生成结果。![](img/zhuanqian_b30ecf7a1f6216b4248791bdbee21c45.png)
到这里，一个文生图网站的骨架就算搭完了。把代码推到GitHub，再导入Vercel部署，就能获得一个公网可访问的AI图片生成站。所谓“套壳网站”，说白了就是“API调用 + 前端交互”。Replicate把繁琐的模型部署和算力问题全解决了，你只要专注做好页面和逻辑就行。是不是比想象中简单得多？那就动手试试看吧。
打造AI绘画套壳站：从0到1部署全流程，看这一篇就够了
最近不少朋友在折腾AI绘图类应用，但一直卡在“代码写好了却不知道如何上线”。别着急，今天我把一条完整可落地的全流程分享出来——从后端API搭建，到前端页面渲染，再到部署上云，手把手带你走通。整个过程基于Replicate平台的图像生成模型来跑通，顺便还会介绍一个开发调试的好帮手Ngrok，建议先收藏再细读。
先来说说服务端部分。我们设计了两个关键的接口文件，配合起来就能完成一次完整的图像生成请求闭环：第一个负责接收用户POST上来的提示词，并把预测任务提交给模型，再把返回结果送回到前端；第二个则是通过GET方式，用图像生成ID去查询生成进度和最终结果，同时把异常情况也处理妥当了。两方面结合，用户既能提交任务，也能随时掌握生成的动态，整个体验自然顺畅。
服务端通信打赢了，接下来就是做用户看得见摸得着的部分——前端界面。在项目结构里，有个page.js文件，这是Next.js初始化时自带的模板，一开始只渲染一个默认欢迎页。我们要做的就是清空它，替换成自己写的界面代码。这个新页面要完成几件事：显示标题、提供一个文本输入框供用户输入提示词、点击触发生成的按钮、把错误提示和图像结果都展示在页面上。简单说，用户在前端填好描述、点一下按钮，请求就交到后端，随后由后端去调用Replicate的图像模型返回生成结果。
光是页面能跑还不够，外观也得过得去。接下来就是把globals.css里的初始样式全部移除，换成这版配套的基础样式，让整体布局干净、层级清晰，这里不追求复杂设计，够用就行。
另一个值得注意的是图片域名白名单的配置。既然我们调用的是第三方replicate图像接口，而这个外部API不是我们自建可控的，如果不加约束，容易产生安全隐患。配置图片host主要从两个角度考虑：一是安全防护，避免恶意构造的图片URL把用户带去钓鱼站、窃取数据；二是资源管控，避免应用任意加载未经审核的外部图片资源。操作也很简单，在next.config.mjs里补上对应的图片域名配置即可。
本地测试环节也顺手过一遍。在终端执行npm run dev启动开发服务器，然后打开http://localhost:3000访问页面。输入提示词，比如“woman”，点击Go按钮开始生成。Flux Schnell是一个超链接，指向实际调用到的模型。第一次测试时可能会报错，没关系——直接切到cursor控制台，把错误信息丢给cursor，按提示安装replicate包，再重启项目，重新打开页面，图像就能正常生成出来了。
项目开发完，接下来是部署环节。第一步当然是把代码托管到GitHub。先在GitHub建一个空白仓库，然后把本地仓库与远程仓库关联起来，推代码上去，等远程仓库里出现对应文件，托管这一步就算完成了。紧接着，登录Vercel，选择“Add New Project”，导入刚才的GitHub仓库，点击Deploy等部署完成，Vercel会分配一个临时域名供访问测试。输入提示词点Go，页面却没有反应？别慌，去Vercel的后台查看日志，会发现大概率是少了Replicate的API Token。把本地环境变量里用到的Token在Vercel线上环境也配置一份，重新发布，再刷新页面，这次就稳了。
回想整个流程：用户在页面输入提示词，提交给后端，后端调用Replicate图像模型API生成图片，最后把结果回显到屏幕上——一个完善的套壳网站就完成了。后续还可以绑定自己的域名，教程在3月航海手册里写得很详细，按图索骥即可。
最后补一个压箱底的调试利器——Ngrok。它其实就是一个内网穿透工具，能把本地电脑上的服务映射成一个临时公共URL，让外部网络也能直接访问。尤其在开发调试阶段，不需要把服务部署上云，就可以快速验证一些外部回调（比如Webhook）。它的核心功能有几个：利用反向代理创建安全隧道，将公网请求转发到本地端口；支持HTTP/HTTPS/TCP/TLS多种协议转发；默认启用HTTPS加密，也可以配置密码、OAuth鉴权，甚至限制IP或域名访问。典型的使用场景包括：开发测试时快速调试支付回调和API通知；向客户或朋友临时演示本地项目；手机上调试本地后端接口；还有穿透防火墙访问内网设备比如NAS、数据库等。使用方法也简单：官网下载对应系统的压缩包，解压后放到/usr/local/bin目录；再到官网注册账号，拿到认证令牌后在命令行执行绑定命令，Token会保存在本地文件中，之后就可以使用了。
```
import { NextResponse } from "next/server";
import Replicate from "replicate";
const replicate = new Replicate({
auth: process.env.REPLICATE_API_TOKEN,
});
export async function GET(request, context) {
const { id } = await context.params;
const prediction = await replicate.predictions.get(id);
if (prediction?.error) {
return NextResponse.json({ detail: prediction.error }, { status: 500 });
}
return NextResponse.json(prediction);
}
```
![](img/zhuanqian_320538772dee5bcf1eec73757fd7631f.png)
```
'use client';
import { useState } from "react";
import Image from "next/image";
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
export default function Home() {
const [prediction, setPrediction] = useState(null);
const [error, setError] = useState(null);
const handleSubmit = async (e) => {
e.preventDefault();
const response = await fetch("/api/predictions", {
method: "POST",
headers: {
"Content-Type": "application/json",
},
body: JSON.stringify({
prompt: e.target.prompt.value,
}),
});
let prediction = await response.json();
if (response.status !== 201) {
setError(prediction.detail);
return;
}
setPrediction(prediction);
while (
prediction.status !== "succeeded" &&
prediction.status !== "failed"
) {
await sleep(1000);
const response = await fetch("/api/predictions/" + prediction.id);
prediction = await response.json();
if (response.status !== 200) {
setError(prediction.detail);
return;
}
console.log({ prediction: prediction });
setPrediction(prediction);
}
};
return (
#
Dream something with{" "}
[Flux Schnell](https://replicate.com/black-forest-labs/flux-schnell?utm_source=project&utm_project=getting-started)
{error && {error}}
{prediction && (
<>
{prediction.output && (
![output]({prediction.output[prediction.output.length)
)}
status: {prediction.status}
>
)}
);
}
```
![](img/zhuanqian_d43c4d3061285270963f7c5a94b05289.png)
```
@tailwind base;
@tailwind components;
@tailwind utilities;
.container {
padding: 2rem;
font-size: 1.3rem;
max-width: 48rem;
margin: 0 auto;
}
form {
display: flex;
margin-bottom: 2rem;
}
form input {
width: 100%;
padding: 1rem;
border: 1px solid #000;
border-radius: 0.25rem;
font-size: 1.3rem;
margin-right: 1rem;
}
form button {
padding: 1rem;
border: none;
border-radius: 0.25rem;
box-sizing: border-box;
cursor: pointer;
font-size: 1.3rem;
}
.imageWrapper {
width: 100%;
aspect-ratio: 1 / 1;
position: relative;
}
```
```
const nextConfig = {
reactStrictMode: true,
images: {
remotePatterns: [
{
protocol: "https",
hostname: "replicate.com",
},
{
protocol: "https",
hostname: "replicate.delivery",
},
],
},
};
export default nextConfig;
```
![](img/zhuanqian_c18bcdd8bae6d622131ed071b617f5e9.png)
```
// next.config.js
const nextConfig = {
reactStrictMode: true, // 与图片配置无关，是 React 严格模式开关
images: {
remotePatterns: [ // 远程图片规则配置
{
protocol: "https",  // 强制使用 HTTPS 协议
hostname: "replicate.com", // 允许的域名1
},
{
protocol: "https",
hostname: "replicate.delivery", // 允许的域名2
},
],
},
};
```
![](img/zhuanqian_871e34aebdd49874aeb94dabd76ffc56.png)
![](img/zhuanqian_ede6bd6824a33e9d1020137f8737725c.png)
![](img/zhuanqian_1748a35132ed8477f100eb06ce99ba98.png)
![](img/zhuanqian_ff52d88a91bfbaa48b297bd1d6c4a2e3.png)
![](img/zhuanqian_b08b38d32232475971414584e25a06e5.png)
![](img/zhuanqian_8c835584d7f336583e4db00538ccc671.png)
![](img/zhuanqian_4120d176dfeb44d4df3aa679ea4f9a4f.png)
```
git remote add origin 你的GitHub仓库地址.git
```
![](img/zhuanqian_1a0d74726d77aebba6dc181b4d559254.png)
```
# 添加所有文件到暂存区（或指定文件）
git add .
# 提交更改到本地仓库
git commit -m "Initial commit"
# 推送到 GitHub（首次推送需设置上游分支）
git push -u origin main
```
![](img/zhuanqian_fa1b70aff3d7a0efd1924144ca93318c.png)
![](img/zhuanqian_5191cc98bdf8ba568037496f8df85971.png)
![](img/zhuanqian_74ea767dfcee9a018171b78b4c3803a6.png)
![](img/zhuanqian_86258c1b4690013cfb89ca44d79325be.png)
![](img/zhuanqian_5378f558e6c747fffc27e1e6ae09dfdb.png)
![](img/zhuanqian_11d0f14cec6ab85ffd9fca95c6e089d2.png)
![](img/zhuanqian_4450939765dcac3b020dd226a82bd0de.png)
![](img/zhuanqian_51aec9fe406ccb97ff490660a8eb3124.png)
![](img/zhuanqian_daff48a34c137f999684ce6c304eb4db.png)
![](img/zhuanqian_c5502f43bc55f38d234b90c12b68b169.png)
![](img/zhuanqian_140d6804c2427c46f48c97e5c09546e0.png)
![](img/zhuanqian_282a92f85281f8c06a382d9360066c5c.png)
![](img/zhuanqian_8be23b058b1930c26b6241c71cd95984.png)
![](img/zhuanqian_5028fbc8ebf4f67247468a4f97a23bd1.png)
![](img/zhuanqian_3d097804aa0b099be9b1bda28f396fec.png)
![](img/zhuanqian_3111d8591eed25685eaac43981c5527d.png)
![](img/zhuanqian_c211cbf349f7fb67bccf61579777645d.png)
```
ngrok config add-authtoken <你的令牌>
```
![](img/zhuanqian_4e20919d15b6124af7d43b09c4b62296.png)
![](img/zhuanqian_ba963a3df227ea313ac313e9e83a1be0.png)
3）启动服务
```
ngrok http 80
```
![](img/zhuanqian_813f0b4b8c77d7eecc9278fa4c5d20de.png)
*   把运行在本地 80 端口的项目，比如本地搭建的网站，通过工具映射到互联网，并自动分配一个临时的公网地址，例如 https://abc.ngrok.app。
*   拿到这个地址后，外网用户直接打开就能远程访问你电脑上的本地服务。