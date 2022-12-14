from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SERVICE = (
    ('O', 'Oil Change'),
    ('C', 'Coolant Flush'),
    ('B', 'Brake Pads'),
    ('F', 'Fuel Filter')
)

class Fluid(models.Model):
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('fluids_detail', kwargs={'pk': self.id})


class Car(models.Model):
    make = models.CharField(max_length=30)
    year = models.IntegerField()
    model = models.CharField(max_length=30)
    trim = models.CharField(max_length=30)
    mileage = models.IntegerField()
    # add many to many relationship
    fluids = models.ManyToManyField(Fluid)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Maintain(models.Model):
    date = models.DateField('Service Date')
    service = models.CharField(
        max_length=1,
        choices=SERVICE,
        default=SERVICE[0][0]
        )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"
    
    # sort by most recent date of service
    class Meta:
        ordering = ['-date']