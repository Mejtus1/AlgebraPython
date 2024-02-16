# - a lot of people have problem converting word problems into math 

#/////////////////////////////////////////////////
#|   add    |  subtract  |  multiply  |  divide  | 
#|plus      |minus       |by          |out of    |
#|more      |less        |of          |per       | 
#|increased |decreased   |factor      |quotient  | 
#|and       |gave        |times       |rate      | 
#|received  |down        |area        |divided   | 
#|up        |subtracted  |each        |each      | 
#|added to  |difference  |            |          |
#|sum       |            |            |          | 
#/////////////////////////////////////////////////                                


# Jessica is walking home from freind's house. After 2 minutes she is 1.4 miles from home. 
# Twelve minutes after leaving she is 0.9 miles from home. 
# What is her rate in miles per hour ? 
# - we have time and distance          2 minutes = 1.4 miles from home 
# - and another time and distance     12 minutes = 0.9 miles from home 
# x = time, y = distance 
# ---------------------------------------------------|
# from our calculator                               #|
# Slope-intercept equation from two points          #|
import matplotlib.pyplot as plt                     #| 
import numpy as np                                  #|
                                                    #|
x1 = 2/60                                           #|
y1 = 1.4                                            #|
x2 = 12/60                                          #|
y2 = 0.9                                            #|
                                                    #|
# Develop the equation y = mx + b                   #|
m = (y2 - y1) / (x2 - x1)                           #|
b = y1 - m*x1                                       #|
print("y = ", m, "x + ", b)                         #|
                                                    #|
# For the graph                                     #|
xmin = 0                                            #|
xmax = 3                                            #|
ymin = 0                                            #|
ymax = 3                                            #|
                                                    #|
# For the line on the graph                         #|
y3 = m*xmin + b                                     #|
y4 = m*xmax + b                                     #|
                                                    #|
# Basic setup for the graph                         #|
fig, ax = plt.subplots()                            #|
plt.axis([xmin,xmax,ymin,ymax]) # window size       #|
plt.plot([xmin,xmax],[0,0],'b') # blue x axis       #|
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis      #|
                                                    #|
# Add details to the graph                          #|
ax.set_xlabel("x values")                           #|
ax.set_ylabel("y values")                           #|
ax.grid(True)                                       #|
#ax.set_xticks(np.arange(xmin, xmax, 2))            #|
#ax.set_yticks(np.arange(ymin, ymax, 1))            #|
                                                    #|
# Plot the linear function as a red line            #|
plt.plot([xmin,xmax],[y3,y4],'r')                   #|
                                                    #|
plt.show()                                          #| y =  -2.999999999999999 x +  1.4999999999999998
# ---------------------------------------------------|

# -------------------------------------------------------------------------------------------------
# For the following exercise, determine whether equation of curve can be written as linear function 
# - linear function has no exponents 
# y = 1/4x +6                         (linear)
# 3x + 5y = 15                        (linear)
# y = 3x - 5                          (linear)
# y = 3x2squared - 2                  (non-linear)
# 3x2squared + 5y = 15                (non-linear)
# 3x + 5y2squared = 15                (non-linear)
# -2x2squared + 3y2squared = 6        (non-linear)
#     x - 3 
#  - ------- = 2y                     (linear)
#       5

# ----------------------------------------------------------------------------------------
# For the following exercises, determine whether each function is increasing or decreasing
# - slope = x coefficient 
# - just look at slope 
# - if slope is positive = increasing 
# - if slope negative = decreasing 
# f(x) = 4x + 3         (increasing)
# g(x) = 5x + 6         (increasing)
# a(x) = 5 - 2x         (decreasing)
# b(x) = 8 - 3x         (decreasing)
# h(x) = -2x + 4        (decreasing)
# k(x) = -4x + 1        (decreasing)
# j(x) = 1/2x - 3       (increasing)
# p(x) = 1/4x - 5       (increasing)
# n(x) = -1/3x - 2      (decreasing)
# m(x) = -3/8x + 3      (decreasing)

