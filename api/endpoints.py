from django.urls import path, include
from rest_framework.generics import CreateAPIView
from .views import *


api_urls = [
    path('setGender', CreateCustomer.as_view(), name='setGender'),
    path('getFeed', GetFeed.as_view(), name='getFeed'),
    path('getTags', GetTags.as_view(), name='getTags'),
    path('like', Like.as_view(), name='like'),
    path('dislike', Dislike.as_view(), name='dislike'),
    path('getFavourites', GetFavourites.as_view(), name='getFavourites'),
]