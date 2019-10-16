from django.contrib import admin
from django.urls import path


app_name="user" # istediyimiz ad ola biler

from user import views
urlpatterns = [
    path('register/', views.registerUser,name="register"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),

]
