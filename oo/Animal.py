class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass


dog = Dog()
cat = Cat()
dog.run()
cat.run()


print(isinstance(dog, Animal))
print(isinstance(dog, Dog))