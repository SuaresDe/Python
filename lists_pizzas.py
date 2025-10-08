# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

pizza_and_prices = []

for i in range(len(toppings)):
  pizza_and_prices.append([prices[i], toppings[i]])

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

new_pizza = [2.5, "peppers"]
pizza_and_prices.append(new_pizza)
pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)