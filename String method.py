# Define a sample string
text = "   Hello, Laraib! Welcome to Python Programming!!!   "
text1 = "hello laraib"
# 1️⃣ Display original string
print("Original String:", repr(text))   # repr() shows hidden spaces clearly

# 2️⃣ Convert to uppercase and lowercase
print("Uppercase:", text.upper())       # Converts all letters to uppercase
print("Lowercase:", text.lower())       # Converts all letters to lowercase

# 3️⃣ Capitalize and title case
print("Capitalize:", text1.capitalize()) # Makes first letter uppercase, rest lowercase
print("Title Case:", text1.title())      # Makes first letter of every word uppercase

# 4️⃣ Remove spaces from different sides
print("Using lstrip():", repr(text.lstrip()))   # Removes spaces from the left
print("Using rstrip():", repr(text.rstrip()))   # Removes spaces from the right
print("Using strip():", repr(text.strip()))     # Removes spaces from both sides

# 5️⃣ Using rstrip() with specific characters
txt = "Hello Laraib!!!!!"
print("Before rstrip:", repr(txt))
print("After rstrip with '!':", repr(txt.rstrip("!")))  # Removes trailing exclamation marks only

# 6️⃣ Using rstrip() with multiple characters
txt2 = "Hello Laraib!?!!?"
print("After rstrip with '!?':", repr(txt2.rstrip("!?")))  # Removes both ! and ? from right side

# 7️⃣ Replace substring
print("Replace Example:", text.replace("Laraib", "Khalid"))  # Replace one word with another

# 8️⃣ Split and join
words = text.split()            # Splits string into words (default by spaces)
print("Split into list:", words)
joined = " ".join(words)        # Joins list elements back with spaces
print("Join list into string:", joined)

# 9️⃣ Find, Index, and Count substrings
print("Find 'Python':", text.find("Python"))     # Returns index of first occurrence
print("Find 'Java':", text.find("Java"))         # Returns -1 if not found
print("Count of 'o':", text.count("o"))          # Counts occurrences of a character

# 🔟 index() method → similar to find(), but raises an error if substring not found
print("Index of 'Laraib':", text.index("Laraib"))   # Works same as find() when substring exists

# ⚠️ Uncommenting below line will cause an error since 'Java' doesn't exist
# print("Index of 'Java':", text.index("Java"))   # Raises ValueError

# 11️⃣ Startswith and endswith
print("Starts with 'Hello':", text.startswith("Hello"))       # False due to leading spaces
print("After strip(), starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with '!!!':", text.endswith("!!!"))               # True

# 12️⃣ isalpha(), isalnum(), isdigit()
sample1 = "Python"
sample2 = "Python123"
sample3 = "1234"
print("Is Alpha:", sample1.isalpha())   # True → only letters
print("Is Alnum:", sample2.isalnum())   # True → letters + numbers
print("Is Digit:", sample3.isdigit())   # True → only digits

# 13️⃣ Swapcase — changes lowercase to uppercase and vice versa
print("Swapcase Example:", "HeLLo PyTHon".swapcase())

# 14️⃣ Center text with padding
print("Centered text:", "Python".center(30))
print("Centered text:", "Python".center(30, "*"))

# 15️⃣ Remove newline characters (real use case in file data)
lines = ["Hello\n", "World\n", "Python\n"]
cleaned = [line.rstrip("\n") for line in lines]  # Removes '\n' from right
print("Cleaned lines:", cleaned)

# 16️⃣ Using in and not in operators
print("'Laraib' in text:", "Laraib" in text)   # True
print("'Java' not in text:", "Java" not in text)  # True

# 17️⃣ Length of string
print("Length of text:", len(text))   # Counts characters including spaces and punctuation



# String Methods: startswith(), endswith(), and character check methods

# Example string
text = "Welcome To Python123"

# -----------------------------
# startswith() examples
# -----------------------------
print("\n--- startswith() Examples ---")
print("Does text start with 'Welcome'? →", text.startswith("Welcome"))     # ✅ True → string starts with "Welcome"
print("Does text start with 'welcome'? →", text.startswith("welcome"))     # ❌ False → case-sensitive
print("Does substring text[8:11] start with 'To'? →", text.startswith("To", 8, 11))   # ✅ True → checks substring "To "

