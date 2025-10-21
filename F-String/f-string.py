# Example: Using f-strings in Python

name = "Laraib"       # A string variable
age = 25              # An integer variable
city = "Islamabad"    # Another string variable

# Using an f-string to insert variables into a sentence
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# ✅ Output: My name is Laraib, I am 25 years old, and I live in Islamabad.


# You can also include expressions directly inside f-strings
print(f"Next year, I will be {age + 1} years old.")
print(f"Next year, I will be {{age + 1}} years old.")

# ✅ Output: Next year, I will be 26 years old.


# f-strings also work with function calls and formatting
print(f"My name in uppercase is {name.upper()}.")

# ✅ Output: My name in uppercase is LARAIB.


# Formatting numbers (e.g., round a float to 2 decimal places)
pi = 3.14159265
print(f"The value of pi is approximately {pi:.2f}.")

# ✅ Output: The value of pi is approximately 3.14.


# Example: Using f-strings with a list of dictionaries

# A list containing multiple dictionaries
students = [
    {"name": "Laraib", "age": 25, "city": "Islamabad"},
    {"name": "Ali", "age": 23, "city": "Karachi"},
    {"name": "Sara", "age": 24, "city": "Lahore"}
]

# Loop through the list to access each student's details
for student in students:
    # Using f-string to print values from each dictionary
    print(f"Name: {student['name']}, Age: {student['age']}, City: {student['city']}")

# ✅ Output:
# Name: Laraib, Age: 25, City: Islamabad
# Name: Ali, Age: 23, City: Karachi
# Name: Sara, Age: 24, City: Lahore


# Example 2: More advanced — using index and formatting
print("\n--- Student Details with Index ---")
for index, student in enumerate(students, start=1):
    print(f"Student {index}: {student['name']} from {student['city']} is {student['age']} years old.")

# ✅ Output:
# Student 1: Laraib from Islamabad is 25 years old.
# Student 2: Ali from Karachi is 23 years old.
# Student 3: Sara from Lahore is 24 years old.


# Example 3: Using expressions inside f-string
print("\n--- Next Year Ages ---")
for student in students:
    print(f"{student['name']} will be {student['age'] + 1} next year.")

# ✅ Output:
# Laraib will be 26 next year.
# Ali will be 24 next year.
# Sara will be 25 next year.