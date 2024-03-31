from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.urls import path,include
from frontend.views import (home_view,logout_user)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('backend/', include('backend.urls')),
     #path('', include('frontend.urls')),
     path('',home_view,name='home'),
     path('',logout_user,name='logout'),
     path('', include('frontend.urls')),


     
     # path('backend/', include('djoser.urls')),
      # path('backend/', include('djoser.urls.authtoken')),
       #path('accounts/',include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