# -----------------------------
# endswith() examples
# -----------------------------
print("\n--- endswith() Examples ---")
print("Does text end with '123'? →", text.endswith("123"))           # ✅ True → string ends with "123"
print("Does text end with 'thon'? →", text.endswith("thon"))          # ❌ False → does not end with "thon"
print("Does substring text[4:11] end with 'To'? →", text.endswith("To", 4, 11))     # ✅ True → substring ends with "To"

# -----------------------------
# isalpha() → True if all characters are alphabets (no numbers, no spaces)
# -----------------------------
print("\n--- isalpha() Examples ---")
only_alpha = "Python"
print("String:", only_alpha, "→", only_alpha.isalpha(), "→ ✅ All characters are alphabets")

mixed_text = "Python123"
print("String:", mixed_text, "→", mixed_text.isalpha(), "→ ❌ Contains digits")

# -----------------------------
# isalnum() → True if all characters are alphabets or digits (no special chars/spaces)
# -----------------------------
print("\n--- isalnum() Examples ---")
alpha_num = "Python123"
print("String:", alpha_num, "→", alpha_num.isalnum(), "→ ✅ Alphabets and digits only")

with_space = "Python 123"
print("String:", with_space, "→", with_space.isalnum(), "→ ❌ Contains space, so False")

# -----------------------------
# isdigit() → True if all characters are digits
# -----------------------------
print("\n--- isdigit() Examples ---")
num = "12345"
print("String:", num, "→", num.isdigit(), "→ ✅ All digits")

num_with_text = "123abc"
print("String:", num_with_text, "→", num_with_text.isdigit(), "→ ❌ Includes alphabets")

# -----------------------------
# islower() → True if all characters are lowercase
# -----------------------------
print("\n--- islower() Examples ---")
lower_text = "python"
print("String:", lower_text, "→", lower_text.islower(), "→ ✅ All lowercase")

print("String:", text, "→", text.islower(), "→ ❌ Mixed case, contains uppercase letters")

# -----------------------------
# isupper() → True if all characters are uppercase
# -----------------------------
print("\n--- isupper() Examples ---")
upper_text = "HELLO"
print("String:", upper_text, "→", upper_text.isupper(), "→ ✅ All uppercase")

print("String:", text, "→", text.isupper(), "→ ❌ Mixed case, not all uppercase")

# -----------------------------
# istitle() → True if each word starts with uppercase letter
# -----------------------------
print("\n--- istitle() Examples ---")
title_case = "Welcome To Python"
print("String:", title_case, "→", title_case.istitle(), "→ ✅ Each word starts with capital")

wrong_case = "Welcome to python"
print("String:", wrong_case, "→", wrong_case.istitle(), "→ ❌ Not all words are title-cased")

# -----------------------------
# isspace() → True if string only has spaces
# -----------------------------
print("\n--- isspace() Examples ---")
space_str = "     "
print("String:", repr(space_str), "→", space_str.isspace(), "→ ✅ Contains only spaces")

non_space = " Python "
print("String:", repr(non_space), "→", non_space.isspace(), "→ ❌ Contains letters, not pure spaces")


# -----------------------------
# Example: isprintable() and isspace() Methods in Python
# -----------------------------
print("\n--- isprintable() Examples ---")

str1 = "We wish you a Merry Christmas"
print("String:", str1, "→", str1.isprintable(), "→ ✅ All characters are printable (letters, spaces, punctuation)")

str1 = "We wish you a Merry Christmas\n"
print("String with newline:", repr(str1), "→", str1.isprintable(), "→ ❌ Contains non-printable character (\\n)")


# -----------------------------
# More isspace() tests (whitespace detection)
# -----------------------------
print("\n--- isspace() Detailed Examples ---")

str1 = "         "       # Using only spacebar spaces
print("String:", repr(str1), "→", str1.isspace(), "→ ✅ Contains only spaces")

str2 = "\t"              # Using Tab character
print("String: Tab character (\\t) →", str2.isspace(), "→ ✅ Tab counts as whitespace")

str3 = "   a   "         # Contains a non-space character ('a')
print("String:", repr(str3), "→", str3.isspace(), "→ ❌ Contains letter 'a', not pure whitespace")


