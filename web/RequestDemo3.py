# 代理
import urllib.request
import http.cookiejar

proxy_handel = urllib.request.ProxyHandler({
    "http:": 'http://127.0.0.1:8123',
    "https:": 'http://127.0.0.1:8123'
})
opener = urllib.request.build_opener(proxy_handel)
response = opener.open('http://httpbin.org/get')
print(response.read())

# cookie
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)

# 保存cookie在本地
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

# 携带本地cookie访问
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
