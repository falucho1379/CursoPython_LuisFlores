from django.db import models

# Definimos el modelo para la entidad Category
class Category(models.Model):
    name = models.CharField(max_length=60)
    recommended_age = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


# Definimos el modelo para la entidad Language
class Language(models.Model):
    language = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


# Definimos el modelo para la entidad Author
class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


# Definimos el modelo para la entidad Book
class Book(models.Model):
    title = models.CharField(max_length=60)
    pages = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


# Definimos el modelo para la entidad Partner
class Partner(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dni = models.CharField(max_length=8)
    address = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


# Definimos el modelo para la entidad BookLoan
class BookLoan(models.Model):
    status = models.CharField(max_length=30)
    return_date = models.DateField(null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
