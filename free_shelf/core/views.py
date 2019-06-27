from django.shortcuts import render
from .models import Book, Category
from django.views import generic
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
