# ('利用AI批量爬取并且清洗1000名AI方向博主微信，并且自动化添加好友', (2, 37))

克拉克有一句广为流传的判断：当科技发展到足够成熟，它看起来就等同于魔法。我以前觉得这是作家惯用的修辞，直到最近亲自做了一件颇为“土”的事情——借助AI，从短视频平台抓取1000名AI方向的内容创作者，再到他们的主页里整理出微信ID，最后自动发送好友申请。整个过程竟然像变了一场小魔术。

为什么会有这个需求？想拓展AI、内容创作、创业等领域的人脉，关注那些在短视频平台活跃的博主是最直接的路径。很多厉害的人都会在主页留下自己的联络方式。可是手动去逐个打开主页、复制ID、发出申请，几十个人还能接受，换成上千个就是纯粹的体力活。于是我想，能不能让AI来写Python脚本，把采集、清洗、自动联系这些环节全部串起来？试下来，确实可行。

**第一步：批量采集目标用户**

我选了一款名为Octopus的采集工具。在短视频App的搜索框里，轮流输入“AI”“聊聊AI”“说说AI”“AI课程”“AI绘图”“用AI赚钱”等词，将搜出的用户基础信息批量抓取下来，先统一整理到一张Excel表里。

**第二步：借助AI处理数据**

原始数据无法直接使用。例如点赞量和收藏量大多显示为“1.2万”“3.5万”，无法直接按大小排序。我先给GPT设定好角色，并把Excel表结构喂给它。![](img/65c72c999af8a1f3bc4eb0c76432a46b.png)![](img/5c19c7285b0fe9bdfca77290956e24fc.png)![](img/1b35429e0ba2aaa6f2508cc4f45b47e2.png)![](img/14e76d3769dab9c0523ea030999fad48.png)接着请它编写一个转换脚本，将“万”还原成具体数字。过程中我不断补充要求。![](img/a88cd3b1362c355ba4333008f7b20f99.png)![](img/dadd9a9a509d665eb57d6fa25648c7b1.png)第一次执行时出了问题：数字虽然被提取出来，却漏掉了乘以10000这一步，导致“万”被忽略。![](img/33b07825282b6d03f5494588b689877d.png)我把报错信息回传给它，让它修正。![](img/bd282b0096e340596b63c9b5de75d8f5.png)修改后的代码顺利通过，```
import openpyxl
import re

def convert_to_number(value_str):
    units = {'万': 10000, '亿': 100000000}
    try:
        if value_str[-1] in units:
            return float(value_str[:-1]) * units[value_str[-1]]
        else:
            return float(value_str)
    except ValueError as e:
        print(f"无法转换的字符串：'{value_str}'，跳过此行。")
        return None

def remove_text(value_str):
    # 使用正则表达式保留数字、小数点和单位
    value_str = re.sub(r"[^0-9.万亿]", "", value_str)
    return value_str

def main():
    # 读取 Excel 文件
    excel_file = "AI博主.xlsx"
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    # 遍历 Excel 文件中的数据，假设获赞数在第五列（E列），粉丝数在第六列（F列）
    for row in range(2, sheet.max_row + 1):
        # 读取获赞数和粉丝数
        like_str = sheet.cell(row=row, column=5).value
        follower_str = sheet.cell(row=row, column=6).value

        # 删除文本
        like_str = remove_text(like_str)
        follower_str = remove_text(follower_str)

        # 转换为纯数字
        like_num = convert_to_number(like_str)
        follower_num = convert_to_number(follower_str)

        # 如果转换成功，则更新数据
        if like_num is not None and follower_num is not None:
            sheet.cell(row=row, column=5).value = like_num
            sheet.cell(row=row, column=6).value = follower_num

    # 保存修改后的 Excel 文件
    workbook.save("AI博主_更新后.xlsx")
    print("已成功更新并保存为 'AI博主_更新后.xlsx' 文件！")

if __name__ == "__main__":
    main()
```数据也终于能按照点赞量和收藏量做排序了。![](img/c535997e5e80815f05e46931e343dd96.png)

