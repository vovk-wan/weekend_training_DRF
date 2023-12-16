from rest_framework import viewsets
from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from api.serializers.books import (
    BookSerializer, WriteBookSerializer, SelectSerializerMixin,
    RetrieveOkSerializer, RetrieveErrorSerializer
)
from api.models import Books

CUSTOM_PARAM = openapi.Parameter(
    'custom_param',
    openapi.IN_QUERY,
    description='Пример параметра querystring',
    type=openapi.TYPE_STRING,
    enum=['еврей', 'гой'],
    required=False
)

CUSTOM_PARAM2 = openapi.Parameter(
    'просто поле',
    openapi.IN_QUERY,
    description='Пример параметра querystring',
    type=openapi.TYPE_STRING,
    required=False
)


class BooksViewSet(SelectSerializerMixin, viewsets.ModelViewSet):
    """ **Мой первый вьювсет**"""
    queryset = Books.objects.prefetch_related('author').all()
    serializer_class = BookSerializer
    create_serializer_class = WriteBookSerializer


class ListBooksViewSet(viewsets.ReadOnlyModelViewSet):
    """ **Мой второй вьювсет**"""
    queryset = Books.objects.prefetch_related('author').all()
    serializer_class = BookSerializer

    @swagger_auto_schema(manual_parameters=[CUSTOM_PARAM, CUSTOM_PARAM2])
    def list(self, request: Request, *args, **kwargs):
        print(f'{request.query_params=}')
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Пример получения Retrieve',
        responses={
            200: RetrieveOkSerializer(),
            400: RetrieveErrorSerializer()
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

