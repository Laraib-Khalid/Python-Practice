# Example: Stop the loop when a condition is met
print("Example: break in for loop")

for num in range(1, 10):
    if num == 5:  # Condition to stop loop
        print("Breaking the loop at", num)
        break  # Exit the loop completely
    print(num)

print("For loop ended\n" + "-"*50)


# Example: Skip a value in the loop
print("Example: continue in for loop")

for num in range(1, 10):
    if num == 5:  # Condition to skip value
        print("Skipping", num)
        continue  # Skip the current iteration
    print(num)

print("For loop ended\n" + "-"*50)


# Example: Stop while loop when condition is met
print("Example: break in while loop")

count = 1

while count <= 10:
    if count == 6:
        print("Breaking at", count)
        break  # Exit loop immediately
    print(count)
    count += 1

print("While loop ended\n" + "-"*50)


# Example: Skip certain iteration in while loop
print("Example: continue in while loop")

num = 0

while num < 5:
    num += 1
    if num == 3:
        print("Skipping", num)
        continue  # Skip current iteration
    print(num)

print("While loop ended\n" + "-"*50)


for i in range(1, 5):
    if i == 3:
        print("Number is", i)
        continue
    print(i)
else:
    print("This will run because loop was continue")
print("-"*50)


for i in range(1, 5):
    if i == 3:
        print("Number is", i)
        break
    print(i)
else:
    print("This won't run because loop was broken")
