from django.db.models import query
from django.http import request
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from core.models import *
from .serializers import *
from hackzurich.settings import BASE_URL

import requests
import re
from core.parser_config import *


class CreateCustomer(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            uid = request.data['uid']
            gender = request.data['gender']

            customer = Customer.objects.get_or_create(uid=uid)[0]
            customer.gender = gender
            customer.save()
            
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class GetFeed(views.APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            uid = request.GET['uid']
            tags = request.GET['tags'].split(' ')
            category = request.GET['category']

            customer = Customer.objects.get(uid=uid)
            tags = Tag.objects.filter(name__in=tags)
            category = Category.objects.get(name=category)

            if len(tags) > 0:
                goods = Good.objects.filter(category=category, tags__in=tags).order_by('id')[:7]
            else:
                goods = Good.objects.filter(category=category).order_by('id')[:7]

            serialized_goods = GoodSerializer(goods, many=True).data
            for elem in serialized_goods:
                elem['brand'] = Brand.objects.get(id=elem['brand']).name
                elem['category'] = category.name
                elem_tags = []
                for tag in elem['tags']:
                    elem_tags.append(Tag.objects.get(id=tag).name)
                elem['tags'] = elem_tags
                elem['liked'] = customer.favourites.filter(id=elem['id']).exists()

            return Response(serialized_goods, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)



class GetTags(views.APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            tags = Tag.objects.all()
            serialized_tags = [tag.name for tag in tags]
            return Response(serialized_tags, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class Like(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            uid = request.data['uid']
            good_id = request.data['good_id']
            customer = Customer.objects.get(uid=uid)
            good = Good.objects.get(id=good_id)
            customer.favourites.add(good)
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class Dislike(views.APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            uid = request.data['uid']
            good_id = request.data['good_id']
            customer = Customer.objects.get(uid=uid)
            good = Good.objects.get(id=good_id)
            customer.favourites.remove(good)
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class GetFavourites(views.APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            uid = request.GET['uid']
            customer = Customer.objects.get(uid=uid)
            goods = customer.favourites.all()
            serialized_goods = GoodSerializer(goods, many=True).data
            for elem in serialized_goods:
                elem['brand'] = Brand.objects.get(id=elem['brand']).name
                elem['category'] = Category.objects.get(id=elem['category']).name
                elem_tags = []
                for tag in elem['tags']:
                    elem_tags.append(Tag.objects.get(id=tag).name)
                elem['tags'] = elem_tags
                elem['liked'] = customer.favourites.filter(id=elem['id']).exists()

            return Response(serialized_goods, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class Parse(views.APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            # response = requests.post('https://www.zalando.dk/api/graphql/', cookies=cookies, headers=headers, json=json_data).json()
            # for good in response:
            #     try:
            #         name = good['data']['product']['name']
            #         brand = good['data']['product']['brand']['name']
            #         image_url = re.findall("(.*\.jpg).*", good['data']['product']['largeDefaultMedia']['uri'])[0]
            #         link = good['data']['product']['uri']
            #         price = int(good['data']['product']['displayPrice']['original']['formatted'][:-6])
            #         silhouette = good['data']['product']['silhouette']

            #         brand = Brand.objects.get_or_create(name=brand)[0]
            #         silhouette = Silhouette.objects.get_or_create(name=silhouette)[0]
            #         category = Category.objects.get_or_create(name='clothes')[0]

            #         good = Good.objects.get_or_create(name=name, brand=brand, image_url=image_url, link=link, price=price, silhouette=silhouette, category=category)[0]
            #     except Exception as e:
            #         print(e)
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)