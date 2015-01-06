import math
from TurtleWorld import *

world = TurtleWorld()
bob= Turtle()
bob.delay = 0.00001


def convertRads(angle):
	"""Converts angle in degrees to radians"""
	return angle* 2 * math.pi / 360

def pie_slice(t, angle, length):
	op_length = 2.0 * length * math.sin(convertRads(angle)/2)
	op_angle = 180-((180 - angle)/2)

	fd(t, length)
	lt(t, op_angle)
	fd(t, op_length)
	lt(t, op_angle)
	fd(t, length)
	lt(t, 180)

def draw_pie(t, slices, l):
	for i in range(slices):
		pie_slice(t, 360/slices, l)

def draw_spiral(t, circles, radius):
	totalangle = circles * 360
	circumference = 2.0 * math.pi * radius
	n = int(circumference * circles /3)
	step_angle = float (totalangle / n)
	step_distance = circumference * circles / n

	for i in range (n):
		fd(t, (step_distance*(n-i)/n))
		lt(t, step_angle)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


def koch2(t, length):
	if length < 3:
		fd(t, length)
		return
	m = length / 3.0
	koch(t, m)
	lt(t, 60)
	koch(t, m)
	rt(t, 120)
	koch(t, m)
	lt(t, 60)
	koch(t, m)

def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)

def snowflake ():
	for i in range (3):
		koch2(bob, 100.0)
		rt(bob, 120)

def b(z):
    prod = a(z, z)
    print z, prod
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print c(x, y+3, x+y)

wait_for_user()