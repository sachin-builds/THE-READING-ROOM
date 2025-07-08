from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BindingChoices(models.TextChoices):
    PAPERBACK = 'PAPERBACK', 'Paperback'
    HARDCOVER = 'HARDCOVER', 'Hardcover'

class Book(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=8 ,decimal_places=2)
    stock = models.IntegerField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book-cover/')
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    binding = models.CharField(choices=BindingChoices.choices)

    def __str__(self):
        return self.title + ' by ' + self.author.author_name

class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_description = models.TextField()
    author_image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return self.author_name
    
class Genre(models.Model):
    genre_name = models.CharField(max_length=200)
    genre_description = models.TextField()
    
    def __str__(self):
        return self.genre_name
    
class Customer(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.user.get_full_name()
