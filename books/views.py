from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Book


class BookBaseView(View):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("book_list")


class BookListView(BookBaseView, ListView):
    context_object_name = "book_list"
    template_name = "book_list.html"


class BookCreateView(BookBaseView, CreateView):
    template_name = "book_form.html"


class BookUpdateView(BookBaseView, UpdateView):
    template_name = "book_form.html"


class BookDeleteView(BookBaseView, DeleteView):
    template_name = "delete_book.html"
