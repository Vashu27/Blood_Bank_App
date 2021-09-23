from django.urls import path
from .views import blooddisplay

urlpatterns = [
    path('', blooddisplay, name='bloodsite'),
]
