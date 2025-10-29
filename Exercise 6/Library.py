class Library:
    def __init__(self, name):
        # Instance variables
        self.name = name
        self.books = []  # List to store book names

    def add_book(self, book_name):
        """Add a new book to the library."""
        self.books.append(book_name)
        print(f"'{book_name}' has been added to the library.")

    def show_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books available in the library.")
        else:
            print(f"\nBooks in {self.name}:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def get_book_count(self):
        """Return the number of books in the library."""
        return len(self.books)


# -----------------------------
# Creating a Library object
# -----------------------------
my_library = Library("City Central Library")

# Adding books
my_library.add_book("Harry Potter")
my_library.add_book("The Hobbit")
my_library.add_book("Python Programming")

# Showing all books
my_library.show_books()

# Getting total number of books
print(f"\nTotal number of books: {my_library.get_book_count()}")

# ⚠️ This data will be lost when the program stops
# If you run the program again, the library will be empty
