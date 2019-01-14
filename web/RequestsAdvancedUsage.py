import requests

# requests高级用法

# 文件上传
files = {'file': open('logo.png', 'rb')}
response = requests.post('http://httpbin.org/post', data=files)
print(response.text)

# 获取cookie
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)

# 会话维持
requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)

session = requests.Session()
session.get('http://httpbin.org/cookies/set/number/123456789')
response = session.get('http://httpbin.org/cookies')
print(response.text)

# 证书验证
response = requests.get('https://www.12306.cn')
print(response.status_code)

# 代理设置
proxy = {
    'http': 'http://127.0.0.1:8123',
    'https': 'https://127.0.0.1:8123'
}
response = requests.get('https://www.baidu.com', proxies=proxy)
print(response.status_code)


