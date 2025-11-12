"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

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