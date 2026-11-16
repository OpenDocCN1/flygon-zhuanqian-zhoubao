# 用7万篇历史内容，还原153个头部作者的增长轨迹
作者：龙哥

最近龙哥在文章里提到一个值得留意的方向：聚焦细分赛道做垂直资讯与工具盘点，等影响力起来后接商务合作完成变现。

这个模式能否复制？与其主观判断，不如直接拆解已经跑通的账号。

于是启动了一次面向🛰️生态的盘点项目：把当前活跃的AI垂类创作者的历史稿件全部抓取下来，从内容主题、互动表现、爆点时间点到账号演进路径做一次量化复盘，尝试把自媒体的成功路径拆解出来。

首轮工作已经收敛。

## 一、数据抓取范围

这次以🛰️号为切口，完成了三件事：

1. 筛选出153个在榜单上排名靠前的AI垂类账号；
2. 对这些账号的历史发布物进行全量抓取，累计超过7万篇；
3. 用模型辅助做摘要、软文标记与主题归类。

单篇记录尽量保留：标题、链接、发布时间、阅读表现、点赞表现、账号标识、是否原创等字段。

账号层则额外统计：稿件总量、历史阅读走势、爆款出现时段、更新频率、月度阅读与点赞变化、从冷启动到拐点的关键节点。

为让观察更直观，借助 Claude 做了可视化图，并为每个号生成独立的画像报告。

后续会逐步开放这批内容数据、模型提示词与处理流程。下一步计划把采集面扩展到📕、抖音、X 等平台，持续同步头部创作者的产出。

## 二、案例拆解：卡兹克的破圈节奏

先看一个典型样本——卡兹克。

从采集结果看，流量跃升并非偶然，而是长期内容沉淀后的集中释放。

按阅读量倒排可见：

- 2024 年 1 月 10 日，关于 Magnific AI 的测评首次触达十万 +；
- 2024 年 2 月，Sora 相关内容再次触达十万 +；
- 此后半年多里，账号连续产出爆款，累计 11 篇进入十万 + 区间。

换句话说，Sora 并非第一次被关注，而是前期积累后的破圈催化剂。

![](img/5f842cdd71920f5872b4e694cf9e7989.png)

### 爆发前已有信号

在首篇十万 + 之前，2023 年 12 月 6 日发布的一篇 Pika 评测已拿到约 7.8 万阅读。

标题为：《全网首发】PIKA1.0 上手评测》
原文：https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647660666&idx=1&sn=0e9e2a11d5c06cd512479d35ca84bf3f

在此之前，历史峰值约为 4 万。从曲线看，Pika 是第一次明显抬升，Magnific AI 与 Sora 把势能推向破圈。

![](img/43f37a29cfef98813fc7f0420c2c161d.png)

阅读随时间的整体走势：

![](img/df7b3a61456167c99cd2c5663b9fb92b.png)

篇数与阅读的分布关系：

![](img/46644643223447b5370e4ce4cec67ea1.png)

### 按月看拐点清晰

把阅读与点赞按月汇总后可以发现，整体流量从 2024 年 1 月起明显抬升。此后账号长期维持高位，而非单篇脉冲。

![](img/f817e9b50eb5167081646bfa708bbb9c.png)

结合时间、阅读与主题，可把演进分为三段。

第一阶段：沉淀期 2023.2 - 2023.12.5
持续输出 AI 相关内容，单篇峰值约 4 万，初步建立内容能力与种子受众。

第二阶段：爆发期 2023.12.6 - 2024.2
2023.12.6 Pika 评测 7.8 万；2024.1 Magnific AI 突破十万；2024.2 Sora 再次突破十万，完成破圈。

第三阶段：高产期 2024.2 起
围绕 AI 应用、工具测评、技术解读与行业案例持续输出，累计 11 篇十万 +。

这说明增长并非单篇决定，而是长期积累、热点卡点与持续输出的叠加。

## 三、账号来源

主要依据新榜的 AI 账号榜单：https://www.newrank.cn/rankai/gongzhonghao

先分别抓取日榜与月榜，合并去重后得到 153 个对象，作为对标池。

榜单页本身仅支持前 20 条导出，但不影响采集。借助影刀自动化，可定位标签页后批量抽取表格结构，将完整榜单导出。

![](img/6d1ea28392972327e73283abee0147d1.png)

整理榜单后，按账号名称回溯历史稿件。

![](img/8e65ee234137a205829e31e679deb19d.png)

具体采集手段不展开。最终得到约 7 万条记录，覆盖🛰️生态里代表性较强的 AI 创作者，仍在持续补充。受飞书多维表格条数限制，建议原始数据以 Excel 或数据库形式保存。

## 四、从原始稿件到洞察

7 万条数据直接浏览效率极低，需要转为可视化与结构化结论。

向 Claude 提出的任务要点：

1. 可视化看板
展示阅读随时间变化、发文量、互动趋势、爆款分布、跨账号对比。支持图表下钻到单篇级别。图表类型包括折线、柱状、散点、热力、分布等。

2. 互动与发布时间分析
日/周/月阅读走势，点赞与阅读比例，评论与阅读关系，不同发布时间段的表现差异。

3. 自动化报告
自动输出账号概览、关键增长节点、代表爆款、阅读与互动趋势、运营特征与可复用的内容策略。

数据表结构示例：

```sql
CREATE TABLE `wechat_articles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nick_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `original_article_count` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `original_content_str` text COLLATE utf8mb4_general_ci,
  `title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `digest` text COLLATE utf8mb4_general_ci,
  `show_desc` text COLLATE utf8mb4_general_ci,
  `item_index` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `url` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `is_original` tinyint(1) DEFAULT NULL,
  `read_view` int DEFAULT NULL,
  `like_count` int DEFAULT NULL,
  `send_time` datetime DEFAULT NULL,
  `collect_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=18252 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

该结构可支撑账号识别、稿件统计、阅读计算、原创判断、发布时间分析等需求。

![](img/c1b9ca29b9de87a7bac57e9180035550.png)

![](img/671403ca4c24bf1bd7d6ec02689df56a.png)

Cursor 初次生成的脚本已能完成清洗与绘图，但把全部稿件当成单一账号处理。需要明确按账号名称分组，逐号输出画像。

每个账号需包含：账号名称、最早发布时间、最近发布时间、稿件总数、平均阅读、平均点赞、原创数、阅读最高的 20 篇、阅读随时间曲线、阅读分布、月度阅读与点赞趋势。

![](img/81d392d91931fd41494d2f8c93765b3b.png)

![](img/4cab3c7ab6e52f172891b83f30547965.png)

再次执行后，每个账号都能得到独立画像。若逐个文件输出不便阅读，于是合并为统一 PDF。

![](img/6888fe0208392b0643809ef84012ea06.png)

