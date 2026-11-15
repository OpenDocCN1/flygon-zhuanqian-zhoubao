# 从翻车到搞定：我用Cursor重装云服务器的全过程
先交代下背景。之前我为了搭一个Web网站，在Cursor的帮助下，按照Claude的指示装好了Node.js和pm2，跑通了一套环境。最近又开始研究iOS航海，照着手册想配置宝塔面板，结果配完Nginx直接冲突了。
我两边都不想放弃，就在云服务器上折腾一套能兼容的部署方案。最后决定：干脆把服务器重装了，直接交给Cursor来指导部署。由于星球里关于云服务器配置的帖子真的很少，所以我把整个流程写下来，希望能帮大家少踩坑。
这套教程适合：
- 想给Web或应用搭服务器，但是完全没思路；
- 之前配置过，但因为种种原因想重来一遍；
- 服务器已经准备好了，想搭建API、部署网页。
## 第一步：重装服务器系统
重装系统之前，系统选择很关键。我当时直接选了Ubuntu，一方面CentOS官方已经停止维护，另一方面如果本机Windows配置一般，CentOS用起来也费劲。重装时设置好登录密码就好。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_97839ff5e635963c4a180ac61facd883.png>
系统重装完成后，打开本地终端（Terminal）。以云服务器IP地址11.22.33.44为例，执行下面的命令：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_36a262d8b9e1e77a27a17475601f4940.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_35f39f1ed52be7773b5858173841b9ef.png>
```
ssh root@11.22.33.44 -p 22
```
执行后终端会提示输入密码，也就是刚才重装时设置的那个登录密码。输对之后，就能连上云服务器了，到这里服务器的初始状态就准备好了。
## 第二步：让Cursor来规划开发部署
连接好服务器之后，不要急着乱装东西，先让Cursor出一份完整的部署计划。我直接在对话里发起了需求：
```
我已经重装了服务器了，请结合当前ios应用的项目架构和需求，以及我还想做同一整套的web网站，你先帮我制定下开发部署计划吧，你可以提问我任何问题来确认方案细节
```
Cursor很快就回复了，先是跟我确认几个关键点，比如用户数据是否需要跨端同步、Web端功能是否要和iOS完全一致、两个平台开发的优先级、用哪家AI服务生成内容、是个人开发还是团队协作。
之后它给了这样一套架构设计方案：
```
+----------------+
|   DNS服务     |
+-------+--------+
v
+----------------+
|   Nginx代理    |
+-------+--------+
+-------------------------+
v                         v
+---------------------+    +--------------------+
|   Web前端应用        |    |    API服务        |
| (React/Vue/Angular) |    | (Node.js+Express) |
+---------------------+    +--------+----------+
+---------+---------+
v                   v
+------------+     +---------------+
| 数据库      |     | AI服务集成     |
| (MongoDB/  |     | (Claude API/  |
|  MySQL)    |     |  OpenAI API)  |
+------------+     +---------------+
```
整体开发周期计划比较长，这里就先忽略了。但里面提到的几个开发重点和挑战值得注意：数据要有实时同步机制、两个平台的用户体验要保持一致、AI服务的稳定性和响应速度要可靠、还要考虑用户数据和API的安全、以及性能优化，尤其是卡片生成和渲染。
再往后它问了我一堆问题，涉及到前端框架、数据库选型、AI服务集成、第三方登录、部署方式、时间线等。我也一一做了回应：
- Web前端框架我其实不太懂，就说是照着帖子用工具搭建的，最后确认是原生JavaScript，没上框架。
- 数据库方面，Cursor建议用MongoDB，我同意了。
- AI服务我有现成的API密钥，也有目标API站点。
- 用户认证问支不支持第三方登录，我说如果苹果登录不复杂的话可以加上。
- 部署模式我不太懂，让Cursor自己推荐。
- 时间要求就一条：越快越好。
```
web前端我已经用工具做好网站页面了，如何确认它用的什么框架？
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ceab5af379ba9a83211ac10235b7a662.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_457fda440eca0284bf302564e59db7d7.png>
## 第三步：安装宝塔面板
接下来就是在服务器上装宝塔面板。打开终端，登录云服务器，然后根据系统版本执行对应的下载命令。Ubuntu系统：
```
wget -O install_panel.sh https://download.bt.cn/install/install_panel.sh && sudo bash install_panel.sh ed8484bec
```
也可以用Linux通用安装脚本：
```
if [ -f /usr/bin/curl ];then curl -sSO https://download.bt.cn/install/install_panel.sh;else wget -O install_panel.sh https://download.bt.cn/install/install_panel.sh;fi;bash install_panel.sh ed8484bec
```
命令来源可以参考宝塔官方下载页：https://www.bt.cn/new/download.html
安装完成后，宝塔会给出管理面板的URL、用户名和密码。把地址复制到浏览器里打开，用给的账号密码登录。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ddce0c5c591ae444b2f44a19c54276b6.png>
一登录上去，宝塔会推荐一键安装组合套装。航海手册里用的是LNMP，可以参考，但我打算完全按Cursor的建议来装，所以直接忽略了一键安装，把弹窗关掉就行。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d162d2f9549b7dc7ade97ee516b1fc10.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6892cb06d5728e00e2db8b6ce8d02a58.png>
接下来进入软件商店，安装这几个配置项：
- Nginx 1.18以上（推荐1.20），我直接选了最新的1.24；
- Node.js 16以上（推荐16.14.0），我选了16.9.0；
- MongoDB 5以上，我装了7.0；
- PM2管理器。
这里有个坑要注意：PM2管理器计划于2023年12月31日下架，如果之后再用，得去【网站->Node项目】里操作。另外，下载Node.js之前，得先安装Node.js版本管理器，而且装Node.js时会自带PM2，所以不用再单独下载PM2管理器了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d2dbc1b8f080754c7f4b28943ffca14c.png>
### 排查常见问题：Node版本不一致
如果你发现命令行里的Node.js版本和面板里设置的不一致，可以这样处理：
1. 先到宝塔面板里确认Node.js路径，一般是 `/www/server/nodejs/bin/node`。
2. 在命令行里执行版本检查。
3. 如果旧版本缓存还在，就更新系统路径的优先级。
```
# 查看系统中的node命令位置
which node
# 直接使用宝塔安装的Node.js
/www/server/nodejs/v16.9.0/bin/node -v
```
```
echo 'export PATH="/www/server/nodejs/v16.9.0/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
## 第四步：安全组与防火墙规则
为什么要配置安全组？简单说，云服务器的IP有很多端口，安全组就是一个门禁，只放行我们需要的端口，其他都挡在外面。
举个例子，我们之前用SSH连服务器的时候，命令里有个 `-p 22`，就是走的22号端口。如果没配置安全组，这个端口可能无法从外部访问。安装宝塔面板后，面板也会提示：请在安全组放行xxxxx端口。比如它用 `IP:33871` 访问管理界面，那就要在安全组里把33871放行。
安全组的配置方法不复杂：去云服务器控制台找到“安全组”入口，新建一个安全组。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e6b9a196b49270b316f5ba5fb186c68f.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_faa84be4cb151490809611ea073ae7fc.png>
名称和标签可以随意填，自己看得懂就行。比如名称写项目名，标签注明开放了哪些端口。
建完安全组后，点击“配置规则”，然后新建规则：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4ee04f4bc18d1d6395bbe14b2c3f80a9.png>
常用协议和端口基本都列出来了，按需勾选就行：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ebbcff7aff88d65796eef5ec29945871.png>
现阶段我们需要开放这些端口：
- 80（HTTP）
- 443（HTTPS）
- 22（SSH）
- 宝塔面板端口
规则配好后，回到安全组列表，在“管理实例”里选择“新增关联”，把安全组绑到我们的云服务器上。这样规则就生效了。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_886d8912c700dceb17be456669993ef8.png>
## 第五步：部署Web页面（iOS可忽略）
如果你的重心是全栈，这里就是重头戏。部署Web页面分几步走。
### 上传现有的HTML页面
先用终端连上云服务器，创建网站目录结构。然后通过宝塔面板的文件管理器，把HTML文件传到 `/www/wwwroot/ainotecard/public`。需要上传的文件包括 `index.html`、`generate.html` 以及相关的静态资源，可以拖拽上传。
```
mkdir -p /www/wwwroot/ainotecard/{api,public,logs,data,scripts}
chmod -R 755 /www/wwwroot/ainotecard
chown -R www:www /www/wwwroot/ainotecard
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bc726a1cd30a8f7fe7fe1524b1a87661.png>
### 配置Nginx站点
第一步：创建必要的目录结构和文件。如果目录还不存在，就先到宝塔文件管理器里把它们建好。然后在这些目录下新建文件，比如在 `/www/wwwroot/ainotecard/api/` 目录下新建 `server.js`，填入服务端代码。同样在 `/api` 目录下创建 `package.json`，写入依赖信息。
```
/www/wwwroot/ainotecard/api/
```
```
// 基础Express服务器配置
const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;
// 中间件配置
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));
// 测试路由
app.get('/api/test', (req, res) => {
res.json({ message: '服务器运行正常' });
});
// 启动服务器
app.listen(PORT, () => {
console.log(`服务器运行在端口: ${PORT}`);
});
```
```
{
"name": "ainotecard-api",
"version": "1.0.0",
"description": "AINoteCard API服务",
"main": "server.js",
"scripts": {
"start": "node server.js"
},
"dependencies": {
"express": "^4.18.2"
}
}
```
第二步：安装基础依赖。在终端里通过SSH连上云服务器，先检查Node版本。如果版本低于14.0.0，需要更新到16。
```
node -v
# 安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
# 安装 Node.js 16
nvm install 16
nvm use 16
```
```
cd /www/wwwroot/ainotecard/api
```
```
apt install npm
```
```
npm install
```
第三步：添加Node项目。现在基础文件已经有了，去宝塔面板添加Node项目，配置信息如下：
- 项目名称：ainotecard-api
- Node版本：v16.9.0
- 启动文件：`/www/wwwroot/ainotecard/api/server.js`
- 运行目录：`/www/wwwroot/ainotecard/api`
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_970e727dcadc45ef729373752342dc5f.png>
第四步：测试基本功能。项目添加完后，在Node项目管理页面点击“启动”，等状态变成“正在运行”，然后在浏览器里访问 `http://服务器IP:3000/api/test`，如果能看到 `{"message":"服务器运行正常"}`，说明服务已经正常启动。
注意：如果浏览器访问不到，多半是因为我们还没在安全组里放行3000端口。去安全组把3000端口加上就好。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9b265f42c39c2907ed3df83a91e7fc82.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d8d0377d06f288bc817ac7bd3146362.png>
添加完后可以再回终端确认一下防火墙状态：
```
# 查看UFW防火墙状态
sudo ufw status
# 如果3000端口未开放，可以添加规则
sudo ufw allow 3000/tcp
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c32fc2fd70adb918a81ffff271dd8d65.png>
放行后，再访问 `http://ip:3000/api/test` 就能看到JSON响应了。通过域名访问也一样，比如 `http://域名:3000/api/test`。
两种访问方式都返回了 `{"message":"服务器运行正常"}`，说明Node.js服务已经正确运行，且能从外部访问。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_32f28ced565c896c07f427cb7c6a5f90.png>
第五步：设置Nginx反向代理。这一步其实是在宝塔面板里操作：
1. 在“网站”里选择“PHP项目”，点击“添加站点”，填好域名，PHP版本选“纯静态”，提交即可。
2. 在网站列表找到刚创建的站点，点击右侧“设置”，找到左侧菜单里的“反向代理”选项（如果没看到，可能要展开“更多功能”）。
3. 点击“添加反向代理”，打开高级功能，填写代理名称，比如“api”，然后保存。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a479af1057ea5f4a67b77d3cf686c441.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2f72f3a3df749b05b58ecd7382a5a89a.png>
到这里，整个服务器的部署流程就清晰了。通过重装系统解决环境冲突，用Cursor规划开发，再用宝塔面板做可视化管理，最后一步一步把Web服务跑起来。整个过程其实没有想象中那么复杂，关键是按顺序来，不要跳过安全组和依赖安装这些基础环节。希望这篇攻略能帮到正在折腾云服务器的你。
最近折腾 Node 服务的转发规则时，被一个细节绊住。先说宝塔里的设置方法：目标地址写成 http://127.0.0.1:3000，即本地 Node 进程的监听地址；发出方域名沿用系统默认的 $host；转发路径填写 /api，意指所有以 /api 开头的请求都导向 Node 进程，其余参数维持原样，点下保存即可。<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_39c226b308898c3cac22631b9db4b85c.png>
设置完成后，形如 http://你的域名/api/xxx 的请求会进入 http://127.0.0.1:3000/api/xxx 的处理流程，也就是落到 Node 服务上。需要留意的是，这里生效的是域名触发的转发；如果直接用 IP 拼凑 http://ip/api/xxx 并不会走这条规则，也无需刻意处理。用浏览器打开 http://域名/api/test 能正常返回，就代表转发生效。之所以会出现这种现象，是因为宝塔默认的转发策略仅作用于域名，IP 形式的访问不会被送到对应端口。当时我自检很久都没找到症结，后来在航海群求助，两位同行一眼就点出了关键。<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_35ae0dab67cbf5e5f93ce7b5d142fc9d.png>
下面进入第四部分，服务端底层搭建。
先把所需包装好，同时把工程目录搭起来。```
cd /www/wwwroot/ainotecard/api
npm install express mongoose cors dotenv body-parser jsonwebtoken bcrypt
mkdir -p models routes controllers middleware config
touch .env config/database.js server.js
```
随后新建并修改环境变量配置文件。```
cat > .env << EOF
PORT=3000
MONGODB_URI=mongodb://localhost:27017/ainotecard
JWT_SECRET=$(openssl rand -base64 32)
EOF
```
再准备数据库连接的配置文件。```
cat > config/database.js << EOF
const mongoose = require('mongoose');
require('dotenv').config();
// 数据库连接选项
const options = {
useNewUrlParser: true,
useUnifiedTopology: true
};
// 连接到数据库
const connectDB = async () => {
try {
await mongoose.connect(process.env.MONGODB_URI, options);
console.log('数据库连接成功');
} catch (err) {
console.error('数据库连接失败:', err.message);
process.exit(1);
}
};
module.exports = connectDB;
EOF
```
再写主程序入口 server.js。```
cat > server.js << EOF
// 导入必要的包
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const connectDB = require('./config/database');
// 初始化Express应用
const app = express();
const PORT = process.env.PORT || 3000;
// 连接数据库
connectDB();
// 中间件
app.use(cors());
app.use(bodyParser.json());
// 测试路由 - 保留现有功能
app.get('/api/test', (req, res) => {
res.json({ message: '服务器运行正常' });
});
// 路由占位 - 将在后续步骤实现
// app.use('/api/auth', require('./routes/auth'));
// app.use('/api/cards', require('./routes/cards'));
// 错误处理中间件
app.use((err, req, res, next) => {
console.error(err.stack);
res.status(500).json({ message: '服务器错误', error: err.message });
});
// 启动服务器
app.listen(PORT, () => {
console.log(\`服务器运行在端口: \${PORT}\`);
});
EOF
```
接着生成用户数据模型文件，执行对应指令。```
cat > models/User.js << EOF
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
// 用户模式定义
const userSchema = new mongoose.Schema({
username: {
type: String,
required: true,
unique: true,
trim: true,
minlength: 3
},
email: {
type: String,
required: true,
unique: true,
trim: true,
lowercase: true
},
password: {
type: String,
required: true,
minlength: 6
},
createdAt: {
type: Date,
default: Date.now
}
});
// 保存前加密密码
userSchema.pre('save', async function(next) {
// 只有当密码被修改时才加密
if (!this.isModified('password')) return next();
try {
// 生成盐
const salt = await bcrypt.genSalt(10);
// 生成加密密码
this.password = await bcrypt.hash(this.password, salt);
next();
} catch (error) {
next(error);
}
});
// 验证密码的方法
userSchema.methods.comparePassword = async function(candidatePassword) {
return await bcrypt.compare(candidatePassword, this.password);
};
// 创建模型
const User = mongoose.model('User', userSchema);
module.exports = User;
EOF
```
再写一个用于校验 JWT 的中间层。```
cat > middleware/auth.js << EOF
const jwt = require('jsonwebtoken');
require('dotenv').config();
// 认证中间件：验证JWT令牌
const auth = (req, res, next) => {
// 从请求头获取令牌
const token = req.header('Authorization')?.replace('Bearer ', '');
// 如果没有令牌，返回401未授权
if (!token) {
return res.status(401).json({ message: '无访问令牌，授权失败' });
}
try {
// 验证令牌
const decoded = jwt.verify(token, process.env.JWT_SECRET);
// 将用户信息添加到请求对象
req.user = decoded;
next();
} catch (error) {
res.status(401).json({ message: '令牌无效', error: error.message });
}
};
module.exports = auth;
EOF
```
再创建鉴权相关的路由集合。```
cat > routes/auth.js << EOF
const express = require('express');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const router = express.Router();
// 注册新用户
router.post('/register', async (req, res) => {
try {
const { username, email, password } = req.body;
// 检查用户是否已存在
const userExists = await User.findOne({
$or: [{ email }, { username }]
});
if (userExists) {
return res.status(400).json({ message: '用户已存在' });
}
// 创建新用户
const user = new User({
username,
email,
password
});
// 保存用户（密码会在save前被加密）
await user.save();
// 生成JWT令牌
const token = jwt.sign(
{ id: user._id, username: user.username },
process.env.JWT_SECRET,
{ expiresIn: '30d' }
);
// 返回成功消息和令牌
res.status(201).json({
message: '用户注册成功',
token,
user: {
id: user._id,
username: user.username,
email: user.email
}
});
} catch (error) {
res.status(500).json({ message: '服务器错误', error: error.message });
}
});
// 用户登录
router.post('/login', async (req, res) => {
try {
const { email, password } = req.body;
// 查找用户
const user = await User.findOne({ email });
// 如果用户不存在
if (!user) {
return res.status(400).json({ message: '邮箱或密码不正确' });
}
// 验证密码
const isMatch = await user.comparePassword(password);
// 如果密码不匹配
if (!isMatch) {
return res.status(400).json({ message: '邮箱或密码不正确' });
}
// 生成JWT令牌
const token = jwt.sign(
{ id: user._id, username: user.username },
process.env.JWT_SECRET,
{ expiresIn: '30d' }
);
// 返回成功消息和令牌
res.json({
message: '登录成功',
token,
user: {
id: user._id,
username: user.username,
email: user.email
}
});
} catch (error) {
res.status(500).json({ message: '服务器错误', error: error.message });
}
});
module.exports = router;
EOF
```
回到 server.js 把鉴权路由挂载上。```
nano server.js
``` 操作是定位到 `// app.use('/api/auth', require('./routes/auth'));` 这一行，移除行首的注释符号 `//`。```
app.use('/api/auth', require('./routes/auth'));
``` 退出编辑时按 Ctrl+X，然后确认 Y，最后回车。
继续生成卡片数据模型。```
cat > models/Card.js << EOF
const mongoose = require('mongoose');
// 卡片模式定义
const cardSchema = new mongoose.Schema({
user: {
type: mongoose.Schema.Types.ObjectId,
ref: 'User',
required: true
},
title: {
type: String,
required: true,
trim: true
},
content: {
type: String,
required: true
},
tags: [{
type: String,
trim: true
}],
category: {
type: String,
trim: true,
default: '未分类'
},
isAIGenerated: {
type: Boolean,
default: false
},
createdAt: {
type: Date,
default: Date.now
},
updatedAt: {
type: Date,
default: Date.now
}
});
// 更新前更新时间
cardSchema.pre('save', function(next) {
if (this.isModified()) {
this.updatedAt = Date.now();
}
next();
});
// 创建模型
const Card = mongoose.model('Card', cardSchema);
module.exports = Card;
EOF
```
最后补齐卡片相关的路由定义。
```
cat > routes/cards.js << EOF
const express = require('express');
const router = express.Router();
const Card = require('../models/Card');
const auth = require('../middleware/auth');
// 获取当前用户的所有卡片
// GET /api/cards
router.get('/', auth, async (req, res) => {
try {
const cards = await Card.find({ user: req.user.id }).sort({ createdAt: -1 });
res.json(cards);
} catch (error) {
res.status(500).json({ message: '服务器错误', error: error.message });
}
});
// 获取单个卡片
// GET /api/cards/:id
router.get('/:id', auth, async (req, res) => {
try {
const card = await Card.findOne({
_id: req.params.id,
user: req.user.id
});
if (!card) {
return res.status(404).json({ message: '卡片未找到' });
}
res.json(card);
} catch (error) {
res.status(500).json({ message: '服务器错误', error: error.message });
}
});
// 创建新卡片
// POST /api/cards
router.post('/', auth, async (req, res) => {
try {
const { title, content, tags, category, isAIGenerated } = req.body;
const newCard = new Card({
user: req.user.id,
title,
content,
tags: tags || [],
category: category || '未分类',
isAIGenerated: isAIGenerated || false
});
const card = await newCard.save();
res.status(201).json(card);
} catch (error) {
res.status(500).json({ message: '服务器错误', error: error.message });
}
});
// 更新卡片
// PUT /api/cards/:id
router.put('/:id', auth, async (req, res) => {
try {
const { title, content, tags, category } = req.body;
// 构建更新对象
const cardFields = {};
if (title) cardFields.title = title;
if (content) cardFields.content = content;
if (tags) cardFields.tags = tags;
if (category) cardFields.category = category;
// 查找卡片并更新
let card = await Card.findOne({
_id: req.params.id,
user: req.user.id
});
if (!card) {
return res.status(404).json({ message: '卡片未找到' });
}
card = await Card.findByIdAndUpdate(
req.params.id,
{ $set: cardFields },
{ new: true }
);
res.json(card);
} catch (error) {
res.status(500).json({ message: '服务器错误', error: error.message });
}
});
// 删除卡片
// DELETE /api/cards/:id
router.delete('/:id', auth, async (req, res) => {
try {
const card = await Card.findOne({
_id: req.params.id,
user: req.user.id
});
if (!card) {
return res.status(404).json({ message: '卡片未找到' });
}
await Card.findByIdAndRemove(req.params.id);
res.json({ message: '卡片已删除' });
} catch (error) {
res.status(500).json({ message: '服务器错误', error: error.message });
}
});
module.exports = router;
EOF
```
在项目推进的下一个阶段，我们要把注意力放在后端主文件的迭代上。
```
nano server.js
找到// app.use('/api/cards', require('./routes/cards'));
改为
app.use('/api/cards', require('./routes/cards'));
```
先从零搭建一个轻量级的 AI 服务层，把调用逻辑、参数封装和异常处理都收拢到一个独立模块里，方便后续复用和维护。
```
mkdir -p services
cat > services/ai.js << EOF
// AI服务 - 简单实现，未连接实际AI API
class AIService {
/**
* 生成笔记卡片
* @param {string} prompt - 用户输入的提示
* @param {string} template - 卡片模板类型
* @returns {Promise} - 生成的卡片内容
*/
static async generateCard(prompt, template = 'standard') {
// 这里应该连接到真实的AI API
// 目前使用简单的模拟实现
// 模拟API延迟
await new Promise(resolve => setTimeout(resolve, 1000));
// 根据模板生成不同结构的内容
let title, content;
switch (template) {
case 'question':
title = \`关于: \${prompt.substring(0, 30)}\`;
content = \`问题: \${prompt}\\n\\n答案: 这是对"\${prompt}"的回答。详细解释...\\n\\n扩展思考: 这里是一些延伸的相关知识点。\`;
break;
case 'summary':
title = \`摘要: \${prompt.substring(0, 30)}\`;
content = \`原文: \${prompt}\\n\\n摘要: 这是对上述内容的简明摘要。包含主要观点和关键信息。\\n\\n关键点:\\n- 第一个要点\\n- 第二个要点\\n- 第三个要点\`;
break;
default: // standard
title = prompt.substring(0, 30) + '...';
content = \`${prompt}\\n\\n这里是生成的笔记内容。包含了关键概念、解释和例子。\\n\\n关键词: 关键词1, 关键词2, 关键词3\`;
}
return {
title,
content,
isAIGenerated: true,
tags: ['AI生成', template],
category: '自动生成'
};
}
}
module.exports = AIService;
EOF
```
有了服务层之后，紧接着设计对外暴露的 AI 卡片生成接口，为前端提供统一的请求入口。
```
cat > routes/ai.js << EOF
const express = require('express');
const router = express.Router();
const Card = require('../models/Card');
const auth = require('../middleware/auth');
const AIService = require('../services/ai');
// 生成AI卡片
// POST /api/ai/generate
router.post('/generate', auth, async (req, res) => {
try {
const { prompt, template } = req.body;
if (!prompt) {
return res.status(400).json({ message: '提示内容不能为空' });
}
// 调用AI服务生成卡片内容
const cardData = await AIService.generateCard(prompt, template);
// 创建新卡片
const newCard = new Card({
user: req.user.id,
title: cardData.title,
content: cardData.content,
tags: cardData.tags,
category: cardData.category,
isAIGenerated: true
});
const card = await newCard.save();
res.status(201).json(card);
} catch (error) {
res.status(500).json({ message: 'AI生成失败', error: error.message });
}
});
module.exports = router;
EOF
```
这一步需要回头打开 server.js，在现有路由体系中挂载刚刚准备好的 AI 相关路由，确保请求能够正确分发。
```
nano server.js
在卡片路由后添加：
app.use('/api/ai', require('./routes/ai'));
```
路由接入完成后，最后进行一次完整的接口联调，通过真实请求验证生成流程、响应格式和错误提示是否符合预期。
```
测试基础路由：
curl http://www.ainotecard.com/api/test
{"message":"服务器运行正常"}
注册新用户：
curl -X POST http://www.ainotecard.com/api/auth/register -H "Content-Type: application/json" -d '{"username":"testuser","email":"test@example.com","password":"password123"}'
{"message":"用户注册成功","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZTJjZGQ2ZmI1ODYwY2RhOThhZGMyNiIsInVzZXJuYW1lIjoidGVzdHVzZXIiLCJpYXQiOjE3NDI5MTcwNzgsImV4cCI6MTc0NTUwOTA3OH0.S2NHeyIgbFMgVjTY0UquE6pYtZrMLmtjjOmxFMj1P14","user":{"id":"67e2cdd6fb5860cda98adc26","username":"testuser","email":"test@example.com"}}
尝试登录：
curl -X POST http://www.ainotecard.com/api/aun \logi
>   -H "Content-Type: application/json" \
>   -d '{"email":"test@example.com","password":"password123"}'
{"message":"登录成功","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZTJjZGQ2ZmI1ODYwY2RhOThhZGMyNiIsInVzZXJuYW1lIjoidGVzdHVzZXIiLCJpYXQiOjE3NDI5MTcxMDIsImV4cCI6MTc0NTUwOTEwMn0.56xTLFmO6nz9E_j0kBuWlWfrogux_ZQRpsCbGBOiI4U","user":{"id":"67e2cdd6fb5860cda98adc26","username":"testuser","email":"test@example.com"}}
登录成功后，您将收到一个包含 token 的 JSON 响应。请保存这个 token，我们将在后续请求中使用它。
使用 token 创建一个卡片：
curl -X POST http://www.ainotecard.com/api/cards \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZTJjZGQ2ZmI1ODYwY2RhOThhZGMyNiIsInVzZXJuYW1lIjoidGVzdHVzZXIiLCJpYXQiOjE3NDI5MTcxMDIsImV4cCI6MTc0NTUwOTEwMn0.56xTLFmO6nz9E_j0kBuWlWfrogux_ZQRpsCbGBOiI4U" \
>   -d '{"title":"测试卡片","content":"这是一个测试卡片的内容","tags":["测试","示例"]}'
{"user":"67e2cdd6fb5860cda98adc26","title":"测试卡片","content":"这是一个测试卡片的内容","tags":["测试","示例"],"category":"未分类","isAIGenerated":false,"_id":"67e2cf29fb5860cda98adc29","createdAt":"2025-03-25T15:43:37.241Z","updatedAt":"2025-03-25T15:43:37.242Z","__v":0}
获取所有卡片：
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZTdGVzdHVzZXIiLCJpYXQiOjE3NDI5MTcxMDIsImV4cCI6MTc0NTUwOTEwMn0.56xTLFmO6nz9E_j0kBuWlWfrogux_ZQRpsCbGBOiI4U" \
[{"_id":"67e2cf29fb5860cda98adc29","user":"67e2cdd6fb5860cda98adc26","title":"测试卡片","content":"这是一个测试卡片的内容","tags":["测试","示例"],"category":"未分类","isAIGenerated":false,"createdAt":"2025-03-25T15:43:37.241Z","updatedAt":"2025-03-25T15:43:37.242Z","__v":0}]
使用AI生成卡片的命令如下：
curl -X POST http://www.ainotecard.com/api/ai/generate \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZTJjZGQ2ZmI1ODYwY2RhOThhZGMyNiIsInVzZXJuYW1lIjoidGVzdHVzZXIiLCJpYXQiOjE3NDI5MTc5MDMsImV4cCI6MTc0NTUwOTkwM30.2GrrqC3Sl30ovU2f58ca4SyKQ0plRFrVUNWXu1tqdo8" \
>   -d '{"prompt":"人工智能的基础知识","template":"summary"}'
{"user":"67e2cdd6fb5860cda98adc26","title":"摘要: 人工智能的基础知识","content":"原文: 人工智能的基础知识\n\n摘要: 这是对上述内容的简明摘要。包含主要观点和关键信息。\n\n关键点:\n- 第一个要点\n- 第二个要点\n- 第三个要点","tags":["AI生成","summary"],"category":"自动生成","isAIGenerated":true,"_id":"67e2d12bfb5860cda98adc2d","createdAt":"2025-03-25T15:52:11.362Z","updatedAt":"2025-03-25T15:52:11.363Z","__v":0}
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_53f980fa9af2f89958493b578c7392ca.png>
## 当前已上线的接口清单汇总：
1.  GET /api/test - 检测服务端是否在线
2.  POST /api/auth/register - 新建账号
3.  POST /api/auth/login - 账号登录
4.  GET /api/cards - 拉取当前用户下全部卡片
5.  GET /api/cards/:id - 拉取指定 ID 的卡片详情
6.  POST /api/cards - 新增一张卡片
7.  PUT /api/cards/:id - 修改指定卡片内容
8.  DELETE /api/cards/:id - 删除指定卡片
9.  POST /api/ai/generate - 调用 AI 模型自动生成卡片
# 五、为站点开启 HTTPS 并部署 SSL 证书
在接口联调阶段确认：
```
curl http://域名/api/test
{"message":"服务器运行正常"}
但是curl https://域名/api/test
curl: (7) Failed to connect to 域名 port 443: Connection refused
```
HTTP 协议下的服务已经跑通了，接下来要做 HTTPS 加密访问，就得给站点装上 SSL 证书
打开宝塔面板，进入 网站 栏目，找到对应站点，点击 SSL 证书，当前显示未部署状态
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_454900b459e44a033367688531db35af.png>
进入证书管理页后，选择 Let's Encrypt 进行免费证书申请
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4b3e3a9faffdd6484af9f9b8461c5a97.png>
验证方式选用 文件验证，点击 申请证书 按钮提交
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2d8eeab217bd99d5eae64796bc212af2.png>
证书申请成功后，勾选 强制 HTTPS 重定向，并打开 到期提醒功能，证书周期为 90 天，到期前会收到通知来此续签，最后点击 保存
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_78d4328a6e51ae317a23d1a566a139d2.png>
SSL 配置完成之后，再次用 https 域名去访问接口，验证是否正常
```
curl https://域名/api/test
{"message":"服务器运行正常"}
```
# 六、复盘总结
1、Cursor 的能力远不止写代码，它在环境搭建、服务器配置、部署指导方面的表现也非常靠谱。特别是它自己生成的代码，后续的服务器适配它几乎能一气呵成，你只需要给肯定反馈，把问题丢给它让它直接输出方案就行。
2、不过像宝塔面板的默认配置、隐式规则这类只有实操经验才知道的细节，Cursor 很难主动感知到，于是会出现反复试错却找不到方向的情况。这种时候就得及时向有经验的人求助举例：nginx 反向代理的问题，我和 AI 来回排查了两小时毫无进展，放到航海群里问，两位朋友很快就锁定了真正原因。
3、想把 Cursor 用顺手，关键在于提前拆解任务。先做整体规划，再拆成模块和步骤，并且用文档做好记录存档，这样协作效率会大幅提升。