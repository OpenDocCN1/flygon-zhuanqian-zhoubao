# 从零到一：借助AI在YouTube发布首部作品的实战拆解
很多人在问我：零基础、没剪辑经验，也能用AI做一条能上线的YouTube视频吗？我可以说可以。下面这套是我亲测跑通的工作流，从赛道选择到最终发布，全程摊开，跟着走就能上手。
我拿“自我提升”做示范，换成搞笑、生活技巧、职场干货都一样套用同一套逻辑。
## 起步阶段：先把方向和人群想清楚
内容服务于谁，你后面的每一步都要围绕这个人来做。以自我提升为例，受众大多是想突破现状、渴望成长的人。先锁定人群，再倒推选题和表达方式，思路就不会散。
提前去看几位同类创作者的主页，观察他们的风格和受众反馈：
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f009da2d33e477862bdfef3ffe93b267.png>
## 频道搭建：基本可以用ChatGPT代劳
先科普一个点：同一个Google账号下理论上可创建50个频道，足够尝试。
下面的建频道步骤，我基本全丢给ChatGPT去做。首次创建和已有频道时的入口位置会不一样，注意区分。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e2eca77ff2684ad8969b713832e3c488.png>
### 频道名怎么定
可以从喜欢的角色或IP找灵感。我偏爱《战神》里的克拉托斯，力量感强，和自我提升主题很搭。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a670e68d6483c17d2285fa0a93a649e9.png>
交给ChatGPT的示范指令：
“我想做一个关于自我提升的YouTube频道，全部内容由AI生成，并以一个贯穿性角色为主，这个角色的气质接近Kratos。请结合角色意象和克拉托斯的特质，给我10个频道名称建议。”
手上有参考图的话直接上传，AI的联想会更准。
### 频道简介一键生成
选定名字后继续让GPT写简介。举例：我的频道名是“Empowered Anonymity”，让它输出一份200字以内、条理清晰、带表情符号、包含细分赛道关键词的英文简介，并顺带给中文翻译，效率很高。
### 头像与Logo出图思路
先让GPT给设计方向，再根据角色特征细化需求。参考表达：
“我挑了第X个方案。整体配色黑红，画面是戴Guy Fawkes面具的神秘人物，背景带烟雾氛围感。基于这个brief，帮我写5条可在Leonardo AI里使用的文本提示词，风格要更独特。”
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0065ef8e97fb6833afbd01f5452efde7.png>
我实际用的组合是ChatGPT + Leonardo AI，完整功能开了付费。国内也有平价替代，比如Kimi + 可灵，流程几乎一致，去水印可能需要付费。Leonardo AI每日赠送150积分，免费试用绰绰有余。
多试几个模型对比，我最后觉得这个手感最好。头像比例建议固定1:1。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ed93241755145b54adf055272489a9fc.png>
从生成结果里挑一张最对味的，直接作为头像。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3d1e669144af5b577c7dc216b43c5a47.png>
## 制作首支视频
准备阶段结束，进入实拍制作。
### 抓取对标文案的利器
先安装Chrome插件 YouTube Summary with ChatGPT：
https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli
它的价值是快速提取视频文稿。进入同行爆款视频页面，把文稿抓下来备用。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f9a819bbeb21fae0c04dec0187be27ce.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_f9a415b911baff4b171955c4d8924446.png>
### 让ChatGPT重写脚本
把抓到的文案喂给GPT，提示示例：
“这是我之前视频的脚本，请用原作者的写作和说话风格重新组织表达，可以调整措辞顺序，但不要删减核心内容，也不要过度改写。去掉时间轴标记。脚本如下：……”
现实情况是我的配音工具额度只剩1000字符，所以我要求GPT把全文压缩到1000字符以内，正好做短视频。
### 配音生成
脚本确定后开始配音。
剪映自带免费音色可用，我更推荐ElevenLabs，音质更自然，新用户可免费试用10000字符。原计划做中长视频，额度不够，只能先做短视频。官网：https://elevenlabs.io/
操作界面简洁，可试听不同音色，选一个契合视频调性的。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bc5141b67716c9502dbe0b02871f7ce0.png>
生成完成后下载到本地备用。
### 主图与封面素材
这次的主角设定是Guy Fawkes，所以后续封面和画面都围绕这一形象。继续请ChatGPT帮忙：
“请为Leonardo AI写3条文本提示词，我需要一张神秘角色图：穿黑衣、不露脸、戴Guy Fawkes匿名面具，主色调黑红，背景昏暗，氛围像YouTuber直播间。”
得到提示词后去Leonardo AI生成。短视频选9:16，中长视频选16:9。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4077a3e539f8e0c0a1e6d79572ab861e.png>
挑一张满意的保存，主图和封面可共用。
随后可在Leonardo AI内把静态图转成动态视频，需会员，免费用户可找替代方案。把生成的视频片段和配音导入剪映整合。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1b97eadfb10724799e056541a87b6de5.png>
### 配音分段标记
本期使用的英文脚本大致为：
Do you really think people care about you? If you believe that others are concerned about your existence, let me remind you: nobody truly cares. If you died today, you’d likely be forgotten by tomorrow. As a child, people might have cared out of obligation, but as adults, that pretense fades. This realization can sting, but it’s liberating. Accepting that no one cares frees you from judgment and allows you to embrace your authentic self.
Three weeks ago, while in a hospital bed, I understood that if death came for me, no one would genuinely care; I’d just be another number. This might sound depressing, but it’s freeing. Once you accept this, you stop letting fear and opinions hold you back. People are inherently selfish and focused on their own struggles.
Letting go of the idea that others care will lead to true freedom. If you have people who care about you, cherish them, but don’t depend on them. Build your own resilience so your mental peace remains unshaken. Live authentically and fulfill your potential without worrying about judgment.
建议在剪映里开启智能字幕识别，并在每段配音处打标记，方便后续画面衔接。若追求效率，这步也可省略。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2d1ddca64913aa8afcd2908ba2f8b941.png>
### 批量产出分镜画面
一段脚本准备好后，让ChatGPT继续生成画面提示。指令示例：
“请帮我为视频生成画面提示。我会分段提供剧本，每段请给出4个情节递进、风格统一但画面不同的prompt — 第1与第2关联、第2与第3关联、第3与第4关联。整体要兼具故事感、神秘感和科技矩阵感，细节描述要具体，主色调黑红。”
把提示词导入Leonardo AI生成图片，再转成视频片段，统一进剪映。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b8b1590f33f7fc119d4a75e6029c6197.png>
素材拖入剪映时间轴，若视频与音频不同步，可适当降低视频播放速度。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_776cb5273f1df70572620e689005d997.png>
调速后若超出标记点，裁掉多余部分即可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_397a90f08787269a6c99fc8261c87b58.png>
完成第一段后，复制第二、三段脚本重复上述流程：生成prompt → 出图转片 → 导入剪映。每隔一段插入一次主角主图视频，保持视觉连贯，直至配音全部填满。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aa9c20bd463dfa2e245c2be308acd40c.png>
### 背景音乐与细节润色
背景音乐也可以请教GPT：
“基于我的视频脚本，请推荐几类适合的BGM曲风关键词。”
拿到关键词后在剪映中搜索免费音乐即可。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_dcf06d0043dc1c0b8a6b2092dd907be9.png>
其余转场、特效、字幕细节可自行探索，剪映上手很快。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_70119ee272391ef804896a017f3bdf1c.png>
## 发布环节
### 标题与说明
把视频内容要点告诉ChatGPT：
“请根据我的视频内容，输出5个标题建议及对应的YouTube说明文案。”
### 缩略图制作
可在Canva中选用现成的YouTube缩略图模板制作，最省时间。
https://www.canva.com/
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_bed125f47c838d645a370d92558a9af3.png>
### 标签获取
标签可直接询问ChatGPT，也可参考对标账号。我习惯直接问AI。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d8503aee0ff2a8c43f427402162d1455.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2f09ea31a9984f71faa13bd9ae7b5e04.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ebaaa99980355a67ff5e502afcf23340.png>
准备完毕后点击发布。若在国内，建议发布时间选在上午9-10点。
这是我第一次写实操向教程，可能有不完善之处，欢迎交流。希望这份拆解能帮你完成AI视频创作的第一步，有问题评论区见。