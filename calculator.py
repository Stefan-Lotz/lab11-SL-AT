"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a,b):
    a+b
def sub(a,b):
    a-b
def mul(a,b):
    a*b
def div(a,b):
    try:
        a/b
    except ValueError:
        print("Cannont divide by zero")
def log(a,b):
    try:
        math.log(a,b)
    except ValueError:
        print("Can't log number less than or equal to zero")

def exp(a,b):
    a**b
