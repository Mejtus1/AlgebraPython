# Extra problems for linear functions 

# -----------------------------------------------------------------------------------------------------
# A town's population increases at constant rate. In 2010 population was 55000, by 2012 76000
# if this trend continues, predict population in 2016

import matplotlib.pyplot as plt
import numpy as np

x1 = 0
y1 = 55
x2 = 2
y2 = 76

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)           # 10.5
b = y1 - m*x1                       # 55
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 10
ymin = 0
ymax = 150

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("time")
ax.set_ylabel("population")
ax.grid(True)
#ax.set_xticks(np.arange(xmin, xmax, 2))
#ax.set_yticks(np.arange(ymin, ymax, 1))

# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()

# y =  10.5 x +  55.0
# graph 

# ANSWER 
# If town's population increases with this trend, it would be approximately 120 thousand by year 2016.

# -----------------------------------------------------------------------------------------------------
# Number of people afficted with common cold in winter months dropped steadily by 50 each year since 2004,
# until 2010. In 2004 875, people were inflicted. 
# Find linear function that models number of people afflicted with common cold C as function of year, t. 
# When will no one be afflicted ? 

# base values x,y
# 2004 = x = 0 
# y = 875
# y2 = 825           # WE CAN GET VALUE OF y2, x2 by simply subtracting 50 from x1 and adding 1 to y1 
# x2 = 1

# m = 50
# b = ? 

import matplotlib.pyplot as plt
import numpy as np

x1 = 0 
y1 = 875
x2 = 1
y2 = 825

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)           
b = y1 - m*x1                       
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 20
ymin = 0
ymax = 1000

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("time")
ax.set_ylabel("people inflicted")
ax.grid(True)
#ax.set_xticks(np.arange(xmin, xmax, 2))
#ax.set_yticks(np.arange(ymin, ymax, 1))

# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()

# y =  -50.0 x +  875.0
# graph 

# ANSWER 
# No one will be afflicted in 17 and a half year. 

# ----------------------------------------------------------------------------------------------------- 
# For following exercise use graph (note book, 27 page)
# showing profit y in thousands of dollars of comapany in given year, x, where x represents years since 1980
# 1. Find linear function y, where y depents on x, number of years since 1980 
# 2. Find and interpret y- intercept 

# x1 = 5
# x2 = 25
# y1 = 10000
# y2 = 4000

import matplotlib.pyplot as plt
import numpy as np

x1 = 5
y1 = 10000
x2 = 25
y2 = 4000

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)           
b = y1 - m*x1                       
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 50
ymin = 0
ymax = 15000

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("time")
ax.set_ylabel("millions of $")
ax.grid(True)
ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 1000))

# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()

# ANSWER 
# Company will go bankrupt with this linear trend in 38 years. 

# -----------------------------------------------------------------------------------------------------
# In 2004 school population was 1700, by 2012 2500
# How much did population grow between year 2004 and 2012 ? 
# What is average population growth per year ? 
# Find equation for population P of school t years after 2004 

# x1 = 0 = 2004
# y1 = 1700
# x2 = 8
# y2 = 2500

# population grow between 2004 and 2012 ? = 800 
# average population grow per year = m ? 
# equation = b = y1 - m*x1 ? 

import matplotlib.pyplot as plt
import numpy as np

x1 = 0
y1 = 1700
x2 = 8
y2 = 2500

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)           
b = y1 - m*x1                       
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 10
ymin = 0
ymax = 3000

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("time")
ax.set_ylabel("population")
ax.grid(True)
ax.set_xticks(np.arange(xmin, xmax, 1))
ax.set_yticks(np.arange(ymin, ymax, 100))

# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()
# y =  100.0 x +  1700.0

# ANSWER 
# Population grows by average 100 per year. between year 2004 and 2012. 

# -----------------------------------------------------------------------------------------------------
# Amount of garbage G produced by city with population p is given by G = f(p) in tons per week
# p is measured in thousands of people 
# 
# Town of Tola has 40000 population and produces 13 tons of garbage each week. Express it in terms of function f 
# Explain meaning of statement f(5) = 2 

# function of population = 0, than no people would mean no garbage
# - we need to input 0,0 in x1,y1

import matplotlib.pyplot as plt
import numpy as np

x1 = 0
y1 = 0
x2 = 40
y2 = 13

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)           
b = y1 - m*x1                       
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 100
ymin = 0
ymax = 50

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("thousands of people")
ax.set_ylabel("tons")
ax.grid(True)
ax.set_xticks(np.arange(xmin, xmax, 5))
ax.set_yticks(np.arange(ymin, ymax, 5))

# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()
# y =  0.325 x +  0.0 

# ANSWER 
# meaning of f(5) = 2 is 5 thousand people would produce 2 tons of garbage. 

# -----------------------------------------------------------------------------------------------------
# Number of cubic yards of dirt D, needed to cover garden with area of square feet is given by D = g(a)
# Garden of 5000ft2 requires 50 yd3 of dirt. Express this information in terms of function g. 
# Explain meaning of statement g(100) = 1 

# g(5000) = 50
# g(100) = 1 

# ANSWER
# Meaning of statement g(100) = 1 means 100 square feet requires 1rd3 of dirt. 

# -----------------------------------------------------------------------------------------------------
# Let f(t) be number of ducks in lake t years after 1990.
# Explain meaning of statement f(5)=30
# Explain meaning of statement f(10)=40

# f(5) = 30 means after five years there were 30 ducks 
# f(10) = 40 means after ten years there were 40 ducks 

# -----------------------------------------------------------------------------------------------------
# Cost of dollars of making x items is given by function C(x) = 10x + 500
# What is cost of making 25 items ? 
# Suppose maximum cost allowed is 1500

# C(25) = 10 x 25 + 500
# C(25) = 750

# Cost of making 25 items is 750 

# C(x) = 10x + 500 
# 1500 - 500 = 1000 / 10 = 100
# x = 100
# C(100) = 10 x 100 + 500
# C(100) = 1500 

# With maximum cost allowed 1500, we can make 100 items. 

# -----------------------------------------------------------------------------------------------------
# At start of trip odometer on car read 21.395 miles, at end 22,125 13.5 hours later
# What is the average speed ? 

# Formula 
#     y2 - y1    
# M = -------         
#     x2 - x1 

# 22,125 - 21,395 = 730 

# M = 730 / 13.5 
# M = 54.07 mph 

# Average speed is 54.07 hours in this trip. 
