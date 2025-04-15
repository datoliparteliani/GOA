class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return "Woof!"

dog = Dog("jeka", 3)
print(dog.bark())