#
# # String Methods: startswith(), endswith(), and character check methods
#
# # Example string
# text = "Welcome To Python123"
#
# # -----------------------------
# # startswith() examples
# # -----------------------------
# print(text.startswith("Welcome"))     # ✅ True → string starts with "Welcome"
# print(text.startswith("welcome"))     # ❌ False → case-sensitive
# print(text.startswith("To", 8, 11))   # ✅ True → checks substring text[8:11] which is "To "
#
# # -----------------------------
# # endswith() examples
# # -----------------------------
# print(text.endswith("123"))           # ✅ True → string ends with "123"
# print(text.endswith("thon"))          # ❌ False → does not end with "thon"
# print(text.endswith("To", 4, 11))     # ✅ True → substring text[4:11] ends with "To"
#
# # -----------------------------
# # isalpha() → True if all characters are alphabets (no numbers, no spaces)
# # -----------------------------
# only_alpha = "Python"
# print(only_alpha.isalpha())           # ✅ True → all characters are alphabets
#
# mixed_text = "Python123"
# print(mixed_text.isalpha())           # ❌ False → contains digits
#
# # -----------------------------
# # isalnum() → True if all characters are alphabets or digits (no special chars/spaces)
# # -----------------------------
# alpha_num = "Python123"
# print(alpha_num.isalnum())            # ✅ True → contains alphabets and digits
#
# with_space = "Python 123"
# print(with_space.isalnum())           # ❌ False → space not allowed
#
# # -----------------------------
# # isdigit() → True if all characters are digits
# # -----------------------------
# num = "12345"
# print(num.isdigit())                  # ✅ True → all digits
#
# num_with_text = "123abc"
# print(num_with_text.isdigit())        # ❌ False → includes alphabets
#
# # -----------------------------
# # islower() → True if all characters are lowercase
# # -----------------------------
# lower_text = "python"
# print(lower_text.islower())           # ✅ True
#
# print(text.islower())                 # ❌ False → contains uppercase letters
#
# # -----------------------------
# # isupper() → True if all characters are uppercase
# # -----------------------------
# upper_text = "HELLO"
# print(upper_text.isupper())           # ✅ True
#
# print(text.isupper())                 # ❌ False → mixed case
#
# # -----------------------------
# # istitle() → True if each word starts with uppercase letter
# # -----------------------------
# title_case = "Welcome To Python"
# print(title_case.istitle())           # ✅ True → each word starts with capital
#
# wrong_case = "Welcome to python"
# print(wrong_case.istitle())           # ❌ False → not all words are title-cased
#
# # -----------------------------
# # isspace() → True if string only has spaces
# # -----------------------------
# space_str = "     "
# print(space_str.isspace())            # ✅ True
#
# non_space = " Python "
# print(non_space.isspace())            # ❌ False
#
#
# # str1 = "We wish you a Merry Christmas"
# # print(str1.isprintable())
# #
# # str1 = "We wish you a Merry Christmas\n"
# # print(str1.isprintable())
# # str1 = "         "       #using Spacebar
# # print(str1.isspace())
# # str2 = "  "       #using Tab
# # print(str2.isspace())
#
#
# # -----------------------------
# # Example: isprintable() and isspace() Methods in Python
# # -----------------------------
#
# # 1️⃣ isprintable() → Returns True if all characters are printable (i.e. visible characters like letters, numbers, punctuation, and spaces)
# # Non-printable characters include things like: \n (newline), \t (tab), etc.
#
# str1 = "We wish you a Merry Christmas"
# print(str1.isprintable())
# # ✅ True → All characters are printable (letters, spaces, punctuation)
#
# str1 = "We wish you a Merry Christmas\n"
# print(str1.isprintable())
# # ❌ False → Contains '\n' (newline), which is NOT a printable character
#
#
# # -----------------------------
# # 2️⃣ isspace() → Returns True if the string contains ONLY whitespace characters.
# # Whitespace includes spaces, tabs (\t), and newlines (\n)
# # -----------------------------
#
# str1 = "         "       # Using only spacebar spaces
# print(str1.isspace())
# # ✅ True → Contains only space characters
#
# str2 = "\t"              # Using Tab character
# print(str2.isspace())
# # ✅ True → Tab is also a whitespace character
#
# # For comparison
# str3 = "   a   "         # Contains a non-space character ('a')
# print(str3.isspace())
# # ❌ False → Not purely whitespace


