from django.db import models

# 比萨店的模型
class Pizza(models.Model):
    """比萨的有关属性"""
    name = models.TextField()

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

class Topping(models.Model):
    """配料的有关属性"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    
    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name