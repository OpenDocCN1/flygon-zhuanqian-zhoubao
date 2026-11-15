# 结合本地知识库，让Deepseek帮你出题
老师们是不是都有这样的感觉：出一套卷子，简直是“耗时大户”？我问过身边不少当朋友，他们坦言，平时一份试卷往往要好几个人合力，前后折腾好几天才能定稿。最近我试了个新路子——让 DeepSeek 搭上本地知识库，把出题这事儿变得轻松不少。今天就把完整的玩法整理出来，给大家一个参考。
这篇教程主要分成四块：
1.  Cherry Studio 的安装，以及怎么和 DeepSeek 连起来
2.  知识库的搭建与配置
3.  目前存在的短板，以及对应的补救办法
4.  知识库的两种实战用法
如果你已经装好了 DeepSeek，也熟悉 Cherry Studio，可以直接跳到后面的使用方法部分。
# 一、先把 Cherry Studio 装好，接上 DeepSeek
## 下载安装 Cherry Studio
*   官方下载地址：https://cherry-ai.com/
*   点【下载客户端】，跳转后选择下载；嫌慢的话，也可以走网盘渠道。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a3482ecb1e46da0e4f814957726989ba.png>
*   装的时候留个心眼：别放系统盘，其他盘随便放。
## 拿 API_KEY（以派欧云为例）
*   先去派欧云注册账号：https://ppinfra.com/user/register
*   新用户注册会送 5 元代金券，大概相当于 500 万 tokens 的额度
*   填邀请码【2OD5AF】，还能再多拿 15 元代金券
*   接着完成实名认证
*   登录后，点右上角的头像，选【账号管理】
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dfc1595d0f12151c4037b7c59e27195d.png>
*   在【账号管理】左侧菜单里找到【实名认证】，按指引走完流程
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a2ecf354f3f07a579435b2ad55cca667.png>
*   搞定认证后，去拿 API_KEY
*   在左侧菜单点【API密匙管理】→【创建】
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a198d5f494bbf264e3eb3f29fb66c322.png>
*   弹窗里随意填个名称，点确认
*   接着会再弹一个新窗口，马上点【复制】——这一步非常关键，因为密钥只显示一次，忘了复制就只能删除重建了。复制完点【我已保存】关掉窗口
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_540fa9e6634c56d59f02291a174cda0d.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aebb8a50cca454e278d7ff7fcd379a8c.png>
## 在 Cherry Studio 里配置服务
*   添加派欧云服务
*   打开 Cherry Studio → 设置 → 模型服务 → 添加 → 服务商名称填“派欧云”→ 确认
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b248b17d6a953a10bcfb8b4b7336e07b.png>
*   配置模型参数
*   先把刚才复制的 API_KEY 填进去
*   再把 API 地址粘贴过来：https://api.ppinfra.com/v3/openai
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6180039230fc9623a933f89b784c92b8.png>
*   添加模型
*   点“管理”，把 deepseek-r1 模型加进去
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_928475a741448e6c1f7a5195d0a16d09.png>
搞定这一步，前期准备就绪。Cherry Studio 还兼容不少其他平台，套路大同小异，感兴趣可以自己研究。
# 二、知识库怎么搭、怎么用
## （1）搭建步骤：
### 打开 Cherry Studio → 知识库 → 添加
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1deefe72b903ea832f88f6dd56a50216.png>
### 填个名称 → 选嵌入模型
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6b8b5554ad337d1f72922f38931e53bc.png>
#### 嵌入模型是干什么用的？你可以把它想象成一个“文件处理专员”，把上传的资料转成数据存起来，方便后续对话时调用。
#### 派欧云没有提供嵌入模型，所以要再申请一个平台的 API，推荐硅基流动，申请流程和上面差不多。
#### 不同平台提供的嵌入模型不一样，如果某个平台没有，可以同时开启多个平台的服务。
### 上传资料
Cherry Studio 的知识库支持上传文件、目录、网址、网站、笔记等；这次主要用前两类，所以就重点讲这两类，其他的可以自己试。
*   文件：支持单个文件上传，可直接点击添加，也能拖拽进去；文件内容改动了，点刷新就能同步更新数据库。
*   目录：把整个文件夹里的文件都传进去；文件夹里有增删或修改，点刷新就会自动更新。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4f2aa58875216e71ed83426ba17970d9.png>
## （2）使用步骤
### 打开 Cherry Studio → 助手 → 添加助手 → 默认助手
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_35697bc5e1dd430876a8e34d3b725285.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_87e8e23ab2beeca744bf6c4c9daddb86.png>
### 右键 → 编辑助手
在编辑页面改好助手名称（提示词可写可不写），然后找到知识库设置，选中你要用的知识库
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5f03041c2de3f8c23acc1e0e91badfec.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_87b60777a581cf1d007eb61a8e222873.png>
### 像平时一样在对话框里聊天
知识库配好之后，出题就变得很简单了，把需求说清楚即可。需求表达得越具体、越详细，DeepSeek 给出的结果就越贴合你的预期。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_15c330a57288284bf067dd8294ddedab.png>
# 三、现在的短板，以及怎么补
### 短板1：知识库只能处理纯文字，扫描件和图片没法直接读
解决办法：先让 Kimi 把文件内容提取出来，存成 Word 文档，再传到知识库（Cherry Studio 可以直接唤起 Kimi，不用另外开网页）
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_60de8f0ffbd7c20eca763d23653bc173.png>
#### 参考提示词可以这样写：
请你把文件中的内容完整的转换成文字，顺序不变，不要markdown格式
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6af00594a3691c5dc581a9b3cbb7c167.png>
### 短板2：试卷里的图片（漫画、图表等）识别不了，也提取不出来
解决办法：排版时自己找原图贴上去；可以借助助手快速定位到原文
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ff6104687cd1b3974234329339c1fbe3.png>
# 四、知识库的两种用法
我根据 DeepSeek 的工作方式，把它分成了两个角色：组卷高手和出题大师
## 组卷高手
说明：让 DeepSeek 扮演“组卷老师”，按你的要求，从知识库里挑题目，拼成一份新卷子，不需要它自己编题。
优点：速度快、对知识库整理要求低、回答质量挺高
缺点：灵活度一般，原创性不足
适用：重要程度比较低的考试，比如单元测试、月考、模拟考
### 参考提示词：
请你从【XXXX（文件夹名称）】中，挑选XXX道【题型】，组成新的试卷。题号从X号开始，不要markdown格式，不要标注来源。
（提示词不是死的，只是给大家一个思路。前半段用来限定选题范围，后半段是为了方便后期排版。你可以根据实际测试调整出更适合自己的写法）
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a1ef0844b5518cb47cc5492318029203.png>
这种玩法很简单，只要往知识库里多传一些试卷，然后限定范围就行。其实这种场景用 deepseek-V3 或其他大模型也没问题，因为不需要太多思考和推理。
## 出题高手
说明：让 DeepSeek 扮演“出题老师”，按你的要求，依据知识库里的出题规范和考察知识点，自己原创题目。
优点：充分发挥 DeepSeek 的推理能力，题目原创度高
缺点：对知识库内容的质量要求比较严
适用：对题目原创度有要求的考试
### 参考提示词：
请你出XX道【题型】，主要考察【知识点1】、【知识点2】。。。，出题要求要符合【出题规范】中的要求，题号从X号开始，不要markdown格式，不要标注来源。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9949bce20e316163c2416c6979bbd293.png>
想让它原创出题，有两份材料必不可少：知识点、出题规范。
这两份材料的意义，就是给 DeepSeek 画个“框”，让它在这个范围内思考。因为它的推理能力太强、考虑面太广，不设限制的话，它给出来的东西很容易跑偏。
没有约束条件，你的 DeepSeek 就是个“什么都懂”，但说出来的话总不对你胃口的助手。
至于知识点和出题规范，就需要根据不同学科、你自己的实际教学情况去整理了。
# 结语
AI 真正改变的是我们的工作方式。与其被动观望，不如主动拥抱变化，让 AI 为我们赋能，把每个人独特的价值放大。
我是龙哥，在职场搞副业
专注分享个人成长丨Ai提效丨副业赚钱