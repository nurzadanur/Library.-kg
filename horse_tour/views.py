from django.views.generic import ListView
from .models import Location


class LocationListView(ListView):
    model = Location
    template_name = 'location_list.html'
    context_object_name = 'location'
    ordering = ['-id']
    paginate_by = 5