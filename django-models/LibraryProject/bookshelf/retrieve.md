# Retrieve Books

# Retrieving the book
book = Book.objects.get(title="1984")

# Displaying book details
print(book.title, book.author, book.publication_year)


#Expected Outcome
1984 George Orwell 1949


