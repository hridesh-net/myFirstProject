from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # path('monday', views.monday),
    path('tue', views.tue),
]
