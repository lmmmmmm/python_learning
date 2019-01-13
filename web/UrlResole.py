from urllib.parse import urlparse, urlunparse, urljoin, urlencode

result = urlparse('https://www.bilibili.com/video/av18202461/?p=8&t=1276')
print(type(result), result)

result = urlparse('www.bilibili.com/video/av18202461/?p=8&t=1276', scheme='Https')
print(type(result), result)

# 当url中指定协议类型后,scheme无用
result = urlparse('http://www.bilibili.com/video/av18202461/?p=8&t=1276', scheme='Https')
print(type(result), result)

# urlunparse
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

# urljoin
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'http://www.bilibili.com'))

# urlencode
params = {
    'name': 'a',
    'age': 2
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
