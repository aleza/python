from django.db import models
from datetime import date

class Owner(models.Model):
    name            = models.CharField(max_length=30)
    surname         = models.CharField(max_length=30)
    dni             = models.CharField(max_length=10)

    def __str__(self):
        return self.name.capitalize() + ", "+ self.surname.capitalize() + ", "+ self.dni

class Brand(models.Model):
    owner           = models.ForeignKey(Owner, on_delete=models.CASCADE)
    brandName       = models.CharField(max_length=30)

    def __str__(self):
        return self.brandName.capitalize()

class Model(models.Model):
    brand           = models.ForeignKey(Brand, on_delete=models.CASCADE)
    modelName       = models.CharField(max_length=30)
    year            = models.CharField(max_length=8)

    def __str__(self):
        return self.modelName.capitalize() + " "+ self.year

class Repair(models.Model):
    model           = models.ForeignKey(Model, on_delete=models.CASCADE)        
    detail          = models.CharField(max_length=30)

    def __str__(self):
        return self.detail.capitalize()

