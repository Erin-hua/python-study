from restaurant import Restaurant

restaurant = Restaurant("wang", "frying")
print("\n有" + str(restaurant.number_served) + "个人用过餐")
restaurant.number_served = 8
print("\n有" + str(restaurant.number_served) + "个人用过餐")

restaurant.set_number_served(15)
print("\n有" + str(restaurant.number_served) + "个人用过餐")

restaurant.increment_number_served(4)
print("\n有" + str(restaurant.number_served) + "个人用过餐")