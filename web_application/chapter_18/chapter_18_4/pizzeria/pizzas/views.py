from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """比萨店的主页"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """显示所有比萨的页面"""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """显示特定的比萨的配料"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
