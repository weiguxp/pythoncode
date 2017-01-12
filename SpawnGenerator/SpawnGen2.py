import random

spawnList = []

class gameMonster(object):
	"""docstring for gameMonster"""
	def __init__(self, monsterAsset, speed, hitPoint, atk, aiBehaviour):
		self.monsterAsset  = str(monsterAsset)
		self.speed  = float(speed)
		self.hitPoint  = int(hitPoint)
		self.atk  = int(atk)
		self.aiBehaviour = str(aiBehaviour)


class SpawnRecord(object):
	def __init__(self, waveId, spawnDelay, spawnPosition, monsterName):
		self.waveId = int(waveId)
		self.spawnDelay = int(spawnDelay)
		self.spawnPosition = str(spawnPosition)
		self.monsterName = monsterName

	def __str__(self):
		return str(self.waveId) + "," + str(self.spawnDelay) + "," + self.spawnPosition + "," + self.monsterName.monsterAsset + "," + str(self.monsterName.speed) + "," + str(self.monsterName.hitPoint) + "," + str(self.monsterName.atk) + "," + self.monsterName.aiBehaviour


def randomSpawnPoint(spawnlist):
	spawnpoints = ["-6.7;-0.2;17.9;", "18.1;-0.1;-.60;", "-30.2;4.0;36.3;", "41.7;4.0;-26.7;"]
	chosenspawn = random.choice(spawnlist)
	return spawnpoints[chosenspawn]

def randomSpawnTime(spawnMin, spawnMax):
	time = random.randint(spawnMin , spawnMax)
	return time

# set some monsters for this stage
# monsterAsset, speed, hitPoint, atk, aiBehaviour
slime1 = gameMonster("Slime1",0.1,5,20,"AI_TDMonster")
slimeBrothers1 = gameMonster("slimeBrothers1",0.12,6,20,"AI_TDMonster")
skeletonlizard1 = gameMonster("skeletonlizard1",0.20,10,30,"AI_TDMonster")
skeletonmage1 = gameMonster("skeletonmage1",0.1,20,20,"AI_TDMonster")
slime3 = gameMonster("slime3",0.05,30,50,"AI_TDMonster")

#set some global variables!
auto_spawnMin = 1
auto_spawnMax = 55
mergedList = []

def createSpawn(monster, wave, spawnNumber, spawnLocations, spawnMin = auto_spawnMin, spawnMax = auto_spawnMax):
	spawnList = []
	for i in range(spawnNumber):                                                                                             
		mySpawn = SpawnRecord(wave,randomSpawnTime(spawnMin, spawnMax), randomSpawnPoint(spawnLocations) , monster)
		spawnList.append(mySpawn)
	return spawnList


#start editing here
# monster, wave, number, spawn location(as list), min time, max time
mergedList = mergedList + createSpawn(slime1,1, 40, [0,1])
mergedList = mergedList + createSpawn(slime3,1, 1, [0,1], 20,20)

mergedList = mergedList + createSpawn(slime1,2, 50, [0,1,2,3])
mergedList = mergedList + createSpawn(skeletonlizard1,2, 5, [0,1], 10)
mergedList = mergedList + createSpawn(slimeBrothers1,2, 5, [2,3], 10)
mergedList = mergedList + createSpawn(slime3,2, 2, [0,1], 15,20)

mergedList = mergedList + createSpawn(slime1,3, 60, [0,1,2,3])
mergedList = mergedList + createSpawn(skeletonlizard1,3, 20, [0,1], 1)
mergedList = mergedList + createSpawn(skeletonmage1,3, 15, [0,1], 10)
mergedList = mergedList + createSpawn(slimeBrothers1,3, 20, [2,3], 10)
mergedList = mergedList + createSpawn(slime3,3, 2, [0,1], 30)

mergedList = mergedList + createSpawn(slime1,4, 40, [0,1,2,3])
mergedList = mergedList + createSpawn(skeletonlizard1,4, 40, [0,1], 10)
mergedList = mergedList + createSpawn(skeletonmage1,4, 30, [0,1], 10)
mergedList = mergedList + createSpawn(slimeBrothers1,4, 20, [2,3], 10)
mergedList = mergedList + createSpawn(slime3,4, 10, [0,1], 30)


#output the list
for i in mergedList:
	print i