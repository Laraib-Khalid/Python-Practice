numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())


print("-" * 50)


names = ["John", "Jane", "Jim"]
lower_names = [name.lower() for name in names]
print(lower_names)

if (name := (input("Enter a name: ")).lower()) in lower_names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")


print("-" * 50)


# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)
