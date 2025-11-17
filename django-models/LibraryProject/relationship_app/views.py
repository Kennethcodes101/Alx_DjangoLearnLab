from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library
from .models import Book


# Create your views here.
# ------------------------------
# FUNCTION-BASED VIEW
# ------------------------------
def list_books(request):
    books = Book.objects.all()

    return render(request, "relationship_app/list_books.html", {"books": books})

# ------------------------------
# CLASS-BASED VIEW
# ------------------------------
def library_detail(request, library_id):
   
    library = get_object_or_404(Library, id=library_id)

    
    return render(request, "relationship_app/library_detail.html", {"library": library})
