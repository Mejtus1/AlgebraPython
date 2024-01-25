# ---------
# Factoring  
# - any factor is something that we multiply
# 6 = 2 x 3 
# 15 = 5 x 3 

# Factoring in fraction 
# 
# - both are divisible by 3 
#   6     2
# ---- = ---
#  15     5

# - we can factor multiple times (if we dont see it for that first time)
#    6     3      1
#  ---- = ---- = ---
#   24     12     4
#      /2     /3

# Common factors, redistributing factors
# 4x + 16
# 4 (x + 4) 
# OR 
# x + 4 

# Remainders
# - remainders are important in finding factors
# - because a remainder means a number is not a factor 
print(5%3) # 2 = finds remainder 
print(31%10) # 1 

# -----------------------------------
# Use modulus in loop to find factors 
number = 12 
# Find all factors 
for test_factor in range(1,number+1): 
    if number%test_factor==0: 
        print(test_factor) 
# 1
# 2
# 3
# 4
# 6
# 12
# all of those are factors of 12 
        
# ---------------------------
# Fractions to lowest numbers 
numerator = 12
denominator = 24
factor = 1

# Find greatest common factor 
for test_factor in range(1,denominator+1): 
    if numerator%test_factor==0 and denominator%test_factor==0:
        factor = test_factor 

# Divide out greatest common factor 
n = int(numerator/factor) 
d = int(denominator/factor) 

print("original: ", numerator, "/", denominator) 
print("reduced: ", n, "/", d) 
# original:  12 / 24
# reduced:  1 / 2


# -----------------------------
# Decimal numbers to fractions

# Get decimal number to convert
digits = input("Enter a decimal number to convert: ") 

# Convert to fraction 
exponent = int(len(digits))-1 
n = float(digits) 
numerator = int(n * 10**exponent) 
denominator = 10**exponent 

# Reduce that fraction
factor = 1 
for test_factor in range(1,denominator+1): 
    if numerator%test_factor==0 and denominator%test_factor==0: 
        factor = test_factor 

# Divide out greatest common factor 
num = int(numerator/factor) 
den = int(denominator/factor) 

# Output 
print("The decimal is ", n) 
print("The fraction is ", num, "/", den) 
# Enter a decimal number to convert: .02
# The decimal is  0.02
# The fraction is  1 / 50

# ----------------------
# factoring square roots 
import math
print(math.sqrt(24)) 
# 4.898979485566356

# -------------------------------
# Factoring Square roots 

# Divide out any perfect square factors
# Calculate square root of 12 = square root of 4 * 3 = 4 is perfect square and answer is = 2 to square root of 3
import math

# number to factor
n = 12 

# This variable will change
max_factor = 1 

# The key ingredient
upper_limit = math.floor(math.sqrt(n)) + 1 

# Find square factors
for maybe_factor in range(1,upper_limit): 
    if n % (maybe_factor**2) == 0: 
        max_factor = maybe_factor 

# Results so far
print("n = ", n)                             # 12
print("Square rooted factor = ", max_factor) # 2    # number in front of square root      # OUTSIDE 
print("Square factor = ", max_factor**2)     # 4    # number we divide                    # BETWEEN STEP 
print("integer: ", n/(max_factor**2))        # 3    # number after square root            # INSIDE 

# -----------------------------------
# add visual effects for Square roots 
import math
import sympy
from sympy import symbols

n = 24 

# Use these variables
upper_limit = math.floor(math.sqrt(n)) + 1 
max_factor = 1 
other_factor = 1 
square_root = 1 

# Slightly different variable strategy
for maybe_factor in range(1, upper_limit): 
    if n % (maybe_factor**2) == 0: 
        max_factor = maybe_factor**2 

# Divide out the greatest square factor
other_factor = n/max_factor 

# Output variables
square_root = int(math.sqrt(max_factor)) 
other_factor = int(other_factor) 
output = square_root*sympy.sqrt(other_factor) 

# Sympy output without print statement - must be last line
output 


# EXPLAINED previous code 
# - this script utilizes math and sympy modules for mathematical operations and symbolic computation

# Initialization:
n = 24
upper_limit = math.floor(math.sqrt(n)) + 1
max_factor = 1
other_factor = 1
square_root = 1
# - n is given number (in this case, 24)
# - upper_limit is calculated as floor of square root of n plus 1

# Loop to Find Square Factors:
for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
        max_factor = maybe_factor**2
# - loop iterates through range from 1 to upper_limit
# - checks if square of maybe_factor is factor of n, if it is, it updates max_factor with square of maybe_factor
# - loop continues until it finds greatest square factor of n

# Divide out Greatest Square Factor:
other_factor = n / max_factor
# - other_factor is calculated as result of dividing n by greatest square factor (max_factor)

# Output Variables:
square_root = int(math.sqrt(max_factor))
other_factor = int(other_factor)
output = square_root * sympy.sqrt(other_factor)
# square_root is calculated as integer square root of max_factor
# other_factor is converted to integer
# output is calculated as product of square_root and square root of other_factor using sympy module

