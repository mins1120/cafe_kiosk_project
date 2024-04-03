from django.urls import path
from . import views

app_name = 'cafe_kiosk_app'  # URL 이름 공간 설정
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]