from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# class Car: 
#     def __init__(self, make, year, model, trim):
#         self.make = make
#         self.year = year
#         self.model = model
#         self.trim = trim

# cars = [
#     Car('Nissan', 1989, 'GTR', 'base'),
#     Car('Oldsmobile', 1967, 'Cutlass', '442'),
#     Car('Mitsubishi', 1997, 'Eclipse', 'GSX')
# ]


def home(request):
    return HttpResponse("<h1>hello</h1>")

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', { 'car': car })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['mileage',]

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'