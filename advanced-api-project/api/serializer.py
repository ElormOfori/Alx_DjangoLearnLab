from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Fields:
    - id: Auto-generated primary key.
    - title: Title of the book.
    - publication_year: Year the book was published.
    - author: ForeignKey linking to the Author model.

    Validation:
    - Ensures `publication_year` is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year','author']

    def validate_publication_year(self, value):
        """Custom validation to check the publication year is not in the future."""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Fields:
    - id: Auto-generated primary key.
    - name: Name of the author.
    - books: Nested serialization of related books using BookSerializer.

    Relationships:
    - Uses the BookSerializer to dynamically serialize related books.
    - The `many=True` argument ensures multiple books are included in the serialized response.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']