![](img/7d50635e32b1b37997ec046ab207099e.png)

![](img/b78b333de4172e4c4c5ce6cb76548e88.png)

![](img/76cce99e47107586265ba2363217b863.png)

![](img/7ff5936a689d7da1be8a6e8c4f5f91e3.png)

要求直接生成总 PDF，并附账号目录，支持点击跳转。

![](img/af421c6bd4c11b56f051bfbf84d14f11.png)

![](img/3a3a93b45e591a9ff635834e356e30ac.png)

![](img/0bef3a96ae8019804d248f6fb2cce570.png)

最终 PDF 形态如下。实现代码由模型一次生成通过。

这套流程的核心价值在于：从海量公开稿件中看到主题传播规律、拐点出现时机、爆款前的铺垫信号、内容结构差异，以及工具盘点、技术解读、热点追踪各自带来的流量贡献，帮助判断增长来自偶发爆文还是系统化运营。

```
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import os
import matplotlib as mpl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from io import BytesIO

# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 注册中文字体
pdfmetrics.registerFont(TTFont('SimHei', 'SimHei.ttf'))

# 连接数据库并读取数据
engine = create_engine('mysql+pymysql://username:password@host/wechat_article')
query = "SELECT * FROM wechat_articles"
df = pd.read_sql(query, engine)

# 数据预处理
df['send_time'] = pd.to_datetime(df['send_time'])
df['collect_time'] = pd.to_datetime(df['collect_time'])

# 创建输出目录
output_dir = 'wechat_analysis_reports'
os.makedirs(output_dir, exist_ok=True)

# 创建一个PDF合并器
merger = PdfMerger()

# 创建目录
toc = []

# 对每个👸号进行分析
for i, nickname in enumerate(df['nick_name'].unique(), 1):
    account_df = df[df['nick_name'] == nickname]

    # 创建临时PDF文件
    temp_pdf = BytesIO()
    with PdfPages(temp_pdf) as pdf:

        # 1\. 👸号基本信息
        plt.figure(figsize=(12, 6))
        info = {
            '👸号名称': nickname,
            '最早文章日期': account_df['send_time'].min().strftime('%Y-%m-%d'),
            '最新文章日期': account_df['send_time'].max().strftime('%Y-%m-%d'),
            '平均阅读数': f"{account_df['read_view'].mean():.2f}",
            '平均点赞数': f"{account_df['like_count'].mean():.2f}",
            '文章总数': len(account_df),
            '原创文章数': account_df['is_original'].sum()
        }
        plt.text(0.1, 0.1, '\n'.join([f'{k}: {v}' for k, v in info.items()]), {'fontsize': 12})
        plt.axis('off')
        plt.title(f'👸号基本信息 - {nickname}')
        pdf.savefig()
        plt.close()

        # 2\. 阅读数最高的20篇文章
        top_articles = account_df.nlargest(20, 'read_view')[['title', 'read_view', 'like_count', 'send_time']]
        plt.figure(figsize=(12, 10))
        plt.barh(top_articles['title'], top_articles['read_view'])
        plt.title(f'阅读数最高的20篇文章 - {nickname}')
        plt.xlabel('阅读数')
        plt.tight_layout()
        pdf.savefig()
        plt.close()

        # 3\. 阅读数随时间的变化趋势图
        plt.figure(figsize=(12, 6))
        account_df.set_index('send_time')['read_view'].plot()
        plt.title(f'阅读数随时间的变化趋势 - {nickname}')
        plt.ylabel('阅读数')
        pdf.savefig()
        plt.close()

        # 4\. 文章阅读数分布图
        plt.figure(figsize=(12, 6))
        sns.histplot(account_df['read_view'], kde=True)
        plt.title(f'文章阅读数分布 - {nickname}')
        plt.xlabel('阅读数')
        pdf.savefig()
        plt.close()

        # 5\. 月度阅读数和点赞数趋势图
        monthly_stats = account_df.set_index('send_time').resample('M').agg({
            'read_view': 'mean',
            'like_count': 'mean'
        })

        fig, ax1 = plt.subplots(figsize=(12, 6))
        ax2 = ax1.twinx()

        ax1.plot(monthly_stats.index, monthly_stats['read_view'], 'g-')
        ax2.plot(monthly_stats.index, monthly_stats['like_count'], 'b-')

        ax1.set_xlabel('日期')
        ax1.set_ylabel('平均阅读数', color='g')
        ax2.set_ylabel('平均点赞数', color='b')

        plt.title(f'月度平均阅读数和点赞数趋势 - {nickname}')
        plt.tight_layout()
        pdf.savefig()
        plt.close()

    # 将临时PDF添加到合并器
    temp_pdf.seek(0)
    merger.append(temp_pdf)

    # 添加到目录
    toc.append((nickname, i))

    print(f"已生成 {nickname} 的报告")

# 创建目录页
toc_pdf = BytesIO()
c = canvas.Canvas(toc_pdf, pagesize=letter)
c.setFont("SimHei", 14)
c.drawString(100, 750, "目录")
y = 700
for name, page in toc:
    c.setFont("SimHei", 12)
    c.drawString(100, y, f"{name}")
    c.drawString(400, y, f"{page}")
    y -= 20
    if y < 50:
        c.showPage()
        y = 750
c.save()

# 将目录添加到合并器的开头
toc_pdf.seek(0)
merger.merge(0, toc_pdf)

# 保存最终的PDF
final_pdf_path = os.path.join(output_dir, 'wechat_analysis_report.pdf')
merger.write(final_pdf_path)
merger.close()

print(f"总报告已生成：{final_pdf_path}")
```
报告倒是出来了，但光看那一屏界面，总觉得差点意思。想让颜值再往上走一点，还能随时切换风格，那也只能自己动手搞前端界面了。于是继续把需求丢给Cursor，让它按想法生成一套视觉、交互俱佳的界面。不巧的是，Cursor有500条对话的硬限制，超了之后我注销重来，之前的提示词全被清空。实在没别的办法，只能将现有代码一股脑全部贴进去。最终把整版界面彻底优化了一遍，也就是开头截屏里看到的效果。

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
'use client';

import { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, BarChart, Bar, ScatterChart, Scatter } from 'recharts';
import {  TooltipProps } from 'recharts';
import { NameType, ValueType } from 'recharts/types/component/DefaultTooltipContent';
import { useCallback } from 'react';
import WordCloud from 'react-d3-cloud';

