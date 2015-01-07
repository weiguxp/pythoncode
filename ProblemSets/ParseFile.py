def ParseF(n):
	''' opens file n and returns a list of words
	n = name of file
	'''
	fin = open(n)
	myList = []
	for line in fin:
		word = line.strip()
		myList.append(word)
	return myList

def ParsePartF(n, l):
	''' Opens a file and parses the first l words
	n = file name
	l = desired length of list'''

	myList = ParseF(n)
	return myList[:l]