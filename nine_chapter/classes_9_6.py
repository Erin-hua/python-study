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


class IceCreamStand(Restaurant):
    """继承餐馆类"""

    def __init__(self, restaurant_name, cuisine_type, *tastes):
        """初始化冰淇淋的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        for taste in tastes:
            self.flavors.append(taste)

    def show_tastes(self):
        """显示不同口味的冰淇淋"""
        print("The ice cream has some flavors:")
        for flavor in self.flavors:
            print("-" + flavor) 
        

icecream = IceCreamStand("wang", "frying", "milk", "chocolate", "vanilla")
icecream.show_tastes()

