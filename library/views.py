import datetime

from django.http import HttpResponse
from rest_framework.status import *
from rest_framework.views import APIView
from library.models import *
from django.core.serializers import serialize
from datetime import datetime
import json


class CategoryView(APIView):
    def get(self, request, parameter=None):

        if parameter:
            if parameter.isdigit():
                if Category.objects.filter(pk=int(parameter)).exists():
                    category_response = list(Category.objects.filter(pk=int(parameter)).values("id", "name", "recommended_age"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Category not found'}),
                                        status=HTTP_404_NOT_FOUND)
            else:
                if parameter.isalpha():
                    category_response = list(Category.objects.filter(name__icontains=parameter).values("id", "name", "recommended_age"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Parameter of Category is not valid'}),
                                        status=HTTP_400_BAD_REQUEST)
        else:
            category_response = list(Category.objects.all().values("id", "name", "recommended_age"))

        #category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=json.dumps(category_response),
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        category, created = Category.objects.get_or_create(**body)
        if created:
            category.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category alredy exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                category = Category.objects.filter(pk=int(parameter))
                if not category.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'PK Category not found'}),
                                        status=HTTP_404_NOT_FOUND)
                body = json.loads(request.body)
                body['last_update'] = datetime.now()
                category.update(**body)
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Category updated successful'}),
                                    status=HTTP_404_NOT_FOUND)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Category is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)

    def delete(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                category = Category.objects.filter(pk=int(parameter))
                if not category.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Category not found'}),
                                        status=HTTP_404_NOT_FOUND)
                category.delete()
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Category deleted successful'}),
                                    status=HTTP_200_OK)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Category is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)


class AuthorView(APIView):
    def get(self, request, parameter=None):

        if parameter:
            if parameter.isdigit():
                if Author.objects.filter(pk=int(parameter)).exists():
                    author_response = list(Author.objects.filter(pk=int(parameter)).values("id", "first_name",
                                                                                           "last_name"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Author not found'}),
                                        status=HTTP_404_NOT_FOUND)
            else:
                if parameter.isalpha():
                    author_response = list(Author.objects.filter(last_name__icontains=parameter).values("id",
                                                                                                        "first_name",
                                                                                                        "last_name"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'PK of Author is not valid'}),
                                        status=HTTP_400_BAD_REQUEST)
        else:
            author_response = list(Author.objects.all().values("id", "first_name", "last_name"))

        # category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=json.dumps(author_response),
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        author, created = Author.objects.get_or_create(**body)
        if created:
            author.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author alredy exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                author = Author.objects.filter(pk=int(parameter))
                if not author.exists():
                        return HttpResponse(content_type='application/json',
                                            content=json.dumps({'detail': 'PK Author not found'}),
                                            status=HTTP_404_NOT_FOUND)
                body = json.loads(request.body)
                body['last_update'] = datetime.now()
                author.update(**body)
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author updated successful'}),
                                    status=HTTP_404_NOT_FOUND)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Author is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)

    def delete(self, request, parameter=None):

        if parameter:
            if parameter.isdigit():
                author = Category.objects.filter(pk=int(parameter))
                if not author.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Author not found'}),
                                        status=HTTP_404_NOT_FOUND)
                author.delete()
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author deleted successful'}),
                                    status=HTTP_200_OK)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Author is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)


class PartnerView(APIView):
    def get(self, request, parameter=None):

        if parameter:
            if parameter.isdigit():
                if Partner.objects.filter(pk=int(parameter)).exists():
                    partner_response = list(Partner.objects.filter(pk=int(parameter)).values("id", "first_name",
                                                                                             "last_name", "dni",
                                                                                             "address"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Partner not found'}),
                                        status=HTTP_404_NOT_FOUND)
            else:
                if parameter.isalpha():
                    partner_response = list(Partner.objects.filter(last_name__icontains=parameter).values("id", "first_name",
                                                                                                          "last_name", "dni",
                                                                                                          "address"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'PK of Partner is not valid'}),
                                        status=HTTP_400_BAD_REQUEST)
        else:
            partner_response = list(Partner.objects.all().values("id", "first_name", "last_name", "dni", "address"))

        # category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=json.dumps(partner_response),
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        partner, created = Partner.objects.get_or_create(**body)
        if created:
            partner.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner alredy exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                partner = Partner.objects.filter(pk=int(parameter))
                if not partner.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'PK Partner not found'}),
                                        status=HTTP_404_NOT_FOUND)
                body = json.loads(request.body)
                body['last_update'] = datetime.now()
                partner.update(**body)
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Partner updated successful'}),
                                    status=HTTP_404_NOT_FOUND)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Partner is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)

    def delete(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                partner = Partner.objects.filter(pk=int(parameter))
                if not partner.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'PK Partner not found'}),
                                        status=HTTP_404_NOT_FOUND)
                partner.delete()
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Partner deleted successful'}),
                                    status=HTTP_200_OK)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Partner is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)


