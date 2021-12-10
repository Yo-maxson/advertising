from django.db.models import fields
from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    pub_date = serializers.DateField()
    author = serializers.CharField()
    text = serializers.CharField()
    price = serializers.IntegerField()
    photo = serializers.ImageField()

class AdvertModelSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='author', required=False)

    class Meta:
        model = Advert
        fields = '__all__'