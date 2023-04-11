#
# CS1010S --- Programming Methodology
#
# Side Quest 2.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n,pic):
    i,j = 1, pic
    for i in range(n):
        j = overlay_frac( 1/(1+i) , scale( (n-i)/n , pic) , j )
    return j

# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

from math import sin, cos, pi

def helix(pic,n):
    wholepic = translate(0, 1/2 - 1/n, scale(2/n,pic) )
    i = 1
    for i in range(n+1):
        r = 1/2-1/n
        if i*(2*pi/n)<=pi/2:
            angle = pi/2 - i*(2*pi/n)
        elif pi/2 <= i*(2*pi/n) <= pi:
            angle = pi - i*(2*pi/n)
        elif pi <= i*(2*pi/n) <=3*pi/2:
            angle = 3*pi/2 - i*(2*pi/n)
        else:
            angle = pi/2 - (2*pi/n)
        wholepic = overlay_frac( 1-(1/(1+i)), wholepic, translate(r*cos(angle),r*sin(angle),scale(2/n,pic)) )
        return wholepic

show(translate(0, 1/2 - 1/n, scale(2/n,pic) ))

# Test
#show(helix(make_cross(rcross_bb), 9))
