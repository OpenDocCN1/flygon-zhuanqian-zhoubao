# 安卓也能搞定 AI 智能体：小红书笔记抓取 + 二次创作全链路自动化实操
# 为什么要做这套方案
苹果阵营早已用快捷指令配合飞书多维表格实现视频文案一键导出，安卓用户完全不必落后。文章将演示如何借助安卓端的自动化应用，搭建一套从笔记采集到内容再生的一体化流程，让创作效率实现质变。
# 你将得到的能力
*   学会 MacroDroid 在安卓系统上的宏任务搭建方法
*   掌握在 Coze 平台搭建小红书笔记解析智能体的完整思路
*   知道飞书多维表格如何接入自动化流程
*   熟悉飞书机器人流程的搭建技巧
*   懂得使用飞书多维表格自带的 AI 插件功能
# 准备清单
1.  飞书电脑版
*   获取方式：https://www.feishu.cn/download
2.  飞书机器人流程
*   账号条件：
*   个人版账号即可使用
3.  扣子 Coze 账号
*   官网：https://www.coze.cn
*   登录方式：手机验证码
*   当前由 Coze 智能体发布的飞书多维表格字段快捷插件每日调用次数约 200 次，专业版是否放宽未知。若达到上限，可先用我已搭建的 Coze 流程调用字段快捷插件的方式过渡。
4.  MacroDroid 安卓自动化工具
*   系统要求：
*   Android 7.0 及以上
*   MacroDroid 版本：5.5.24
*   安装方式：
*   Play 商店：MacroDroid - Device Automation
*   官网直链：https://www.macrodroid.com/
*   权限设置：
*   悬浮窗权限，用于界面操作
*   后台常驻权限，保持运行稳定
*   使用建议：
*   开启全部必要权限
5.  小红书 App
*   状态要求：
*   保持登录状态
# 搭建全景
## Coze 小红书文案提取智能体搭建
构建文案处理的智能中枢
### 智能体基础配置
1、进入扣子后，点左上角 ➕ 新建智能体，在弹出的窗口里点击【创建】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9c9c95b0ab45d1a10f71120af3bd74df.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_293c58d2ea5ee948748292424fc9ca81.png>
2、为智能体填写基本信息：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_196bfd571cbf9a53b9d88ff41e6c9198.png>
3、将智能体类型设为【单 Agent 对话流模式】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e799c20ec5bf05cb1eaa8010d3705f4c.png>
4、点击【点击添加对话流】新增对话流，再点【创建对话流】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3e9ec2feb3d6865235ad8fa61cc18252.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_983d751878a77c1df52d7d554f70801f.png>
### 工作流细节配置
1、填写对话流信息：
对话流名称：rednote_extract
对话流描述：小红书笔记信息提取
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cf48a6b6bb1fe372e38f642b263b0911.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_efd15f1638931be36be72c52db2e09c0.png>
2、起始节点保持默认，将鼠标移到起始节点右侧中部会出现 ➕，点击 ➕ 新建插件节点：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7f4501a37557d03f4b0af83359840c6c.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_56ea9b653d1f050e08e8659a85dbafd1.png>
3、搜索工具集合，点击 > 展开后选择【get_rednote_info】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_da33294eeb2c7ee30f3bf64c99b2f6b5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4a64a924bb8f8fbc3e2ebed6fb225576.png>
4、对【get_rednote_info】节点进行设置：
节点名称：get_rednote_info
输入设置：
content：引用【开始】节点的【USER_INPUT】
cookiestr：按需，可不填
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0f30aea4dafeeed1d12d29803bb11cae.png>
5、新增选择器节点：
节点名称：选择器
分支条件设置：
如果分支：
条件1：【get_rednote_info】节点的flag 等于 1
条件2：【get_rednote_info】节点的type 等于 video
两个条件为与关系
否则如果分支：
条件1：【get_rednote_info】节点的flag 等于 1
条件2：【get_rednote_info】节点的type 等于 normal
两个条件为与关系
否则分支：
无需设置
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2e8d500a5adce71df001052b609eba81.png>
5.1、如果分支下挂载【字幕获取】插件节点：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c3eac1794f65989771e49d0d3e201ff2.png>
节点名称：generate_video_captions_sync
输入设置：
url：引用【get_rednote_info】节点的video/url
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_07db8b8231657762d28d89c6328edfb3.png>
5.2、否则如果分支挂载代码节点：
节点名称：设置asr空内容
输入设置：
无需设置
输出设置：
asr：string类型
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_41f159dd4b19c4944c10d8d252b7a663.png>
代码(Python)：
```
async def main(args: Args) -> Output:
params = args.params
asr = ""
# 构建输出对象
ret: Output = {
"asr": asr
}
return ret
```
可复制代码：
5.3、否则分支挂载代码节点：
节点名称：设置空内容
输入设置：
无需设置
输出设置：
collectedCount、commentCount、likedCount、shareCount、urlDefault、notetype、desc、userId、avatar、nickname、video_url、title、ipLocation、lastUpdateTime、tag_text、asr：均为string类型
imageList：Array类型
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_035fe6a1ea99540c1569a5be9b4ead64.png>
代码(Python)：
```
async def main(args: Args) -> Output:
params = args.params
collectedCount = "无法获取"
commentCount = "无法获取"
likedCount = "无法获取"
shareCount = "无法获取"
urlDefault = "无法获取"
notetype = "无法获取"
desc = "无法获取"
userId = "无法获取"
avatar = "无法获取"
nickname = "无法获取"
video_url = "无法获取"
title = "无法获取"
ipLocation = "无法获取"
lastUpdateTime = "无法获取"
asr = ""
imageList = []
tag_text = "无法获取"
# 构建输出对象
ret: Output = {
"collectedCount": collectedCount,
"commentCount": commentCount,
"likedCount": likedCount,
"shareCount": shareCount,
"urlDefault": urlDefault,
"notetype": notetype,
"desc": desc,
"userId": userId,
"avatar": avatar,
"avatar": avatar,
"nickname": nickname,
"video_url": video_url,
"title": title,
"ipLocation": ipLocation,
"lastUpdateTime": lastUpdateTime,
"asr": asr,
"imageList": imageList,
"tag_text": tag_text,
}
return ret
```
可复制代码：
6、添加变量聚合节点，具体配置如下：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_20c9ee45253e702d1d4991f4bc52b195.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b789b18e6d19f11430b9bec41f9b8f8a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_050a306cd369f6fabe9de064319e177d.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5002ed43f9541f6eb7ab2c07668cd52f.png>
7、设置结束节点，选择返回变量：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fc0e2859b1286947ecbad2dd07c816ee.png>
8、拿一篇笔记链接做验证，点击【试运行】：
```
https://www.xiaohongshu.com/explore/67daa906000000001e007d6d?xsec_token=AB160KrsrDX4GWgUibp6cRQ7qjDlyWLEHJ94-TsJAS_yM=&xsec_source=pc_feed
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ea66cead653097de98e019480685fe4a.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8adb1367c720602bd88c9f0715ed146e.png>
运行通过即工作流可用。
9、发布工作流，点击【发布】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dc6cbcd0158c82bdf920acc356a7aa90.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c7d045c46cb35cc8e5c547b25f78248a.png>
### 开场白设置
开场白是否填写影响不大，因我们主要通过插件调用该流程。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e5b872a480e81d81da200398ccf1e99a.png>
## 创建个人访问令牌
工作流完成后即可创建个人访问令牌。
### 令牌获取流程
需要在扣子平台先获取令牌。
步骤：
1.  登录 Coze 控制台【https://www.coze.cn/】，点击左侧菜单的【扣子API】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fa2925a4a0fed14fcb451828d5c0446d.png>
1.  进入【授权 ➡️ 个人访问令牌】页面，点击【添加新令牌】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b6c446e35f2446cd1068dba803da9e97.png>
1.  输入令牌名称，建议与用途对应，设置有效期、勾选【工作流】权限、选择工作流所在空间，最后点击【确定】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2d9f9e213b92fecb57865b8b03bd4da2.png>
1.  保存生成的 API key，仅展示一次，请妥善保存：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_66b2120c9a8ceb06d79fdc3317dc91e0.png>
将令牌信息存本地，后续飞书多维表格会用到。
注意事项：
*   令牌权限范围需包含工作流操作
*   外泄令牌会带来数据安全风险
## 飞书多维表格设计
### 创建多维表格
1、在飞书个人空间新建多维表格，删除多余字段，将第一列命名为【笔记信息】，名称可自定义：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_21851e443c2d2a3abbcb3e4c8199ad9a.png>
2、新增字段，标题设为【小红书信息获取】，搜索字段快捷插件【扣子工作流调用】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9d923a94277323556052937a56538acd.png>
### 字段快捷插件配置
1、把前面生成的扣子令牌填入插件的认证令牌，工作流 ID 可在编辑工作流的链接中获取，workflow_id 后面的值即为 ID，参数字段指向【笔记信息】列：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_562b4ccac911950a2510a0834600f806.png>
2、其它配置：
参数名称：USER_INPUT
请求模板：
```
{
"CONVERSATION_NAME": "Default",
"USER_INPUT": "$$USER_INPUT$$"
}
```
$$USER_INPUT$$为占位符。
输出结果1：desc
输出结果2：asr
输出结果 x 表示取工作流的哪个变量，最多取 2 个，其余通过完整响应获取。此处主要取视频语音文案，视频作品一般无标题，故未取。
获取更多信息：全选
自动更新：开启
3、点击【确定】保存配置：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7f8d7ce3910153bae9934c4812fb4fff.png>
4、点击【仅保存配置】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e187f430ac006cfec7f115ad0b91195d.png>
## 飞书机器人流程设计
设计机器人流程把内容写入多维表格。
1、电脑打开飞书，搜索【飞书机器人】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4797d42276ae67c7f5e10f7b0dfbf951.png>
2、点击【新建应用】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b240bdce809363ee4c4402d1dedb07fa.png>
3、设置应用名称、描述、图标，点击【确定】创建：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5eb714c4b5b0bfc704c9b4ab1094a8aa.png>
4、点击【创建流程】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e850b5bbbdc817965f40719a1f6bc9d8.png>
5、触发器选择【Webhook 触发】，保存好【Webhook 地址】，后续会用到：
参数设置：
```
{
"content":""
}
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5050235e4b478b80fec9fe13c8b0b27a.png>
6、操作选择【新增多维表格记录】，数据表选择我们新建的多维表格的数据表，注意不要通过多维表格名称搜索，无法展开，只能操作云空间多维表格：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3aa28849469aa716ef07cec65fde49b6.png>
字段选【笔记信息】，值选 Webhook 触发的 content。
7、点击【启用】，流程命名为【小红书笔记转存】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ff41ce34b59a516075ef420aa7d46f82.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cbfef30d6694a3b17fb0474baf60b5f6.png>
8、点击【发布】发布流程：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_74ad7c73614076594b4012edfd318367.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a77795c12675641c1a81dddebc0ba2d1.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e4adc1c20d3456a65ccbaa0f7b989a1d.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_51daae03584d8baf615dd7100fb34289.png>
个人版直接免审。
## MacroDroid 流程设计
安装完成后进入配置。
### 新建宏
1、打开 MacroDroid 应用，点击添加宏：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_76547dbb3e4c0327d192d49b696f5154.png>
### 设置触发器
1、设置宏名称后，点击触发器右侧 ➕，选择用户输入的【浮动按钮】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d3024bc2827565143b9257142172e552.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0d31d457c6ee7a0cbda2844d0df87efb.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_707a9ce14e28241a5a9189d4656ed3c8.png>
2、开启显示在其他应用上层的权限，点击左上角返回：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_78580875f60c6f58e06e1cd83c338b87.png>
3、按喜好设置浮动按钮样式：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8edf89eabe14edd7a3f3eaf599d42982.png>
### 设置动作
1、点击动作右侧 ➕，新增【设置变量】动作，在【变量➡️设置变量】中选择【提取文本】，点击【确定】：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7eca9c7f88c8ff6317d2bcd89c9f9bc3.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_981cecb4f0580f163bb0d0272787b6e5.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d970cc3538e31a4776d8cf24a61063db.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d6e488f8c7326ad649e3dbd74c712dbf.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3d2939795d62c8cac1db45ed09a2cd13.png>
2、新增如果动作，在【条件/循环】中配置：
条件1：
```
https://www.xiaohongshu.com/explore/
```
条件2：
```
http://xhslink.com/a/
```
今天来分享一个很实用的自动化玩法：把小红书笔记的关键信息，通过宏工具和飞书多维表格自动存下来。整个过程用到 MacroDroid、飞书多维表格和扣子工作流，配置一次之后，用起来非常方便。下面直接开工，前面两步已经准备好，我们从第三步开始。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0ece3d061638c5a7b40a7abee7e88de7.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e6d48045e7b02afa450a028b8e984ac2.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3dbb23dc33726688c1e41d6f4828135f.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_70b66a98cabc1db8f23eb5ba097e38b4.png>
第三步：先添加一个“如果”条件，然后在该分支下找到“添加‘否则’子句”，把判断结构搭好。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d5cde2e602e530402f07b84b30eab73f.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f8fbef42e1b6ac3bfa1c52d93eb25e2d.png>
第四步：接着在“如果”分支里添加子动作。选择“网络互动 → HTTP请求”，把请求方法改成 POST，网址填成刚才复制好的 Webhook 地址。别忘了勾选“完成后才能后续动作”，再往下滚动，把“将 HTTP 响应保存在字符串变量中”也选上。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_db3ebe60da23917e754b4dad987772af.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f035db4debd0e2935d7c63d6617518c7.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3a192518593bfe4e034617aa08fdba68.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_86f26976658e3980ce6876bf17bfb6f0.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6d4b8482f759851abb6a8c766195abf3.png>
第五步：设置请求正文。内容类型选 application/json，正文模式选择“文本”，然后把下面这段内容填进去。
```
{
"content":"{v=分享内容}"
}
```
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f4469383867626681cdbb215c17ad003.png>
第六步：继续在“如果”分支中加入子动作，选“网络互动 → JSON解析”，把上一步拿到的响应数据解析成可供后续判断的结构。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a2b6aaeb8923b67f0c42d206a33c4801.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_32ac98bdf07145f81ae90d3096130672.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c0091a1b2c1c80a3efe2863d0a4f5153.png>
第七步：在同一个“如果”分支里，继续追加一个“如果”子动作。在“条件/循环”区域新增条件，来源选择 MacroDroid 的变量，手动定义并填入 [msg]。接着配置 msginfo[msg]=success，这样后续就能根据这个值判断是否成功。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_66c9d6476f19f2ffa93a3fa0107127bc.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ffc84e4be2680db7169545cebbfc27c8.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ec36fa332559296f0df9d21008eb96cd.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f172a6ebf6543634005a067221b2cc59.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aed20b030f611dec5aec844e7329a344.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b5d5dc4e464cfddf18161ec4564fbe12.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_cfe51385351749aa12572e4371918f75.png>
第八步：这次要给“如果”加上“否则”子句。然后在“如果”和“否则”下面分别设置“弹出信息提示”，用来反馈处理结果。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8b4c05a62831dcb8650d94737986c301.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_18212925d0c60d4a6c2274d329d85736.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_da5651f2d7222f84c1bab073297493a1.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f169e3a8f4be1faeede2304367cd9ede.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b7afb77a91fd956aa020231fe239c71b.png>
第九步：最外层的“否则”分支里，同样放置一个“弹出消息提示”，这样不管成不成功，都会给到明确提示。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a8947a7777b9608e3406bc6f4f066eea.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_30ee102d4df04f0401195a04d74aeb6e.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ae728d5fe3447064df3eae3bcd122031.png>
第十步：配置完成后就可以先跑一遍测试，记得一定要授权通知权限，否则弹窗可能不显示。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f9e3ce19d6fedcffea85c5c071231e99.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6d81665f261e8ea18b84bbd839e03f93.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_882f41cec709f94e14028907eab8747c.png>
第十一步：测试完去飞书多维表格里看看成果。在 MacroDroid 里点击浮动按钮，刚才的数据应该已经写进表格了。注意，数据是追加在最后一行，所以建表时一定要把多余的空行删掉。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aa62725c54e4a376e947dd98458e5edd.png>
第十二步：测试过程中发现一个问题——只有点浮动按钮时才有效，从小红书复制内容时剪贴板居然是空的。解决办法是新增一个“剪贴板刷新”动作，让系统先读取剪贴板，再交给后续流程处理。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_fa84f8c83118d18a1165e21f5739c5ab.png>
## 展示视频
这里放一个实际运行的展示视频，方便你直观感受整个过程。
## 信息提取
注意到一个问题：插件默认只能输出两个变量的值。如果响应里还有其他字段想要拿下来，可以借助“信息提取”字段捷径插件来处理。具体做法如下：
先新建一个自定义字段，比如“作品标题”，然后搜索并添加“信息提取”字段。在“选择需要提取的字段”中，选中扣子工作流调用插件输出的“完整响应数据”，提取信息填写“提取"title"的值”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_de0824b5713761fc42fd1ea29b9b0922.png>
接着再新建“作品封面”字段，同样选择“完整响应数据”，提取信息填写“提取"urlDefault"的值”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_12c8d49d63123247254afdc494d873a4.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_97885c697f1d526600130d31f14cd255.png>
再来一个“作品话题”字段，操作同上，提取信息写“提取"tag_text"的值”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_87e9846204402eca0643b05843f178f6.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_19fdd6167fee82a5258b814db05e524b.png>
然后新建“作者”字段，提取信息填“提取"nickname"的值”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_45b6f325f23d27e2c419d153d935a6cd.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4076df7c432699144027754ae1ab1313.png>
最后是“视频地址”字段，提取信息填“提取"video_url"的值”。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_95e68e6323a5c27a5a4c1ffd05dab907.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d399f9822127c67bdc2f2e11b6ac57aa.png>
信息提取就是这么简单，想拿哪个字段就写哪个字段的提取规则，完全按自己的需求来。
## Deepseek AI二创
用 DeepSeek 做二次创作本身不难，真正决定效果的是提示词写得好不好。这里容我当一回标题党，具体怎么发挥就看大家的想象力了。
# 思路扩展
这个方法不仅能提取小红书笔记，改成提取抖音、B站视频的内容也完全可行。相信聪明的小伙伴还能开发出更多新玩法，到时候记得来分享！
# 附录
## 小红书笔记转存宏脚本
把写好的宏脚本分享给大家，直接在 MacroDroid 里导入就能用。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_af3c35badfcd60e27ee755b70d55e015.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_02037046e67a5b4690ed1ba70054b2e2.png>
不过要提醒一句：导入脚本时会清除当前已有的所有宏。如果你已经有其他宏，切记先备份一份，或者手动创建一个“小红书笔记转存宏”。