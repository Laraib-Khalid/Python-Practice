# Example 1: Creating different types of lists

numbers = [1, 2, 3, 4, 5]  # List of integers
fruits = ["Apple", "Banana", "Cherry"]  # List of strings
mixed = [1, "Hello", True, 3.14]  # Mixed data types
empty_list = []  # Empty list

print(numbers)
print(fruits)
print(mixed)
print(empty_list)


# Access elements using index (starts from 0)

fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])  # First element -> Apple
print(fruits[1])  # Second element -> Banana
print(fruits[-1]) # Last element -> Cherry



# Get a sublist using slicing with start, end, and step (jump)
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# Basic slicing
print(numbers[1:4])    # Elements from index 1 to 3 -> [20, 30, 40]
print(numbers[:3])      # First three elements -> [10, 20, 30]
print(numbers[2:])      # Elements from index 2 to end -> [30, 40, 50, 60, 70, 80]
print(numbers[-3:])     # Last three elements -> [60, 70, 80]

# Slicing with step (jumping)
print(numbers[::2])     # Every 2nd element -> [10, 30, 50, 70]
print(numbers[1::2])    # Every 2nd element starting from index 1 -> [20, 40, 60, 80]
print(numbers[:6:3])    # First 6 elements, every 3rd element -> [10, 40, 70]
print(numbers[5:1:-1])  # Reverse slice from index 5 to 2 -> [60, 50, 40, 30]
print(numbers[::-1])    # Reverse the entire list -> [80, 70, 60, 50, 40, 30, 20, 10]


# Lists are mutable (we can change elements)
fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Mango"  # Change second element
print(fruits)

# Adding elements
fruits.append("Orange")  # Add at the end
fruits.insert(1, "Grapes")  # Add at specific index
print(fruits)

# Removing elements
fruits.remove("Apple")  # Remove by value
print(fruits)
del fruits[2]           # Remove by index
print(fruits)
popped = fruits.pop()   # Remove last element and store it
print(fruits)
print("Popped item:", popped)


# Using for loop
fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    print(fruit)

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# Useful List Methods
numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()        # Sort in ascending order
print("Sorted:", numbers)

numbers.sort(reverse=True)  # Sort in descending order
print("Descending:", numbers)

print("Length:", len(numbers))  # Number of elements
print("Max:", max(numbers))     # Maximum value
print("Min:", min(numbers))     # Minimum value
print("Count of 5:", numbers.count(5))  # Count occurrences of 5


# =====================================================
# Example: Using 'in' and 'not in' with lists
# =====================================================

fruits = ["Apple", "Banana", "Cherry", "Mango"]

# Check if an item exists in the list using 'in'
if "Banana" in fruits:
    print("Banana is in the list")

# Check if an item does NOT exist in the list using 'not in'
if "Orange" not in fruits:
    print("Orange is NOT in the list")

# Using 'in' inside a loop
print("\nLooping through list to check membership:")
for fruit in ["Apple", "Orange", "Mango", "Grapes"]:
    if fruit in fruits:
        print(f"{fruit} is in the list")
    else:
        print(f"{fruit} is NOT in the list")

print("-"*50)

# Create a new list using comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]  # Square each number
print("Squares:", squares)


# With condition
even_squares = [n**2 for n in numbers if n % 2 == 0]  # Squares of even numbers
print("Even Squares:", even_squares)


# Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Fahrenheit:", fahrenheit)



# Flatten a matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten the matrix into a single list
flat = [num for row in matrix for num in row]
print("Flattened List:", flat)


# 5️⃣ Using if-else in List Comprehension
numbers = [1, 2, 3, 4, 5, 6]

# Mark numbers as 'Even' or 'Odd'
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Labels:", labels)



# 6️⃣ With Strings
words = ["python", "java", "c++", "javascript"]

# Get length of each word
lengths = [len(word) for word in words]
print("Lengths:", lengths)

# Uppercase all words
upper_words = [word.upper() for word in words]
print("Uppercase:", upper_words)


# 7️⃣ Removing Vowels from a String
sentence = "List comprehensions are powerful"
vowels = "aeiou"

filtered = [char for char in sentence if char.lower() not in vowels]
print("Without vowels:", ''.join(filtered))
