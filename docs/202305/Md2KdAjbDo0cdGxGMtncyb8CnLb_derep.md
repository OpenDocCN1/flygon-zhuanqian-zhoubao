# 用Colab + Stable Diffusion 搞定云端免费的自动批量无限出图
作者：龙哥



大家好，我是龙哥，赚钱老用户一枚。理工背景，在广州做工程管理，业余健身，积累了几万粉丝，也在做健身赛道的产品推广。说白了就是一个工具控，写点代码，核心诉求就是把活交给工具，自己多摸鱼。下面分享的这套打法，就是怎么用零成本的云端资源实现AI作图自由。

# 先说问题

*   Stable Diffusion目前是AI绘画的顶流，但本地部署对显卡要求很高，普通电脑根本扛不住。

*   硬件不够就上云。Google Colab正好提供免费的云端算力环境，可以白嫖来出图。

*   AI绘画的容错率很低，基本要筛个二三十张才能挑到一张能用的，所以量必须堆起来。

*   Colab给每个账号分的GPU额度有限，手动点一下很快就用完了。

*   下面这套组合拳，能让你在Colab上跑Stable Diffusion，实现云端、免费、自动化、批量化、几乎无限的出图。

# 第一部分：把Stable Diffusion WebUI部署到Colab

*   提前准备好🪜账号和Google账号

*   用Google账号登录后，打开下面这份Colab笔记，直接点运行

*   这份笔记是camenduru大佬维护的版本，稳定好用

https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/main/nightly/stable_diffusion_v2_1_base_webui_colab.ipynb

![](img/f97b157b46d1f94c1c328b3636fed464.png)

*   运行过程中可能会跳出验证码，按提示完成即可

*   代码执行时下面会实时滚动日志

*   中途可能会多次出现人机验证，注意及时处理

*   等资源下载安装完毕后，会出现几个 Public WebUI Colab URL

*   把这些链接复制到浏览器打开，就是你的在线Stable Diffusion操作面板

![](img/2716c6bc95bacb24b6a8984f704dbf85.png)

![](img/9c062ab3d3ee5a1e129e34c39ada5df3.png)

# 第二部分：实操上手，调模型开始画

## 1. 先下个底模

ChilloutMix是针对亚洲面孔微调的底模，人像效果比原版更自然，很适合做人物。

1.  切到Civitai标签页
1.  Content Type选Checkpoint
1.  勾上Search by term
1.  Search Term填入chilloutmix
1.  点Get List，从Civitai拉取模型列表
1.  在Model里挑chilloutmix
1.  Version选最新版
1.  Model FileName选对应的文件
1.  等待Download Url出现下载链接
1.  点击Download Model
1.  回Colab看下载进度，看到Successful Downloaded就说明搞定

![](img/ec4a7cd12d7d692827b777eb3b4af135.png)

![](img/781019cdf82a79708ae59699b1e94cc2.png)

## 2. 再配个Lora风格包

Lora模型体积小、加载快，能给你的人物加上特定风格或细节。

1.  切到Civitai标签页
1.  Content Type改成Lora
1.  勾上Search by term
1.  Search Term输入你想要的Lora名字
1.  点击Get List加载列表
1.  选择Model、Version、Model FileName
1.  等Download Url生成后点Download Model
1.  在Colab里等Successful Downloaded提示

![](img/e48f374cab0ac119e028457fcfc32d6c.png)

![](img/8426bd20ae6d5a2d9be1dc4c8c3d388f.png)

## 3. 载入底模

1.  切到txt2img标签页
1.  左上角点刷新底模
1.  左侧列表里选刚下载好的ChilloutMix
1.  等界面刷新完成

![](img/7f949fb3610fbb66ff1c5cbe5b66c96d.png)

## 4. 载入Lora

1.  左下角展开Additional Networks
1.  勾上Enable启用Lora
1.  点Refresh Model刷新列表
1.  在Model 1里选择刚下载的Lora模型

![](img/945e81b0696c2c145cae672479647a2e.png)

## 5. 调参出图

1.  填入正向提示词
1.  填入负面提示词
1.  选采样器
1.  设定步数
1.  开启或关闭面部修复
1.  调整CFG Scale
1.  设置画布宽高
1.  点Generate生成

![](img/e5b4e9dbdb39498972da1fbe2c79a1c3.png)

![](img/955b2c4586f24e20b0b91395de052f0a.png)

# 第三部分：把手动变自动，把单张变批量，把有限变无限

## 自动化出图怎么玩

Colab出图速度很快，30秒到1分钟一张。参数调熟练后，鼠标右键Generate按钮，选Generate Forever，就能让它一直循环出图不用管。

![](img/0e7ea7df52d6cd3e2c51d2cd287495ac.png)

## 自动生成的图在哪找

1.  回到Colab主界面
1.  点左侧文件浏览器
1.  路径是 /content/stable-diffusion-webui/outputs/txt2img-images/ + 出图日期
1.  双击图片右侧就能预览

![](img/2153b9a9dd29802df8077656607b0d6f.png)

## 怎么一键打包下载

1.  回Colab界面，先停止运行Stable Diffusion WebUI的代码块
1.  新增一个代码块
1.  把下面这段代码贴进去，把路径改成你自己的图片文件夹
1.  运行后等进度条走完，图片会自动打包下载到本地

```
import os, tarfile

import os
from google.colab import files

def make_targz_one_by_one(output_filename, source_dir):
  tar = tarfile.open(output_filename,"w")
  for root,dir_name,files_list in os.walk(source_dir):
    for file in files_list:
      pathfile = os.path.join(root, file)
      tar.add(pathfile)
  tar.close()

  files.download(output_filename)

#把第二个参数修改为自己图片存放路径 
make_targz_one_by_one('neg_tar', '/content/stable-diffusion-webui/outputs/txt2img-images/2023-04-26')
```

![](img/23ea7a7aae336db915faab512118d6b6.png)

![](img/89baee9f78bf03d2e4c23a97f324b767.png)

## 批量出图怎么做

*   在本地装多个浏览器，比如Chrome、Edge、Firefox
*   每个浏览器登录不同的Google账号，同时开多个WebUI窗口一起跑
*   追求效率的可以用指纹浏览器多开

## 无限出图怎么做

*   免费Colab账号一天大概能用3到6小时GPU
*   想更持久：升级Colab Pro
*   想白嫖：多准备几个Google账号，账号用完就切号，循环使用
*   按5个窗口算，1分钟出3张，1小时就是900张，量完全够用