# Algebra
# Solving for x 
# - we are doing opposite on both sites of the equation: 

# + 
# x + 3 = 9 
#    -3  -3 
# x = 2

# -
# x - 2 = 10
#    +2   +2 
# x = 12  

# *
# 3x = 12 
# 3/3   12/3
# x = 4

# x              x
# -- = 2     (4) -- = 2 (4)
# 4              4
# x = 8

#######################################################################################
# these were easy problems but if we have harder ones we need to follow algebra methods

# x + 7.2 = 11.1 
#    -7.2   -7.2   
# x = 3.9

# two step equation
# 4x + 6 = 22
#     -6   -6        #(first step)
# 4/4x = 16 / 4      #(second step)
# x = 4

#######################################################################################
# Python proportions and algebra using Sympy
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x') # sympy module import, we specify x as symbol
# Put equation here
eq = x -2 # x = [2]
eq = x**2 - 2 # x = [-sqrt(2), sqrt(2)]
eq = x**2 - 4 # x = [-2, 2]
print("x = ", sole(eq,x))

