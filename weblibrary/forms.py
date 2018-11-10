from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Author
from .models import Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname']
        labels = {
            'name': _('Имя'),
            'surname':_('Фамилия'),
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']
