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
    books = []
    author_n = list(Author.objects.filter(name = search))
    author_s = list(Author.objects.filter(surname = search))
    book_name = list(Book.objects.filter(name = search))
    # Full author name + surname
    x = search.split()
    if(len(x) == 2):
        authors = list(Author.objects.filter(name = x[0], surname = x[1]))
        while(len(authors) != 0):
            book_author = list(Book.objects.filter(author = authors.pop()))
            books += book_author
    # Author name
    while(len(author_n) != 0):
        book_author = list(Book.objects.filter(author = author_n.pop()))
        books += book_author
    # Author surname
    while(len(author_s) != 0):
        book_author = list(Book.objects.filter(author = author_s.pop()))
        books += book_author
    # Book name
    if(len(book_name) != 0):
        books += book_name
    if request.method == 'GET':
        return render(request, template_name, {'books': books})
    return redirect('all_lists')    
     
