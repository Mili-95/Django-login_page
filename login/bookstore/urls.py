from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_form, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('regform/', views.registerForm, name='regform'),
    path('register/', views.registerView, name='register'),
    path('dashboard/', views.dashboardView, name='dashboard'),
   
]
