from django.urls import path
from . import views


app_name = 'sight-api'

urlpatterns = [
    path('home/', views.home_view, name= 'home'),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),


]