import {WechatArticle} from "@/app/types/wechatarticle"
export default function Wechat() {

  const [selectedUsername, setSelectedUsername] = useState('gh_57bbdcde9820');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const publicAccounts = [

  ];
  interface ApiResponse {
    code: number;
    message: string;
    data: WechatAccount[];
  }
  interface WechatAccount {
    nickname: string;
    username: string;
    createTime: string;
    fetchTime: string | null;
  }
  interface WechatAnalyticsProps {
    chartData: {
      readViewTrend: Array<{ sendTime: string; readView: number }>;
      readViewDistribution: Array<{ label: string; count: number }>; // 修改这里

      readLikeScatter: Array<{ readView: number; likeCount: number }>;
      monthlyStats: Array<{ month: string; avgReadView: number; avgLikeCount: number; articleCount: number }>;
    };
  }
  interface WechatAnaInfo {
    data: {
      data: {
        stats: {
          wechatNickname: string;
          earliestArticleDate: string;
          latestArticleDate: string;
          averageReadCount: number;
          averageLikeCount: number;
          totalArticles: number;
          totalOriginalArticles: number;
        };
        viralArticles: WechatArticle[];
        surgeArticles: WechatArticle[];
        topLikedArticles: WechatArticle[];
        topReadArticles: WechatArticle[];
        earliestArticles: WechatArticle[];
        latestArticles: WechatArticle[];
        aboveAverageReadArticles: WechatArticle[];
        allArticles: WechatArticle[];
        chartData: WechatAnalyticsProps['chartData'];
      };
    };
  }

const [wechatarticleInfo, setWechatarticleInfo] = useState<wechatarticle>([]);
const [wechatanaInfo, setWechatanaInfo] = useState<wechatanainfo null="">(null);
const [stats, setStats] = useState<any>(null);
const [activeTab, setActiveTab] = useState<string>("最新文章");
const [activeAccounts, setActiveAccounts] = useState<wechataccount>([]);

const fontSizeMapper = useCallback((word: { value: number }) => Math.log2(word.value) * 5 + 16, []);

const generateWordCloudData = (articles: WechatArticle[]) => {
  const wordCount: { [key: string]: number } = {};
  articles.forEach(article => {
    const words = article.title.split(/\s+/);
    words.forEach(word => {
      if (word.length > 1) {  // 忽略单个字符
        wordCount[word] = (wordCount[word] || 0) + 1;
      }
    });
  });
  return Object.entries(wordCount).map(([text, value]) => ({ text, value }));
};
const getActiveAccounts = async () => {
  setIsLoading(true);
  try {
    const uri = "/api/wechat/keyword";

    const response = await fetch(uri, {
      method: "POST",
    });
    if (response.ok) {
      const result: ApiResponse = await response.json();
      if (result.code === 0 && Array.isArray(result.data)) {
        setActiveAccounts(result.data);
        if (result.data.length > 0) {
          setSelectedUsername(result.data[0].username);
        }
      } else {
        console.error("获取活跃👸号失败:", result.message);
        setActiveAccounts([]);
      }
    } else {
      console.error("获取活跃👸号失败: 服务器响应错误");
      setActiveAccounts([]);
    }
  } catch (error) {
    console.error("获取活跃👸号失败:", error);
    setActiveAccounts([]);
  } finally {
    setIsLoading(false);
  }
};
 const getWechatInfo = async () => {
  try {
    const uri = "/api/wechat_info";
    const params = {
      "keyword":"username"
    };
    const resp = await fetch(uri, {
      method: "POST",
      body: JSON.stringify(params),
    });
    if (resp.ok) {
      const res = await resp.json();
      console.log("开始设置咯", res)
      setWechatarticleInfo(res)
    }
  } catch (e) {
    console.log("insert failed: ", e);
  }
 }

 const getWechatAna = async (username: string) => {
  setIsLoading(true);
  try {
    const uri = "/api/wechat/ana";
    const params = {
      "username": username
    };
    const resp = await fetch(uri, {
      method: "POST",
      body: JSON.stringify(params),
    });
    if (resp.ok) {
      const res = await resp.json();
      console.log("开始设置ana咯", res);
      setWechatanaInfo(res);
      setSelectedUsername(username);
    }
  } catch (e) {
    console.log("获取数据失败: ", e);
  } finally {
    setIsLoading(false);
  }
}

 useEffect(() => {
  if (selectedUsername) {
    getWechatAna(selectedUsername);
  }
}, [selectedUsername]);

useEffect(() => {
  getActiveAccounts();
}, []);

  const renderStats = () => {
    if (!wechatanaInfo || !wechatanaInfo.data || !wechatanaInfo.data.data) return null;

    const { stats, viralArticles, allArticles, topLikedArticles, topReadArticles, earliestArticles, latestArticles, aboveAverageReadArticles, chartData } = wechatanaInfo.data.data;

    return (

# 👸号名称：{stats.wechatNickname}

          最早文章日期
          {new Date(stats.earliestArticleDate).toLocaleDateString('zh-CN')}

          最新文章日期
          {new Date(stats.latestArticleDate).toLocaleDateString('zh-CN')}

          平均阅读数
          {stats.averageReadCount}

          平均点赞数
          {stats.averageLikeCount}

          文章总数
          {stats.totalArticles}

          原创文章数
          {stats.totalOriginalArticles}

       setActiveTab("所有文章")}>所有文章
           setActiveTab("爆款文章")}>爆款文章
           setActiveTab("最新文章")}>最新文章🔥
           setActiveTab("阅读最高")}>阅读最高
           setActiveTab("点赞最高")}>点赞最高
           setActiveTab("最早文章")}>最早文章
           setActiveTab("高于平均阅读")}>高于平均阅读

        {activeTab === "所有文章" && renderArticleTable("所有文章", allArticles)}
        {activeTab === "爆款文章" && renderArticleTable("爆款文章", viralArticles)}
        {activeTab === "点赞最高" && renderArticleTable("点赞最高的文章", topLikedArticles.slice(0, 10))}
        {activeTab === "阅读最高" && renderArticleTable("阅读最高的文章", topReadArticles.slice(0, 20))}
        {activeTab === "最早文章" && renderArticleTable("最早发布的文章", earliestArticles.slice(0, 10))}
        {activeTab === "最新文章" && renderArticleTable("最新发布的文章", latestArticles.slice(0, 10))}
        {activeTab === "高于平均阅读" && renderArticleTable("高于平均阅读数的文章", aboveAverageReadArticles)}

    );
  };

  const renderArticleTable = (title: string, articles: WechatArticle[]) => {
    return (

## {title}

          {articles.map((article, index) => (

          ))}

             标题 |
               阅读数 |
               点赞数 |
               发布时间 |
               链接 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

               {article.title} |
               {article.readView} |
               {article.likeCount} |
               {new Date(article.sendTime).toLocaleDateString('zh-CN')} |
                                []({article.url}) 
               |

    );
  };

  const renderChart = () => {
    if (!wechatanaInfo || !wechatanaInfo.data || !wechatanaInfo.data.data) return null;
    const { allArticles, chartData } = wechatanaInfo.data.data;

    if (!chartData) return null;

    const wordCloudData = generateWordCloudData(allArticles);

    const CustomTooltip = ({ active, payload, label }: TooltipProps<valuetype nametype="">) => {
      if (active && payload && payload.length) {
        return (

{`阅读数范围: ${label}`}

{`文章数量: ${payload[0].value}`}

        );
      }

      return null;
    };

    return (

        <chartsection title="阅读数随时间变化趋势"><linechart width="{800}" height="{400}" data="{chartData.readViewTrend}"><xaxis datakey="sendTime" name="时间"><yaxis><cartesiangrid strokedasharray="3 3"></cartesiangrid></yaxis></xaxis></linechart></chartsection> 

        <chartsection title="文章阅读数分布"><barchart width="{800}" height="{400}" data="{chartData.readViewDistribution}"><xaxis datakey="label"><yaxis><cartesiangrid strokedasharray="3 3"><tooltip content="{<CustomTooltip">} />
          <legend><bar datakey="count" name="文章数量" fill="#8884d8"></bar></legend></tooltip></cartesiangrid></yaxis></xaxis></barchart></chartsection> 

        <chartsection title="月度统计"><linechart width="{800}" height="{400}" data="{chartData.monthlyStats}"><xaxis datakey="month"><yaxis yaxisid="left"><yaxis yaxisid="right" orientation="right"><cartesiangrid strokedasharray="3 3"></cartesiangrid></yaxis></yaxis></xaxis></linechart></chartsection> 

        <chartsection title="阅读数与点赞数关系"><scatterchart width="{800}" height="{400}"><xaxis datakey="readView" name="阅读数"><yaxis datakey="likeCount" name="点赞数"><tooltip cursor="{{" strokedasharray:=""><scatter name="阅读-点赞" data="{chartData.readLikeScatter}" fill="#8884d8"></scatter></tooltip></yaxis></xaxis></scatterchart></chartsection> 

        {/* <chartsection title="文章标题词云">

        </chartsection> */}

    );
  };
  const ChartSection = ({ title, children }: { title: string, children: React.ReactNode }) => (

## {title}

      {children}

  );
  return (

        {activeAccounts.map((account, index) => (
          setSelectedUsername(account.username)}
          >
            {account.nickname || account.username} 
        ))}

      {isLoading ? (
        加载中...
      ) : (
        <>
          {renderStats()}
          {renderChart()}
        >
      )}

  );
}</valuetype></wechataccount></string></any></wechatanainfo></wechatarticle></boolean> 
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
'use client';

import { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, BarChart, Bar, ScatterChart, Scatter } from 'recharts';
import {  TooltipProps } from 'recharts';
import { NameType, ValueType } from 'recharts/types/component/DefaultTooltipContent';
import { useCallback } from 'react';
import WordCloud from 'react-d3-cloud';

import {WechatArticle} from "@/app/types/wechatarticle"
export default function Wechat() {

  const [selectedUsername, setSelectedUsername] = useState('gh_57bbdcde9820');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const publicAccounts = [

  ];
  interface ApiResponse {
    code: number;
    message: string;
    data: WechatAccount[];
  }
  interface WechatAccount {
    nickname: string;
    username: string;
    createTime: string;
    fetchTime: string | null;
  }
  interface WechatAnalyticsProps {
    chartData: {
      readViewTrend: Array<{ sendTime: string; readView: number }>;
      readViewDistribution: Array<{ label: string; count: number }>; // 修改这里

      readLikeScatter: Array<{ readView: number; likeCount: number }>;
      monthlyStats: Array<{ month: string; avgReadView: number; avgLikeCount: number; articleCount: number }>;
    };
  }
  interface WechatAnaInfo {
    data: {
      data: {
        stats: {
          wechatNickname: string;
          earliestArticleDate: string;
          latestArticleDate: string;
          averageReadCount: number;
          averageLikeCount: number;
          totalArticles: number;
          totalOriginalArticles: number;
        };
        viralArticles: WechatArticle[];
        surgeArticles: WechatArticle[];
        topLikedArticles: WechatArticle[];
        topReadArticles: WechatArticle[];
        earliestArticles: WechatArticle[];
        latestArticles: WechatArticle[];
        aboveAverageReadArticles: WechatArticle[];
        allArticles: WechatArticle[];
        chartData: WechatAnalyticsProps['chartData'];
      };
    };
  }

const [wechatarticleInfo, setWechatarticleInfo] = useState<wechatarticle>([]);
const [wechatanaInfo, setWechatanaInfo] = useState<wechatanainfo null="">(null);
const [stats, setStats] = useState<any>(null);
const [activeTab, setActiveTab] = useState<string>("最新文章");
const [activeAccounts, setActiveAccounts] = useState<wechataccount>([]);

const fontSizeMapper = useCallback((word: { value: number }) => Math.log2(word.value) * 5 + 16, []);

const generateWordCloudData = (articles: WechatArticle[]) => {
  const wordCount: { [key: string]: number } = {};
  articles.forEach(article => {
    const words = article.title.split(/\s+/);
    words.forEach(word => {
      if (word.length > 1) {  // 忽略单个字符
        wordCount[word] = (wordCount[word] || 0) + 1;
      }
    });
  });
  return Object.entries(wordCount).map(([text, value]) => ({ text, value }));
};
const getActiveAccounts = async () => {
  setIsLoading(true);
  try {
    const uri = "/api/wechat/keyword";

    const response = await fetch(uri, {
      method: "POST",
    });
    if (response.ok) {
      const result: ApiResponse = await response.json();
      if (result.code === 0 && Array.isArray(result.data)) {
        setActiveAccounts(result.data);
        if (result.data.length > 0) {
          setSelectedUsername(result.data[0].username);
        }
      } else {
        console.error("获取活跃👸号失败:", result.message);
        setActiveAccounts([]);
      }
    } else {
      console.error("获取活跃👸号失败: 服务器响应错误");
      setActiveAccounts([]);
    }
  } catch (error) {
    console.error("获取活跃👸号失败:", error);
    setActiveAccounts([]);
  } finally {
    setIsLoading(false);
  }
};
 const getWechatInfo = async () => {
  try {
    const uri = "/api/wechat_info";
    const params = {
      "keyword":"username"
    };
    const resp = await fetch(uri, {
      method: "POST",
      body: JSON.stringify(params),
    });
    if (resp.ok) {
      const res = await resp.json();
      console.log("开始设置咯", res)
      setWechatarticleInfo(res)
    }
  } catch (e) {
    console.log("insert failed: ", e);
  }
 }

 const getWechatAna = async (username: string) => {
  setIsLoading(true);
  try {
    const uri = "/api/wechat/ana";
    const params = {
      "username": username
    };
    const resp = await fetch(uri, {
      method: "POST",
      body: JSON.stringify(params),
    });
    if (resp.ok) {
      const res = await resp.json();
      console.log("开始设置ana咯", res);
      setWechatanaInfo(res);
      setSelectedUsername(username);
    }
  } catch (e) {
    console.log("获取数据失败: ", e);
  } finally {
    setIsLoading(false);
  }
}

 useEffect(() => {
  if (selectedUsername) {
    getWechatAna(selectedUsername);
  }
}, [selectedUsername]);

useEffect(() => {
  getActiveAccounts();
}, []);

  const renderStats = () => {
    if (!wechatanaInfo || !wechatanaInfo.data || !wechatanaInfo.data.data) return null;

    const { stats, viralArticles, allArticles, topLikedArticles, topReadArticles, earliestArticles, latestArticles, aboveAverageReadArticles, chartData } = wechatanaInfo.data.data;

    return (

# 👸号名称：{stats.wechatNickname}

          最早文章日期
          {new Date(stats.earliestArticleDate).toLocaleDateString('zh-CN')}

          最新文章日期
          {new Date(stats.latestArticleDate).toLocaleDateString('zh-CN')}

          平均阅读数
          {stats.averageReadCount}

          平均点赞数
          {stats.averageLikeCount}

          文章总数
          {stats.totalArticles}

          原创文章数
          {stats.totalOriginalArticles}

       setActiveTab("所有文章")}>所有文章
           setActiveTab("爆款文章")}>爆款文章
           setActiveTab("最新文章")}>最新文章🔥
           setActiveTab("阅读最高")}>阅读最高
           setActiveTab("点赞最高")}>点赞最高
           setActiveTab("最早文章")}>最早文章
           setActiveTab("高于平均阅读")}>高于平均阅读

        {activeTab === "所有文章" && renderArticleTable("所有文章", allArticles)}
        {activeTab === "爆款文章" && renderArticleTable("爆款文章", viralArticles)}
        {activeTab === "点赞最高" && renderArticleTable("点赞最高的文章", topLikedArticles.slice(0, 10))}
        {activeTab === "阅读最高" && renderArticleTable("阅读最高的文章", topReadArticles.slice(0, 20))}
        {activeTab === "最早文章" && renderArticleTable("最早发布的文章", earliestArticles.slice(0, 10))}
        {activeTab === "最新文章" && renderArticleTable("最新发布的文章", latestArticles.slice(0, 10))}
        {activeTab === "高于平均阅读" && renderArticleTable("高于平均阅读数的文章", aboveAverageReadArticles)}

    );
  };

  const renderArticleTable = (title: string, articles: WechatArticle[]) => {
    return (

## {title}

          {articles.map((article, index) => (

          ))}

             标题 |
               阅读数 |
               点赞数 |
               发布时间 |
               链接 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

               {article.title} |
               {article.readView} |
               {article.likeCount} |
               {new Date(article.sendTime).toLocaleDateString('zh-CN')} |
                                []({article.url}) 
               |

    );
  };

  const renderChart = () => {
    if (!wechatanaInfo || !wechatanaInfo.data || !wechatanaInfo.data.data) return null;
    const { allArticles, chartData } = wechatanaInfo.data.data;

    if (!chartData) return null;

    const wordCloudData = generateWordCloudData(allArticles);

    const CustomTooltip = ({ active, payload, label }: TooltipProps<valuetype nametype="">) => {
      if (active && payload && payload.length) {
        return (

{`阅读数范围: ${label}`}

{`文章数量: ${payload[0].value}`}

        );
      }

      return null;
    };

    return (

        <chartsection title="阅读数随时间变化趋势"><linechart width="{800}" height="{400}" data="{chartData.readViewTrend}"><xaxis datakey="sendTime" name="时间"><yaxis><cartesiangrid strokedasharray="3 3"></cartesiangrid></yaxis></xaxis></linechart></chartsection> 

        <chartsection title="文章阅读数分布"><barchart width="{800}" height="{400}" data="{chartData.readViewDistribution}"><xaxis datakey="label"><yaxis><cartesiangrid strokedasharray="3 3"><tooltip content="{<CustomTooltip">} />
          <legend><bar datakey="count" name="文章数量" fill="#8884d8"></bar></legend></tooltip></cartesiangrid></yaxis></xaxis></barchart></chartsection> 

        <chartsection title="月度统计"><linechart width="{800}" height="{400}" data="{chartData.monthlyStats}"><xaxis datakey="month"><yaxis yaxisid="left"><yaxis yaxisid="right" orientation="right"><cartesiangrid strokedasharray="3 3"></cartesiangrid></yaxis></yaxis></xaxis></linechart></chartsection> 

        <chartsection title="阅读数与点赞数关系"><scatterchart width="{800}" height="{400}"><xaxis datakey="readView" name="阅读数"><yaxis datakey="likeCount" name="点赞数"><tooltip cursor="{{" strokedasharray:=""><scatter name="阅读-点赞" data="{chartData.readLikeScatter}" fill="#8884d8"></scatter></tooltip></yaxis></xaxis></scatterchart></chartsection> 

        {/* <chartsection title="文章标题词云">

        </chartsection> */}

    );
  };
  const ChartSection = ({ title, children }: { title: string, children: React.ReactNode }) => (

## {title}

      {children}

  );
  return (

        {activeAccounts.map((account, index) => (
          setSelectedUsername(account.username)}
          >
            {account.nickname || account.username} 
        ))}

      {isLoading ? (
        加载中...
      ) : (
        <>
          {renderStats()}
          {renderChart()}
        >
      )}

  );
}</valuetype></wechataccount></string></any></wechatanainfo></wechatarticle></boolean> 
```。

接下来要做的，就是接住它，然后，把故事讲下去。

Next.js API 路由实现方式

Route：

```
import { respData, respErr } from "@/app/utils/resp";

