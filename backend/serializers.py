from .models import Category, Sight
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name')



class SightSerializer(GeoFeatureModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Sight
        geo_field = 'point_geom'
        fields = ('pk', 'category', 'name','city', 'slug')