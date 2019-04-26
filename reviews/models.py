# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')

    def __str__(self):
        return self.tag_name

class Review(models.Model):
    image_url = models.CharField(max_length=500)
    product_name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    description = models.CharField(max_length=10000)
    tags = models.ManyToManyField(Tag)
    resemblance_to_package = models.IntegerField()
    hot_sauce_needed = models.IntegerField()
    texture = models.IntegerField()
    deliciousness_level = models.IntegerField()
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')

    def overall_rating(self):
        average = (self.resemblance_to_package + self.hot_sauce_needed + self.texture +self.deliciousness_level)/4
        return average

    def __str__(self):
        return self.product_name

class Article(models.Model):
    title = models.CharField(max_length=50)
    hiking_trail = models.CharField(max_length=50)
    image_url = models.CharField(max_length=500)
    content = models.CharField(max_length=10000)
    reviews = models.ManyToManyField(Review)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')

    def __str__(self):
        return self.title
