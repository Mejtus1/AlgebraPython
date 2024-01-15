# Functions 
# - taking some input and doing something to it 

input x | input y
    0   |    3
    1   |    5
    2   |    7
    3   |    9

x = 0
y = 2x + 3
y = 2x0 + 3 
y = 3

x = 1
y = 2x1 + 3 
y = 5

x = 2
y = 2x2 + 3 
y = 7

x = 3
y = 2x3 + 3
y = 9



# Function and a table of (x,y) values 
x = 5
x = 4*x + 3 # The function 

print(x,",",y)
print("x \t y") # \t = tab

for x in range(11):
    y = 4*x + 3 # The function 
    print(x, "\t", y)

# outputs table
# 5  ,  23
# x     y 
# 0     3 
# 1     7
# 2     11
# 3     15
# 4     19
# 5     23
# 6     27 


# Defning a Python function 
def f(x): 
    y = 4*x + 3 
    return y

print(5, ",", f(5)) # 5 is my 'x' value 
# (5, 23)

# a for loop 
def f(x): 
    y = 4*x + 3 
    return y

print(5, ",", f(5))

#Next, a loop
for x in range(11):
    y = 4*x + 3 # The function 
    print(x, "\t", y)

# outputs table
# 5  ,  23
# x     y 
# 0     3 
# 1     7
# 2     11
# 3     15
# 4     19
# 5     23
# 6     27 