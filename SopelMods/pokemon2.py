import random
import time
from sopel.module import commands, priority

@commands('startgame')
def startgame(bot, trigger):
	if 'pokedex' in globals():
		bot.say('game has already been started')
	else:
		global pokedex
		pokedex = dict()
		bot.say ('gotta catch them all')
		global myBot
		myBot = bot

@commands('create')
def createpokemon(bot, trigger):
	if trigger.nick in pokedex:
		bot.say('You already have a pokemon!' )
	else:
		myPokemon = Pokemon(trigger.group(2), 100, bot)
		pokedex[trigger.nick] = myPokemon

		bot.say(str(pokedex[trigger.nick]))

@commands('feed')
def feedpokemon(bot, trigger):
	if myPokemon.hp < 0 :
		myBot.say('Sorry %s is dead and no longer wants to eat' % myPokemon.pokename)
	else:
		lastfed = int( time.time() - myPokemon.time )
		if lastfed < 100:
			myBot.say('Im not hungry(last fed %s seconds ago)' % str(lastfed))
		else:
			foodType = [('peanut', 25), ('Roach', -10), ('Mana Biscuit', 50), ('Lobster', 100), ('Grass', 5), ('Soup', 150)]
			fruit, gainHP = foodType[random.randint(0, len(foodType)-1)]
			bot.say ('You fed %s a %s. Gains %g HP' % (myPokemon.pokename, fruit, gainHP))
			myPokemon.addXP(gainHP/10)
			myPokemon.heal(gainHP)
			myPokemon.time = time.time()

@commands('revive')
def reviveP(bot, trigger):
	if myPokemon.hp > 0:
		myBot.say ('%s is not dead and doesnt need reviving')
	else:
		minRevivetime = 300
		if time.time() - myPokemon.time < minRevivetime:
			revivetime = int(minRevivetime - (time.time() - myPokemon.time))
			myBot.say ('you still need to wait %g seconds before reviving' % revivetime)
		else:
			myBot.say ('%s, you have successfully revived %s' % (trigger.nick , myPokemon.pokename))
			myPokemon.hp = myPokemon.maxhp

@commands('poke')
def poke(bot, trigger):
	bot.say(str(myPokemon))

@commands('enemy')
def cEnemy(bot, trigger):
	global enemyPokemon
	enemyName = trigger.nick + GenSuffix()
	enemyPokemon = Pokemon(enemyName, 100, bot)
	myBot.say(str(enemyPokemon))

@commands('fight')
def fightp(bot, trigger):

	
	if 'enemyPokemon' in globals():
		myBot.say ('%s (%s Damage) will now battle %s (%s Damage)' % (myPokemon.pokename, str(myPokemon.getDamage()), enemyPokemon.pokename, str(enemyPokemon.getDamage())))
		if enemyPokemon.hp > 0:
			PokeBattle(myPokemon, enemyPokemon)
		else:
			myBot.say('You cant fight dead pokemon (create a new one with .enemy)')
	else:
		myBot.say('Currently no enemy, create one with .enemy')

@commands('evolve')
def evolvepoke(bot, trigger):
	myBot.say('[warning]evolve will consume 1 level from the active pokemon. To successfully evolve, roll 2D6 with 6 or higher roll')
	if myPokemon.level > 4 :
		if RollDice(2,6,1) > 6:
			myBot.say('Evolution Complete! check out the new stats with .poke')
			myPokemon.level -= 1
			damageDice, damageRoll = myPokemon.weapon
			damageRoll += RollDice(1,5)
			myPokemon.weapon = damageDice, damageRoll
			myPokemon.pokename = myPokemon.pokename + GenSuffix()
			myPokemon.nextLvlXP = RollDice(10,100)
		else:
			myBot.say ('Evolution Failed, %s lost a level' % myPokemon.pokename)
			myPokemon.level -= 1
	else: 
		myBot.say ('%s Needs to be at least level 5 before evolving' % myPokemon.pokename)

@commands('cheat')
def cheatcode(bot, trigger):
	myPokemon.addXP(500)

@commands('pokehelp')
def pokehelp(bot, trigger):
	bot.say ('Available commands are .poke .create .feed .evolve .fight .enemy')



def RollDice(numDice, numHeads, verbose = 0):
	diceSum = 0
	for i in range (numDice):
		diceSum += random.randint(1,numHeads)
	if verbose == 1:
		myBot.say ( '[DiceRoll] I rolled %g D %g , result is %g' % (numDice, numHeads, diceSum))
	return diceSum


class Pokemon(object):
	def __init__(self, pokename, initiative, bot):
		self.level = 1
		self.pokename = str(pokename)
		self.initiative = float(initiative)
		print 'Deciding the starting HP via DiceRoll (6D16)'
		self.maxhp = RollDice(6,16, 1)
		self.hp = self.maxhp
		self.xp = 0
		self.nextLvlXP = 500
		self.weapon = 2,12
		self.time = time.time() - 600
		print self

	def updateHP(self):
		return 100 * ( 1 + self.level / 10)

	def addXP(self, addedXP):
		self.xp += addedXP
		myBot.say ('%s has gained %g XP' % (self.pokename, addedXP))
		if self.xp > self.nextLvlXP:
			self.xp -= self.nextLvlXP
			self.nextLvlXP += 50
			self.levelUp()

	def levelUp(self):
		myBot.say ( '%s levelup up and will gain 1D6 hp' % self.pokename)
		self.maxhp += RollDice(1,6, 1)
		self.hp = self.maxhp
		self.level += 1

	def __str__(self):
		return '[%s]Hi!. My name is %s, I am a level %g pokemon. (HP:%g/%g) (XP:%g /%g)' % (self.pokename, self.pokename, self.level, self.hp, self.maxhp, self.xp, self.nextLvlXP)

	def takeDamage(self, damage):
		self.hp -= damage
		myBot.say ( '%s took %g damage (Hp:%g/%g)' % (self.pokename, damage, self.hp, self.maxhp))
		if self.hp < 0:
			print '%s has died' % self.pokename

	def heal(self, healamount):
		self.hp += healamount
		if self.hp > self.maxhp:
			self.hp = self.maxhp
		myBot.say ( '%s healed for %g  (Hp:%g/%g)' % (self.pokename, healamount, self.hp, self.maxhp))

	def attack(self):
		dice, weapon = self.weapon
		print '%s is now attacking with weapon %g, %g' % (self.pokename, dice, weapon)
		numDice, numHeads = self.weapon
		damage = RollDice(numDice, numHeads)
		return damage

	def getDamage(self):
		damage = '%gD%g' % (self.weapon)
		return damage


def PokeBattle(poke1, poke2):

	while poke1.hp > -1 and poke2.hp > -1:
		damage = poke1.attack()
		poke2.takeDamage(damage)
		if poke2.hp < 0:
			deadPokemon = poke2
			myBot.say ('Tango Down!')
			poke1.addXP(random.randint(200,450))
			break
		time.sleep(1)


		damage = poke2.attack()
		poke1.takeDamage(damage)
		if poke1.hp <0:
			deadPokemon = poke1
			break
		time.sleep(1)

	myBot.say (str(deadPokemon.pokename) + ' has died')


def GenSuffix():
	suffixtype = ['mon', 'chu', 'izard', 'saur', 'pie', 'pod','ly']
	chosensuffix = suffixtype[random.randint(0,len(suffixtype)-1)]
	return chosensuffix