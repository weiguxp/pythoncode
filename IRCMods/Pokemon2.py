import random
import time
from sopel.module import commands, priority
import sopel

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
	bot.say ('Available commands are .create .poke .perk .feed .evolve .fight (optional: target username) .explore .explorewilds')

@commands('create')
def createpokemon(bot, trigger):
	if trigger.nick in pokedex:
		bot.say('[PROF. OAK] I already gave you a pokemon! Dont be greedy! (if only you could change your name)' )
	else:
		BotBlueMsg('[PROF. OAK] Welcome to the world of Pokemon. Wild Pokemon live in the tall grass, take this Pokemon for your protection! [DiceRoll (6D16)]')
		newPokemon = Pokemon(trigger.group(2), RollDice(6,16,1))
		pokedex[trigger.nick] = newPokemon
		bot.say(str(pokedex[trigger.nick]))


@commands('rename')
def renamePokemon(bot, trigger):
	myPokemon = pokedex[trigger.nick]
	if myPokemon.pokename == 'None':
		myPokemon.pokename = trigger.group(2)
	else:
		BotErrMsg('%s is stubborn and does not want to be renamed' %myPokemon.pokename)

@commands('perk')
def AddPerk(bot, trigger):
	myPokemon = pokedex[trigger.nick]
	if pokedex[trigger.nick].perks > 0:
		if trigger.group(2) == 'block':
			if myPokemon.maxhp > 20:
				myPokemon.block +=5
				myPokemon.maxhp -= 15
				myPokemon.hp = myPokemon.maxhp
				myPokemon.perks -= 1 
				bot.say('You staple some rudimendary armor on %s (ouch), %s permanently loses 15 hp.' % (myPokemon.pokename, myPokemon.pokename))
			else:
				BotErrMsg('%s is too weak endure the staple gun' % myPokemon.pokename)
		elif trigger.group(2) == 'crit':
			myPokemon.crit +=5
			myPokemon.perks -= 1 
			BotBlueMsg('%s gains 5 percent crit chance' %myPokemon.pokename)
		elif trigger.group(2) =='evade':
			myPokemon.evade += 5
			myPokemon.perks -= 1 
			BotBlueMsg('%s gains 5 percent evade chance' %myPokemon.pokename)
		else:
			bot.say('your options are block, evade or crit')
	else:
		bot.say ('%s does not have any available perks (Try evolving)'%pokedex[trigger.nick].pokename)

@commands('feed')
def feedpokemon(bot, trigger):
	if pokedex[trigger.nick].hp < 0 :
		myBot.say('Sorry %s in a coma and no longer wants to eat (hint: .revive)' % pokedex[trigger.nick].pokename)
	else:
		lastfed = int( time.time() - pokedex[trigger.nick].time )
		if lastfed < 100:
			bot.say('Im not hungry(last fed %s seconds ago)' % str(lastfed))
		else:
			foodType = [('peanut', 25), ('Roach', -10), ('Mana Biscuit', 50), ('Lobster', 100), ('Grass', 5), ('Soup', 150)]
			fruit, gainHP = foodType[random.randint(0, len(foodType)-1)]
			bot.say ('You fed %s a %s. Gains %g HP' % (pokedex[trigger.nick].pokename, fruit, gainHP))
			pokedex[trigger.nick].AddXP(gainHP/10)
			pokedex[trigger.nick].Heal(gainHP)
			pokedex[trigger.nick].time = time.time()

@commands('revive')
def reviveP(bot, trigger):
	if pokedex[trigger.nick].hp > 0:
		BotBlueMsg ('[NURSE JOY] %s does not need to be revived' % pokedex[trigger.nick].pokename)
	else:
		minRevivetime = 300
		if time.time() - pokedex[trigger.nick].revivetime < minRevivetime:
			revivetime = int(minRevivetime - (time.time() - pokedex[trigger.nick].revivetime))
			BotBlueMsg ('[NURSE JOY] You still need to wait %g seconds before reviving' % revivetime)
		else:
			BotBlueMsg('[NURSE JOY] %s, you have successfully revived %s' % (trigger.nick , pokedex[trigger.nick].pokename))
			pokedex[trigger.nick].hp = pokedex[trigger.nick].maxhp
			pokedex[trigger.nick].revivetime = time.time()

