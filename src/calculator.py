import math

def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    c = a - b
    return c

def multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    c = b / a
    return round(c,9)

def square(a):
    c = a * a
    return c

def squareRoot(a):
    math.sqrt(a)
    return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return  self.result

    def sub(self, a, b):
        self.result = subtraction(a, b)
        return  self.result

    def mul(self, a, b):
        self.result = multiplication(a, b)
        return  self.result

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def __square__(self, a):
        self.result =square(a)

    def __squareRoot__(self, a):
        self.result = math.sqrt(a)