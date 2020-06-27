from django.urls import path
from . import views
from .views import index, room

app_name = "games"

urlpatterns = [
    path('', index, name='index'),
    path('<slug:room_name>/', room, name='room')
]