# Graphing Systems 

# - we are graphing 2 equations on x,y axis 
# - here is example of admission fees and when would be the same price with discound of 10 times 
# y = 3x + 10 and y = 4x
# - we have on our graph y = 3 and goes till 10 on x line
# - and y = 4 which is steeper slope
# - and solution to our system of equations is where they cross 
# Test:
# - they intercept at (10,40)
# - we can test our case by 
# y = 3x + 10 and y = 4x
# 40 = 3*10 + 10 = 40 
# 40 = 4x10 = 40


# - with numpy, we get insteal of looping over points, defining array of x values
# - and define how many points we want to have 
import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10

# Define how many points to plot 
points = 10*(xmax-xmin) 

# Define the array of x values once
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# line 1
y1 = 3*x
plt.plot(x, y1) 

# line 2
y2 = x**3
plt.plot(x, y2) 

ax.grid(True)
plt.show()