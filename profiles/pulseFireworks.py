import chromance, hub, myRandom, colours, time

lastTime = 0
lastLocation = -1
nextColour = colours.off

spawnLocations = [210, 0, 322, 307, 532, 112, 182, 167, 504, 434]

def setProfile():
    chromance.profile = 'PulseFireworks'
    chromance.speed = 0.001
    
def doUpdate():
    chromance.fadeAll()
    spawnFirework()
    
def spawnFirework():
    global lastLocation, lastTime, nextColour
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    
    nextColour = colours.getRandomColour()
    requiredCurrent = 360 * 6 * ((nextColour[0] + nextColour[1] + nextColour[2]) / (255 * 3))
    
    if chromance.getCurrent() + requiredCurrent <= 1900 and elapsed >= 400:
        spawn = myRandom.pickRandomBut(spawnLocations, lastLocation)
        chromance.createTrail(colours.red, spawn, 12, False, 1, True)
        
        lastTime = currentTime
        lastLocation = spawn
        
def spawnPulse(deathLocation):
    global nextColour
    chromance.speed = 0.001
    targetHub = hub.getConnectedHub(deathLocation)
    
    for i in range(len(targetHub.ledIDs)):
        
        spawn = targetHub.ledIDs[i]
        chromance.createTrail(nextColour, spawn, 13, False)