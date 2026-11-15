# 大多数人都踩过的坑：MCP 根本不能在 Claude Code 里面装
上周五晚上十一点，我还在屏幕前干瞪眼。
“这 MCP 到底该怎么装？在 claude code 里跑，全是红字报错！”
起因是飞书 MCP 的用户凭证过期了，必须去改配置，整个人都要炸了。
我硬是不信这个邪，一直在试。凌晨两点，终于看到飞书 MCP 配置修改成功的提示，差点喊出来。
最打脸的是什么呢？
答案其实就一句话：MCP 的安装操作，必须在 Claude Code 的外部完成。
文末我放了 MCP 实战的终极省心方案！
# 方法一：先搞清楚内外之分，这一步错全错
## 几乎人人都会上的当
第一次装 MCP，十之八九的人都会这么搞：
```
# ❌ 错误示范
> claude mcp add feishu --app-id xxx
AI执行一通，然后没依旧没有安装
```
为什么会这样呢？因为你把系统命令直接打在了 Claude Code 的对话窗口里。
这相当于在微信聊天框里敲“重启电脑”，指望机器真重启。Claude Code 的对话区和你电脑的终端，是两个完全不相通的空间。
## 正确的做法
牢记这条铁律：所有 MCP 的增删改查，都必须在退出 Claude Code 之后执行。
先退出： /exit
![](img/zhuanqian_8eaadc3948692920742976b1e899a60c.png)
# 方法二：命令太长记不住？让 AI 代写
## 痛点：参数一大串根本背不下来
MCP 的安装语法确实吓人，比如：
```
claude mcp add-json feishu '{
"command": "npx",
"args": ["@larksuiteoapi/lark-mcp", "mcp", "-a", "APP_ID", "-s", "SECRET"]
}'
```
看到这种长串，谁不头疼？比背元素周期表还痛苦。
## 轻松解法：把活交给 Cursor
我后来摸到一条捷径：把所需参数丢给 Cursor，让它帮你拼好完整指令。
第一步：在 Cursor 里说明你的安装需求
```
安装飞书 MCP
{
"mcpServers": {
"feishu": {
"command": "npx",
"args": [
"-y",
"@larksuiteoapi/lark-mcp",
"mcp",
"-a",
"cli_a8cfe74****",
"-s",
"mFO4aJkNV2****",
"-u",
"u-f0Hf3****"
],
"env": {}
}
}
}
命令参考：claude mcp add-json feishu '{
"command": "npx",
"args": ["@larksuiteoapi/lark-mcp", "mcp", "-a", "APP_ID", "-s", "SECRET"]
}'
```
第二步：开启 Cursor 的 Agent 模式，它就会按你的需求生成安装指令
这样你就不用手动拼 JSON 了，复制出来直接在终端里执行就行。
![](img/zhuanqian_d6998cfc6ae2790fb36850c6564550fe.png)
# 方法三：怎么确认装上了
查看已启用的服务器列表
claude mcp list
![](img/zhuanqian_858a01688ecea945270b0d37d5510ec6.png)
# 方法四：不需要的服务怎么卸掉
## 卸载指令
claude mcp remove <要移除的mcp名称>
![](img/zhuanqian_5922c52f7d6ebf669b9f19894a4d21ef.png)
# 终极省心方案：一套文档搞定所有 MCP
看到这儿，你可能还是觉得步骤多。
告诉你个好消息！
我把常用的 MCP 服务安装命令、配置写法、常见报错处理，全部整理成一份《MCP 安装指令文档》。
这份文档的用处：
*   📝 收录了常用服务的完整安装指令
*   🤖 可以直接喂给 Cursor 或其他 AI 工具使用
*   📋 复制即用，几乎零记忆成本
*   🔧 每个服务都附带常见问题排错法
## 使用方式 3 步完成
1\. 在 Cursor 中新建一份提示词文档
新建一个文件夹，命名为“mcp指南.md”，把下面这段提示词粘贴进去
```
# MCP 安装配置指令文档
> 🤖 专为 AI 助手设计的 MCP 操作指令集
## 基础环境检查
```bash
# 检查 Claude Code 是否安装
claude --version
# 检查当前 MCP 服务状态
claude mcp list
# 检查特定服务详情
claude mcp get <服务名>
```
## MCP 服务管理命令
### 添加服务
```bash
# 基础添加命令
claude mcp add <服务名> <命令路径> [参数...]
# 带环境变量添加
claude mcp add <服务名> <命令路径> -e KEY1=value1 -e KEY2=value2
# JSON 配置添加（推荐复杂配置）
claude mcp add-json <服务名> '{"command": "命令", "args": ["参数1", "参数2"], "env": {"KEY": "value"}}'
# 指定作用域添加
claude mcp add -s local <服务名> <命令>     # 仅当前项目
claude mcp add -s project <服务名> <命令>  # 项目共享
claude mcp add -s user <服务名> <命令>     # 全局用户
```
### 服务操作
```bash
# 查看所有服务
claude mcp list
# 查看服务详情
claude mcp get <服务名>
# 删除服务
claude mcp remove <服务名>
# 重置项目选择
claude mcp reset-project-choices
```
## 常用 MCP 服务配置
### 飞书 MCP
```bash
claude mcp add-json feishu '{
"command": "npx",
"args": [
"@larksuiteoapi/lark-mcp", "mcp",
"-a", "APP_ID_HERE",
"-s", "APP_SECRET_HERE",
"-u", "USER_TOKEN_HERE"
],
"env": {}
}'
```
## 项目配置文件模板
### .mcp.json 文件格式
```json
{
"mcpServers": {
"service-name": {
"command": "/path/to/command",
"args": ["arg1", "arg2"],
"env": {
"ENV_VAR": "value"
}
}
}
}
```
## 安装操作流程
### 标准安装流程
1\. 退出 Claude 会话（如果正在运行）
2\. 在系统终端执行 MCP 安装命令
3\. 验证安装：`claude mcp list`
4\. 重新启动 Claude：`claude`
5\. 测试服务：在 Claude 中使用 `/mcp` 命令
## AI 助手操作指南
当用户需要安装 MCP 服务时，请：
1\. **确认需求**：询问用户想要安装什么类型的 MCP 服务
2\. **收集参数**：获取必要的配置信息（API Key、数据库连接等）
3\. **生成命令**：根据上述模板生成具体的安装命令
4\. **提供流程**：提醒用户按照标准安装流程操作
5\. **验证测试**：指导用户验证安装是否成功
```
手册会持续更新，获取最新版本可以进群
2\. 把需求告诉 Cursor，并把该文件拖进对话框
```
@mcp指南.md
安装飞书 MCP：详情
```
![](img/zhuanqian_ab8d1f653fcd7d420ea9a7ff1e254fd6.png)
3\. 让 Agent 自动处理
Cursor 会读取这份模板，自动生成正确指令，甚至可以直接帮你执行
从此以后，你就不用再死记各种命令格式了，相当于拥有一位 24 小时在线的 MCP 安装助理。
# 记住四点就行：
1\. MCP 安装必须在 Claude Code 外部进行，这是第一优先级
2\. 用 claude mcp list 核对安装状态
3\. 复杂命令让 AI 生成，别硬背
4\. 用好这份指令文档，一次配置永久受用