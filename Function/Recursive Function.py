def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


num = 7
print(f"Number is: {num}")
print(f"Factorial: {factorial(num)}")


def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 10
print(f"Number is: {number}")
print(f"Fibonacci: {fibonacci(number)}")