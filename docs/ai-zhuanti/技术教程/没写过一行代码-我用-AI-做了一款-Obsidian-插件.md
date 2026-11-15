# 没写过一行代码：我用 AI 做了一款 Obsidian 插件
龙哥前阵子用一颗龙珠悬赏 AI 编程做产品的实践者，恰好我刚靠纯 AI 协作把一个 Chrome 扩展送上了商店，全程零手写代码。这个契机让我想把整套流程整理成 SOP，供圈友参考。
## 一、SOP 总览
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3f9d79558da735649e5f860c2144114b.png>
## 二、解决什么问题
我常年在 Obsidian 里记录笔记，碰到好的网页内容就先收藏链接。问题是链接很容易失效，过段时间再点开就是 404，原文找不回来。同时我还想把文章的某段内容单独做成知识点卡片。基于这两个需求，我做了 MarkClipper for Obsidian：将网页内容转换成 Markdown，并在文件头部自动写入属性，方便在 Obsidian 中搜索和建立关联。
生成的笔记长这样：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_88f45ebb2c13092fad0289c9ca060253.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0406af1ea08bc64b9a49cc65bb0ea580.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e332db6ed00fafc25d7ae7b77425984c.png>
商店后台的数据也印证了需求成立：没有投放过任何广告，用户全部来自自然搜索。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_72bb7e3457b368226108207f538547c5.png>
## 三、工具准备
我的组合是：
- 能访问外网的环境
- 付费版 ChatGPT，可以用各种 GPTs，比如起名、调研、产品经理、文案等角色
- Claude
- Cursor
- Git
## 四、没有灵感怎么办
不着急动手，先回看自己日常有什么不舒服的流程，和 Claude 头脑风暴几轮，再用 GPTs 调研助手验证。也可以直接看榜单，选几个头部产品拆解，重点读它们的差评——差评里藏着未被满足的需求，把这些补上就是机会。
## 五、起名
还是交给 GPTs 调研助手，让它先分析竞品再生成名字，中英文都能出。
## 六、图标和宣传图
让 Claude 按照苹果或谷歌的设计规范来：风格极简、配色明快、有呼吸感。商店详情页的配图就是 Claude 生成的，中英文兼容。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e299d76ac4ac1f10f0a0de1ffa3405dc.png>
图标更香，连商店要求的各种尺寸都能一次性导出。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d594d438ce5d3abbb3db62e84f10315.png>
## 七、商店文案
这个环节用 ChatGPT 的 GPTs 产品经理来写，中英文各一版。以中文版为例，它的结构大致是：先用一句话定位（你的 Obsidian 笔记助手），然后列基础能力——一键收藏网页、右击菜单操作不打扰、标题和文件名自动关联、存储位置可自定义；再列进阶能力——自定义模板、中英文国际化、Readability 优化可读性；最后给使用场景和安装引导。
## 八、向 Cursor 下需求
流程上分三步：先用 Claude 把需求聊透，能确定个八成；再让 GPTs 产品经理产出产品文档；最后基于文档转成 Cursor 能直接执行的指令。
指令有个关键技巧：把任务拆小，要求它分步完成，并且写明确技术选型和限制条件。
下面是我线上插件实际用的提示词（稍作精简）：
**角色设定**
一位有丰富 Chrome 商店发布经验的扩展开发专家，同时也懂个人知识管理，曾经做过多个被商店精选的插件。具备产品、交互设计、前端开发、后端开发、安全和知识管理等多方面能力。目标：做出一款能上架并成为精选的剪藏扩展。
**技术方案**
- 原生 JavaScript + HTML + CSS
- 扩展版本：Manifest V3
- 权限：activeTab、contextMenus、downloads、scripting
- 第三方库：turndown
**功能需求**
基础功能：
- 用户选中内容时，只剪藏选中部分；没选中时，默认收藏整个网页
- 所有操作通过鼠标右击菜单完成，不出现弹窗或按钮
- 一级菜单名称【MarkClipper-for-Obsidian】，二级菜单动作是“导出笔记”
- 标题默认由“网页标题 + 选中内容最近的标题（支持 H1 到 H6）”组成，文件名和标题同步
- 让用户自选保存路径，而不是直接落进默认下载目录
高级功能：
- 支持用户自定义笔记模板，生成时可以在默认模板和自定义模板之间切换
- 完成中英文国际化
- 调用 Readability 库，让输出的 Markdown 结构更清晰
我存的模板示例（MECE 法则笔记）是这样：头部有 id、title、source、date、status、tags、aliases、links、stars 等字段，正文拆成 Summary 和 Note 两个区块。
**硬性要求**
- 生成的 Markdown 里不能出现 HTML 代码，但文字加粗、删除线、颜色等格式要保留
- 图片保留 URL，Obsidian 中要能正常显示
- 删掉网页的页眉、页脚、侧边栏，只留正文
**界面风格**
简约主义、绿色主调、排版通透。
**参考竞品**
Obsidian Clipper、MarkDownload。
**开发流程**
按阶段推进：先设计目录结构和功能模块；再实现右击菜单、正文提取与转换、文件保存；随后做自定义模板；接着测试功能和优化性能；最后准备商店素材并提交审核。
**注意事项**
- 每段代码需要附带简短解释
- manifest.json 里要把权限配置完整
- 照顾不同操作系统和 Chrome 版本的兼容性
- 遵守商店政策，保障用户数据隐私
最后给出的指令可以是：“请先设计插件的文件目录结构，并说明每个文件或文件夹的用途。”
## 九、推广
这块是我的短板。目前只在即刻和 Reddit 各发了一篇帖子，没有持续跟进。Reddit 对自家产品链接挺友好。我当时的目的不是爆量，而是验证两件事：AI 编程能不能走通全流程？能不能拿到自然流量？现在结论是：都可以。
## 十、没有编程基础能做吗
完全能。技术没那么神秘，它只是实现需求的工具。2025 年 AI 编程工具还会持续迭代，你只要问 AI“做这件事需要哪些技术”，然后让它照着清单实现就行。
比技术更关键的是找到用户的真实痛点，用 AI 去解决。
最关键的还有耐心。人会犯错，AI 也会犯错，你要愿意和它磨合，磨合顺了之后，产出效率会远超预期。
2025 年 AI 编程对普通人来说就是杠杆，各位不妨用起来，做出自己热爱、对别人有价值和也能带来收益的产品。