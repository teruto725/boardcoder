from django.urls import path
from . import views

app_name = "scripts"

urlpatterns = [
    path('upload', views.CreateScriptView.as_view(), name="create"),
    path('', views.ListScriptView.as_view(), name="index"),
    path('<int:pk>/delete', views.DeleteScriptView.as_view(), name='delete'),
]
