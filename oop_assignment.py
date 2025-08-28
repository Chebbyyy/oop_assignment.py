# Assignment 1: Create your own class with attributes, methods, constructors, and inheritance

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  # default battery level

    def introduce(self):
        print(f"This is a {self.brand} {self.model} with {self.storage}GB storage. ")

    def use(self, hours):
        self.battery -= hours * 10
        if self.battery < 0:
            self.battery = 0
        print(f"{self.model} used for {hours} hours. Battery at {self.battery}% ")

# Inheritance example: GamingSmartphone extends Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    # Polymorphism: overriding the use() method
    def use(self, hours):
        self.battery -= hours * 20  # gaming drains battery faster
        if self.battery < 0:
            self.battery = 0
        print(f"{self.model} (Gaming Mode ) used for {hours} hours with {self.cooling_system} cooling. Battery at {self.battery}% ")


# Activity 2: Polymorphism Challenge with animals
class Animal:
    def move(self):
        print("The animal moves...")

class Dog(Animal):
    def move(self):
        print("The dog runs ")

class Bird(Animal):
    def move(self):
        print("The bird flies ")

class Fish(Animal):
    def move(self):
        print("The fish swims ")


# Example usage of both parts
if __name__ == "__main__":
    print("Smartphones:")
    phone1 = Smartphone("Apple", "iPhone 15", 256)
    phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, "liquid cooling")

    phone1.introduce()
    phone1.use(3)

    phone2.introduce()
    phone2.use(2)

    print("\nAnimals:")
    animals = [Dog(), Bird(), Fish()]
    for animal in animals:
        animal.move()
