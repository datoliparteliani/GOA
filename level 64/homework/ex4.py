class Rectange:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rectange = Rectange(5, 10)
print(rectange.area())