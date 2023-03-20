from random import randrange

def getRandomNumber(min, max):
    return randrange(min, max)

def getRandomNumberBut(min, max, exclusion):
    number = getRandomNumber(min, max)
    if(max - min > 1):
        while number == exclusion:
            number = getRandomNumber(min, max)
    
    return number

def pickRandom(options):
    return options[randrange(0, len(options))]

def pickRandomBut(options, exclusion):
    option = pickRandom(options)
    if len(options) > 1:
        while option == exclusion:
            option = pickRandom(options)
            
    return option