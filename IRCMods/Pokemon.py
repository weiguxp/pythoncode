import random
import time
from sopel.module import commands, priority

# These are the commands for this game

@commands('startgame')
def startgame(bot, trigger):
	# This starts the game. 
	if 'pokedex' in globals():
		bot.say('game has already been started')
	else:
		global pokedex
		pokedex = dict()
		bot.say ('DovantorrPokemon v0.2: Gotta catch them all!! type .pokehelp for commands')
		global myBot
		myBot = bot

@commands('pokehelp')
def pokehelp(bot, trigger):
	bot.say ('Available commands are .poke .create .feed .evolve .fight .enemy')

@commands('create')
def createpokemon(bot, trigger):
	if trigger.nick in pokedex:
		bot.say('You already have a pokemon!' )
	else:
		newPokemon = Pokemon(trigger.group(2), 100, bot)
		pokedex[trigger.nick] = newPokemon
		bot.say(str(pokedex[trigger.nick]))

@commands('feed')
def feedpokemon(bot, trigger):
	if pokedex[trigger.nick].hp < 0 :
		myBot.say('Sorry %s is dead and no longer wants to eat' % pokedex[trigger.nick].pokename)
	else:
		lastfed = int( time.time() - pokedex[trigger.nick].time )
		if lastfed < 100:
			myBot.say('Im not hungry(last fed %s seconds ago)' % str(lastfed))
		else:
			foodType = [('peanut', 25), ('Roach', -10), ('Mana Biscuit', 50), ('Lobster', 100), ('Grass', 5), ('Soup', 150)]
			fruit, gainHP = foodType[random.randint(0, len(foodType)-1)]
			bot.say ('You fed %s a %s. Gains %g HP' % (pokedex[trigger.nick].pokename, fruit, gainHP))
			pokedex[trigger.nick].addXP(gainHP/10)
			pokedex[trigger.nick].heal(gainHP)
			pokedex[trigger.nick].time = time.time()

@commands('revive')
def reviveP(bot, trigger):
	if pokedex[trigger.nick].hp > 0:
		myBot.say ('%s is not dead and doesnt need reviving')
	else:
		minRevivetime = 300
		if time.time() - pokedex[trigger.nick].time < minRevivetime:
			revivetime = int(minRevivetime - (time.time() - pokedex[trigger.nick].time))
			myBot.say ('you still need to wait %g seconds before reviving' % revivetime)
		else:
			myBot.say ('%s, you have successfully revived %s' % (trigger.nick , pokedex[trigger.nick].pokename))
			pokedex[trigger.nick].hp = pokedex[trigger.nick].maxhp

@commands('poke')
def poke(bot, trigger):
	bot.say(str(pokedex[trigger.nick]))

@commands('enemy')
def cEnemy(bot, trigger):
	global evilPokemon
	enemyName = trigger.nick + GenSuffix()
	evilPokemon = Pokemon(enemyName, 100, bot)
	myBot.say('Hard Mode Activated + 10000 hp')
	evilPokemon.hp += 100000
	myBot.say(str(evilPokemon))

@commands('fight')
def fightp(bot, trigger):
	if pokedex[trigger.nick].hp < 1:
		bot.say('sorry your pokemon is dead. please revive him with .revive')
	else:
		if trigger.group(2) in pokedex:
			if pokedex[trigger.group(2)].hp < 1:
				bot.say('your target pokemon is dead.')
			else:
				PokeBattle(pokedex[trigger.nick], pokedex[trigger.group(2)])
		else:
			if 'evilPokemon' in globals():
				if evilPokemon.hp > 0:
					PokeBattle(pokedex[trigger.nick], evilPokemon)
				else:
					myBot.say('You cant fight dead pokemon (create a new one with .enemy)')
			else:
				myBot.say('Currently no enemy, create one with .enemy')

@commands('evolve')
def evolvepoke(bot, trigger):
	myBot.say('[warning]evolve will consume 1 level from the active pokemon. To successfully evolve, roll 2D6 with 6 or higher roll')
	if pokedex[trigger.nick].level > 4 :
		if RollDice(2,6,1) > 5:
			myBot.say('Evolution Complete! check out the new stats with .poke')
			damageDice, damageRoll = pokedex[trigger.nick].weapon
			damageRoll += RollDice(1,5)
			pokedex[trigger.nick].weapon = damageDice, damageRoll
			pokedex[trigger.nick].pokename = pokedex[trigger.nick].pokename + GenSuffix()
			pokedex[trigger.nick].nextLvlXP = RollDice(10,100)
		else:
			myBot.say ('Evolution Failed, %s lost a level' % pokedex[trigger.nick].pokename)
			pokedex[trigger.nick].level -= 1
	else: 
		myBot.say ('%s Needs to be at least level 5 before evolving' % pokedex[trigger.nick].pokename)

@commands('cheat')
def cheatcode(bot, trigger):
	pokedex[trigger.nick].addXP(500)





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
		self.block = 0
		self.crit = 0 
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
		tdamage = damage - self.block
		if tdamage < 0:
			tdamage = 0
		
		self.hp -= tdamage
		myBot.say ( '%s took %g damage (%g Blocked) (Hp:%g/%g)' % (self.pokename, damage, self.block, self.hp, self.maxhp))
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
	myBot.say ('%s (%s Damage) will now battle %s (%s Damage)' % (poke1.pokename, str(poke1.getDamage()), poke2.pokename, str(poke2.getDamage())))
	while poke1.hp > -1 and poke2.hp > -1:
		damage = poke1.attack()
		poke2.takeDamage(damage)
		if poke2.hp < 1:
			deadPokemon = poke2
			myBot.say ('Tango Down!')
			poke1.addXP(random.randint(200,450))
			break
		time.sleep(1)


		damage = poke2.attack()
		poke1.takeDamage(damage)
		if poke1.hp <1:
			deadPokemon = poke1
			break
		time.sleep(1)

	myBot.say (str(deadPokemon.pokename) + ' has died')


def GenSuffix():
	suffixtype = ['mon', 'chu', 'izard', 'saur', 'pie', 'pod','ly']
	chosensuffix = suffixtype[random.randint(0,len(suffixtype)-1)]
	return chosensuffix