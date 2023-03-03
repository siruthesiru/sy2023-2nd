# Classes
# Serve as blueprints to describe concepts of objects;
# Created using "class" keyword along with class name (conventionally starts with uppercase)
# Contains properties and methods

class Car():
    # properties
    def __init__(self, brand, model, year_of_make, color, fuel_type):
        self.brand = brand
        self.model = model
        self.year_of_make = year_of_make
        self.color = color
        self.fuel_type = fuel_type

        # other properties can be added and assigned hard coded values
        # self.fuel = "Carrots"
        self.fuel_level = 0

    # methods
    def fill_fuel(self, carrot_number):

        print(f"Current fuel level: {self.fuel_level}%")
        print("Filling up the fuel tank...")
        self.fuel_level += carrot_number
        print(f"New fuel level: {self.fuel_level}%")

# ----------------------------------------------------------------
# New instance is created by calling the class and providing new arguments
new_car = Car("Ford", "Horse and Carriage", 1733, "brown", "Carrots")

print(f"My car is a {new_car.year_of_make} {new_car.color} {new_car.brand} {new_car.model}")

new_car.fill_fuel(20)