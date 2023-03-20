import chromance, colours, myRandom, time, math

options = [27, 363, 279, 83, 378, 392, 56, 140, 461, 209, 321, 111, 490, 97]

lastTime = 0
lastLocation = -1
lastColour = colours.black
delay = 0
startTime = time.ticks_ms()

def setProfile():
    chromance.profile = 'Blossom'
    chromance.speed = 0.05
    startTime = time.ticks_ms()

def doUpdate():
    chromance.superFadeAll()
    spawnTrails()

def spawnTrails():
    global lastTime, lastLocation, lastColour, delay
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    
    if chromance.getCurrent() >= (1500) or elapsed < delay:
        return
        
    start = myRandom.pickRandomBut(options, lastLocation)
    red = 255
    totalElapsed = time.ticks_ms() - startTime
    ratio = ((math.sin(totalElapsed / 1000 )) + 1) / 2
    greenBlue = int(64 * ratio)
    colour = (red, greenBlue, greenBlue)
        
    chromance.createTrail(colour, start, 12, False, 1)
    lastTime = currentTime
    delay = myRandom.getRandomNumber(100, 200)
