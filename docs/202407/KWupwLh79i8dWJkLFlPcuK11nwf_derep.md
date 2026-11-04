# 用影刀RPA玩转剪映图文AI：把批量文案变成成片的自动化工作流



一、这套自动化工具是什么

工具名称：剪映图文AI自动创作影刀RPA机器人

主要能力：

1. 批量抓取本地 TXT 文案并一键生成图文视频
2. 自动匹配本地封面素材使用
3. 全程无人值守完成导出成片

输出成果：

二、开工前准备

所需软件：影刀RPA软件
官网地址：www.yingdao.com

三、运行逻辑概览

1. 指定素材目录
（1）文案以 txt 形式存放，每个文件一份脚本
（2）封面图与对应 txt 同名放置在同一目录

2. 启动影刀RPA环境

3. 调用剪映图文成片功能

4. 载入本地素材包

5. 将导入的封面图拖拽至与音频时长一致

6. 设定导出文件名与保存路径

7. 执行批量输出

四、流程实现代码

主流程

![](img/22e113477d4648d827dfc3a9cd4fd283.png)

![](img/e0ce714712fe4adecbe22ffba9bd4b8d.png)

![](img/7fd4dd210b7653b9e576a0ff9bec9e88.png)

A.读取文件夹下的txt.flow

![](img/11ba579ae609b18c683aa634e6203d91.png)

![](img/81225862c68cd435203c48832bb87838.png)

B1.开始剪映创作流程.flow

![](img/ca16747cb1a5e59f896c57163cc583a1.png)

![](img/ee9d4dfa8bd4b57564abe0f52d7fc42c.png)

![](img/4d7a08ace2708bbc78d9fccd5e0239c0.png)

![](img/7428455958d3fbb4faa516cc76b4966e.png)

![](img/9dbf368304b0af586fb2329f2b4cc982.png)

![](img/8a04b50f881bcbc4d061f2819f3c7d9f.png)

![](img/28f308617dc1ea68b3ab690bcb92ac0a.png)

![](img/07b723600d2a1d1fe1d4217acb635e25.png)

![](img/0fba0652f86d24cdee378054e5ff5a92.png)

![](img/11edfae4a3d92bfd7615a25ecde8d8e5.png)

![](img/316aae446def1edc72252613b7ec7c4d.png)

![](img/fb5e7e304c76b9b95e428acccceb3631.png)

![](img/dee5e0bd9dc404642bd1b96cd651a548.png)

G1.关闭图文成片窗口.flow

![](img/2d75684695485b5497a76ef5f60adeff.png)

G2.关闭剪映.flow

![](img/488ed9afe04e0ac6fe5d4fe9f461c0e2.png)

G3.启动剪映.flow

![](img/2d1f59579d1ec5dd36a0836edb7f1c85.png)

G4.当前进度.flow

![](img/3896c2675a2f0e9ec3c63f6709746229.png)

![](img/4daa39c7ec4787aedf140055ff5a44f7.png)

![](img/cb5dbd016f8083aad6ef6fde9035724b.png)

![](img/136b545d3e915e76a09b5b7d2538669d.png)

![](img/ff942cf234dc9c762c3b561cd2047c5b.png)

G6.时间轴拉长图片.flow

![](img/0a56d345d461fa74e463a1e1c0e147e7.png)

![](img/364c20ec23c7db065bb36a0e1fa26b02.png)

G7.删除草稿.flow

![](img/df9ae25a7388197620dadf00fac88ad5.png)