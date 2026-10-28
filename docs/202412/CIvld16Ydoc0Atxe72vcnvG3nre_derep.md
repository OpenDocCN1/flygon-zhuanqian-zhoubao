嘿，各位做YouTube Shorts的小伙伴们，我是龙哥！

不知道你们是不是也跟我一样，在做频道的时候被这两件事折磨过：第一，满世界找对标账号，还要挨个记录人家的订阅数、播放量、地区这些数据，就为了判断这个赛道到底值不值得做；第二，好不容易锁定了对标账号，又得把人家那些爆款视频一个个扒下来，然后掰开揉碎了研究、模仿。

说实话，我自己在运营YouTube的时候就被这两个问题卡过脖子。最开始全靠人工操作：手动搜对标、手动记数据、手动复制链接，再跑去在线下载网站一个个扒视频。数量少的时候倒还好，咬咬牙一会儿就搞定了。可一旦遇上几十个对标账号、几百条爆款视频，纯手动基本就是灾难——咱们算笔账，收集一个频道的资料差不多要一分钟，下载一条视频又要一分钟，几十个、几百个需求堆在一起，光做这些重复劳动就得耗掉好几个小时，效率低到让人抓狂。

所以后来我干脆自己动手，用Cursor写了两个自动化小工具，今天分享出来，希望能帮大家省点时间：

第一个是“YouTube数据采集器”——支持把频道ID、频道链接或者用户名批量写进Excel，软件会自动帮你抓取频道信息和热门视频数据；
第二个是“YouTube批量视频下载器”——把视频链接批量放进Excel，就能实现全自动下载，不用再一个个手动保存了。

废话不多说，我直接奔主题，把这两个工具的用法给大家讲清楚。

先提醒一句：这俩工具都是在Windows环境下开发的，Mac能不能用我不太确定，用Mac的朋友可以自己试试看。

---

## 一、YouTube数据采集器

### 工具是干嘛的？

先给大家看一下它的界面长什么样：

![](img/948cf89d6c5a63a9f24a942d4800815c.png)

它的底层逻辑其实很简单：调用YouTube官方提供的API去抓取频道和视频信息。当然，官方API是有配额限制的，不过咱们自己用的话，每天采集几千个频道或视频的数据完全够使了。

具体来说，它能帮你做两件事：

第一，支持用Excel文件批量导入频道的ID、链接或用户名，自动抓取这个频道的核心数据，包括：频道名称、简介、订阅数、总观看次数、作品总数、创建时间、所在地区。

![](img/bd710742ffe637820fea4d79308f0e01.png)

第二，在抓取频道信息的基础上，你还可以设定一个观看量阈值（比如只看超过X次播放的视频），然后批量抓取符合条件的视频数据，具体包括：视频标题、简介、发布时间、播放量、点赞数、评论数、标签、视频链接。

![](img/37d9b22ddd363862a4224200f98f0262.png)

### 用之前需要准备什么？

因为工具要调用YouTube API，而咱们在国内访问不了，所以用之前必须做几项准备工作：

**第一步，先把魔法打开。**  
不开魔法，工具根本跑不动，这一点千万记住！具体怎么开我就不多说了，大家自行解决。

**第二步，去申请你的YouTube API Key（重点！）**  
这个方法是参考马哥的教程整理的，步骤走一遍就行：

先开好魔法，打开这个网站：https://console.cloud.google.com/

进去之后，在页面上找到“API和服务”并点击。

![](img/ff82c74ca18b82eff11a84e9030fe6cf.png)

接着，点击“启用API和服务”按钮。

![](img/1269fb5649c1807066ee021909c6fa68.png)

在搜索框里输入“Youtube”，敲一下回车。

![](img/d75cd0811c597425768f8afe03ff94bb.png)

搜索结果里选第一个——“YouTube Data API v3”。

![](img/a6d5f62b0876225f4e07bb95b50b3797.png)

点进去之后，点击“启动”，等页面显示“API已启用”就表示成功了。

![](img/89bde2f9b0a4bca889c76ae411469c0b.png)

然后点击“管理”，跳转后，在左侧菜单找到“凭据”并点击。

![](img/e59cf982a48af64477de11677bd194a1.png)

![](img/d39d75cc06e0badaa70d8c0679dc91c2.png)

进入凭据页面后，点击顶部的“创建凭据”，在下拉菜单里选择“API密钥”。

![](img/142b3b52e7c87a7555746f530391e133.png)

![](img/cd0f619482a97f7f96d7e07ac09cec16.png)

密钥生成后，点击“显示密钥”，把那一长串字符复制下来。

![](img/bf2c57ba1d329d9a01d5305ff85d6862.png)

![](img/309affa410e0bdcc9833b45c0de4ab1a.png)

复制好之后，打开工具，把密钥粘贴到“YouTube API Key”输入框里，然后点“保存”就搞定收工了。

（这里说一下：如果你不点保存，下次打开软件还得重新输入一遍；保存之后就不用再动了。）

![](img/b18ca715e6e80a7e493f144c31ec18d1.png)

**第三步，找到你的代理端口地址（重点！）**

因为咱们在墙内，光有API Key还不够，软件还得借助你的代理才能“出门”采集数据。那怎么看自己的代理端口是多少？这个直接去问ChatGPT就行。

打开ChatGPT，输入这段提示词：

> 我用的代理软件是（填你自己用的软件名字），我不太会用这个软件，麻烦你一步一步教我怎么查看代理端口地址。

聊天过程中，如果GPT让你发截图，你就把自己软件界面的截图丢给它，它会一步步带着你找到正确的端口。

![](img/6af1d9b05577ecf5fd5f578d5af48199.png)

这里要特别提醒一下：不同代理软件的端口地址是不同的，千万别照抄我的——你照抄我的大概率会报错！正确的做法就是像我说的，去问GPT。

拿到端口地址后，同样打开工具，在“代理地址”栏里输入并保存。

![](img/573a1644fcd1c6431269cab2e6681024.png)

**第四步，准备一个Excel文件，里面包含频道ID/频道链接/用户名**

这个工具支持三种格式来填写频道信息：

① 频道ID：以UC开头，比如“UC-PzuWWwlOMynKP7w2BvM6g”，获取方式可以按图示操作。

![](img/339f24c5301255a9f1d4559b042591e4.png)

② 频道链接：格式是“https://www.youtube.com/@username”，比如“https://www.youtube.com/@CalmCity-channel”，获取方式如下图。

![](img/dbb01a5cb4287f6a062d78f98b65f679.png)

![](img/6fb74a4b45c64941e599717350054f28.png)

③ 用户名：格式是“@username”，比如“@CalmCity-channel”，获取方式同样可以看图。

![](img/b3af59f29c8882467c1bb0de64d9761f.png)

这三种格式里，频道ID是最精准的，但不太好找；频道链接比较常用，精确度一般也够用；用户名虽然最方便，但精确度最差。所以我个人最推荐前两种。

补充一个小插曲：我之前采集“https://www.youtube.com/@HealingWithMe.”这个频道的数据时，用URL格式一直报错，因为它的链接末尾带了一个点号，跟别的频道链接太像了，程序老是认错。最后换成频道ID才搞定。这种情况算是比较特殊，但如果你追求百分百精确，那就用频道ID；大多数情况下，频道链接已经足够用了。

收集好频道信息后，把它们写进一个Excel文件里，格式参照下图：频道链接放在第一列，黄色那个格子不要放内容，程序识别不了，那个格子写不写东西都行。

![](img/fa8a09ac5958bc36ef6e99246d7e7554.png)

### 具体怎么操作？

前面那些准备都搞定了，就打开软件按下面步骤走：

① 输入API Key（记得保存）。

![](img/f56acad80497efac44f5fab0fdb5f8f3.png)

② 输入代理地址（记得保存）。

![](img/ee444cc0637644beef69b6cb91a75a96.png)

③ 设置你想抓取的视频播放量下限（只采集大于这个数值的视频）。

![](img/606154a61645a91a3b34ba6689a24513.png)

④ 选择Excel文件的路径。

![](img/298e98d6994dcb01485b9e874a8152c2.png)

⑤ 设置视频数据的保存路径（抓取到的视频信息会存成Excel文件）。

![](img/9ee972ac53192c556f85f485ce7f7b1a.png)

⑥ 点击“开始采集”，软件界面上会实时显示采集进度（比如一共抓了多少条符合条件的视频、文件存在了哪里）。

![](img/ec90b0918d8d2c0212b3a81e3d7b6485.png)

有一点要注意：频道的资料会保存在你放频道链接的那个Excel文件所在目录，视频数据则存在你选的保存路径里。给大家看下保存样例——

频道数据文件命名格式是：channel_updated_具体采集时间（年月日时分秒）：

![](img/8d64aa2055916e77bd0b9366a28a4092.png)

视频数据文件命名格式是：@用户名_video：

![](img/07b89a8e40bd45cee5c9efabda1d706c.png)

---

## 软件下载地址

工具放在百度网盘了，拿走不谢：

链接：https://pan.baidu.com/s/1PNbXdqmZPrjzQLi2cUYMUA?pwd=v8dk  
提取码：v8dk

## 源代码

### 主程序

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
import os
import logging
from datetime import datetime
import pandas as pd
from googleapiclient.discovery import build
from tenacity import retry, stop_after_attempt, wait_exponential

