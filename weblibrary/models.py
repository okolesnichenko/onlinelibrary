from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)
    def __str__(self):
        return self.name + ' ' + self.surname 

class Book(models.Model):
    name = models.CharField(max_length = 30)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    def __str__(self):
        return self.name 
    
