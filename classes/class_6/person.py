class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHello(self):
        print("Hello, my name is %s" % self.name)

p1 = Person("john", 18)

# print(p1.name, p1.age)
p1.sayHello()