from urllib import request, error

try:
    response = request.urlopen('https://www.bilibili.com/videos')
    print(response.read())
except error.URLError as e:
    print(e.reason)
