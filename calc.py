#!/usr/bin/env python3
""" 
This module is used to create calculation functions suc as addition, subtraction, multiplication, and division using GitHub Copilot.
"""

__author__ = "Pranav & Amogh Kulkarni"
__version__ = "0.1.0"
__license__ = "GPLv3"

def add(a, b):
    """ This function adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """ This function subtracts two numbers and returns the result."""
    return a - b

def multiply(a, b):
    """ This function multiplies two numbers and returns the result."""
    return a * b

def divide(numerator, denominator):
    """ This function divides two numbers and returns the result."""
    # check that denominator is not zero 
    if denominator == 0:
        raise ValueError("Cannot divide by zero!")
    else:
        return float(numerator) / denominator
