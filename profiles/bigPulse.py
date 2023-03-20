import chromance, hub, colours, myRandom, time

lastHub = -1
lastLife = 0

def setProfile():
    chromance.profile = 'BigPulse'
    chromance.speed = 0.01

def doUpdate():
    chromance.fadeAll()
    spawnTrails()

def spawnTrails():
    global lastHub, lastLife
    
    if len(chromance.trails) > 1:
        return;
    
    randomColour = colours.getRandomColour()
    randomHub = hub.getRandomExcept(lastHub)
    while len(randomHub.ledIDs) < 4:
        randomHub = hub.getRandomExcept(lastHub)    
    
    lastHub = randomHub.hubID
    
    for i in range(len(randomHub.ledIDs)):
        life = myRandom.getRandomNumberBut(14, 43, lastLife)
        lastLife = life
        
        spawn = randomHub.ledIDs[i]
        chromance.createTrail(randomColour, spawn, life, False)
