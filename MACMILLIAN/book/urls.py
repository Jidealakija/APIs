from django.urls import path
from .views import display_books,get_single_book, create_single_book, update_single_book

urlpatterns = [
    path('', display_books ,name='all'),
    path('create/', create_single_book, name='create_book'),
    path('<slug:slug>/update/', update_single_book, name='update_book'),
    path('<slug:slug_passed_in>/', get_single_book, name='single_book')

]