class YouTubeDataCollector:
    def __init__(self, api_key, view_threshold=1000000, proxy=None, save_path=None, logger_callback=None):
        """
        初始化收集器
        :param api_key: YouTube API密钥
        :param view_threshold: 视频观看量阈值
        :param proxy: 代理设置
        :param save_path: 数据保存路径
        :param logger_callback: 日志回调函数
        """
        # 配置代理
        if proxy:
            os.environ['HTTP_PROXY'] = proxy
            os.environ['HTTPS_PROXY'] = proxy

        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.logger_callback = logger_callback
        self.view_threshold = view_threshold  # 设置观看量阈值

        # 验证并设置保存路径
        if not save_path:
            raise ValueError("必须指定保存路径")
        self.video_save_path = save_path

        # 设置日志路径为保存路径下的 logs 文件夹
        self.log_path = os.path.join(self.video_save_path, "logs")

        # 配置日志
        self.setup_logging()

    def setup_logging(self):
        """设置日志"""
        # 创建日志目录
        os.makedirs(self.log_path, exist_ok=True)
        log_file = os.path.join(self.log_path, f'youtube_collector_{datetime.now().strftime("%Y%m%d")}.log')

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def log_message(self, message):
        """统一的日志记录函数"""
        self.logger.info(message)
        if self.logger_callback:
            self.logger_callback(message)

    def extract_channel_info(self, input_str):
        """
        从多种输入格式中提取频道信息
        支持的格式：
        1\. 频道ID (UC...)
        2\. 频道URL (https://www.youtube.com/@...)
        3\. 频道用户名 (@...)
        """
        try:
            self.log_message(f"正在处理输入: {input_str}")

            # 1\. 检查是否是频道ID (UC开头)
            if input_str.startswith('UC'):
                self.log_message("检测到频道ID格式")
                return self.get_channel_by_id(input_str)

            # 2\. 检查是否是频道URL或用户名
            if '/@' in input_str or input_str.startswith('@'):
                self.log_message("检测到频道用户名格式")
                username = input_str.split('/@')[-1].split('/')[0].strip() if '/@' in input_str else input_str.strip()
                return self.get_channel_by_username(username)

            self.log_message(f"无法识别的输入格式: {input_str}")
            return None

        except Exception as e:
            self.log_message(f"提取频道信息时出错: {str(e)}")
            return None

    def get_channel_by_id(self, channel_id):
        """直接通过频道ID获取信息"""
        try:
            request = self.youtube.channels().list(
                part="snippet,statistics,brandingSettings",
                id=channel_id
            )
            response = request.execute()

            if response.get('items'):
                channel = response['items'][0]
                self.log_message(f"成功获取频道信息: {channel['snippet']['title']}")
                return channel
            else:
                self.log_message(f"未找到频道ID: {channel_id}")
                return None

        except Exception as e:
            self.log_message(f"获取频道信息时出错: {str(e)}")
            return None

    def get_channel_by_username(self, username):
        """通过用户名获取频道信息"""
        try:
            # 移除@符号（如果存在）
            clean_username = username.lstrip('@')
            self.log_message(f"正在获取频道信息，用户名: {clean_username}")

            # 使用搜索方法查找频道
            try:
                request = self.youtube.search().list(
                    part="snippet",
                    q=clean_username,
                    type="channel",
                    maxResults=5
                )
                response = request.execute()

                if response.get('items'):
                    # 获取第一个搜索结果的频道ID
                    channel_id = response['items'][0]['id']['channelId']

                    # 使用频道ID获取完整信息
                    channel_request = self.youtube.channels().list(
                        part="snippet,statistics,brandingSettings",
                        id=channel_id
                    )
                    channel_response = channel_request.execute()

                    if channel_response.get('items'):
                        channel = channel_response['items'][0]
                        self.log_message(f"成功找到频道: {channel['snippet']['title']}")
                        return channel

            except Exception as e:
                self.log_message(f"搜索频道时出错: {str(e)}")

            return None

        except Exception as e:
            self.log_message(f"获取频道信息时出错: {str(e)}")
            return None

    def get_channel_data(self, input_str):
        """获取频道数据的主方法"""
        try:
            channel = self.extract_channel_info(input_str)
            if not channel:
                self.log_message(f"无法获取频道信息: {input_str}")
                return None

            channel_data = {
                'channel_name': channel['snippet']['title'],
                'description': channel['snippet']['description'],
                'subscriber_count': channel['statistics'].get('subscriberCount', 'N/A'),
                'view_count': channel['statistics'].get('viewCount', 'N/A'),
                'video_count': channel['statistics'].get('videoCount', 'N/A'),  # 添加总视频数
                'created_date': channel['snippet']['publishedAt'],
                'country': channel['snippet'].get('country', 'Not specified'),
                'channel_id': channel['id']
            }

            self.log_message(f"成功获取频道信息: {channel_data['channel_name']}")
            self.log_message(f"频道总视频数: {channel_data['video_count']}")  # 添加日志输出
            return channel_data

        except Exception as e:
            self.log_message(f"获取频道数据时出错: {str(e)}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def get_videos_details(self, video_ids):
        """获取视频详细信息"""
        try:
            # 每次最多请求50个视频的详情
            results = []
            for i in range(0, len(video_ids), 50):
                batch = video_ids[i:i + 50]
                request = self.youtube.videos().list(
                    part="snippet,statistics",  # statistics 部分包含了点赞数和评论数
                    id=','.join(batch)
                )
                response = request.execute()
                results.extend(response['items'])
                self.log_message(f"成功获取一批 {len(batch)} 个视频的详情")

            return results
        except Exception as e:
            self.log_message(f"获取视频详情时出错: {str(e)}")
            raise

    def get_channel_videos(self, channel_id):
        """获取频道的所有符合条件的视频"""
        videos = []
        next_page_token = None
        total_videos_found = 0
        total_videos_filtered = 0
        page_count = 0

        try:
            while True:  # 移除页数限制，持续获取直到没有更多视频
                try:
                    self.log_message(f"正在获取频道 {channel_id} 的视频列表... (第 {page_count + 1} 页)")
                    request = self.youtube.search().list(
                        part="id",
                        channelId=channel_id,
                        maxResults=50,  # YouTube API 的最大限制
                        pageToken=next_page_token,
                        type="video",
                        order="date"  # 按日期排序，确保获取所有视频
                    )
                    response = request.execute()

                    if not response.get('items'):
                        self.log_message("没有找到更多视频")
                        break

                    video_ids = [item['id']['videoId'] for item in response['items']]
                    total_videos_found += len(video_ids)
                    self.log_message(f"本页找到 {len(video_ids)} 个视频")

                    # 获取视频详情
                    try:
                        video_details = self.get_videos_details(video_ids)
                        self.log_message(f"成功获取 {len(video_details)} 个视频的详细信息")

                        # 筛选观看数大于阈值的视频
                        filtered_videos = []
                        for video in video_details:
                            try:
                                view_count = int(video['statistics'].get('viewCount', 0))
                                self.log_message(f"视频 {video['id']} 的观看数为: {view_count}")
                                if view_count >= self.view_threshold:
                                    filtered_videos.append(video)
                                    self.log_message(
                                        f"视频 {video['id']} 观看数 {view_count} 符合条件（大于等于 {self.view_threshold}）")
                                else:
                                    self.log_message(
                                        f"视频 {video['id']} 观看数 {view_count} 不符合条件（小于 {self.view_threshold}）")
                            except ValueError:
                                self.log_message(f"视频 {video['id']} 的观看数无效")
                                continue

                        total_videos_filtered += len(filtered_videos)
                        self.log_message(f"本页筛选出 {len(filtered_videos)} 个符合条件的视频")
                        videos.extend(filtered_videos)

                    except Exception as e:
                        self.log_message(f"获取视频详情时出错: {str(e)}")
                        if "quotaExceeded" in str(e):
                            raise
                        continue

                    next_page_token = response.get('nextPageToken')
                    if not next_page_token:
                        self.log_message("没有更多页面，视频获取完成")
                        break

                    page_count += 1
                    self.log_message(f"准备获取下一页数据 (当前第 {page_count} 页)")

                except Exception as e:
                    self.log_message(f"获取频道视频列表时出错: {str(e)}")
                    if "quotaExceeded" in str(e):
                        raise
                    continue

            self.log_message(f"\n频道视频获取统计:")
            self.log_message(f"- 总共找到的视频数: {total_videos_found}")
            self.log_message(f"- 符合观看数阈值({self.view_threshold})的视频数: {total_videos_filtered}")
            self.log_message(f"- 最终收集到的视频数: {len(videos)}")
            self.log_message(f"- 处理的页数: {page_count}")

            return videos

        except Exception as e:
            self.log_message(f"获取频道视频时出错: {str(e)}")
            raise

    def save_videos_to_excel(self, channel_id, videos, original_url):
        """将视频数据保存到Excel"""
        try:
            video_data = []
            processed_video_ids = set()

            # 从URL中提取用户名
            username = None
            if '/@' in original_url:
                username = original_url.split('/@')[1].split('/')[0].strip()

            for video in videos:
                video_id = video['id']
                if video_id in processed_video_ids:
                    self.log_message(f"跳过重复视频ID: {video_id}")
                    continue

                processed_video_ids.add(video_id)
                video_data.append({
                    'title': video['snippet']['title'],
                    'description': video['snippet']['description'],
                    'published_at': video['snippet']['publishedAt'],
                    'view_count': video['statistics'].get('viewCount', 'N/A'),
                    'like_count': video['statistics'].get('likeCount', 'N/A'),
                    'comment_count': video['statistics'].get('commentCount', 'N/A'),
                    'tags': ','.join(video['snippet'].get('tags', [])),
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'video_id': video_id
                })

            if video_data:
                # 转换为DataFrame
                df = pd.DataFrame(video_data)

                # 记录原始数据
                original_count = len(df)
                self.log_message(f"原始数据数量: {original_count}")

                # 只基于video_id去重
                df = df.drop_duplicates(subset=['video_id'], keep='first')

                # 记录清洗后的数据
                cleaned_count = len(df)
                self.log_message(f"清洗后数据数量: {cleaned_count}")

                if original_count > cleaned_count:
                    self.log_message(f"清除了 {original_count - cleaned_count} 条重复数据")
                    duplicate_ids = df['video_id'].value_counts()[df['video_id'].value_counts() > 1].index
                    if len(duplicate_ids) > 0:
                        self.log_message(f"重复的视频ID: {list(duplicate_ids)}")

                # 删除video_id列
                df = df.drop('video_id', axis=1)

                # 使用用户名作为文件名，如果无法获取用户名则使用频道ID
                if username:
                    filename = f"{username}_videos.xlsx"
                else:
                    filename = f"{channel_id}_videos.xlsx"

                output_path = os.path.join(self.video_save_path, filename)
                df.to_excel(output_path, index=False)
                self.log_message(f"视频数据已保存到: {output_path}")

            else:
                self.log_message("没有数据需要保存")

        except Exception as e:
            self.log_message(f"保存视频数据时出错: {str(e)}")
            raise

    def process_excel_file(self, excel_path):
        """处理Excel文件"""
        try:
            # 读取Excel文件，确保不跳过任何行
            try:
                df = pd.read_excel(excel_path, dtype=str)
                df = df.dropna(how='all')
                df = df.reset_index(drop=True)

                self.log_message(f"成功读取Excel文件，共有 {len(df)} 个频道待处理")
                self.log_message(f"读取到的URL列表：{df.iloc[:, 0].tolist()}")
            except Exception as e:
                self.log_message(f"读取Excel文件失败: {str(e)}")
                return

            if df.empty:
                self.log_message("Excel文件为空")
                return

            # 确保所需的列存在
            required_columns = ['channel_name', 'description', 'subscriber_count',
                                'view_count', 'video_count', 'created_date', 'country']  # 添加 video_count
            for col in required_columns:
                if col not in df.columns:
                    df[col] = ''

            channel_urls = df.iloc[:, 0].astype(str).tolist()
            success_count = 0

            for idx, url in enumerate(channel_urls):
                if pd.isna(url) or url.strip() == '':
                    self.log_message(f"第 {idx + 1} 行的URL为空，已跳过")
                    continue

                try:
                    self.log_message(f"正在处理第 {idx + 1}/{len(channel_urls)} 个频道: {url}")

                    # 使用新的get_channel_data方法
                    channel_data = self.get_channel_data(url)
                    if channel_data:
                        for col, value in channel_data.items():
                            if col != 'channel_id':
                                df.loc[idx, col] = value

                        self.log_message(f"开始获取频道 {url} 的视频数据...")
                        videos = self.get_channel_videos(channel_data['channel_id'])
                        if videos:
                            self.save_videos_to_excel(channel_data['channel_id'], videos, url)
                            self.log_message(f"成功保存频道 {url} 的视频数据，共 {len(videos)} 个视频")
                            # 添加统计信息
                            self.log_message(f"频道统计信息:")
                            self.log_message(f"- 总视频数: {channel_data['video_count']}")
                            self.log_message(f"- 符合观看量阈值的视频数: {len(videos)}")
                        else:
                            self.log_message(f"频道 {url} 没有符合条件的视频（观看数 >= {self.view_threshold}）")

                        success_count += 1
                    else:
                        self.log_message(f"无法获取频道数据: {url}")

                except Exception as e:
                    self.log_message(f"处理频道 {url} 时出错: {str(e)}")
                    continue

            self.log_message(f"总共处理了 {len(channel_urls)} 个频道，成功 {success_count} 个")

            # 保存更新后的Excel文件
            try:
                base_path = os.path.splitext(excel_path)[0]
                current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_excel_path = f"{base_path}_updated_{current_time}.xlsx"

                df.to_excel(new_excel_path, index=False)
                self.log_message(f"数据已保存到新文件: {new_excel_path}")

            except Exception as e:
                self.log_message(f"保存Excel文件时出错: {str(e)}")
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                backup_file = os.path.join(desktop_path, f"youtube_data_backup_{current_time}.xlsx")
                try:
                    df.to_excel(backup_file, index=False)
                    self.log_message(f"数据已保存到备份文件: {backup_file}")
                except Exception as e2:
                    self.log_message(f"保存备份文件也失败: {str(e2)}")
                    raise

        except Exception as e:
            self.log_message(f"处理Excel文件时出错: {str(e)}")
            raise

    def run(self, excel_path):
        """运行主程序"""
        try:
            self.log_message("开始处理数据...")
            self.process_excel_file(excel_path)
            self.log_message("数据处理完成！")
        except Exception as e:
            self.log_message(f"程序运行出错: {str(e)}")
            raise
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
import os
import logging
from datetime import datetime
import pandas as pd
from googleapiclient.discovery import build
from tenacity import retry, stop_after_attempt, wait_exponential

class YouTubeDataCollector:
    def __init__(self, api_key, view_threshold=1000000, proxy=None, save_path=None, logger_callback=None):
        """
        初始化收集器
        :param api_key: YouTube API密钥
        :param view_threshold: 视频观看量阈值
        :param proxy: 代理设置
        :param save_path: 数据保存路径
        :param logger_callback: 日志回调函数
        """
        # 配置代理
        if proxy:
            os.environ['HTTP_PROXY'] = proxy
            os.environ['HTTPS_PROXY'] = proxy

        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.logger_callback = logger_callback
        self.view_threshold = view_threshold  # 设置观看量阈值

        # 验证并设置保存路径
        if not save_path:
            raise ValueError("必须指定保存路径")
        self.video_save_path = save_path

        # 设置日志路径为保存路径下的 logs 文件夹
        self.log_path = os.path.join(self.video_save_path, "logs")

        # 配置日志
        self.setup_logging()

    def setup_logging(self):
        """设置日志"""
        # 创建日志目录
        os.makedirs(self.log_path, exist_ok=True)
        log_file = os.path.join(self.log_path, f'youtube_collector_{datetime.now().strftime("%Y%m%d")}.log')

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def log_message(self, message):
        """统一的日志记录函数"""
        self.logger.info(message)
        if self.logger_callback:
            self.logger_callback(message)

    def extract_channel_info(self, input_str):
        """
        从多种输入格式中提取频道信息
        支持的格式：
        1\. 频道ID (UC...)
        2\. 频道URL (https://www.youtube.com/@...)
        3\. 频道用户名 (@...)
        """
        try:
            self.log_message(f"正在处理输入: {input_str}")

            # 1\. 检查是否是频道ID (UC开头)
            if input_str.startswith('UC'):
                self.log_message("检测到频道ID格式")
                return self.get_channel_by_id(input_str)

            # 2\. 检查是否是频道URL或用户名
            if '/@' in input_str or input_str.startswith('@'):
                self.log_message("检测到频道用户名格式")
                username = input_str.split('/@')[-1].split('/')[0].strip() if '/@' in input_str else input_str.strip()
                return self.get_channel_by_username(username)

            self.log_message(f"无法识别的输入格式: {input_str}")
            return None

        except Exception as e:
            self.log_message(f"提取频道信息时出错: {str(e)}")
            return None

    def get_channel_by_id(self, channel_id):
        """直接通过频道ID获取信息"""
        try:
            request = self.youtube.channels().list(
                part="snippet,statistics,brandingSettings",
                id=channel_id
            )
            response = request.execute()

            if response.get('items'):
                channel = response['items'][0]
                self.log_message(f"成功获取频道信息: {channel['snippet']['title']}")
                return channel
            else:
                self.log_message(f"未找到频道ID: {channel_id}")
                return None

        except Exception as e:
            self.log_message(f"获取频道信息时出错: {str(e)}")
            return None

    def get_channel_by_username(self, username):
        """通过用户名获取频道信息"""
        try:
            # 移除@符号（如果存在）
            clean_username = username.lstrip('@')
            self.log_message(f"正在获取频道信息，用户名: {clean_username}")

            # 使用搜索方法查找频道
            try:
                request = self.youtube.search().list(
                    part="snippet",
                    q=clean_username,
                    type="channel",
                    maxResults=5
                )
                response = request.execute()

                if response.get('items'):
                    # 获取第一个搜索结果的频道ID
                    channel_id = response['items'][0]['id']['channelId']

                    # 使用频道ID获取完整信息
                    channel_request = self.youtube.channels().list(
                        part="snippet,statistics,brandingSettings",
                        id=channel_id
                    )
                    channel_response = channel_request.execute()

                    if channel_response.get('items'):
                        channel = channel_response['items'][0]
                        self.log_message(f"成功找到频道: {channel['snippet']['title']}")
                        return channel

            except Exception as e:
                self.log_message(f"搜索频道时出错: {str(e)}")

            return None

        except Exception as e:
            self.log_message(f"获取频道信息时出错: {str(e)}")
            return None

    def get_channel_data(self, input_str):
        """获取频道数据的主方法"""
        try:
            channel = self.extract_channel_info(input_str)
            if not channel:
                self.log_message(f"无法获取频道信息: {input_str}")
                return None

            channel_data = {
                'channel_name': channel['snippet']['title'],
                'description': channel['snippet']['description'],
                'subscriber_count': channel['statistics'].get('subscriberCount', 'N/A'),
                'view_count': channel['statistics'].get('viewCount', 'N/A'),
                'video_count': channel['statistics'].get('videoCount', 'N/A'),  # 添加总视频数
                'created_date': channel['snippet']['publishedAt'],
                'country': channel['snippet'].get('country', 'Not specified'),
                'channel_id': channel['id']
            }

            self.log_message(f"成功获取频道信息: {channel_data['channel_name']}")
            self.log_message(f"频道总视频数: {channel_data['video_count']}")  # 添加日志输出
            return channel_data

        except Exception as e:
            self.log_message(f"获取频道数据时出错: {str(e)}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def get_videos_details(self, video_ids):
        """获取视频详细信息"""
        try:
            # 每次最多请求50个视频的详情
            results = []
            for i in range(0, len(video_ids), 50):
                batch = video_ids[i:i + 50]
                request = self.youtube.videos().list(
                    part="snippet,statistics",  # statistics 部分包含了点赞数和评论数
                    id=','.join(batch)
                )
                response = request.execute()
                results.extend(response['items'])
                self.log_message(f"成功获取一批 {len(batch)} 个视频的详情")

            return results
        except Exception as e:
            self.log_message(f"获取视频详情时出错: {str(e)}")
            raise

    def get_channel_videos(self, channel_id):
        """获取频道的所有符合条件的视频"""
        videos = []
        next_page_token = None
        total_videos_found = 0
        total_videos_filtered = 0
        page_count = 0

        try:
            while True:  # 移除页数限制，持续获取直到没有更多视频
                try:
                    self.log_message(f"正在获取频道 {channel_id} 的视频列表... (第 {page_count + 1} 页)")
                    request = self.youtube.search().list(
                        part="id",
                        channelId=channel_id,
                        maxResults=50,  # YouTube API 的最大限制
                        pageToken=next_page_token,
                        type="video",
                        order="date"  # 按日期排序，确保获取所有视频
                    )
                    response = request.execute()

                    if not response.get('items'):
                        self.log_message("没有找到更多视频")
                        break

                    video_ids = [item['id']['videoId'] for item in response['items']]
                    total_videos_found += len(video_ids)
                    self.log_message(f"本页找到 {len(video_ids)} 个视频")

                    # 获取视频详情
                    try:
                        video_details = self.get_videos_details(video_ids)
                        self.log_message(f"成功获取 {len(video_details)} 个视频的详细信息")

                        # 筛选观看数大于阈值的视频
                        filtered_videos = []
                        for video in video_details:
                            try:
                                view_count = int(video['statistics'].get('viewCount', 0))
                                self.log_message(f"视频 {video['id']} 的观看数为: {view_count}")
                                if view_count >= self.view_threshold:
                                    filtered_videos.append(video)
                                    self.log_message(
                                        f"视频 {video['id']} 观看数 {view_count} 符合条件（大于等于 {self.view_threshold}）")
                                else:
                                    self.log_message(
                                        f"视频 {video['id']} 观看数 {view_count} 不符合条件（小于 {self.view_threshold}）")
                            except ValueError:
                                self.log_message(f"视频 {video['id']} 的观看数无效")
                                continue

                        total_videos_filtered += len(filtered_videos)
                        self.log_message(f"本页筛选出 {len(filtered_videos)} 个符合条件的视频")
                        videos.extend(filtered_videos)

                    except Exception as e:
                        self.log_message(f"获取视频详情时出错: {str(e)}")
                        if "quotaExceeded" in str(e):
                            raise
                        continue

                    next_page_token = response.get('nextPageToken')
                    if not next_page_token:
                        self.log_message("没有更多页面，视频获取完成")
                        break

                    page_count += 1
                    self.log_message(f"准备获取下一页数据 (当前第 {page_count} 页)")

                except Exception as e:
                    self.log_message(f"获取频道视频列表时出错: {str(e)}")
                    if "quotaExceeded" in str(e):
                        raise
                    continue

            self.log_message(f"\n频道视频获取统计:")
            self.log_message(f"- 总共找到的视频数: {total_videos_found}")
            self.log_message(f"- 符合观看数阈值({self.view_threshold})的视频数: {total_videos_filtered}")
            self.log_message(f"- 最终收集到的视频数: {len(videos)}")
            self.log_message(f"- 处理的页数: {page_count}")

            return videos

        except Exception as e:
            self.log_message(f"获取频道视频时出错: {str(e)}")
            raise

    def save_videos_to_excel(self, channel_id, videos, original_url):
        """将视频数据保存到Excel"""
        try:
            video_data = []
            processed_video_ids = set()

            # 从URL中提取用户名
            username = None
            if '/@' in original_url:
                username = original_url.split('/@')[1].split('/')[0].strip()

            for video in videos:
                video_id = video['id']
                if video_id in processed_video_ids:
                    self.log_message(f"跳过重复视频ID: {video_id}")
                    continue

                processed_video_ids.add(video_id)
                video_data.append({
                    'title': video['snippet']['title'],
                    'description': video['snippet']['description'],
                    'published_at': video['snippet']['publishedAt'],
                    'view_count': video['statistics'].get('viewCount', 'N/A'),
                    'like_count': video['statistics'].get('likeCount', 'N/A'),
                    'comment_count': video['statistics'].get('commentCount', 'N/A'),
                    'tags': ','.join(video['snippet'].get('tags', [])),
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'video_id': video_id
                })

            if video_data:
                # 转换为DataFrame
                df = pd.DataFrame(video_data)

                # 记录原始数据
                original_count = len(df)
                self.log_message(f"原始数据数量: {original_count}")

                # 只基于video_id去重
                df = df.drop_duplicates(subset=['video_id'], keep='first')

                # 记录清洗后的数据
                cleaned_count = len(df)
                self.log_message(f"清洗后数据数量: {cleaned_count}")

                if original_count > cleaned_count:
                    self.log_message(f"清除了 {original_count - cleaned_count} 条重复数据")
                    duplicate_ids = df['video_id'].value_counts()[df['video_id'].value_counts() > 1].index
                    if len(duplicate_ids) > 0:
                        self.log_message(f"重复的视频ID: {list(duplicate_ids)}")

                # 删除video_id列
                df = df.drop('video_id', axis=1)

                # 使用用户名作为文件名，如果无法获取用户名则使用频道ID
                if username:
                    filename = f"{username}_videos.xlsx"
                else:
                    filename = f"{channel_id}_videos.xlsx"

                output_path = os.path.join(self.video_save_path, filename)
                df.to_excel(output_path, index=False)
                self.log_message(f"视频数据已保存到: {output_path}")

            else:
                self.log_message("没有数据需要保存")

        except Exception as e:
            self.log_message(f"保存视频数据时出错: {str(e)}")
            raise

    def process_excel_file(self, excel_path):
        """处理Excel文件"""
        try:
            # 读取Excel文件，确保不跳过任何行
            try:
                df = pd.read_excel(excel_path, dtype=str)
                df = df.dropna(how='all')
                df = df.reset_index(drop=True)

                self.log_message(f"成功读取Excel文件，共有 {len(df)} 个频道待处理")
                self.log_message(f"读取到的URL列表：{df.iloc[:, 0].tolist()}")
            except Exception as e:
                self.log_message(f"读取Excel文件失败: {str(e)}")
                return

            if df.empty:
                self.log_message("Excel文件为空")
                return

            # 确保所需的列存在
            required_columns = ['channel_name', 'description', 'subscriber_count',
                                'view_count', 'video_count', 'created_date', 'country']  # 添加 video_count
            for col in required_columns:
                if col not in df.columns:
                    df[col] = ''

            channel_urls = df.iloc[:, 0].astype(str).tolist()
            success_count = 0

            for idx, url in enumerate(channel_urls):
                if pd.isna(url) or url.strip() == '':
                    self.log_message(f"第 {idx + 1} 行的URL为空，已跳过")
                    continue

                try:
                    self.log_message(f"正在处理第 {idx + 1}/{len(channel_urls)} 个频道: {url}")

                    # 使用新的get_channel_data方法
                    channel_data = self.get_channel_data(url)
                    if channel_data:
                        for col, value in channel_data.items():
                            if col != 'channel_id':
                                df.loc[idx, col] = value

                        self.log_message(f"开始获取频道 {url} 的视频数据...")
                        videos = self.get_channel_videos(channel_data['channel_id'])
                        if videos:
                            self.save_videos_to_excel(channel_data['channel_id'], videos, url)
                            self.log_message(f"成功保存频道 {url} 的视频数据，共 {len(videos)} 个视频")
                            # 添加统计信息
                            self.log_message(f"频道统计信息:")
                            self.log_message(f"- 总视频数: {channel_data['video_count']}")
                            self.log_message(f"- 符合观看量阈值的视频数: {len(videos)}")
                        else:
                            self.log_message(f"频道 {url} 没有符合条件的视频（观看数 >= {self.view_threshold}）")

                        success_count += 1
                    else:
                        self.log_message(f"无法获取频道数据: {url}")

                except Exception as e:
                    self.log_message(f"处理频道 {url} 时出错: {str(e)}")
                    continue

            self.log_message(f"总共处理了 {len(channel_urls)} 个频道，成功 {success_count} 个")

            # 保存更新后的Excel文件
            try:
                base_path = os.path.splitext(excel_path)[0]
                current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_excel_path = f"{base_path}_updated_{current_time}.xlsx"

                df.to_excel(new_excel_path, index=False)
                self.log_message(f"数据已保存到新文件: {new_excel_path}")

            except Exception as e:
                self.log_message(f"保存Excel文件时出错: {str(e)}")
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                backup_file = os.path.join(desktop_path, f"youtube_data_backup_{current_time}.xlsx")
                try:
                    df.to_excel(backup_file, index=False)
                    self.log_message(f"数据已保存到备份文件: {backup_file}")
                except Exception as e2:
                    self.log_message(f"保存备份文件也失败: {str(e2)}")
                    raise

        except Exception as e:
            self.log_message(f"处理Excel文件时出错: {str(e)}")
            raise

    def run(self, excel_path):
        """运行主程序"""
        try:
            self.log_message("开始处理数据...")
            self.process_excel_file(excel_path)
            self.log_message("数据处理完成！")
        except Exception as e:
            self.log_message(f"程序运行出错: {str(e)}")
            raise
```。

接下来要做的，就是接住它，然后，把故事讲下去。

在数字产品世界里，UI常被简称为“界面”，但它远不止是几块屏幕和几个按钮那么简单。用户界面，是人与机器之间的一座桥梁，每一次点击、滑动、长按，其实都是在与UI对话。好的UI不会刻意刷存在感，而是让你在不知不觉中完成所有操作，甚至忘记设计的存在。它藏在排版里、色彩中、动效背后，用润物无声的方式，传递着产品对使用者的理解与体贴。可以说，UI既是一门技术，也是一份用心。

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
class YouTubeCollectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube数据采集器")
        self.root.geometry("700x650")

        # 配置文件路径
        self.config_file = 'collector_config.json'
        # 加载配置
        self.load_config()

        # 创建消息队列用于更新进度
        self.message_queue = queue.Queue()

        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # API Key 输入、保存和清空按钮
        ttk.Label(self.main_frame, text="YouTube API Key:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.api_key_var = tk.StringVar(value=self.saved_api_key)
        self.api_key_entry = ttk.Entry(self.main_frame, textvariable=self.api_key_var, width=50)
        self.api_key_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        # 创建一个框架来容纳API Key的按钮
        api_key_buttons_frame = ttk.Frame(self.main_frame)
        api_key_buttons_frame.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)

        self.save_api_key_button = ttk.Button(api_key_buttons_frame, text="保存", command=self.save_api_key)
        self.save_api_key_button.pack(side=tk.LEFT, padx=(0, 5))

        self.clear_api_key_button = ttk.Button(api_key_buttons_frame, text="清空", command=self.clear_api_key)
        self.clear_api_key_button.pack(side=tk.LEFT)

        # 代理设置、保存和清空按钮
        ttk.Label(self.main_frame, text="代理地址:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.proxy_var = tk.StringVar(value=self.saved_proxy)
        self.proxy_entry = ttk.Entry(self.main_frame, textvariable=self.proxy_var, width=50)
        self.proxy_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        # 创建一个框架来容纳代理地址的按钮
        proxy_buttons_frame = ttk.Frame(self.main_frame)
        proxy_buttons_frame.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

        self.save_proxy_button = ttk.Button(proxy_buttons_frame, text="保存", command=self.save_proxy)
        self.save_proxy_button.pack(side=tk.LEFT, padx=(0, 5))

        self.clear_proxy_button = ttk.Button(proxy_buttons_frame, text="清空", command=self.clear_proxy)
        self.clear_proxy_button.pack(side=tk.LEFT)

        # 观看量阈值设置 (修改这部分)
        ttk.Label(self.main_frame, text="收集观看量大于").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.threshold_var = tk.StringVar()  # 不设置默认值
        self.threshold_entry = ttk.Entry(self.main_frame, textvariable=self.threshold_var, width=15)
        self.threshold_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        ttk.Label(self.main_frame, text="的视频信息").grid(row=2, column=1, sticky=tk.W, padx=(120,0), pady=5)

        # Excel文件选择
        ttk.Label(self.main_frame, text="选择提供频道的Excel文件:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.excel_path_var = tk.StringVar()
        self.excel_path_entry = ttk.Entry(self.main_frame, textvariable=self.excel_path_var, width=40)
        self.excel_path_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        self.browse_button = ttk.Button(self.main_frame, text="浏览", command=self.browse_excel_file)
        self.browse_button.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)

        # 视频数据保存路径选择
        ttk.Label(self.main_frame, text="保存路径:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.save_path_var = tk.StringVar()
        self.save_path_entry = ttk.Entry(self.main_frame, textvariable=self.save_path_var, width=40)
        self.save_path_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        self.save_path_button = ttk.Button(self.main_frame, text="选择", command=self.browse_save_path)
        self.save_path_button.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

        # 进度显示文本框
        self.progress_text = tk.Text(self.main_frame, height=15, width=60)
        self.progress_text.grid(row=5, column=0, columnspan=3, pady=10)

        # 滚动条
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.progress_text.yview)
        scrollbar.grid(row=5, column=3, sticky=(tk.N, tk.S))
        self.progress_text['yscrollcommand'] = scrollbar.set

        # 进度条
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.main_frame, length=400, mode='determinate',
                                            variable=self.progress_var)
        self.progress_bar.grid(row=6, column=0, columnspan=3, pady=10)

        # 开始按钮
        self.start_button = ttk.Button(self.main_frame, text="开始采集", command=self.start_collection)
        self.start_button.grid(row=7, column=0, columnspan=3, pady=10)

        # 定期检查消息队列
        self.check_message_queue()

    def load_config(self):
        """加载配置文件"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.saved_api_key = config.get('api_key', '')
                    self.saved_proxy = config.get('proxy', '')  # 默认为空字符串
            else:
                self.saved_api_key = ''
                self.saved_proxy = ''  # 默认为空字符串
        except Exception as e:
            self.saved_api_key = ''
            self.saved_proxy = ''  # 默认为空字符串

    def clear_api_key(self):
        """清空API Key"""
        try:
            config = self.load_current_config()
            if 'api_key' in config:
                del config['api_key']
            self.save_config(config)
            self.api_key_var.set('')  # 清空输入框
            self.saved_api_key = ''  # 清空保存的值
            messagebox.showinfo("成功", "API Key已清空")
        except Exception as e:
            messagebox.showerror("错误", f"清空API Key失败: {str(e)}")

    def clear_proxy(self):
        """清空代理地址"""
        try:
            config = self.load_current_config()
            if 'proxy' in config:
                del config['proxy']
            self.save_config(config)
            self.proxy_var.set('')  # 清空输入框
            self.saved_proxy = ''  # 清空保存的值
            messagebox.showinfo("成功", "代理地址已清空")
        except Exception as e:
            messagebox.showerror("错误", f"清空代理地址失败: {str(e)}")

    def save_api_key(self):
        """保存API Key到配置文件"""
        api_key = self.api_key_var.get().strip()
        if not api_key:
            messagebox.showerror("错误", "API Key不能为空")
            return

        config = self.load_current_config()
        config['api_key'] = api_key
        self.save_config(config)
        self.saved_api_key = api_key  # 更新保存的值
        messagebox.showinfo("成功", "API Key已保存")

    def save_proxy(self):
        """保存代理地址到配置文件"""
        proxy = self.proxy_var.get().strip()
        if not proxy:
            messagebox.showerror("错误", "代理地址不能为空")
            return

        config = self.load_current_config()
        config['proxy'] = proxy
        self.save_config(config)
        self.saved_proxy = proxy  # 更新保存的值
        messagebox.showinfo("成功", "代理地址已保存")

    def load_current_config(self):
        """加载当前配置"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}

    def save_config(self, config):
        """保存配置到文件"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f)
        except Exception as e:
            messagebox.showerror("错误", f"保存配置文件失败: {str(e)}")

    def browse_excel_file(self):
        """选择Excel文件"""
        filename = filedialog.askopenfilename(
            title="选择Excel文件",
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if filename:
            self.excel_path_var.set(filename)

    def browse_save_path(self):
        """选择保存路径"""
        dirname = filedialog.askdirectory(title="选择保存路径")
        if dirname:
            self.save_path_var.set(dirname)

    def update_progress(self, message):
        """更新进度显示"""
        self.progress_text.insert(tk.END, message + "\n")
        self.progress_text.see(tk.END)

    def check_message_queue(self):
        """检查消息队列并更新UI"""
        try:
            while True:
                message = self.message_queue.get_nowait()
                self.update_progress(message)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_message_queue)

    def custom_logger(self, message):
        """自定义日志处理函数"""
        self.message_queue.put(message)

    def validate_threshold(self):
        """验证观看量阈值"""
        threshold = self.threshold_var.get().strip()
        if not threshold:
            messagebox.showerror("错误", "请输入观看量阈值")
            return False
        if not threshold.isdigit():
            messagebox.showerror("错误", "观看量阈值必须为数字")
            return False
        return True

    def start_collection(self):
        """开始数据采集"""
        # 验证输入
        if not self.api_key_var.get().strip():
            messagebox.showerror("错误", "请输入YouTube API Key")
            return
        if not self.excel_path_var.get().strip():
            messagebox.showerror("错误", "请选择Excel文件")
            return
        if not os.path.exists(self.excel_path_var.get()):
            messagebox.showerror("错误", "Excel文件不存在")
            return
        if not self.save_path_var.get().strip():
            messagebox.showerror("错误", "请选择保存路径")
            return
        if not self.validate_threshold():
            return

        save_path = self.save_path_var.get().strip()
        if not os.path.exists(save_path):
            try:
                os.makedirs(save_path)
            except Exception as e:
                messagebox.showerror("错误", f"无法创建保存路径: {str(e)}")
                return

        # 禁用按钮和输入框
        self.start_button.state(['disabled'])
        self.api_key_entry.state(['disabled'])
        self.proxy_entry.state(['disabled'])
        self.excel_path_entry.state(['disabled'])
        self.save_path_entry.state(['disabled'])
        self.browse_button.state(['disabled'])
        self.save_path_button.state(['disabled'])

        # 清空进度显示
        self.progress_text.delete(1.0, tk.END)
        self.progress_var.set(0)

        # 创建并启动采集线程
        thread = threading.Thread(target=self.run_collection)
        thread.daemon = True
        thread.start()

    def run_collection(self):
        """运行采集程序"""
        try:
            # 创建采集器实例，确保正确传入观看量阈值
            collector = YouTubeDataCollector(
                api_key=self.api_key_var.get().strip(),
                view_threshold=int(self.threshold_var.get().strip()),  # 确保正确传入阈值
                proxy=self.proxy_var.get().strip(),
                save_path=self.save_path_var.get().strip(),
                logger_callback=self.custom_logger
            )

            # 运行采集
            collector.run(self.excel_path_var.get())

            # 完成后的处理
            self.message_queue.put("采集完成！")
            self.root.after(0, self.collection_completed)

        except Exception as e:
            error_message = str(e)
            if "配额已用完" in error_message or "quotaExceeded" in error_message:
                detailed_message = (
                    "YouTube API 配额已用完！\n\n"
                    "解决方法：\n"
                    "1\. 等待24小时后再试\n"
                    "2\. 使用新的 API Key\n"
                    "3\. 增加项目的配额限制\n\n"
                    "建议：每个 API Key 每天可以处理约 100 个频道的数据"
                )
                self.message_queue.put(f"错误: {detailed_message}")
                self.root.after(0, lambda: messagebox.showerror("API 配额超限", detailed_message))
            else:
                self.message_queue.put(f"错误: {error_message}")
            self.root.after(0, lambda: self.collection_error(error_message))

    def collection_error(self, error_message):
        """采集出错后的处理"""
        if "配额已用完" not in error_message and "quotaExceeded" not in error_message:
            messagebox.showerror("错误", error_message)
        self.enable_inputs()

    def collection_completed(self):
        """采集完成后的处理"""
        messagebox.showinfo("完成", "数据采集已完成！")
        self.enable_inputs()

    def collection_error(self, error_message):
        """采集出错后的处理"""
        messagebox.showerror("错误", error_message)
        self.enable_inputs()

    def enable_inputs(self):
        """启用所有输入控件"""
        self.start_button.state(['!disabled'])
        self.api_key_entry.state(['!disabled'])
        self.proxy_entry.state(['!disabled'])
        self.excel_path_entry.state(['!disabled'])
        self.save_path_entry.state(['!disabled'])
        self.browse_button.state(['!disabled'])
        self.save_path_button.state(['!disabled'])

def main():
    root = tk.Tk()
    app = YouTubeCollectorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
class YouTubeCollectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube数据采集器")
        self.root.geometry("700x650")

        # 配置文件路径
        self.config_file = 'collector_config.json'
        # 加载配置
        self.load_config()

        # 创建消息队列用于更新进度
        self.message_queue = queue.Queue()

        # 创建主框架
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # API Key 输入、保存和清空按钮
        ttk.Label(self.main_frame, text="YouTube API Key:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.api_key_var = tk.StringVar(value=self.saved_api_key)
        self.api_key_entry = ttk.Entry(self.main_frame, textvariable=self.api_key_var, width=50)
        self.api_key_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        # 创建一个框架来容纳API Key的按钮
        api_key_buttons_frame = ttk.Frame(self.main_frame)
        api_key_buttons_frame.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)

        self.save_api_key_button = ttk.Button(api_key_buttons_frame, text="保存", command=self.save_api_key)
        self.save_api_key_button.pack(side=tk.LEFT, padx=(0, 5))

        self.clear_api_key_button = ttk.Button(api_key_buttons_frame, text="清空", command=self.clear_api_key)
        self.clear_api_key_button.pack(side=tk.LEFT)

        # 代理设置、保存和清空按钮
        ttk.Label(self.main_frame, text="代理地址:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.proxy_var = tk.StringVar(value=self.saved_proxy)
        self.proxy_entry = ttk.Entry(self.main_frame, textvariable=self.proxy_var, width=50)
        self.proxy_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        # 创建一个框架来容纳代理地址的按钮
        proxy_buttons_frame = ttk.Frame(self.main_frame)
        proxy_buttons_frame.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

        self.save_proxy_button = ttk.Button(proxy_buttons_frame, text="保存", command=self.save_proxy)
        self.save_proxy_button.pack(side=tk.LEFT, padx=(0, 5))

        self.clear_proxy_button = ttk.Button(proxy_buttons_frame, text="清空", command=self.clear_proxy)
        self.clear_proxy_button.pack(side=tk.LEFT)

        # 观看量阈值设置 (修改这部分)
        ttk.Label(self.main_frame, text="收集观看量大于").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.threshold_var = tk.StringVar()  # 不设置默认值
        self.threshold_entry = ttk.Entry(self.main_frame, textvariable=self.threshold_var, width=15)
        self.threshold_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        ttk.Label(self.main_frame, text="的视频信息").grid(row=2, column=1, sticky=tk.W, padx=(120,0), pady=5)

        # Excel文件选择
        ttk.Label(self.main_frame, text="选择提供频道的Excel文件:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.excel_path_var = tk.StringVar()
        self.excel_path_entry = ttk.Entry(self.main_frame, textvariable=self.excel_path_var, width=40)
        self.excel_path_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        self.browse_button = ttk.Button(self.main_frame, text="浏览", command=self.browse_excel_file)
        self.browse_button.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)

        # 视频数据保存路径选择
        ttk.Label(self.main_frame, text="保存路径:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.save_path_var = tk.StringVar()
        self.save_path_entry = ttk.Entry(self.main_frame, textvariable=self.save_path_var, width=40)
        self.save_path_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        self.save_path_button = ttk.Button(self.main_frame, text="选择", command=self.browse_save_path)
        self.save_path_button.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

        # 进度显示文本框
        self.progress_text = tk.Text(self.main_frame, height=15, width=60)
        self.progress_text.grid(row=5, column=0, columnspan=3, pady=10)

        # 滚动条
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.progress_text.yview)
        scrollbar.grid(row=5, column=3, sticky=(tk.N, tk.S))
        self.progress_text['yscrollcommand'] = scrollbar.set

        # 进度条
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.main_frame, length=400, mode='determinate',
                                            variable=self.progress_var)
        self.progress_bar.grid(row=6, column=0, columnspan=3, pady=10)

        # 开始按钮
        self.start_button = ttk.Button(self.main_frame, text="开始采集", command=self.start_collection)
        self.start_button.grid(row=7, column=0, columnspan=3, pady=10)

        # 定期检查消息队列
        self.check_message_queue()

    def load_config(self):
        """加载配置文件"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.saved_api_key = config.get('api_key', '')
                    self.saved_proxy = config.get('proxy', '')  # 默认为空字符串
            else:
                self.saved_api_key = ''
                self.saved_proxy = ''  # 默认为空字符串
        except Exception as e:
            self.saved_api_key = ''
            self.saved_proxy = ''  # 默认为空字符串

    def clear_api_key(self):
        """清空API Key"""
        try:
            config = self.load_current_config()
            if 'api_key' in config:
                del config['api_key']
            self.save_config(config)
            self.api_key_var.set('')  # 清空输入框
            self.saved_api_key = ''  # 清空保存的值
            messagebox.showinfo("成功", "API Key已清空")
        except Exception as e:
            messagebox.showerror("错误", f"清空API Key失败: {str(e)}")

    def clear_proxy(self):
        """清空代理地址"""
        try:
            config = self.load_current_config()
            if 'proxy' in config:
                del config['proxy']
            self.save_config(config)
            self.proxy_var.set('')  # 清空输入框
            self.saved_proxy = ''  # 清空保存的值
            messagebox.showinfo("成功", "代理地址已清空")
        except Exception as e:
            messagebox.showerror("错误", f"清空代理地址失败: {str(e)}")

    def save_api_key(self):
        """保存API Key到配置文件"""
        api_key = self.api_key_var.get().strip()
        if not api_key:
            messagebox.showerror("错误", "API Key不能为空")
            return

        config = self.load_current_config()
        config['api_key'] = api_key
        self.save_config(config)
        self.saved_api_key = api_key  # 更新保存的值
        messagebox.showinfo("成功", "API Key已保存")

    def save_proxy(self):
        """保存代理地址到配置文件"""
        proxy = self.proxy_var.get().strip()
        if not proxy:
            messagebox.showerror("错误", "代理地址不能为空")
            return

        config = self.load_current_config()
        config['proxy'] = proxy
        self.save_config(config)
        self.saved_proxy = proxy  # 更新保存的值
        messagebox.showinfo("成功", "代理地址已保存")

    def load_current_config(self):
        """加载当前配置"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}

    def save_config(self, config):
        """保存配置到文件"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f)
        except Exception as e:
            messagebox.showerror("错误", f"保存配置文件失败: {str(e)}")

    def browse_excel_file(self):
        """选择Excel文件"""
        filename = filedialog.askopenfilename(
            title="选择Excel文件",
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if filename:
            self.excel_path_var.set(filename)

    def browse_save_path(self):
        """选择保存路径"""
        dirname = filedialog.askdirectory(title="选择保存路径")
        if dirname:
            self.save_path_var.set(dirname)

    def update_progress(self, message):
        """更新进度显示"""
        self.progress_text.insert(tk.END, message + "\n")
        self.progress_text.see(tk.END)

    def check_message_queue(self):
        """检查消息队列并更新UI"""
        try:
            while True:
                message = self.message_queue.get_nowait()
                self.update_progress(message)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_message_queue)

    def custom_logger(self, message):
        """自定义日志处理函数"""
        self.message_queue.put(message)

    def validate_threshold(self):
        """验证观看量阈值"""
        threshold = self.threshold_var.get().strip()
        if not threshold:
            messagebox.showerror("错误", "请输入观看量阈值")
            return False
        if not threshold.isdigit():
            messagebox.showerror("错误", "观看量阈值必须为数字")
            return False
        return True

    def start_collection(self):
        """开始数据采集"""
        # 验证输入
        if not self.api_key_var.get().strip():
            messagebox.showerror("错误", "请输入YouTube API Key")
            return
        if not self.excel_path_var.get().strip():
            messagebox.showerror("错误", "请选择Excel文件")
            return
        if not os.path.exists(self.excel_path_var.get()):
            messagebox.showerror("错误", "Excel文件不存在")
            return
        if not self.save_path_var.get().strip():
            messagebox.showerror("错误", "请选择保存路径")
            return
        if not self.validate_threshold():
            return

        save_path = self.save_path_var.get().strip()
        if not os.path.exists(save_path):
            try:
                os.makedirs(save_path)
            except Exception as e:
                messagebox.showerror("错误", f"无法创建保存路径: {str(e)}")
                return

        # 禁用按钮和输入框
        self.start_button.state(['disabled'])
        self.api_key_entry.state(['disabled'])
        self.proxy_entry.state(['disabled'])
        self.excel_path_entry.state(['disabled'])
        self.save_path_entry.state(['disabled'])
        self.browse_button.state(['disabled'])
        self.save_path_button.state(['disabled'])

        # 清空进度显示
        self.progress_text.delete(1.0, tk.END)
        self.progress_var.set(0)

        # 创建并启动采集线程
        thread = threading.Thread(target=self.run_collection)
        thread.daemon = True
        thread.start()

    def run_collection(self):
        """运行采集程序"""
        try:
            # 创建采集器实例，确保正确传入观看量阈值
            collector = YouTubeDataCollector(
                api_key=self.api_key_var.get().strip(),
                view_threshold=int(self.threshold_var.get().strip()),  # 确保正确传入阈值
                proxy=self.proxy_var.get().strip(),
                save_path=self.save_path_var.get().strip(),
                logger_callback=self.custom_logger
            )

            # 运行采集
            collector.run(self.excel_path_var.get())

            # 完成后的处理
            self.message_queue.put("采集完成！")
            self.root.after(0, self.collection_completed)

        except Exception as e:
            error_message = str(e)
            if "配额已用完" in error_message or "quotaExceeded" in error_message:
                detailed_message = (
                    "YouTube API 配额已用完！\n\n"
                    "解决方法：\n"
                    "1\. 等待24小时后再试\n"
                    "2\. 使用新的 API Key\n"
                    "3\. 增加项目的配额限制\n\n"
                    "建议：每个 API Key 每天可以处理约 100 个频道的数据"
                )
                self.message_queue.put(f"错误: {detailed_message}")
                self.root.after(0, lambda: messagebox.showerror("API 配额超限", detailed_message))
            else:
                self.message_queue.put(f"错误: {error_message}")
            self.root.after(0, lambda: self.collection_error(error_message))

    def collection_error(self, error_message):
        """采集出错后的处理"""
        if "配额已用完" not in error_message and "quotaExceeded" not in error_message:
            messagebox.showerror("错误", error_message)
        self.enable_inputs()

    def collection_completed(self):
        """采集完成后的处理"""
        messagebox.showinfo("完成", "数据采集已完成！")
        self.enable_inputs()

    def collection_error(self, error_message):
        """采集出错后的处理"""
        messagebox.showerror("错误", error_message)
        self.enable_inputs()

    def enable_inputs(self):
        """启用所有输入控件"""
        self.start_button.state(['!disabled'])
        self.api_key_entry.state(['!disabled'])
        self.proxy_entry.state(['!disabled'])
        self.excel_path_entry.state(['!disabled'])
        self.save_path_entry.state(['!disabled'])
        self.browse_button.state(['!disabled'])
        self.save_path_button.state(['!disabled'])

def main():
    root = tk.Tk()
    app = YouTubeCollectorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```。

接下来要做的，就是接住它，然后，把故事讲下去。

## Youtube批量视频下载器 全新升级版

### 它能做什么

下载器的主界面长这样：

![](img/2d1d02d6344551b2290199ec3a7ae1ab.png)

底层逻辑很简单：

基于Python的yt_dlp库实现本地批量拉取YouTube视频，量不限。唯一前提是先配好代理端口和cookies。

具体能力有这三点：

(1) 能读取Excel批量导入视频链接，自动循环下载
(2) 分辨率自由选，720p、1080p、1440p都可以
(3) 可限制下载条数，比如Excel里有5条链接，你可以只下前n条，程序会按从上到下的顺序执行

### 上手前的准备工作

#### 第一步，开启魔法上网

前面已提到，这里不再重复

#### 第二步，拿到代理端口

【点击跳转教程】

#### 【关键】第三步，准备cookies

① 先装一个取cookie的插件：

https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm

② 安装完成后，点击浏览器右上角拼图图标，把插件固定到工具栏里，Edge用户操作类似

![](img/ae13e12899f457723b6af6446ffb49c9.png)

![](img/cc055679b33120516f582faebdbac3fc.png)

![](img/e32f1bd092602aecf6049cea0168740d.png)

③ 打开YouTube官网：https://www.youtube.com/，先登录账号，再点开插件选择“This Site”

![](img/391a267c580e510fefeac2031174e9e5.png)

![](img/55f592c2337596963fcdf6ecc84371cc.png)

④ 在插件右下角点“Export”，格式选“Netscape”，cookie内容就会复制到剪贴板

![](img/ad2f1b1a93f783191f4d8f7579cb9dea.png)

![](img/2057da4af167e5afa2a365ec9ed6ac32.png)

⑤ 在桌面任意位置新建一个.txt文本，把复制的cookie粘进去，按Ctrl+S保存

![](img/1e157274acbfd6b5a451c648a3ca9bc5.png)

![](img/e13f61bba052623fb6b7350d87dff673.png)

⑥ 启动软件后，在“Cookies文件”处选中刚才保存的txt即可

![](img/153cec07f22c7a59709c7c61599e2bf9.png)

温馨提示：

cookie的有效期大约两周，到期前程序会自动提醒，需要你按同样流程重新导出一次并更换。

#### 【关键】第四步，准备好视频链接的Excel

链接的来源有三种：

① 用YouTube数据采集器导出，可直接衔接本工具批量下载
② 普通长视频链接获取方式
![](img/fe059b6d9eff38d81ec8155442d6fac9.png)

![](img/837172c07c262777c44b38b3d7e1a383.png)

![](img/f8742a117e01fcd2075eb98bda27427e.png)
③ Shorts短视频链接获取方式
![](img/3bdf86cb3bf530410615556498928fa1.png)

![](img/32428742929d3f427403a4847ed5c05c.png)

![](img/47ea4754542c680248c9e2578b653cdb.png)

Excel的写法要求：链接放在任意一列都可以，但该列的第一行必须写“URL”或“url”，否则程序无法识别！

![](img/0e54148261dedc6043a7d9fd5d8fa3dd.png)

![](img/3839bd4b6e08c421c090f1b87300077a.png)

### 操作流程

准备工作就绪后打开软件：

① 填入代理地址并保存
![](img/e90fc09c422bd0f1455d7403293d56a7.png)

② 导入存放视频链接的Excel文件
![](img/7b917cdc8622c5e35da8408d663ee953.png)

③ 指定下载完成后视频的保存文件夹
![](img/5240b1e41cc07591f18dd8415f534fcc.png)

④ 选择存放cookie的txt文件
![](img/4858939d8bbe112e7d6fad8d22e053ce.png)

⑤ 选择目标分辨率
⑥ 选择需要下载的视频数量

右侧会实时显示Excel中可识别的视频总数，输入n后就会下载最前面的n个，程序从上往下依次读取，待下载的链接会实时显示在底部文本框

![](img/352b14c1f2830e8046991f606594dab5.png)

![](img/9fde81f2386431cfcdb4ff4c167b9c9f.png)

⑦ 点击开始下载

任务完成后会自动生成一份Excel记录，文件名格式为“下载结果_具体下载时间”，里面清晰标注每个视频是否下载成功

![](img/9e4ad7f4d9a33ad5d77da4aecd1d3c10.png)

### 获取软件

百度网盘分享：Youtube批量视频下载.rar

链接：https://pan.baidu.com/s/1_zFUb72xeABeVpldlqambQ?pwd=xrmc

提取码：xrmc

### 源码

#### 主程序

```
import yt_dlp
from tqdm import tqdm
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

def get_format_option(resolution):
    """根据选择的分辨率返回格式选项"""
    resolution_map = {
        '720p': 720,
        '1080p': 1080,
        '1440p': 1440
    }
    height = resolution_map[resolution]
    # 添加编码格式限制，优先选择 H.264 编码
    return f'bestvideo[height<={height}][vcodec^=avc]+bestaudio[ext=m4a]/best[height<={height}]/best'

def batch_download(urls, output_path, resolution, proxy=None, progress_callback=None):
    """批量下载视频的函数"""
    results = []
    total = len(urls)
    completed = 0

    ydl_opts = {
        'format': get_format_option(resolution),
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'ignoreerrors': True,
        'quiet': True,
        'no_warnings': True,
        'format_sort': ['vcodec:h264'],
        # 使用aria2c作为外部下载器
        'external_downloader': 'aria2c',
        'external_downloader_args': [
            '--min-split-size=1M',  # 最小分片大小
            '--max-connection-per-server=16',  # 单个服务器最大连接数
            '--split=16',  # 单个文件分成16片下载
            '--max-concurrent-downloads=3',  # 同时下载数
            '--continue=true',  # 支持断点续传
            '--optimize-concurrent-downloads=true'  # 优化并发下载
        ]
    }

    if proxy:
        ydl_opts['proxy'] = proxy
        # 为aria2c也添加代理设置
        ydl_opts['external_downloader_args'].extend([
            f'--all-proxy={proxy}'
        ])

    # 添加下载进度回调
    def download_progress_hook(d):
        if d['status'] == 'downloading':
            try:
                downloaded = d.get('downloaded_bytes', 0)
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                if total_bytes:
                    video_progress = downloaded / total_bytes
                    total_progress = (completed + video_progress) / total
                    if progress_callback:
                        progress_callback(total_progress, f"正在下载第 {completed + 1}/{total} 个视频")
            except Exception:
                pass

    ydl_opts['progress_hooks'] = [download_progress_hook]

    for i, url in enumerate(urls):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                results.append({
                    'URL': url,
                    '状态': '成功',
                    '信息': '下载成功'
                })
        except Exception as e:
            results.append({
                'URL': url,
                '状态': '失败',
                '信息': str(e)
            })

        completed += 1
        if progress_callback:
            progress_callback(completed / total, f"完成第 {completed}/{total} 个视频")

    return results

def read_urls_from_excel(file_path):
    """从Excel文件读取URL列表"""
    try:
        df = pd.read_excel(file_path)
        url_column = None
        for col in df.columns:
            if col.lower() == 'url':
                url_column = col
                print(f"找到URL列：{col}（第 {list(df.columns).index(col) + 1} 列）")
                break

        if url_column is None:
            print("错误：Excel文件中没有找到'URL'或'url'列")
            return None

        urls = df[url_column].dropna().tolist()
        return urls
    except Exception as e:
        print(f"读取Excel文件时出错: {str(e)}")
        return None

def save_results_to_excel(results, output_path):
    """保存下载结果到Excel文件"""
    try:
        df = pd.DataFrame(results)
        result_file = os.path.join(output_path, f'下载结果_{time.strftime("%Y%m%d_%H%M%S")}.xlsx')
        df.to_excel(result_file, index=False)
        print(f"\n下载结果已保存到: {result_file}")
    except Exception as e:
        print(f"保存结果文件时出错: {str(e)}")

def get_valid_path():
    """获取有效的保存路径"""
    while True:
        path = input("请输入保存视频的完整路径: ").strip()
        if not path:
            print("错误：请输入有效的保存路径！")
            continue

        path = os.path.abspath(path)

        try:
            if not os.path.exists(path):
                os.makedirs(path)
            if os.access(path, os.W_OK):
                return path
            else:
                print("错误：没有写入权限，请选择其他路径")
        except Exception as e:
            print(f"错误：无效的路径 ({str(e)})")

def get_resolution_choice():
    """获取用户选择的分辨率"""
    while True:
        print("\n请选择下载视频的分辨率：")
        print("1\. 720p")
        print("2\. 1080p")
        print("3\. 1440p")
        choice = input("请输入选择（1-3）: ").strip()

        resolution_map = {
            '1': '720p',
            '2': '1080p',
            '3': '1440p'
        }

        if choice in resolution_map:
            return resolution_map[choice]
        print("无效的选择，请重新输入！")

def main():
    print("YouTube视频批量下载器")
    print("=" * 50)

    # 获取Excel文件路径
    while True:
        excel_path = input("请输入Excel文件的完整路径: ").strip()
        if os.path.exists(excel_path):
            break
        print("错误：文件不存在，请重新输入！")

    # 读取URL列表
    urls = read_urls_from_excel(excel_path)
    if not urls:
        print("无法从Excel文件中读取URL，请检查文件格式")
        return

    print(f"从Excel中读取到 {len(urls)} 个URL")

    # 获取保存路径
    save_path = get_valid_path()
    print(f"视频将保存到: {save_path}")

    # 获取分辨率选择
    resolution = get_resolution_choice()
    print(f"已选择下载分辨率: {resolution}")

    # 获取下载数量
    while True:
        try:
            max_videos = input(f"请输入要下载的视频数量（最大{len(urls)}个，直接回车下载全部）: ").strip()
            if not max_videos:
                max_videos = None
                break
            max_videos = int(max_videos)
            if 1 <= max_videos <= len(urls):
                break
            print(f"请输入1到{len(urls)}之间的数字！")
        except ValueError:
            print("请输入有效的数字！")

    # 执行批量下载
    results = batch_download(urls, save_path, resolution, max_videos)

    # 保存下载结果
    save_results_to_excel(results, save_path)

    # 显示统计信息
    success_count = sum(1 for r in results if r['状态'] == '成功')
    print(f"\n下载完成！成功: {success_count}/{len(results)}")

if __name__ == "__main__":
    main()
```

#### UI

你有没有想过，一个看似不起眼的按钮，为什么能让你毫不犹豫地点下去？一段简洁的布局，为什么能让你在进入页面的三秒内就感到安心？答案藏在一个常被忽视却无处不在的概念里——UI。

UI，即用户界面，它不只是屏幕上的图标、配色和字体，更是产品与用户之间最直接的对话方式。它像是一座无形的桥，一头连着冰冷的代码逻辑，另一头连着鲜活的人类直觉。好的UI不会大声说话，它只会在你恰好需要的地方，递上你恰好想要的选项。

一个真正优秀的界面，往往让人感受不到它的存在。你不会为“怎么用”而分心，只会自然而然地“用起来”。这种体验不是偶然，而是设计师对每一个像素间距、每一次点击反馈、每一帧过渡节奏精细打磨的结果。UI的价值，恰恰藏在这些看不见的取舍里：它让复杂的东西变得简单，让陌生的流程变得熟悉，让每一次交互都像和老朋友打招呼一样顺畅。

在信息过载的时代，UI更像是一种克制的艺术。它用清晰的层级告诉你什么重要，用克制的色彩引导你的情绪，用流畅的动效补偿你对等待的不耐烦。它不追求炫目，而追求理解；不强调存在，而强调完成。当你流畅地完成一次网购、顺利地上传一份文件、轻松地找到一条设置时，你其实正在享受一场由UI精心编排的无声演出。

所以，下一次当你指尖轻触屏幕、毫无阻碍地完成某个操作时，不妨在心里为那个沉默的界面设计者点个赞。毕竟，是UI让技术的冰山，显露出温暖而可靠的一角。

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
from Youtube_Downloader import batch_download, read_urls_from_excel
from threading import Thread

class YoutubeDownloaderUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube视频批量下载器")
        self.root.geometry("900x800")  # 增加窗口高度以适应新添加的链接显示区域

        # 设置整体样式
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('Header.TLabel', font=('Microsoft YaHei UI', 12, 'bold'), background='#f0f0f0')
        self.style.configure('TLabel', font=('Microsoft YaHei UI', 10), background='#f0f0f0')
        self.style.configure('TButton', font=('Microsoft YaHei UI', 10))
        self.style.configure('Download.TButton', font=('Microsoft YaHei UI', 11, 'bold'))

        # 加载保存的代理设置
        self.proxy_config_file = 'proxy_config.json'
        self.saved_proxy = self.load_proxy_config()

        self.urls = []
        self.setup_ui()
        self.setup_callbacks()

    def setup_ui(self):
        # 创建主容器
        main_container = ttk.Frame(self.root, padding="20", style='TFrame')
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # 标题
        title_label = ttk.Label(main_container, text="YouTube视频批量下载器",
                                style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # 创建输入区域框架
        input_frame = ttk.LabelFrame(main_container, text="下载设置", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # Excel文件选择
        ttk.Label(input_frame, text="Excel文件路径:").grid(row=0, column=0, sticky=tk.W, pady=8)
        self.excel_path = tk.StringVar()
        excel_entry = ttk.Entry(input_frame, textvariable=self.excel_path, width=60)
        excel_entry.grid(row=0, column=1, sticky=tk.W, padx=(10, 10))
        ttk.Button(input_frame, text="浏览", command=self.select_excel, width=15).grid(row=0, column=2)

        # 保存路径选择
        ttk.Label(input_frame, text="保存路径:").grid(row=1, column=0, sticky=tk.W, pady=8)
        self.save_path = tk.StringVar()
        save_entry = ttk.Entry(input_frame, textvariable=self.save_path, width=60)
        save_entry.grid(row=1, column=1, sticky=tk.W, padx=(10, 10))
        ttk.Button(input_frame, text="浏览", command=self.select_save_path, width=15).grid(row=1, column=2)

        # 代理设置
        ttk.Label(input_frame, text="代理地址:").grid(row=2, column=0, sticky=tk.W, pady=8)
        self.proxy = tk.StringVar(value=self.saved_proxy)
        proxy_entry = ttk.Entry(input_frame, textvariable=self.proxy, width=60)
        proxy_entry.grid(row=2, column=1, sticky=tk.W, padx=(10, 10))
        ttk.Button(input_frame, text="保存代理", command=self.save_proxy, width=15).grid(row=2, column=2)

        # 创建选项区域框架
        options_frame = ttk.LabelFrame(main_container, text="下载选项", padding="10")
        options_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # 分辨率选择
        ttk.Label(options_frame, text="视频分辨率:").grid(row=0, column=0, sticky=tk.W, pady=8)
        self.resolution = tk.StringVar(value="1080p")
        resolution_frame = ttk.Frame(options_frame)
        resolution_frame.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))

        resolutions = [("720p", "720p"), ("1080p", "1080p"), ("1440p", "1440p")]
        for i, (text, value) in enumerate(resolutions):
            ttk.Radiobutton(resolution_frame, text=text, variable=self.resolution,
                            value=value).grid(row=0, column=i, padx=20)

        # 下载数量设置
        ttk.Label(options_frame, text="下载数量:").grid(row=1, column=0, sticky=tk.W, pady=8)
        download_frame = ttk.Frame(options_frame)
        download_frame.grid(row=1, column=1, sticky=tk.W, padx=(10, 0))

        self.download_count = tk.StringVar()
        ttk.Entry(download_frame, textvariable=self.download_count, width=10).grid(row=0, column=0)
        self.max_videos_label = ttk.Label(download_frame, text="最多可以下载0个视频")
        self.max_videos_label.grid(row=0, column=1, padx=(20, 0))

        # 创建视频链接显示区域
        urls_frame = ttk.LabelFrame(main_container, text="视频链接列表", padding="10")
        urls_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # 创建滚动文本框
        self.urls_text = tk.Text(urls_frame, height=6, width=80, font=('Microsoft YaHei UI', 9))
        scrollbar = ttk.Scrollbar(urls_frame, orient="vertical", command=self.urls_text.yview)
        self.urls_text.configure(yscrollcommand=scrollbar.set)

        self.urls_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # 设置文本框只读
        self.urls_text.configure(state='disabled')

        # 创建进度显示区域
        progress_frame = ttk.LabelFrame(main_container, text="下载进度", padding="10")
        progress_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        self.progress_label = ttk.Label(progress_frame, text="准备就绪")
        self.progress_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 5))

        self.progress = ttk.Progressbar(progress_frame, length=800, mode='determinate')
        self.progress.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 5))

        self.status_label = ttk.Label(progress_frame, text="总进度: 0%")
        self.status_label.grid(row=2, column=0, columnspan=3, sticky=tk.W)

        # 下载按钮
        self.download_button = ttk.Button(main_container, text="开始下载",
                                          command=self.start_download, style='Download.TButton', width=20)
        self.download_button.grid(row=5, column=0, columnspan=3, pady=10)

    def setup_callbacks(self):
        """设置回调函数"""

        def on_download_count_change(*args):
            if self.urls:
                self.update_urls_display()

        self.download_count.trace_add("write", on_download_count_change)

    def update_urls_display(self):
        """更新视频链接显示"""
        self.urls_text.configure(state='normal')
        self.urls_text.delete(1.0, tk.END)

        count = int(self.download_count.get()) if self.download_count.get() else len(self.urls)
        count = min(count, len(self.urls))

        for i, url in enumerate(self.urls[:count], 1):
            self.urls_text.insert(tk.END, f"{i}. {url}\n")

        self.urls_text.configure(state='disabled')

    def load_proxy_config(self):
        try:
            if os.path.exists(self.proxy_config_file):
                with open(self.proxy_config_file, 'r') as f:
                    config = json.load(f)
                    return config.get('proxy', '')
        except Exception:
            pass
        return ''

    def save_proxy(self):
        proxy = self.proxy.get()
        try:
            with open(self.proxy_config_file, 'w') as f:
                json.dump({'proxy': proxy}, f)
            messagebox.showinfo("成功", "代理设置已保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存代理设置失败: {str(e)}")

    def select_excel(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if filename:
            self.excel_path.set(filename)
            self.urls = read_urls_from_excel(filename) or []
            self.max_videos_label.config(text=f"最多可以下载{len(self.urls)}个视频")
            self.update_urls_display()

    def select_save_path(self):
        path = filedialog.askdirectory()
        if path:
            self.save_path.set(path)

    def update_progress(self, progress, status_text):
        """更新进度显示"""
        self.progress['value'] = progress * 100
        self.progress_label.config(text=status_text)
        self.status_label.config(text=f"总进度: {progress:.1%}")
        self.root.update_idletasks()

    def validate_inputs(self):
        if not self.excel_path.get():
            messagebox.showerror("错误", "请选择Excel文件")
            return False
        if not self.save_path.get():
            messagebox.showerror("错误", "请选择保存路径")
            return False
        if not self.urls:
            messagebox.showerror("错误", "Excel文件中没有找到有效的URL")
            return False

        try:
            count = int(self.download_count.get() or len(self.urls))
            if count <= 0 or count > len(self.urls):
                messagebox.showerror("错误", f"下载数量必须在1到{len(self.urls)}之间")
                return False
            self.update_urls_display()
        except ValueError:
            messagebox.showerror("错误", "请输入有效的下载数量")
            return False

        return True

    def start_download(self):
        if not self.validate_inputs():
            return

        self.download_button.state(['disabled'])
        Thread(target=self.download_thread).start()

    def download_thread(self):
        try:
            count = int(self.download_count.get() or len(self.urls))
            proxy = self.proxy.get()

            def progress_callback(progress, status):
                self.root.after(0, self.update_progress, progress, status)

            results = batch_download(
                self.urls[:count],
                self.save_path.get(),
                self.resolution.get(),
                proxy=proxy,
                progress_callback=progress_callback
            )

            success_count = sum(1 for r in results if r['状态'] == '成功')
            messagebox.showinfo("完成", f"下载完成！成功: {success_count}/{len(results)}")

        except Exception as e:
            messagebox.showerror("错误", f"下载过程中出错: {str(e)}")

        finally:
            self.download_button.state(['!disabled'])
            self.status_label.config(text="就绪")
            self.progress_label.config(text="")
            self.progress['value'] = 0

def main():
    root = tk.Tk()
    app = YoutubeDownloaderUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
from Youtube_Downloader import batch_download, read_urls_from_excel
from threading import Thread

class YoutubeDownloaderUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube视频批量下载器")
        self.root.geometry("900x800")  # 增加窗口高度以适应新添加的链接显示区域

        # 设置整体样式
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('Header.TLabel', font=('Microsoft YaHei UI', 12, 'bold'), background='#f0f0f0')
        self.style.configure('TLabel', font=('Microsoft YaHei UI', 10), background='#f0f0f0')
        self.style.configure('TButton', font=('Microsoft YaHei UI', 10))
        self.style.configure('Download.TButton', font=('Microsoft YaHei UI', 11, 'bold'))

        # 加载保存的代理设置
        self.proxy_config_file = 'proxy_config.json'
        self.saved_proxy = self.load_proxy_config()

        self.urls = []
        self.setup_ui()
        self.setup_callbacks()

    def setup_ui(self):
        # 创建主容器
        main_container = ttk.Frame(self.root, padding="20", style='TFrame')
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # 标题
        title_label = ttk.Label(main_container, text="YouTube视频批量下载器",
                                style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # 创建输入区域框架
        input_frame = ttk.LabelFrame(main_container, text="下载设置", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # Excel文件选择
        ttk.Label(input_frame, text="Excel文件路径:").grid(row=0, column=0, sticky=tk.W, pady=8)
        self.excel_path = tk.StringVar()
        excel_entry = ttk.Entry(input_frame, textvariable=self.excel_path, width=60)
        excel_entry.grid(row=0, column=1, sticky=tk.W, padx=(10, 10))
        ttk.Button(input_frame, text="浏览", command=self.select_excel, width=15).grid(row=0, column=2)

        # 保存路径选择
        ttk.Label(input_frame, text="保存路径:").grid(row=1, column=0, sticky=tk.W, pady=8)
        self.save_path = tk.StringVar()
        save_entry = ttk.Entry(input_frame, textvariable=self.save_path, width=60)
        save_entry.grid(row=1, column=1, sticky=tk.W, padx=(10, 10))
        ttk.Button(input_frame, text="浏览", command=self.select_save_path, width=15).grid(row=1, column=2)

        # 代理设置
        ttk.Label(input_frame, text="代理地址:").grid(row=2, column=0, sticky=tk.W, pady=8)
        self.proxy = tk.StringVar(value=self.saved_proxy)
        proxy_entry = ttk.Entry(input_frame, textvariable=self.proxy, width=60)
        proxy_entry.grid(row=2, column=1, sticky=tk.W, padx=(10, 10))
        ttk.Button(input_frame, text="保存代理", command=self.save_proxy, width=15).grid(row=2, column=2)

        # 创建选项区域框架
        options_frame = ttk.LabelFrame(main_container, text="下载选项", padding="10")
        options_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # 分辨率选择
        ttk.Label(options_frame, text="视频分辨率:").grid(row=0, column=0, sticky=tk.W, pady=8)
        self.resolution = tk.StringVar(value="1080p")
        resolution_frame = ttk.Frame(options_frame)
        resolution_frame.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))

        resolutions = [("720p", "720p"), ("1080p", "1080p"), ("1440p", "1440p")]
        for i, (text, value) in enumerate(resolutions):
            ttk.Radiobutton(resolution_frame, text=text, variable=self.resolution,
                            value=value).grid(row=0, column=i, padx=20)

        # 下载数量设置
        ttk.Label(options_frame, text="下载数量:").grid(row=1, column=0, sticky=tk.W, pady=8)
        download_frame = ttk.Frame(options_frame)
        download_frame.grid(row=1, column=1, sticky=tk.W, padx=(10, 0))

        self.download_count = tk.StringVar()
        ttk.Entry(download_frame, textvariable=self.download_count, width=10).grid(row=0, column=0)
        self.max_videos_label = ttk.Label(download_frame, text="最多可以下载0个视频")
        self.max_videos_label.grid(row=0, column=1, padx=(20, 0))

        # 创建视频链接显示区域
        urls_frame = ttk.LabelFrame(main_container, text="视频链接列表", padding="10")
        urls_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        # 创建滚动文本框
        self.urls_text = tk.Text(urls_frame, height=6, width=80, font=('Microsoft YaHei UI', 9))
        scrollbar = ttk.Scrollbar(urls_frame, orient="vertical", command=self.urls_text.yview)
        self.urls_text.configure(yscrollcommand=scrollbar.set)

        self.urls_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # 设置文本框只读
        self.urls_text.configure(state='disabled')

        # 创建进度显示区域
        progress_frame = ttk.LabelFrame(main_container, text="下载进度", padding="10")
        progress_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))

        self.progress_label = ttk.Label(progress_frame, text="准备就绪")
        self.progress_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 5))

        self.progress = ttk.Progressbar(progress_frame, length=800, mode='determinate')
        self.progress.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 5))

        self.status_label = ttk.Label(progress_frame, text="总进度: 0%")
        self.status_label.grid(row=2, column=0, columnspan=3, sticky=tk.W)

        # 下载按钮
        self.download_button = ttk.Button(main_container, text="开始下载",
                                          command=self.start_download, style='Download.TButton', width=20)
        self.download_button.grid(row=5, column=0, columnspan=3, pady=10)

    def setup_callbacks(self):
        """设置回调函数"""

        def on_download_count_change(*args):
            if self.urls:
                self.update_urls_display()

        self.download_count.trace_add("write", on_download_count_change)

    def update_urls_display(self):
        """更新视频链接显示"""
        self.urls_text.configure(state='normal')
        self.urls_text.delete(1.0, tk.END)

        count = int(self.download_count.get()) if self.download_count.get() else len(self.urls)
        count = min(count, len(self.urls))

        for i, url in enumerate(self.urls[:count], 1):
            self.urls_text.insert(tk.END, f"{i}. {url}\n")

        self.urls_text.configure(state='disabled')

    def load_proxy_config(self):
        try:
            if os.path.exists(self.proxy_config_file):
                with open(self.proxy_config_file, 'r') as f:
                    config = json.load(f)
                    return config.get('proxy', '')
        except Exception:
            pass
        return ''

    def save_proxy(self):
        proxy = self.proxy.get()
        try:
            with open(self.proxy_config_file, 'w') as f:
                json.dump({'proxy': proxy}, f)
            messagebox.showinfo("成功", "代理设置已保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存代理设置失败: {str(e)}")

    def select_excel(self):
        filename = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if filename:
            self.excel_path.set(filename)
            self.urls = read_urls_from_excel(filename) or []
            self.max_videos_label.config(text=f"最多可以下载{len(self.urls)}个视频")
            self.update_urls_display()

    def select_save_path(self):
        path = filedialog.askdirectory()
        if path:
            self.save_path.set(path)

    def update_progress(self, progress, status_text):
        """更新进度显示"""
        self.progress['value'] = progress * 100
        self.progress_label.config(text=status_text)
        self.status_label.config(text=f"总进度: {progress:.1%}")
        self.root.update_idletasks()

    def validate_inputs(self):
        if not self.excel_path.get():
            messagebox.showerror("错误", "请选择Excel文件")
            return False
        if not self.save_path.get():
            messagebox.showerror("错误", "请选择保存路径")
            return False
        if not self.urls:
            messagebox.showerror("错误", "Excel文件中没有找到有效的URL")
            return False

        try:
            count = int(self.download_count.get() or len(self.urls))
            if count <= 0 or count > len(self.urls):
                messagebox.showerror("错误", f"下载数量必须在1到{len(self.urls)}之间")
                return False
            self.update_urls_display()
        except ValueError:
            messagebox.showerror("错误", "请输入有效的下载数量")
            return False

        return True

    def start_download(self):
        if not self.validate_inputs():
            return

        self.download_button.state(['disabled'])
        Thread(target=self.download_thread).start()

    def download_thread(self):
        try:
            count = int(self.download_count.get() or len(self.urls))
            proxy = self.proxy.get()

            def progress_callback(progress, status):
                self.root.after(0, self.update_progress, progress, status)

            results = batch_download(
                self.urls[:count],
                self.save_path.get(),
                self.resolution.get(),
                proxy=proxy,
                progress_callback=progress_callback
            )

            success_count = sum(1 for r in results if r['状态'] == '成功')
            messagebox.showinfo("完成", f"下载完成！成功: {success_count}/{len(results)}")

        except Exception as e:
            messagebox.showerror("错误", f"下载过程中出错: {str(e)}")

        finally:
            self.download_button.state(['!disabled'])
            self.status_label.config(text="就绪")
            self.progress_label.config(text="")
            self.progress['value'] = 0

