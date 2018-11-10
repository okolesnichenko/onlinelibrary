from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import AuthorForm
from .forms import BookForm
from .models import Author
from .models import Book
from django.forms import ModelForm

# Create your views here.
def show_all(request,  template_name = "weblibrary/all_lists.html"):
    authors = Author.objects.all()
    books = Book.objects.all()
    data = {}
    data['authors'] = authors
    data['books'] = books
    return render(request, template_name, data)

def author_create(request, template_name = "weblibrary/author_form.html"):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_lists')
    return render(request, template_name, {'form':form})

def author_edit(request, pk, template_name = "weblibrary/author_form.html"):
    author = get_object_or_404(Author, pk = pk)
    form = AuthorForm(request.POST or None, instance = author)
    if form.is_valid():
        form.save()
        return redirect('all_lists')
    return render(request, template_name, {'form':form})

def author_delete(request, pk, template_name = "weblibrary/delete.html"):
    author = get_object_or_404(Author, pk = pk)
    if request.method == 'POST':
        author.delete()
        return redirect('all_lists')
    return render(request, template_name, {"object": author})

def book_create(request, template_name = "weblibrary/book_form.html"):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_lists')
    return render(request, template_name, {'form':form})

def book_edit(request, pk, template_name = "weblibrary/book_form.html"):
    book = get_object_or_404(Book, pk = pk)
    form = BookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect('all_lists')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name = "weblibrary/delete.html"):
    book = get_object_or_404(Book, pk = pk)
    if request.method == 'POST':
        book.delete()
        return redirect('all_lists')
    return render(request, template_name, {"object": book})

def book_find(request, template_name = "weblibrary/book_find.html"):
    search = request.GET['search']
    books = Book.objects.filter(name = search)
    if request.method == 'GET':
        return render(request, template_name, {'books': books})
    return redirect('all_lists')    
     
