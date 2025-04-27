class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Saxeli: {self.name}. Gvari: {self.surname}."

p1 = Person("Levani", "Liparteliani")
print(p1)