class Borrower:
    """Represents a person that can borrow a book"""

    newIDCode = 1  # class attribute

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.id = Borrower.newIDCode
        Borrower.newIDCode += 1  # increments this for each new instance of Borrower
        self.booksBorrowed = []

    def show_all_books(self):
        if len(self.booksBorrowed) == 0:
            print("There are currently zero borrowed books")
        else:
            print(f"{self.firstname} has borrowed the following books:")
            for b in self.booksBorrowed:
                b.show_title()

    def show_borrower_details(self):
        print(f"{self.firstname} {self.lastname} ID: {self.id}")


class Book:
    def __init__(self, title, author, code):
        self.title = title
        self.author = author
        self.code = code
        self.onLoan = False

    def show_title(self):
        print(f"Title: {self.title}")


class Library:
    def __init__(self):  # do not need to add empty attributes as arguments.
        self.all_borrowers = []
        self.all_books = []

    def add_book(self, book):
        self.all_books.append(book)

    def add_borrower(self, borrower):
        self.all_borrowers.append(borrower)

    def lend_book(self, book, borrower):
        if book.onLoan == False:
            print(f"Book loaned to {borrower.firstname} ")
            book.onLoan = True
            borrower.booksBorrowed.append(book)

        else:
            print("This cannot be loaned since it does not belong to this library.")


def main():
    ## Create some books ...
    book1 = Book('Kafkas motorbike', 'Bridget Jones', 1290)
    book2 = Book('Cooking with Custard', 'Jello Biafra', 1002)
    book3 = Book('History of Bagpipes', 'John Cairncross', 987)

    # Put the books in the library
    library = Library()  # Creates the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create some borrowers ...
    bor1 = Borrower('Kevin', 'Wilson')
    bor2 = Borrower('Rita', 'Shapiro')
    bor3 = Borrower('Max', 'Normal')

    library.add_borrower(bor1)
    library.add_borrower(bor2)
    library.add_borrower(bor3)

    # make some loans ...
    library.lend_book(borrower=bor1, book=book1)
    bor1.show_borrower_details()
    bor1.show_all_books()
    library.lend_book(borrower=bor2, book=book3)
    bor2.show_borrower_details()
    bor2.show_all_books()
    # Try to lend book3 out again ....
    library.lend_book(borrower=bor3,
                      book=book3)  # make sure arguements of the instance are in same order of initial contruction.


if __name__ == "__main__":
    main()


# can access methods from other classes once initiated.

