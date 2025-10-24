# ------------------------------------------------------------
# 📘 STRING FORMATTING IN PYTHON
# ------------------------------------------------------------

name = "Laraib"
age = 25
salary = 75400.5678

# ------------------------------------------------------------
# 1️⃣ f-STRING (Python 3.6+)
# ------------------------------------------------------------
# The modern, recommended, and fastest method

print(f"My name is {name}, I am {age} years old.")
print(f"My salary is ${salary:.2f}")  # format to 2 decimal places
print(f"In 5 years, I will be {age + 5} years old.")

# Alignment inside f-strings:
# < : left align, > : right align, ^ : center align
print(f"{'Name':<10}{'Age':^10}{'Salary':>10}")
print(f"{name:<10}{age:^10}{salary:>10.2f}")

# Padding numbers with zeros
print(f"Employee ID: {7:03}")  # prints 007

# ------------------------------------------------------------
# 2️⃣ str.format() METHOD
# ------------------------------------------------------------
# Older but still commonly used method

print("\nUsing format() method:")
print("My name is {}, and I am {} years old.".format(name, age))
print("My salary is ${:.2f}".format(salary))  # precision formatting

# Positional arguments
print("Name: {0}, Age: {1}, Age again: {1}".format(name, age))

# Named placeholders
print("Employee: {n}, Salary: ${s:.2f}".format(n=name, s=salary))

# Alignment with format()
print("{:<10}{:^10}{:>10}".format("Name", "Age", "Salary"))
print("{:<10}{:^10}{:>10.2f}".format(name, age, salary))

# ------------------------------------------------------------
# 3️⃣ OLD STYLE (% OPERATOR)
# ------------------------------------------------------------
# Used in older Python versions — similar to printf in C

print("\nUsing %% operator:")
print("My name is %s and I am %d years old." % (name, age))
print("My salary is $%.2f" % salary)

# Width and alignment with % formatting
print("%-10s | %5d | %10.2f" % (name, age, salary))

# ------------------------------------------------------------
# 4️⃣ WIDTH AND ALIGNMENT EXAMPLES
# ------------------------------------------------------------
# Left (<), Right (>), Center (^)
print("\nAlignment examples using f-strings:")
print(f"{'Left':<10} | {'Right':>10} | {'Center':^10}")
print(f"{123:<10} | {123:>10} | {123:^10}")

# ------------------------------------------------------------
# 5️⃣ NUMBER FORMATTING
# ------------------------------------------------------------
num = 1234567.89123

# Thousand separator using commas
print(f"\nWith comma separator: {num:,}")

# Underscore separator (useful for big numbers)
print(f"With underscore: {num:_}")

# Scientific notation
print(f"Scientific notation: {num:e}")

# Percentage format
percentage = 0.8567
print(f"Percentage: {percentage:.2%}")  # Converts to 85.67%

# ------------------------------------------------------------
# 6️⃣ NESTED FORMATTING EXAMPLE
# ------------------------------------------------------------
for i in range(1, 6):
    print(f"{i:<5} squared = {i ** 2:>5}")

# ------------------------------------------------------------
# 7️⃣ ALIGN TEXT IN TABULAR FORM
# ------------------------------------------------------------
print("\nFormatted Table:")
data = [("Ali", 23, 88.5), ("Sara", 21, 92.4), ("John", 25, 85.9)]

print(f"{'Name':<10}{'Age':<10}{'Score':<10}")
print("-" * 30)
for name, age, score in data:
    print(f"{name:<10}{age:<10}{score:<10.2f}")
