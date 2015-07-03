fin = open('sample.txt')


myList = []

for line in fin:
	word = line.split()
	print '"'+ word[0].strip()+'"' +',"China","0","0"'
