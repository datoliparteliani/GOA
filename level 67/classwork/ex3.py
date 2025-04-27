class Cat:
    def __init__(self, meow):
        self.meow = meow

class Dog(Cat):
    def __init__(self, meow):
        super().__init__(meow)
    def __str__(self):
        return f"{self.meow}"

dog = Dog("meow")
print(dog)