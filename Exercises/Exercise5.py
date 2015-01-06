input math

def fermat_input():
	a = raw_input('input a')
	b = raw_input('input b')

	n = raw_input('input n')
	a = int(a)
	b = int(b)
	n = int(n)

	c=a+b

	while c > 2:
		print a,'^', n, '+', b, '^', n,'=', c, '^', n
		print a**n , '+', b**n, '=', c**n
		if a**n + b**n == c**n:
			print 'fermat is wrong!'
		c -=1




fermat_input()
