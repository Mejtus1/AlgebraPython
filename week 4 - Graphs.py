# Graphing 

# Basic blank graph
import matplotlib.pyplot as plt 
fig, ax = plt.subplots()
plt.show()
# -----------------------------

# Define dimensions of graph 
import matplotlib.pyplot as plt 
fig, ax = plt.subplots()

# Dimensions
plt.axis([-10,10,-10,10])
plt.show()
# - we define dimensions of our plot 

# -----------------------------
# Better way to set dimensions 
import matplotlib.pyplot as plt 

xmin = -10 # - we set dimensions of our plot at beginning 
xmax = 10
ymin = -10
ymin = 20 # - althrough we set y-axis to 20, plot adjusts and looks like before just with bigger number

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.show()

# -----------------------------
# Display axis lines 
import matplotlib.pyplot as plt 

xmin = -10
xmax = 10
ymin = -10
ymin = 20

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0], 'b') # blue x axis     # 'b' = blue, 
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis     # values need to be set like this, because it is a line, so one side needs to be [0,0]
plt.show()                                         # draws blue line from xmin 0, to xmax 0 

# -----------------------------
# Plot one point 
import matplotlib.pyplot as plt 

xmin = -10
xmax = 10
ymin = -10
ymin = 20

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0], 'b') # blue x axis 
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis 

plt.plot([[5],[4], 'ro']) # 'ro' r=red, o=circle, 

plt.show()

# -----------------------------
# Plot several points as function 
# Plot one point 
import matplotlib.pyplot as plt 

xmin = -10
xmax = 10
ymin = -10
ymin = 20

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0], 'b') # blue x axis 
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis 

for x in range(10):
    y = 0.5*x + 1            # we plot these points and output them 
    plt.plot([x],[y], 'ro')  # linear function 

plt.show()

# -----------------------------
# Graph and table of (x,y) values 
import matplotlib.pyplot as plt 

xmin = -10
xmax = 10
ymin = -10
ymin = 20

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0], 'b') # blue x axis 
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis 

print("x \t y")
for x in range(-5,10): 
    y = 0.5*x + 1
    plt.plot([x],[y], 'ro') # plot the point 
    print(x, "\t", y)       # add them all to the table 

plt.show()

# ---------------------------------------------------------------------------------------
# Extra loop function problems 
import matplotlib.pyplot as plt 

xmin = -10
xmax = 10
ymin = -10
ymin = 20

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0], 'b') # blue x axis 
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis 

for x in range(10): 
    y = 0.5*x + 1
    plt.plot([x],[y], 'ro')

plt.show()

# -----------------------------
# array used inside plot
# drawing lines in graphs 

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)                   # - we define points as 2*(xmax-xmin), so if we chagne our window everything will chagne accordingly
x = np.linspace(xmin, xmax, points)      # xmin = where do we start 
                                         # points = how many points do I have 
                                         # xmax = where do we end
# np = numpy, linspace = function for linear graphing from numpy                                          # xmax = where do we end 
                                         
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

y = 2*x +1
plt.plot(x,y, 'pink') # x, y here represent array, x is defined in linespace function, y therefore becomes array too 
                      # r = red 
plt.show()

# -----------------------------
# - line names, graph names, values 

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

ax.set_xlabel("x values")  # - creates x values name for graph label
ax.set_ylabel("y values")  # - creates y values name for graph label 
ax.set_title("Some Graph") # - name of graph 
ax.grid(True)              # - shows grid lines on graph 

ax.set_xticks(np.arange(xmin, xmax, 1)) # - changes and draws tickmarks on graph for x line in range 1
ax.set_yticks(np.arange(ymin, ymax, 1)) # - changes and draws tickmarks on graph for y line in range 1

y = 2*x +1
plt.plot(x,y, label='y=2x+1')           # - plot line of submitted label 
plt.plot([4],[6], 'ro', label='point')  # - plot point in submitted position 
plt.plot(x,3*x, label='steeper line')   # - plot another line (we can input y value directly
plt.legend() # - shows labels           # - (x,3*x) 3*x = y value, which represents x*3 
plt.show()
