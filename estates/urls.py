from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('addowner/', views.addowner, name="addowner"),
    path('addestate/', views.addestate, name="addestate"),
    path('deleteowner/<int:owner_id>/', views.deleteowner, name="deleteowner"),
    path('deleteestate/<int:estate_id>/', views.deleteestate, name="deleteestate"),
    path('editowner/<int:owner_id>/', views.editowner, name="editowner"),
    path('editestate/<int:estate_id>/', views.editestate, name="editestate"),
]