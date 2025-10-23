# --------------------------------------------
# 📘 Example: Python Set Methods (with comments)
# --------------------------------------------

# A set is an unordered collection of unique elements (no duplicates allowed)
fruits = {"apple", "banana", "cherry"}
print("Original Set:", fruits)

# ------------------------------------------------
# Adding elements
# ------------------------------------------------
fruits.add("orange")        # Adds a single element
print("After add():", fruits)

# Adding multiple elements using update()
fruits.update(["mango", "grapes"])  # Can take list, tuple, or another set
print("After update():", fruits)

# ------------------------------------------------
# Removing elements
# ------------------------------------------------
fruits.remove("banana")     # Removes an element (raises error if not found)
print("After remove():", fruits)

fruits.discard("kiwi")      # Removes element if present (NO error if missing)
print("After discard():", fruits)

# pop() removes and returns a random element (since sets are unordered)
removed_item = fruits.pop()
print("Removed with pop():", removed_item)
print("After pop():", fruits)

# clear() removes all elements
temp = fruits.copy()        # copy() creates a shallow copy
temp.clear()
print("After clear():", temp)

# ------------------------------------------------
# Set Operations (Mathematical)
# ------------------------------------------------
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("\nSet A:", A)
print("Set B:", B)

# Union: combines all unique elements
print("Union (A ∪ B):", A.union(B))
print("Using | operator:", A | B)

# Intersection: common elements
print("Intersection (A ∩ B):", A.intersection(B))
print("Using & operator:", A & B)

# Difference: elements in A but not in B
print("Difference (A - B):", A.difference(B))
print("Using - operator:", A - B)

# Symmetric Difference: elements in either A or B but not both
print("Symmetric Difference (A Δ B):", A.symmetric_difference(B))
print("Using ^ operator:", A ^ B)

# ------------------------------------------------
# Subset and Superset Operations
# ------------------------------------------------
C = {1, 2, 3}
D = {1, 2, 3, 4, 5}

print("\nC is subset of D:", C.issubset(D))       # True if all C in D
print("D is superset of C:", D.issuperset(C))     # True if D contains all C
print("C and B are disjoint:", C.isdisjoint(B))   # True if no elements common

# ------------------------------------------------
# Other Useful Operations
# ------------------------------------------------
# len() gives the number of elements
print("\nLength of A:", len(A))

# in keyword checks membership
print("Is 3 in A?", 3 in A)
print("Is 10 not in A?", 10 not in A)

# ------------------------------------------------
# Frozen Set (Immutable version of a set)
# ------------------------------------------------
# Once created, cannot be modified
frozen = frozenset([1, 2, 3, 4])
print("\nFrozen set:", frozen)
# frozen.add(5)  # ❌ Would raise AttributeError (frozen sets are immutable)
