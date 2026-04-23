from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionnaire_list, name='questionnaire_list'),
    path('create/', views.create_questionnaire, name='create_questionnaire'),
    path('update/<int:id>/', views.update_questionnaire, name='update_questionnaire'),
    path('delete/<int:id>/', views.delete_questionnaire, name='delete_questionnaire'),
]