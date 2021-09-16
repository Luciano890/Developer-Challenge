from django.contrib import admin
from django.urls import path, include
from estates.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("estates.urls"))
]
