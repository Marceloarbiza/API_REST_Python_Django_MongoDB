from django.db import models

# Create your models here.


class Provider(models.Model):
    """ Model to represent a Provider."""
    ProviderId = models.AutoField(primary_key=True)
    ProviderName = models.CharField(max_length=50, unique=True, null=False)
    ProviderEmail = models.EmailField(max_length=50)
    ProviderPhoneNumber = models.CharField(max_length=50)
    ProviderLanguage = models.CharField(max_length=50)
    ProviderCurrency = models.CharField(max_length=50)


class GeoJson(models.Model):
    """ Model to represent a GeoJson."""
    GeoJsonId = models.AutoField(primary_key=True)
    GeoJsonName = models.CharField(max_length=50)
    GeoJsonPrice = models.CharField(max_length=50)
    GeoJsonData = models.JSONField()
    GeoProviderName = models.CharField(max_length=50, null=False)
