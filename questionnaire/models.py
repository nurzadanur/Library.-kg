from django.db import models


class Questionnaire(models.Model):
    full_name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    education = models.CharField(max_length=150)
    hobby = models.TextField()

    experience_years = models.IntegerField()

    photo = models.ImageField(upload_to='photos/')
    document = models.FileField(upload_to='documents/')

    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name