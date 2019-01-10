# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'zhangs'
print(s.name)
s.age = 12
print(s.age)

# don't have sex properties
# s.sex = 'man'
# print(s.sex)


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的  
class maleStudent(Student):
   pass

s1 = maleStudent()
s1.name = 'zhangs'
s1.age = 20
s1.sex = 'male'
print(s1.sex)