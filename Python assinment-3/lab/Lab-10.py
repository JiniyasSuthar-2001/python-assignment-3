#Write Python programs to demonstrate method overloading and method overriding.

#Method Overloading

class Calculator:
    # Method to add varying number of arguments
    def add(self, *args):
        if len(args) == 0:
            return "No numbers to add."
        elif len(args) == 1:
            return args[0]
        else:
            total = 0
            for num in args:
                total += num
            return total

calc = Calculator()
print(calc.add())           # No numbers to add.
print(calc.add(5))          # 5
print(calc.add(1, 2, 3, 4)) # 10


#Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # Overriding the parent class method
        print("Dog barks")

class Cat(Animal):
    def sound(self):  # Overriding the parent class method
        print("Cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()  # Animal makes a sound
dog.sound()     # Dog barks
cat.sound()     # Cat meows
