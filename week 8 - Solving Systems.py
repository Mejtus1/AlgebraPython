# Solving Systems of equations even without graph 

# y = 3x + 10 and y = 4x
# - if y = 3x + 10 = y 
# and 
# - if 4x = y 
# - than they must equal each other 
# 3x + 10 = 4x 
# -3        -3 
# 10 = x 
# - now we have x value, we need y value, co we plug our x value into y values
# y = 3x + 10 = y = 3*10 + 10 = 40 
# y = 4x = 4*10 = 40 
# Test: 
# 3x+10-y = 0
# 4x - y = 0 

# -------------------------------------
from sympy import *
x,y = symbols('x y')

# Equations set equal to zero
first = 2*x + y - 1  # our 1. equation
second = x - 2*y + 7 # our 1. equation

# The solution
print(linsolve([first, second], (x, y))) # linear solve function 
# {(-1, 3)}

#----------------------------------------------
from sympy import * # sympy = symbolic math python 

x,y = symbols('x y')

first = 2*x + y - 1  # our 1. equation 
second = x - 2*y + 7 # our 2. equation 

# parse finite set answer as coordinate pair
solution = linsolve([first, second], (x, y)) 
x_solution = solution.args[0][0] 
y_solution = solution.args[0][1] 

# Print a coordinate pair
print("(", x_solution, ",", y_solution, ")") 
# ( -1 , 3 )

# ------------------------------------------------------------------------
# Solve and graph. Factor to change from "0 =" to "y =" preparing to graph
# - going through loops doesnt work with sympy, going through numpy doenst work with sympy
# - we need to use with sympy own plot, 
from sympy import *
from sympy.plotting import plot # sympy own plot 
from sympy import sqrt

# variable declaration 
var('x y') 

# First equation set equal to zero, ready to solve
first = -x**2 - y + 10
#first = sqrt(x) - y

#Second equation set equal to zero, ready to solve
second = 2*x**2 - 2*y - 4
#second = -x + 5 - y

# Solve - can be linear or nonlinear equations
solution = nonlinsolve([first, second], (x, y)) 
for a in range(len(solution.args)):
    x_solution = solution.args[a][0] 
    y_solution = solution.args[a][1] 
    print("Solution = (", x_solution, ",", y_solution, ")")

# Sympy syntax for equation equal to zero, ready to factor
y_first = Eq(first,0) 

# Sympy solve for y
y1 = solve(y_first,y) 

# Same two steps for second equation
y_second = Eq(second,0) 
y2 = solve(y_second,y)

# Show factored results
print("y = ", y1[0])
print("y = ", y2[0])

# Plot solution
x = symbols('x')
xmin = -10
xmax = 10
plot(y1[0], y2[0], (x,xmin,xmax))  

# Solution = ( sqrt(6) , 4 )
# Solution = ( -sqrt(6) , 4 )
# y =  10 - x**2
# y =  x**2 - 2