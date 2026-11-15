# 用 VS Code + DeepSeek 搭一套更顺手的 AI 编程环境
最近用 Cursor 的时候总觉得回复有点拖沓，而国产大模型 DeepSeek 的口碑也在圈子里越传越好。
翻看当下主流的大模型排行榜，DeepSeek-V3 在开源阵营里稳居第一，表现甚至能和顶尖的闭源模型掰手腕。
既然这样就试试看好了。和 Cursor 相比，DeepSeek 的响应更快、成本更低，关键还是要看实际用起来的回答质量。
下面就带你一步步把环境搭起来。
## 先装上 VS Code
VS Code 和 Cursor 的关系很亲近，严格说 Cursor 就是在 VS Code 的基础上二次开发的，可以理解为 VS Code 是 Cursor 的前辈。所以换成 VS Code 也不会有陌生感。
直接打开 https://code.visualstudio.com/ 官网，按自己的系统下载安装即可完成。
![](img/zhuanqian_5c887a86cf706c22cf902b12d91dff3a.png)
## 装上 Cline 插件
进入 VS Code 左侧的扩展市场，搜索 cline。注意挑下载量靠上、评分高的那个官方版本，别装错了。
![](img/zhuanqian_9ab62ea6bbfccd3ee81b611ff08416ae.png)
## 去 DeepSeek 领 API Key
打开 DeepSeek 官网 https://www.deepseek.com/ ，找到 API 接入入口。
![](img/zhuanqian_dc3df86b3035f17e5bfee82375f7229e.png)
用手机号注册登录即可。
![](img/zhuanqian_6c9e2ce5699d02f2bfe49d8535abe3db.png)
登录后能看到新用户赠送 10 元额度，约 500 万 token，普通体验完全够用很久。
![](img/zhuanqian_c14b85cbd660524b44b0f8abf36782e9.png)
下一步创建自己的 API Key。
![](img/zhuanqian_3e97d162a5ca91bb7f427e45a8f0e345.png)
生成后一定要保存好，丢了就得重新申请。
## 回到 VS Code 填入密钥
回到 VS Code 的插件页面，打开刚才安装的 Cline。
![](img/zhuanqian_a23becb0944252aa23a3098b19de4b4a.png)
在模型选择里选 DeepSeek。
![](img/zhuanqian_b9b338a0b0f996a418efb9bcfa2314b7.png)
在自定义提示词框里可以像用 Cursor 一样写上：Always respond in 中文 ，这样它就会一直用中文和你交流。
![](img/zhuanqian_fd8a79f61623602d5bd9cc4ac408d59f.png)
设置完后关闭窗口。
![](img/zhuanqian_f1d2824c1d8d1bd82a327fff92e11646.png)
接着点开工作区设置或功能开关。
![](img/zhuanqian_6e04e63e43f7f3f49639731606895192.png)
把需要启用的权限全部勾选上。
![](img/zhuanqian_e22f5912f4e1d190a5626b5505f55ec9.png)
到这一步，整个配置就算搞定了。
如果你希望 Cline 也像 Cursor 那样显示在右侧面板，可以这样调整布局。
![](img/zhuanqian_45603c1f3b11266f9b78c6a7be7fec3e.png)
来实战一把，让它帮我们做个贪吃蛇吧~
## 实际体验
新建一个空文件夹，用 VS Code 打开它。
![](img/zhuanqian_3c8207562f1ffe397fc5fc83bcf32633.png)
在聊天窗口输入提示词：帮我在这个项目下，完成一个贪吃蛇小游戏，用网页写
然后你就能感受到流畅度上的区别了，我也录了段演示视频一起感受。
效果是不是挺让人惊喜？
跑起来偶尔会有小问题，这很正常，毕竟提示词写得很简洁，能做到这个程度已经很能理解了。
就到这儿啦！