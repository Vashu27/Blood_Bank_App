from django.urls import path
from .views import blooddondisplay

urlpatterns = [
    path('', blooddondisplay, name='blooddonsite'),
]
