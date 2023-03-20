import chromance, hub, colours, myRandom, time, shapes.dot

lastTime = 0
lastLocation = -1

def setProfile():
    chromance.profile = 'Fireflies'
    chromance.speed = 0.1
    
def doUpdate():
    chromance.fadeAll()
    spawnDots()
    
def spawnDots():
    global lastTime, lastLocation
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    if chromance.getCurrent() >= (1800) or elapsed <= 50: return
    lastTime = currentTime
    
    start = myRandom.getRandomNumberBut(0, 560, lastLocation)
    chromance.createDot(colours.greenYellow, start, 1)