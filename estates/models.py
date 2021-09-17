from django.db import models
from estates.choices import locations,type

class Estate(models.Model):
    
    """
    Model to the Estate table with many-to-many relantionship
    """
    
    identificationCadastral = models.CharField(max_length=20)
    typeEstate = models.CharField(max_length=10, choices=locations)
    registrationNumber = models.CharField(max_length=20, unique=True)
    
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    
    owners = models.ManyToManyField("Owner")
    
    def __str__(self) -> str:
        return f"Estate with registration number: {self.registrationNumber}"

class Owner(models.Model):
    
    """
    Model to the Owner table with many-to-many relantionship
    """
    
    ID = models.CharField(max_length=20,unique=True)
    identificationNumber = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=type)
    
    estates = models.ManyToManyField("Estate")
    
    def __str__(self) -> str:
        return f"Owner with id: {self.ID}"