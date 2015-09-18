from sopel import module
import random

@module.rule('hello!?')
def hi(bot, trigger):
    bot.say('Hi, ' + trigger.nick)

@module.rule('benson')
def hi(bot, trigger):
    messages = ["is very gay", "is super gay", "is gays as a unicorn", "is lord of gays", "is - all hail king of the gays", "is GAYYYYY", "eats babies", "loves to spoon", "is a baby cockroach(squish)", "is XXXS"]
    answer = random.randint(0,len(messages) - 1)
    bot.say('[FACT] Benson ' + messages[answer]);