class BookView(APIView):
    def get(self, request, parameter=None):

        if parameter:
            if parameter.isdigit():
                if Book.objects.filter(pk=int(parameter)).exists():
                    book_response = list(Book.objects.filter(pk=int(parameter)).values("id", "title", "pages", "author",
                                                                                       "category", "language"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Book not found'}),
                                        status=HTTP_404_NOT_FOUND)
            else:
                if parameter.isalpha():
                    book_response = list(Book.objects.filter(author__last_name=parameter).values("id", "title",
                                                                                                 "pages", "author",
                                                                                                 "category", "language"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'PK of Book is not valid'}),
                                        status=HTTP_400_BAD_REQUEST)
        else:
            book_response = list(Book.objects.all().values("id", "title", "pages", "author",
                                                           "category", "language"))

        # category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=json.dumps(book_response),
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['author'] = Author.objects.get(pk=body['author'])
        body['category'] = Category.objects.get(pk=body['category'])
        body['language'] = Language.objects.get(pk=body['language'])
        book, created = Book.objects.get_or_create(**body)
        if created:
            book.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book alredy exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                book = Book.objects.filter(pk=int(parameter))
                if not book.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Book not found'}),
                                        status=HTTP_404_NOT_FOUND)
                body = json.loads(request.body)
                body['last_update'] = datetime.now()
                book.update(**body)
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book updated successful'}),
                                    status=HTTP_404_NOT_FOUND)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Book is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)

    def delete(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                book = Book.objects.filter(pk=int(parameter))
                if not book.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Book not found'}),
                                        status=HTTP_404_NOT_FOUND)
                book.delete()
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book deleted successful'}),
                                    status=HTTP_200_OK)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Book is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)


class LanguageView(APIView):
    def get(self, request, parameter=None):

        if parameter:
            if parameter.isdigit():
                if Language.objects.filter(pk=int(parameter)).exists():
                    language_response = list(Language.objects.filter(pk=int(parameter)).values("id", "language"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Language not found'}),
                                        status=HTTP_404_NOT_FOUND)
            else:
                if parameter.isalpha():
                    language_response = list(Language.objects.filter(language__icontains=parameter).values("id", "language"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Parameter of Language is not valid'}),
                                        status=HTTP_400_BAD_REQUEST)
        else:
            language_response = list(Language.objects.all().values("id", "language"))

        # category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=json.dumps(language_response),
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        language, created = Language.objects.get_or_create(**body)
        if created:
            language.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Language created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Language alredy exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                language = Language.objects.filter(pk=int(parameter))
                if not language.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Language not found'}),
                                        status=HTTP_404_NOT_FOUND)
                body = json.loads(request.body)
                body['last_update'] = datetime.now()
                language.update(**body)
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Language updated successful'}),
                                    status=HTTP_404_NOT_FOUND)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Language is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)

    def delete(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                language = Language.objects.filter(pk=int(parameter))
                if not language.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Language not found'}),
                                        status=HTTP_404_NOT_FOUND)
                language.delete()
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Language deleted successful'}),
                                    status=HTTP_200_OK)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Language is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)


class BookLoanView(APIView):
    def get(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                if BookLoan.objects.filter(partner__dni=parameter).exists():
                    book_loan_response = list(BookLoan.objects.filter(partner__dni=parameter).values("id", "status",
                                                                                                     "book", "partner"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'DNI Partner not found'}),
                                        status=HTTP_404_NOT_FOUND)
            else:
                if parameter.isalpha():
                    book_loan_response = list(BookLoan.objects.filter(status__exact=parameter).values("id", "status",
                                                                                                      "book", "partner"))
                else:
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Parameter of Book Loan is not valid'}),
                                        status=HTTP_400_BAD_REQUEST)
        else:
            book_loan_response = list(BookLoan.objects.all().values("id", "status", "book", "partner"))

        # category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=json.dumps(book_loan_response),
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['book'] = Book.objects.get(pk=body['book'])
        body['partner'] = Partner.objects.get(pk=body['partner'])
        book_loan, created = BookLoan.objects.get_or_create(**body)
        if created:
            book_loan.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book Loan created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book Loan alredy exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                book_loan = BookLoan.objects.filter(pk=int(parameter))
                if not book_loan.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Book Loan not found'}),
                                        status=HTTP_404_NOT_FOUND)
                body = json.loads(request.body)
                body['last_update'] = datetime.now()
                book_loan.update(**body)
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book Loan updated successful'}),
                                    status=HTTP_404_NOT_FOUND)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Book Loan is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)

    def delete(self, request, parameter=None):
        if parameter:
            if parameter.isdigit():
                book_loan = BookLoan.objects.filter(pk=int(parameter))
                if not book_loan.exists():
                    return HttpResponse(content_type='application/json',
                                        content=json.dumps({'detail': 'Book Loan not found'}),
                                        status=HTTP_404_NOT_FOUND)
                book_loan.delete()
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book Loan deleted successful'}),
                                    status=HTTP_200_OK)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'PK of Book Loan is not valid'}),
                                    status=HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'PK Parameter is required'}),
                                status=HTTP_400_BAD_REQUEST)