随后需要清理无效和重复的数据。如果主页介绍里是“未填写说明”“感谢关注”这类默认文案，或者那一栏根本没有内容，通常不是目标账号，可以删除。![](img/a67d7ddaedc8042e6aa98b415a73d97b.png)另外，采集阶段容易出现重复抓取，还需要按照“账号唯一标识”一列去重。![](img/a48442e0e520baf0ae75f1a86913374b.png)这两步同样由AI生成的代码执行，跑完后表格清爽了不少。```
import openpyxl

def main():
    # 读取 Excel 文件
    excel_file = "AI博主_更新后.xlsx"
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    # 去重抖音号
    unique_douyin_ids = set()
    row = 2
    while row <= sheet.max_row:
        douyin_id = sheet.cell(row=row, column=4).value

        # 如果抖音号已经存在，删除整行记录
        if douyin_id in unique_douyin_ids:
            sheet.delete_rows(row)
        else:
            unique_douyin_ids.add(douyin_id)
            row += 1

    # 删除个人简介为“此用户没有填写简介”的记录
    row = 2
    while row <= sheet.max_row:
        bio = sheet.cell(row=row, column=7).value

        # 如果个人简介等于“此用户没有填写简介”，删除整行记录
        if bio == "此用户没有填写简介":
            sheet.delete_rows(row)
        else:
            row += 1

    # 保存清洗后的 Excel 文件
    workbook.save("AI博主_重复项清洗.xlsx")
    print("已成功清洗并保存为 'AI博主_重复项清洗.xlsx' 文件！")

if __name__ == "__main__":
    main()

```![](img/afab173496e1bbe6a2540393df68d1b8.png)

接下来是最有价值的环节：找出潜在的微信ID。很多人喜欢把平台账号直接设置成自己的微信ID。![](img/3da0032772cfdd864d50850f33294647.png)我针对【账号标识】一列，用正则表达式把疑似微信ID的内容筛出来，写入表格第8列。规则很简单：微信ID通常是6到20位，由字母、数字、_或-组成，并且首字符必须是一个字母；如果平台账号恰好是手机号（以1开头、共11位）或QQ号（5到10位），也可以视为有效候选。```
import openpyxl
import re

def is_wechat_id(douyin_id):
    # 检查是否符合微信号规则
    wechat_rule = re.compile(r"^[a-zA-Z][a-zA-Z0-9_-]{5,19}$")
    phone_rule = re.compile(r"^1\d{10}$")
    qq_rule = re.compile(r"^\d{5,10}$")

    if wechat_rule.match(douyin_id) or phone_rule.match(douyin_id) or qq_rule.match(douyin_id):
        return True
    return False

def main():
    # 读取 Excel 文件
    excel_file = "AI博主_重复项清洗.xlsx"
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    # 检查抖音号字段，并将可能的微信号保存到第8列
    for row in range(2, sheet.max_row + 1):
        douyin_id = sheet.cell(row=row, column=4).value

        # 使用正则表达式检查抖音号是否可能是微信号
        if is_wechat_id(douyin_id):
            sheet.cell(row=row, column=8).value = douyin_id

    # 保存更改后的 Excel 文件
    workbook.save("AI博主_重复项清洗.xlsx")
    print("已成功将可能的微信号保存到 'AI博主_重复项清洗.xlsx' 文件中的【微信号】字段！")

if __name__ == "__main__":
    main()
```![](img/0c03bfb6e399039606eff5d6408219fb.png)

