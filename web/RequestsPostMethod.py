import requests

data = {"name": 'a', 'age': 1}

response = requests.post('http://httpbin.org/post', data=data)
print(response.text)

# 添加header信息
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.post('http://httpbin.org/post', data=data, headers=header)
print(response.text)
