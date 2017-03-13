from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author)
