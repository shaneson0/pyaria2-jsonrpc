## summary
aria2是一个十分牛逼的下载神器，有时候项目需要一个很牛逼的下载中间件的话，aria2是一个不错的选择。其中支持jsonrpc和websocket的特性尤其诱人。但是python用起来还是有点不爽，所以简单封装一下aria2的jsonrpc。


所以，用python简单的封装了aria2的jsonrpc中adduri的脚本。
使用起来非常简单，仅需要三行代码。
```python
from pyaria2 import Jsonrpc
jsonrpc = Jsonrpc('localhost', 6800)
resp = jsonrpc.addUris('https://music.snowmusic.cc/radio/13714_1507261169_4.mp3', options={"out": "aa.mp3"})
print resp
# {"id":0,"jsonrpc":"2.0","result":"3f6fa9aa6428a25f"}
```

## Install

首先需要安装aria2c(以mac为例)

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

```
然后使用homebrew安装即可
```
brew install aria2
```

然后自己找一个文件夹新建一个aria2.conf文件，示例如下：
```
#允许rpc
enable-rpc=true
#允许非外部访问
rpc-listen-all=true
#RPC端口, 仅当默认端口被占用时修改
rpc-listen-port=6800

#最大同时下载数(任务数), 路由建议值: 3
max-concurrent-downloads=10
#断点续传
continue=true
#同服务器连接数
max-connection-per-server=10
#最小文件分片大小, 下载线程数上限取决于能分出多少片, 对于小文件重要
min-split-size=10M
#单文件最大线程数, 路由建议值: 5
split=10
#下载速度限制
max-overall-download-limit=0
#单文件速度限制
max-download-limit=0
#上传速度限制
max-overall-upload-limit=0
#单文件速度限制
max-upload-limit=0

#文件保存路径, 默认为当前启动位置
dir=./Files

#hook 文件的路径
on-download-complete=/Users/csx/GitProject/snowmusic/pyaria2-jsonrpc/hook.py


```

**其中hook文件路径是回调脚本的路径，这里要改为开发者当前hook文件路径**

启动aria2

```
# 这里是填入aria2.conf的路径
aria2c --conf-path=aria2.conf

```

## Use

首先导入pyaria2模块的jsonrpc

```
from pyaria2 import Jsonrpc

```

编写hook.py，用于下载完成的回调。
```python
import sys

# ['/Users/csx/GitProject/snowmusic/pyaria2-jsonrpc/hook.py', 'e3f97be6d4490a5a', '1', './temp/aa.mp3']
Argv = sys.argv

# 这里自己编写任意的回调函数，可以进行更新数据库等操作
def Hook(Argv):
    print Argv

```

然后直接调用就可以了。

```
jsonrpc = Jsonrpc('localhost', 6800)
resp = jsonrpc.addUris('https://music.snowmusic.cc/radio/13714_1507261169_4.mp3', options={"out": "aa.mp3"})
print resp

```

## API

http://aria2.github.io/manual/en/html/index.html
