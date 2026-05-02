from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateEmergency.as_view(), name='createEmergency'),
    path('responder/', views.ResponderDashboard.as_view(), name='responderDashboard'),
]