from django.urls import path

from .views import BookDeleteView, BookListView, BookCreateView, BookUpdateView


urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("add", BookCreateView.as_view(), name="add_book"),
    path("update/<uuid:pk>", BookUpdateView.as_view(), name="update_book"),
    path("delete/<uuid:pk>", BookDeleteView.as_view(), name="delete_book")
]
