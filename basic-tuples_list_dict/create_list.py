# create list food: 

food = ["rice", "beans"]
food.append("brocolli")
food.extend(["bread","pizza"])
print(food[0:2])
print(food[-1])


# create list using string.split 

food_item_string = "eggs, fruit, orange juice"
breakfast = food_item_string.split(",")
print(breakfast)
print(len(breakfast))

# List comprehension

lengths = [len(item) for item in breakfast]
print(lengths)