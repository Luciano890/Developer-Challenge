from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput
from estates import models
from estates import choices
from estates.models import Owner, Estate
from estates.choices import type, locations

class OwnerForm(forms.ModelForm):
    
    ID = forms.CharField(label=False,min_length=4, max_length=30,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':"CC",
                                     'class':'form-control',
                                 }
                             ))
    identificationNumber = forms.CharField(label=False,min_length=4, max_length=50,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':"Indentification Number",
                                     'class':'form-control',
                                 }
                             ))
    type = forms.ChoiceField(label=False,choices=type,
                             widget=forms.Select(
                                 attrs={
                                     'placeholder':"Type",
                                     'class':'form-control',
                                 }
                             ))
    
    class Meta:
        model = Owner
        fields = ['ID','identificationNumber','type']
        
class EstateForm(forms.ModelForm):
    
    identificationCadastral = forms.CharField(label=False,min_length=4, max_length=20,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':"Indentification Cadastral",
                                     'class':'form-control',
                                 }
                             ))
    typeEstate = forms.ChoiceField(label=False,choices=locations,
                             widget=forms.Select(
                                 attrs={
                                     'placeholder':"Type Estate",
                                     'class':'form-control',
                                 }
                             ))
    registrationNumber = forms.CharField(label=False,min_length=4, max_length=30,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':"Registration Number",
                                     'class':'form-control',
                                 }
                             ))
    
    class Meta:
        model = Estate
        fields = ['identificationCadastral','typeEstate','registrationNumber']
         
class UserRegisterForm(forms.ModelForm):
    
    username = forms.CharField(label=False,min_length=4, max_length=50,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':"UserName",
                                     'class':'form-control',
                                 }
                             ))
    
    email = forms.EmailField(label=False,min_length=4, max_length=30,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder':"Email",
                                     'class':'form-control',
                                 }
                             ))
    
    password = forms.CharField(label=False,min_length=8, max_length=30,
                             widget=forms.PasswordInput(
                                 attrs={
                                     'placeholder':"Password",
                                     'class':'form-control',
                                 }
                             ))
    
    password_conf = forms.CharField(label=False,min_length=8, max_length=30,
                             widget=forms.PasswordInput(
                                 attrs={
                                     'placeholder':"Password Confirmation",
                                     'class':'form-control',
                                 }
                             ))
    
    class Meta:
        model = User
        fields = ['username','email', 'password','password_conf']
        help_texts = {i:"" for i in fields}