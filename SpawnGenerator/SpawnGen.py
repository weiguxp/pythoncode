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
		return str(self.waveId) + "," + str(self.spawnDelay) + "," + self.monsterName.monsterAsset + "," + self.spawnPosition + "," + str(self.amount)

	def __add__(self, other):
		try:
			return SpawnRecord(self.amount + other.amount)
		except AttributeError:
			return self.amount + other

	__radd__=__add__

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
chaos_runner = gameMonster("chaos_runner"	 ,0.12,	1818	,		100,		1.5,	1,		1,     "AI_TDMonster",1)
skeletonmage1 = gameMonster("skeletonmage1"		 ,0.07,	3182	,		50,			1.5,	1,		1,     "AI_TDMonster",10)
boss_chiyou = gameMonster("boss_chiyou"			 ,0.02,	9091	,		150,		1.5,	1,		1,     "AI_TDMonster",50)
skeleton_footman = gameMonster("skeleton_footman",0.05, 1000	,		50,			2,		1,		1,     "AI_TDMonster",1)
dragon_large = gameMonster("dragon_large"		 ,0.02,	20000	,		250,		1.5,	1,		1,     "AI_TDMonster",600)

#set some global variables!
auto_spawnMin = 1
auto_spawnMax = 55
mergedList = []

def createSpawn(monster, wave, spawnNumber, spawnLocations, waves = 1, spawnMin = auto_spawnMin, spawnMax = auto_spawnMax):
	# Divides up the spawn into MiniWaves
	#spawns the appropriate number
	spawnList = []
	
	duration = spawnMax - spawnMin
	numberWaves = waves
	miniWaveMobs = spawnNumber / numberWaves
	miniWaveDuration = duration / numberWaves

	#Creates 4 mini waves
	for i in range(numberWaves):
		miniSpawn = []
		waveStart = spawnMin + i*miniWaveDuration
		waveEnd = waveStart + miniWaveDuration
		# print str(waveStart) + " , " + str(waveEnd) + " , " + str(miniWaveMobs)
		miniSpawn = spawnAI.spawnBetween(waveStart, waveEnd, miniWaveMobs)

		#Creates mobs for each mini wave
		for spawnTime, amount in miniSpawn:
			if amount > 0:
				mySpawn = SpawnRecord(wave, spawnTime , spawnLocations , monster, amount)
				spawnList.append(mySpawn)

	return spawnList



#start editing here
# monster, wave, number, spawn location(as list), min time, max time
mergedList = mergedList + createSpawn(skeleton_footman	,1, 40, "B", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,1, 40, "C", 4)
mergedList = mergedList + createSpawn(skeletonlizard1	,1, 2, "C", 2, 45 , 55)

mergedList = mergedList + createSpawn(skeleton_footman	,2, 20, "A", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,2, 20, "B", 4)
mergedList = mergedList + createSpawn(skeletonmage1		,2, 30, "B", 4)
mergedList = mergedList + createSpawn(skeletonlizard1	,2, 15, "C", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,2, 20, "C", 4)
mergedList = mergedList + createSpawn(chaos_runner		,2, 2, "C", 2, 45 , 55)


mergedList = mergedList + createSpawn(skeleton_footman	,3, 30, "A", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,3, 10, "B", 4)
mergedList = mergedList + createSpawn(skeletonmage1		,3, 30, "B", 4)
mergedList = mergedList + createSpawn(chaos_runner		,3, 25, "C", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,3, 20, "C", 4)
mergedList = mergedList + createSpawn(bossbat1			,3, 3, "C", 2, 45 , 55)


mergedList = mergedList + createSpawn(skeleton_footman	,4, 40, "A", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,4, 10, "B", 4)
mergedList = mergedList + createSpawn(skeletonmage1		,4, 30, "B", 4)
mergedList = mergedList + createSpawn(chaos_runner		,4, 25, "C", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,4, 20, "C", 4)
mergedList = mergedList + createSpawn(bossbat1			,4, 4, "C", 1, 45 , 55)

mergedList = mergedList + createSpawn(skeletonmage1		,5, 30, "A", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,5, 10, "B", 4)
mergedList = mergedList + createSpawn(skeletonmage1		,5, 40, "B", 4)
mergedList = mergedList + createSpawn(chaos_runner		,5, 25, "C", 4)
mergedList = mergedList + createSpawn(skeleton_footman	,5, 20, "C", 4)
mergedList = mergedList + createSpawn(skeletonlizard1	,5, 15, "C", 4)
mergedList = mergedList + createSpawn(bossbat1			,5, 4, "C", 1, 45 , 55)
mergedList = mergedList + createSpawn(boss_chiyou		,5, 1, "C", 1, 45 , 55)

#output the list
for i in mergedList:
	print i

