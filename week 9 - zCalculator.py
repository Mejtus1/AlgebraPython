# Calculator 
# - for calcualtion of week 9 word problems 

# -----------
# Proportions 
# Put a zero in for the unknown value
n1 = 1
d1 = 2
n2 = 4
d2 = 0

if n2==0:
    answer = d2 * n1 / d1
    print("n2 = ", answer)

if d2==0:
    answer = n2 * d1 / n1
    print("d2 = ", answer)

# ---------------------------------------
# Convert decimal to fraction and percent
# Get string input, which will include a decimal point
digits = input("Enter a decimal number to convert: ")

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

# -----------
# Solve for x 
import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

eq = input('Enter equation: 0 = ')

solution = solve(eq,x)
for s in solution:
    print("x = ", s)

sympy.factor(eq)

# --------------------
# Factor an expression 
import sympy
from sympy import *
import math

var('x y')

# Equation to factor
eq = x**3 - 2*x**2 - 5*x + 6


sympy.factor(eq)

# ------------------
# Solve for variable
from sympy import *
import math

# Identify all variables
var('a b c d x')

# Left and right sides of the equal sign
left = 0
right = a*x**2 + b*x + c

# Variable to solve for
variable = x

# Sympy equation left = right
eq1 = Eq(left,right)

# Sympy solve for that variable
sol = solve(eq1,variable)

# Show factored results
for s in sol:
    print(variable, " = ", s)

# ----------------------------------------
# Slope-intercept equation from two points
import matplotlib.pyplot as plt
import numpy as np

x1 = 0
y1 = 32
x2 = 100
y2 = 212

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 10
ymin = 0
ymax = 500

# For the line on the graph
y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.grid(True)
#ax.set_xticks(np.arange(xmin, xmax, 2))
#ax.set_yticks(np.arange(ymin, ymax, 1))


# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()

# ------------------------------
# Graph lines and zoom in or out
%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

# Define the graphing function
def f(zoom):
    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom
    points = 10*xmax-xmin
    x = np.linspace(xmin, xmax, points)

    fig, ax = plt.subplots()
    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'black') # black x axis
    plt.plot([0,0],[ymin,ymax], 'black') # black y axis

    # Change y1 to be any function
    y1 = 3*x
    plt.plot(x, y1)
    # Plot another line here if you want
    # y2 =
    # plt.plot(x, y2)

    ax.set_xlabel("x values")
    ax.set_ylabel("y values")
    ax.set_title("Some Graph")
    ticks = int(round((xmax-xmin)/10))
    ax.set_xticks(np.arange(xmin, xmax, ticks))
    ax.set_yticks(np.arange(ymin, ymax, ticks))
    ax.grid(True)
    plt.show()

# Set up the slider
interactive_plot = interactive(f, zoom=(1,100))
interactive_plot

# ----------------------------------
# Solve and graph a system equations
from sympy import *
from sympy.plotting import plot
from sympy import sqrt

var('x y')

# First equation set equal to zero, ready to solve
first =


# Second equation set equal to zero, ready to solve
second =


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

# -----------------------------
# Save graph and download image
# use this when graphing

from google.colab import files

# to save and output graph
plt.savefig("abc.png")
plt.show()
files.download("abc.png")