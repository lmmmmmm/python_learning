#把一个getter方法变成属性，只需要加上@property就可以了，
#此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an Integet value')
        if value < 0 or value > 200:
            raise ValueError('score must between 0 ~ 200')
        self._score = value

s = Student()
s.score = 60
print(s.score)
# s.score = 999
# s.score = '1'

class Person(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def sex(self):
        return self._sex
    
p = Person()
p.name = 'zhang san'
print(p.name)
p.sex = 'man'
print(s.sex)