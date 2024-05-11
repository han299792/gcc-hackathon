from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('posts/<int:pk>/', views.posts.as_view(), name='posts'),
    path('posts/', views.posts.as_view(), name='posts'),
    path('calender/<int:year>/<int:month>/', views.PostsLastMonthAPIView.as_view(), name='year-to-month')
]