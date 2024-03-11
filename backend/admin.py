from django.contrib.gis import admin

# Register your models here.

from .models import Marker,Place

# Register your models here.

@admin.register(Marker)
class MarkerAdmin(admin.GISModelAdmin):
    list_display = ("name", "location")


@admin.register(Place)
class MarkerAdmin(admin.GISModelAdmin):
    list_display = ("name", "location")

