from django.contrib import admin
from library.models import Category, Language, Author, Book, BookLoan

admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookLoan)
