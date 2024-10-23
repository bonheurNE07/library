from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    published_date = models.DateField(default=timezone.now)
    language = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    