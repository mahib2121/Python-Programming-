foods = []
prices = []
total = 0
while True:
    food = input("Enter a food to buy or q to quit: ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter Price of food {food}: $"))
        prices.append(price)

for x in foods:
    print(x, end=(" "))
for y in prices:
    total = total + y
    print(f"and total amount is {total}")
