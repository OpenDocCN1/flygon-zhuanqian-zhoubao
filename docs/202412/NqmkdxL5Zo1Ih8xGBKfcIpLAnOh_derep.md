# 五分钟，用 Cursor 帮我把头像从 5000 人大图里揪了出来
作者：龙哥



https://t.zsxq.com/R3nuz

![](img/4cc5b80b4b1e952ed54703b380463a76.png)

鱼丸这边搞了个寻头像的互动，5000 个人头像拼成一幅超大图，找自己那个小方块。愣是看了我快 15 分钟，眼睛都快瞎了，还是没翻到圈友的头像😂没错，不是没找到我自己的，我的早被别人揪出来了，是我找不到她的。

@Rice

![](img/b9ae879ed970ead40888aa386e16aef3.png)

干嘛非得靠人肉搜？这活直接丢给程序啊，马上就干！

对了，万一你还没摸过 Cursor 怎么办？去 @阿紫 的帖子补个课 https://scys.com/articleDetail/xq_topic/1525488422112812

### 1 先把需求想清楚

本质就是在一张巨图里定位一个小头像。

大图找小图天然是图像匹配的活，Python 生态做这个最顺手。于是我直接让 Cursor 用 Python 写个匹配脚本。

我跟它描述的需求是：大图尺寸大概 14173 x 3701，里面密密麻麻排满头像，每个约 64x64。我会丢一张不同分辨率的个人头像进去，让它在大图里搜出来，找到就把对应区域裁剪返回。行不行？

把大图拉下来确认尺寸后，就开始和 Cursor 对话。

![](img/2295d5e8c8271cd2c9f800e10b048adc.png)

![](img/258e6b2e811c1b5cad62281fecaa600b.png)

### 2 让它能命令行跑

一版代码很快就出来了，但交互太麻烦。于是我让 Cursor 改成命令行调用，参数直接传进去就行。

![](img/b4258ab3c32865e29b51d237ff541740.png)

![](img/48a3760211182b4882df123a59ffa8a2.png)

### 3 先跑起来，再精细调

跑通后发现确实能定位到，但返回的裁剪图小得像像素点。

![](img/373974c935d9c596259942386fac9bfb.png)

![](img/736033defe03de6567eacb102e8c890f.png)

另外一次搜索会蹦出 8 个候选，还得继续优化。

![](img/1a3362072d7515047baf98d24c348b8a.png)

![](img/1eb6a06896f4e541e065b81f85db312e.png)

### 4 把结果图放大看清

随后我让它把定位框和裁剪结果一起放大输出，阅读体验才算合格。

![](img/42de4201ee939689aa882482fb3189bc.png)

![](img/39c2ca067ac9b6b93f2fdaa275c0a77b.png)

### 5 成果展示

最终导出的效果如下

![](img/66f46e9dc6f13de46d80ec0346cddaca.png)

![](img/d3f54a95acf7c3373e80df176cebac77.png)

![](img/5210bb97088400468dc1ecbff6487191.png)

第二个一看就知道是 @佳文 吧hhh（佳文，快来学😉）

![](img/993ec76c7910b0ea097ad23c914e69e5.png)

![](img/4654674e3a7730f43830eb947664b6d1.png)

![](img/66ff56c94f2f2cfb58cbe92c243b6c38.png)

### 7 中间的小插曲

找 @Time 的头像时程序直接没反应。

![](img/3b0b803f7ad7d9eb7826cf9571c15d5d.png)

后来才发现是相似度阈值设得太严了，默认 0.8 挡掉了。改成 0.7 就行

也可以这样跑：python .\find_me.py .\images\scys.jpg --threshold 0.7

![](img/fd744d2b1482df3617788bc657cfc22c.png)

再搜一次就稳稳找到了！

![](img/84f81acd059da38de66c8c1638c3a253.png)

![](img/e9420f374f70d78803ded7a06524e51e.png)

![](img/039da561d5ed16ee040168db8b98b980.png)

### 6 代码放一下

最后把脚本贴出来。

依赖：pip install opencv-python numpy

用法：python .\find_me.py 大图路径 头像路径

