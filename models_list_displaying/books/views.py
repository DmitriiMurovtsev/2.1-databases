from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book


def books_view(request):
    books = [{'name': c.name, 'author': c.author, 'pub_date': c.pub_date} for c in Book.objects.all()]
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def books_view_date(request, pub_date):
    books = [{'name': c.name, 'author': c.author, 'pub_date': c.pub_date} for c in Book.objects.all()
             if str(c.pub_date) == pub_date]
    template = 'books/books_list_pagi.html'
    context = {'books': books}
    return render(request, template, context)
