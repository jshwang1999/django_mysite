# chat/urls.py

from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('room/<str:room_name>/', views.room, name='room'),  # 패턴에 이름 추가
]
