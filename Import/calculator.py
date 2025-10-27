# file: calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# Only runs when executed directly, not when imported
if __name__ == "__main__":
    print("Testing calculator functions...")
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))