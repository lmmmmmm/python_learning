class Student(object):
    def __init__(self,name):
        self.name = name

stu = Student("bob")
stu.age = 20
print(stu.name)
print(stu.age)


# if class self has one property,can define into class,this property call class property
class MaleStu():
    name = "boy"

s = MaleStu()
print(s.name)
s.name = '0.0'
print(s.name)

#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

#test
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')