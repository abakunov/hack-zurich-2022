from unicodedata import category
from hackzurich.settings import BASE_URL
from django.db import models


class Customer(models.Model):
    uid = models.CharField(max_length=1000, unique=True)
    GENDER_CATEGORIES = [
        ('m', 'Мужской'),
        ('f', 'Женский'),
    ]
    gender = models.CharField(max_length=1, choices = GENDER_CATEGORIES, default='m')
    favourites = models.ManyToManyField('core.Good', related_name='favourites', blank=True)

    def __str__(self):
        return str(self.uid)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    img = models.ImageField(blank=True, null=True)
    link = models.URLField(default='https://www.google.com/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField('core.Tag', blank=True)

    @property
    def image_url(self):
        return BASE_URL + '/media/' + str(self.image)

    def __str__(self):
        return self.name