#Write a Python program to create a class and access its properties using an object.

# Define a class named Person
class Person:
    def __init__(self, name, age, city):
        self.name = name  # Property name
        self.age = age    # Property age
        self.city = city  # Property city

# Create an object (instance) of the Person class
person1 = Person("Arjun", 30, "Pune")

# Access and print the properties using the object
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print(f"City: {person1.city}")
