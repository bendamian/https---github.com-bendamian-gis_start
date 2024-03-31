from django.urls import path
from . import views


app_name = 'frontend'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.my_login, name="login"),
    path('dashbord/', views.dashbord, name="dashbord"),

    
    path('reg/', views.register, name="register"),
    #path('', views.register, name="register"),
]

