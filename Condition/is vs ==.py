# ----------------------------------------
# Example 1: == vs is (with integers)
# ----------------------------------------

a = 10
b = 10

# == compares values
print(a == b)  # ✅ True → both have the same value (10)

# is compares memory locations (identity)
print(a is b)  # ✅ True → small integers (-5 to 256) are cached by Python

# ----------------------------------------
# Example 2: == vs is (with lists)
# ----------------------------------------

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # ✅ True → same contents
print(list1 is list2)  # ❌ False → stored in different memory locations

# Verify memory addresses
print(id(list1), id(list2))  # Different IDs


# ----------------------------------------
# Example 3: Same object reference
# ----------------------------------------

list3 = list1  # list3 points to the same object as list1

print(list3 == list1)  # ✅ True → same contents
print(list3 is list1)  # ✅ True → same memory reference

# ----------------------------------------
# Example 4: Using is with None (correct usage)
# ----------------------------------------

x = None

# 'is' is recommended when checking for None
if x is None:
    print("x is None")  # ✅ True

# Avoid using == None (less safe)
if x == None:
    print("x == None")  # ✅ Also True, but not the best practice


# ----------------------------------------
# Example 5: == vs is with strings
# ----------------------------------------

str1 = "hello"
str2 = "hello"

print(str1 == str2)  # ✅ True → same text
print(str1 is str2)  # ✅ True (sometimes) because of string interning (Python optimization)

# But not always guaranteed for larger strings
str3 = "".join(["he", "llo"])
print(str3 == str1)  # ✅ True → same content
print(str3 is str1)  # ❌ False → different memory object
