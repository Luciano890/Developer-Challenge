import estates
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from estates.models import *
from estates.forms import OwnerForm, EstateForm, UserRegisterForm

def Home(request):
    owners = Owner.objects.all()
    estates = Estate.objects.all()
    context = {'owners':owners, 'estates':estates}
    
    return render(request, 'estates/index.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"User {username} was successfully created")
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'estates/register.html',context)

def addowner(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OwnerForm()
        
    context = {'form':form}
    return render(request, 'estates/addowner.html', context)

def addestate(request):
    if request.method == "POST":
        form = EstateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EstateForm()
        
    context = {'form':form}
    return render(request, 'estates/addestate.html', context)
    
def deleteowner(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    owner.delete()
    return redirect('home')

def deleteestate(request, estate_id):
    estate = Estate.objects.get(id=estate_id)
    estate.delete()
    return redirect('home')

def editowner(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    if request.method == "POST":
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OwnerForm(instance=owner)
        
    context = {'form':form}
    return render(request, 'estates/editowner.html', context)

def editestate(request, estate_id):
    estate = Estate.objects.get(id=estate_id)
    if request.method == "POST":
        form = EstateForm(request.POST, instance=estate)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EstateForm(instance=estate)
        
    context = {'form':form}
    return render(request, 'estates/editestate.html', context)