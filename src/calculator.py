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

def squared(a):
    c = a * a
    return c

def squareRoot(a):
    c = math.sqrt(a)
    return round(c,8)

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

    def square(self, a):
        self.result =squared(a)
        return self.result

    def squareRoot(self, a):
        self.result =squareRoot(a)
        return self.result