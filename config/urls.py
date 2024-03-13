from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
     path('backend/', include('backend.urls')),
      path('backend/', include('djoser.urls')),
       path('backend/', include('djoser.urls.authtoken')),
]
