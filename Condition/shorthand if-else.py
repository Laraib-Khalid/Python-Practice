# 🟢 Example 1: Even or Odd label
numbers = [1, 2, 3, 4, 5, 6]

# Add label "Even" or "Odd" for each number
labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

print(labels)


# 🟢 Example 2: Pass/Fail result
marks = [85, 40, 70, 55, 30]

# Students with >= 50 marks pass, otherwise fail
results = ["Pass" if m >= 50 else "Fail" for m in marks]

print(results)


# 🟢 Example 3: Replace negative numbers with 0
nums = [5, -3, 8, -1, 0, 2]

# Convert negatives to 0
cleaned = [num if num >= 0 else 0 for num in nums]

print(cleaned)


# 🟢 Example 4: Shorthand condition with string formatting
temperatures = [30, 42, 18, 25]

# Label temperature as 'Hot' or 'Cold'
labels = [f"{t}°C → {'Hot' if t >= 35 else 'Cold'}" for t in temperatures]

for label in labels:
    print(label)


# 🟢 Example 5: Filter with shorthand if (no else part)
nums = [1, 2, 3, 4, 5, 6]
even_nums = [n for n in nums if n % 2 == 0]

print(even_nums)
