class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_voer(self):
        print(f"{self.name} rolled voer.")

my_dog = Dog("White",3)
print(my_dog.name)
print(my_dog.age)
my_dog.sit()

from car import Car

my_car = Car("audi","a4",2024)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 100
my_car.read_odometer()