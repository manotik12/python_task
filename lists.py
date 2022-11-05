# delcalre an initialize a list
fruits = ["orange", "peache", "banana", "mango", "plum"]
print(fruits)

# loop through entire list of fruits
for fruit in fruits:
    print(fruit)

# Retrieve list items
print(f"the fruit at index 1: {fruits[1]}")
print(f"the fruit at the end of the list is: {fruits[-1]}")
# check length of the list
print(f"the fruit basket currently has {len(fruits)} fruits")

# add something to the list

fruits.append("lemon")
print(fruits)
print(f"the fruit basket now currently has {len(fruits)} fruits")

# add list item to a specific position in the list
fruits.insert(5, "apple")
print(fruits)

# remove specific item from list
fruits.remove("plum")
print(fruits)

# remove item from a specified index on the list
fruits.pop(1)
print(fruits)
