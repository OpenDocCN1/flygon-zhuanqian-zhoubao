# 我靠 Cursor 做了个抖音爆款留痕站，全程没手写代码

> 转自：飞书文档

## 开篇先交代

这篇文章想聊三件事：

1. 怎么用 AI 写代码，把一个能实际使用的工具站从想法推到上线。

2. 做数据采集类项目时，怎么让结果更直观；重点是“给作品留痕”，靠每次抓取记录看清涨势。

3. 这类给运营提效的小网站，基本都能照着这个套路快速做完。

## 需求是从哪里来的

我有这样一套固定动作：每天定时采集约 100 位对标账号近 3 天的表现，整理进 Excel，再发邮件出去。

![](img/zhuanqian_3920f9de9d40f5aa762232f4dbe1798b.png)

![](img/zhuanqian_04a68aa778f74dfcf20a6c43a0cc93a4.png)

采集虽然一直在跑，但账号数量差不多一百个，表格里的信息太密，根本看不出哪些爆品正在快速起量；想做分组、标签和筛选也都不好用。

于是我想换一种思路：每个作品只要被采集一次，就在存储里追加一条留痕记录。

这事的价值在于——带货短视频里，选品基本决定生死。当这些留痕记录汇总起来，运营能直接看到同行作品的上涨轨迹，也能更快跟上爆款脚本和拍摄思路。

![](img/zhuanqian_0f7ba46b5010cebfc5e104537bf1e69c.png)

![](img/zhuanqian_5842664a9507088a01254e60f0442aae.png)

![](img/zhuanqian_f7d57c288e3bdb89d8cb91afa9fb5036.png)

![](img/zhuanqian_c14b8bfbcad5de7f5dfc9c237dc03ae5.png)

## 先找 ChatGPT 把需求理清楚

我习惯先把想法整理成一份可执行的需求说明，再往下走。

框架方面，我选了 Next.js。它最近热度高，很多 AI 产品站都在用；更关键的是能接到 Vercel 的免费托管，代码改完就能实时更新。

![](img/zhuanqian_9ed0ae3ebca7838664e3ba86e493632d.png)

![](img/zhuanqian_064207551e1b3456bfe12c9c766a5a1a.png)

## 再用 bolt 画一套免费原型

之前看到有人在社群里分享，用 bolt.new 做出来的前端页面很合我胃口，直接圈粉。

工具链接：bolt.new

![](img/zhuanqian_c988c52355d7da25616dee3bc2c2f82e.png)

我只让 bolt 出原型，真实功能还是交给 Cursor 来写。原型只是把页面布局和点击交互演示出来，不接任何后端数据。

原型界面演示略。

## 用 Cursor 落地功能

### 先把 Cursor Rules 备好

我从一个开源项目里拿了一套现成的 Cursor Rules，再根据自己的项目环境做了调整。

有了 Rules，AI 会按统一的风格和规范输出，代码结构和质量更稳，后续沟通成本也少很多。

![](img/zhuanqian_6e3c7163b4d2fa04c891d519435123d9.png)

### 把功能做完

我把整理好的需求说明、bolt 生成的原型代码，以及刚才那套 Rules 一股脑交给 Cursor，让它直接产出功能代码。

模型通常用 Claude 3.7 或 Claude 4.0。这套组合的编码表现确实强，来回聊几轮基本就能跑通。遇到报错就把报错内容原样贴回去，让它自己修，绝大多数问题都能解决。

## Supabase 做后端，免费档够用

Supabase 适合快速把后端凑齐，注册登录、认证、存储、接口都能一站搞定。

它的免费配额对独立开发者来说足够起步。下面的信息整理于 2025 年年中。

### 基础配额

- Postgres 提供 500MB 容量，SQL 功能完整。

- CPU 按共享方式分配，内存 500MB，应对小型项目绰绰有余。

- 每个月有 5GB 出网流量，超了要升级。

- 另给 1GB 文件空间。

- 接口调用次数不限。

### 免费档能力上限

- 月活用户上限 5 万，包含登录认证。

- 同时可保持 200 条实时长连接。

- Edge Function 每月有 50 万次执行额度。

### 免费档的项目规则

- 免费档最多同时运行两个项目。

- 项目连续一周没动静会进入休眠；再想启动，得自己去控制台点一下。

### 和同类产品对比

- 和 Firebase 比：Supabase 的底层是开源 Postgres，改造成本低、玩法多；Firebase 的文档存储在某些场景下反而更好上手。

- 和 CMS 比：Supabase 管的是后端数据和登录认证，CMS 管的是内容发布和后台编辑，定位完全不一样。

### 几点提醒

- 用量要去自家控制台盯着，接近上限会有提醒。

- 免费档没有人工客服，只能去社区提问。

- 备份能力比较基础，想要每天自动备份或保留更久，就得升级付费版，25 美元/月起步。

