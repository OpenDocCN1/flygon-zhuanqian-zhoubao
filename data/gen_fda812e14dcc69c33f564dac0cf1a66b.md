[PRE0]

在打包成 exe 之前，先把代码本地跑通一遍，确认无报错再进行下一步。

如果运行过程中提示缺包，先去终端把依赖装上：

[PRE1]

[PRE2]

* * *

等这三件事都准备好后，就只剩最后的打包环节了。整体打包流程可以拆成 4 个环节来做：

1、把 pyinstaller 装到环境里。操作共两步：

点击这里

[PRE3]

在命令行里执行 pip install pyinstaller，看到安装日志滚动后耐心等到完成。

2、确定你要打包的 Python 脚本名，可以直接敲也可以复制路径。举例我这边用的是 test.py

[PRE4]

3、开始封装程序，分两步完成。

点击这里：

[PRE5]

执行命令 pyinstaller -F -w test.py 然后回车。

也可以写完整路径的方式执行：pyinstaller -F -w C:\Users\PC\.cursor-tutor\projects\python\test.py 回车即可。

这里的第二个写法就是指定文件的绝对路径。

我的示例文件叫 test.py，你只要把文件名替换成自己的即可。