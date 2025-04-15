class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"{self.title} {self.author} {self.year}"
    
book = Book("The Hound of the Baskervilles", "Arthur Conan Doyle", 1902)
print(book.info())