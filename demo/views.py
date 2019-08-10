from django.shortcuts import render
from django.views import View
from .models import Book


def first(request):
    return render(request, 'first_temp.html')
