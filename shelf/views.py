from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Author, Book, Publisher
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class MainPageView(TemplateView):
    template_name = 'index.html'

index_view = MainPageView.as_view()

#def index_view(request, *args, **kwargs):
      #  return HttpResponse('OK - funkcja')

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class PublisherListView(ListView):
    model = Publisher