from django.contrib import admin
from django.urls import path
from .views import ListEndPoints


urlpatterns = [
    path('', ListEndPoints.as_view())
]
