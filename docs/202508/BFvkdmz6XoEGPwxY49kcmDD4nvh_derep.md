《影刀RPA实操：PDF/Word批量生成小红书商品笔记，10分钟20篇的全流程拆解》

大家好，我是锦城。最近一直在折腾小红书虚拟电商，成绩算不上亮眼，但好赖把闭环跑通了。这段时间我也写了不少相关脚本：手机端店铺关键词采集、同行商品采集、淘宝/小红书商品采集、商品上架、多账号笔记上传等等。今天重点聊第六个——用PDF或Word直接生成小红书商品笔记。这套东西一旦跑顺，10分钟产出20篇SEO笔记是没问题的，标题、文案、话题、下拉词都能一步到位。

先说句实在话：脚本只能提效，不能直接给你变出钱。我自己的做法是先把所有手动流程跑通，确认能出单，才考虑用影刀来加速。别总想着走捷径，赚钱这事，捷径没那么多。

一、不会Python也能用“魔法指令”

很多朋友在B站看了不少影刀教程，但一到实战就不知道怎么落地。其实影刀里有个很实用的“魔法指令”，官方说明可以看这里![](img/1f522cb214891b234b48218cfb21764e.png)。它支持直接粘贴Python代码，还能自动转成影刀能调用的命令。我自己并不会Python，但可以让Deepseek、豆包这类AI先写代码，再把代码丢给魔法指令改造成可用脚本，很多平时没有现成命令的功能，就这样解决了。

二、笔记模板的两种玩法

目前我常用的有两条路线：

第一种，直接把PDF/Word导出的图片当底图，给图加文字、加背景框、拼四宫格或九宫格，最终组成一篇笔记，效果参考![](img/27606fffff8777a1774e6ef399064f07.png)。

第二种，先自己做好喜欢的模板，把字体、颜色、版式都定好，再往里面填内容，这样原创度更高、观感更好，但做起来也复杂一些，效果参考![](img/0229359f07313a5ef058d7d3b30801ef.png)。

今天主要讲第一种，代码简单，新手容易复刻。演示里我固定生成6张图，你完全可以按自己需要增减。

三、先手动跑通，再谈自动化

这套脚本的思路，说白了就是把手动操作“翻译”成影刀能执行的动作。如果你连手动流程都没做过，凭空想象出来的自动化大概率不靠谱。所以我每个脚本都是先手动折腾一段时间，知道哪一步最卡，写代码时就先攻难点，确定能搞定再补齐其他环节。

手动做笔记的完整链路是：找PDF→导出图片→拼宫格→在图上加文字→让AI写标题/文案/话题。影刀要解决的难点主要有三个：PDF导出图片、图片拼接、文案自动生成。这三个点你不用同时攻克，哪怕只解决其中一个，也能省下不少时间。例如拼接搞不定，可以先借助第三方工具；AI文案搞不定，就手动去Deepseek或豆包里生成，再填进本地文件。影刀只要能帮你提升一部分效率，就已经很值了![](img/b1087bd44f80bfe0b5a2c93b23bc4722.png)![](img/3163718448850141be20943501239ebf.png)![](img/65463dc66af77b34d8423bfe3cb995da.png)。

四、好看的PDF去哪里找

最近刷小红书，我注意到一个现象：很多爆款资料笔记，干脆直接把PDF第一页当成封面，点赞收藏数据都很好。说明这种玩法并不需要多复杂的制作，关键是找到排版漂亮、清晰美观的PDF。比如这种![](img/7b0265930b7ada9c63505aafec4bf6ef.png)![](img/fb0badc2667f9a1b41671edbf0b45aaa.png)![](img/0e7df76ead607152592f927cc8a1a27b.png)![](img/3ca8a0bd7c5e2f7e889e21f01a297992.png)，拿到手几乎不用改。

这种PDF很多是用Word排出来的，自己做非常费时，所以我们完全可以靠“搜”来解决问题。渠道可以是淘宝、拼多多、闲鱼、微信群、学科类小程序等等。还有一些学科小程序也能每天更新资料、支持预览，但需要付费，这里就不具体展开了。

免费且好用的，我重点推荐两个：

1. 微信搜一搜

比如你在小红书看到一条笔记![](img/7967b0e83c4dc8b7e6eea35659cd637a.png)，就拿着关键词去微信搜一搜里找![](img/5d33ee40674464e169ef00a6977d6e3f.png)，经常能找到同款，或者同年级但内容不同的PDF![](img/fc34914ad86da48d2e221026c271426a.png)。很多公众号文章会直接放出PDF，先通过预览确认排版合不合适，合适再下载到本地。

2. 同行微信群

这个很好理解，多潜伏几个卖学科资料的同行群，他们每天都会发新资料![](img/7d0e2ebf4433901f74ea65aecf96de79.png)![](img/2989a672bf042cb55fe4469c245b48c4.png)，看到排版好看的直接拿来做成笔记。不只是小学、初中资料，考公、考研等类目也能这么玩。如果是做搜索流量，有些资料甚至不要求排版多精美，关键词布局好、封面过得去就行。

五、把PDF/Word变成图片

这一步有几种做法。

先说WPS自带的“导出图片”功能![](img/cad9bc5e64982f5eea3bf0be9a678015.png)。能用，但部分能力要会员，而且文件一多，就得不停地点导出、选目录、命名，非常繁琐。

再看影刀。第一种是影刀自带命令，直接在指令框搜“PDF”![](img/60c41004b14b2594f7b8cc9191af27ae.png)，把PDF路径和保存目录填进去点运行就行![](img/d3edd48ab1501f6d83ea4c65c72d6060.png)。不过实测下来，自带命令偶尔会导出失败，或者图片顺序错乱。

如果你也遇到这种情况，可以试试影刀魔法指令。直接告诉它需求，比如“导出PDF所有图片，按0、1、2、3……命名，保存到自定义文件夹”![](img/1ca6a72713e3fd63039f94ffef768658.png)。点一下“优化提问”![](img/5ecaaa6455601bbde9b2f99ed36d3a12.png)，等它把问题优化得更清楚，再把提示词发给魔法指令生成代码![](img/71404020e2450c099eb81717248749d5.png)。第一次生成的结果如果不对，就继续反馈“图片不完整”或“不是完整图片”，让它调整。还要注意，魔法指令每周提问次数有限，大约150次，简单命令自己写就好，复杂的再交给它。

对比一眼：自带命令的效果![](img/196c660859be04c7666842aafd2aa0fc.png)，魔法指令的效果![](img/c03486675945edb8062eeba0606d7db5.png)，后者明显更稳。

六、标题、文案、话题怎么自动生成

三种方法都可以用：

1. 对接影刀AI Power工作流

把大模型和提示词提前配置在工作流里，影刀直接调用并传参，返回结果就能用![](img/fa66b28323cd1d542108a33b579c6797.png)![](img/fff5b499d8dfd331b2ddd2eaa0fc29fd.png)![](img/d3c8c45e3c52127a5aa812b475b26dc4.png)。

2. 影刀内置AI大语言模型

影刀自带调用主流AI的命令，需要先充值，然后提交提示词和参数，内容质量基本由提示词决定![](img/e0bc10876a87fd15d881808087513872.png)。

