# Project 2 - Calc 1
import math

# 3

x = 4

def f(x):
    output = 3*x**2 - 6*x + 1
    return output

h = 1e-6

def Derivative():
    numerator = f(x+h) - f(x)
    output = numerator/h

    print("The slope of the equation at the point x = " + str(x) + " is " + str(round(output,4)))

Derivative()

# 4
import math

def QuadraticFormula(A, B, C):
    numerator1 = float(-B + math.sqrt(B**2 -4*A*C))
    numerator2 = float(-B - math.sqrt(B**2 -4*A*C))

    Result1 = numerator1/(2*A)
    Result2 = numerator2/(2*A)

    print("The first root is: " + str(Result1))
    print("The second root is: " + str(Result2))

QuadraticFormula(3, -4, 1)