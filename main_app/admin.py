from django.contrib import admin
from .models import Car, Maintain, Fluid

# Register your models here.
admin.site.register(Car)
admin.site.register(Maintain)
admin.site.register(Fluid)