from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .views import Hello
from .views import link
  
urlpatterns = [
    path('', Hello),
    path('link', link)
]