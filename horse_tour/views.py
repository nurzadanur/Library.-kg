from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Location


def location_list_view(request):
    location = Location.objects.all().order_by('-id')

    paginator = Paginator(location, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'location_list.html',
        {
            'location': page_obj 
        }
    )