from django.urls import path, include
from .views import api_view
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
]