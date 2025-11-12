"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

<<<<<<< HEAD
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Cannot square root negative number!")

def hypotenuse(a, b):
    return math.hypot(a, b)
=======
>>>>>>> 834b55ab6ac01ac57c47c00396badf2b57f39f86

def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        print("Cannot divide by zero!")

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        print("Cannot take the log of a number less than or equal to zero!")

def exp(a, b):
    return a ** b

