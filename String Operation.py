# String Operations Examples

str1 = "Hello"
str2 = "Laraib"

# Concatenation
print(str1 + " " + str2)   # Output: Hello Laraib

# Repetition
print(str1 * 3)            # Output: HelloHelloHello

# Length of string
print(len(str2))           # Output: 6

# Membership operators
print("L" in str2)         # Output: True
print("z" not in str2)     # Output: True

# Changing case
print(str2.upper())        # Output: LARAIB
print(str2.lower())        # Output: laraib
print(str2.title())        # Output: Laraib

# String methods
sentence = "   Python is Fun!   "
print(sentence.strip())    # Removes extra spaces
print(sentence.replace("Fun", "Powerful"))  # Output: Python is Powerful!
print(sentence.split())    # Splits into list -> ['Python', 'is', 'Fun!']
