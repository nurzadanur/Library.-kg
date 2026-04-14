from django.db import models


class CategoryTour(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(CategoryTour, blank=True)

    def __str__(self):
        return f"{self.title} --- {', '.join(i.name for i in self.categories.all())}"


class Person(models.Model):
    name = models.CharField(max_length=100, default='Ivanov Ivan')
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -> {self.location}"


class Comment(models.Model):
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.location} --- {self.text[:20]}"

