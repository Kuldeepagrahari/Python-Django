class Calculator:
    def calculate(self, a, b):
        print(f"Adding {a} + {b} = {a + b}")

class ScientificCalculator(Calculator):
    # Method Overriding
    def calculate(self, a, b=None, operation='minus'):
        if b is None:
            print(f"Square of {a} = {a * a}")
        elif operation == 'minus':
            print(f"Subtracting {a} - {b} = {a - b}")
        elif operation == 'power':
            print(f"{a} raised to {b} = {a ** b}")
        else:
            print("Unknown operation")

# Usage
basic = Calculator()
sci = ScientificCalculator()

print("▶ Using Parent Class:")
basic.calculate(5, 3)            # Regular add

print("\n▶ Using Child Class with Overriding:")
sci.calculate(5, 3)              # Add (overridden)
sci.calculate(2, 3, 'power')     # Power (overloading)
sci.calculate(4)                # Square (overloading)
