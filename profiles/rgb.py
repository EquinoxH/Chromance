import chromance, hub, colours, time

lastSpawn = -1
lastTime = 0

def setProfile():
    chromance.profile = 'RGB'
    chromance.speed = 0.00001

def doUpdate():
    chromance.fadeAll()
    spawnTrails()

def spawnTrails():
    global lastSpawn, lastTime
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    
    randColour = colours.getRandomColour()
    predictedCurrent = 366 * ((randColour[0] + randColour[1] + randColour[2]) / (3 * 255))
    
    current = chromance.getCurrent()
    
    if (predictedCurrent + current < 1900) and elapsed >= 250:
        spawn = hub.getRandom().getRandomLEDExcept(lastSpawn)
        lastSpawn = spawn
        lastTime = currentTime
        chromance.createTrail(colour = randColour, start = spawn, lifetime = 70, immortal = False)
