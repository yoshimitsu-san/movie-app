from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


class Another(View):

    books = Book.objects.all()

    output = ''

    for book in books:
        output += f"{book.title} (Book ID {book.id}) was published on {book.published}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')
