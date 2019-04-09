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
    description = models.CharField(max_length=2000)
    tags = models.ManyToManyField(Tag)
    resemblance_to_package = models.IntegerField()
    hot_sauce_needed = models.IntegerField()
    texture = models.IntegerField()
    deliciousness_level = models.IntegerField()
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')

    def __str__(self):
        return self.product_name
