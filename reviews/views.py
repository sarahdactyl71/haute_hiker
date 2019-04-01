# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from .models import Review


def index(request):
    latest_review_list = Review.objects.order_by('-created')[:5]
    reviews = Review.objects.all()
    context = {'reviews': reviews, 'latest_review_list': latest_review_list}
    return render(request, 'reviews/index.html', context)
