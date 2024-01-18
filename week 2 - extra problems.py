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


#################################################
# useful function when you need to handle input strings that may represent fractions and convert them into numerical values for further calculations
        
# converts string input (even fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        # If the input string contains '/', it is treated as fraction
        nd = in_string.split("/")  # Split the string at '/'
        n = float(nd[0])  # Convert the numerator to a float
        d = float(nd[1])  # Convert the denominator to a float
        ans = n / d  # Calculate the result by dividing numerator by denominator
        return ans
    else:
        # If the input string does not contain '/', it is treated as a regular float
        ans = float(in_string)  # Convert the string to a float
        return ans

result1 = string_frac("4/8")
result2 = string_frac("7.58")
print(result1) # 0.5
print(result2) # 7.58

############################
# Simplest one-step addition
def one_step_add():
    import random

    # Display problem
    a = random.randint(-4, 10)  # Generate a random integer between -4 and 10 (inclusive) for 'a'
    b = random.randint(2, 24)   # Generate a random integer between 2 and 24 (inclusive) for 'b'
    print("x + ", a, " = ", b)  # Display the addition problem in the form 'x + a = b'

    ans = float(input("x = "))  # Prompt the user to enter their answer for 'x' and convert it to a float

    answer = b - a  # Calculate the correct answer for 'x' by subtracting 'a' from 'b'

    # Test input
    if ans == answer:
        print("Correct! \n")  # If the user's answer matches the correct answer, print a success message
    else:
        print("Try again")  # If the user's answer is incorrect, print a message to try again
        print("The correct answer is ", answer, "\n")  # Display the correct answer for reference

# Call the function to play the game
one_step_add()

result3 = one_step_add()
# x +  1  =  8
# x = 7
# Correct! 

# x +  3  =  5
# x = 2
# Correct! 

# x +  8  =  23
# x = 5
# Try again
# The correct answer is  15 

# x +  -2  =  10
# x = 2
# Try again
# The correct answer is  12 

#######################################
# One-step additon with negaive numbers
def one_step_subtract():
    import random
    a = random.randint(-19,-1)
    b = random.randint(2,24)
    print(a, " + x = ", b)
    ans = float(input("x = "))

    # test
    answer = b-a
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

result5 = one_step_subtract()
# -8  + x =  5
# x = 13
# Correct! 

###################
# One-step multiply
def one_step_mult():
    # Uses string_frac(<input string>)
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print(a, "x = ", b)
    print("Round your answer to two decimal places.")
    ans_in = (input("x = "))
    answer = round(b/a,2)
    # test
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
        
result6 = one_step_mult()

# 7 x =  4
# Round your answer to two decimal places.
# x = 0.5
# Try again
# The correct answer is  0.57 

#################
# One-step divide
def one_step_div():
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print("x/", a, " = ", b)
    ans = float(input("x = "))
    answer = b*a
    # test
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

result7 = one_step_div()

# x/ 4  =  4
# x = 16
# Correct! 

###################
# Two-step problems
def two_step():
    import random
    # Uses string_frac()
    a = random.randint(1,11)
    b = random.randint(-7,12)
    c = random.randint(2,36)
    print(a, "x + ", b, " = ", c)
    print("Round answer to two decimal places")
    ans_in = input("x = ")
    answer = (c-b)/a
    # test
    if round(string_frac(ans_in),2)==round(answer,2):
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

result8 = two_step()

# 4 x +  2  =  19
# Round answer to two decimal places
# x = 4.25
# Correct! 

# 4 x +  8  =  20
# Round answer to two decimal places
# x = 5
# Try again
# The correct answer is  3.0 

###########
# test loop
for a in range(2):
    one_step_add()
    one_step_subtract()
    one_step_mult()
    one_step_div()
    two_step()
    print(" ")

two_step()
two_step()

# x +  -3  =  10
# x = 13
# Correct! 

# -13  + x =  15
# x = 17
# Try again
# The correct answer is  28 

# 1 x =  15
# Round your answer to two decimal places.
# x = 15
# Correct! 

# x/ 9  =  6
# x = 54
# Correct! 

# 7 x +  4  =  15
# Round answer to two decimal places
# x = 1.57
# Correct! 

# x +  9  =  11
# x = 2
# Correct! 

# -16  + x =  21
# x = 37
# Correct! 

# 1 x =  14
# Round your answer to two decimal places.
# x = 14
# Correct! 