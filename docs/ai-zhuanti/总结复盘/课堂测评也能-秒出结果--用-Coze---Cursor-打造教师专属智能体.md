# 课堂测评也能“秒出结果”？用 Coze + Cursor 打造教师专属智能体
每次随堂测验结束后，最让老师头疼的是什么？——收卷、翻题、手动统计、逐项汇总……一圈忙下来，大半天就过去了。能不能让 AI 来接手这些重复劳动，让测评数据自动生成、实时呈现？今天就分享一套基于 Coze 与 Cursor 的课堂智能体方案，把“统计”这件事彻底交给机器。
## 整体思路一览
整套方案分成三端：学生端负责拍照上传，Coze 智能体负责识别与数据处理，教师端负责一键查看结果。三者通过 API 串联，形成“上传—识别—入库—统计—展示”的完整闭环。
## 学生端：拍照即传，不用额外装 App
学生在网页上打开链接，调用摄像头对准测评卷拍照，点击上传即可。图片会传送给 Coze 的 API，由智能体完成识别并写入数据库。
这里的前端页面用 Cursor 按照咱们提供的 UI 草图自动生成 HTML 代码，并封装好对 Coze 函数的调用。换句话说，整个交互页面几乎不用手写，交给 Cursor 就能快速搞定。
## Coze 智能体：三条核心模块，各司其职
### 1. 数据库：先定好要存什么
最终展示信息离不开这几项：每个小组收到多少份报告（小组、学生姓名）；每道题及每个维度的得分（题目、评价维度、分数）；原始评价单的查看入口（图片链接）。因此，在 Coze 的资源库里创建“数据库”，并提前配置好上述字段，后续所有流程才能顺滑衔接。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_35b47c1ea2216583403eca7042122346.png>
### 2. 工作流：四个功能对应四条流程
#### 功能一：图片识别 + 数据入库
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_ccc50fb906d803ecd09c0fd685d4ec85.png>
开始节点：因为学生是拍照上传，图片格式需要提前固定；同时让小组信息手动填写，避免分组识别出错。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0523980d676fee2770f9d896eb11b60b.png>
信息提取节点：这里采用视觉模型。为什么不选 OCR？因为学生拍照角度不统一，横屏竖屏都有，OCR 很难保证准确率，视觉模型对这类非规范图片的适应能力明显更强。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_aab5e5e7390636ccbaa0c6e350a6ecfb.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_5d0d22251e69f2e0d93af7383f412718.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_4ba7bbcaefe4f2ea0e724522fd6748aa.png>
格式整理：把识别出的字段整理成 SQL 格式，方便后续导入。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c6894fb1a8898db02e15346f0661aeb5.png>
```
async def main(args: Args) -> Output:
params = args.params
data = params["result"]
name = params["name"]
sys = "AAAA"
zu = params["group"]
url = params["image"]
values = []
for item in data:
subject = item["subject"]
assess = item["assess"]
star = item["star"]
values.append(f"('{subject}', '{assess}', {star},'{name}','{sys}','{zu}','{url}')")
formatted_values = ',\n'.join(values) + ';'
# print(formatted_values)
# 构建输出对象
ret: Output = {
"formatted_values":formatted_values
}
return ret
```
导入数据库：指向刚才建好的数据库节点。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_6f4768bac8dfaacd7722999efd011871.png>
结束节点。
#### 功能二：查看评价成绩结果
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_02dbb40d10e475a1bc59e4549f3ce748.png>
教师端点击“查看结果”时，直接触发这条工作流。
开始节点：无输入参数，调用即执行。
数据库查询节点：一键取出数据库中的全部结果。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b55619969a58056513880d09d81e5fe6.png>
绘制饼图：借助 Coze 的图表大师（ECharts 自定义插件）完成。
具体的做法是：先把数据组装成 ECharts 要求的格式，再批量调用插件生成图表，最后把标题与图片链接打包整理。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_b004b43c4936caf05c2f65703f0b702e.png>
饼图代码可以由 Cursor 代写，为了保持固定的题目顺序，代码里特意加入了排序限制条件。
```
async def main(args: Args) -> Output:
params = args.params
data = params["input"]
# 获取 subject 和 assess 的去重值
subjects = set()
assesses = set()
for record in data:
subjects.add(record["subject"])
assesses.add(record["assess"])
# 按照指定顺序排列 subjects
ordered_subjects = ["获取信息", "处理信息", "表达交流", "态度责任"]
ordered_subjects = [s for s in ordered_subjects if s in subjects]
# 按照指定顺序排列 assesses
ordered_assesses = ["互评", "自评"]
ordered_assesses = [a for a in ordered_assesses if a in assesses]
# 存储最终结果的列表
final_result_list = []
# 定义颜色列表，用于饼图的不同部分
colors = ["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#FF4500"]
for subject in ordered_subjects:
for assess in ordered_assesses:
star_count = {}
for record in data:
if record["subject"] == subject and record["assess"] == assess:
star = record["star"]
if star not in star_count:
star_count[star] = 0
star_count[star] += 1
# 将 star 转换为对应的星号表示并准备饼图数据
pie_data = []
for i, (star, count) in enumerate(star_count.items()):
star_symbol = "★" if star == "1" else "★★" if star == "2" else "★★★"
color_index = i % len(colors)  # 循环使用颜色
pie_data.append({
"name": star_symbol,
"value": count,
"itemStyle": {"color": colors[color_index]}
})
# 构建 ECharts 配置
chart_config = {
"backgroundColor": "#ffffff",  # 添加白色背景
"title": {
"text": f"{subject}'{assess}'分析",
"subtext": "",
"left": "center"
},
"tooltip": {
"trigger": "item",
"formatter": "{a}
{b}: {c} ({d}%)"
},
"legend": {
"top": "10%",
"right": "10%",
"textStyle": {
"fontSize": 16,  # 增大图例文字大小
"fontWeight": "bold"  # 加粗图例文字
}
},
"series": [
{
"name": f"{subject}{assess}评价",
"type": "pie",
"radius": "55%",
"center": ["50%", "60%"],
"data": pie_data,
"label": {
"show": True,
"formatter": "{b}\n{d}%",
"color": "#333",
"fontSize": 16,  # 增大标签文字大小
"fontWeight": "bold"  # 加粗标签文字
},
"labelLine": {
"show": True
},
"emphasis": {
"itemStyle": {
"shadowBlur": 10,
"shadowOffsetX": 0,
"shadowColor": "rgba(0, 0, 0, 0.5)"
}
}
}
]
}
# 构建字典并添加到最终结果列表
result_dict = {
"title": f"{subject}'{assess}'分析",
"content": chart_config
}
final_result_list.append(result_dict)
# 构建输出对象
ret: Output = {
"final_result_list": final_result_list
}
return ret
```
结果整理：因为最终需要把每道题的自评和互评放在一起展示，所以提前将相同题目的图片结果归类打包，后续直接调用。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_8d8428aab4f8545901bade99727cbb6d.png>
统计份数：绘图的同时统计学生总人数，用于最后的数量展示。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7d0af2c56f30b325fc1062a09cea2129.png>
结束节点：输出 Markdown 格式，确保图片能在页面中直接显示。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_9dfaea52b7001e01c22a35e237f070fb.png>
#### 功能三：查看评价单
评价单的查看逻辑是“按小组”展开。先展示每个小组的统计数量，再按小组显示图片缩略图，点击可放大查看详情（这一交互在 HTML 端实现）。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_0fdd123933aaa08772a4e1eae1fb3ec5.png>
开始节点：接收“查看评价”指令后立即执行，无需额外输入。
查询数据库：只取小组信息和图片链接两个字段。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_a65cfbd3e65e2281235a2d0a5101a407.png>
格式整理：统计各组份数，并按小组把图片链接分组。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_83bd6b41d23f3f51f4af295227b147e9.png>
结束节点：直接输出分组结果。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_7447d3e60706c754322cfdbee683d947.png>
#### 功能四：清除缓存
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_59c8684662f40512fd22b5851990a73d.png>
这个最简单，直接使用“删除数据”节点把库里的内容清空即可。
### 3. 智能体：把工作流串起来
在智能体后台把上面四条工作流添加进来，并设置好对应的触发逻辑。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_d825d60377dc2782305ab7ab1cdb1696.png>
发布时必须选择 API 或 SDK 渠道，方便外部网页调用。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_c90f1c6034f68a22f141918a1ae84185.png>
## 教师端：三个按钮搞定所有操作
教师端页面只需三个按钮，点击后分别向智能体发送对应指令，再把返回结果直接展示出来。查看成绩结果时，图片支持点击放大；查看评价单时，图片同样支持点击放大。
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_24725c96ff39e33460b78e994dd7d735.png>
<https://gitcode.com/OpenDocCN1/data/blob/master/imgs/zhuanqian_1a8bc5895ddd6d3595e38cc11510422f.png>
## 写在最后
AI 真正落地的价值，往往就藏在细分场景里。它不是要颠覆整个流程，而是为现有环节注入效率。课堂测评只是一个小小的切入口，类似的“AI + 业务”组合，值得每一位老师、每一个行业去尝试。
欢迎在评论区聊聊你所在的场景，看看 AI 还能怎么帮你减负增效。