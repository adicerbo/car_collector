from django.shortcuts import render
from django.http import HttpResponse

class Car: 
    def __init__(self, make, year, model, trim):
        self.make = make
        self.year = year
        self.model = model
        self.trim = trim

cars = [
    Car('Nissan', 1989, 'GTR', 'base'),
    Car('Oldsmobile', 1967, 'Cutlass', '442'),
    Car('Mitsubishi', 1997, 'Eclipse', 'GSX')
]

def home(request):
    return HttpResponse("<h1>hello</h1>")

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', { 'cars': cars })