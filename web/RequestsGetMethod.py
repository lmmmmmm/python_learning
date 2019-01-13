import requests

response = requests.get('http://httpbin.org/get')
print(response.text)

# 带参数的请求
response = requests.get('http://httpbin.org/get?name=zs&age=2')
print(response.text)

# 另外一种方法
params = {
    'name': 'abc',
    'age': 20
}
response = requests.get('http://httpbin.org/get', params=params)
print(response.text)

# 解析json 调用json()方法
print(response.json())

# 获取二进制数据
response = requests.get('https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_86d58ae1.png')
print(type(response.text), type(response.content))
print(response.text)
print(response.content)
with open('logo.png', 'wb') as f:
    f.write(response.content)

# 添加header
# 知乎如果不加header则无法访问
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get('https://www.zhihu.com/explore', headers=header)
print(response.text)
