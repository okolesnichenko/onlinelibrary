"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weblibrary import views

urlpatterns = [
    path('', views.show_all, name='all_lists'),
    path('create_author', views.author_create, name = 'author_create'),
    path('edit_author/<int:pk>', views.author_edit, name = 'author_edit'),
    path('delete_author/<int:pk>', views.author_delete, name = 'author_delete'),
    path('create_book', views.book_create, name = 'book_create'),
    path('edit_book/<int:pk>', views.book_edit, name = 'book_edit'),
    path('delete_book/<int:pk>', views.book_delete, name = 'book_delete'),
    path('find_book/<str:search>', views.book_find, name = 'book_find'),
]
