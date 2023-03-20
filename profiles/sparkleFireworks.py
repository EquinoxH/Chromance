import chromance, hub, myRandom, colours, time

lastLife = 0
lastTime = 0
lastLocation = -1
nextColour = colours.off

spawnLocations = [210, 0, 322, 307, 532, 112, 182, 167, 504, 434]

def setProfile():
    chromance.profile = 'SparkleFireworks'
    chromance.speed = 0.001
    
def doUpdate():
    chromance.fadeAll()
    spawnFirework()
    
def spawnFirework():
    global lastLocation, lastTime, nextColour
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    
    nextColour = colours.getRandomColour()
    requiredCurrent = 300 * 6 * ((nextColour[0] + nextColour[1] + nextColour[2]) / (255 * 3))
    
    if chromance.getCurrent() + requiredCurrent <= 1900 and elapsed >= 600:
        spawn = myRandom.pickRandomBut(spawnLocations, lastLocation)
        chromance.createTrail(colours.red, spawn, 12, False, 1, True)
        
        lastTime = currentTime
        lastLocation = spawn
           
def spawnDrawing(deathLocation):
    global lastLife, nextColour
    chromance.speed = 0.001
    targetHub = hub.getConnectedHub(deathLocation)
    segments = targetHub.segmentIDs
    
    life = myRandom.getRandomNumberBut(20, 40, lastLife)
    lastLife = life
    
    chromance.createDrawing(nextColour, segments, life, 300, 3)