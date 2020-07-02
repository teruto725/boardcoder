from django.urls import path

from .views import RoomCreateView, RoomListView, RoomView, ExitRoom

app_name = "rooms"

urlpatterns = [
    path('', RoomListView.as_view(), name='index'),
    path('create', RoomCreateView.as_view(), name='create'),
    path('<int:pk>/', RoomView.as_view(), name="room"),
    path('<int:pk>/exit/', ExitRoom.as_view(), name="exit"),
    #path('<slug:room_name>/', room, name='room'),
    #path('<int:pk>/delete/', RoomDeleteView.as_view, name="delete"),
]