from unicodedata import category
from hackzurich.settings import BASE_URL
from django.db import models


class Customer(models.Model):
    uid = models.CharField(max_length=1000, unique=True)
    GENDER_CATEGORIES = [
        ('m', 'Мужской'),
        ('f', 'Женский'),
        ('о', 'Другое'),
    ]
    gender = models.CharField(max_length=1, choices = GENDER_CATEGORIES, default='o')
    favourites = models.ManyToManyField('core.Good', related_name='favourites', blank=True)

    def __str__(self):
        return str(self.uid)


class Category(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Silhouette(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=1000)
    brand = models.ForeignKey('core.Brand', on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField()
    image_url = models.URLField(default='https://www.zalando.dk/solid-poloshirt-panos-poloshirts-med-grey-melange-so422p00k-c12.html')
    link = models.URLField(default='https://www.google.com/')
    silhouette = models.ForeignKey('core.Silhouette', on_delete=models.CASCADE, blank=True, null=True)
    SEX_CATEGORIES = [
        ('m', 'Мужской'),
        ('f', 'Женский'),
        ('u', 'Унисекс'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CATEGORIES, default='m')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField('core.Tag', blank=True)
    promoted = models.BooleanField(default=False)

    # @property
    # def image_url(self):
    #     return BASE_URL + '/media/' + str(self.image)

    def __str__(self):
        return self.name