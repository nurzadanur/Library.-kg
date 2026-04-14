from django.shortcuts import render
from .models import Location


def location_list_view(request):
    if request.method == 'GET':
        location = Location.objects.all().order_by('-id')
        return render(
            request,
            'location_list.html',
            {
                'location': location
            }
        )