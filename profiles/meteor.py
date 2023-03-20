import chromance, colours, myRandom, time

options = [27, 363, 279, 83, 378, 392, 56, 140, 461, 209, 321, 111, 490, 97]
meteorColours = [colours.orange, colours.orangeRed, colours.springGreen, colours.crimson, colours.white, colours.yellow]

lastTime = 0
lastLocation = -1
lastColour = colours.black
delay = 0

def setProfile():
    chromance.profile = 'Meteor'
    chromance.speed = 0.001

def doUpdate():
    chromance.fadeAll()
    spawnTrails()

def spawnTrails():
    global lastTime, lastLocation, lastColour, delay
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    
    if chromance.getCurrent() >= (1500) or elapsed <= delay:
        return
        
    start = myRandom.pickRandomBut(options, lastLocation)
    colour = myRandom.pickRandomBut(meteorColours, lastColour)
        
    chromance.createTrail(colour, start, 12, False, 3)
    lastTime = currentTime
    delay = myRandom.getRandomNumber(500, 1000)