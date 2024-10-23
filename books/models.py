from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    published_date = models.DateField()
    language = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    