class Library:
    def __init__(self, ListOfBooks):
        self.availablebooks = ListOfBooks

    def show_books(self):
        print("available books are: ")
        for book in self.availablebooks:
            print(book)

    def lend_book(self, borrow_book):
        if borrow_book in self.availablebooks:
            print("you have borrowed the book")
            self.availablebooks.remove(borrow_book)
        else:
            print("sorry that book is not available")

    def book_return(self, return_book):
        self.availablebooks.append(return_book)
        print("thankyou for returning the book")

class Customer:
    def borrow_book(self):
        print("enter name of the book you would like borrow: ")
        self.book = input()
        return self.book
    def return_book(self):
        print("enter name of the book you would like return: ")
        self.book = input()
        return self.book
    

library = Library(["lotr", "lotr2", "lotr3"])
customer = Customer()
while True:
    print("enter 1 to show all books available")
    print("enter 2 to request an available book")
    print("enter 3 to return a book")
    print("enter 4 to exit")
    user_choice = int(input())
    if user_choice is 1:
        library.show_books()
    elif user_choice is 2:
        requested_book = customer.borrow_book()
        library.lend_book(requested_book)
    elif user_choice is 3:
        return_book = customer.return_book()
        library.book_return(return_book)
    elif user_choice is 4:
        quit()



