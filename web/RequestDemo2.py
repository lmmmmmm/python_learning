from urllib import request, parse

# 构造更高级的request
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/4.0(compatible; MSIE 5.5; Windows NT)",
    "Host": "httpbin.org"
}
dict1 = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict1), encoding='UTF-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('UTF-8'))

# 直接req添加header
url = "http://httpbin.org/post"
dict1 = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict1), encoding='UTF-8')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('UTF-8'))
