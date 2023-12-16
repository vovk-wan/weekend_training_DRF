from rest_framework import serializers
from api.serializers.authors import AuthorSerializer
from api.models import Books


class SelectSerializerMixin:
    serializer_class = None
    list_serializer_class = None
    retrieve_serializer_class = None
    update_serializer_class = None
    partial_update_serializer_class = None
    create_serializer_class = None

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using self.serializer_class.
        """
        assert self.serializer_class is not None, (
            '"%s" should either include a serializer_class attribute, '
            'or override the get_serializer_class() method.' % self.__class__.__name__)
        return getattr(self, f'{self.action}_serializer_class') or self.serializer_class


class RetrieveOkSerializer(serializers.Serializer):
    books = serializers.CharField(default='Библия')


class RetrieveErrorSerializer(serializers.Serializer):
    detail = serializers.CharField(default='других книг нет')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Books
        fields = ('title', 'author')


class WriteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
