class MyData:
    # Constructor
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    # String printing
    def __str__(self):
        return f"Object for {self.name}"

    # Length of object
    def __len__(self):
        return len(self.numbers)

    # Add two objects
    def __add__(self, other):
        return self.numbers + other.numbers

    # Check equality
    def __eq__(self, other):
        return self.numbers == other.numbers

    # Greater than comparison
    def __gt__(self, other):
        return len(self.numbers) > len(other.numbers)

    # Indexing like obj[0]
    def __getitem__(self, index):
        return self.numbers[index]

    # Call method: obj() like a function
    def __call__(self):
        print(f"{self.name} object is called like a function!")

    # Destructor
    def __del__(self):
        print(f"Object {self.name} deleted")


# -------------------- Testing -----------------------

obj1 = MyData("Ali", [10, 20, 30])
obj2 = MyData("Sara", [5, 15])

print(obj1)                 # __str__
print("Length:", len(obj1)) # __len__

print("Add:", obj1 + obj2)  # __add__

print("Equal?:", obj1 == obj2)   # __eq__
print("Greater?:", obj1 > obj2)  # __gt__

print("Index 1:", obj1[1])  # __getitem__

obj1()   # __call__  ✅ calling object like function

del obj2  # __del__ called
