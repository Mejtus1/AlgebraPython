import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x') 
# Put equation here
eq = 2*x**2 + 1 # [-sqrt(2)*I/2]   # (I = infinite)
solve(eq,x)

eq = input('Enter equation: 0 = ')
print("x = ", solve(eq,x))
# Enter equation: 0 = 3*x-6 
x = [2]

eq = 2*x - 4 
solution = solve(eq,x)
print("x = ", solution{0}) # if we have multiple solutions we can have them assigned like this in array
# displays solution index 0 
# x = 2

# multiple answers and we want to output all of them (using for loop)
eq - inpit('Enter equation: 0 = ')
solution = solve(eq,x)
for s in solution:
    print("x = ", s)
# enter equation: 0 = (x-1)*(x+2)*(x+3)
# x = -2 
# x = 1 
# x = 3    (outputs all 3 solutions)



