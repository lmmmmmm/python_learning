# 标准选择器
# find_all(name,attrs,recursive,text,**kwargs) 可以根据标签名.属性名.内容查找文档

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('--------简单的测试---------------')
print(soup.find_all('title'))
print(soup.find_all('p', 'title'))
print(soup.find_all('a'))

# name参数:name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉.
print('name参数:', soup.find_all('title'))

# keyword参数:如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,
# 如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
print(soup.find_all(id='link3'))
