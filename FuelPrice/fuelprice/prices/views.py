from django.views.generic import ListView, CreateView
from .models import FuelPrice
from .forms import FuelPriceForm

class PriceListView(ListView):
    model = FuelPrice
    template_name = 'prices/price_list.html'
    context_object_name = 'prices'

class PriceCreateView(CreateView):
    model = FuelPrice
    form_class = FuelPriceForm
    template_name = 'prices/price_create.html'
    success_url = '/prices/'
