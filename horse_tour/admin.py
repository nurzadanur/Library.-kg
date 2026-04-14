from django.contrib import admin
from .models import Location, Person, Comment, CategoryTour

admin.site.register(Location)
admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(CategoryTour)