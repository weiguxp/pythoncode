import math
import random

def sqrt(a):
	b =20
	y = 30

	while abs(y-b)>0.01:
		b = y
		y = (b + a/b)/2.0
		
	return y

		

def test_sqrt(n):
	for i in range(n):
		y = random.randint(1,100)
		print i, " ", sqrt(y), " ", math.sqrt(y), " ", 

test_sqrt(5)


