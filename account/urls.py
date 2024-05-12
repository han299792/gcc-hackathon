from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns =[
    #회원가입 화면
    path('signup/',views.RegisterAPIView.as_view()),
    #로그인 화면
    path('api/register/', views.CreateUser.as_view(), name='register'),
    path('api/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/update/', views.UpdateUser.as_view(), name='update_user'),
]