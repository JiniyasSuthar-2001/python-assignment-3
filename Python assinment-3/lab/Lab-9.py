#Write Python programs to demonstrate different types of inheritance (single, multiple,
# multilevel, etc.).


# Single Inheritance
# One child class inherits from one parent class.


# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Inherited method
dog.bark()





# Multiple Inheritance
# One child class inherits from multiple parent classes.


class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

# Child inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        print("Child skills:")
        Father.skills(self)
        Mother.skills(self)

child = Child()
child.skills()



# Multilevel Inheritance
# A chain of inheritance where a class inherits from a child class of another parent class.


class Grandparent:
    def heritage(self):
        print("Inheritance from Grandparent")

class Parent(Grandparent):
    def traits(self):
        print("Traits from Parent")

class Child(Parent):
    def skills(self):
        print("Skills of Child")

c = Child()
c.heritage()
c.traits()
c.skills()



# Hierarchical Inheritance
# Multiple child classes inherit from a single parent class.


class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()