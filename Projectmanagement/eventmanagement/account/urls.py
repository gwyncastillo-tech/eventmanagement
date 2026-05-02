from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='loginUser'),
    path('edit-profile/', views.EditProfile.as_view(), name='editProfile'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('my-emergencies/', views.MyEmergencies.as_view(), name='myEmergencies'),
]