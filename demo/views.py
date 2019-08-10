from django.shortcuts import render
from django.views import View
from .models import Book


def first(request):

    books = Book.objects.all()

    return render(request, 'first_temp.html', {'books': books})
