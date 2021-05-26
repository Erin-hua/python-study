"""定义pizzas的URL模式"""
from django.urls import path
from . import views

urlpatterns = [
    # pizza的主页
    path('', views.index, name='index')
]