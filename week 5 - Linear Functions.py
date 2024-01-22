# Linear Functions 

# -----
# Slope
# - slope is picturing lines and their sort of angle 
# - how much is the line going up and over 

# - if we have linear line, (1,1), (2,4) ....
# - we can define slope as move up 3, move right 1 in perfect linear equation

# 4 - 1    3
# ----- = --- = 3
# 2 - 1    1

# Formula 
#     y2 - y1
# M = -------
#     x2 - x1 

# M = slope because it means how much ve MOVE on the graph 

# ---------------------------------------
# In python it is pretty straight forward 
x1 = 1
y1 = 7
x2 = 2
y2 = 10

slope = (y2 - y1) / (x2 - x1) # formula we mentioned 

print("slope = ", slope) # slope =  3.0

# ---------------------------------------------------------------------------------------
# Linear Equations 
# Slope-Intercept Equation 

#     4 - 1    3
# M = ----- = --- = 3
#     2 - 1    1

# - y intercept is where it crosses on linear 
# y = mx + b 

# b = y intercept, M = 3 from previous calculation of slope
# y = 1 , x = 1 (from our graph)

# y = mx + b 
# 1 = 3(1) + b 
# 1 = 3 + b 
# 1 - 3 = b 
# -2 = b                    final equation "y = 3x - 2" = SLOPE INTERCEPT 

# IF WE HAVE SLOPE INTERCEPT = LIENAR EQUATION we can calculate slope 
# IF WE HAVE SLOPE = WE CAN CALCULATE SLOPE INTERCEPT 

# --------------
# in python code 
x1 = 632 #1
y1 = 84 #7
x2 = 1800 #2
y2 = 8 #10

# The slope is "m"
m = (y2 - y1) / (x2 - x1)

# The y intercept is "b"
b = y1 - m*x1

# The full equation
print("y = ", m, "x + ", b) # y =  -0.06506849315068493 x +  125.12328767123287

# -----------------
# display the graph
import matplotlib.pyplot as plt

x1 = 2
y1 = 3
x2 = 6
y2 = 8

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1
print("y = ", m, "x + ", b)

# For the graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()
# y =  1.25 x +  0.5 (abd graph)