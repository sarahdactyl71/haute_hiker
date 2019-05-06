# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from .models import Review, Article

def home(request):
    latest_review_list = Review.objects.order_by('-created')[:5]
    latest_article_list = Article.objects.order_by('-created')[:5]
    context = {'latest_review_list': latest_review_list, 'latest_article_list': latest_article_list}
    return render(request, 'reviews/home.html', context)

def reviews(request):
    latest_review_list = Review.objects.order_by('-created')[:5]
    reviews = Review.objects.all()
    context = {"home_page": "active", 'reviews': reviews, 'latest_review_list': latest_review_list}
    return render(request, 'reviews/reviews.html', context)

def show(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/show.html', {'review': review})

def about(request):
    context = {"about_page": "active"}
    return render(request, 'reviews/about.html', context)

def contact(request):
    context = {"contact_page": "active"}
    return render(request, 'reviews/contact.html', context)

def articles(request):
    articles = Article.objects.all()
    context= {"articles_page": "active", 'articles': articles}
    return render(request, 'articles/articles.html', context)

def show_article(request):
    artcile = get_object_or_404(Artcile, pk=article_id)
    return render(request, 'articles/show_article', {'article': article})
