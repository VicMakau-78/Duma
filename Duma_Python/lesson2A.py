cars = ["BMW", "BENZ", "HIACE", "PRADO", "PROBOX", "MCLAREN"]
print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("the car on index four is:",cars[4])

# list slicing-This is creating a list from a given bigger list
print(cars[4:])

# printing from index zero to index three
print(cars[:3])

# printing from hiace to probox
print(cars[2:5])

# List-Mutability
# we use the funcion append to add an item at the end of a list
cars.append("MERCEDES")
print(cars)

# we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# we can use an index to add items to a list
cars[5] = "PAJERO"
print(cars)

# we can use the sort function to sort out itemsin alphabetical order
cars.sort()
print(cars)
