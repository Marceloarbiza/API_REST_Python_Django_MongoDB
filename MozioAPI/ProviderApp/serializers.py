from rest_framework import serializers
from django.core.serializers import serialize
from ProviderApp.models import Provider
from ProviderApp.models import GeoJson


class ProviderSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format."""
    class Meta:
        """ Meta class to map serializer's fields with the model fields."""
        model = Provider
        fields = ('ProviderId', 'ProviderName', 'ProviderEmail', 'ProviderPhoneNumber', 'ProviderLanguage', 'ProviderCurrency')


class GeoJsonSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format."""
    class Meta:
        """ Meta class to map serializer's fields with the model fields."""
        model = GeoJson
        fields = ('GeoJsonId', 'GeoJsonName', 'GeoJsonPrice', 'GeoJsonData', 'GeoProviderName')
