from django.contrib import admin
from django.urls import path
from estates.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predios/', Main),
]
