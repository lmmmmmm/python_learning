from bs4 import BeautifulSoup

# 标准选择器
# find_all(name,attrs,recursive,text,**kwargs) 可以根据标签名.属性名.内容查找文档

html = """
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    
"""
soup = BeautifulSoup(html, 'lxml')
print('--------------------根据标签名查找---------------------')
print('查找所有ul标签', soup.find_all('ul'))
print('查找第一个ul标签', soup.find_all('ul')[0])
print('第一个ul标签类型', type(soup.find_all('ul')[0]))
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))

print('--------------------根据属性名查找---------------------')
# 元素如果拥有id或class则可以通过find_all(id或class_='') 查找
# 否则通过find_all(attrs = {'id/name':''}) 查找
print(soup.find_all(id='list-1'))
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))
print(soup.find_all(class_='element'))

print('--------------------利用text查找---------------------')
# 返还结果是text,不返还元素标签
print(soup.find_all(text='Foo'))
