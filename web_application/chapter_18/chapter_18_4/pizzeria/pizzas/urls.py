"""定义pizzas的URL模式"""
from django.urls import path
from . import views

urlpatterns = [
    # pizza的主页
    path('', views.index, name='index'),
    # 显示所有比萨的页面
    path('pizzas/', views.pizzas, name='pizzas'),
    # 显示对应比萨的配料的页面
    path('pizzas/<pizza_id>', views.pizza, name='pizza'),
]
