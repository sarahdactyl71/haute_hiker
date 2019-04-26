from django.urls import path

from . import views

# app_name = 'reviews'
urlpatterns = [
    #urls for review
    path('reviews/', views.reviews, name='reviews'),
    path('reviews/<int:review_id>/', views.show, name='show'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.articles, name='articles'),
]
