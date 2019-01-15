from bs4 import BeautifulSoup

# 标签选择器
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)

# 标签选择器
print(soup.title)
print(type(soup.title))
print(soup.p)
print(soup.a)

# 获取名称
print(soup.title.name)

# 获取属性
print(soup.p.attrs['name'])
print(soup.p['name'])

# 获取内容
print(soup.p.string)

# 嵌套选择
print(soup.head.title.string)
print(soup.a.string)

# 子节点和子孙节点
# contents返回所有子节点,返回类型列表,
# children也是返回所有子节点,返回类型是迭代器
# descendants返还所有子孙节点,返还类型是迭代器
print(soup.p.contents)
print(soup.body.children)
for child in enumerate(soup.body.children):
    print(child)

print(soup.html.descendants)
for child in enumerate(soup.html.descendants):
    print(child)

# 获取父节点
print('-------获取父节点----------')
print(soup.p.parent)
print('--------获取祖先节点-----------')
print(soup.a.parents)
for parent in soup.a.parents:
    print(parent)

# 获取兄弟节点
print('---------获取兄弟节点--------------')
# 获取前一个节点
print('前一个节点', list(enumerate(soup.p.previous_siblings)))
# 获取后一个节点
print('后一个节点', list(enumerate(soup.p.next_siblings)))
