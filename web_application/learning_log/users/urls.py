"""定义应用程序users的URL模式"""
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    # 登陆页面
    path('login/', LoginView.as_view(template_name='users/login.html'), 
        name="login"),
    # 注销页面
    path('logout/', views.logout_view, name='logout'),
    # 注册页面
    path('register/', views.register, name='register'),
]