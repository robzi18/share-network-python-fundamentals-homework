import random
toppings = ["pepperoni", "pineapple", "cheese",
            "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = 0
for x in prices:
    if x == 2:
        num_two_dollar_slices += 1
print(f"Number of occurrences of 2: {num_two_dollar_slices}")
num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")
pizza_and_prices = list(zip(prices, toppings))
print(pizza_and_prices)
print("Price   |    Toppings ")
print("---------------------")
for index in range(len(prices)):
    print(f"{prices[index]}     |   {toppings[index]}")
# Sorting
pizza_and_prices.sort()
priciest_pizza = pizza_and_prices[-1]
cheapest_pizza = pizza_and_prices[0]
print(f"The expensive pizza is: {priciest_pizza}")
print("==SELLING THE CHEAPEST PIZZA==")
print(f"The cheapest pizza is: {cheapest_pizza}")
print("=====\n")
print("=====\n")
pizza_and_prices.pop()
print(pizza_and_prices)
new_topping = (2.5, "peppers")
pizza_and_prices.append(new_topping)
print(pizza_and_prices)
pizza_and_prices.sort()
print("Price   |    Toppings ")
print("---------------------")
for price, topping in pizza_and_prices:
    print(f"{price}     |   {topping}")

three_cheapest = pizza_and_prices[0:3]
three_cheapest = []
for i in range(3):
    three_cheapest.append(random.choice(pizza_and_prices))
print(f"cheapest deal: {three_cheapest}\n")
print("The three cheapest pizzas are:")
print("Price   |    Toppings ")
print("---------------------")
three_cheapest.sort()
for price, topping in three_cheapest:
    print(f"{price}     |   {topping}")
