from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Car, Fluid
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MaintainForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    fluids_car_doesnt_have = Fluid.objects.exclude(
        id__in=car.fluids.all().values_list('id'))
    # instaniate maintainform to be rendered in template
    maintain_form = MaintainForm()
    return render(request, 'cars/detail.html', {
        # includes car and feeding form in the context
        'car': car,
        'maintain_form': maintain_form,
        'fluids': fluids_car_doesnt_have
    })


def add_maintain(request, car_id):
    # create model form using data in request.post
    form = MaintainForm(request.POST)
    # validate the form
    if form.is_valid():
        # dont save the form to the db until it has the car_id assigned
        new_maintain = form.save(commit=False)
        new_maintain.car_id = car_id
        new_maintain.save()
        # use redirect instead of render if data has been changed in the database
    return redirect('detail', car_id=car_id)


def assoc_fluid(request, car_id, fluid_id):
  # Note that you can pass a fluid's id instead of the whole object
    Car.objects.get(id=car_id).fluids.add(fluid_id)
    return redirect('detail', car_id=car_id)


class CarCreate(CreateView):
    model = Car
    fields = ['make', 'year', 'model', 'trim', 'mileage']
    success_url = '/cars/'


class CarUpdate(UpdateView):
    model = Car
    fields = ['mileage', ]


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'


class FluidCreate(CreateView):
    model = Fluid
    fields = ('name', 'weight')


class FluidUpdate(UpdateView):
    model = Fluid
    fields = ('name', 'weight')


class FluidDelete(DeleteView):
    model = Fluid
    success_url = '/fluids/'


class FluidDetail(DetailView):
    model = Fluid
    template_name = 'fluids/detail.html'


class FluidList(ListView):
    model = Fluid
    template_name = 'fluids/index.html'
