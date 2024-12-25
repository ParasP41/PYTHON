class Library:
    def __init__(self):
        self.no_of_books = 0;
        self.books = [];

    def display_books(self, book):
        self.books=book;

        self.no_of_books=len(self.books);
        print(f"The number of books in library is {self.no_of_books} and the books are");
        for book in self.books:
            print(book)

a=Library();
a.display_books(["Hunting Adline","Slient Patient","I Hear You","Then She Was Gone"]);



#///////////////////////////////////////////////

        
# class Library:
#   def __init__(self):
#     self.noBooks = 0
#     self.books = []
    
#   def addBook(self, book):
#     self.books.append(book)
#     self.noBooks = len(self.books)

#   def showInfo(self):
#     print(f"The library has {self.noBooks} books. The books are")
#     for book in self.books:
#       print(book)


# l1 = Library()
# l1.addBook("Harry Potter1")
# l1.addBook("Harry Potter2")
# l1.addBook("Harry Potter3")
# l1.showInfo()
    
  
     
