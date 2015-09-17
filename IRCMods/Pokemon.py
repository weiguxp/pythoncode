import random
import time
from sopel.module import commands, priority





@commands('createpokemon')
def createpokemon(bot, trigger):
	myPokemon = Pokemon(trigger.group(2), 100, bot)
	bot.say(str(myPokemon))
	myPokemon.takeDamage(50)



def RollDice2(numDice, numHeads, bot):
	diceSum = 0
	for i in range (numDice):
		diceSum += random.randint(1,numHeads)
	bot.say ('[DiceRoll] I rolled %g D %g , result is %g' % (numDice, numHeads, diceSum))
	return diceSum


def RollDice(numDice, numHeads, verbose = 0):
	diceSum = 0
	for i in range (numDice):
		diceSum += random.randint(1,numHeads)
	if verbose == 1:
		print '[DiceRoll] I rolled %g D %g , result is %g' % (numDice, numHeads, diceSum)
	return diceSum


class Pokemon(object):
	def __init__(self, pokename, initiative, bot):
		self.level = 1
		self.pokename = str(pokename)
		self.initiative = float(initiative)
		print 'Deciding the starting HP via DiceRoll (6D16)'
		self.maxhp = RollDice2(6,16, bot)
		self.hp = self.maxhp
		self.xp = 0
		self.nextLvlXP = 500
		self.weapon = 2,12
		self.bot = bot
		print self

	def updateHP(self):
		return 100 * ( 1 + self.level / 10)

	def addXP(self, addedXP):
		self.xp += addedXP
		if self.xp > self.nextLvlXP:
			self.xp -= self.nextLvlXP
			self.nextLvlXP += 50
			self.levelUp()

	def levelUp(self):
		print '%s have levelup up and will gain 1D6 hp' % self.pokename
		self.maxhp += RollDice(1,6)
		self.hp = self.maxhp

	def __str__(self):
		return '[%s]Hi!. My name is %s, i am a level %g pokemon. (HP:%g/%g) (XP:%g /%g)' % (self.pokename, self.pokename, self.level, self.hp, self.maxhp, self.xp, self.nextLvlXP)

	def takeDamage(self, damage):
		self.hp -= damage
		print '%s took %g damage (Hp:%g/%g)' % (self.pokename, damage, self.hp, self.maxhp)
		self.bot.say ('i took some damage')
		if self.hp < 0:
			print '%s has died' % self.pokename

	def attack(self):
		dice, weapon = self.weapon
		print '%s is now attacking with weapon %g, %g' % (self.pokename, dice, weapon)
		numDice, numHeads = self.weapon
		damage = RollDice(numDice, numHeads)
		return damage

def PokeBattle(poke1, poke2):

	while poke1.hp > 0 and poke2.hp > 0:
		damage = poke1.attack()
		poke2.takeDamage(damage)
		if poke2.hp < 0:
			deadPokemon = poke2
			break
		time.sleep(1)


		damage = poke2.attack()
		poke1.takeDamage(damage)
		if poke1.hp <0:
			deadPokemon = poke1
			break
		time.sleep(1)

	print deadPokemon 

# myPokemon = Pokemon('Skibear', 100)

# evilPokemon = Pokemon('Evil Skibear', 100)

# evilPokemon = Pokemon('Kobold', 100)

# mytime = time.time()



# PokeBattle(myPokemon, evilPokemon)

# print time.time() - mytime