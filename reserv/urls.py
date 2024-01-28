from django.urls import path
from reserv import views

app_name = 'reserv'

urlpatterns = [
    path('', views.index, name='index')
]
