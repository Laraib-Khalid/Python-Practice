class Employee:
    # 👇 Class variable (shared by all employees)
    company_name = "Tech Solutions"

    def __init__(self, name, salary):
        # 👇 Instance variables (unique for each employee)
        self.name = name
        self.salary = salary

    # ✅ Instance Method
    def show_details(self):
        """Works with instance variables (uses self)."""
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

    # ✅ Class Method
    @classmethod
    def change_company(cls, new_name):
        """Works with class variables (uses cls)."""
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")

    # ✅ Static Method
    @staticmethod
    def is_work_day(day):
        """
        Doesn't use self or cls.
        Used for general-purpose logic related to the class.
        """
        if day.lower() in ['saturday', 'sunday']:
            return False
        return True


# -------------------------------
# Create Employee objects
# -------------------------------
e1 = Employee("Ali", 50000)
e2 = Employee("Sara", 60000)

# Calling Instance Method (works with object data)
e1.show_details()
e2.show_details()
print("Class Compnay name is:", Employee.company_name)

# Calling Class Method (works with class-level data)
Employee.change_company("Innovative Tech")

# Access updated class variable
print("\nUpdated company name:", Employee.company_name)

# Calling Static Method (independent logic)
print("\nIs Monday a work day?", Employee.is_work_day("Monday"))   # True
print("Is Sunday a work day?", Employee.is_work_day("Sunday"))     # False
