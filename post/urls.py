from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    path('posts/', views.posts.as_view(), name='posts'),
    path('posts/<int:pk>/', views.posts.as_view(), name='posts'),
    path('places/', views.PlacesView.as_view()),
    path('places/<int:pk>/', views.place_get_in_spot),
    path('calender/<int:pk>/', views.PostsLastMonthAPIView.as_view(), name='year-to-month'),
    path('personal/places/', views.PlacesView.as_view()),
    path('personal/places/<int:pk>/', views.place_get_in_spot),
    path('global/places/', views.global_place_get),
    path('global/places/<int:pk>/', views.global_place_get_detail),
    path('places/tag/', views.PlaceTagView.as_view()),
    path('posts/mood/', views.MoodStatusView.as_view())
]