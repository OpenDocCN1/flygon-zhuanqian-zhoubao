# Windows Copilot 开发者预览版上车全攻略
今年五月底的 Build 大会上，微软官宣 Windows Copilot 要来了，升级后的系统将自带 GPT 小助手，日后用 AI 几乎像伸手拿筷子一样顺手。
6 月 30 日，Windows Copilot 的开发者预览版悄悄推送，小编第一时间上手，体验感确实如官方所说，私人的 GPT 真的很上头！
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ac6750698e59f7be31ff09ccdaada99b.png>
下面把从报名到可用的一整套流程拆开讲清楚。
先划重点：想在本次预览版里用上 Copilot，必须同时满足两点硬性门槛
一是本机处于开发者通道且系统版本为 Windows 11 Build 23493 及以上；
二是 Microsoft Edge 已升到 115.0.1901.150 及以上。
另外记得把系统区域调成美国。
首先把 Windows 的区域调整为美国。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_008312e43b92efb6bd375762c56b2c6c.png>
拉取 Windows 11 Insider Preview 23493 或更高版本
在浏览器里搜 windowsinsider，点击进入“Preview Windows now”，按指引用微软账号绑定，绑定成功后会提示 open settings，直接打开系统设置。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3a94a355bad46d13c472b597cad46bce.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_05a48a1294001440f0ba14cd941a4219.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aedfe25e12deb250a17704d891d089af.png>
点进“立即体验”加入 Windows 预览体验计划
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2eb26ab68493e19301e61cd1876ed3e1.png>
把通道切到“开发人员频道”
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_47dfb7fbe817fb73729a091427e81af3.png>
拉取并安装 Windows 11 Insider Preview 23493 更新包。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d390b57af76b037c69b28beab96e80a8.png>
升级 Microsoft Edge 到 115.0.1901.150
打开 Edge，进入 设置-关于 Microsoft Edge，触发自动更新即可拉到最新版。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_77d993bd12294b7c77edbe387819d1b1.png>
升级完成后，Edge 图标上会带有“BETA”标识，说明版本已达标
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8c801f1f5de14e5c6c415b4b0fb98b5a.png>
手动开启 Windows Copilot
上面两项只是基础条件，因为 Copilot 仍处在 A/B 测试阶段，并不是人人都能直接看见。如果按部就班操作后任务栏仍未出现 Copilot 图标，就需要借助 ViVeTool 工具强制激活。
先去 https://github.com/thebookisclosed/ViVe/releases 下载最新版 ViVeTool。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_e0c1d33ba4b70f5c4507368141ce348e.png>
解压后记住该文件夹的路径
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5011ef8e592aac1202f360ae8555d32f.png>
在开始菜单搜索“terminal”，右键选择“以管理员身份运行”
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_3b39ef35892fc11a6e1d4f7a05d8534e.png>
用 CD 命令切换到存放 ViVeTool 的目录，然后执行以下指令
.\vivetool /enable /id:44774629,44850061,44776738,42105254,41655236
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4539db96732402d658ea8cb6fe1363de.png>
重启机器后，任务栏里就能看到新冒出来的 Copilot 图标！
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d0990f4795220d89bbccd238571ea69f.png>
大功告成，现在就可以在桌面端和 Bing 一样聊天了！网页能做的，桌面版基本都能做！
小提示：按快捷键【WIN+C】就能一键呼出或收起 Copilot！
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0ea1e147907f8771c074bcd55ebbbc47.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_2efc94549d72e68cd8f4be31ace4e561.png>
试着用文生图功能生成一张“车水马龙”的画面，效果相当在线！
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_67815250756b18f61596096edd98b0cd.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d7aba32f1fa64d7490628b076e26bca6.png>