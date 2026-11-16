# 从零到上线，我是怎么做出来的一个 GPTs 导航站



![](img/92bba16cc5fb6115af24aa8fbf2cc68a.png)

# 一、站点的快速搭建

1.  直接用 WordPress 做快速部署。
2.  主题就选 WordPress 自带的免费款，基础功能完全够用。
3.  站点建好后做些基础设置，基本就开张了。
4.  核心是把导航菜单和页面排版调好，按自己的喜好可视化改一下就行，也可以先不碰，后面再弄。

# 二、数据的收集整理

1.  全网抓取为主，目标是所有以 https://chat.openai.com/g/g- 开头的 GPTs 链接。
2.  爬虫范围覆盖 Google、Twitter、Reddit 等社区，以及其他聚合类站点，全部跑一遍后做去重处理。
3.  链接收集完后，再用一个 Chrome 插件写的脚本去 ChatGPT 里逐个提取对应 GPTs 的详细资料。
4.  这个采集环节比较耗时间，而且数据是会持续变动的，需要定期维护更新。

# 三、数据写入站点

1.  从 ChatGPT 侧抓取完结构化信息后，就调用 WordPress 的接口把内容批量写入后台。
2.  写入完成后就形成了现在的 GPTs 管理站点。https://gpt-stores.com/

# 四、向量检索与浏览器插件的叠加

1.  站点成型后顺手把整库做了向量化处理。
2.  又单独做了个 Chrome 插件，直接嵌进 ChatGPT 页面里使用，搜索体验模仿 ChatGPT 自带的插件样式，能在原界面内直接检索并调用。

![](img/52692c757db83e15bc5163b9583f7a02.png)

![](img/dcb8ec8ece3cdf80f54afd62711e7d08.png)

![](img/ba17f0d8c095e162d548d12132954c8d.png)

![](img/0d576f022158784bfd607170c53f6b92.png)

# 五、借助 WordPress 接口实现文章批量导入

把抓到的 GPTs 信息整理成文章格式批量写入 WordPress，可以通过 WP-API 配合插件来完成。下面是操作思路的简化版流程：

## 安装并配置 JWT Authentication for WP-API 插件

1\. 安装并配置 JWT Authentication for WP-API 插件

先在 WordPress 后台装上并启用 “JWT Authentication for WP-API” 插件，用它来申请访问 API 的鉴权凭证。

2\. 获取令牌

通过接口申请 token：

请求地址: https://yourdomain.com/wp-json/jwt-auth/v1/token

请求体：

```
https://yourdomain.com/wp-json/jwt-auth/v1/token
{     
    "username": "wordpress_username",     
    "password": "wordpress_password" 
}
```

返回结果会包含 token，例如：

```
{         
    "token": "xxx",         
    "user_email": "xxx@x.com",         
    "user_nicename": "xxx",         
    "user_display_name": "xxx" 
}
```

## 增加自定义字段

因为封面图需要使用外部 CDN 地址，所以要新增一个自定义字段。可以借助 “Advanced Custom Fields” 插件来创建。

https://www.advancedcustomfields.com/

装好后新建一个字段用来保存第三方图片链接，比如命名为 "cdn_featured_image"。

![](img/8a0fca631c7bf6f34fd0de31fde1cded.png)

## 让自定义字段可通过 API 写入

默认情况下 WordPress 自定义字段不支持 API 写入，需要在主题 functions.php 里加一段代码来放开权限。把下面代码加到 functions.php 末尾，其中 "cdn_featured_image" 为你刚才创建的字段名：

```
function custom_register_post_meta() {
    register_post_meta('post', 'cdn_featured_image', array(
        'show_in_rest' => true,
        'single' => true,
        'type' => 'string',
    ));
}
add_action('init', 'custom_register_post_meta');

```

## 执行批量写入或更新

下面是一段 Python 示例，展示如何用 token 调用 API 完成文章的批量新建或更新：

```
import requests
import json
import datetime

gloab_your_jwt_token = "xxxx"

def create_wordpress_post(post_id, title, content, categories, tags,base_url, featured_media_image_url,download_link,custom_properties, your_jwt_token):
    if your_jwt_token is None:
        your_jwt_token = gloab_your_jwt_token

    url = f'{base_url}/wp-json/wp/v2/posts'
    if post_id is not None:
        url = f'{base_url}/wp-json/wp/v2/posts/{post_id}'

    current_datetime = datetime.datetime.now()
    yesterday = current_datetime - datetime.timedelta(days=1)
    formatted_datetime = yesterday.strftime('%Y-%m-%dT%H:%M:%S')

    # 要插入的Post数据
    postDict = {
        "title": title,  
        "content": content,  
        "date": formatted_datetime, 
        "status": 'publish',  
        "format": 'standard',  
        "categories": categories,  
        "meta":{}
        # TODO: featured_media, excerpt
    }
    # 更新的话，不更新时间
    # if post_id is None:
    #     postDict["date"] = formatted_datetime

    if tags and len(tags)>0:
        postDict["tags"] = tags

    # 判断featured_media_image_url是否为空
    if featured_media_image_url and featured_media_image_url != 461:
        # 如果featured_media_image_url不为空，将其作为自定义字段加入到meta中
        postDict["meta"]["cdn_featured_image"] = featured_media_image_url
    else:
        # 如果featured_media_image_url为空，将featured_media设置为201
        postDict["meta"]["featured_media"] = 461

    if download_link and download_link != '':
        # 如果 download_link 不为空，将其作为自定义字段加入到meta中
        postDict["meta"]["download_link"] = download_link

    curHeaders = {
        "Authorization": "Bearer %s" % your_jwt_token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # print(postDict)

    # 发送POST请求
    response = requests.post(
        url,
        headers=curHeaders,
        json=postDict,
    )

    # 检查响应状态码
    if response.status_code == 200 or response.status_code == 201:
        print('Post创建或者更新成功！')
    else:
        print(f'Post创建或者更新失败，状态码：{response.status_code}')
        print(response.json())
```