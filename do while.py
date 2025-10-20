# ====================================================
# Example 1: Simulating a do-while loop in Python
# ====================================================

count = 1

while True:
    print("Count is:", count)
    count += 1

    # Condition check after execution (like do...while)
    if count > 5:
        break  # Exit loop if condition is False

print("Loop ended\n" + "-"*50)


# ====================================================
# Example 2: Taking user input until correct password
# ====================================================

while True:
    password = input("Enter password: ")

    if password == "python123":
        print("Access granted ✅")
        break  # Exit loop if password is correct
    else:
        print("Wrong password, try again.")

# ====================================================
# Example 3: Sum positive numbers until user enters 0
# ====================================================

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num < 0:
        print("Enter Positive Number")
        continue
    total += num
    if num == 0:
        break  # Stop when user enters 0

print("Total sum =", total)


# ====================================================
# Example 4: Generate random numbers until 7 appears
# ====================================================

import random

while True:
    num = random.randint(1, 10)
    print("Generated:", num)
    if num == 7:
        print("Lucky 7 found! 🎯")
        break
