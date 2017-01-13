import random
import math
import spawnAI

spawnList = []

class gameMonster(object):
	"""docstring for gameMonster"""
	def __init__(self, monsterAsset, speed, hitPoint, atk, attackInterval, attackRange, visionRange, aiBehaviour, drop):
		self.monsterAsset  = str(monsterAsset)
		self.speed  = float(speed)
		self.hitPoint  = int(hitPoint)
		self.atk  = int(atk)
		self.attackInterval = float(attackInterval)
		self.attackRange = float (attackRange)
		self.visionRange = float (visionRange)
		self.aiBehaviour = str(aiBehaviour)
		self.drop = int(drop)




class SpawnRecord(object):
	def __init__(self, waveId, spawnDelay, spawnPosition, monsterName, amount=1):
		self.waveId = int(waveId)
		self.spawnDelay = int(spawnDelay)
		self.spawnPosition = str(spawnPosition)
		self.monsterName = monsterName
		self.amount = amount

	def __str__(self):
		return str(self.waveId) + "," + str(self.spawnDelay) + "," + self.spawnPosition + "," + self.monsterName.monsterAsset + "," + str(self.monsterName.speed) + "," + str(self.monsterName.hitPoint) + "," + str(self.monsterName.atk) + "," + str(self.monsterName.attackInterval) + "," + str(self.monsterName.attackRange) + "," + str(self.monsterName.visionRange) + "," + self.monsterName.aiBehaviour + "," + str(self.monsterName.drop) + "," + str(self.amount)


def randomSpawnPoint(spawnlist):
	#returns the co-ordinates given location in form of a list
	spawnpoints = ["A", "B", "C", "D"]
	chosenspawn = random.choice(spawnlist)
	return spawnpoints[chosenspawn]

def randomSpawnTime(spawnMin, spawnMax):
	time = random.randint(spawnMin , spawnMax)
	return time

# set some monsters for this stage
# monsterAsset, 						       speed, hitPoint, 		atk, atkInterval, attackRange, visionRange, aiBehaviour, drop
bossbat1 = gameMonster("bossbat1"				 ,0.8,	1818	,		50,			1.5, 	1,		1,     "AI_TDMonster",15)
skeletonlizard1 = gameMonster("skeletonlizard1"	 ,0.12,	1818	,		100,		1.5,	1,		1,     "AI_TDMonster",1)
skeletonmage1 = gameMonster("skeletonmage1"		 ,0.07,	3182	,		50,			1.5,	1,		1,     "AI_TDMonster",10)
boss_chiyou = gameMonster("boss_chiyou"			 ,0.02,	9091	,		150,		1.5,	1,		1,     "AI_TDMonster",50)
skeleton_footman = gameMonster("skeleton_footman",0.05, 1000	,		50,			2,		1,		1,     "AI_TDMonster",1)
dragon_large = gameMonster("dragon_large"		 ,0.02,	20000	,		250,		1.5,	1,		1,     "AI_TDMonster",600)

#set some global variables!
auto_spawnMin = 1
auto_spawnMax = 55
mergedList = []

def createSpawn(monster, wave, spawnNumber, spawnLocations, spawnMin = auto_spawnMin, spawnMax = auto_spawnMax):
	spawnList = []
	
	duration = spawnMax - spawnMin
	numberWaves = 4
	miniWaveMobs = spawnNumber / numberWaves
	miniWaveDuration = duration / numberWaves


	for i in range(numberWaves):
		miniSpawn = []
		waveStart = spawnMin + i*miniWaveDuration
		waveEnd = waveStart + miniWaveDuration
		miniSpawn = spawnAI.spawnBetween(waveStart, waveEnd, miniWaveMobs)
		for spawnTime, amount in miniSpawn:
			if amount == 0: break
			mySpawn = SpawnRecord(wave, spawnTime , "A" , monster, amount)
			spawnList.append(mySpawn)

	return spawnList


	# miniWaveList = []
	# for i in range(numberWaves):
	# 	miniWaveList.append(spawnMin + miniWaveDuration*i)

	# spawnList = []

	# miniWaveMobs = float(spawnNumber) / (numberWaves * len(spawnLocations))
	# miniWaveMobs = int(math.ceil(miniWaveMobs))


	# for time in miniWaveList:
	# 	for spawn in spawnLocations:
	# 		tempList = []
	# 		tempList.append(spawn)                                                                                             
	# 		mySpawn = SpawnRecord(wave, time , randomSpawnPoint(tempList) , monster, miniWaveMobs)
	# 		spawnList.append(mySpawn)

	# 		numSpawned += miniWaveMobs
	# 		if numSpawned >= spawnNumber: break

	# 	if numSpawned >= spawnNumber: break

	# return spawnList


#start editing here
# monster, wave, number, spawn location(as list), min time, max time
mergedList = mergedList + createSpawn(skeleton_footman	,1, 40, [0,1])
mergedList = mergedList + createSpawn(boss_chiyou		,1, 1, [0,1], 20,20)

mergedList = mergedList + createSpawn(skeleton_footman	,2, 60, [0,1,2,3])
mergedList = mergedList + createSpawn(skeletonlizard1	,2, 10, [0,1], 10)
mergedList = mergedList + createSpawn(bossbat1			,2, 5, [2,3], 10)
mergedList = mergedList + createSpawn(boss_chiyou		,2, 2, [0,1], 15,20)

mergedList = mergedList + createSpawn(skeleton_footman,3, 60, [0,1,2,3])
mergedList = mergedList + createSpawn(skeletonlizard1,3, 20, [0,1], 1)
mergedList = mergedList + createSpawn(skeletonmage1,3, 15, [0,1], 10)
mergedList = mergedList + createSpawn(bossbat1,3, 20, [2,3], 10)
mergedList = mergedList + createSpawn(boss_chiyou,3, 1, [2], 30)

mergedList = mergedList + createSpawn(skeleton_footman,4, 40, [0,1,2,3])
mergedList = mergedList + createSpawn(skeletonlizard1,4, 40, [0,1], 10)
mergedList = mergedList + createSpawn(skeletonmage1,4, 30, [0,1], 10)
mergedList = mergedList + createSpawn(bossbat1,4, 20, [2,3], 10)
mergedList = mergedList + createSpawn(boss_chiyou,4, 10, [0,1], 30)

mergedList = mergedList + createSpawn(skeleton_footman,5, 20, [0,1,2,3])
mergedList = mergedList + createSpawn(skeletonlizard1,5, 40, [0,1], 10)
mergedList = mergedList + createSpawn(skeletonmage1,5, 30, [0,1], 10)
mergedList = mergedList + createSpawn(bossbat1,5, 20, [2,3], 10)
mergedList = mergedList + createSpawn(boss_chiyou,5, 10, [0,1], 30)




#output the list
for i in mergedList:
	print i