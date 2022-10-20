from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cats/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),
    path('cars/<int:car_id>/add_service/', views.add_maintain, name='add_maintain'),
    path('fluids/', views.FluidList.as_view(), name='fluids_index'),
    path('fluids/<int:pk>/', views.FluidDetail.as_view(), name='fluids_detail'),
    path('fluids/create/', views.FluidCreate.as_view(), name='fluids_create'),
    path('fluids/<int:pk>/update/', views.FluidUpdate.as_view(), name='fluids_update'),
    path('fluids/<int:pk>/delete/', views.FluidDelete.as_view(), name='fluids_delete'),
    path('cars/<int:car_id>/assoc_fluid/<int:fluid_id>/', views.assoc_fluid, name='assoc_fluid'),
]