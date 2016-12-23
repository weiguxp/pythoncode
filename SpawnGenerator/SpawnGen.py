import random

spawnList = []

class gameMonster(object):
	"""docstring for gameMonster"""
	def __init__(self, monsterAsset, speed, hitPoint, atk, aiBehaviour):
		self.arg = arg


class SpawnRecord(object):
	def __init__(self, waveId, spawnDelay, spawnPosition, monsterAsset, speed, hitPoint, atk, aiBehaviour):
		self.waveId = int(waveId)
		self.spawnDelay = int(spawnDelay)
		self.spawnPosition = str(spawnPosition)
		self.monsterAsset  = str(monsterAsset)
		self.speed  = float(speed)
		self.hitPoint  = int(hitPoint)
		self.atk  = int(atk)
		self.aiBehaviour = str(aiBehaviour)

	def __str__(self):
		return str(self.waveId) + "," + str(self.spawnDelay) + "," + self.spawnPosition + "," + self.monsterAsset + "," + str(self.speed) + "," + str(self.hitPoint) + "," + str(self.atk) + "," + self.aiBehaviour


def randomSpawnPoint():
	spawnpoints = ["-6.7;-0.2;17.9;", "18.1;-0.1;-.60;", "-30.2;4.0;36.3;", "41.7;4.0;-26.7;"]
	chosenspawn = random.choice(spawnpoints)
	return chosenspawn

def randomSpawnTime(duration):
	time = random.randint(1,duration)
	return time


def createSpawn():
	mySpawn = SpawnRecord(1,randomSpawnTime(30),randomSpawnPoint(),"Slime1",0.05,2,10,"test")
	return mySpawn


spawnList = []
for i in range(50):
	spawnList.append(createSpawn())

spawnList2 = []
for i in range(50):
	spawnList2.append(createSpawn())

mergedList = spawnList + spawnList2

for i in mergedList:
	print i