3. 闲鱼买“硅基流动”key

我目前就是用这个，闲鱼上买一个key大概0.5元![](img/d501b5372761c3e432c6a94e04855c4c.png)![](img/119e746ea21c5dc4c9de1b811d0fd543.png)，商家会发教程，一个key大约够用半个月。可以多备几个key，代码里写清楚：第一个key失效就自动切换第二个，如果都失效了，用影刀微信通知提醒，再手动删掉坏key就好。

提交给AI的参数，至少要有PDF文件名，比如“六年级上册语文句子专项练习.pdf”，让AI知道资料大概是什么；再加上核心关键词，也就是原始下拉词和加A/Z字母的下拉词，这样生成出来的笔记才更符合SEO逻辑。提示词我这里就不放了，怕大家生成出来的内容都一个样![](img/3d64810dc9d26770aae65a8e7a82823c.png)。

七、图片原创度不够怎么办

按上面的流程做，有些笔记可能没流量，甚至被判“非原创”或“搬运图片”。图片去重其实不外乎几个办法：封面加大标题小标题、调亮度对比度饱和度、加背景、拼四宫格/九宫格。人工用美图秀秀也能做，但一套笔记6张图慢慢调，太费时间，更适合交给影刀批量处理。

我手里有几个用Deepseek写好的Python脚本![](img/66ac3cf17d46ea78ec5fb6832005cc94.png)，直接复制给魔法指令，让它“改成影刀可用的格式”就行。实操下来几个功能都很好用：

- 图片加文字![](img/3075a68ca8f2de864a0f8b9ba259ef4b.png)：把py代码粘贴给魔法指令![](img/8bfad6a42e08ca8b82cbd61ce1b63f34.png)，生成后效果见![](img/e5c70f19c8c7f24c45cdb9f5d1a35cc1.png)![](img/a0c7ac4f7454933d66bf49cd9cce7c36.png)，文字、字体、大小、描边宽度都能自定义。
- 图片拼接![](img/e6be9bbccc8e6b8b04f33cda96aa1db1.png)：让魔法指令生成四宫格或九宫格拼接脚本。
- 图片微调![](img/80d600320d89f6fa1195abb003915cf1.png)：把亮度、对比度、饱和度等参数直接发过去。
- 图片加背景框![](img/b2ddb17668be31caeeb47de0d51a3353.png)：同样一句话搞定。

经过这波处理，原创度基本就上来了，笔记也能放心投薯条。另外提醒一句：生成文案时，要让AI避开“点赞、收藏、私信、关注”这类诱导词，否则容易触发违规。

八、模板怎么选

我最早的模板是“144991”：首图封面上加文字，中间放两个四宫格、两个九宫格，最后再接一张单图。这个模板能出单，但朋友提醒我，第2到第5张图如果让用户看不清资料内容，转化就会打折扣。后来就改成了“111149”模板：首图封面+文字，接着三张单图，再放一个四宫格+文字，一个九宫格+文字。

我们今天就按6图来举例。因为很多PDF本身只有10多页，也就是10多张图，如果强行做8图或10图，随机抽取时很容易抽到重复的。

九、落地时的文件夹结构

真正写代码时，先按PDF文件名建主文件夹。比如PDF路径是“D:\Desktop\生成图片的pdf\2025国考申论范文100篇.pdf”，就建一个“2025国考申论范文100篇”文件夹，然后在里面新建四个子文件夹，分别存放不同处理阶段的图片。这样影刀在跑流程时，输出文件不会乱，后续拼接、加字、加背景也都有据可查。

其实整套脚本拆开看并不复杂，关键是把导出图片、加字、拼接、加背景这几步用影刀命令串起来。对新手来说，影刀就像搭积木，把对应命令拖过来就行。希望这篇文章能帮你少走点弯路，也祝你在小红书虚拟电商这条路上，早日跑通属于自己的闭环。

今天分享一套超实用的自动化玩法，教你把“2025国考申论范文100篇”这类PDF，做成小红书笔记图片，还能自动搞下拉词、标题和文案。全程靠影刀就能跑，新手也能照着做。

先把手头素材理清楚：单图文件夹、四宫格文件夹、九宫格文件夹、成品笔记文件夹，一个都不能少。 ![](img/1eeca0a04dd47e71558b5e10683fbf36.png) ![](img/a475e4de34a43377100705207e941a0b.png) ![](img/fad564fa00db598b24b7a33dcffd7ed7.png) ![](img/bb2582011f9ce0a45f0aeb7774d2ec5a.png)

第一步，先判断PDF页数。页数少于4页的直接放弃，压根不值得做；页数在4到9之间，就跳过九宫格文件夹——因为图不够，拼不出九宫格。

接下来，把PDF导出成图片，统一丢进单图文件夹。 ![](img/c99b60bbdeb4e1d8e63a82d29df444a4.png)

第二步，拼接图片。直接调用四宫格或九宫格的魔法指令，把单图里的图片组合到一起，再放进对应文件夹。 ![](img/fad8c47666f4766c0912c0dc3882bce8.png) ![](img/a3e8dff0d9fab93554f63d9aceee0453.png)

到这一步，所有图片都备齐了，接下来就能自由加背景框、加文字了。

先说封面图思路。我习惯直接取单图文件夹的第一张图，也就是PDF的第一页，通常自带大标题，再人工补两行字，就能当封面。直接生成到成品笔记目录，命名为0.png。上传时按数字从小到大传，0自然排最前。 ![](img/1b0ebdf2e0fa471cb1e74c17f4b0b2ab.png) ![](img/8f3283906aca0a41542beeffffac30d5.png)

第2、3、4张图思路一样：从单图文件夹随机抽一张，分别命名成1.png、2.png、3.png。但有个坑——PDF页数少时，随机抽很容易抽到同一张。所以得加个判断：页数多的话，每次抽完就把那张图挪到临时文件夹，等抽完了再移回去；页数少的话，干脆直接拷贝第2、3、4页。 ![](img/10fbfa54da27113d42a1467828fc1166.png) ![](img/a3863e377f9056726cfec822efb2cf84.png)

第5张我用四宫格，第6张用九宫格：随机抽取，需要背景就加背景，然后移进成品文件夹。 ![](img/13083d9b934bf7a761e6a64a10af5ed9.png) ![](img/a225a74e2ff7c9596904c64604f6d1e3.png) ![](img/e7a4b9941ab9c4d1d3ec641d56639925.png) ![](img/46b902bae22990b13b712a691902287a.png) 最后给第五张四宫格、第六张九宫格加上对应文字。 ![](img/b5696a2a3ebcbc029b8b0ee813ab2ced.png) ![](img/2cc47a1ce25e19e08fb8f45758b6b6bf.png)

到这里，图片部分全部搞定，下面说下拉词。

先看完整代码截图。 ![](img/280753c06876a6e4ebe730391dc6b829.png)

获取Cookie的方法：打开小红书网页版，登录账号，按F12，右上角选Network（中文界面叫“网络”），然后搜一下，在右侧找到Cookies，直接写进代码第一行的变量里。 ![](img/4d0cfb20ecfe7ed1b2c448d0397944ca.png) ![](img/dd6e39fbc4655e4e9d6d24349c7f5dfd.png) ![](img/7c5d93f486af1ede7f1d3f4382a87c4e.png) ![](img/f3d1f3cf022ca6f1772cb7aa2e467a15.png)

