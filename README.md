# OOP Assignment – Classes, Inheritance & Polymorphism

This is my solution for the OOP assignment given in class.  
It contains answers for **Assignment 1** and **Activity 2**, showing how to create classes, use inheritance, and demonstrate polymorphism in Python.

## Assignment 1: Design Your Own Class
- Created a `Smartphone` class with attributes: brand, model, storage, and battery.
- Added methods:
  - `introduce()` → shows phone details.
  - `use(hours)` → simulates phone usage and reduces battery.
- Used a constructor (`__init__`) to initialize objects with unique values.
- Added `GamingSmartphone` subclass that inherits from `Smartphone`.
- Demonstrated **polymorphism** by overriding the `use()` method.

## Activity 2: Polymorphism Challenge
- Created an `Animal` base class with a `move()` method.
- Defined subclasses:
  - `Dog` → runs 🐕  
  - `Bird` → flies 🐦  
  - `Fish` → swims 🐟  
- Each subclass overrides `move()` to demonstrate **polymorphism**.

## How to Run
Clone the repository and run the Python file:

python oop_assignment.py
Example Output
Smartphones:
This is a Apple iPhone 15 with 256GB storage. 📱
iPhone 15 used for 3 hours. Battery at 70% 🔋
This is a Asus ROG Phone 7 with 512GB storage. 📱
ROG Phone 7 (Gaming Mode 🎮) used for 2 hours with liquid cooling. Battery at 60% 🔋

Animals:
The dog runs 🐕
The bird flies 🐦
The fish swims 🐟
