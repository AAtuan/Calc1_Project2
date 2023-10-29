import math
# Project 2 - Calc 1

# 3

x = 1

def f(x):
    output = 3*x**2 - 6*x + 1
    return output

h = 0.1

def Derivative():
    numerator = f(x+h) - f(x)
    output = numerator/h

    print("The slope of the equation at the point x = " + str(x) + " is " + str(output))

Derivative()

# 4

A = float(3)
B = float(-4)
C = float(1)

def QuadraticFormula():
    numerator1 = float(-B + math.sqrt(B**2 -4*A*C))
    numerator2 = float(-B - math.sqrt(B**2 -4*A*C))

    Result1 = numerator1/(2*A)
    Result2 = numerator2/(2*A)

    print("The first root is: " + str(Result1))
    print("The second root is: " + str(Result2))

QuadraticFormula()