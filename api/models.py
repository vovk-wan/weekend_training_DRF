from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author, related_name='books')