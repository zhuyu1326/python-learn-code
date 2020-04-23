class Animal(object):
    def run(self):
        print('Animal is running......')

    def run_twice(animal):
        animal.run()
        animal.run()

    '''
    此处的animal如果都换成self效果一样，
    在类中定义的函数（方法）第一个参数
    永远是实例变量self，并且调用时，不
    用传递该参数，故此处animal=self
    '''

class Dog(Animal):
    def run(self):
        print('Dog is running....')

class Cat(Animal):
    def run(self):
        print('Cat is running....')


a = Animal()
b = Dog()
c = Cat()

a.run_twice()
b.run_twice()
c.run_twice()

