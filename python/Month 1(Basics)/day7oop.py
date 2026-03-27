class Libarary:
    def __init__(self,books):
        self.books = books
    def show_books(self):
        print("Available Books: ")
        for book in self.books:
            print(book)
    def borrow_book(self,book_name):
        if book_name in self.books:
            print("You Borrow:",book_name)
            self.books.remove(book_name)
        else:
            print("Book not aviable")
    def return_book(self,book_name):
        self.books.append(book_name)
        print("book returned: ",book_name)

lib = Libarary(["python","Ai","Data"])
lib.show_books()
lib.borrow_book("python")
lib.borrow_book("python")
lib.show_books()
# lib.return_book("python")
# lib.show_books()


        