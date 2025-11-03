class Human:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Name: {self.name}")


class Employee(Human):
    def __init__(self, name, salary):
        Human.__init__(self,name)
        self.salary = salary

    def info(self):
        print("Employee Info:")
        Human.info(self)
        print(f"Salary: {self.salary}")


class Student(Human):
    def __init__(self, name, grade):
        Human.__init__(self,name)
        self.grade = grade

    def info(self):
        print("Student Info:")
        Human.info(self)
        print(f"Grade: {self.grade}")


class WorkingStudent(Employee, Student):
    def __init__(self, name, salary, grade):
        # Employee().__init__(name, salary)
        # Student().__init__(name, grade)
        self.name = name
        self.salary = salary
        self.grade = grade

    def info(self):
        print("Working Student Info:")
        super().info()


ws = WorkingStudent("Laraib", 50000, "A")
ws.info()
print(WorkingStudent.mro())



print("-" * 50)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)


class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details()


program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()