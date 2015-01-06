import math
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.00001



def polyline(t, n, unit_distance, angle):
	"""
	Draws an arc that is split into
	n segments
	unit_distance = distance of line
	and arc angle
	"""
	for i in range(n):
		fd(t, unit_distance)
		lt(t, angle)

def flower_leaf(t, l):
	"""
	Draws an arc that is split into
	l = width of flower
	"""
	n = 40 #number of steps to complete flower
	stepangle = 360.0/n


	for i in range(n):
		current_angle = i * stepangle * 2* math.pi /360 #angle in radians
		distorted_distance = abs(math.sin(current_angle)**5 * l)
		fd(t, distorted_distance)
		lt(t, stepangle)


def poly_arc(t, radius, angle):
	"""
	Draws an arc with radius and angle(degrees)
	"""
	#circumference is  2 math.pi r
	arc_length = 2* math.pi * radius *angle / 360
	n  = int(arc_length/3) + 1
	step_distance = arc_length / n
	arc_draws = n
	polyline(t, arc_draws, step_distance, float(angle)/n)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)



def draw_circle(t, radius):
	"""
	Draws circle with radius
	"""
	draw_polygon(t, radius, 360)


def draw_flower(t, l, leafs):
	for i in range (leafs):
		flower_leaf(t, l)
		rt(t, 360/leafs)

def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

petal (bob, 70)



wait_for_user()