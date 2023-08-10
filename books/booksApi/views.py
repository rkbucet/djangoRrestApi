from django.shortcuts import render
from booksApi.models import Books
from django.http import JsonResponse

# Create your views here.
def books_list(request):
    books = Books.objects.all()
    booksPython = list(books.values())
    return JsonResponse({
        'books': booksPython
    })