# 手把手教你：在CentOS VPS上从零装好Docker

> 教程出处：[链接]

## 第一步：拥有一台CentOS服务器

想动手实践，先得有一台CentOS系统的云服务器。阿里云、腾讯云或者别的VPS服务商都可以，我挑的是香港节点——好处很明显，网络环境更自由，以后部署些网站或应用做测试，不用折腾备案，直接就能访问。

买好机器后，第一件事就是重置root密码。在服务商控制台能看到这台VPS的公网IP，这个IP是我们接下来远程登录的重要凭证。

![](img/ab2fdc03076f91e821a64c7c4d356944.png)

重置完成后，记下公网IP。

![](img/e5e36fe0e81fd4032d9bb538f30cf1fe.png)

## 第二步：把防火墙规则全放开

为了后面测试方便，建议先把VPS的防火墙策略设为全部放行。进入服务器管理控制台，找到“防火墙”选项。

![](img/3acc0bc78bf7b0721072aef26a4a5355.png)

点击“添加规则”，把需要的端口都放通。

![](img/621eae89d0dcfc5a5cbdbc0d2bbf2862.png)

![](img/dc075a8a32800996b75edef49ce402db.png)

搞定后，拿出我们的SSH工具准备远程连接。

## 第三步：SSH登录服务器

这里我用的是Xshell和Xftp这对搭档，一个负责命令行操作，一个负责传文件。连接服务器用Xshell就够了。

![](img/e69179c7e683b6cc2930a362377dcdd3.png)

打开Xshell，在右上角找到“新建会话”按钮。

![](img/2a8cd5b4443ecf8067c442faf0a9a0b9.png)

在弹出的窗口里填上你的服务器公网IP，以及SSH端口（默认22）。

![](img/3e755ecc5b3742fd7489993d8af75764.png)

![](img/d2177889d88615d24c77bc27d0064861.png)

填好之后点连接，输入用户名root和刚才重置的密码，回车。

看到命令行提示符变成 `root@你的主机名` 这样的形式，就说明登录成功了。

![](img/8ba495225c072e656675c269c64349b0.png)

## 第四步：安装Docker

接下来是重头戏。把下面两行命令依次粘贴到终端里，Docker就会自动开始安装。这个过程会花一点时间，耐心等它跑完就行。

```
curl -fsSL https://get.docker.com -o get-docker.sh

sh get-docker.sh
```

命令执行完毕后，如果看到类似成功的提示，就代表安装流程结束了。

![](img/71a87a5cd38ea55a9904757546bee71e.png)

![](img/3d8c8ad99f6d8605b8bd87ea66663859.png)

```
docker --version
```

为了确认安装结果，运行 `docker --version`，如果屏幕上出现了Docker的版本号，那就妥妥装好了。

![](img/cb0054c23e082c61e8e9a995cb88a74a.png)

## 第五步：检查并启动Docker服务

```
#设置docker服务开机自启动
systemctl enable docker

#启动docker容器
systemctl start docker

#查看docker是否运行
systemctl status docker
```

再看看Docker服务的运行状态：只要 `active` 一栏显示 `running`，说明Docker已经在正常工作了。

![](img/7ade45c6590a83ea464ea7acf5cce81e.png)

好了，到这里你的CentOS上已经成功跑起了Docker。下一期，我们来聊聊怎么用Docker快速搭建一个ChatGPT应用，敬请期待！