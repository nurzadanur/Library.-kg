from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    pages = models.IntegerField()
    price = models.FloatField()
    published = models.DateField()
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()

    def __str__(self):
        return self.title