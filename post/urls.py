from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('posts/<int:pk>/', views.posts.as_view(), name='posts'),
    path('posts/', views.posts.as_view(), name='posts'),
    path('calender/<int:year>/<int:month>/', views.PostsLastMonthAPIView.as_view(), name='year-to-month')
    path('places/', views.place_get_in_map),
    path('places/<int:pk>/', views.place_get_in_spot)
]