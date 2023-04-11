#
# CS1010S --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:







# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(10)(0.1), 50)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

# print( profile_fn( lambda: gosper_curve(10)(0.1),1000))

# Time measurements
g1 = 35.9061999770347
g2 = 36.60770002170466
g3 = 34.23059999477118
g4 = 53.600800019921735
g5 = 52.44320002384484
g_avg =(g1+g2+g3+g4+g5)/5= 42.55770000745542


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# print( profile_fn( lambda: gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1), 1000))

#  Time measurements
ga1 = 36.27449998748489
ga2 = 37.26689997711219
ga3 = 35.59990000212565
ga4 = 35.57169999112375
ga5 = 38.56190000078641
ga_avg =(ga1+ga2+ga3+ga4+ga5)/5 = 36.65497999172658

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below
def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        scale_factor = (1/cos(theta))/2
        scaled_curve = scale(scale_factor)(curve_fn)
        left_curve = rotate(theta)(scaled_curve)
        right_curve = translate(0.5,sin(theta)*scale_factor)(rotate(-theta)(scaled_curve))
        return put_in_standard_position(connect_ends(left_curve,right_curve))
    return inner_gosperize

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))


# print(profile_fn(lambda: your_gosper_curve_with_angle( 10, lambda lvl: pi/4)(0.1), 1000))

#  Time measurements
yg1 = 1019.7469999839086
yg2 = 1072.8487000160385
yg3 = 1063.3391999872401
yg4 = 1068.251099990448
yg5 = 1089.6452000015415
yg_avg = (yg1+yg2+yg3+yg4+yg5)/5 = 1062.7662399958353

# Conclusion:
#  functions that are more customized (gosper_curve and gosper_curve_with_angle) have an advantage (in speed) as compared to functions which are more customizable (in this case,your_gosper_curve_with_angle).
#  customized functions were about 26 times faster than the customizable function

##########
# Task 2 #
##########

#  1) Yes.

#  2) every time joe_rotate is used, curve(t) will call for gosper_curve which calls for gosperize that has to go through all the levels

##########
# Task 3 #
##########
def rotate ( angle ):
    def transform ( curve ):
        def rotated_curve ( t ):
            pt = curve ( t )
            x , y = x_of ( pt ) , y_of ( pt )
            cos_a , sin_a = cos ( angle ) , sin ( angle )
            return make_point ( cos_a * x - sin_a *y , sin_a * x + cos_a * y )
        return rotated_curve
    return transform

def joe_rotate ( angle ):
    def transform ( curve ):
        def rotated_curve ( t ):
            x , y = x_of ( curve ( t )) , y_of ( curve ( t ))
            cos_a , sin_a = cos ( angle ) , sin ( angle )
            return make_point ( cos_a * x - sin_a *y , sin_a * x + cos_a * y )
        return rotated_curve
    return transform

original_rotate = rotate

trace(gosper_curve)
gosper_curve(3)(0.5)
untrace(gosper_curve)
gosper_curve(3)(0.5)

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <3>         <4>
#                      2         <5>         <10>
#                      3         <7>         <22>
#                      4         <9>         <46>
#                      5         <11>         <94>
#
#  Evidence of exponential growth in joe_rotate.

