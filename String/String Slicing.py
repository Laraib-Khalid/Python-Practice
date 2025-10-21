# String Slicing Examples

text = "HelloLaraib"

# Basic slicing
print(text[0:5])    # Output: Hello   (characters from index 0 to 4)
print(text[5:11])   # Output: Laraib  (characters from index 5 to 10)

# Omitting start or end index
print(text[:5])     # Output: Hello   (from start to index 4)
print(text[5:])     # Output: Laraib  (from index 5 to end)

# Using step value
print(text[::2])    # Output: Hloaab   (every 2nd character)
print(text[::-1])   # Output: biaraLolleH  (reverses the string)
