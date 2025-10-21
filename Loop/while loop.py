# ==========================================================
# 🌀 Example: While Loop in Python (Without break/continue)
# ==========================================================

# A while loop repeats a block of code **as long as a condition is True**

# Example 1: Simple counting from 1 to 5
print("Example 1: Counting from 1 to 5 using while loop")

count = 1  # Initialize the counter variable

while count <= 5:  # Condition: loop runs while count is less than or equal to 5
    print("Count is:", count)  # Print the current value of count
    count += 1  # Increment the counter by 1

print("Loop finished!")
print("-" * 50)


# Example 2: Printing even numbers from 2 to 10
print("Example 2: Printing even numbers from 2 to 10")

num = 2  # Start from 2

while num <= 10:  # Run the loop until num exceeds 10
    print(num)
    num += 2  # Increment by 2 to get next even number

print("Even numbers loop finished!")
print("-" * 50)


# Example 3: Looping through a list using while
print("Example 3: Looping through a list using while")

fruits = ["Apple", "Banana", "Cherry"]
index = 0  # Start index at 0

while index < len(fruits):  # Loop until index reaches the length of the list
    print(fruits[index])  # Access item by index
    index += 1  # Move to the next index

print("List loop finished!")
print("-" * 50)


# Example 4: Using while with a string
print("Example 4: Looping through a string using while")

text = "PYTHON"
i = 0  # Start index

while i < len(text):  # Loop until index reaches length of string
    print(text[i], end=" ")  # Print each character on same line
    i += 1  # Move to next character

print("\nString loop finished!")
print("-" * 50)


# Example 5: Sum numbers from 1 to 10 using while
print("Example 5: Calculating sum of numbers 1 to 10")

total = 0
num = 1

while num <= 10:  # Loop until num reaches 10
    total += num  # Add num to total
    num += 1  # Increment num

print("Total sum =", total)
print("Sum loop finished!")
print("-" * 50)



# Example 6: Sum numbers 1 to 10 with while and else
print("Example 6: Sum of numbers 1 to 10 using while and else")

total = 0
num = 1

while num <= 10:
    total += num
    num += 1

else:  # Executes after loop completes
    print("Total sum =", total)
    print("Sum loop completed successfully!")

print("-" * 50)

# ✅ Key Points:
# 1. While loops run as long as the condition is True.
# 2. Make sure to update the counter or variable inside the loop, otherwise it becomes an infinite loop.
# 3. Useful when the number of iterations is **not known in advance**.
