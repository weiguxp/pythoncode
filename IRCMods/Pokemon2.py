import random
import time
from sopel.module import commands, priority
import sopel
import pickle

# These are the commands for this game

def BotErrMsg(redtext):
	myBot.say (sopel.formatting.color((redtext), '04'))

def BotGreenMsg(redtext):
	myBot.say (sopel.formatting.color((redtext), '03'))

def BotBlueMsg(redtext):
	myBot.say (sopel.formatting.color((redtext), '12'))

def GetBuildNumber():
	buildsave = open('/home/ubuntu/build.txt', 'r+')
	buildnum = int(float(buildsave.read())) + 1
	buildsave.seek(0)
	buildsave.write(str(buildnum))
	buildsave.close()
	return buildnum

@commands('savegame')
def savegame(bot, trigger):
	SaveGame()


@commands('loadgame')
def loadgame(bot,trigger):
	LoadGame()


@commands('startgame')
def startgame(bot, trigger):
	# This starts the game. 
	if 'pokedex' in globals():
		bot.say('game has already been started')
	else:
		global pokedex
		global myBot	
		myBot = bot
		pokedex = dict()
		BotBlueMsg ('DovantorrPokemon v0.2(BuildNumber %g): type .pokehelp for commands' % GetBuildNumber())
		BotBlueMsg ('==Gotta catch them all!!==')


@commands('pokehelp')
def pokehelp(bot, trigger):
	bot.say ('Available commands are .create .poke .perk .feed .evolve .fight (optional: target username) .explore .explorewilds .rename')

@commands('create')
def createpokemon(bot, trigger):
	if trigger.nick in pokedex:
		bot.say('[PROF. OAK] I already gave you a pokemon! Dont be greedy! (if only you could change your name)' )
	else:
		BotBlueMsg('[PROF. OAK] Welcome to the world of Pokemon. Wild Pokemon live in the tall grass, take this Pokemon for your protection! [DiceRoll (6D16)]')
		newPokemon = Pokemon(trigger.group(2), RollDice(6,16,1))
		pokedex[trigger.nick] = newPokemon
		pokedex[trigger.nick].owner = trigger.nick
		bot.say(str(pokedex[trigger.nick]))


@commands('rename')
def renamePokemon(bot, trigger):
	myPokemon = pokedex[trigger.nick]
	if myPokemon.pokename == 'None':
		myPokemon.pokename = trigger.group(2)
	else:
		BotErrMsg('%s is stubborn and does not want to be renamed' %myPokemon.pokename)

@commands('perk')
def APerk(bot, trigger):
	try: pokedex[trigger.nick].AddPerk(trigger.group(2))
	except KeyError: BotErrMsg('You need a Pokemon First! (.create)')

@commands('feed')
def feedpokemon(bot, trigger):
	try: pokedex[trigger.nick].Feed()
	except KeyError: BotErrMsg('You need a Pokemon First! (.create)')


@commands('revive')
def reviveP(bot, trigger):
	try: pokedex[trigger.nick].Revive()
	except KeyError: BotErrMsg('You need a Pokemon First! (.create)')



@commands('fight')
def fightp(bot, trigger):
	#Checks if it is possible to do a fight, 
	#If possible, start the PokeBattle()
	if pokedex[trigger.nick].hp < 1:
		bot.say('Sorry your pokemon is dead. please revive him with .revive')
	else:
		if trigger.group(2) in pokedex:
			if pokedex[trigger.group(2)].hp < 1:
				bot.say('Your target pokemon has fainted. (ask that player to .revive their pokemon)')
			else:
				PokeBattle(pokedex[trigger.nick], pokedex[trigger.group(2)])
		else:
			if 'evilPokemon' in globals():
				if evilPokemon.hp > 0:
					PokeBattle(pokedex[trigger.nick], evilPokemon)
				else:
					myBot.say('You cant fight dead pokemon (You can find enemies with .explore)')
			else:
				myBot.say('Currently no enemy, create one with .explore')

