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
    context = {"home_page": "active", 'reviews': reviews, 'latest_review_list': latest_review_list}
    return render(request, 'reviews/index.html', context)

def show(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/show.html', {'review': review})

def about(request):
    context = {"about_page": "active"}
    return render(request, 'reviews/about.html', context)

def contact(request):
    context = {"contact_page": "active"}
    return render(request, 'reviews/contact.html', context)
