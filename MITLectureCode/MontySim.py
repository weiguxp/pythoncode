import random
import pylab

# def MontyOpen (guess, prize):
# 	x = random.choice([1,2,3])
# 	if x == guess or x == prize:
# 		x = MontyOpen(guess, prize)
# 	return x


# def MontySim(numTrials):
# 	stickWin = 0
# 	switchWin = 0
# 	noWin = 0

# 	for i in range(numTrials):
# 		playerChoice = random.choice([1,2,3])
# 		prizeChoice = random.choice([1,2,3])
# 		montyChoice = MontyOpen(prizeChoice, playerChoice)
# 		switchChoice = MontyOpen(playerChoice, montyChoice)
# 		print 'player: %i, prize %i, montyChoice %i,  switch %i' % (playerChoice, prizeChoice, montyChoice, switchChoice)
# 		if playerChoice == prizeChoice:
# 			stickWin += 1
# 		elif switchChoice == prizeChoice:
# 			switchWin += 1
# 		else:	
# 			noWin +=1 

# 	print 'Number of stickwins %i, number of SwitchWins %i, number of no wins %i' % (stickWin, switchWin, noWin)

# MontySim(100)
def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3

def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2,3])
    if guessDoor == 2:
        return random.choice([1,3])
    return random.choice([1,2])
    
def simMontyHall(numTrials = 100, chooseFcn = montyChoose):
    stickWins = 0
    switchWins = 0
    noWin = 0
    prizeDoorChoices = [1, 2, 3]
    guessChoices = [1, 2, 3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)

def displayMHSim(simResults):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins], colors = ['r', 'g'],
              labels = ['stick', 'change'], autopct = '%.2f%%')
    pylab.title('To Switch or Not to Switch')

simResults = simMontyHall(100000, montyChoose)
displayMHSim(simResults)
pylab.figure()
simResults = simMontyHall(100000, randomChoose)
displayMHSim(simResults)
pylab.show()





