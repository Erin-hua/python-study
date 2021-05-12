"""餐馆模块"""

class Restaurant():
    """模拟餐馆营业"""

    def __init__(self, restaurant_name, cuisine_type):
        """给餐馆的属性赋值"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆的属性"""
        print("The restaurant's name is " + self.restaurant_name.title() + 
            ", cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """打印餐馆是否营业"""
        print("The restaurant is opened.")

    def set_number_served(self, num):
        """修改用餐人数"""        
        if num >= self.number_served:
            self.number_served = num
        else:
            print("你不能减少用餐人数。")

    def increment_number_served(self, increase):
        """就餐人数递增"""
        self.number_served += increase