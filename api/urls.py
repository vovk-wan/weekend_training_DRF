from rest_framework.routers import DefaultRouter
from api.viewsets.books import BooksViewSet, ListBooksViewSet
from api.viewsets.authors import AuthorViewSet


router = DefaultRouter()

router.register('books', BooksViewSet)
router.register('authors', AuthorViewSet)
router.register('read-books', ListBooksViewSet)
