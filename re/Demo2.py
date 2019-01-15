import re

# re.search()方法 为了匹配方便能用search就不用match

content = 'Extra setting Hello 123456 World_this is Regex Demo'
result = re.match('He.*?(\d+).*?Demo', content)
print(result)

result = re.search('He.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))

