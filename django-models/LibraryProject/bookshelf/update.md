# Update Book Title


# Fetch the book
book = Book.objects.get(title="1984")

# Update title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
updated_book = Book.objects.get(author="George Orwell")
print(updated_book.title)


#Expected Outcome
Nineteen Eighty-Four

