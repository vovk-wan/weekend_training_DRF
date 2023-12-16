from rest_framework import serializers
from api.models import Author
from drf_yasg.utils import swagger_serializer_method


class OtherStuffSerializer(serializers.Serializer):
    pass


class AuthorSerializer(serializers.ModelSerializer):
    about = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'about')

    # пример хака документации метода сериализатора
    @swagger_serializer_method(serializer_or_field=OtherStuffSerializer())
    def get_about(self, obj: Author) -> str:
        return 'Еврей' if obj.last_name.endswith('ий') else 'Гой'
