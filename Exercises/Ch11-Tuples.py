import math

myString = 'hello world this is wei!'
fibDict = dict()
fibDict = {0:0, 1:1}

def SumAll(*args):
    '''Sums any number of arguments'''
    TempSum = 0.0 
    for i in args:
        TempSum += i
    return TempSum

eng2ch = dict()
eng2ch = {'one':'nihao', 'two' : 'er', 'three':'san'}

def histogram(s):
    myDict = dict()
    for letter in s:
        myDict[letter] = myDict.get(letter, 0) + 1
    return myDict

def PrintHist(h):
    '''Print keypairs in reverse alphabetical order'''
    myList = h.keys()
    myList.sort()
    revList = myList[::-1]
    for key in revList:
        print key, h[key]
    print myList

def RevLookup(h, v):
    myList = []
    for i in h:
        if h[i] == v:
            return i
    raise ValueError

def InvertDict(d):
    revDict = dict()
    for k in d:
        val = d[k]
        if val in revDict:
            revDict[val].append(k)
        else:
            revDict[val] = [k]

    return revDict

def Fibonacci(n):
    if n in fibDict:
        return fibDict[n]
    res = Fibonacci(n-1) + Fibonacci(n-2)
    fibDict[n] = res
    return res 


ackCount = {}
cache = {}
myCounter = 0
myCounter2 = 0

def Ack(m,n):
    global myCounter
    myCounter += 1

    if (m, n) in ackCount:
        return ackCount[m,n]
    if m == 0:
        ackCount[m,n] = n+1
    if n==0 and m>0:
        ackCount[m,n] = Ack(m-1, 1)
    if m>0 and n>0:
        ackCount[m,n] = Ack(m-1, Ack(m,n-1))
    return ackCount[m,n]

def ackermann(m, n):
    global myCounter2
    myCounter2 += 1

    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


primeList= [2,3]

def IsPrime(n):
    for prime in primeList:
        if n % prime == 0:
            return False
    return True

def FindPrime(n):
    for i in range (3, n):
        if IsPrime(i) == True:
            primeList.append(i)
    print primeList

def PhiFunction(n):
    phiCount = 0
    for i in range(1,n):
        if IsRelativePrime(n, i) == True:
            phiCount += 1
    return phiCount

def IsRelativePrime(m,n):
    for i in range (2, min(m,n)+1):
        if m % i ==0 and n%i ==0:
            return False
    return True

primep = 3
primeq = 11
RSAn = 33
phin = 20
e = 7
d = 3



def encrypt(n):
    return (n**e)%RSAn

print encrypt(2)