import { analyzeWechatAccount } from "@/app/models/wechatinteract";

export async function POST(req: Request) {
  const { username } = await req.json();

  const articles = await analyzeWechatAccount(username)

  return respData(articles);
}

```

API：

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
import mysql, { FieldPacket } from 'mysql2/promise';
import { WechatArticle } from '@/app/types/wechatarticle';
import { RowDataPacket } from 'mysql2';

// 数据库连接配置
const dbConfig = {
  your host address
};

// 获取数据库连接
async function getDbConnection() {
  return await mysql.createConnection(dbConfig);
}

async function getWechatArticlesByUsername(username: string): Promise {
  const conn = await getDbConnection();
  try {
    const query = `
      SELECT 
        id, user_name, nick_name, title, digest, url, 
        is_original, read_view, like_count, send_time
      FROM wechat_articles 
      WHERE user_name = ? 
      ORDER BY send_time DESC
    `;
    const [rows] = await conn.execute<rowdatapacket>(query, [username]);

    return rows.map(row => ({
      id: row.id,
      userName: row.user_name,
      nickName: row.nick_name,
      title: row.title,
      digest: row.digest,
      url: row.url,
      isOriginal: Boolean(row.is_original),
      readView: row.read_view,
      likeCount: row.like_count,
      sendTime: new Date(row.send_time)
    }));
  } finally {
    await conn.end();
  }
}

// 获取👸号文章数据

async function fetchData(userName: string): Promise <wechatarticle>{
  const conn = await getDbConnection();
  try {
    const [rows] = await conn.execute<mysql.rowdatapacket>(
      'SELECT * FROM wechat_articles WHERE user_name = ? order by send_time desc',
      [userName]
    );
    const articles = rows.map(row => ({
      id: row.id,
      userName: row.user_name,
      nickName: row.nick_name,
      title: row.title,
      digest: row.digest,
      url: row.url,
      isOriginal: Boolean(row.is_original),
      readView: row.read_view,
      likeCount: row.like_count,
      sendTime: new Date(row.send_time)
    }));

    // 计算原创文章数量
    const originalArticleCount = articles.filter(article => article.isOriginal).length;

    // 将原创文章数量添加到每个文章对象中
    return articles.map(article => ({
      ...article,
      originalArticleCount
    }));
  } finally {
    await conn.end();
  }
}

// 预处理数据
function preprocessData(articles: WechatArticle[]): WechatArticle[] {
  return articles.sort((a, b) => a.sendTime.getTime() - b.sendTime.getTime());
}

// 计算统计信息
function calculateStats(articles: WechatArticle[]) {
  return {
    wechatNickname: articles[0].nickName,
    earliestArticleDate: articles[0].sendTime,
    latestArticleDate: articles[articles.length - 1].sendTime,
    averageReadCount: Math.round(articles.reduce((sum, article) => sum + article.readView, 0) / articles.length),
    averageLikeCount: Math.round(articles.reduce((sum, article) => sum + article.likeCount, 0) / articles.length),
    totalArticles: articles.length,
    totalOriginalArticles: articles[0].originalArticleCount

  };
}

// 分析爆款文章
function analyzeViralArticles(articles: WechatArticle[]): WechatArticle[] {
  const threshold = articles.reduce((sum, article) => sum + article.readView, 0) / articles.length * 2;
  return articles
    .filter(article => article.readView > threshold)
    .sort((a, b) => b.readView - a.readView)
    .slice(0, 5);
}

// 分析阅读量增长
function analyzeReadViewGrowth(articles: WechatArticle[]): WechatArticle[] {
  const growthRates = articles.map((article, index) => {
    if (index === 0) return 0;
    return (article.readView - articles[index - 1].readView) / articles[index - 1].readView;
  });

  const meanGrowth = growthRates.reduce((sum, rate) => sum + rate, 0) / growthRates.length;
  const stdDevGrowth = Math.sqrt(growthRates.reduce((sum, rate) => sum + Math.pow(rate - meanGrowth, 2), 0) / growthRates.length);
  const growthThreshold = meanGrowth + 2 * stdDevGrowth;

  return articles.filter((_, index) => growthRates[index] > growthThreshold);
}

// 获取点赞最高的十篇文章
function getTopLikedArticles(articles: WechatArticle[], limit: number = 10): WechatArticle[] {
  return [...articles].sort((a, b) => b.likeCount - a.likeCount).slice(0, limit);
}

// 获取阅读量最高的十篇文章
function getTopReadArticles(articles: WechatArticle[], limit: number = 20): WechatArticle[] {
  return [...articles].sort((a, b) => b.readView - a.readView).slice(0, limit);
}

// 获取最早的十篇文章
function getEarliestArticles(articles: WechatArticle[], limit: number = 10): WechatArticle[] {
  return [...articles].sort((a, b) => a.sendTime.getTime() - b.sendTime.getTime()).slice(0, limit);
}

// 获取最新的十篇文章
function getLatestArticles(articles: WechatArticle[], limit: number = 10): WechatArticle[] {
  return [...articles].sort((a, b) => b.sendTime.getTime() - a.sendTime.getTime()).slice(0, limit);
}

// 获取高于平均阅读数的所有文章
function getAboveAverageReadArticles(articles: WechatArticle[]): WechatArticle[] {
  const averageReadCount = articles.reduce((sum, article) => sum + article.readView, 0) / articles.length;
  return articles.filter(article => article.readView > averageReadCount);
}

// 新增函数用于生成图表数据
function generateChartData(articles: WechatArticle[]) {
  // 阅读数随时间变化趋势
  const readViewTrend = articles.map(article => ({
    sendTime: article.sendTime.toISOString().slice(0, 10),
    readView: article.readView
  }));

   // 动态生成阅读量分布区间
   function generateReadViewRanges(articles: WechatArticle[]): { min: number; max: number; label: string }[] {
    const readViews = articles.map(a => a.readView);
    const minReadView = Math.min(...readViews);
    const maxReadView = Math.max(...readViews);

    // 确定基础单位（1000, 5000, 10000 等）
    let baseUnit = 1000;
    if (maxReadView > 100000) baseUnit = 10000;
    else if (maxReadView > 50000) baseUnit = 5000;

    const ranges = [];
    let currentMin = 0;
    while (currentMin < maxReadView) {
      let currentMax = currentMin + baseUnit - 1;
      if (currentMax > maxReadView) currentMax = maxReadView;

      let label = `${currentMin}-${currentMax}`;
      if (currentMin === 0) label = `0-${currentMax}`;
      if (currentMax === maxReadView) label = `${currentMin}+`;

      ranges.push({ min: currentMin, max: currentMax, label });
      currentMin = currentMax + 1;

      // 动态调整基础单位
      if (currentMin >= baseUnit * 10) baseUnit *= 2;
    }

    return ranges;
  }

  const readViewRanges = generateReadViewRanges(articles);

  const readViewDistribution = articles.reduce((acc, article) => {
    const range = readViewRanges.find(r => article.readView >= r.min && article.readView <= r.max);
    if (range) {
      acc[range.label] = (acc[range.label] || 0) + 1;
    }
    return acc;
  }, {} as Record<string number="">);

  // 阅读数与点赞数关系
  const readLikeScatter = articles.map(article => ({
    readView: article.readView,
    likeCount: article.likeCount
  }));

  // 月度统计
  const monthlyStats = articles.reduce((acc, article) => {
    const month = new Date(article.sendTime).toISOString().slice(0, 7);
    if (!acc[month]) {
      acc[month] = { readView: 0, likeCount: 0, count: 0 };
    }
    acc[month].readView += article.readView;
    acc[month].likeCount += article.likeCount;
    acc[month].count++;
    return acc;
  }, {} as Record<string readview:="" number="" likecount:="" count:="">);

  const monthlyStatsArray = Object.entries(monthlyStats).map(([month, stats]) => ({
    month,
    avgReadView: Math.round(stats.readView / stats.count),
    avgLikeCount: Number((stats.likeCount / stats.count).toFixed(1)),
    articleCount: stats.count
  }));

  return {
    readViewTrend,
    readViewDistribution: Object.entries(readViewDistribution).map(([label, count]) => ({ label, count })),

    readLikeScatter,
    monthlyStats: monthlyStatsArray
  };
}

// API函数
async function analyzeWechatAccount(userName: string) {
  try {
    const articles = await fetchData(userName);
    const processedArticles = preprocessData(articles);

    const stats = calculateStats(processedArticles);
    const viralArticles = analyzeViralArticles(processedArticles);
    // const surgeArticles = analyzeReadViewGrowth(processedArticles);

    const topLikedArticles = getTopLikedArticles(processedArticles);
    const topReadArticles = getTopReadArticles(processedArticles);
    const earliestArticles = getEarliestArticles(processedArticles);
    const latestArticles = getLatestArticles(processedArticles);
    const aboveAverageReadArticles = getAboveAverageReadArticles(processedArticles);

     // 生成图表数据
     const chartData = generateChartData(processedArticles);

    return {
      status: 'success',
      data: {
        stats,
        viralArticles: viralArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        topLikedArticles: topLikedArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        topReadArticles: topReadArticles.map(article => ({
          title: article.title,
          likeCount: article.likeCount,
          readView: article.readView,
          sendTime: article.sendTime,
          url: article.url
        })),
        earliestArticles: earliestArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        latestArticles: latestArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        aboveAverageReadArticles: aboveAverageReadArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        allArticles: articles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        chartData
      }
    };
  } catch (error) {
    return {
      status: 'error',
      message: error instanceof Error ? error.message : '发生未知错误'
    };
  }
}

async function getActiveWechatAccounts(): Promise<array nickname:="" string="" null="" username:="" createtime:="" date="" fetchtime:="">> {
  const conn = await getDbConnection();
  try {
    const query = `
      SELECT nickname, username, create_time, fetch_time
      FROM wechat_keyword

      ORDER BY create_time DESC
    `;
    const [rows] = await conn.execute<rowdatapacket>(query);

    return rows.map(row => ({
      nickname: row.nickname,
      username: row.username,
      createTime: new Date(row.create_time),
      fetchTime: row.fetch_time ? new Date(row.fetch_time) : null
    }));
  } finally {
    await conn.end();
  }
}

// 导出函数
export {
  getWechatArticlesByUsername,
  analyzeWechatAccount,
  getActiveWechatAccounts
};</rowdatapacket></array></string></string></mysql.rowdatapacket></wechatarticle></rowdatapacket> 
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
import mysql, { FieldPacket } from 'mysql2/promise';
import { WechatArticle } from '@/app/types/wechatarticle';
import { RowDataPacket } from 'mysql2';

// 数据库连接配置
const dbConfig = {
  your host address
};

// 获取数据库连接
async function getDbConnection() {
  return await mysql.createConnection(dbConfig);
}

async function getWechatArticlesByUsername(username: string): Promise {
  const conn = await getDbConnection();
  try {
    const query = `
      SELECT 
        id, user_name, nick_name, title, digest, url, 
        is_original, read_view, like_count, send_time
      FROM wechat_articles 
      WHERE user_name = ? 
      ORDER BY send_time DESC
    `;
    const [rows] = await conn.execute<rowdatapacket>(query, [username]);

    return rows.map(row => ({
      id: row.id,
      userName: row.user_name,
      nickName: row.nick_name,
      title: row.title,
      digest: row.digest,
      url: row.url,
      isOriginal: Boolean(row.is_original),
      readView: row.read_view,
      likeCount: row.like_count,
      sendTime: new Date(row.send_time)
    }));
  } finally {
    await conn.end();
  }
}

// 获取👸号文章数据

async function fetchData(userName: string): Promise <wechatarticle>{
  const conn = await getDbConnection();
  try {
    const [rows] = await conn.execute<mysql.rowdatapacket>(
      'SELECT * FROM wechat_articles WHERE user_name = ? order by send_time desc',
      [userName]
    );
    const articles = rows.map(row => ({
      id: row.id,
      userName: row.user_name,
      nickName: row.nick_name,
      title: row.title,
      digest: row.digest,
      url: row.url,
      isOriginal: Boolean(row.is_original),
      readView: row.read_view,
      likeCount: row.like_count,
      sendTime: new Date(row.send_time)
    }));

    // 计算原创文章数量
    const originalArticleCount = articles.filter(article => article.isOriginal).length;

    // 将原创文章数量添加到每个文章对象中
    return articles.map(article => ({
      ...article,
      originalArticleCount
    }));
  } finally {
    await conn.end();
  }
}

// 预处理数据
function preprocessData(articles: WechatArticle[]): WechatArticle[] {
  return articles.sort((a, b) => a.sendTime.getTime() - b.sendTime.getTime());
}

// 计算统计信息
function calculateStats(articles: WechatArticle[]) {
  return {
    wechatNickname: articles[0].nickName,
    earliestArticleDate: articles[0].sendTime,
    latestArticleDate: articles[articles.length - 1].sendTime,
    averageReadCount: Math.round(articles.reduce((sum, article) => sum + article.readView, 0) / articles.length),
    averageLikeCount: Math.round(articles.reduce((sum, article) => sum + article.likeCount, 0) / articles.length),
    totalArticles: articles.length,
    totalOriginalArticles: articles[0].originalArticleCount

  };
}

// 分析爆款文章
function analyzeViralArticles(articles: WechatArticle[]): WechatArticle[] {
  const threshold = articles.reduce((sum, article) => sum + article.readView, 0) / articles.length * 2;
  return articles
    .filter(article => article.readView > threshold)
    .sort((a, b) => b.readView - a.readView)
    .slice(0, 5);
}

// 分析阅读量增长
function analyzeReadViewGrowth(articles: WechatArticle[]): WechatArticle[] {
  const growthRates = articles.map((article, index) => {
    if (index === 0) return 0;
    return (article.readView - articles[index - 1].readView) / articles[index - 1].readView;
  });

  const meanGrowth = growthRates.reduce((sum, rate) => sum + rate, 0) / growthRates.length;
  const stdDevGrowth = Math.sqrt(growthRates.reduce((sum, rate) => sum + Math.pow(rate - meanGrowth, 2), 0) / growthRates.length);
  const growthThreshold = meanGrowth + 2 * stdDevGrowth;

  return articles.filter((_, index) => growthRates[index] > growthThreshold);
}

// 获取点赞最高的十篇文章
function getTopLikedArticles(articles: WechatArticle[], limit: number = 10): WechatArticle[] {
  return [...articles].sort((a, b) => b.likeCount - a.likeCount).slice(0, limit);
}

// 获取阅读量最高的十篇文章
function getTopReadArticles(articles: WechatArticle[], limit: number = 20): WechatArticle[] {
  return [...articles].sort((a, b) => b.readView - a.readView).slice(0, limit);
}

// 获取最早的十篇文章
function getEarliestArticles(articles: WechatArticle[], limit: number = 10): WechatArticle[] {
  return [...articles].sort((a, b) => a.sendTime.getTime() - b.sendTime.getTime()).slice(0, limit);
}

// 获取最新的十篇文章
function getLatestArticles(articles: WechatArticle[], limit: number = 10): WechatArticle[] {
  return [...articles].sort((a, b) => b.sendTime.getTime() - a.sendTime.getTime()).slice(0, limit);
}

// 获取高于平均阅读数的所有文章
function getAboveAverageReadArticles(articles: WechatArticle[]): WechatArticle[] {
  const averageReadCount = articles.reduce((sum, article) => sum + article.readView, 0) / articles.length;
  return articles.filter(article => article.readView > averageReadCount);
}

// 新增函数用于生成图表数据
function generateChartData(articles: WechatArticle[]) {
  // 阅读数随时间变化趋势
  const readViewTrend = articles.map(article => ({
    sendTime: article.sendTime.toISOString().slice(0, 10),
    readView: article.readView
  }));

   // 动态生成阅读量分布区间
   function generateReadViewRanges(articles: WechatArticle[]): { min: number; max: number; label: string }[] {
    const readViews = articles.map(a => a.readView);
    const minReadView = Math.min(...readViews);
    const maxReadView = Math.max(...readViews);

    // 确定基础单位（1000, 5000, 10000 等）
    let baseUnit = 1000;
    if (maxReadView > 100000) baseUnit = 10000;
    else if (maxReadView > 50000) baseUnit = 5000;

    const ranges = [];
    let currentMin = 0;
    while (currentMin < maxReadView) {
      let currentMax = currentMin + baseUnit - 1;
      if (currentMax > maxReadView) currentMax = maxReadView;

      let label = `${currentMin}-${currentMax}`;
      if (currentMin === 0) label = `0-${currentMax}`;
      if (currentMax === maxReadView) label = `${currentMin}+`;

      ranges.push({ min: currentMin, max: currentMax, label });
      currentMin = currentMax + 1;

      // 动态调整基础单位
      if (currentMin >= baseUnit * 10) baseUnit *= 2;
    }

    return ranges;
  }

  const readViewRanges = generateReadViewRanges(articles);

  const readViewDistribution = articles.reduce((acc, article) => {
    const range = readViewRanges.find(r => article.readView >= r.min && article.readView <= r.max);
    if (range) {
      acc[range.label] = (acc[range.label] || 0) + 1;
    }
    return acc;
  }, {} as Record<string number="">);

  // 阅读数与点赞数关系
  const readLikeScatter = articles.map(article => ({
    readView: article.readView,
    likeCount: article.likeCount
  }));

  // 月度统计
  const monthlyStats = articles.reduce((acc, article) => {
    const month = new Date(article.sendTime).toISOString().slice(0, 7);
    if (!acc[month]) {
      acc[month] = { readView: 0, likeCount: 0, count: 0 };
    }
    acc[month].readView += article.readView;
    acc[month].likeCount += article.likeCount;
    acc[month].count++;
    return acc;
  }, {} as Record<string readview:="" number="" likecount:="" count:="">);

  const monthlyStatsArray = Object.entries(monthlyStats).map(([month, stats]) => ({
    month,
    avgReadView: Math.round(stats.readView / stats.count),
    avgLikeCount: Number((stats.likeCount / stats.count).toFixed(1)),
    articleCount: stats.count
  }));

  return {
    readViewTrend,
    readViewDistribution: Object.entries(readViewDistribution).map(([label, count]) => ({ label, count })),

    readLikeScatter,
    monthlyStats: monthlyStatsArray
  };
}

// API函数
async function analyzeWechatAccount(userName: string) {
  try {
    const articles = await fetchData(userName);
    const processedArticles = preprocessData(articles);

    const stats = calculateStats(processedArticles);
    const viralArticles = analyzeViralArticles(processedArticles);
    // const surgeArticles = analyzeReadViewGrowth(processedArticles);

    const topLikedArticles = getTopLikedArticles(processedArticles);
    const topReadArticles = getTopReadArticles(processedArticles);
    const earliestArticles = getEarliestArticles(processedArticles);
    const latestArticles = getLatestArticles(processedArticles);
    const aboveAverageReadArticles = getAboveAverageReadArticles(processedArticles);

     // 生成图表数据
     const chartData = generateChartData(processedArticles);

    return {
      status: 'success',
      data: {
        stats,
        viralArticles: viralArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        topLikedArticles: topLikedArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        topReadArticles: topReadArticles.map(article => ({
          title: article.title,
          likeCount: article.likeCount,
          readView: article.readView,
          sendTime: article.sendTime,
          url: article.url
        })),
        earliestArticles: earliestArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        latestArticles: latestArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        aboveAverageReadArticles: aboveAverageReadArticles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        allArticles: articles.map(article => ({
          title: article.title,
          readView: article.readView,
          likeCount: article.likeCount,
          sendTime: article.sendTime,
          url: article.url
        })),
        chartData
      }
    };
  } catch (error) {
    return {
      status: 'error',
      message: error instanceof Error ? error.message : '发生未知错误'
    };
  }
}

async function getActiveWechatAccounts(): Promise<array nickname:="" string="" null="" username:="" createtime:="" date="" fetchtime:="">> {
  const conn = await getDbConnection();
  try {
    const query = `
      SELECT nickname, username, create_time, fetch_time
      FROM wechat_keyword

      ORDER BY create_time DESC
    `;
    const [rows] = await conn.execute<rowdatapacket>(query);

    return rows.map(row => ({
      nickname: row.nickname,
      username: row.username,
      createTime: new Date(row.create_time),
      fetchTime: row.fetch_time ? new Date(row.fetch_time) : null
    }));
  } finally {
    await conn.end();
  }
}

// 导出函数
export {
  getWechatArticlesByUsername,
  analyzeWechatAccount,
  getActiveWechatAccounts
};</rowdatapacket></array></string></string></mysql.rowdatapacket></wechatarticle></rowdatapacket> 
```。

接下来要做的，就是接住它，然后，把故事讲下去。

龙哥有句话特别戳人：最好的机会，永远是在“现在”这个节点上。与其观望等待，不如立刻出发。所以我把这份数据分析整理了出来，希望能给正在关注AI自媒体方向的朋友们一些启发和落地参考。数据不一定能告诉你标准答案，但它能照亮下一步该怎么走。想入局的圈友，不妨趁此刻，顺势行动起来。[PRE*]