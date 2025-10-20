# 1️⃣ append() – Add an item to the end
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")  # Adds 'Mango' at the end
print(fruits)

# 2️⃣ extend() – Add multiple items from another iterable
fruits = ["Apple", "Banana"]
more_fruits = ["Cherry", "Mango", "Grapes"]

fruits.extend(more_fruits)  # Adds all items from more_fruits
print(fruits)


# 3️⃣ insert() – Insert item at a specific position
fruits = ["Apple", "Banana", "Cherry"]
fruits.insert(1, "Mango")  # Insert 'Mango' at index 1
print(fruits)


# 4️⃣ remove() – Remove first occurrence of a value
fruits = ["Apple", "Banana", "Cherry", "Banana"]
fruits.remove("Banana")  # Removes the first 'Banana'
print(fruits)


# 5️⃣ pop() – Remove and return an element
fruits = ["Apple", "Banana", "Cherry"]
popped = fruits.pop()  # Removes last item by default
print("Popped item:", popped)
print(fruits)

popped_index = fruits.pop(0)  # Remove item at index 0
print("Popped index 0:", popped_index)
print(fruits)


# 6️⃣ index() – Get index of first occurrence
fruits = ["Apple", "Banana", "Cherry", "Banana"]
print(fruits.index("Banana"))  # First occurrence index


# 7️⃣ count() – Count occurrences of a value
fruits = ["Apple", "Banana", "Cherry", "Banana"]
print(fruits.count("Banana"))  # How many times 'Banana' appears



# 8️⃣ reverse() – Reverse the list in-place
fruits = ["Apple", "Banana", "Cherry"]
fruits.reverse()
print(fruits)


# 9️⃣ sort() – Sort the list in ascending/descending order
numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()  # Ascending order
print("Ascending:", numbers)

numbers.sort(reverse=True)  # Descending order
print("Descending:", numbers)


# 🔟 copy() – Create a shallow copy of the list
fruits = ["Apple", "Banana", "Cherry"]
fruits_copy = fruits.copy()  # Copy the list

fruits.append("Mango")  # Modify original list
print("Original:", fruits)
print("Copy:", fruits_copy)


# 1️⃣1️⃣ clear() – Remove all items
fruits = ["Apple", "Banana", "Cherry"]
fruits.clear()  # Remove everything
print(fruits)


# 1️⃣2️⃣ List Membership
fruits = ["Apple", "Banana", "Cherry"]

print("Apple" in fruits)      # True
print("Orange" not in fruits) # True



# 1️⃣️3️⃣ Adding / Combining Lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Method 1: Using + operator
combined = list1 + list2
print("Combined:", combined)

# Method 2: Using extend()
list1.extend(list2)
print("Extended list1:", list1)

# Method 3: Using append() to add entire list as a single element
list1 = [1, 2, 3]
list1.append(list2)
print("Append list2 as single element:", list1)

# Method 4: Repeating lists
repeated = list2 * 3
print("Repeated list2 3 times:", repeated)


# 1️⃣️4️⃣ List Methods
numbers = [5, 2, 9, 1, 5, 6]

numbers.append(10)        # Add single element
print(numbers)

numbers.extend([11, 12])  # Add multiple elements
print(numbers)

numbers.insert(0, 0)      # Insert at index 0
print(numbers)

numbers.remove(5)          # Remove first occurrence of 5
print(numbers)

popped = numbers.pop()     # Remove last element
print(numbers)

numbers.reverse()          # Reverse the list
print(numbers)

numbers.sort()             # Sort ascending
print(numbers)

numbers.sort(reverse=True) # Sort descending
print(numbers)

copy_list = numbers.copy() # Shallow copy
numbers.clear()            # Remove all items
print(numbers)
print("Copy of list:", copy_list)


fruits = ["Apple", "Banana", "Cherry", "Banana"]

print(fruits.index("Banana")) # First occurrence index -> 1
print(fruits.count("Banana")) # Count occurrences -> 2
