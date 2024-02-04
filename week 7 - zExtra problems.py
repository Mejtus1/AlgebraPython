# Extra problems with Graph Systems 

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# line 1
y1 = x+6
plt.plot(x, y1,'-')
plt.fill_between(x, y1, ymax, facecolor='red')

# line 2
y2 = x+3
plt.plot(x, y2,'-')
plt.fill_between(x, y2, y1, facecolor='yellow')

# line 3
y3 = x-1
plt.plot(x, y3)
plt.fill_between(x, y3, y2, facecolor='green')

# line 4
y4 = x-4
plt.plot(x, y4)
plt.fill_between(x, y4, y3, facecolor='blue')

plt.show()

# -------------------------------------------------------
# interactive graphs 

%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

# Define the graphing function
def f(m, b, zoom):
    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom
    points = 10*xmax-xmin
    x = np.linspace(xmin, xmax, points)

    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'black') # black x axis
    plt.plot([0,0],[ymin,ymax], 'black') # black y axis
    
    # Line 1
    y1 = 3*x**2 - 4
    
    # Line 2
    plt.plot(x, y1)
    plt.show()
    # plt.fill_between(x, y3, y2, facecolor='blue')

# Set up the sliders
interactive_plot = interactive(f, m=(-9, 9), b=(-9, 9), zoom=(1,100))
interactive_plot

# -------------------------------------------------------
# Graphing weather data 
# - we need to install meteostat
!pip install meteostat

# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Documentation
# https://dev.meteostat.net/python/daily.html#data-structure

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 7, 31)

# Create Point for Vancouver,BC or Philadelphia, PA
#vancouver = Point(49.2497, -123.1193, 70)
philly = Point(39.97,-75.13,25)

# Get daily data for 2018
data = Daily(philly, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'prcp','snow'])
plt.show()

# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Documentation
# https://dev.meteostat.net/python/daily.html#data-structure

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 7, 31)

# Create Point for Vancouver,BC or Philadelphia, PA
#vancouver = Point(49.2497, -123.1193, 70)
philly = Point(39.97,-75.13,25)

# Get daily data for 2018
data = Daily(philly, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'prcp','snow'])
plt.show()