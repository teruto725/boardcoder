from django.urls import path

from . import views


app_name = "home"#名前空間の定義


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]