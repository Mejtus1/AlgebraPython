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

# Extra problems (working with proportions and ratios)
#   2      4
# 1 -- + 3 -- - 7 
#   3      5
# python knows order of operations so we can write it like this 
print(1+2/3+3+4/5-7) 
# or it can be stored as a variable and used later
c = (1+2/3+3+4/5-7) 

# if the c is 0.444444444 never ending 
# - all never ending numbers can be mitigated and changed to fractions and ratios 
# ccc = 0.44444444
# 10ccc = 4.44444
# 9ccc = 4 
# ccc = 4/9

# algebra acrobatics (how .9999 repeating equals 1)
# ff = 0.99999999
# 10ff = 9.9999999
# 10ff = 9 (10 - 0.999999 = 9.9999 - 0.99999)
# 9ff = 9
# ff = 1

# Exchange CAD and USD 
#  1 USD     1 USD          q1   w1
# -------- = -------        -- = --
# 1.29 CAD   1.29 CAD       q2   w2
q1 = 1
q2 = 1.29
w1 = 50
w2 = 0 
# 0 means unknown value 
if w1==0:
    answer = q1 * w2 / q2
    print("USD value = ", answer) 

if w2==0:
    answer = q2 * w1 / q1
    print("CAD value = ", answer) #64.5 CAD

# Miles and km converter 
# 1 mile     1 mile          rt1   cv1
# ------- = --------         --- = ---
# 1.6 km     1.6 km          rt2   cv2
rt1 = 1
rt2 = 1.6
cv1 = 50
cv2 = 0
# 0 means unknown value 
if cv1==0:
    answr = rt1 * cv2 / rt2
    print(answr)

if cv2==0:
    answr = cv1 * rt2 / rt1
    print(answr) # 80.0 