### 小结

这套免费方案拿来做练手项目、个人站点或者跑通想法都挺合适。真需要更高配置或多人协作时，再升级付费套餐就行。国内访问海外节点（比如日韩）延迟偏高，但整体可用。

配套视频：B 站搜 “Supabase 教程” 能找到不少。

官网：supabase.com

![](img/zhuanqian_fd5fc2fff352218e777cbba630eec8ab.png)

![](img/zhuanqian_3c030f730e86264f25177c9961a4d353.png)

![](img/zhuanqian_7aad631552298d44348cde2ec4ec531c.png)

![](img/zhuanqian_0bf8bacc2f38934f197c1201942dbf71.png)

![](img/zhuanqian_b1214737c516ba4673e2c64fa2aa5052.png)

![](img/zhuanqian_4a06dd5d5e85a50abca63c58b2670598.png)

![](img/zhuanqian_21562f45ed22854434084ba686f8e18a.png)

![](img/zhuanqian_8003926c243faef33a45568042e9aa8a.png)

![](img/zhuanqian_d4b0ebaa7b4938cc4d9d3c00e3bab06e.png)

把 Cursor 生成的建表 SQL 复制到 Supabase 里执行，表结构就算就位了。

### 打开邮箱登录认证

![](img/zhuanqian_d7b0e3a5aa328d69afca4b662b63f2a9.png)

![](img/zhuanqian_dec349de3075dd8e49321bd79a5d65e6.png)

![](img/zhuanqian_10e6b5743d80874e2f6b0e1fff60b380.png)

在控制台里把邮箱密码登录打开即可。

## 用 Vercel 发布上线，也是免费

Vercel 跟 Next.js 配合得很顺，官方模板库也有一堆现成示例。

官网：vercel.com

用 GitHub 身份登录后关联仓库，就能实现自动发布：每次提交代码，平台都会立刻构建并上线。

Vercel 免费档（Hobby）面向个人用户和小型项目，要点如下：

### 基础配额

- 每个月能发布 1000 次，每次往仓库提交代码，都会消耗一次发布次数。

- 每月有 100GB 带宽，再加 100GB-小时的 Serverless 实例累计用量。

- Node.js、Python 都能跑；单次任务能跑多久，上限要看官方说明。

### 能力上限

- 如果仓库属于 GitHub 的 Organization，免费档不支持；想用就得升级，每人每月 20 美元；或者用 Vercel CLI 单独建项目来绕过。

- Docker 应用没法放到上面跑。

- 自定义域名可以绑，平台会顺带配好 HTTPS 证书。

### 仓库联动方式

- GitHub、GitLab、Bitbucket 都能关联，提交代码的瞬间就会触发新的构建。

- 静态资源会走遍布各地的加速节点，加载体验不错。

### 典型用途

- 放个人主页、博客或者轻量前端项目都很顺手。

- 用来跑 Demo 或做临时展示都没问题；应付正式流量还是得升配。

### 和同类平台对比

- 它最大的好处是发布链路极短，跟 Next.js 是绝配，特别适合 Serverless 形态的站点。

- 免费档给到的余量不多，多人一起用要付费，Docker 也基本无缘。

其他参数（比如单次任务最长跑多久、并发上限）建议直接看官方说明。若嫌配额紧，Netlify 或 Cloudflare Pages 也能看。

## 填好项目变量

项目里的 .env 配置，拿到 Vercel 后台对应页面填一遍即可。

```
变量名: NEXT_PUBLIC_SUPABASE_URL
值: https://your-project-id.supabase.co
环境: Production, Preview, Development (全选)
变量名: NEXT_PUBLIC_SUPABASE_ANON_KEY
值: your-anon-key
环境: Production, Preview, Development (全选)
变量名: NEXT_PUBLIC_API_BASE_URL
值: https://your-vercel-domain.vercel.app
环境: Production, Preview, Development (全选)
变量名: NEXT_PUBLIC_APP_NAME
值: "抖音达人数据中心"
环境: Production, Preview, Development (全选)
变量名: NODE_ENV
值: production
环境: Production (只选择生产环境)
```

![](img/zhuanqian_f2341ef77231d917778d22a0e10138ee.png)

## 开启自动发布

打开这个开关后，我们只要把代码推到 GitHub，平台就会立刻构建并发布，非常省心。

![](img/zhuanqian_dbdb46d8ba9f7e1fd4d9f2301dd197bc.png)

## 绑定域名

我用的域名买自国内服务商，加了一段子域名前缀，解析到 Vercel 就算完成。

![](img/zhuanqian_661459b965092c0d10d47e06baa1af9c.png)

![](img/zhuanqian_ec3cafa0792547cb6b5df1fc052bd484.png)

## 最后

「这波经验若能帮到你，记得回社群给个赞👍」