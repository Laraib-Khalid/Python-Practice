# -----------------------------
# Example 1: if-else statement
# -----------------------------

age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ----------------------------------
# Example 2: if-elif-else statement
# ----------------------------------

marks = int(input("Enter your marks: "))

# Check grade based on marks
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

# ---------------------------------------
# Example 3: Nested if (if inside another)
# ---------------------------------------

num = int(input("Enter a number: "))

# Check if number is positive, and even/odd inside it
if num >= 0:
    print("The number is positive.")

    # Inner if to check even/odd
    if num % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("The number is negative.")
