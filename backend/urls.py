from django.urls import path
from . import views


app_name = 'backend'

urlpatterns = [
      path('category/', views.CategoryList.as_view(), name=views.CategoryList.name),
      path('sight/', views.SightList.as_view(),name=views.SightDetail.name  ),
      path('sight/<int:pk>/',views.SightDetail.as_view(),name=views.SightDetail.name)
]

