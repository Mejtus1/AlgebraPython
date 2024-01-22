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