@commands('evolve')
def evolvepoke(bot, trigger):
	try: pokedex[trigger.nick].EvolvePokemon() 
	except KeyError: BotErrMsg('You need a pokemon before you evolve')


@commands('poke')
def poke(bot, trigger):
	if trigger.group(2) in pokedex: bot.say(str(pokedex[trigger.group(2)]))
	else: bot.say(str(pokedex[trigger.nick]))

@commands('enemyinfo')
def enemyInfo(bot, trigger):
	bot.say(str(evilPokemon))

##################################################    ENEMY CREATION SECTION       ##############################################################

@commands('explore')
def cEnemy(bot, trigger):

	#Creates a global variable called evil Pokemon
	if 'evilPokemon' in globals() == False: global evilPokemon

	try:
		if evilPokemon.hp > 0:
			BotErrMsg('%s is preventing you from exploring' %evilPokemon.pokename)
			return 0
	except Exception:
		hello = 1

	
	BotBlueMsg('A wild Pokemon has appeared!')
	try:	genEnemyLevel = random.randint(1, pokedex[trigger.nick].level+3) 
	except KeyError: genEnemyLevel = 1
	evilPokemon = WildPokemon1(genEnemyLevel)

	bot.say(str(evilPokemon))

@commands('explorewilds')
def cEnemy2(bot, trigger):
	if pokedex[trigger.nick].level > 15:
		BotBlueMsg('You explore the tall grass.... A wild [Dragon] Pokemon has appeared!')
		global evilPokemon
		enemyLevel = RollDice(15,30)
		evilPokemon = DragonPokemon(enemyLevel)
		bot.say(str(evilPokemon))

	else:
		BotErrMsg('You must be level 15 before exploring the wilds')


# @commands('operationcwal')
# def cheatcode(bot, trigger):
# 	pokedex[trigger.nick].AddXP(1000)




#################################################  This is the Pokemon Class, Defines what it is to be a Pokemon #########################################################

