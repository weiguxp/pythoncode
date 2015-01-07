from structshape import structshape
import math

class Point(object):
	"""This is a point in space"""

	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def __str__(self):
		return 'my current location is (%g, %g)' % (self.x, self.x)

	def distTo(self, tpl):
		x, y = tpl
		distx = self.x - x
		disty = self.y - y
		distance = (disty**2 + distx**2)**0.5
		print 'distance to target (%g,%g) is %g' % (x, y, distance)

	def __add__(self, tpl):
		x, y = tpl
		self.x += x
		self.y += y
		

myPoint = Point(10,10)
myPoint + (10, 10)

print myPoint
myPoint.distTo((0, 0))
print myPoint