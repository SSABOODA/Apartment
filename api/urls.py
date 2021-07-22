from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/admins', include('api.admins.urls')),
    path('/publics', include('api.publics.urls')),
]
