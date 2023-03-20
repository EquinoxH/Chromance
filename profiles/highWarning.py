import chromance, hub, colours, time

lastHub = -1
lastTime = 0

def setProfile():
    chromance.profile = 'High'
    chromance.speed = 0.001
    
def doUpdate():
    chromance.fadeAll()
    spawnTrails()

def spawnTrails():
    global lastHub, lastTime
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    
    current = chromance.getCurrent()
    if len(chromance.trails) < 3 and elapsed >= 100:
        
        spawnHub = hub.getRandomExcept(lastHub)
        spawn = spawnHub.getRandomLED()
        chromance.createTrail(colours.red, spawn, 12, False, 3)
        
        lastSpawn = spawn
        lastTime = currentTime
        

