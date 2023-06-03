from django.views.generic import ListView, CreateView
from .models import Station
from .forms import StationForm

class StationListView(ListView):
    model = Station
    template_name = 'stations/station_list.html'
    context_object_name = 'stations'

class StationCreateView(CreateView):
    model = Station
    form_class = StationForm
    template_name = 'stations/station_create.html'
    success_url = '/stations/'
