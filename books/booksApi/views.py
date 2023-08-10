from http.client import responses
from django.shortcuts import render
from booksApi.models import Books
from booksApi.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def books_list(request):
    books = Books.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)