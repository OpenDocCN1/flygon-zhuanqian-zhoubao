# 从设计稿到可运行代码：手把手教你把 Figma 官方 MCP 接到 Cursor 上
Figma 上周正式上线了基于 Dev Mode 的官方 MCP 原生接入。告别过去那种装插件、配端口、时不时掉线的第三方方案，现在官方提供了更稳、更省心、功能也更完整的原生能力。
这篇笔记就用最直白的步骤，带你把 Figma 官方的 MCP 接上 Cursor，真正实现“看到设计稿就能让 AI 直接生成”的所见即所得体验。
### 一、Figma 端先把服务打开
第一步，本地 Figma 客户端一定要升到 125.4.9 或更新的版本。
升级完成后进入设置页 Preferences，打开 Dev Mode MCP Server 的开关即可。
![](img/zhuanqian_c0e3a2b468d46de586c6a4f238206d1d.png)
### 二、在 Cursor 里完成 MCP 配置
打开 Cursor，进入设置页面，点击 New MCP Server 新建一个服务器配置。
![](img/zhuanqian_55aff60dca3fedc21a735afd568096d8.png)
把下面的 Figma MCP 配置整段复制，粘贴进 mcp.json 并保存。
```
"Figma Dev Mode MCP": {
"type": "sse",
"url": "http://127.0.0.1:3845/sse"
},
```
![](img/zhuanqian_56dff0bd67f37eabd0fdd1de68c2b80f.png)
保存后回到 Cursor 的设置页，用三点来判断是否成功激活：
1. Figma Dev Mode MCP 的开关是打开状态
2. 状态灯是否已经变成绿色
3. Tools 区域是否已经加载出具体的工具数量
![](img/zhuanqian_449a57b45a904c909a4baeb1868159ea.png)
### 三、开始用 MCP 让 AI读懂你的设计稿
配置生效后，切回 Figma 客户端，右键选中你想要落地的设计稿，复制其链接。
![](img/zhuanqian_dc04535c7393e9a59361c0c00033c1af.png)
把链接直接丢进 Cursor 的对话窗口，AI 就能准确解析这份设计稿的内容。
![](img/zhuanqian_371f2336ae40e92dac46dfd6be87ff8f.png)
目前官方 Dev MCP 已经开放了 4 项核心能力，可以配合使用：
| MCP 能力 | 它能做什么 | 典型用法 |
| get_code | 将当前选区一键转成可直接运行的前端代码，支持在设置里切换 React + Tailwind 或纯 HTML/CSS 输出 | 新建页面骨架时，选好画板调用 get_code，让模型在此基础上补充交互逻辑，省去手工还原像素的工作 |
| get_variable_defs | 提取选区中实际用到的设计系统变量，包含变量名、当前值和模式 | 避免 AI 硬编码色值，让输出严格遵循你的设计规范，比如使用 color-primary 而不是写死 #FF5630 |
| get_code_connect_map | 建立 Figma 组件与代码仓库中真实组件的映射关系，依赖 Figma Code Connect 配置 | 在大型项目中引导 AI 复用已有的 <Button>，而不是重复造轮子，降低技术债务 |
| get_image | 导出选区或整张画板的 PNG/JPEG，可自定义倍率，作为视觉参考给模型 | 遇到复杂流程、响应式断点或组件密集的场景，先给一张全景图帮助模型理解层级，再用 get_code 精细化生成 |
希望这套流程能帮你把设计到开发的衔接提速。
想深入了解可以参考官方资料：
[1]《Guide to the Dev Mode MCP Server》官方英文原版教程：https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server
[2] 《Introducing our Dev Mode MCP server: Bringing Figma into your workflow》这篇介绍 MCP 技术理念的文章：https://www.figma.com/blog/introducing-figmas-dev-mode-mcp-server/