# 🎯 Bonus Learning Tip
#
# To test regex patterns interactively:
# https://regex101.com

# 1️⃣ Check if a string contains a word
import re

text = "I love Python programming"

# Search for word 'Python'
match = re.search(r"Python", text)

if match:
    print("✅ Word found!")
else:
    print("❌ Word not found")


# 2️⃣ Find all digits in string
text = "My number is 03456789012 and age is 22"

# \d = match digits
digits = re.findall(r"\d+", text)

print(digits)  # ['03456789012', '22']



# 3️⃣ Validate Email
email = "user@example.com"

# Basic email pattern
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("✅ Valid Email")
else:
    print("❌ Invalid Email")


# ✅ 4. Validate Pakistani Phone Number Format
phone = "+923145678900"

# ^\+92\d{10}$ means:
# start -> +92 -> 10 digits -> end
pattern = r"^\+92\d{10}$"

if re.match(pattern, phone):
    print("✅ Valid Number")
else:
    print("❌ Invalid Number")


# ✅ 5. Extract all words
text = "Python is awesome!"

# \w+ means: letters, digits, underscore (one or more)
words = re.findall(r"\w+", text)

print(words)  # Output: ['Python', 'is', 'awesome']



# ✅ 6. Split text by comma OR space
text = "apple, banana orange, mango"

# [ ,]+ means: one or more spaces OR commas
result = re.split(r"[ ,]+", text)

print(result)  # Output: ['apple', 'banana', 'orange', 'mango']




# ✅ 7. Replace digits with *
text = "My pin is 5678"

# Replace each digit with *
new_text = re.sub(r"\d", "*", text)

print(new_text)  # Output: My pin is ****



# ✅ 8. Extract all capital letters
text = "Hello and WELCOME To Pakistan"

# [A-Z] means: match capital letters only
caps = re.findall(r"[A-Z]", text)

print(caps)




# ✅ 9. Find all hashtags from text
text = "Learning #Python and #AI is fun!"

# #\w+ means: literal # then word characters
hashtags = re.findall(r"#\w+", text)

print(hashtags)  # Output: ['#Python', '#AI']



# ✅ 10. Check if string starts with capital letter
text = "Hello world"

# ^[A-Z] means: first character must be capital A-Z
if re.match(r"^[A-Z]", text):
    print("✅ Starts with Capital")
else:
    print("❌ Does not start with Capital")

# 📌 Quick Regex Symbols Recap
# | Pattern | Meaning                     |
# | ------- | -----------------------     |
# | `\d`    | Digit                       |
# | `\d+`   | One or more digits          |
# | `\w`    | Word character              |
# | `\w+`   | One or more word chars      |
# | `^`     | Start of string             |
# | `$`     | End of string               |
# | `[]`    | Character group             |
# | '[A-Z]'	| capital letters only        |
# | '[ ,]+'	| one or more space or comma  |
# | `{n}`   | Exactly `n` repetitions     |
# | `+`     | 1 or more repetitions       |
