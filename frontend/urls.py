from django.urls import path
from . import views


app_name = 'sight-api'

urlpatterns = [
    path('home/', views.home_view, name= ''),

    path('register/', views.register, name="register"),

    path('my-login/', views.my_login, name="my-login"),

    path('dashboard/', views.dashbord, name="dashboard"),

   


]


