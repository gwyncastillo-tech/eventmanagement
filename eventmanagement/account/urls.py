from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('registerStudent/', views.RegisterStudent.as_view(), name='registerStudent'),
    path('login/', views.LoginUser.as_view(), name='loginUser'),
]