# -------------------------------------------------------------------------------------------
# for following exercises, find slope of line that passes through two given points 
# (2,4) and (4,10)           # y =  3.0 x +  -2.0
# (1,5) and (4,11)           # y =  1.75 x +  2.25
# (-1,4) and (5,2)           # y =  -0.6 x +  4.4
# (8, -2) and (4,6)          # y =  -0.2 x +  5.6
# (6,11) and (-4,3)          # y =  0.8 x +  6.199999999999999

# -------------------------------------------------------------------------------------------
# For following exercises, determine whether lines given by equations below are parallel, perpendicular or neither
# a) 4x - 7y = 10      b) 3y + x = 12      c) 3y + 4x = 12       d) 6x - 9y = 10 
#    7x + 4y = 1          -y = 8x + 1         -6y = 8x + 1          3x + 2y = 1

# -------------------------------------------------------|
# Graph lines and zoom in or out                        #|
%matplotlib inline                                      #|
from ipywidgets import interactive                      #|
import matplotlib.pyplot as plt                         #|
import numpy as np                                      #|
                                                        #|
# Define the graphing function                          #|
def f(zoom):                                            #|
    xmin = -zoom                                        #|
    xmax = zoom                                         #|
    ymin = -zoom                                        #|
    ymax = zoom                                         #|
    points = 10*xmax-xmin                               #|
    x = np.linspace(xmin, xmax, points)                 #|
                                                        #|
    fig, ax = plt.subplots()                            #|
    plt.axis([xmin,xmax,ymin,ymax]) # window size       #|
    plt.plot([xmin,xmax],[0,0],'black') # black x axis  #|
    plt.plot([0,0],[ymin,ymax], 'black') # black y axis #|
                                                        #|
    # Change y1 to be any function                      #|
    y1 = 3*x                                            #| INPUT first function 
    plt.plot(x, y1)                                     #| needs to be in y format 
    # Plot another line here if you want                #|
    # y2 =                                              #| INPUT second function 
    # plt.plot(x, y2)                                   #| needs to be in y format 
                                                        #|
    ax.set_xlabel("x values")                           #|
    ax.set_ylabel("y values")                           #|
    ax.set_title("Some Graph")                          #|
    ticks = int(round((xmax-xmin)/10))                  #|
    ax.set_xticks(np.arange(xmin, xmax, ticks))         #|
    ax.set_yticks(np.arange(ymin, ymax, ticks))         #|
    ax.grid(True)                                       #|
    plt.show()                                          #|
                                                        #|
# Set up the slider                                     #|
interactive_plot = interactive(f, zoom=(1,100))         #|
interactive_plot                                        #|
# -------------------------------------------------------|

# ------------------------------------------------------------------|
# Solve and graph a system equations                               #|
from sympy import *                                                #|
from sympy.plotting import plot                                    #|
from sympy import sqrt                                             #|
                                                                   #|
var('x y')                                                         #|
                                                                   #|
# First equation set equal to zero, ready to solve                 #|
first =                                                            #| input first equation 
                                                                   #|
# Second equation set equal to zero, ready to solve                #|
second =                                                           #| input second equation 
                                                                   #|
# Solve - can be linear or nonlinear equations                     #|
solution = nonlinsolve([first, second], (x, y))                    #|
for a in range(len(solution.args)):                                #|
    x_solution = solution.args[a][0]                               #|
    y_solution = solution.args[a][1]                               #|
    print("Solution = (", x_solution, ",", y_solution, ")")        #|
                                                                   #|
# Sympy syntax for equation equal to zero, ready to factor         #|
y_first = Eq(first,0)                                              #|
                                                                   #|
# Sympy solve for y                                                #|
y1 = solve(y_first,y)                                              #|
                                                                   #|
# Same two steps for second equation                               #|
y_second = Eq(second,0)                                            #|
y2 = solve(y_second,y)                                             #|
                                                                   #|
# Show factored results                                            #|
print("y = ", y1[0])                                               #|
print("y = ", y2[0])                                               #|
                                                                   #|
# Plot solution                                                    #| 
x = symbols('x')                                                   #|
xmin = -10                                                         #|
xmax = 10                                                          #|
plot(y1[0], y2[0], (x,xmin,xmax))                                  #|
# ------------------------------------------------------------------| 

