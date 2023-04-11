#
# CS1010S --- Programming Methodology
#
# Side Quest 1.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(params):
    
    return

# Test
show(egyptian(make_cross(rcross_bb), 5))





#horizontal row
def hor_row(pic,n):
    return quarter_turn_right(stackn(n-2,quarter_turn_left(pic)))

#top row + middle + bottom row
def middle(pic,n):
    return stack_frac(1/n,hor_row(pic,n),(stack_frac((n-2)/(n-1), pic, hor_row(pic,n))))

#side row
def side_row(pic,n):
    return stackn(n,pic)

#whole
def egyptian(pic,n):
    return quarter_turn_right(stack_frac(1/n, quarter_turn_left(side_row(pic,n)),stack_frac((n-2)/(n-1),quarter_turn_left(middle(pic,n)),quarter_turn_left(side_row(pic,n)))))
