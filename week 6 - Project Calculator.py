# Proportions
# Put a zero in for the unknown value
n1 = 2
d1 = 3
n2 = 5
d2 = 0

if n2==0:
    answer = d2 * n1 / d1
    print("n2 = ", answer)

if d2==0:
    answer = n2 * d1 / n1
    print("d2 = ", answer)



# --------------
# x in equations
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

eq = input('Enter equation: 0 = ')

solution = solve(eq,x)
for s in solution:
    print("x = ", s)

sympy.factor(eq)



# -------------------
# factor square roots
import sympy
from sympy import *
import math

var('x y')

# Equation to factor
eq = x**3 - 2*x**2 - 5*x + 6


sympy.factor(eq)



# ------------------------------------------
# convert decimals to fractions and percents
# Get string input, which will include a decimal point
digits = input("Enter a decimal number to convert:")

# Get number of decimal places as an integer
exponent = int(len(digits))-1

# Convert the input to a float number
n = float(digits)

# Use the exponent to get the numerator
numerator = int(n * 10**exponent)

# Use the expoent to get the denominator
denominator = 10**exponent

# percent is the first two decimal places
percent = n * 100

# Output
print("The decimal is ", n)
print("The fraction is ", numerator, "/", denominator)
print("The percent is ", percent, " %")
