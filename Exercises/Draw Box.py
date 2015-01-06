def add_space(num_spaces, target_string):
	repeart_unit = ' '
	target_string = repeart_unit*num_spaces
	return target_string

def right_align(target_string):
	spaces_needed = 70 - len(target_string)
	target_string = add_space(spaces_needed, target_string) + target_string
	print target_string


def print_multiple(print_what, print_times, target_string):
	target_string = target_string + print_what*print_times
	return target_string

def boxtop(n):
	output = '+'
	while n > 0:
		output = print_multiple('-',4,output)
		output = print_multiple('+',1,output)
		n = n-1

	print output

def boxbody(n):
	output = '/'
	while n >0:
		output = print_multiple(' ',4, output)
		output = print_multiple('/',1, output)
		n -= 1
	print output

def do_n(f,n):
	while n > 0:
		f()
		n -= 1

def box(num_col,num_rows):
	boxtop(num_col)
	while num_rows > 0:
		boxbody(num_col)
		boxbody(num_col)
		boxtop(num_col)
		num_rows -=1

box(8,8)