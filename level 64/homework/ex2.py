class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        if self.grade > 5:
            return True
        return False

p1 = Student("davit", "liparteliani", 10)
print(p1.is_passing())