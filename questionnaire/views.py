from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Questionnaire
from .forms import QuestionnaireForm


class QuestionnaireCreateView(CreateView):
    model = Questionnaire
    form_class = QuestionnaireForm
    template_name = "create_questionnaire.html"
    success_url = '/questionnaires/'


class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = "questionnaire_list.html"
    context_object_name = "data"
    ordering = ['-id']


class QuestionnaireUpdateView(UpdateView):
    model = Questionnaire
    form_class = QuestionnaireForm
    template_name = "update_questionnaire.html"
    pk_url_kwarg = "id"
    success_url = '/questionnaires/'


class QuestionnaireDeleteView(DeleteView):
    model = Questionnaire
    template_name = "questionnaire_delete.html"
    pk_url_kwarg = "id"
    success_url = '/questionnaires/'


class QuestionnaireDetailView(DetailView):
    model = Questionnaire
    template_name = "questionnaire_detail.html"
    context_object_name = "obj"
    pk_url_kwarg = "id"

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj