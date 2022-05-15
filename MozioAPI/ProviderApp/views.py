from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ProviderApp.models import Provider
from ProviderApp.serializers import ProviderSerializer

from ProviderApp.models import GeoJson
from ProviderApp.serializers import GeoJsonSerializer


@csrf_exempt
def providerApi(request, id=0):
    """ Function to handle the provider API."""
    if request.method == 'GET':
        if id == 0:
            providers = Provider.objects.all()
            serializer = ProviderSerializer(providers, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            provider = Provider.objects.get(ProviderId=id)
            serializer = ProviderSerializer(provider)
            return JsonResponse(serializer.data)
    elif request.method == 'POST':
        provider_data = JSONParser().parse(request)
        provider_serializer = ProviderSerializer(data=provider_data)
        if provider_serializer.is_valid():
            provider_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        provider_data = JSONParser().parse(request)
        provider = Provider.objects.get(ProviderId=id)
        provider_serializer = ProviderSerializer(provider, data=provider_data)
        if provider_serializer.is_valid():
            provider_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        provider = Provider.objects.get(ProviderId=id)
        provider.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def geojsonApi(request, id=0):
    """ Function to handle GeoJson API """
    if request.method == 'GET':
        if id == 0:
            geojsons = GeoJson.objects.all()
            serializer = GeoJsonSerializer(geojsons, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            geojson = GeoJson.objects.get(GeoJsonId=id)
            serializer = GeoJsonSerializer(geojson)
            return JsonResponse(serializer.data)
    elif request.method == 'POST':
        geojson_data = JSONParser().parse(request)
        geojson_serializer = GeoJsonSerializer(data=geojson_data)
        if geojson_serializer.is_valid():
            geojson_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        geojson_data = JSONParser().parse(request)
        geojson = GeoJson.objects.get(GeoJsonId=id)
        geojson_serializer = GeoJsonSerializer(geojson, data=geojson_data)
        if geojson_serializer.is_valid():
            geojson_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        geojson = GeoJson.objects.get(GeoJsonId=id)
        geojson.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def geoLocationApi(request, lat=0, lng=0):
    """ Function to get GeoJson by Latitude and Longitude """
    if request.method == 'GET':
        geoLocations = GeoJson.objects.all()
        list_GeoJsonData = []
        for geoLocation in geoLocations:
            for loc in geoLocation.GeoJsonData.get('coordinates')[0]:
                if loc[0] == float(lat) and loc[1] == float(lng):
                    list_GeoJsonData.append(geoLocation)
                    break
        serializer = GeoJsonSerializer(list_GeoJsonData, many=True)
        return JsonResponse(serializer.data, safe=False)
