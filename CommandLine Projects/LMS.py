class Library:
    def __init__(self, Books):
        self.BookList = Books
        self.took_books = []


    def displayBooks(self):
        print("\nThese Books are available: ")
        [print('-> ', i.capitalize()) for i in self.BookList]


    def display_Took_Books(self):
        print("\nYou had borrowed these books: ")
        [print('-> ', i.capitalize()) for i in self.took_books]


    def borrowBook(self, Book):
        if Book.lower() in self.BookList:
            print(f"You have got '{Book}' book\n")
            self.BookList.remove(Book.lower())
            self.took_books.append(Book.lower())
            
        else:
            print(f"This book is not available")
            self.displayBooks()


    def returnBook(self, Book):
        if Book.lower() in self.took_books:
            print(f"You have returned '{Book}' book\n")
            self.BookList.append(Book.lower())
            self.took_books.remove(Book.lower())

        else:
            print("You had not borrowed this book")
            self.display_Took_Books()



class Student:
    def requestBook(self):
        Book = input("\nEnter Name of the Book: ")
        return Book
    
    def returnBook(self):
        Book = input("\nEnter Name of the Book: ")
        return Book



if __name__ == "__main__":
    Books = ['python', 'c', 'c++', 'c#', 'java']
    library = Library(Books)
    student = Student()

    while True:
        n = input("\n1. Display Books\n2. Borrow Book\n3. Return Book\n4. Exit\n------> ")

        match n:
            case '1':
                library.displayBooks()

            case '2':
                library.borrowBook(student.requestBook())

            case '3':
                library.returnBook(student.returnBook())

            case '4':
                break

            case _:
                print("Wrong Input, Enter again...")