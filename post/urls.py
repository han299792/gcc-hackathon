from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('posts/', views.post_add)
 ]