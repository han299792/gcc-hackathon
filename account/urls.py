from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    #회원가입 화면
    path('signup/',views.RegisterAPIView.as_view()),
    #로그인 화면
    path('auth/',views.AuthAPIView.as_view()),
    #path('api-auth/', include('rest_framework.urls')),
    path('post/add/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
 ]