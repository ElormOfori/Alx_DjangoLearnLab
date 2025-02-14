from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns in admin panel
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Add a filter for publication year

admin.site.register(Book, BookAdmin)  # Register the Book model with these settings



