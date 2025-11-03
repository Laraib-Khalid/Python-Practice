class Vehicle:   # Parent class
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):  # Child class 1
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def details(self):
        self.show()
        print(f"Car Doors: {self.doors}")

class Bike(Vehicle):  # Child class 2
    def __init__(self, brand, engine_cc):
        super().__init__(brand)
        self.engine_cc = engine_cc

    def details(self):
        self.show()
        print(f"Bike Engine: {self.engine_cc}cc")


car = Car("Toyota", 4)
bike = Bike("Honda", 150)

car.details()
print("----------------")
bike.details()
print(Car.mro())
print(Bike.mro())
