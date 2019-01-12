import urllib.request
import urllib.parse
import urllib.error
import socket

# get 请求方式
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read())

# post 请求方式
data = bytes(urllib.parse.urlencode({"world": "hello"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read())

# 出错
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('超时啦!')
