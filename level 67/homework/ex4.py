class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject
    def introduce(self):
        return f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}."
    
p1 = Student("Dato", 10, "English")
print(p1.introduce())