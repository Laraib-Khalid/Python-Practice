class Student:
    # 🎓 Class variable — shared by all objects of the class
    school_name = "City Public School"

    def __init__(self, name, grade):
        # 👇 Instance variables — unique for each object
        self.name = name
        self.grade = grade


# Create two objects (students)
s1 = Student("Ali", "A")
s2 = Student("Sara", "B")

# Accessing instance variables
print(s1.name, s1.grade)  # Output: Ali A
print(s2.name, s2.grade)  # Output: Sara B

# Accessing class variable (same for all objects)
print(s1.school_name)  # Output: City Public School
print(s2.school_name)  # Output: City Public School

# ✅ Changing instance variable (only affects that object)
s1.grade = "A+"
print(s1.grade)  # Output: A+
print(s2.grade)  # Output: B (unchanged)

# ⚠️ Changing class variable using class name (affects all objects)
Student.school_name = "National Grammar School"
print(s1.school_name)  # Output: National Grammar School
print(s2.school_name)  # Output: National Grammar School

# ⚠️ If changed through an object, it creates a new instance variable instead of modifying class one
s1.school_name = "Private Academy"
print(s1.school_name)  # Output: Private Academy (only for s1)
print(s2.school_name)  # Output: National Grammar School
print(Student.school_name)  # Output: National Grammar School



print("\n")



# Harry Code
class Employee:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()
