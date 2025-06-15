class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

# Usage
d = Dog()
d.speak()  # ✅ Inherited from Animal
d.bark()   # ✅ Defined in Dog
