class MyClass:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f"My name is {self.name}, My surname is {self.surname}, I am {self.age} years old"

p1 = MyClass("Dato", "Liparteliani", 16)
print(p1)