请求地址里word=后面的关键词换成你的核心词，网页就会返回下拉词，再用魔法指令提取出来。 ![](img/771911d20ddcf750201bf9e53278c87e.png) ![](img/4b9a74892380ba731c43701dfe57bd9a.png)

为了挖得更深，我建了一个a-z的字母列表，循环把每个字母加到搜索词后面，这样就能拿到核心词和字母扩展的所有下拉词，最后汇总成一个列表。 ![](img/9bdf42ef64660d6687da3a586ad7e906.png) ![](img/8c3d0fb755f3f159276a16f83957117c.png)

这样得到一组完整下拉词，既有原始词，也有字母扩展词，一起丢给AI，让它生成SEO标题、文案和话题。 ![](img/03b88f0c6706e0b66caa977319841e85.png) ![](img/3e19b2e826922bab4f98fca59bb291b7.png) ![](img/cb79cf7b41a024b59ad0b176d94ac816.png) ![](img/0db3f3648e2d58e963cea2b2a27cf80c.png)

文案部分可以翻影刀代码思路第三部分，那里专门讲了怎么对接大语言模型，生成完整笔记标题、文案、话题。

重点提醒：不需要把所有PDF都上架到小红书店铺。哪怕资料再多，也只上架一个商品就行。 ![](img/f503c9616d7ced199b73f13f8d7a2e04.png) 用户下单后，让他发笔记截图给你，你再把网盘链接发给他。

视频讲解在这里。 ![](img/84d02aafa1316c1771a88f7828134bb3.png) 另外还有全流程代码长截图，以及部分魔法指令（比如给图片添加文字）都在下面，直接抄作业就行。

```
# pip install pillow

from PIL import Image, ImageDraw, ImageFont
import os

from typing import *
try:
    from xbot.app.logging import trace as print
except:
    from xbot import print

def add_text_to_image(image_path, text1, text2, font_path=None, font_size=110, 
                     text_color="#f7c643", stroke_color="#000000", stroke_width=9, 
                     background_color=None, text_spacing=None, 
                     text_bg_color="#000000", text_bg_opacity=128, 
                     text_bg_padding=20, use_auto_size_bg=True):
    """
    title: 为单张图片添加带背景的文字水印
    description: 为指定图片添加两行文字水印，每行文字可带有矩形背景，可自定义文字内容、字体、颜色、背景等样式，处理后直接覆盖原图片。
    inputs:
        - image_path (file): 需要处理的图片文件路径，eg: "D:/图片素材/示例图片.jpg"
        - text1 (str): 第一行文字内容，eg: "Pdf高清电子文档"
        - text2 (str): 第二行文字内容，eg: "排版整洁&打印清晰"
        - font_path (str): 字体文件路径，留空使用系统默认字体，eg: "C:/Windows/Fonts/simhei.ttf"
        - font_size (int): 字体大小，eg: 110
        - text_color (str): 文字颜色(十六进制)，eg: "#f7c643"
        - stroke_color (str): 描边颜色(十六进制)，eg: "#000000"
        - stroke_width (int): 描边宽度，eg: 9
        - background_color (str): 整个图片的背景颜色(十六进制)，留空表示不修改背景，eg: "#ffffff"
        - text_spacing (int): 文字间距(像素)，决定两行文字与中线的距离，留空使用默认值，eg: 100
        - text_bg_color (str): 文字背景矩形的颜色(十六进制)，eg: "#000000"
        - text_bg_opacity (int): 文字背景矩形的透明度(0-255)，0为完全透明，255为不透明，eg: 128
        - text_bg_padding (int): 文字背景矩形的内边距(像素)，eg: 20
        - use_auto_size_bg (bool): 是否让背景矩形尺寸自动跟随文字，True为自动，False为固定宽度使用图片宽度，eg: True
    outputs:
        - success (bool): 处理结果，True表示成功，False表示失败，eg: True
    """

    # 参数验证
    if not os.path.isfile(image_path):
        raise ValueError(f"图片文件不存在: {image_path}")

    # 将颜色从十六进制转换为RGB元组
    def _hex_to_rgb(hex_color):
        if not hex_color:
            return None
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    text_color_rgb = _hex_to_rgb(text_color)
    stroke_color_rgb = _hex_to_rgb(stroke_color)
    background_color_rgb = _hex_to_rgb(background_color)
    text_bg_color_rgb = _hex_to_rgb(text_bg_color)

    # 添加透明度到文字背景颜色
    text_bg_color_rgba = text_bg_color_rgb + (text_bg_opacity,)

    # 寻找可用的字体
    def _find_font():
        if font_path and os.path.exists(font_path):
            return font_path

        # 尝试常见字体路径
        default_fonts = [
            r'C:\Windows\Fonts\simhei.ttf',  # 黑体
            r'C:\Windows\Fonts\simsun.ttc',  # 宋体
            r'C:\USERS\ADMINISTRATOR\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\汉仪润圆-55.TTF'
        ]

        for path in default_fonts:
            if os.path.exists(path):
                return path

        return None  # 使用默认字体

    font_file = _find_font()

    try:
        # 打开图片
        image = Image.open(image_path)

        # 如果指定了背景颜色，创建新的背景并粘贴原图
        if background_color_rgb:
            new_image = Image.new('RGB', image.size, background_color_rgb)
            new_image.paste(image, (0, 0))
            image = new_image

        # 确保图片有Alpha通道，以便添加半透明背景
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        width, height = image.size

        # 创建一个透明层用于绘制文字和背景
        overlay = Image.new('RGBA', image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        # 尝试加载字体文件
        try:
            font = ImageFont.truetype(font_file, font_size) if font_file else ImageFont.load_default()
        except Exception as e:
            print(f"加载字体失败: {e}")
            font = ImageFont.load_default()

        # 兼容不同版本的PIL库，处理textbbox方法不存在的情况
        def _get_text_size(text, font):
            try:
                # 尝试使用textbbox方法（PIL 8.0.0及以上版本）
                bbox = draw.textbbox((0, 0), text, font=font)
                return bbox[2] - bbox[0], bbox[3] - bbox[1]
            except AttributeError:
                # 回退到使用textsize方法（旧版本PIL）
                try:
                    return draw.textsize(text, font=font)
                except AttributeError:
                    # 如果textsize也不存在，使用getsize方法（更旧的版本）
                    return font.getsize(text)

        # 计算文字尺寸
        text1_width, text1_height = _get_text_size(text1, font)
        text2_width, text2_height = _get_text_size(text2, font)

        # 计算中心线
        center_y = height // 2

        # 默认间距是图片高度的1/6，可由用户自定义
        default_spacing = height // 6
        spacing = text_spacing if text_spacing is not None else default_spacing

        # 计算文字位置，使两行文字距离中线相等
        y1 = center_y - spacing - text1_height // 3
        y2 = center_y + spacing - text2_height // 2

        # 第一行文字居中
        x1 = (width - text1_width) // 2

        # 绘制第一行文字的背景矩形
        if use_auto_size_bg:
            # 自动尺寸背景，根据文字大小加上内边距
            bg1_left = x1 - text_bg_padding
            bg1_top = y1 - text_bg_padding
            bg1_right = x1 + text1_width + text_bg_padding
            bg1_bottom = y1 + text1_height + text_bg_padding
        else:
            # 固定宽度背景，使用图片宽度
            bg1_left = 0
            bg1_top = y1 - text_bg_padding
            bg1_right = width
            bg1_bottom = y1 + text1_height + text_bg_padding

        draw.rectangle([bg1_left, bg1_top, bg1_right, bg1_bottom], fill=text_bg_color_rgba)

        # 第二行文字居中
        x2 = (width - text2_width) // 2

        # 绘制第二行文字的背景矩形
        if use_auto_size_bg:
            # 自动尺寸背景，根据文字大小加上内边距
            bg2_left = x2 - text_bg_padding
            bg2_top = y2 - text_bg_padding
            bg2_right = x2 + text2_width + text_bg_padding
            bg2_bottom = y2 + text2_height + text_bg_padding
        else:
            # 固定宽度背景，使用图片宽度
            bg2_left = 0
            bg2_top = y2 - text_bg_padding
            bg2_right = width
            bg2_bottom = y2 + text2_height + text_bg_padding

        draw.rectangle([bg2_left, bg2_top, bg2_right, bg2_bottom], fill=text_bg_color_rgba)

        # 在透明层上绘制文字
        draw.text((x1, y1), text1, fill=text_color_rgb, font=font,
                  stroke_width=stroke_width, stroke_fill=stroke_color_rgb)
        draw.text((x2, y2), text2, fill=text_color_rgb, font=font,
                  stroke_width=stroke_width, stroke_fill=stroke_color_rgb)

        # 将透明层合并到原图
        result = Image.alpha_composite(image, overlay)

        # 如果原图没有Alpha通道，转回RGB模式
        if image.mode != 'RGBA':
            result = result.convert('RGB')

        # 保存处理后的图片（覆盖原图）
        result.save(image_path, quality=95)
        print(f"成功处理图片: {image_path}")
        return True
    except Exception as e:
        print(f"处理图片时出错: {e}")
        return False

```

