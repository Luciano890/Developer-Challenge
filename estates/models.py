from django.db import models
from estates.choices import locations,type

class Owner(models.Model):
    
    ID = models.CharField(max_length=20)
    identificationNumber = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=type)
    
    def __str__(self) -> str:
        return f"Owner with id: {self.ID}"
    
    
class Estate(models.Model):
    
    identificationCadastral = models.CharField(max_length=20)
    typeEstate = models.CharField(max_length=10, choices=locations)
    registrationNumber = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"Estate with registration number: {self.registrationNumber}"
    