@commands('poke')
def poke(bot, trigger):
	if trigger.group(2) in pokedex:
		bot.say(str(pokedex[trigger.group(2)]))
	else:
		bot.say(str(pokedex[trigger.nick]))

@commands('explore')
def cEnemy(bot, trigger):
	if 'evilPokemon' in globals() == False:
		global evilPokemon

	try:
		if evilPokemon.hp > 0:
			BotErrMsg('%s is preventing you from exploring' %evilPokemon.pokename)
			return 0
	except Exception:
		hello = 1

	enemyName = GenPokeName()
	BotBlueMsg('A wild Pokemon has appeared!')
	evilPokemon = NPCPokemon(enemyName, RollDice(3,40))
	evilPokemon.isNPC = True
	evilPokemon.weapon = 2, random.randint(1,18)

	if random.randint(0,100) < 80:
		evilPokemon.crit = random.randint(2,30)
		evilPokemon.killxp += 50
	if random.randint(0,100) < 20:
		evilPokemon.block = random.randint(2,10)
		evilPokemon.killxp += 115
	if random.randint(0,100) < 20:
		evilPokemon.evade = random.randint(20,65)
		evilPokemon.killxp += 300
	if random.randint(0,100) < 15:
		evilPokemon.dunkmaster = random.randint(20,70)
		evilPokemon.pokename = '[Dunkmaster]' + evilPokemon.pokename

	try:
		evilPokemon.level = random.randint(1, pokedex[trigger.nick].level+3)
	except KeyError:
		evilPokemon.level = 1
	bot.say(str(evilPokemon))

@commands('enemyinfo')
def enemyInfo(bot, trigger):
	bot.say(str(evilPokemon))

@commands('explorewilds')
def cEnemy2(bot, trigger):
	if pokedex[trigger.nick].level > 15:
		global evilPokemon
		enemyName = '[Dragon]' + trigger.nick + 'saur'
		BotBlueMsg('You explore the tall grass.... A wild [Dragon] Pokemon has appeared!')
		evilPokemon = Pokemon(enemyName, RollDice(12,36))
		evilPokemon.weapon = 3,20
		evilPokemon.crit = RollDice(1,30)
		evilPokemon.block = RollDice(1,12)
		evilPokemon.evade = RollDice(1,12)
		evilPokemon.level = RollDice(15,30)
		bot.say(str(evilPokemon))
	else:
		BotErrMsg('You must be level 15 before exploring the wilds')


@commands('fight')
def fightp(bot, trigger):
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
	myBot.say('[warning]evolve will consume 1 level from the active pokemon. To successfully evolve, roll 2D6 with 6 or higher roll')
	if pokedex[trigger.nick].level > pokedex[trigger.nick].nextEvolve :
		if RollDice(2,6,1) > 5:
			myBot.say('Evolution Complete! check out the new stats with .poke')
			pokedex[trigger.nick].nextEvolve += 5
			damageDice, damageRoll = pokedex[trigger.nick].weapon
			damageRoll += RollDice(1,5)
			pokedex[trigger.nick].weapon = damageDice, damageRoll
			pokedex[trigger.nick].pokename = pokedex[trigger.nick].pokename + GenSuffix()
			pokedex[trigger.nick].perks += 2
			# pokedex[trigger.nick].nextLvlXP = RollDice(10,100)
		else:
			myBot.say ('Evolution Failed, %s lost a level' % pokedex[trigger.nick].pokename)
			pokedex[trigger.nick].level -= 1
	else: 
		myBot.say ('%s Needs to be at least level %g before evolving' % (pokedex[trigger.nick].pokename, pokedex[trigger.nick].nextEvolve))

# @commands('operationcwal')
# def cheatcode(bot, trigger):
# 	pokedex[trigger.nick].AddXP(1000)


def RollDice(numDice, numHeads, verbose = 0):
	diceSum = 0
	for i in range (numDice):
		diceSum += random.randint(1,numHeads)
	if verbose == 1:
		myBot.say ( sopel.formatting.color('[DICE(%gD%g)] I rolled %g' % (numDice, numHeads, diceSum), '02'))
	return diceSum


