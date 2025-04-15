class MyCat:
    cat = "კატა"

p1 = MyCat()

# print(p1.cat)

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname} {self.age}"
    
    def my_name(self):
        return f"chemi saxelia {self.name}"
    
    def my_surname(self):
        return f"chemi gvaria {self.surname}"
    
    def my_age(self):
        return f"var {self.age} wlis"

p1 = Human("davit", "liparteliani", 16)
print(p1)