class Pokemon(object):
	def __init__(self, pokename, hp):
		self.owner = 'wild'
		self.level = 1
		self.pokename = str(pokename)
		self.maxhp = hp
		self.hp = self.maxhp
		self.xp = 0
		self.nextLvlXP = 500
		self.nextEvolve = 4
		self.perks = 3
		self.isNPC = False
		self.killxp = 0
		self.slainby = 'wild'
		self.fighting = []
		self.deathTriggered = False

		#Battle information
		self.weapon = 2,12
		self.block = 0
		self.crit = 0
		self.evade = 0.0
		self.dunkmaster = 0
		self.leechseed = 0

		#Time information
		self.time = time.time() - 600
		self.revivetime = time.time() - 600
		print self


	def AddXP(self, addXP):
		self.xp += addXP
		# myBot.say ('%s has gained %g XP (%g/%g)' % (self.pokename, addXP, self.xp, self.nextLvlXP))
		if self.xp > self.nextLvlXP:
			self.xp -= self.nextLvlXP
			self.nextLvlXP += 90
			self.LevelUp()

	def LevelUp(self):
		myBot.say ( '%s LevelUp up and will gain 1D6 hp' % self.pokename)
		self.maxhp += RollDice(1,6, 1)
		self.hp = self.maxhp
		self.level += 1

	def __str__(self):
		numDice, diceDamage = self.weapon
		myMsg = '[%s] is a level %g pokemon. (HP:%g/%g) (XP:%g /%g) (Damage:%gD%g)(Crit:%g, Defense:%g, Evade:%g)' % (self.pokename, self.level, self.hp, self.maxhp, self.xp, self.nextLvlXP, numDice, diceDamage, self.crit, self.block, self.evade)
		if self.perks > 0:
			myMsg += '. You have %g Available perks, type .perk to distribute' %self.perks
		return myMsg


	def Heal(self, Healamount):
		self.hp += Healamount
		if self.hp > self.maxhp:
			self.hp = self.maxhp
		#myBot.say ( '%s Healed for %g  (Hp:%g/%g)' % (self.pokename, Healamount, self.hp, self.maxhp))

	def GetAttackDamage(self):
		# print '%s is now GetAttackDamageing with weapon %g, %g' % (self.pokename, numDice, numHeads)
		numDice, numHeads = self.weapon
		damage = RollDice(numDice, numHeads)
		if self.crit > random.randint(1,100):
			damage = damage*2
			myBot.say('%s Scored a Critial Strike (%g Damage)!!'% (self.pokename, damage))
		if self.dunkmaster > random.randint(1,100):
			damage = damage * 5
			BotBlueMsg('%s Used Noxian Guillotine - It was super effective!' %self.pokename)

		return damage	

	def AttackTurn2(self, myBlog):
		if self.leechseed > random.randint(1,100):
			self.hp += myBlog.damageTaken
			BotBlueMsg('%s Used Leechseed and healed %g' % (self.pokename, myBlog.damageTaken))

	def TakeDamage(self, myBlog):
		if self.hp > 0:
			#Adds the attacker into self.fighting
			if myBlog.attackerOwner != 'wild' and myBlog.attackerOwner not in self.fighting:
				self.fighting.append(myBlog.attackerOwner)

			#Check if Evade
			if self.evade > RollDice(1,100):
				# myBot.say('%s Evaded the attack' % self.pokename)
				myBlog.log = 'Evaded'
				myBlog.damageTaken = 0
				return myBlog

			#Do a block!
			tdamage = myBlog.toDealDamage - self.block
			if tdamage < 0:
				tdamage = 0

			#take some damage
			myBlog.damageTaken = tdamage
			self.hp -= tdamage

			#Saves who killed it
			if self.hp < 1:
				self.slainby = myBlog.attackerOwner

			#Adds the Blocked message
			myBlog.log =  ( '%s took %g damage (Hp:%g/%g)' % (self.pokename, tdamage, self.hp, self.maxhp))
			if self.block > 0:
				myBlog.log += '(%g Blocked)' % self.block
		else: myBlog.log = 'Fainted'

		return myBlog

	def TriggerDeath(self):

		if self.slainby != 'wild':

			xpList = []

			if self.isNPC == True: killxp = self.killxp
			else: killxp = random.randint(200,450)

			#starts the XP share!
			if len(self.fighting) > 1:
				killstealxp = int(killxp/2)
			else:
				killstealxp = killxp

			xpList.append([self.slainby, killstealxp])
			# pokedex[self.slainby].AddXP(killstealxp)

			Log = "%s gained %g XP " % (self.slainby, killstealxp)
			self.fighting.remove(self.slainby)



			if len(self.fighting) > 0:
				splitxp = int(killxp/(2*len(self.fighting)))
				for player in self.fighting:
					
					# pokedex[player].AddXP(splitxp)
					xpList.append([player, splitxp])
					Log += "| %s gained %g XP" % (player, splitxp)
			
			myBot.say(Log)

			for player, xp in xpList:
				pokedex[player].AddXP(xp)


	def GetDamage(self):
		damage = '%gD%g' % (self.weapon)
		return damage

	def AddPerk(self, selectedPerk):
		if self.perks > 0:
			#List of perks of what they do!
			if selectedPerk == 'block':
				if self.maxhp > 20:
					self.block +=5
					self.maxhp -= 15
					self.hp = self.maxhp
					self.perks -= 1 
					myBot.say('You staple some rudimendary armor on %s (ouch), %s permanently loses 15 hp.' % (self.pokename, self.pokename))
				else:
					BotErrMsg('%s is too weak endure the staple gun' % self.pokename)
			elif selectedPerk == 'crit':
				self.crit +=5
				self.perks -= 1 
				BotBlueMsg('%s gains 5 percent crit chance' %self.pokename)
			elif selectedPerk =='evade':
				evadegain = (50-self.evade)*0.1
				self.evade += evadegain
				self.perks -= 1 
				BotBlueMsg('%s gains %g percent evade chance' %(self.pokename, evadegain))
			else:
				myBot.say('your options are block, evade or crit')	
		else:
			myBot.say ('%s does not have any available perks (Try evolving)'%self.pokename)

	def EvolvePokemon(self):
		myBot.say('[Warning]evolve will consume 1 level from the active pokemon. To successfully evolve, roll 2D6 with 6 or higher roll')
		if self.level > self.nextEvolve :
			if RollDice(2,6,1) > 5:
				myBot.say('Evolution Complete! check out the new stats with .poke')
				self.nextEvolve += 5
				damageDice, damageRoll = self.weapon
				damageRoll += RollDice(1,5)
				self.weapon = damageDice, damageRoll
				self.pokename = self.pokename + GenSuffix()
				self.perks += 2
				# self.nextLvlXP = RollDice(10,100)
			else:
				myBot.say ('Evolution Failed, %s lost a level' % self.pokename)
				self.level -= 1
		else: 

			myBot.say ('%s Needs to be at least level %g before evolving' % (self.pokename, self.nextEvolve + 1))

	def Revive(self):
		if self.hp > 0:
			BotBlueMsg ('[NURSE JOY] %s does not need to be revived' % self.pokename)
		else:
			minRevivetime = 300
			if time.time() - self.revivetime < minRevivetime:
				revivetime = int(minRevivetime - (time.time() - self.revivetime))
				BotBlueMsg ('[NURSE JOY] You still need to wait %g seconds before reviving' % revivetime)
			else:
				BotBlueMsg('[NURSE JOY] Successfully revived %s' % (self.pokename))
				self.hp = self.maxhp
				self.deathTriggered = False
				self.revivetime = time.time()

	def Feed(self):
		if self.hp < 0 :
			myBot.say('Sorry %s in a coma and no longer wants to eat (hint: .revive)' % self.pokename)
		else:
			lastfed = int( time.time() - self.time )
			if lastfed < 100:
				myBot.say('Im not hungry(last fed %s seconds ago)' % str(lastfed))
			else:
				foodType = [('peanut', 25), ('Roach', -10), ('Mana Biscuit', 50), ('Lobster', 100), ('Grass', 5), ('Soup', 150)]
				fruit, gainHP = foodType[random.randint(0, len(foodType)-1)]
				myBot.say ('You fed %s a %s. Gains %g HP' % (self.pokename, fruit, gainHP))
				self.AddXP(gainHP/10)
				self.Heal(gainHP)
				self.time = time.time()







