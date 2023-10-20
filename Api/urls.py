from .views import Portfolio
from django.urls import path

# app_name = 'api'
urlpatterns = [
    path('home/', Portfolio),
]
