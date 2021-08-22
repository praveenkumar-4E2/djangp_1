from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .views import Hello
  
urlpatterns = [
    path('', Hello),
]