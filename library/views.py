import datetime

from django.http import HttpResponse
from rest_framework.status import *
from rest_framework.views import APIView
from library.models import *
from django.core.serializers import serialize
from datetime import datetime
import json


class CategoryView(APIView):
    def get(self, request, category_id=None):
        if category_id:
            if Category.objects.filter(pk=category_id).exists():
                category_response = Category.objects.filter(pk=category_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Category not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            category_response = list(Category.objects.all())

        category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=category_response,
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

    def put(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        category.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category updated successful'}),
                            status=HTTP_404_NOT_FOUND)

    def delete(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        category.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category deleted successful'}),
                            status=HTTP_200_OK)


class AuthorView(APIView):
    def get(self, request, author_id=None):
        if author_id:
            if Author.objects.filter(pk=author_id).exists():
                author_response = Author.objects.filter(pk=author_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            author_response = list(Author.objects.all())

        author_response = serialize('json', author_response)
        return HttpResponse(content_type='application/json',
                            content=author_response,
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

    def put(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        author.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author updated successful'}),
                            status=HTTP_404_NOT_FOUND)

    def delete(self, request, author_id):
        author = Category.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        author.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author deleted successful'}),
                            status=HTTP_200_OK)


class PartnerView(APIView):
    def get(self, request, partner_id=None):
        if partner_id:
            if Partner.objects.filter(pk=partner_id).exists():
                partner_response = Partner.objects.filter(pk=partner_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Partner not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            partner_response = list(Partner.objects.all())

        partner_response = serialize('json', partner_response)
        return HttpResponse(content_type='application/json',
                            content=partner_response,
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

    def put(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.now()
        partner.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner updated successful'}),
                            status=HTTP_404_NOT_FOUND)

    def delete(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        partner.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner deleted successful'}),
                            status=HTTP_200_OK)


class BookView(APIView):
    def get(self, request, book_id=None):
        if book_id:
            if Book.objects.filter(pk=book_id).exists():
                book_response = Book.objects.filter(pk=book_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Book not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            book_response = list(Partner.objects.all())

        book_response = serialize('json', book_response)
        return HttpResponse(content_type='application/json',
                            content=book_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['category'] = Category.objects.get(pk=body['category'])
        body['author'] = Author.objects.get(pk=body['author'])
        book, created = Book.objects.get_or_create(**body)
        if created:
            book.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book alredy exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
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

    def delete(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        book.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book deleted successful'}),
                            status=HTTP_200_OK)