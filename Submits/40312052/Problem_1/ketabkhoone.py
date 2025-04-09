class Book :
    def __init__(self , name , author) :
        self.name = name
        self.author = author
        self.status = "avalible"

    def borrow(self):
        if self.status == "avalible" :
            print("borrowed")
            self.status = "not avalible"
        else :
            print("there is no such book")

    def return_book(self) :
        self.status = "avalible"
        print("returned")

    def get_ditails(self , name) :
        print(f"{name} by {self.author} is {self.status}")

class Library() :
    def __init__(self) :
        self.books = list()

    def add_book(self , book) :
        print("book added")
        self.books.append(book)

    def borrow_book(self , name) :
        for i in self.books :
            if i.name == name :
                i.borrow(name)

    def return_book(self, name) :
        for i in self.books :
            if i.name == name :
                i.return_book(name)

    def show_books(self) :
        for i in self.books :
            print(f"{i.name} by {i.author} is {i.status}")

library = Library()
for i in range(2) :
    x = input().split(" ")
    if "ADD" in x :
        book = Book(x[1] , x[2])
        library.add_book(book)
    elif "BORROW" in x :
        library.borrow_book(x[1])
    elif "RETURN" in x :
        library.borrow_book(x[1])
    elif "SHOW" in x :
        library.show_books()
