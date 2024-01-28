from django.urls import path
from reserv import views

app_name = 'reserv'

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('reserva/', views.reserva, name='reserva'),
    path('login/', views.login, name='login'),
    path('register/', views.register_login, name='register')
]