### 2. 照片拼贴：双行双列与三行三列布局

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
# 使用此指令前，请确保安装必要的Python库，例如使用以下命令安装：
# pip install Pillow

import os
import re
import gc
import traceback
from PIL import Image, ImageDraw

from typing import *
try:
    from xbot.app.logging import trace as print
except:
    from xbot import print

def create_image_grid(input_folder, output_folder, grid_type=4, num_grids=None):
    """
    title: 图片拼图工具
    description: 将图片文件夹中的所有图片按指定行列数拼接成网格，自动在图片间添加灰色间隙。可指定生成的拼图数量，每个拼图左上角始终是序号最小的图片。
    inputs: 
        - input_folder (folder): 包含图片的输入文件夹路径，eg: "D:/images"
        - output_folder (folder): 拼图结果的保存路径，eg: "D:/output"
        - grid_type (int): 拼图类型，4表示四宫格(2x2)，9表示九宫格(3x3)，eg: 4
        - num_grids (int): 要生成的拼图数量(可选)，不指定或为0时会根据图片数量自动计算，eg: 3
    outputs: 
        - output_paths (list): 生成的拼图图片路径列表，eg: ["D:/output/四宫格_0.png"]
    """
    # 禁用PIL的像素限制
    Image.MAX_IMAGE_PIXELS = None

    # 定义背景图片的尺寸
    BACKGROUND_WIDTH = 1242
    BACKGROUND_HEIGHT = 1656
    # 定义图片之间的空隙大小
    GAP = 10
    # 定义淡灰色，用于空隙颜色
    GRAY_COLOR = (220, 220, 220)
    # 图片最大尺寸，用于降低内存使用
    MAX_IMAGE_SIZE = (800, 800)

    # 打印所有输入参数，帮助调试
    print(f"输入参数: input_folder={input_folder}, output_folder={output_folder}, grid_type={grid_type}, num_grids={num_grids}")

    try:
        # 标准化路径，确保路径格式正确
        input_folder = os.path.normpath(input_folder)
        output_folder = os.path.normpath(output_folder)

        # 检查输入有效性
        if not os.path.isdir(input_folder):
            print(f"输入文件夹不存在: {input_folder}")
            raise ValueError(f"输入文件夹不存在: {input_folder}")

        # 确保num_grids是整数
        if num_grids is not None:
            try:
                num_grids = int(num_grids)
                print(f"用户指定的拼图数量: {num_grids}")
                if num_grids <= 0:
                    num_grids = None
                    print("拼图数量小于或等于0，将使用自动计算的数量")
            except (TypeError, ValueError):
                print(f"无效的拼图数量: {num_grids}，将使用自动计算的数量")
                num_grids = None

        # 确保输出文件夹存在
        os.makedirs(output_folder, exist_ok=True)

        # 确定网格行列数
        if int(grid_type) == 4:
            rows, cols = 2, 2
            grid_name = "四宫格"
            cells_per_grid = 4
        else:  # grid_type == 9
            rows, cols = 3, 3
            grid_name = "九宫格"
            cells_per_grid = 9

        print(f"开始处理: 输入文件夹 {input_folder}, 输出文件夹 {output_folder}, 网格类型 {grid_name}")

        def _create_background():
            """创建一个指定尺寸的白色背景图片"""
            return Image.new('RGB', (BACKGROUND_WIDTH, BACKGROUND_HEIGHT), color='white')

        def _resize_image(img, target_width, target_height):
            """调整图片大小以适应目标尺寸，同时保持图片的高清晰度"""
            # 计算调整大小后的尺寸，保持原始宽高比
            width, height = img.size
            ratio = min(target_width / width, target_height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)

            # 使用 LANCZOS 提高清晰度
            try:
                return img.resize((new_width, new_height), Image.LANCZOS)
            except AttributeError:
                # 对于较新版本的Pillow
                return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        def _load_image_with_reduced_size(image_path):
            """以较低分辨率加载图片，减少内存使用"""
            try:
                # 打开图片但不立即加载
                img = Image.open(image_path)

                # 如果图片大于最大尺寸，先缩小它
                if img.width > MAX_IMAGE_SIZE[0] or img.height > MAX_IMAGE_SIZE[1]:
                    img.thumbnail(MAX_IMAGE_SIZE, Image.LANCZOS)

                # 将图片转换为RGB模式，减少内存使用
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                print(f"成功加载图片: {os.path.basename(image_path)}, 尺寸: {img.size}")
                return img
            except Exception as e:
                print(f"加载图片 {image_path} 时出错: {e}")
                # 创建一个小的替代图片
                return Image.new('RGB', (100, 100), color=(200, 200, 200))

        def _arrange_images(image_paths, rows, cols, first_image_path):
            """将图片按照指定的行列数排列在背景图片上，一次只加载一张图片以节省内存"""
            # 创建白色背景图片
            background = _create_background()
            draw = ImageDraw.Draw(background)

            # 计算每个单元格的宽度和高度
            cell_width = (BACKGROUND_WIDTH - (cols + 1) * GAP) // cols
            cell_height = (BACKGROUND_HEIGHT - (rows + 1) * GAP) // rows

            # 绘制水平间隙线
            for i in range(1, rows):
                y_pos = i * (cell_height + GAP)
                draw.rectangle((0, y_pos, BACKGROUND_WIDTH, y_pos + GAP), fill=GRAY_COLOR)

            # 绘制垂直间隙线
            for j in range(1, cols):
                x_pos = j * (cell_width + GAP)
                draw.rectangle((x_pos, 0, x_pos + GAP, BACKGROUND_HEIGHT), fill=GRAY_COLOR)

            # 计算每个图片的位置
            positions = []
            for i in range(rows):
                for j in range(cols):
                    x = GAP + j * (cell_width + GAP)
                    y = GAP + i * (cell_height + GAP)
                    positions.append((x, y))

            # 加载并放置第一张图片（序号最小的图片）
            first_img = _load_image_with_reduced_size(first_image_path)
            resized_first_img = _resize_image(first_img, cell_width, cell_height)
            x, y = positions[0]
            x_offset = (cell_width - resized_first_img.width) // 2
            y_offset = (cell_height - resized_first_img.height) // 2
            background.paste(resized_first_img, (x + x_offset, y + y_offset))

            # 释放第一张图片的内存
            del first_img
            del resized_first_img
            gc.collect()

            # 粘贴其余图片到对应位置
            for i in range(1, len(positions)):  # 从位置1开始，位置0已经放了序号最小的图片
                if i-1 < len(image_paths):  # 注意索引调整，因为image_paths不包括第一张图片
                    # 加载图片
                    img = _load_image_with_reduced_size(image_paths[i-1])

                    # 调整图片大小
                    resized_img = _resize_image(img, cell_width, cell_height)

                    # 获取图片要放置的位置
                    x, y = positions[i]

                    # 计算图片在目标区域内居中的偏移量
                    x_offset = (cell_width - resized_img.width) // 2
                    y_offset = (cell_height - resized_img.height) // 2

                    # 将图片粘贴到背景图上的指定位置
                    background.paste(resized_img, (x + x_offset, y + y_offset))

                    # 释放图片对象，减少内存使用
                    del img
                    del resized_img
                    gc.collect()

            return background

        def _natural_sort_key(s):
            """使用自然排序算法对文件名进行排序，识别文件名中的数字部分"""
            return [int(text) if text.isdigit() else text.lower() 
                    for text in re.split(r'(\d+)', os.path.basename(s))]

        # 主处理函数
        output_paths = []

        # 获取输入文件夹中的所有图片文件
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
        image_files = []

        try:
            # 列出目录内容，捕获可能的编码错误
            dir_content = os.listdir(input_folder)
            print(f"成功列出目录内容，共 {len(dir_content)} 个文件或文件夹")

            for file in dir_content:
                file_path = os.path.join(input_folder, file)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(file)[1].lower()
                    if ext in image_extensions:
                        image_files.append(file_path)

            print(f"在输入文件夹中找到 {len(image_files)} 个图片文件")
        except Exception as e:
            print(f"列出目录内容时出错: {e}")
            print(traceback.format_exc())

        if not image_files:
            print(f"在 {input_folder} 中没有找到图片文件，退出处理")
            return []

        # 使用自然排序算法对图片文件进行排序（比如0.png, 1.png, 2.png，...，10.png）
        image_files.sort(key=_natural_sort_key)
        print(f"按自然顺序排序后的第一个文件: {os.path.basename(image_files[0])}")

        # 记录最小序号图片的路径
        first_image_path = image_files[0]
        print(f"序号最小的图片是: {os.path.basename(first_image_path)}")

        # 确定要生成的网格数量
        if num_grids is None:
            # 自动计算可以生成的完整网格数量
            calculated_num_grids = max(3, (len(image_files) + cells_per_grid - 1) // cells_per_grid)
            num_grids = calculated_num_grids
            print(f"自动计算的拼图数量: {num_grids}")

        print(f"将生成 {num_grids} 个{grid_name}")

        # 处理每一个网格
        for grid_index in range(int(num_grids)):  # 确保num_grids是整数
            try:
                print(f"开始处理第 {grid_index+1}/{num_grids} 个网格")

                # 为当前网格选择图片路径，第一个位置总是序号最小的图片
                grid_image_paths = []

                # 计算需要多少张图片来填充剩余的格子
                remaining_cells = cells_per_grid - 1

                # 如果有足够的图片，不需要重复
                if len(image_files) - 1 >= remaining_cells:
                    # 从第二张图片开始选择，避免重复使用第一张
                    start_idx = 1 + (grid_index * remaining_cells) % (len(image_files) - 1)
                    for i in range(remaining_cells):
                        img_idx = (start_idx + i) % len(image_files)
                        if img_idx == 0:  # 跳过序号最小的图片
                            img_idx = 1
                        grid_image_paths.append(image_files[img_idx])
                else:
                    # 需要重复使用图片
                    # 首先添加所有剩余的图片（除了第一张）
                    for i in range(1, len(image_files)):
                        grid_image_paths.append(image_files[i])

                    # 如果还不够，循环添加图片直到填满
                    remaining_needed = remaining_cells - len(grid_image_paths)
                    if remaining_needed > 0:
                        print(f"需要额外重复 {remaining_needed} 张图片")
                        repeat_idx = 0
                        while len(grid_image_paths) < remaining_cells:
                            idx_to_use = 1 + (repeat_idx % (len(image_files) - 1))
                            grid_image_paths.append(image_files[idx_to_use])
                            repeat_idx += 1

                # 确保只使用需要的图片数量
                grid_image_paths = grid_image_paths[:remaining_cells]

                print(f"处理第 {grid_index+1} 个网格，共 {cells_per_grid} 个位置，第1个位置为序号最小的图片，其余 {len(grid_image_paths)} 个位置为其他图片")

                # 进行图片排列和拼图
                combined_image = _arrange_images(grid_image_paths, rows, cols, first_image_path)

                # 构建输出文件的文件名
                output_filename = f"{grid_name}_{grid_index}.png"
                output_path = os.path.join(output_folder, output_filename)

                # 保存拼图结果
                print(f"保存拼图到: {output_path}")
                combined_image.save(output_path)
                output_paths.append(output_path)
                print(f"已成功保存拼图图片到 {output_path}")

                # 释放资源
                del combined_image
                gc.collect()

            except Exception as e:
                print(f"处理网格 {grid_index} 时出错: {e}")
                print(traceback.format_exc())

        if not output_paths:
            print("没有生成任何拼图图片，请检查输入文件夹中的图片是否有效。")
        else:
            print(f"总共生成了 {len(output_paths)} 张拼图图片。")

        return output_paths

    except Exception as e:
        print(f"发生错误: {e}")
        print(traceback.format_exc())
        return []

```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
# 使用此指令前，请确保安装必要的Python库，例如使用以下命令安装：
# pip install Pillow

import os
import re
import gc
import traceback
from PIL import Image, ImageDraw

from typing import *
try:
    from xbot.app.logging import trace as print
except:
    from xbot import print

def create_image_grid(input_folder, output_folder, grid_type=4, num_grids=None):
    """
    title: 图片拼图工具
    description: 将图片文件夹中的所有图片按指定行列数拼接成网格，自动在图片间添加灰色间隙。可指定生成的拼图数量，每个拼图左上角始终是序号最小的图片。
    inputs: 
        - input_folder (folder): 包含图片的输入文件夹路径，eg: "D:/images"
        - output_folder (folder): 拼图结果的保存路径，eg: "D:/output"
        - grid_type (int): 拼图类型，4表示四宫格(2x2)，9表示九宫格(3x3)，eg: 4
        - num_grids (int): 要生成的拼图数量(可选)，不指定或为0时会根据图片数量自动计算，eg: 3
    outputs: 
        - output_paths (list): 生成的拼图图片路径列表，eg: ["D:/output/四宫格_0.png"]
    """
    # 禁用PIL的像素限制
    Image.MAX_IMAGE_PIXELS = None

    # 定义背景图片的尺寸
    BACKGROUND_WIDTH = 1242
    BACKGROUND_HEIGHT = 1656
    # 定义图片之间的空隙大小
    GAP = 10
    # 定义淡灰色，用于空隙颜色
    GRAY_COLOR = (220, 220, 220)
    # 图片最大尺寸，用于降低内存使用
    MAX_IMAGE_SIZE = (800, 800)

    # 打印所有输入参数，帮助调试
    print(f"输入参数: input_folder={input_folder}, output_folder={output_folder}, grid_type={grid_type}, num_grids={num_grids}")

    try:
        # 标准化路径，确保路径格式正确
        input_folder = os.path.normpath(input_folder)
        output_folder = os.path.normpath(output_folder)

        # 检查输入有效性
        if not os.path.isdir(input_folder):
            print(f"输入文件夹不存在: {input_folder}")
            raise ValueError(f"输入文件夹不存在: {input_folder}")

        # 确保num_grids是整数
        if num_grids is not None:
            try:
                num_grids = int(num_grids)
                print(f"用户指定的拼图数量: {num_grids}")
                if num_grids <= 0:
                    num_grids = None
                    print("拼图数量小于或等于0，将使用自动计算的数量")
            except (TypeError, ValueError):
                print(f"无效的拼图数量: {num_grids}，将使用自动计算的数量")
                num_grids = None

        # 确保输出文件夹存在
        os.makedirs(output_folder, exist_ok=True)

        # 确定网格行列数
        if int(grid_type) == 4:
            rows, cols = 2, 2
            grid_name = "四宫格"
            cells_per_grid = 4
        else:  # grid_type == 9
            rows, cols = 3, 3
            grid_name = "九宫格"
            cells_per_grid = 9

        print(f"开始处理: 输入文件夹 {input_folder}, 输出文件夹 {output_folder}, 网格类型 {grid_name}")

        def _create_background():
            """创建一个指定尺寸的白色背景图片"""
            return Image.new('RGB', (BACKGROUND_WIDTH, BACKGROUND_HEIGHT), color='white')

        def _resize_image(img, target_width, target_height):
            """调整图片大小以适应目标尺寸，同时保持图片的高清晰度"""
            # 计算调整大小后的尺寸，保持原始宽高比
            width, height = img.size
            ratio = min(target_width / width, target_height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)

            # 使用 LANCZOS 提高清晰度
            try:
                return img.resize((new_width, new_height), Image.LANCZOS)
            except AttributeError:
                # 对于较新版本的Pillow
                return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        def _load_image_with_reduced_size(image_path):
            """以较低分辨率加载图片，减少内存使用"""
            try:
                # 打开图片但不立即加载
                img = Image.open(image_path)

                # 如果图片大于最大尺寸，先缩小它
                if img.width > MAX_IMAGE_SIZE[0] or img.height > MAX_IMAGE_SIZE[1]:
                    img.thumbnail(MAX_IMAGE_SIZE, Image.LANCZOS)

                # 将图片转换为RGB模式，减少内存使用
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                print(f"成功加载图片: {os.path.basename(image_path)}, 尺寸: {img.size}")
                return img
            except Exception as e:
                print(f"加载图片 {image_path} 时出错: {e}")
                # 创建一个小的替代图片
                return Image.new('RGB', (100, 100), color=(200, 200, 200))

        def _arrange_images(image_paths, rows, cols, first_image_path):
            """将图片按照指定的行列数排列在背景图片上，一次只加载一张图片以节省内存"""
            # 创建白色背景图片
            background = _create_background()
            draw = ImageDraw.Draw(background)

            # 计算每个单元格的宽度和高度
            cell_width = (BACKGROUND_WIDTH - (cols + 1) * GAP) // cols
            cell_height = (BACKGROUND_HEIGHT - (rows + 1) * GAP) // rows

            # 绘制水平间隙线
            for i in range(1, rows):
                y_pos = i * (cell_height + GAP)
                draw.rectangle((0, y_pos, BACKGROUND_WIDTH, y_pos + GAP), fill=GRAY_COLOR)

            # 绘制垂直间隙线
            for j in range(1, cols):
                x_pos = j * (cell_width + GAP)
                draw.rectangle((x_pos, 0, x_pos + GAP, BACKGROUND_HEIGHT), fill=GRAY_COLOR)

            # 计算每个图片的位置
            positions = []
            for i in range(rows):
                for j in range(cols):
                    x = GAP + j * (cell_width + GAP)
                    y = GAP + i * (cell_height + GAP)
                    positions.append((x, y))

            # 加载并放置第一张图片（序号最小的图片）
            first_img = _load_image_with_reduced_size(first_image_path)
            resized_first_img = _resize_image(first_img, cell_width, cell_height)
            x, y = positions[0]
            x_offset = (cell_width - resized_first_img.width) // 2
            y_offset = (cell_height - resized_first_img.height) // 2
            background.paste(resized_first_img, (x + x_offset, y + y_offset))

            # 释放第一张图片的内存
            del first_img
            del resized_first_img
            gc.collect()

            # 粘贴其余图片到对应位置
            for i in range(1, len(positions)):  # 从位置1开始，位置0已经放了序号最小的图片
                if i-1 < len(image_paths):  # 注意索引调整，因为image_paths不包括第一张图片
                    # 加载图片
                    img = _load_image_with_reduced_size(image_paths[i-1])

                    # 调整图片大小
                    resized_img = _resize_image(img, cell_width, cell_height)

                    # 获取图片要放置的位置
                    x, y = positions[i]

                    # 计算图片在目标区域内居中的偏移量
                    x_offset = (cell_width - resized_img.width) // 2
                    y_offset = (cell_height - resized_img.height) // 2

                    # 将图片粘贴到背景图上的指定位置
                    background.paste(resized_img, (x + x_offset, y + y_offset))

                    # 释放图片对象，减少内存使用
                    del img
                    del resized_img
                    gc.collect()

            return background

        def _natural_sort_key(s):
            """使用自然排序算法对文件名进行排序，识别文件名中的数字部分"""
            return [int(text) if text.isdigit() else text.lower() 
                    for text in re.split(r'(\d+)', os.path.basename(s))]

        # 主处理函数
        output_paths = []

        # 获取输入文件夹中的所有图片文件
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp']
        image_files = []

        try:
            # 列出目录内容，捕获可能的编码错误
            dir_content = os.listdir(input_folder)
            print(f"成功列出目录内容，共 {len(dir_content)} 个文件或文件夹")

            for file in dir_content:
                file_path = os.path.join(input_folder, file)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(file)[1].lower()
                    if ext in image_extensions:
                        image_files.append(file_path)

            print(f"在输入文件夹中找到 {len(image_files)} 个图片文件")
        except Exception as e:
            print(f"列出目录内容时出错: {e}")
            print(traceback.format_exc())

        if not image_files:
            print(f"在 {input_folder} 中没有找到图片文件，退出处理")
            return []

        # 使用自然排序算法对图片文件进行排序（比如0.png, 1.png, 2.png，...，10.png）
        image_files.sort(key=_natural_sort_key)
        print(f"按自然顺序排序后的第一个文件: {os.path.basename(image_files[0])}")

        # 记录最小序号图片的路径
        first_image_path = image_files[0]
        print(f"序号最小的图片是: {os.path.basename(first_image_path)}")

        # 确定要生成的网格数量
        if num_grids is None:
            # 自动计算可以生成的完整网格数量
            calculated_num_grids = max(3, (len(image_files) + cells_per_grid - 1) // cells_per_grid)
            num_grids = calculated_num_grids
            print(f"自动计算的拼图数量: {num_grids}")

        print(f"将生成 {num_grids} 个{grid_name}")

        # 处理每一个网格
        for grid_index in range(int(num_grids)):  # 确保num_grids是整数
            try:
                print(f"开始处理第 {grid_index+1}/{num_grids} 个网格")

                # 为当前网格选择图片路径，第一个位置总是序号最小的图片
                grid_image_paths = []

                # 计算需要多少张图片来填充剩余的格子
                remaining_cells = cells_per_grid - 1

                # 如果有足够的图片，不需要重复
                if len(image_files) - 1 >= remaining_cells:
                    # 从第二张图片开始选择，避免重复使用第一张
                    start_idx = 1 + (grid_index * remaining_cells) % (len(image_files) - 1)
                    for i in range(remaining_cells):
                        img_idx = (start_idx + i) % len(image_files)
                        if img_idx == 0:  # 跳过序号最小的图片
                            img_idx = 1
                        grid_image_paths.append(image_files[img_idx])
                else:
                    # 需要重复使用图片
                    # 首先添加所有剩余的图片（除了第一张）
                    for i in range(1, len(image_files)):
                        grid_image_paths.append(image_files[i])

                    # 如果还不够，循环添加图片直到填满
                    remaining_needed = remaining_cells - len(grid_image_paths)
                    if remaining_needed > 0:
                        print(f"需要额外重复 {remaining_needed} 张图片")
                        repeat_idx = 0
                        while len(grid_image_paths) < remaining_cells:
                            idx_to_use = 1 + (repeat_idx % (len(image_files) - 1))
                            grid_image_paths.append(image_files[idx_to_use])
                            repeat_idx += 1

                # 确保只使用需要的图片数量
                grid_image_paths = grid_image_paths[:remaining_cells]

                print(f"处理第 {grid_index+1} 个网格，共 {cells_per_grid} 个位置，第1个位置为序号最小的图片，其余 {len(grid_image_paths)} 个位置为其他图片")

                # 进行图片排列和拼图
                combined_image = _arrange_images(grid_image_paths, rows, cols, first_image_path)

                # 构建输出文件的文件名
                output_filename = f"{grid_name}_{grid_index}.png"
                output_path = os.path.join(output_folder, output_filename)

                # 保存拼图结果
                print(f"保存拼图到: {output_path}")
                combined_image.save(output_path)
                output_paths.append(output_path)
                print(f"已成功保存拼图图片到 {output_path}")

                # 释放资源
                del combined_image
                gc.collect()

            except Exception as e:
                print(f"处理网格 {grid_index} 时出错: {e}")
                print(traceback.format_exc())

        if not output_paths:
            print("没有生成任何拼图图片，请检查输入文件夹中的图片是否有效。")
        else:
            print(f"总共生成了 {len(output_paths)} 张拼图图片。")

        return output_paths

    except Exception as e:
        print(f"发生错误: {e}")
        print(traceback.format_exc())
        return []

```。

接下来要做的，就是接住它，然后，把故事讲下去。

### 三、把 PDF 文档导出成图片

```
# 使用此指令前，请确保安装必要的Python库，例如使用以下命令安装：
# pip install PyMuPDF Pillow numpy

import fitz  # PyMuPDF
import io
import os
import numpy as np
from PIL import Image
import traceback

from typing import *
try:
    from xbot.app.logging import trace as print
except:
    from xbot import print

def extract_pages_as_images(pdf_file, output_folder, filter_blank_pages=True):
    """
    title: 从PDF导出整页为PNG图片
    description: 将PDF文件的每一页作为单独的PNG图片导出，可选是否过滤空白页面。
    inputs: 
        - pdf_file (file): PDF文件路径，eg: "example.pdf"
        - output_folder (folder): 图片保存的文件夹路径，eg: "output_images"
        - filter_blank_pages (bool): 是否过滤空白占比大的页面，eg: True
    outputs: 
        - result (str): 执行结果信息，包括导出的图片数量和可能的错误信息，eg: "成功导出5张页面图片"
    """

    # 检查输入文件和输出文件夹
    if not os.path.exists(pdf_file):
        raise FileNotFoundError(f"找不到PDF文件: {pdf_file}")

    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 图片质量检查函数
    def _is_blank_image(img, threshold=0.90):
        """检查图片是否为空白占比大的图片，调低阈值使检测不那么严格"""
        if img.mode == 'RGBA':
            # 转换为RGB模式
            img = img.convert('RGB')

        # 将图片转换为灰度图像
        if img.mode != 'L':
            img = img.convert('L')

        # 将图片转换为NumPy数组
        img_array = np.array(img)

        # 检查图片是否大部分为白色或透明
        white_ratio = np.mean(img_array > 240)
        if white_ratio > threshold:
            return True, white_ratio

        # 检查图片是否大部分为黑色
        black_ratio = np.mean(img_array < 15)
        if black_ratio > threshold:
            return True, black_ratio

        return False, max(white_ratio, black_ratio)

    try:
        # 打开PDF文件
        pdf_document = fitz.open(pdf_file)

        # 检查PDF权限
        if pdf_document.is_encrypted:
            try:
                # 尝试不带密码打开
                if not pdf_document.authenticate(""):
                    return "PDF文件被加密，无法导出页面"
            except:
                return "PDF文件被加密，无法导出页面"

        image_count = 0
        blank_count = 0
        issues = []
        successful_extractions = []

        # 遍历PDF的每一页并导出为图片
        for page_num in range(len(pdf_document)):
            try:
                # 获取当前页
                page = pdf_document[page_num]

                # 使用高分辨率渲染页面
                pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))

                # 将pixmap转换为PIL图像以检查是否为空白
                img_bytes = pix.tobytes("png")
                img = Image.open(io.BytesIO(img_bytes))

                # 检查页面是否为空白
                is_blank, blank_ratio = _is_blank_image(img)

                # 如果是空白页面且用户选择过滤，则跳过
                if filter_blank_pages and is_blank:
                    blank_count += 1
                    continue

                # 保存为PNG图片
                image_filename = f"{image_count}.png"
                image_path = os.path.join(output_folder, image_filename)
                pix.save(image_path)

                # 添加成功导出记录
                blank_info = f" (空白占比: {blank_ratio:.2%})" if blank_ratio > 0.5 else ""
                successful_extractions.append(f"第{page_num+1}页 -> {image_count}.png{blank_info}")
                image_count += 1

            except Exception as e:
                issues.append(f"处理第{page_num+1}页时出错: {str(e)}")

        # 关闭PDF文件
        pdf_document.close()

        # 准备返回结果
        if image_count > 0:
            filter_state = "已过滤" if filter_blank_pages else "检测到但未过滤"
            result = f"成功导出{image_count}张页面图片"
            if blank_count > 0:
                result += f"，{filter_state}{blank_count}张空白占比大的页面"
            if issues:
                result += f"\n\n可能的问题({len(issues)}个):\n" + "\n".join(issues)
            result += f"\n\n成功导出的页面列表:\n" + "\n".join(successful_extractions)
        else:
            if blank_count > 0:
                result = f"未导出任何页面，但检测到{blank_count}张空白占比大的页面，可能原因:\n"
                result += "1\. 所有页面空白占比都超过阈值\n"
                result += "2\. 如需查看这些空白页面，请将'过滤空白页面'选项设为False"
            else:
                result = "无法从PDF导出任何页面图片，可能的原因：\n"
                result += "1\. PDF可能是空文件\n"
                result += "2\. PDF可能有特殊保护措施"

            if issues:
                result += f"\n\n详细问题({len(issues)}个):\n" + "\n".join(issues)

        return result

    except Exception as e:
        error_trace = traceback.format_exc()
        return f"处理PDF时发生错误:\n{str(e)}\n\n详细错误信息:\n{error_trace}"

```

### 四、批量从指定文件夹里随机抓取图片

```
# pip install Pillow

import os
import random
import shutil
from PIL import Image, ImageStat
import numpy as np

from typing import *
try:
    from xbot.app.logging import trace as print
except:
    from xbot import print

def random_select_images(source_folder, target_folder):
    """
    title: 随机抽取优质图片
    description: 从指定文件夹中随机抽取两张不重复的图片，并以1.png和2.png的名称保存到目标文件夹。优先选择内容不空白、美观的四宫格或九宫格图片。
    inputs: 
        - source_folder (folder): 源图片文件夹路径，eg: "C:/Pictures"
        - target_folder (folder): 目标保存文件夹路径，eg: "C:/Selected_Pictures"
    outputs: 
        - selected_images (list): 已选择的图片路径列表，eg: ["C:/Selected_Pictures/1.png", "C:/Selected_Pictures/2.png"]
    """

    # 检查文件夹是否存在
    if not os.path.exists(source_folder):
        raise ValueError(f"源文件夹 '{source_folder}' 不存在")

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 获取所有图片文件
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    image_files = [f for f in os.listdir(source_folder) 
                  if os.path.isfile(os.path.join(source_folder, f)) and 
                  os.path.splitext(f)[1].lower() in valid_extensions]

    if len(image_files) < 2:
        raise ValueError(f"源文件夹中没有足够的图片文件（至少需要2张）")

    # 分析图片质量
    def _analyze_image_quality(image_path):
        """分析图片质量，返回质量分数"""
        try:
            with Image.open(image_path) as img:
                # 检查是否为四宫格或九宫格图片
                width, height = img.size

                # 转为灰度图计算空白区域
                gray_img = img.convert('L')
                stat = ImageStat.Stat(gray_img)

                # 计算图像的标准差，标准差小说明图像可能比较空白
                std_dev = stat.stddev[0]

                # 检测可能的网格线，评估是否为宫格图片
                is_grid = False

                # 简单估计是否为网格图像（通过检查图像尺寸是否接近等分）
                if abs(width - height) < width * 0.1:  # 近似正方形
                    # 检查是否可被2或3整除（四宫格或九宫格）
                    if width % 2 == 0 and height % 2 == 0:
                        is_grid = True
                    elif width % 3 == 0 and height % 3 == 0:
                        is_grid = True

                # 综合评分：优先选择非空白的宫格图片
                score = std_dev * (1.5 if is_grid else 1.0)

                return score
        except Exception:
            return 0  # 如果图片无法打开或处理，评分为0

    # 计算所有图片的质量分数
    image_scores = {}
    for img_file in image_files:
        img_path = os.path.join(source_folder, img_file)
        score = _analyze_image_quality(img_path)
        image_scores[img_file] = score

    # 按分数排序
    sorted_images = sorted(image_scores.items(), key=lambda x: x[1], reverse=True)

    # 选择得分最高的两张图片，如果所有图片质量都不好（得分为0），则随机选择
    selected_files = []

    # 检查是否所有图片得分都为0
    if all(score == 0 for _, score in sorted_images):
        selected_files = random.sample(image_files, 2)
    else:
        # 至少有一张图片质量不错，优先选择高分图片
        selected_files = [file for file, _ in sorted_images[:2]]

        # 如果高分图片不足两张，从剩余图片中随机选择
        if len(selected_files) < 2:
            remaining = [f for f in image_files if f not in selected_files]
            selected_files.extend(random.sample(remaining, 2 - len(selected_files)))

    # 复制选中的图片到目标文件夹，并重命名为1.png和2.png
    selected_paths = []
    for i, img_file in enumerate(selected_files, 1):
        source_path = os.path.join(source_folder, img_file)
        target_path = os.path.join(target_folder, f"{i}.png")

        # 如果目标文件已存在，先删除
        if os.path.exists(target_path):
            os.remove(target_path)

        # 读取原图并保存为PNG格式
        try:
            with Image.open(source_path) as img:
                img.save(target_path, "PNG")
        except Exception:
            # 如果无法转换，直接复制
            shutil.copy2(source_path, target_path)

        selected_paths.append(target_path)

    return selected_paths

```

在日常处理PDF文件时，我们常常需要从完整的文件路径中快速获取文件名。这个看似简单的操作，其实有不少实用技巧。今天就来聊聊如何高效提取PDF路径里的文件名，让你告别手动复制粘贴的繁琐。

```
import os

from typing import *
try:
    from xbot.app.logging import trace as print
except:
    from xbot import print

def extract_filename(file_path):
    """
    title: 提取文件路径中的文件名
    description: 从完整文件路径中提取文件名（不含扩展名）
    inputs: 
        - file_path (str): 完整的文件路径，eg: "D:\\Desktop\\文档\\报告.pdf"
    outputs: 
        - filename (str): 提取的文件名（不含扩展名），eg: "报告"
    """

    # 检查输入是否为字符串
    if not isinstance(file_path, str):
        raise TypeError("文件路径必须是字符串类型")

    # 检查路径是否为空
    if not file_path:
        raise ValueError("文件路径不能为空")

    # 从路径中提取文件名（带扩展名）
    full_filename = os.path.basename(file_path)

    # 分离文件名和扩展名
    filename, _ = os.path.splitext(full_filename)

    return filename

```