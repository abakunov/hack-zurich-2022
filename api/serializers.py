from django.db.models import fields
from rest_framework import serializers

from core.models import *
from hackzurich.settings import BASE_URL


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', ]


class GoodSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Good
        exclude = ['img']

    def get_image_url(self, obj):
        return BASE_URL + '/media/' + str(obj.img)