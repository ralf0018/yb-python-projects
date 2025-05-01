class libraryBookManager:
  #Constructor to initialize an empty book list, ready to store books
  def __init__(self):
    self.book = []
  
  # Method to add a book to the library
  def addBook(self,book):
    # add a book and show a message if the book is added successfully or not
    self.book.append(book)
    print(f"<{book}> added")

  
  # Method to show books in the library.
  def showBooks(self):
    # show a special message if there is no book
    if len(self.book) == 0:
      print("there isn't any book in the library")
    else:
    # show all the books
      print("Here is the book list:")
      for book in self.book:
        print(book)


# a test of libraryBookManager class
if __name__ == "__main__":
  lib = libraryBookManager()
  lib.showBooks()
  lib.addBook("Test")
  lib.showBooks()