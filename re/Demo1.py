import re

# re.match()方法使用
# 尽量使用泛匹配,使用括号得到匹配目标,尽量使用非贪婪模式,有换行就用re.S

# \s 匹配空格 \d 匹配数字
content = 'Hello 123 4567 World_this is Regex Demo'
print(len(content))
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$', content)
print(result)

# 泛匹配
# ^匹配开头 $ 匹配结尾
result = re.match('^He.*o$', content)
print(result)

# 匹配目标
result = re.match('^Hello\s(\d+)\s(\d+)\sW.*Demo$', content)
print(result)
print(result.group(1))
print(result.group(2))

# 贪婪匹配
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))

# 非贪婪匹配
result = re.match('^He.*?(\d+)\s(\d+).*Demo$', content)
print(result)
print(result.group(1))
print(result.group(2))

content2 = 'Hello 1234567 World_this' \
           ' is Regex Demo'

# 匹配模式
result = re.match('^Hello.*?(\d+).*Demo$', content2, re.S)
print(result)
print(result.group(1))

# 转义
content3 = 'price is $5.00'
result = re.match('price is \$5\.00', content3)
print(result)