# a) 
# first = 4*x - 7*y -10
# second = 7*x + 4*y -1
# - we need to subtract -10 and -1 which are on the other side of equation and input it in that format 

# Solution = ( 47/65 , -66/65 )
# y =  4*x/7 - 10/7
# y =  1/4 - 7*x/4

# b)
# first = 3*y + x -12 
# second = 8*x -1 + y

# Solution = ( -9/23 , 95/23 )
# y =  4 - x/3
# y =  1 - 8*x

# c)
# first = 3*y + 4*x -12
# second = 8*x + 1 + 6*y

# y =  4 - 4*x/3
# y =  -4*x/3 - 1/6
# - these two dont meet in specified range 

# d)
# first = 6*x - 9*y -10 
# second = 3*x +2*y -1
# Solution = ( 29/39 , -8/13 )
# y =  2*x/3 - 10/9
# y =  1/2 - 3*x/2


# -------------------------------------------------------------------------------------------
# For following exercises, use descriptions of each pair of lines given below to find slopes of Line 1 and Line 2 
# Is each pair of lines, parallel, perpendicular or neither ? 
# a) Line 1: passes through (0,6) and (3,-24)
#    Line 2: passes through (-1,19) and (8,-23)
#
# b) Line 1: passes through (-8,-55) and (10,89)
#    Line 2: passes through (9, -44) and (4,-14)
# 
# c) Line 1: passes through (2,5) and (5,-1)
#    Line 2: passes through (-3,7) and (3,-5)

# 1. STEP calculate Line 1 and Line 2, y = mx + b 
# ---------------------------------------------------|
# from our calculator                               #|
# Slope-intercept equation from two points          #|
import matplotlib.pyplot as plt                     #| 
import numpy as np                                  #|
                                                    #|
x1 =                                                #|
y1 =                                                #|
x2 =                                                #|
y2 =                                                #|
                                                    #|
# Develop the equation y = mx + b                   #|
m = (y2 - y1) / (x2 - x1)                           #|
b = y1 - m*x1                                       #|
print("y = ", m, "x + ", b)                         #|
                                                    #|
# For the graph                                     #|
xmin = 0                                            #|
xmax = 3                                            #|
ymin = 0                                            #|
ymax = 3                                            #|
                                                    #|
# For the line on the graph                         #|
y3 = m*xmin + b                                     #|
y4 = m*xmax + b                                     #|
                                                    #|
# Basic setup for the graph                         #|
fig, ax = plt.subplots()                            #|
plt.axis([xmin,xmax,ymin,ymax]) # window size       #|
plt.plot([xmin,xmax],[0,0],'b') # blue x axis       #|
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis      #|
                                                    #|
# Add details to the graph                          #|
ax.set_xlabel("x values")                           #|
ax.set_ylabel("y values")                           #|
ax.grid(True)                                       #|
#ax.set_xticks(np.arange(xmin, xmax, 2))            #|
#ax.set_yticks(np.arange(ymin, ymax, 1))            #|
                                                    #|
# Plot the linear function as a red line            #|
plt.plot([xmin,xmax],[y3,y4],'r')                   #|
                                                    #|
plt.show()                                          #| 
# ---------------------------------------------------|
# 2. STEP solve system of equations 
# ------------------------------------------------------------------|
# Solve and graph a system equations                               #|
from sympy import *                                                #|
from sympy.plotting import plot                                    #|
from sympy import sqrt                                             #|
                                                                   #|
var('x y')                                                         #|
                                                                   #|
# First equation set equal to zero, ready to solve                 #|
first =                                                            #| input first equation 
                                                                   #|
# Second equation set equal to zero, ready to solve                #|
second =                                                           #| input second equation 
                                                                   #|
# Solve - can be linear or nonlinear equations                     #|
solution = nonlinsolve([first, second], (x, y))                    #|
for a in range(len(solution.args)):                                #|
    x_solution = solution.args[a][0]                               #|
    y_solution = solution.args[a][1]                               #|
    print("Solution = (", x_solution, ",", y_solution, ")")        #|
                                                                   #|
# Sympy syntax for equation equal to zero, ready to factor         #|
y_first = Eq(first,0)                                              #|
                                                                   #|
