from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionnaireListView.as_view(), name='questionnaire_list'),
    path('create/', views.QuestionnaireCreateView.as_view(), name='create_questionnaire'),
    path('update/<int:id>/', views.QuestionnaireUpdateView.as_view(), name='update_questionnaire'),
    path('delete/<int:id>/', views.QuestionnaireDeleteView.as_view(), name='delete_questionnaire'),
    path('detail/<int:id>/', views.QuestionnaireDetailView.as_view(), name='questionnaire_detail'),
]