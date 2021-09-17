from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

"""
specifying urls for the web application
"""

urlpatterns = [
    
    path('', views.register, name="register"),
    path('home/', views.Home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='estates/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='estates/logout.html'), name="logout"),
    path('addowner/', views.addowner, name="addowner"),
    path('addestate/', views.addestate, name="addestate"),
    path('deleteowner/<int:owner_id>/', views.deleteowner, name="deleteowner"),
    path('deleteestate/<int:estate_id>/', views.deleteestate, name="deleteestate"),
    path('editowner/<int:owner_id>/', views.editowner, name="editowner"),
    path('editestate/<int:estate_id>/', views.editestate, name="editestate"),
]