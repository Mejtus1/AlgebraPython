# Fractions and Decimals 
# how to convert from one to another 
# "out of" = divide

#   1
#  --- = 0.1 = one tenth
#   10

#   1
#  --- = 0.01 = one hendreth 
#  100 

#          234                     4
# 0.234 = ------            0.4 = ---
#          1000                    10

# Repeating decimals 
#      _
# 0.3333
# How to deal with this ? 
#              _
#   10x = 3.3333
# -   x = 0.3333
# --------------
#    9x = 3    (9/9 = 1x , 3/9 = 3/9)
#          3
#     x = ---
#          9

#              _
#   10x = 4.4444
# -   x = 0.4444
# --------------
#    9x = 4
#    x = 9/4

#              __ 
# 100x = 9.090909   (when we have double digit that is repeating we multiply it with 100 insted of 10)
# -  x = 0.090909
# ---------------
#  99x = 9 
#    x = 9/99 = 1/11 (we reduce it)

# Convert Decimals to fractions with code 
print(10**1) # 10
print(10**2) # 100
print(10**3) # 1000

print(10**0) # 1

print(10**-1) # 0.1
print(10**-2) # 0.01
print(10**-3) # 0.001

# Convert decimals to fractions with code EXAMPLE

# Get string input, which will include a decimal point
digits = input("Enter a decimal number to incude a decimal number ")

# Get a decimal number places as an designer 
exponent = int(len(digits))-1                   # example 0.07 = len(0.07) = 3 -1 (minus 1 because we want only decimal)
                                                # convert digits to integer
                                                # exponent = position of digits after decimal point

# Convert the input to a float number
n = float(digits)

# Use the exponent to get the numerator       
numerator = int(n * 10**exponent)                # numerator = top part of fraction

# Use the exponent to get the denominator
denominator = 10**exponent                       # decominator = bottom part of fraction 

# percent is the first two decimal places
percent = n * 100                                # float times 100 to convert it to % 

print("The decimal is ", n)
print("The fraction is ", numerator, "/", denominator)
print("The percent is", percent, " %")
# Enter a decimal number to convert: .2
# The decimal is 0.2
# fraction is 2 / 10 
# percent is 20.0 % 