#####################################################################         NPC  Pokemons are defined here            ######################################################################

class NPCPokemon(Pokemon):

	def __init__(self):
		Pokemon.__init__(self, 'Pokename Not Set', 1)
		self.isNPC = True
		self.killxp = 1


	def __str__(self):
		numDice, diceDamage = self.weapon
		myMsg = '[%s]Hi! I am a level %g pokemon. (HP:%g/%g) (Damage:%gD%g)(Crit:%g, Defense:%g, Evade:%g)(XP value: %g)' % (self.pokename, self.level, self.hp, self.maxhp, numDice, diceDamage, self.crit, self.block, self.evade, self.killxp)
		return myMsg

	def MakeWild(self):
		if random.randint(0,100) < 80:
			self.crit = random.randint(2,30)
			self.killxp += 50
		if random.randint(0,100) < 20:
			self.block = random.randint(2,10)
			self.killxp += 115
		if random.randint(0,100) < 20:
			self.evade = random.randint(20,65)
			self.killxp += 150
		if random.randint(0,100) < 15:
			self.dunkmaster = random.randint(20,70)
			self.pokename = '[Dunkmaster]' + self.pokename
			self.killxp *= int(self.killxp * 1.3)
		if random.randint(0,100) < 20:
			self.leechseed = random.randint(20,70)
			self.pokename = '[Leechseed]' + self.pokename
			self.killxp = int(self.killxp * 1.2)


