from django.shortcuts import render

# Create your views here.
def index(requests):
    """比萨店的主页"""
    return render(requests, 'pizzas/index.html')
