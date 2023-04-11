#
# CS1010S --- Programming Methodology
#
# Side Quest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    angle = angle * pi / 180
    y = velocity * sin(angle)
    x = velocity * cos(angle)
    return (x,y)

#print(get_velocity_component(30, 50)) # (43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    total_x = 0
    total_y = 0
    for planet in planets:
        M = get_mass(planet)
        planet_x = get_x_coordinate(planet)
        planet_y = get_y_coordinate(planet)
        dist_x = planet_x - current_x
        dist_y = planet_y - current_y
        dist = sqrt(dist_x**2 + dist_y**2)
        acc_x = G * get_mass(planet) * dist_x / (dist**3)
        acc_y = G * get_mass(planet) * dist_y / (dist**3)
        total_x += acc_x
        total_y += acc_y
    return (total_x,total_y)

#print(calculate_total_acceleration(planets, 0.1, 0.1)) # (-1423.6113504393045, -1425.4297228686778)

# c)
# Do not change the return statement
def f(t, Y):
    dist_x = Y[0]
    dist_y = Y[1]
    vel_x = Y[2]
    vel_y = Y[3]
    acc_x = calculate_total_acceleration(planets, dist_x, dist_y)[0]
    acc_y = calculate_total_acceleration(planets, dist_x, dist_y)[1]
    return np.array([vel_x, vel_y, acc_x, acc_y])

np.set_printoptions(precision=5)
#print(f(0.5, [0.1, 0.1, 15.123, 20.211])) # [15.123  20.211  -1423.61135  -1425.42972]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(111.3,-26.88)
77, 27.3
111.6, 27

##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)
