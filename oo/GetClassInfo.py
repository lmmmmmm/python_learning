# use type to judge Object type
print(type(123))
print(type(2.14))
print(type('abc'))
print(type(True))

# use isinstance() to judge object inheritance relationship
class Person(object):
    pass

class Man(Person):
    pass

class Woman(Person):
     pass
        
man = Man()
woman = Woman()
person = Person()
print(isinstance(person,Person))     
print(isinstance(man,Person))
print(isinstance(woman,Person))

# use dir() get one Object all property and function
print(dir('abc'))
