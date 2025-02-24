
# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()  #Ensure this query is present
    return render(request, "relationship_app/list_books.html", {"books": books})  #Ensure correct template is used

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  #Ensure correct template is used
    context_object_name = "library"  # Allows template to use {{ library }} instead of {{ object }}

# Create your views here.
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  #Ensure this query is present
    return render(request, "relationship_app/list_books.html", {"books": books})  #Ensure correct template is used

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  #Ensure correct template is used
    context_object_name = "library"  # Allows template to use {{ library }} instead of {{ object }}