另外，主页介绍里也可能藏着微信ID。匹配逻辑主要包括：标准的微信ID格式、以1开头共11位的手机号码、冒号之后跟着的英文和数字串，以及“联系”“合作”等提示词后出现的英文数字组合。提取结果统一放到第9列“微信ID1”字段。```
import openpyxl
import re

def find_wechat_id(bio):
    patterns = [
        r"[a-zA-Z\d][ a-zA-Z\d_-]{5,19}",
        r"1\d{10}",
        r"[:：][\s]?[a-zA-Z\d][a-zA-Z\d_-]{5,19}",
        r"[\u52a0/\u5fae].{0,10}[a-zA-Z\d][a-zA-Z\d_-]{5,19}",
        r"(\u5fae\u4fe1/\u8054\u7cfb/\u5408\u4f5c).{0,10}[a-zA-Z\d][a-zA-Z\d_-]{5,19}"
    ]

    for pattern in patterns:
        match = re.search(pattern, bio)
        if match:
            return match.group()
    return None

def main():
    # 读取 Excel 文件
    excel_file = "AI博主_重复项清洗.xlsx"
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    # 从个人简介字段解析可能的微信号，并保存到第9列
    for row in range(2, sheet.max_row + 1):
        bio = sheet.cell(row=row, column=7).value

        # 使用正则表达式检查个人简介中是否可能包含微信号
        wechat_id = find_wechat_id(bio)
        if wechat_id:
            sheet.cell(row=row, column=9).value = wechat_id

    # 保存更改后的 Excel 文件
    workbook.save("AI博主_重复项清洗.xlsx")
    print("已成功将个人简介中可能的微信号保存到 'AI博主_重复项清洗.xlsx' 文件中的【微信号1】字段！")

if __name__ == "__main__":
    main()
```![](img/77a78d19a77359e087958f45acc2417c.png)清洗结束，我们就拥有一份值得联系的高质量名单了。![](img/9bbcb68cca8ebda232ff431da27d864e.png)

**第三步：用RPA自动发出好友申请**

名单准备就绪后，自动发送申请的工具也不难找。市面上有大量同类软件，我用的这款口碑不错，而且一直有专人维护（没有恰饭，它确实仍在更新，我看到的最新版本日期是7月3日）。![](img/a978cca41e22ba634f2b6710a24ac39d.png)它基于RPA原理，本质上就是模拟真人操作，只是由程序代为执行，和亲手操作完全没有区别，我觉得这是最稳妥的路径。

相关资源如下：
- 工具主页：http://www.jisubianxian.com/
- 需配合专用版本的微信客户端：https://soft.3dmgame.com/down/247977.html
- 关闭微信自动更新的补丁：https://cup.lanzoui.com/pcwxnoupdate

使用起来也非常简单：
1. 导入名单：Excel里需要包含四列，即微信ID、昵称、分组标签、招呼用语。
2. 调整规则：发送频率不要定得过高。我实测过，一个账号每天发出20到30个申请是完全可以的。
3. 启动程序：运行后它会自动操作，剩下就是等待对方通过。

**关于我**

我很欣赏一句话：人应该主动为世界留下一点印记，而不是被世界随意书写。

我是伟业，一名专注AI技术落地的创业者，创办了BitStorm公司；做过不少应用，校园服务、心理测评、校务管理、发票处理等都有涉及；发起了AI价值创造者社群（AI Value Makers）；我的短视频账号始终围绕AI展开，开播20天时播放量冲到200万，获得3万个赞，而且积累下1800位高粘性粉丝；现在正在开发一款AI口语练习产品。在校时，我花了两年自己摸索编程，带着一支七人团队，从零开发并推广了校园一站式服务应用，总用户超过一万人，日活跃用户2000多名。

从小我就怀揣三个梦想：一是创办一份属于自己的事业，哪怕公司只有十个人，也要不辜负自己的名字；二是做知识的传递者，把经验和心得写成文字、讲给有需要的人；三是做一个梦想家，让脑海里的构想慢慢变成可用的产品。非常幸运的是，今年，这几件事居然开始交织成了同一件事。最后，生财平台以及亦仁先生，是我由衷想表示感谢的。