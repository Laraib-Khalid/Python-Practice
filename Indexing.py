# Indexing in Python

# A string example
text = "Laraib"

# Accessing characters using positive indexing (starts from 0)
print(text[0])   # Output: L
print(text[1])   # Output: a
print(text[2])   # Output: r

# Accessing characters using negative indexing (starts from -1 from the end)
print(text[-1])  # Output: b
print(text[-2])  # Output: i
print(text[-3])  # Output: a

# Indexing in lists
fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: mango

# Changing a list element using indexing
fruits[1] = "grape"
print(fruits)      # Output: ['apple', 'grape', 'cherry', 'mango']

# Nested indexing example
nested = ["hello", [10, 20, 30], "world"]
print(nested[1][2])  # Output: 30  (Accessing 2nd list’s 3rd element)
