from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list),
    path('book/<int:id>/', views.book_detail),
]