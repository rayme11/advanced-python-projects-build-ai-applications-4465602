# Introduction to Object-Oriented Programming with Python: Creating and Using Classes

# Class Definition
class Car:
  # Constructor (Initialization) - __init__ method
  def __init__(self, make, model):
    self.make = make
    self.model = model

  # Method - start_engine
  def start_engine(self):
    print(f"The {self.make} {self.model} engine is running")


# Encapsulation: Attributes (make and model) are encapsulated within the class.
# Encapsulation: Accessing attributes through self.


# Creating instances (objects) of the Car class
# Inheritance: Car is a class that can be used to create objects (instances).
# Creating the first car (object)
# Creating the second car (object)
# Abstraction: We create objects without worrying about the internal details of the Car class.

car1 = Car("Ford", "Mustang") 
car2 = Car("GMC", "Sierra")

# Accessing object attributes
print(f"I have a {car1.make} and the model is {car1.model}.")
print(f"I have a {car2.make} and the model is {car2.model}.")

# Encapsulation: Accessing object attributes (make and model) using dot notation.
# Calling object methods
# Polymorphism: Different objects (car1 and car2) can perform the same action (start_engine).
# Method Call - start_engine
car1.start_engine()
car2.start_engine()
