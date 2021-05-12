class Restaurant(object):
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


restaurant = Restaurant("wang", "frying")
print(restaurant.restaurant_name.title() + " " + restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()