# Sympy solve for y                                                #|
y1 = solve(y_first,y)                                              #|
                                                                   #|
# Same two steps for second equation                               #|
y_second = Eq(second,0)                                            #|
y2 = solve(y_second,y)                                             #|
                                                                   #|
# Show factored results                                            #|
print("y = ", y1[0])                                               #|
print("y = ", y2[0])                                               #|
                                                                   #|
# Plot solution                                                    #| 
x = symbols('x')                                                   #|
xmin = -10                                                         #|
xmax = 10                                                          #|
plot(y1[0], y2[0], (x,xmin,xmax))                                  #|
# ------------------------------------------------------------------|

####
# a) 
# STEP 1:
# x1 = 0
# y1 = 6
# x2 = 3
# y2 = -24
# solution: y =  -10.0 x +  6.0

# x1 = -1
# y1 = 19
# x2 = 8
# y2 = -71
# solution: y =  -10.0 x +  9.0

# STEP 2: 
# first = -10*x + 6 -y
# second = -10*x + 9 -y

# answer:
# y =  6 - 10*x
# y =  9 - 10*x
# lines dont intercept 

####
# b) 
# STEP 1: 
# x1 = -8
# y1 = -55
# x2 = 10
# y2 = 89
# y =  8.0 x +  9.0

# x1 = 9
# y1 = -44
# x2 = 4
# y2 = -14
# y =  -6.0 x +  10.0

# STEP 2: 
# first = 8*x + 9 -y
# second = -6*x + 10 - y

# Solution = ( 1/14 , 67/7 )
# y =  8*x + 9
# y =  10 - 6*x

####
# c) 
# STEP 1: 
# x1 = 2
# y1 = 5
# x2 = 5
# y2 = -1
# y =  -2.0 x +  9.0

# x1 = -3
# y1 = 7
# x2 = 3
# y2 = -5
# y =  -2.0 x +  1.0

# STEP 2: 
# first = 2*x + 9 -y
# second = 2*x + 1 -y

# y =  2*x + 9
# y =  2*x + 1
# lines dont intercept 


# -------------------------------------------------------------------------------------------
# A gym membership with two personal training sessions costs 125 dollars, 
# while gym membership with five personal training sessions costs 260 dollars
# What is cost per session ? 

# membership = x 
# cost = y 
# - each session must be 45 dollars 
# 2 sessions = 125
# 5 sessions = 260 

# ---------------------------------------------------|
# from our calculator                               #|
# Slope-intercept equation from two points          #|
import matplotlib.pyplot as plt                     #| 
import numpy as np                                  #|
                                                    #|
x1 =                                                #|
y1 =                                                #|
x2 =                                                #|
y2 =                                                #|
                                                    #|
# Develop the equation y = mx + b                   #|
m = (y2 - y1) / (x2 - x1)                           #|
b = y1 - m*x1                                       #|
print("y = ", m, "x + ", b)                         #|
                                                    #|
# For the graph                                     #|
xmin = 0                                            #|
xmax = 3                                            #|
ymin = 0                                            #|
ymax = 3                                            #|
                                                    #|
# For the line on the graph                         #|
y3 = m*xmin + b                                     #|
y4 = m*xmax + b                                     #|
                                                    #|
# Basic setup for the graph                         #|
fig, ax = plt.subplots()                            #|
plt.axis([xmin,xmax,ymin,ymax]) # window size       #|
plt.plot([xmin,xmax],[0,0],'b') # blue x axis       #|
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis      #|
                                                    #|
# Add details to the graph                          #|
ax.set_xlabel("x values")                           #|
ax.set_ylabel("y values")                           #|
ax.grid(True)                                       #|
#ax.set_xticks(np.arange(xmin, xmax, 2))            #|
#ax.set_yticks(np.arange(ymin, ymax, 1))            #|
                                                    #|
# Plot the linear function as a red line            #|
plt.plot([xmin,xmax],[y3,y4],'r')                   #|
                                                    #|
plt.show()                                          #| 
# ---------------------------------------------------|

# x1 = 2 
# y1 = 125
# x2 = 5 
# y2 = 260

# y = 45 x + 35 

# The membership itself must be 35 dollars and each session must be 45 dollars 