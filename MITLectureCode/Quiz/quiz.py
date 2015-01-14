import pylab

y1 = []
y2 = []
y3 = []

for i in range (20):
	y1.append(3*i**5)
	y2.append(i**3)
	y3.append(3**i)


pylab.figure(1)
pylab.plot(y1)

pylab.figure(2)
pylab.plot(y2)
pylab.semilogy()

pylab.figure(3)
pylab.plot(y3)
pylab.semilogy()

pylab.show()
