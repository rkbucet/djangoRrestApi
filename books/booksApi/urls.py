from django.urls import include, path
from booksApi.views import books_list
from booksApi import views

urlpatterns = [
    path('', views.books_list)
]
