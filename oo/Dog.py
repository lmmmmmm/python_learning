class Dog(object):
    def __init__(self, type, color):
        self.__color = color
        self.__type = type
    def print_info(self):
        print(self.__type,self.__color)

    def get_type(self):
        return self.__type

    def set_color(self):
        return self.__color

dog = Dog("a","red")
print(dog.print_info())

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self,gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.gender = gender


s = Student("man")
print(s.get_gender())
s.set_gender("woman")
print(s.get_gender())