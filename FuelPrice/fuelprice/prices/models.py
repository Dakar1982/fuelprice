from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class FuelPrice(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
