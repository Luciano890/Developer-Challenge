from django.db import models
from estates.choices import locations,type

class Owner(models.Model):
    
    _id = models.CharField(max_length=20)
    _identificationNumber = models.CharField(max_length=10)
    _type = models.CharField(max_length=10, choices=type)
    
    def __str__(self) -> str:
        return f"Owner with id: {self._id} and type: {self._type}"
    
    
class Estate(models.Model):
    
    _identificationCadastral = models.CharField(max_length=20)
    _typeEstate = models.CharField(max_length=10, choices=locations)
    _registrationNumber = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"Estate with id: {self._identificationCadastral} and registration number: {self._registrationNumber}"
    