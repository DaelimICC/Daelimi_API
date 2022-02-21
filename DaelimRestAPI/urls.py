from django.urls import path, include
from .views import TestAPI

urlpatterns = [
    path("test/", TestAPI),
]