class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call parent method
        print(f"{self.name} barks")

# Usage
dog = Dog("Rocky", "Labrador")
dog.speak()

# Super() -> referernce to Parent Class
