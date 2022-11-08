from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookInstance, Language, Genre
from django.views.generic import CreateView, DetailView, ListView


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreate(CreateView):
    model = Book
    fields = '__all__'

    # success_url =


class BookDetail(DetailView):
    # mapping = model_detail.html
    model = Book


class BookList(ListView):

    model = Book
