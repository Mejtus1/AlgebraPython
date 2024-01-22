# Fractions and Decimals 
# how to convert from one to another 
# "out of" = divide

#   1
#  --- = 0.1 = one tenth
#   10

#   1
#  --- = 0.01 = one hendreth 
#  100 

#          234                     4
# 0.234 = ------            0.4 = ---
#          1000                    10

# Repeating decimals 
#      _
# 0.3333
# How to deal with this ? 
#              _
#   10x = 3.3333
# -   x = 0.3333
# --------------
#    9x = 3    (9/9 = 1x , 3/9 = 3/9)
#          3
#     x = ---
#          9

#              _
#   10x = 4.4444
# -   x = 0.4444
# --------------
#    9x = 4
#    x = 9/4

#              __ 
# 100x = 9.090909   (when we have double digit that is repeating we multiply it with 100 insted of 10)
# -  x = 0.090909
# ---------------
#  99x = 9 
#    x = 9/99 = 1/11 (we reduce it)

# Convert Decimals to fractions with code 
print(10**1) # 10
print(10**2) # 100
print(10**3) # 1000

print(10**0) # 1

print(10**-1) # 0.1
print(10**-2) # 0.01
print(10**-3) # 0.001

# Convert decimals to fractions with code EXAMPLE

# Get string input, which will include a decimal point
digits = input("Enter a decimal number to incude a decimal number ")

# Get a decimal number places as an designer 
exponent = int(len(digits))-1                   # example 0.07 = len(0.07) = 3 -1 (minus 1 because we want only decimal)
                                                # convert digits to integer
                                                # exponent = position of digits after decimal point

# Convert the input to a float number
n = float(digits)

# Use the exponent to get the numerator       
numerator = int(n * 10**exponent)                # numerator = top part of fraction

# Use the exponent to get the denominator
denominator = 10**exponent                       # decominator = bottom part of fraction 

# percent is the first two decimal places
percent = n * 100                                # float times 100 to convert it to % 

print("The decimal is ", n)
print("The fraction is ", numerator, "/", denominator)
print("The percent is", percent, " %")
# Enter a decimal number to convert: .2
# The decimal is 0.2
# fraction is 2 / 10 
# percent is 20.0 % 

###########################
# Simplest solve-for-x code
import sympy 
from sympy import symbols 
from sympy.solvers import solve 

x = symbols('x') 

# Put the equation here
eq = 2*x**2 - 4

solve(eq,x)
# [-sqrt(2), sqrt(2)]

######################################################
# Prompt for someone to enter the equation, then solve
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')
eq = input('Enter equation: 0 = ')

print("x = ", solve(eq,x))

# Enter equation: 0 = 3*x-6
x#  =  [2]

##############################
# Doing more with the solution
import sympy 
from sympy import symbols 
from sympy.solvers import solve 

x = symbols('x') 

# Put the equation here
eq = 2*x - 4

solution = solve(eq,x)
print("x = ", solution[0])
# x =  2

##################
# Multiple answers
import sympy 
from sympy import symbols 
from sympy.solvers import solve 

x = symbols('x') 

eq = input('Enter equation: 0 = ')

solution = solve(eq,x)
for s in solution:
    print("x = ", s)

# Enter equation: 0 = (x-1)*(x+2)*(x-3)
# x =  -2
# x =  1
# x =  3
    
#######################    
# Solving in other ways
from sympy import *

var('x y') 

# First equation set equal to zero, ready to solve
first = 2*x - y

# Sympy syntax for equation equal to zero, ready to factor
eq1 = Eq(first,0) 

# Sympy solve for x
sol = solve(eq1,x) 

# Show factored results
print("x = ", sol[0])

# x = y/2 

#################
# Factoring
import sympy 
from sympy import * 

var('x y') 

# Equation set equal to zero, ready to solve
#eq = x**2-4
eq = x**3 - 2*x**2 - 5*x + 6 

sympy.factor(eq)
# (x-3)(x-1)(x+2)

#############################
# Can't do string to fraction
print(3/4) # 0.75

frac = float(input("fraction = "))
print(frac)

##########################################################################################
