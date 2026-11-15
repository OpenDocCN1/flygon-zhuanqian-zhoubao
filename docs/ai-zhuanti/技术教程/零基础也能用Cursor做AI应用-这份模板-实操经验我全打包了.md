# 零基础也能用Cursor做AI应用？这份模板+实操经验我全打包了
这期分享的干货可不只一点点。作为这次“Cursor 零基础做软件应用”的教练，我一直想把手头一些压箱底的东西翻出来给大家看看。
打从接触 Cursor 起，我前前后后折腾了不少网站和小工具，有的是图乐子，有的是给自己日常用。像批量抓取可商用图片、批量存储截图、公众号文章一键导出这些，平时我都用得很顺手。可我心里总犯嘀咕：这些东西太轻了，像家里没什么存货，不好意思端出来见客。
昨晚我忽然一拍大腿：龙哥的超级标发了之后，精华区里全是 YouTube Shorts 和 Cursor 结合的分享，AI 应用这个方向反而几乎没人提起。我手上正好有个之前用 Cursor 整理的 AI 工具站模板，估计想做 AI 工具的朋友正需要。干脆一股脑儿都端出来，连带着几个常用的模型工具和挖需求的心得，算是凑一份大礼包。
## 超级标 AI 应用模板
AI 应用大体上分网站、App、插件，我讲的是其中最容易上手的 AI 网站。它的优势很明显：做起来快、变现路径短、发布门槛低，也更容易获得流量。
说到底，绝大多数 AI 应用都绕不开一件事：向模型投喂输入。不管是生图、聊天还是各种 AI 生成，本质上都是你先给出提示，模型再吐回结果。最典型的例子就是 GPT、Claude 那些对话框。
一个多月前我下决心专心做出海，就用 Cursor 搭了这么个模板。别看它体积小，该有的能力一样不缺。下面我尽量把细节拆开讲。
### 模板示例
我放了一个用 AI 调鸡尾酒的案例，对应文件是 `src/components/cocktail.astro`。
你只要告诉它想要的颜色、口味、喝酒的场景，它就会自动产出风味介绍、配方表、调制步骤、酒精度、卡路里与碳水含量，连怎么装饰都会给你建议。
![](img/345a4fbdaae4a2e174340b3332e21ec5.png "None")
### 如何自定义成自己的 AI 工具
想改成自己的 AI 工具？按这几步走就行：
- 先准备好 API Key（不知道这是啥？直接问 Cursor）。
- 把 `baseUrl` 指向你的 API 服务商。模板默认用的是 OpenRouter，接着用就什么都不用动；如果想换别家，比如对方接口是 `https://xxxxx.ai/api/v1/chat/completions`，你把 `https://xxxxx.ai/api` 填进配置文件就行。
- 配置 `model` 参数，也就是你想调用的模型。
- 配置 `temperature`，这个值控制在 0 到 1 之间，管的是生成内容的随机程度，不懂照样问 Cursor。
- 配置 `maxTokens`，限制 AI 使用的 Token 数量。要生成的内容很长就把这个值调大，否则会被截断。
总结就一句话：拿上自己的 Key，写好提示词，剩下的交给 Cursor 给你生成想要的页面。
### 如何在本地部署
本地先装好 nodejs、npm、git，装法不清楚就继续问 Cursor。
第一步，把代码复制到你的 GitHub 名下。模板仓库在 [AI 应用模板](https://github.com/netlogs/AIwebsite-template) 这里。
![](img/dd47a24add755ec0f1b25d8d0e1fd25e.png "None")
按图里的红线提示，选择 “Use this template”，创建新仓库。
![](img/ab6789874e6784b72c365d1a78f29315.png "None")
在标了 1 的地方填好仓库名，点 Create repository，代码就到你的仓库里了。接着去你的仓库页面，点下面这个入口：
![](img/6ff222d5be0f606bd11253a5a6aa101c.png "None")
然后拉起命令行（cmd 或 Cursor 的 Terminal 都行）。
执行 `git clone git@github.com:yourname/yourepositoryname.git`，记得把地址换成你自己的。
首次 clone 可能会遇到账号问题，比如让你填邮箱之类的。这时候把这句话抛给 Cursor：“我第一次 git clone 自己的 GitHub 仓库，需要做哪些配置”，它一般能帮你搞定。
等 clone 完，代码就躺进你本地目录了。进到代码目录，运行 `npm i` 装依赖。要是没操作过，就按住 Shift 在目录里点右键，选“在此处打开终端”，剩下的交给 Cursor。
依赖装好后，执行 `npm run dev` 启动本地测试。成功后你会看到类似下面的输出，关键看 Local 那条链接。
![](img/2fbbfb3d1363006e21cc034d3884dd1c.png "None")
继续在代码根目录建一个 `.env` 文件，写上 `OPENAI_API_KEY="sk-or-v1-97cd94b96xxxxx"`，后面换成你自己的 key。
打开浏览器里的蓝色地址，就是本地预览。代码一保存，页面会实时刷新。项目 readme 里也有详细描述，照着来就行。
### 部署到 Vercel
这步 Cursor 航海手册已经讲透了，身边也有人照着做完成功上线。唯一要留意的是：在下图标的位置，把本地 `.env` 里的 apikey 填进去。
![](img/518d18478e4b7cc9c9aa291cb149b458.png "None")
### 技术栈选择
模板的技术栈我选了 Astro，理由很简单：
- Astro 文件里可以直接写 HTML，对新手相当友好。模板里那个鸡尾酒页面就是纯 HTML（其实是 Cursor 替我写的）。
- 学会 HTML 再配合 Cursor，Astro 基本能猜个八九不离十，学习曲线特别平缓。
- Astro 生态成熟，以后想写更复杂的项目也不至于卡壳。
要是现在觉得有点懵，也别慌。航海才刚开了两天，现在看不懂没关系，再过一周、两周、甚至到圣诞节，你回头看可能就是小菜一碟。
照着手册走一遍，哪怕完全不会代码也没关系。你完全可以用自然语言告诉 Cursor：项目里哪个部分是干嘛的、想怎么改，它都能照做。
如果你连怎么描述都摸不着头脑，把我上面说的内容直接粘过去，也是一个办法。
### 模板 Prompt 为什么没有
模板 Prompt 我就不放了，时间过去太久，早忘了当初咋写的。但原因更重要：
- 想做自己的 AI 应用，直接用模板就行；
- 想练手，Cursor 里的练习项目也不少，可以照葫芦画瓢自己写一份 Prompt；
- 我敢担保零基础也能让 Cursor 生成这个模板，因为我自己就是用对话描述生成的，而且我压根不会 Astro，准确说是完全不懂前端；
- 现在的 Cursor 航海手册，完全足够陪你走到这里。
## 更多工具
### 可商用的 Unsplash 图片批量下载
以“批量动物图片下载”为例：
- `ACCESS_KEY` 改成你自己的 key，去 Unsplash 官网免费申请；
- `JSON_PATH` 指向 `animals.json`，在同文件夹里新建这个文件，按 JSON 格式填好关键词；
- 想换成别的玩法，直接让 Cursor 把它改造成任何你想要的形态。
拿不到想要的提示词？让 Cursor 分析一下文件的实现逻辑和细节，把它用自然语言描述一遍，你就有了一份 Prompt。想自定义，直接问 Cursor 吧！
```
#multiDownloadunsplashimage.py
import requests
import json
import os
import time
from datetime import datetime
class AnimalImageDownloader:
def __init__(self, access_key):
self.access_key = access_key
self.base_url = "https://api.unsplash.com"
self.headers = {
"Authorization": f"Client-ID {self.access_key}"
}
def load_animals(self, json_path):
"""
从 JSON 文件加载动物名称列表
"""
try:
with open(json_path, 'r', encoding='utf-8') as f:
data = json.load(f)
animals = data.get('animals', [])
print("加载的动物列表：")
for i, animal in enumerate(animals, 1):
print(f"{i}. {animal}")
print(f"\n 总共加载了 {len(animals)} 个动物名称")
return animals
except Exception as e:
print(f"读取 JSON 文件时出错: {str(e)}")
return []
def download_animal_image(self, animal_name):
"""
下载指定动物的图片
"""
# 创建下载目录（如果不存在）
download_dir = "animal_images"
os.makedirs(download_dir, exist_ok=True)
# 构建保存路径
file_path = os.path.join(download_dir, f"{animal_name}.jpg")
# 如果图片已存在，跳过下载
if os.path.exists(file_path):
print(f"图片 {animal_name}.jpg 已存在，跳过下载")
return False
try:
# 搜索图片
search_url = f"{self.base_url}/search/photos"
params = {
"query": f"{animal_name} animal",  # 添加 'animal' 关键词以提高相关性
"per_page": 1,
#"orientation": "square"  # 优先获取方形图片
}
response = requests.get(search_url, headers=self.headers, params=params)
response.raise_for_status()
results = response.json().get("results", [])
if not results:
print(f"未找到 {animal_name} 的图片")
return False
# 获取 200x200 尺寸的图片 URL
image_url = f"{results[0]['urls']['raw']}&w=200&h=200&fit=crop"
# 下载图片
image_response = requests.get(image_url)
image_response.raise_for_status()
# 保存图片
with open(file_path, "wb") as f:
f.write(image_response.content)
print(f"已下载 {animal_name} 的图片")
return True
except requests.exceptions.RequestException as e:
print(f"下载 {animal_name} 图片时出错: {str(e)}")
return False
def download_all_animals(self, json_path):
"""
下载 JSON 文件中所有动物的图片
"""
animals = self.load_animals(json_path)
if not animals:
print("没有找到动物列表或列表为空")
return
print(f"开始下载 {len(animals)} 个动物的图片...")
success_count = 0
for animal in animals:
print(animal)
if self.download_animal_image(animal):
success_count += 1
time.sleep(1)  # 添加延迟以避免 API 限制
print(f"\n 下载完成！成功下载 {success_count}/{len(animals)} 张图片")
print(f"图片保存在 'animal_images' 目录下")
# 使用示例
if __name__ == "__main__":
# 替换成你的 Unsplash API access key
ACCESS_KEY = "xxxxxxx"
# JSON 文件路径
JSON_PATH = "animals.json"
# 创建下载器实例
downloader = AnimalImageDownloader(ACCESS_KEY)
# 执行下载
downloader.download_all_animals(JSON_PATH)
```
### 公众号文章批量导出
具体方法见原精华帖。
### 一键保存多张截图
平时想存截图，不是发聊天框再右键，就是用 Windows 自带工具挨个点保存，图一多真的很烦。所以我做了个小网站：复制图片后打开网页，Ctrl + V 一贴，就能一键全部存到本地。
想更顺手，还能让 Cursor 加个批量重命名之类的优化。
体验地址： [bulkscreenshotdownload.com](https://bulkscreenshotdownload.com/)
## 如何挖掘需求
之前在航海群里，还有花生老师昨天的直播里，不少朋友都在问需求该从哪来。做出海一个多月，我的感受是需求可以分成两类。
第一类，是自己生活中冒出来的需求。它受众不一定大，但能勾起你自己的好奇心，做起来也带劲。
第二类，是通过数据网站挖出来的共性需求。这类需求是大家都在找的，确定性更高。
两条腿走路，灵感才不会断。
希望这份大礼包对你有用。跟着航海手册一步步走，再结合上面的模板和思路，你的 AI 应用也该能落地了。我们路上见！
今天主要拆解一下第一类需求是怎么找出来的，第二类的方法我在出海手册里都整理过，我自己平时也会去哥飞的公众号那边取经，（之前做过的公众号文章批量导出功能，本质就是为了方便我看哥飞的文章）
#### 怎么自己把需求找出来
**最通用的招数：写日记**
别觉得夸张，就是写日记，而且要写得越细越好。
赚钱上有一篇小排老师的文章讲过，看不到需求的原因，往往不是需求不存在，而是你离得太远。地图上陆地和海洋的边界，看起来是一条光滑的线，等你凑近了才发现全是锯齿。
很多时候我们不是没需求可抓，而是太熟悉了。大脑会自动过滤掉那些司空见惯的东西，**因为太懂了，一眼扫过去就觉得“我知道”，于是直接略过了**。
但当你把自己的念头、经历用文字写下来时，这些东西会从潜意识里被拽出来，变得具体可见。
举个我自己的例子：
前段时间和朋友的聊天记录里有一句：
* 怪物猎人明年要出荒野了，真的太期待了
如果我没记下来，这句话顶多给我带来一秒的兴奋，然后知道大概发售时间去买去玩就完了。
记下来之后，我就开始抠每一个字，回忆起相关的上下文。
怪物猎人系列武器多、技能多、配装逻辑复杂，玩的时候经常要查攻略。那新作《荒野》上线前，做一个专门的 wiki 站点，把攻略慢慢整理出来，是不是就是一个天然的需求？
顺手去 Google Trends 看了一下，游戏名字现在已经是个上升词，热度很高。搜一下大家都在问什么：游戏具体哪天发售？是续作还是 DLC？会不会有前作联动？
这些问题背后不就是流量入口吗？完全可以提前搭好网站等着吃。
再发散一下，除了怪物猎人，明年还有一大堆 3A 大作要发售，一个个去查趋势不就一大堆机会？哪怕是老游戏，去 SEMrush 这类工具里扒一扒，也能找到用户在关心、但竞争还没卷起来的长尾点。
最有意思的是我其实挺懒的，日记也没坚持写，就是偶尔无聊翻翻自己最近的记忆，让那些高频出现的词自己冒出来，相当于闭眼翻相册。
一个月前我还在焦虑：需求到底去哪找啊，我怎么一个都想不到，我的小时候好奇心去哪了，我是不是废了。
现在感觉不一样了，世界清晰了点，好奇心也回来了。有时候脑子里蹦出一个词，我就能一头扎进去扒相关需求，看到好多以前根本没注意到的内容，真的开眼了。
另外一件事要强调：**多做多做多做**，重要的事说三遍。我这一个月大概做了十来个站，基本都凉了，但做的过程中把方法论一点点刻进肌肉记忆的那种爽感，真的会上瘾。
最后，如果你也想参与到超级标 AI 应用的共建，欢迎把基于你自己内容优化过的网站代码分享出来，也欢迎去我的模板仓库提 Issue 和 PR 一起把项目做得更好。