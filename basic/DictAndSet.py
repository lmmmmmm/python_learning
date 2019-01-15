# dict 类似Java中Map ==> 键值对
score = {'张三': 20, "李四": 50, '王五': 30}
print(score['张三'])
score['赵六'] = 90
print(score['赵六'])
score.pop('赵六')
print(score.get('赵六'))

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 重复元素在set中自动被过滤：
s = set([1, 1, 2, 3, 4, 5, 6])
print(s)
# set.add()添加元素
s.add(7)
print(s)

# s.remove()移除元素
s.remove(7)
print(s)
