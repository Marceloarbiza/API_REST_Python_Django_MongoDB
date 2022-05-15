from django.urls import path, include, re_path
from ProviderApp import views
from django.urls import re_path as url


urlpatterns = [
    url(r'^provider$', views.providerApi),  # /provider
    url(r'^provider/([0-9]+)$', views.providerApi),  # /provider/1

    url(r'^geojson$', views.geojsonApi),  # /geojson
    url(r'^geojson/([0-9]+)$', views.geojsonApi),  # /geojson/1

    url(r'^geojson/([0-9]+\.[0-9]+)\/([0-9]+\.[0-9]+)$', views.geoLocationApi),  # /geojson/lat/lng
]