class WildPokemon1(NPCPokemon):
	def __init__(self, level):
		NPCPokemon.__init__(self)
		self.pokename = GenPokeName()
		self.level = level
		self.weapon = 2, random.randint(1,15+(self.level))
		self.maxhp = RollDice(3,(35+self.level))
		self.hp = self.maxhp
		self.killxp = random.randint(200,400)

		#Make this pokemon OP
		self.MakeWild()



class DragonPokemon(NPCPokemon):
	def __init__(self, level):
		NPCPokemon.__init__(self)
		self.pokename = '[Dragon]' + trigger.nick + 'saur'
		self.weapon = 3,20
		self.crit = RollDice(1,30)
		self.block = RollDice(1,12)
		self.evade = RollDice(1,12)
		self.killxp = random.randint(1200,1800)
		self.MakeWild()
	
class BattleLog(object):
	def __init__(self):
		BattleLog.log = 'Error: No Log'
		BattleLog.toDealDamage = 0
		BattleLog.damageTaken = 0
		BattleLog.attackerOwner = 'wild'




def GenPokeName():
	pokemons = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidoran', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Farfetchd', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'MrMime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo']
	chosenpokemon = pokemons[random.randint(0,len(pokemons) -1 )]
	return chosenpokemon

def GenSuffix():
	suffixtype = ['mon', 'chu', 'izard', 'saur', 'pie', 'pod','ly']
	chosensuffix = suffixtype[random.randint(0,len(suffixtype)-1)]
	return chosensuffix

def RollDice(numDice, numHeads, verbose = 0):
	diceSum = 0
	for i in range (numDice):
		diceSum += random.randint(1,numHeads)
	if verbose == 1:
		myBot.say ( sopel.formatting.color('[DICE(%gD%g)] I rolled %g' % (numDice, numHeads, diceSum), '02'))
	return diceSum


def SaveGame():
	pickle.dump(pokedex, open("save.p", "wb"))

def LoadGame():
	global pokedex
	pokedex = dict()
	pokedex = pickle.load(open("save.p", "rb"))
	myBot.say('game loaded')
	myBot.say(str(pokedex)) 


###################################################### Battle Logic #################################################

def PokeBattle(poke1, poke2):
	myBot.say ('%s (%s Damage) will now battle %s (%s Damage)' % (poke1.pokename, str(poke1.GetDamage()), poke2.pokename, str(poke2.GetDamage())))

	linePadding = 0
	while poke1.hp > 0 and poke2.hp > 0:
		#time to start fighting
		battlelog = PokeFight(poke1, poke2)

		#Time to do some padding
		if len(battlelog) > linePadding: linePadding = len(battlelog)+ 3
		while len(battlelog) < linePadding:
			battlelog = " " + battlelog
		battlelog += " | " 

		#fight but in reverse
		battlelog += PokeFight(poke2, poke1)

		myBot.say(battlelog)
		time.sleep(2)

	#time to determine the winner!
	if 'deadpokemon' not in locals():
		if poke2.hp < 1 and poke2.hp < poke1.hp:
			deadpokemon = poke2
			winnerpokemon = poke1
		else:
			deadpokemon = poke1
			winnerpokemon = poke2

	#give some XP!
	if winnerpokemon.isNPC == True: winnerpokemon.killxp += 200
	if winnerpokemon.isNPC == False:
		# if deadpokemon.isNPC == True: 
			
			#Trigger the death of the pokemon!
			if deadpokemon.deathTriggered == False:
				deadpokemon.deathTriggered = True
				BotBlueMsg (str(deadpokemon.pokename) + ' has fainted')
				deadpokemon.TriggerDeath()
		# else: 

			# winnerpokemon.AddXP(random.randint(200,450))

def PokeFight(defender, attacker):
	# let them fight!
	myBlog = BattleLog()
	myBlog.attackerOwner = attacker.owner

	myBlog.toDealDamage = attacker.GetAttackDamage()
	myBlog = defender.TakeDamage(myBlog)
	attacker.AttackTurn2(myBlog)

	return myBlog.log