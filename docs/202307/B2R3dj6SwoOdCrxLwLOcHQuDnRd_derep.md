# MJ 5.2 的 Zoom Out 如何用来做成一段流畅视频
作者：龙哥



Midjourney 最新上线的 5.2 版本，最让人兴奋的就是 Zoom Out 缩放功能被大幅强化。从中延伸出的玩法很多，不仅能把画面外延，还能让同一个主体换上不同场景。这期就带你实操一遍，用 Zoom Out 拼出一组连续画面，再合成视频。

整体流程拆成两步走。先用 MJ 生成素材图，再用 Runway 把序列图做成动画。会用到 Discord 和 Runway 这两个工具，注意都需要🪜环境。

# 第一步：用 MJ 产出可延展的图组

### 1. 锁定初始画面

先写一个提示词来出图，这里直接借用丰年老板昨天分享的一组词：

Poster of real estatecompany, Futurism, a semi mechanical woman with face lens, and urban landscape modelsof different buildings in the background, including detailed science fiction illustrations,safe camera art, realistic super detail rendering, orange, quiet meditation, amazing oceanscene and panel composition technology 8k

![](img/63cdb2575e545b815c89bf82122714b7.png)

在 Discord 里把上面的 prompt 丢进去跑。
第一版出来后风格还算对味，保留 V1 的基调，再按这个方向补出 4 张同伙。

![](img/597fce8b53c2233181bed188cf85a162.png)

第二张的构图更喜欢，就点 u2 进入变体，细化出更满意的细节。

![](img/a03405a9b67f1b92692246fa9f3a4d67.png)

到这里，初始主图就定了。

### 2. 用上新版的 Zoom Out

![](img/f8a27bfcf353a481bd6d45de91da84f0.png)

点击缩放后会弹出三个方向的箭头，分别是 2 倍缩小、1.5 倍缩小和自定义倍数。
这里我们选 Custom Zoom 自定义。

![](img/c16e16af15d3c5da486f66bb9164d47c.png)

弹出的输入框里可以调缩小的倍率，默认是 2 倍。这次我们改成 1.1 倍，然后点蓝色的 Submit 提交。

系统会回传 4 张外延图，从中挑最贴合原图的这一张。这里选的是图四。

![](img/65814952559b18ec791ed1c61d4e34e7.png)

![](img/333ed2ac5111757ebc4c098963ad31ad.png)

把选中的图四先存下来备用。回到第一张初始图，继续做外延，这次把倍率调到 1.2 倍。

![](img/1957cdd604d51b37ae607cfa21f2e683.png)

从这一轮里挑出图一，作为新的基准图继续放大。

![](img/81f6225108c397b3ec2c95cc6cc43fd1.png)

重复同样的缩放操作，把倍率逐步拉到 2 倍。下面直接上连贯的中间结果。

![](img/090923a272c9f3f384471c3cf532ce09.png)

![](img/1c4afdb35547eb7ca193d854337c1eb4.png)

![](img/b1a56e293325df860bb76243c190bf12.png)

![](img/88cdae5a0dec80ceab8361228c8d3f0e.png)

![](img/26c57faaa71ff1d4ff49bc404edb380d.png)

![](img/9602b3868e395f914d011e49297e7137.png)

一套从 1.1 倍、1.2 倍一直到 2 倍的外延序列就齐了，就能进入下一步的视频合成。

小提示：其实也可以把每次新生成的图再拿去继续 Zoom Out，理论上可以一直往外延展。

# 第二步：在 Runway 上做成视频

打开 Runway 官网，先完成注册。

![](img/850e66f5cf454477a408f6a56a2f9819.png)

左侧菜单点进 Generate videos 进入视频生成页。

![](img/d8a51432b8ce0e240c9e6ea71186e9ab.png)

找到 Frame Interpolation 帧插值功能，点击进入。

![](img/3922f9b2e23e9426c31554945bd9708e.png)

把前面在 MJ 保存好的那几张顺序图依次上传上去。

![](img/ab22ceecebd9152eec15e65f0ec871e3.png)

下方可以调节输出时长，左边的红色箭头处就是控制点。调好后点 Generate 开始生成。

![](img/2d4edea08937ce82434022a93edba274.png)

![](img/b463e3aed5b4fe967a78f736e7d56366.png)

渲染完成后可以选分辨率，非会员最高 720p，会员可开 1080p。

![](img/98210dc0bdc26dcaa5f29525ca46029b.png)

最后点下载把成品保存到本地。

![](img/4c1f9bff8bb31507e63b27ed68f8e983.png)

成品效果如下：

就这样，Zoom Out 序列图 + 帧插值，视频就完成了。