def main():
    root = tk.Tk()
    app = YoutubeDownloaderUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```。

接下来要做的，就是接住它，然后，把故事讲下去。

# 两个小工具背后的故事

这两款软件的诞生，其实挺偶然的。我学完AI编程航海手册后，又从圈友那里get到了Cursor的厉害之处，就想拿它做几个小项目练练手。没想到一试，效果比预期好不少。

刚做完那会儿，兴奋劲儿还没过，直接在生财立了个flag，说要把成果分享给圈友们。再后来，刷到好多圈友都在发Cursor相关教程，觉得自己再写开发流程就有点炒冷饭了，动力瞬间就没了，哈哈哈。

最初这两个软件其实只是裸的python脚本，压根没做封装。真要拿出来给大家用，光秃秃的脚本肯定不行——不懂编程的圈友根本跑不起来。可一想到还得补UI、搞打包、弄优化，脑子里立刻蹦出“好麻烦”，于是就一直拖着（手动狗头）。

还好有彭哥@老彭 在后面催，这才趁着有空，一口气完成了优化封装，然后赶紧把帖子肝了出来。

需要说明的是，为了不跟已有的教程撞车，这篇就以工具安利为主，开发细节后面再慢慢补（主要是Cursor按项目开了一堆聊天，现在好多记录我自己都翻不到了……）。先把工具交到大家手里，如果你们用着觉得有帮助，欢迎点赞、留言，或者给我提优化建议，我都超需要！

# 致谢环节

特别感谢彭哥@老彭 的连环催更，不然这篇帖子大概率还在难产中。

感谢马哥@老馬🐎内容出海 分享的方法——调用Youtube官方API采集数据，我的第一个软件思路就是从那儿来的。

感谢@阿紫 分享的教程，以及@Time 的《0代码AI编程重塑你的编程体验：Cursor使用教程》，我就是靠这两个教程自己摸索着上手了Cursor。

感谢@阿威 告诉我Python有个yt_dlp库能下载YouTube视频，不然我可能真要跑去做在线下载网站了。

感谢@红哥Frank 分享的YouTube在线网站开发过程。我一直以为视频分辨率最多1080P，看完红哥的帖子才知道还有1440P和更高，实属打开了新世界。

![](img/efa32ad387355ac037d3b99db5e2bfb7.png)

![](img/bacb3763b7a0a63156488daa9f1510eb.png)