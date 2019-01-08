class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name,self.age)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


stu1 = Student("tim",12)
stu1.print_info()

stu2 = Student("zhangsan",28)
print(stu2.get_name())
print(stu2.get_age())