from django.urls import path
from .views import salomlash


urlpatterns = [
    path('', salomlash),
]