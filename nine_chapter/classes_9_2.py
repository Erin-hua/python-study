class Restaurant():
    """模拟餐馆营业"""

    def __init__(self, restaurant_name, cuisine_type):
        """给餐馆的属性赋值"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆的属性"""
        print("The restaurant's name is " + self.restaurant_name.title() + 
            ", cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        """打印餐馆是否营业"""
        print("The restaurant is opened.")


one = Restaurant("wang", "frying")
one.describe_restaurant()

two = Restaurant("hu", "boiling")
two.describe_restaurant()

three = Restaurant("zhao", "stewing")
three.describe_restaurant()
