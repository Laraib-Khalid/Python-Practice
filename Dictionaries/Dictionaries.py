# --------------------------------------------------------
# 📘 Example: Python Dictionary - Detailed Explanation
# --------------------------------------------------------

# A dictionary stores data in key-value pairs {key: value}
# Keys must be unique and immutable (strings, numbers, tuples)
# Values can be of any data type.

# Creating a dictionary
person = {
    "name": "Laraib",
    "age": 25,
    "city": "Lahore",
    "skills": ["Python", "Selenium", "Robot Framework"]
}
print("Original Dictionary:", person)

# --------------------------------------------------------
# Accessing elements
# --------------------------------------------------------
print("\nAccessing Values:")
print(person["name"])        # Access value using key → Laraib
print(person.get("age"))     # get() safely returns value (returns None if key doesn’t exist)

# Using get() with default value
print(person.get("email", "No email found"))  # If key missing, returns default message


# --------------------------------------------------------
# Adding or updating items
# --------------------------------------------------------
person["email"] = "laraib@example.com"   # Adds new key-value pair
person["phone"]= "1234567890"
person["age"] = 26                       # Updates existing value
print("\nAfter adding/updating:", person)


# --------------------------------------------------------
# Removing items
# --------------------------------------------------------
person.pop("city")            # Removes key and returns its value
print("After pop():", person)

person.popitem()              # Removes and returns last inserted item (random before Python 3.7)
print("After popitem():", person)

del person["age"]             # Delete specific key
print("After del:", person)


# --------------------------------------------------------
# Looping through dictionary
# --------------------------------------------------------
# Re-create for demonstration
person = {
    "name": "Laraib",
    "age": 25,
    "city": "Lahore"
}

print("\nLooping through keys:")
for key in person:
    print(key)   # Prints all keys

print("\nLooping through values:")
for value in person.values():
    print(value)  # Prints all values

print("\nLooping through items (key-value pairs):")
for key, value in person.items():
    print(f"{key} → {value}")

# --------------------------------------------------------
# Dictionary Methods
# --------------------------------------------------------
print("\nDictionary Methods Demo:")
print("Keys:", person.keys())  # Returns all keys
print("Values:", person.values())  # Returns all values
print("Items:", person.items())  # Returns all (key, value) pairs

# copy() creates a shallow copy
person_copy = person.copy()
print("Copied Dictionary:", person_copy)

# fromkeys() creates new dict from list of keys
keys = ["name", "age", "city", "data"]
new_dict = dict.fromkeys(keys, "Unknown")
print("Using fromkeys():", new_dict)

# setdefault() returns value of key if it exists, else inserts it with default value
print("\nUsing setdefault():")
print(person.setdefault("country", "Pakistan"))  # Adds new key 'country' if not present
print("After setdefault():", person)

# update() merges dictionaries
extra_info = {"profession": "QA Engineer", "company": "Onyxtec"}
person.update(extra_info)
print("After update():", person)

# --------------------------------------------------------
# Checking membership with 'in' keyword
# --------------------------------------------------------
print("\nIs 'name' key in dictionary?", "name" in person)
print("Is 'salary' key not in dictionary?", "salary" not in person)

# --------------------------------------------------------
# Nested Dictionary Example
# --------------------------------------------------------
students = {
    "student1": {"name": "Ali", "age": 20, "grade": "A"},
    "student2": {"name": "Sara", "age": 22, "grade": "B"}
}

print("\nNested Dictionary Example:")
print(students["student1"]["name"])  # Access nested key → Ali

# --------------------------------------------------------
# Dictionary Comprehension
# --------------------------------------------------------
# Create a dictionary with numbers and their squares
squares = {x: x ** 2 for x in range(1, 6)}
print("\nDictionary Comprehension (squares):", squares)

# Key as formatted string
squares = {f"Square of {x}": x ** 2 for x in range(1, 6)}
print("\nFormatted Dictionary Keys:", squares)

# --------------------------------------------------------
# len() and type()
# --------------------------------------------------------
print("\nLength of person dictionary:", len(person))
print("Type of person:", type(person))
# person.clear()              # Uncomment to remove all items
# print("After clear():", person)