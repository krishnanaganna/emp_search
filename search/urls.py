from django.contrib import admin
from django.urls import path
from . import model

urlpatterns = [
    path('',model.index),
    path('search',model.search),
    ]
