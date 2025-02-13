# Delete Book

```python
from bookshelf.models import Book


# Fetch the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)


#Expected Outcome
<QuerySet []>  # This means the book no longer exists

