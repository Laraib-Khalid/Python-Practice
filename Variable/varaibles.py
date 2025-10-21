# Creating a complex number using the complex() function
# Syntax: complex(real_part, imaginary_part)
a = complex(8, 2)   # This represents 8 + 2j  (j is the imaginary unit in Python)

# Integer variable
a1 = 9

# Boolean variable (True or False)
b = True

# String variable
c = "Harry"

# NoneType variable (represents absence of a value)
d = None


# Printing variables
print(a)       # Output: (8+2j)
print(a + a1)  # Adds 9 to the real part → (17+2j)
print(b)       # Output: True
print(c)       # Output: Harry
print(d)       # Output: None


# Checking the data types of all variables using type()
print("The type of a is ", type(a))    # <class 'complex'>
print("The type of a1 is ", type(a1))  # <class 'int'>
print("The type of b is ", type(b))    # <class 'bool'>
print("The type of c is ", type(c))    # <class 'str'>
print("The type of d is ", type(d))    # <class 'NoneType'>


# --------------------------
# Working with Data Structures
# --------------------------

# LIST: Ordered, mutable (changeable), allows duplicate and mixed data types
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
# list1 contains integers, floats, nested lists, and strings.
print(list1)
# Output: [8, 2.3, [-4, 5], ['apple', 'banana']]


# TUPLE: Ordered, immutable (cannot be changed), allows duplicates
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
# tuple1 contains two tuples as elements (nested tuple)
print(tuple1)
# Output: (('parrot', 'sparrow'), ('Lion', 'Tiger'))


# DICTIONARY: Unordered collection of key-value pairs
# Keys must be unique; values can be any data type.
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
# Output: {'name': 'Sakshi', 'age': 20, 'canVote': True}
