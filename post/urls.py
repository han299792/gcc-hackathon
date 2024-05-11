from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('posts/', views.posts.as_view(), name='posts'),
    path('posts/<int:pk>/', views.posts.as_view(), name='posts'),
    path('places/', views.place_get_in_map),
    path('places/<int:pk>/', views.place_get_in_spot),
    path('calender/<int:pk>/', views.PostsLastMonthAPIView.as_view(), name='year-to-month'),
    path('personal/places/', views.place_get_in_map),
    path('personal/places/<int:pk>/', views.place_get_in_spot),
    path('global/places/', views.global_place_get),
    path('global/places/<int:pk>/', views.global_place_get_detail)
]