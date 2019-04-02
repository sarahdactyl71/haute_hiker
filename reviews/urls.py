from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    #urls for review
    path('', views.index, name='index'),
    path('<int:review_id>/', views.show, name='show'),
]
