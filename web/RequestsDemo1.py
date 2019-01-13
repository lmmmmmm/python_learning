import requests

# requests 基本用法
url = 'http://www.baidu.com'
response = requests.get(url)
print(type(response))
print(response.status_code)
print(response.text)
