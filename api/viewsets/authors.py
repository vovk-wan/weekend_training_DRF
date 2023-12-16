from rest_framework.viewsets import ModelViewSet
from api.serializers.authors import AuthorSerializer
from api.models import Author


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
