def sandwiches(*toppings):
    print("\nThe customer's sanwich has:")
    for topping in toppings:
        print("-" + topping)

sandwiches("mushroom")
sandwiches("pepperoni", "green peppers")
sandwiches("green peppers", "mushroom", "cheese")
