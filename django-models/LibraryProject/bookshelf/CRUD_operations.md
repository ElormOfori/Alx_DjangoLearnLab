#DOCUMENTATION OF EACH CRUD OPERATIONS

#1. Create a Book
from bookshelf.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verifying the creation
print(book)

#Expected Outcome 
<Book: 1984 by George Orwell (1949)>





#2. Retrieve the Book

from bookshelf.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verifying the creation
print(book)

#Expected Outcome
1984 George Orwell 1949






#3. Update the Book 

from bookshelf.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verifying the creation
print(book)

#Expected Outcome
Nineteen Eighty-Four






#4. Delete the Book

# Retrieving the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Deleting the book
book.delete()

# Verifying deletion
books = Book.objects.all()
print(books)

#Expected Outcome
<QuerySet []>  # This means the book no longer exists


