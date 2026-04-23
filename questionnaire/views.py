from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire
from .forms import QuestionnaireForm


def create_questionnaire(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('questionnaire_list')
    else:
        form = QuestionnaireForm()

    return render(request, "create_questionnaire.html", {"form": form})


def questionnaire_list(request):
    data = Questionnaire.objects.all().order_by("-id")
    return render(request, "questionnaire_list.html", {"data": data})


def update_questionnaire(request, id):
    obj = get_object_or_404(Questionnaire, id=id)

    if request.method == "POST":
        form = QuestionnaireForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('questionnaire_list')
    else:
        form = QuestionnaireForm(instance=obj)

    return render(request, "update_questionnaire.html", {"form": form})


def delete_questionnaire(request, id):
    obj = get_object_or_404(Questionnaire, id=id)
    obj.delete()
    return redirect('questionnaire_list')