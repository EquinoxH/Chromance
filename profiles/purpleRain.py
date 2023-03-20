import chromance, colours, myRandom, time

options = [42, 13, 294, 265, 223, 335, 545, 125, 154, 447, 195, 517]
rainColours = [colours.blueViolet,
               colours.darkMagenta,
               colours.darkSlateBlue,
               colours.darkViolet,
               colours.deepPink,
               colours.fuchsia,
               colours.hotPink,
               colours.lavender,
               colours.lavenderBlush,
               colours.magenta,
               colours.mediumOrchid,
               colours.mediumPurple,
               colours.mediumVioletRed,
               colours.orchid,
               colours.plum,
               colours.purple,
               colours.slateBlue,
               colours.thistle]

lastTime = 0
lastLocation = -1
lastColour = colours.black

def setProfile():
    chromance.profile = 'PurpleRain'
    chromance.speed = 0.01

def doUpdate():
    chromance.fadeAll()
    spawnTrails()

def spawnTrails():
    global lastTime, lastLocation, lastColour
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    if chromance.getCurrent() >= (1200) or elapsed <= 100: return
    lastTime = currentTime
    
    start = myRandom.pickRandomBut(options, lastLocation)
    colour = myRandom.pickRandomBut(rainColours, lastColour)
    
    lastLocation = start
    lastColour = colour
    
    chromance.createTrail(colour, start, 13, False)
