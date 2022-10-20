from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Car, Fluid
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MaintainForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def cars_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})


@login_required
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


@login_required
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


@login_required
def assoc_fluid(request, car_id, fluid_id):
  # Note that you can pass a fluid's id instead of the whole object
    Car.objects.get(id=car_id).fluids.add(fluid_id)
    return redirect('detail', car_id=car_id)



class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'year', 'model', 'trim', 'mileage']
    def form_valid(self,form):
        # assign logged in user
        form.instance.user = self.request.user #form instance is a car
        return super().form_valid(form)
    

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['mileage', ]


class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'


class FluidCreate(LoginRequiredMixin, CreateView):
    model = Fluid
    fields = ('name', 'weight')


class FluidUpdate(LoginRequiredMixin, UpdateView):
    model = Fluid
    fields = ('name', 'weight')


class FluidDelete(LoginRequiredMixin, DeleteView):
    model = Fluid
    success_url = '/fluids/'


class FluidDetail(LoginRequiredMixin, DetailView):
    model = Fluid
    template_name = 'fluids/detail.html'


class FluidList(LoginRequiredMixin, ListView):
    model = Fluid
    template_name = 'fluids/index.html'

# SIGNUP VIEW FUNCTION
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # how to create a user form object that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # add user to database
            user = form.save()
            # log user in
            login(request, user)
            return redirect('index')
        else: 
            error_message = 'Invalid sign up - try again'
    # a bad POST or GET, render signup.html with empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)