import chromance, hub, myRandom, time, colours

options = [42, 13, 294, 265, 223, 335, 545, 125, 154, 447, 195, 517]
lastTime = 0
lastLocation = -1

def setProfile():
    chromance.profile = 'Snowfall'
    chromance.speed = 0.5

def doUpdate():
    chromance.superFadeAll()
    spawnTrails()

def spawnTrails():
    global lastTime, lastLocation
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    if chromance.getCurrent() >= (1600) or elapsed <= 100: return
    lastTime = currentTime
    
    start = myRandom.pickRandomBut(options, lastLocation)
    chromance.createTrail(colours.white, start, 13, False)
    lastLocation = start
    