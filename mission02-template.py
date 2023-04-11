#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic,n):
    if n==1:
        return pic
    else:
        return stack(pic,beside(fractal(pic,n-1),fractal(pic,n-1)))
    # Fill in code here
    return

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic,n):
    j,i = quarter_turn_right(stackn(2**(n-1),quarter_turn_left(pic))),n
    while i>1:
        j = stack( quarter_turn_right(stackn(2**(i-2),quarter_turn_left(pic))), j )
        i = i-1
    return j
    # Fill in code here
    return

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(a,b,n):
    if n==1:
        return a
    else:
        return stack(a,beside(dual_fractal(b,a,n-1),dual_fractal(b,a,n-1)))
    # Fill in code here
    return

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(a,b,n):
    if n%2!=0:
        j,i = quarter_turn_right(stackn(2**(n-1),quarter_turn_left(a))),n
    else:
        j,i = quarter_turn_right(stackn(2**(n-1),quarter_turn_left(b))),n
    while i>1:
        if i%2!=0:
            j = stack( quarter_turn_right(stackn(2**(i-2),quarter_turn_left(b))), j )
        else:
            j = stack( quarter_turn_right(stackn(2**(i-2),quarter_turn_left(a))), j )
        i = i-1
    return j
    # Fill in code here
    return

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(a,b,c,d):
    return overlay( (overlay(beside( stack(d,blank_bb) , stack(blank_bb,blank_bb) ),beside( stack(blank_bb,c) , stack(blank_bb,blank_bb) ))) , (overlay(beside( stack(blank_bb,blank_bb) , stack(blank_bb,b) ),beside( stack(blank_bb,blank_bb) , stack(a,blank_bb) ))) )
    # Fill in code here
    return

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
