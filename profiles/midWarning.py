import chromance, hub, colours, time

lastHub = -1
lastTime = 0

def setProfile():
    chromance.profile = 'Mid'
    chromance.speed = 0.001
    
def doUpdate():
    chromance.fadeAll()
    spawnTrails()

def spawnTrails():
    global lastHub, lastTime
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    
    current = chromance.getCurrent()
    if current < 1000 and elapsed >= 250:
        
        spawnHub = hub.getRandomExcept(lastHub)
        spawn = spawnHub.getRandomLED()
        chromance.createTrail(colours.orangeRed, spawn, 69, False, 2)
        
        lastSpawn = spawn
        lastTime = currentTime
        
