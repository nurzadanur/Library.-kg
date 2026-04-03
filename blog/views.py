from django.shortcuts import render
from django.http import HttpResponse

def first_message_view(request):
    if request.method == "GET":
        return HttpResponse("1. Марк Твен\n«Через двадцать лет вы будете больше разочарованы тем, чего не сделали, чем тем, что сделали.»" \
        "2. Джордж Оруэлл\n«Свобода — это право говорить людям то, что они не хотят слышать.»" \
        "3. Виктор Гюго\n«Даже самая тёмная ночь закончится, и взойдёт солнце.»")
#def second_message_view(request):
    #if request.method == "GET":
        #return HttpResponse("Джордж Оруэлл\n«Свобода — это право говорить людям то, что они не хотят слышать.»")
#def third_message_view(request):
    #if request.method == "GET":
        #return HttpResponse("Виктор Гюго\n«Даже самая тёмная ночь закончится, и взойдёт солнце.»")
