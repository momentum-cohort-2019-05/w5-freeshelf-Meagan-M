from django.shortcuts import render
from core.models import Book, Category
from django.views import generic
from django.http import HttpResponse

# Create your views here.
def index(request):
    '''View function for home page of site'''

    books = Book.objects.all()
    
    # Available books
    num_instances_available = Book.objects.filter(status__exact)

    context = {
        'books' : books,
        'num_instances_available' : num_instances_available,
    }
    return render(request, 'index.html', context=context)