```
import cv2
import numpy as np
import argparse

def non_max_suppression(matches, overlap_thresh=0.3):
    """
    对重叠的匹配结果进行非极大值抑制

    参数:
        matches: 匹配结果列表，每个元素为 (x, y, w, h, conf)
        overlap_thresh: 重叠阈值，超过此阈值的重叠区域将被抑制
    """
    if not matches:
        return []

    # 将匹配结果转换为numpy数组
    boxes = np.array([[x, y, x + w, y + h] for x, y, w, h, _ in matches])
    scores = np.array([conf for _, _, _, _, conf in matches])

    # 计算面积
    area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])

    # 按照匹配度排序
    idxs = np.argsort(scores)[::-1]

    keep = []
    while len(idxs) > 0:
        # 保留当前最高分数的框
        current = idxs[0]
        keep.append(current)

        if len(idxs) == 1:
            break

        # 计算其他框与当前框的IoU
        xx1 = np.maximum(boxes[current, 0], boxes[idxs[1:], 0])
        yy1 = np.maximum(boxes[current, 1], boxes[idxs[1:], 1])
        xx2 = np.minimum(boxes[current, 2], boxes[idxs[1:], 2])
        yy2 = np.minimum(boxes[current, 3], boxes[idxs[1:], 3])

        w = np.maximum(0, xx2 - xx1)
        h = np.maximum(0, yy2 - yy1)

        overlap = (w * h) / area[idxs[1:]]

        # 删除重叠度高的框
        idxs = np.delete(idxs, np.concatenate(([0], np.where(overlap > overlap_thresh)[0] + 1)))

    return [matches[i] for i in keep]

def find_avatar(large_image_path, template_path, threshold=0.8):
    """
    在大图中查找目标头像

    参数:
        large_image_path: 包含多个头像的大图路径
        template_path: 要查找的单个头像图片路径
        threshold: 匹配阈值，越高要求越严格

    返回:
        找到的头像图片列表，每个元素为(x, y, w, h)和匹配度
    """
    # 读取图片
    large_image = cv2.imread(large_image_path)
    template = cv2.imread(template_path)

    # 将模板图片调整为64x64
    template = cv2.resize(template, (64, 64))

    # 获取模板尺寸
    h, w = template.shape[:2]

    # 模板匹配
    result = cv2.matchTemplate(large_image, template, cv2.TM_CCOEFF_NORMED)

    # 找到匹配位置
    locations = np.where(result >= threshold)
    matches = []

    # 获取所有匹配位置
    for pt in zip(*locations[::-1]):
        matches.append((pt[0], pt[1], w, h, result[pt[1], pt[0]]))

    # 应用非极大值抑制
    matches = non_max_suppression(matches)

    return matches

def draw_matches(image_path, matches):
    """
    在原图上标记匹配位置并保存结果，并保存扩大范围的截图
    """
    image = cv2.imread(image_path)
    for x, y, w, h, conf in matches:
        # 画红色矩形框，扩大框的范围，增加线条粗细
        padding = 20  # 框的扩展范围
        thickness = 5  # 线条粗细

        # 计算扩展后的框的坐标
        box_x1 = max(0, x - padding)
        box_y1 = max(0, y - padding)
        box_x2 = min(image.shape[1], x + w + padding)
        box_y2 = min(image.shape[0], y + h + padding)

        # 在原图上画扩展后的红色框
        cv2.rectangle(image, (box_x1, box_y1), (box_x2, box_y2), (0, 0, 255), thickness)

        # 计算扩展区域的坐标（3000x3000）
        extend_size = 3000
        half_extend = extend_size // 2
        center_x = x + w // 2
        center_y = y + h // 2

        # 计算扩展区域的边界，确保不超出原图范围
        x1 = max(0, center_x - half_extend)
        y1 = max(0, center_y - half_extend)
        x2 = min(image.shape[1], center_x + half_extend)
        y2 = min(image.shape[0], center_y + half_extend)

        # 截取扩展区域
        extended_avatar = image[y1:y2, x1:x2]

        # 在扩展区域图片上也画扩展后的红色框
        relative_x = x - x1
        relative_y = y - y1
        box_relative_x1 = max(0, relative_x - padding)
        box_relative_y1 = max(0, relative_y - padding)
        box_relative_x2 = min(extended_avatar.shape[1], relative_x + w + padding)
        box_relative_y2 = min(extended_avatar.shape[0], relative_y + h + padding)

        cv2.rectangle(extended_avatar, 
                     (box_relative_x1, box_relative_y1), 
                     (box_relative_x2, box_relative_y2), 
                     (0, 0, 255), thickness)

        # 保存扩展区域截图
        cv2.imwrite(f'matched_avatar_{x}_{y}.png', extended_avatar)

    # 保存标记后的大图
    cv2.imwrite('result.png', image)

# 使用示例
def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='在大图中查找指定头像')
    parser.add_argument('large_image', help='包含多个头像的大图路径')
    parser.add_argument('template', help='要查找的头像图片路径')
    parser.add_argument('--threshold', type=float, default=0.7,
                      help='匹配阈值 (0-1 之间，默认: 0.8)')

    # 解析命令行参数
    args = parser.parse_args()

    # 查找匹配
    matches = find_avatar(args.large_image, args.template, args.threshold)

    if matches:
        print(f"找到 {len(matches)} 个匹配结果")
        # 绘制结果
        draw_matches(args.large_image, matches)
        print("结果已保存")
    else:
        print("未找到匹配结果")

if __name__ == "__main__":
    main()
```