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
