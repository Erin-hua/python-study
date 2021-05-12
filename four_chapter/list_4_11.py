pizzas=["one","two"]
friend_pizzas=pizzas[:]
friend_pizzas.append("three")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
