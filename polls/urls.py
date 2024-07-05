from django.urls import path
from .views import ma_vue_django

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page1", views.index, name="index"),
    path("apply_Model", views.index1, name="index"),
    path('departement/', ma_vue_django, name='departement'),
]