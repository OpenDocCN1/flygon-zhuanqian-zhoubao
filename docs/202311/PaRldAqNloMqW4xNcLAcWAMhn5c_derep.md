# ('自动监控+加图表分析 对标数据', (2, 17))

做抖音一年，我前前后后参考过不下几十个对标账号，说上百也不算夸张。每天最头疼的就是：他们什么时候发作品？作品什么时候爆？今天这几十上百个号里，谁的视频火了？我能不能在第一时间跟上去？于是我就琢磨着，能不能有个工具，帮我定时去抓对标账号的点赞数，比如每隔一小时记录一次，然后自动整理成像Excel图表一样的可视化结果。

比如下面这种表格效果：
![](img/a5f60c2ee38cd0c70370691c391dff66.png)
![](img/f316a9f0b3ec1b0b23fc9b9e1c3e946a.png)
![](img/8b37a584b3994ab2ce470fc18482346a.png)

先亮一下我的整体方案流程图（工具：影刀RPA + 飞书多维表格，两个都是免费的）。

第一步，用影刀写个脚本，让机器人定时（或者每隔一段时间）去抓取对标账号的数据。脚本地址也分享给大家：https://api.winrobot360.com/redirect/robot/share?inviteKey=12838d2e26f47359（密码2023）。

在正式开始前，需要先准备一个Excel配置文件：
1. 在C盘根目录下新建一个名为【抖音配置文件.xlsx】的文件：![](img/ab03d22947c290739de947601b4ede8c.png)
2. 在Excel里把需要的工作表建好：![](img/cc5d35af66bbcc1ebce0f075357b8557.png)
3. 配置对标主页：一行放一个对标账号，注意中间不要留空行（我没有留过空行，所以中间空行会怎样我也不清楚）。![](img/941424da2b7eba0d8a0edf0660f4ef19.png)
4. 【记录】页是本地数据备份，脚本会自动写入，不用手动管，但必须把这个页面提前建好。
5. 影刀还有一些设置项，其余没啥了——官方也有个多维表格ID的示例文档：https://ydrpa.yuque.com/org-wiki-ydrpa-xtutvv/ga4dm6/ir3mh6orhy4ib7zf ![](img/f4ba95cf920c7686c234b225492c56c4.png)
6. 特别提醒：因为影刀在不同系统版本上可能有不兼容的情况。我自己用的系统版本如下，文末也会附上影刀代码：![](img/d0fcd64451d712cb354f775d874f4e3e.png)
   如果你运行脚本时遇到类似下面的报错，第一次先给C列中有数据的位置加一个时间（注意不能是未来时间，否则脚本就不抓取了）。![](img/4711a29018b7a5754ffb25d4eca0a55c.png)![](img/56b729cb47f96bfc8d026851e1dcce73.png)

第二步，就是让影刀把抓到的每一条数据，通过飞书的API接口![](img/8b230830dfdb604de1f8c248bb6ccf06.png)传到多维表格里![](img/467b73a4053e4fb46ccd86edffd7f9c1.png)。接口地址是：https://open.feishu.cn/app/

对接前需要先做一些准备工作：
1. 去飞书开放平台开放相应权限。![](img/8e504b9f7e40fa59b96d4bf631aff2b1.png)
2. 新建一个应用。![](img/4a3f5f4a7b0180ba7ea8eabe2b5d1c03.png)
   把自己应用的ID保管好，后面要填到影刀里。
3. 开通记录的权限。![](img/b702d0bf1ad01049e15fd9283de7e9c0.png)
4. 发布应用版本。![](img/8c22bacba431cd6f8eef68d0a8ff2b0a.png)
5. 在自己的飞书里创建一个多维表格。![](img/ae755159cadd3b9957355bdbaf95a8a3.png)
6. 把这个多维表格添加到刚才创建的应用里，![](img/2bf4452fc65eb6961bb8e94704b27e50.png)![](img/3e51ee8deb358b2dccf993491e826ee1.png)![](img/cd78d27591f319a4e0cbf8d87a36c15b.png) 并授予“编辑”权限。
7. 等影刀机器人自动上传数据之后，就可以去飞书的仪表盘里添加图表了![](img/d2a2bddc9550af92a4ca2ae4867c1b71.png)。不会图表的同学，可以自己去补一下Excel图表的知识。
8. 在多维表格里建表的时候要注意字段格式的设置，![](img/54607ec1d3e64fab56db1ddcf785939d.png)![](img/977ae1e31bc19184edf32dac32f9d6f1.png)![](img/1ffcc8b74e97065fd8e9390efe6c4cee.png)![](img/9af02135648df901be2a72de1d9cf401.png)![](img/9766a9217ef052eb0a98f960ac1c68be.png) 除个别特殊字段外，其余全部设为文本格式。
9. 接下来就自由发挥了，你可以查任何想看的数据。下面是我自己在用的一个数字仪表盘，每个数字都可以点击，点进去就能看到对应的明细表：![](img/995ed6efe33c9105823ab42b3877199b.png)![](img/86ac5d9db593d34bd8c114b666f04104.png)

这样一来，对标账号的数据是不是就一目了然了？看着非常安逸。

第三步，附上影刀的完整代码。代码包括以下几个流程：
- 主流程：![](img/225e7260d1801216359b5fc90d10aa97.png)![](img/5e3c2b27738bb524b795dccfbd528a16.png)![](img/1db65a27b5be45a622aa2163988a7e08.png)![](img/e746a88cff096ed73cd7bdbfdda99c55.png)![](img/7cf72fcf966bdcd671da2b8b9508e85d.png)![](img/050011d1938dced9c1932b6f70c82743.png)
- 监控流程：![](img/5c43062bbad2f0546c9603983a93c8e2.png)![](img/8a02cbca8863c702c5d1809a41e72aee.png)![](img/ffdc296464865cf7d63c4d4373c3b51d.png)
- 检查微信是否存在流程：![](img/fb9705d6ffd85581287441e153ef9e14.png)
- 配置流程：![](img/36b8f5f423285fb82a8677af7c12f69a.png)![](img/49d2e2fdaf24d0907935a49f60b8e4df.png)![](img/3e053df0851e85ecfbe3d515c193ddec.png)
- 筛选流程：![](img/7981eeed3e11ab9cf86726919f3b4ed1.png)![](img/d93aabaaf9bb6d4f0cd04dc121d78e99.png)![](img/c9016cefe815c2ae794878e6ae68650c.png)![](img/c479ed7fc8e8909a98fc895b4b39bf73.png)![](img/db99c61f5d13755b02a122147e146d62.png)![](img/448086155411a7a51841aef7292b3115.png)![](img/26676bd22341f5210f4a195d3934fad1.png)
- 微信发送流程：![](img/3dc61f265a50d5043f32ee424ba78695.png)![](img/7d285644223c1cb39e194e6e20efa93e.png)

至于原理：最早这个方案是设计成发微信通知的，后来我试了飞书，发现比微信好用太多，所以微信部分如果你会写代码，可以自己删减一下。

第一次分享，排版不周，大家将就着看吧，希望对你有帮助。