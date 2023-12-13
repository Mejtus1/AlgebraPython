# Algebra with Python 
# 
# Proportions 
# - ratio is ordered pair of numbers a and b, written a / b where b does not equal 0 
# - proportion is an equation in which two ratios are set equal to each other 
# - example, if there is 1 boy and 3 girls you could write ratio as: 1 : 3
# - fraction is a part of whole 
# 
# 2   5         (2/4 is a fraction but also a ratio)                    2x10=4x5
# - = -         (proportions are 2 equal ratios)                          20=20
# 4   10        (we can cross multiply if we have a proportion)
#               (we can also use it if one of the numbers is unknown)
# 3   x                                                                 3x4=xx6
# - = -                                                                  12=6x
# 6   4                                                                   x=2
# 
# Useful practice in real life
# miles/km 
# 
# 1 mile   2 miles      1.6x2=1xx
# ------ = ------        3.2=1xx
# 1.6 km   x km           x=3.2
#
# Set up a proportion 
# n1   n2
# -- = --
# d1   d2
# Put a zero in for unknown value 
n1 = 1 
d1 = 2
n2 = 0 
d2 = 16

if n2==0:
    answer = d2 * n1 / d1
    print("n2 = ", answer)

if d2==0:
    answer = d1 * n2 / n1
    print("d2 = ", answer) # n2 = 8.0 
# 21:28 