#managing inventory
items = ["oranges","apples","bannana"]
items.append("guava")
items.remove("oranges")
item = "oranges"
if item not in items:
    print(f"{item} are out of stock")
else:
    print(f"{item} are in stock")
