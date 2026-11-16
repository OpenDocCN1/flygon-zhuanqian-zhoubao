# Coze 零成本搭一个迷你版吐槽大会

最近在精华帖里刷到一个用 AI 工具从零做起的吐槽网站：

看完有点上头，就顺手用 Coze 也复刻了一遍。如今 Coze 除了能做智能体，还能直接做应用，功能很全了。

我做的这个简化版吐槽大会的最终效果如下：

![](img/zhuanqian_9542e7f94de35d76eb2c1b82a3a69a34.png)

体验可以直接点这里：https://www.coze.cn/s/ifPYNLNw/

搭建过程其实很直观，分成下面几步：

1. 打开 Coze 工作台：https://www.coze.cn/space/

1. 点右上角的创建

1. 新建一个应用

![](img/zhuanqian_baf1c1ee3bb1bc647607bee7fff4837f.png)

1. 选个应用模板。我这次用的是空白模板，模板可以根据自己的喜好换

![](img/zhuanqian_aae21fb0f1dcc9850a8ee304aad154a8.png)

1. 填写应用的基础信息

![](img/zhuanqian_f4fc0af38837775a806217e2d7ba357c.png)

1. 新建工作流

![](img/zhuanqian_317ef20e17215dbcff15b0dbfb7d827d.png)

1. 工作流里我只放了一个大模型节点，核心是提示词

![](img/zhuanqian_35405977838b99f333ffdd50eaec69f9.png)

配置开始节点

![](img/zhuanqian_bd4d4ca80ee7fc2267ffeb515ecf3cba.png)

配置大模型节点

![](img/zhuanqian_54c4c82d6d1d2395be5710da4c4d762f.png)

```
你是一个致力于创作反心灵鸡汤的灵魂段子手​
#根据{{input}}创作对应的反心灵鸡汤​
#采用具有强烈讽刺意味的表达​
#风格应当毒舌、辛辣、讽刺​
#内容应当深刻、直击灵魂​
#内容应当精简，不超过50字​
#当{{input}}为空时，吐槽用户这个行为​
#当{{input}}涉及政治、党派、种族歧视等敏感内容时，拒绝创作，并吐槽用户的钓鱼行为​
#请尽情挥洒你的创造力
```

配置结束节点

![](img/zhuanqian_60f091b94295dd39c9837fd2a923e780.png)

1. 调整用户界面

![](img/zhuanqian_4cb2e9074cba5c1bc05305eaf47b1bca.png)

可以先选一个界面模板，也可以直接跳过

![](img/zhuanqian_e034ec8d4a4c5da4cb7a30589e0ad249.png)

1. 添加组件，这次只用了输入框、输出区和按钮三个

![](img/zhuanqian_e9721889c5f18d6c5abbba0c55021621.png)

1. 给组件设置属性

配置输入组件

![](img/zhuanqian_3beed29b30561f124696fa294178d7c5.png)

配置输出组件

![](img/zhuanqian_87937869935ad40ceff19cd9b8513826.png)

配置按钮的属性和交互事件

![](img/zhuanqian_48efe4039b651094a8bf90c1cf31d8d9.png)

![](img/zhuanqian_3d96ed21c8adcf97194e900378459c30.png)

1. 发布上线

发布类型可以根据使用场景自行选择

![](img/zhuanqian_cefe95c5f0dfc86b41dc2cbdef4e714b.png)

![](img/zhuanqian_7604884e6ba68b16fddf99254bd56c18.png)

![](img/zhuanqian_377611dd718cec004e14ff53c8809a92.png)

![](img/zhuanqian_f89c2cdef18eff5d19a1262290ed36cb.png)