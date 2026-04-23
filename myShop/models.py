from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    university = models.CharField(max_length=150)
    faculty = models.CharField(max_length=150)

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    passport_file = models.FileField(upload_to='passports/', null=True, blank=True)