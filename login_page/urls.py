from django.urls import path
from . import views
from . serializers import CandidatesSerializer

urlpatterns = [
    path("", views.index),
    # path('monday', views.monday),
    path('tue', views.tue),
    path("index",views.index_page),
    path("candidatelist/", views.CandidateList.as_view(), name='candidates-list'),
    path("candidatelist/<int:pk>/", views.CandidatesDetail.as_view(), name='candidates-details'),
]
