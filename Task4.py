class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")

book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

print("Book 1 Details:")
book1.describe()
print("\nBook 2 Details:")
book2.describe()
print("\nBook 3 Details:")
book3.describe()
