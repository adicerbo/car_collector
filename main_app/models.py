from django.db import models

class Car(models.Model):
    make: models.CharField(max_length=30)
    year: models.IntegerField()
    model: models.CharField(max_length=30)
    trim: models.CharField(max_length=30)
    


