from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import Advert
from .serializers import AdvertSerializer, AdvertModelSerializer
from global_ads import serializers

class GetAdvertInfoView(APIView):
    def get(self, request):
        queryset = Advert.objects.all()
        serializer_for_queryset = AdvertSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class AdvertListAPIView(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertModelSerializer

class AdvertCreateAPIView(generics.CreateAPIView):

    queryset = Advert.objects.all()
    serializer_class = AdvertModelSerializer

class AdvertRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertModelSerializer
