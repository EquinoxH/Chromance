import chromance, hub, myRandom, time, colours

options = [55, 0, 307, 252, 210, 322, 532, 112, 167, 434, 182, 504]
lastTime = 0
lastLocation = -1

def setProfile():
    chromance.profile = 'Embers'
    chromance.speed = 0.5

def doUpdate():
    chromance.superFadeAll()
    spawnTrails()

def spawnTrails():
    global lastTime, lastLocation
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    if chromance.getCurrent() >= (1600) or elapsed <= 50: return
    lastTime = currentTime
    
    start = myRandom.pickRandomBut(options, lastLocation)
    chromance.createTrail((255,64,0), start, 13, False)