class Pokemon(object):
	def __init__(self, pokename, hp):
		self.level = 1
		self.pokename = str(pokename)
		self.maxhp = hp
		self.hp = self.maxhp
		self.xp = 0
		self.nextLvlXP = 500
		self.nextEvolve = 4
		self.perks = 3
		self.isNPC = False
		self.killxp = random.randint(200,450)

		#Battle information
		self.weapon = 2,12
		self.block = 0
		self.crit = 0
		self.evade = 0
		self.dunkmaster = 0

		#Time information
		self.time = time.time() - 600
		self.revivetime = time.time() - 600
		print self


	def AddXP(self, addXP):
		self.xp += addXP
		myBot.say ('%s has gained %g XP' % (self.pokename, addXP))
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


	def TakeDamage(self, damage):
		if self.evade > RollDice(1,100):
			myBot.say('%s Evaded the attack' % self.pokename)
		else:
			tdamage = damage - self.block
			if tdamage < 0:
				tdamage = 0
			self.hp -= tdamage
			myBot.say ( '%s took %g damage (%g Blocked) (Hp:%g/%g)' % (self.pokename, tdamage, self.block, self.hp, self.maxhp))
		if self.hp < 1:
			BotBlueMsg (str(self.pokename) + ' has fainted')

	def Heal(self, Healamount):
		self.hp += Healamount
		if self.hp > self.maxhp:
			self.hp = self.maxhp
		myBot.say ( '%s Healed for %g  (Hp:%g/%g)' % (self.pokename, Healamount, self.hp, self.maxhp))

	def GetAttackDamage(self):
		# print '%s is now GetAttackDamageing with weapon %g, %g' % (self.pokename, numDice, numHeads)
		numDice, numHeads = self.weapon
		damage = RollDice(numDice, numHeads)
		if self.crit > random.randint(1,100):
			damage = damage*2
			myBot.say('%s Scored a Critial Strike (%g Damage)!!'% (self.pokename, damage))
		return damage

	def GetDamage(self):
		damage = '%gD%g' % (self.weapon)
		return damage

class NPCPokemon(Pokemon):

	def __str__(self):
		numDice, diceDamage = self.weapon
		myMsg = '[%s]Hi! I am a level %g pokemon. (HP:%g/%g) (Damage:%gD%g)(Crit:%g, Defense:%g, Evade:%g)(XP value: %g)' % (self.pokename, self.level, self.hp, self.maxhp, numDice, diceDamage, self.crit, self.block, self.evade, self.killxp)
		return myMsg

	def GetAttackDamage(self):
		# print '%s is now GetAttackDamageing with weapon %g, %g' % (self.pokename, numDice, numHeads)
		numDice, numHeads = self.weapon
		damage = RollDice(numDice, numHeads)
		if self.crit > random.randint(1,100):
			damage = damage*2
			myBot.say('%s Scored a Critial Strike (%g Damage)!!'% (self.pokename, damage))
		if self.dunkmaster > random.randint(1,100):
			damage = damage * 5
			BotBlueMsg('%s Uses Noxian Guillotine - It is super effective!' %self.pokename)
		return damage	

def PokeBattle(poke1, poke2):
	myBot.say ('%s (%s Damage) will now battle %s (%s Damage)' % (poke1.pokename, str(poke1.GetDamage()), poke2.pokename, str(poke2.GetDamage())))
	while poke1.hp > 0 and poke2.hp > 0:
		damage = poke1.GetAttackDamage()
		poke2.TakeDamage(damage)
		if poke2.hp < 1:
			if poke2.isNPC == True:
				poke1.AddXP(poke2.killxp)
			else:
				poke1.AddXP(random.randint(200,450))
			break
		time.sleep(1)


		damage = poke2.GetAttackDamage()
		poke1.TakeDamage(damage)
		if poke1.hp <1:
			if poke2.isNPC == False:
				poke2.AddXP(random.randint(200,450))
			break
		time.sleep(1)

	
def GenPokeName():
	pokemons = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidoran', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'Farfetchd', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'MrMime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo']
	chosenpokemon = pokemons[random.randint(0,len(pokemons) -1 )]
	return chosenpokemon

def GenSuffix():
	suffixtype = ['mon', 'chu', 'izard', 'saur', 'pie', 'pod','ly']
	chosensuffix = suffixtype[random.randint(0,len(suffixtype)-1)]
	return chosensuffix


