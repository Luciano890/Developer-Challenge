from django import forms
from django.forms import fields
from estates.models import Owner, Estate

class OwnerForm(forms.ModelForm):
    
    class Meta:
        model = Owner
        fields = '__all__'
        
class EstateForm(forms.ModelForm):
    
    class Meta:
        model = Estate
        fields = '__all__'
         
         