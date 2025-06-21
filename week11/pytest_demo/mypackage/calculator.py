import math
class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def root(a, b):
        if b == 0:
            raise ValueError("Cannot take zero root of a number")
        return a ** (1 / b)

    @staticmethod
    def sine(degrees):
        radians = math.radians(degrees)
        return math.sin(radians)

    @staticmethod
    def cosine(degrees):
        radians = math.radians(degrees)
        return math.cos(radians)

    @staticmethod
    def tangent(degrees):
        radians = math.radians(degrees)
        return math.tan(radians)
    
if __name__ == "__main__":
    # Example usage
    calc = Calculator()
    print(calc.root(-2,0))