from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    path('signup', views.UserCreateView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='update')
]