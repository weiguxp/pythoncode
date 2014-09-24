import string

file = open('Book.txt', 'r')

lines = file.readlines()

print len(lines)

words = []

for line in lines:
	wordlist = line.split()
	for w in wordlist:
		words.append(w)

letters = []

for letter in words:
	letterlist = list(letter)
	for l in letterlist:
		letters.append(list(l)) 

print len(letters)

# for w in lines:
# 	words.append(w.readline()) 

# print len(words)

# print words


