"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from library.views import *


urlpatterns = [
    path('library/admin/', admin.site.urls),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<parameter>', CategoryView.as_view(), name='categories'),
    path('authors/', AuthorView.as_view(), name='authors'),
    path('authors/<parameter>', AuthorView.as_view(), name='authors'),
    path('partners/', PartnerView.as_view(), name='partners'),
    path('partners/<parameter>', PartnerView.as_view(), name='partners'),
    path('books/', BookView.as_view(), name='books'),
    path('books/<parameter>', BookView.as_view(), name='books'),
    path('languages/', LanguageView.as_view(), name='languages'),
    path('languages/<parameter>', LanguageView.as_view(), name='languages'),
    path('book-loans/', BookLoanView.as_view(), name='book-loans'),
    path('book-loans/<parameter>', BookLoanView.as_view(), name='book-loans'),
]
