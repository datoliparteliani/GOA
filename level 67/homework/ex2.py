class Car:
    def __init__(self, d, s):
        self.d = d
        self.s = s
    def drive(self):
        return self.d
    def stop(self):
        return self.s

car = Car("The car is driving", "The car has stopped")
print(f"{car.drive()}. {car.stop()}.")