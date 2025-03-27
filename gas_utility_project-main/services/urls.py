from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.create_request, name='create_request'),
    path('status/', views.track_request, name='track_request'),
]
