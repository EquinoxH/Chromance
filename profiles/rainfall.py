import chromance, colours, myRandom, time

options = [42, 13, 294, 265, 223, 335, 545, 125, 154, 447, 195, 517]
rainColours = [colours.aqua,
               colours.cornflowerBlue,
               colours.cyan,
               colours.darkBlue,
               colours.darkTurquoise,
               colours.deepSkyBlue,
               colours.dodgerBlue,
               colours.lightBlue,
               colours.lightCyan,
               colours.lightSkyBlue,
               colours.lightSteelBlue,
               colours.mediumBlue,
               colours.midnightBlue,
               colours.navy,
               colours.royalBlue,
               colours.skyBlue]

lastTime = 0
lastLocation = -1
lastColour = colours.black

def setProfile():
    chromance.profile = 'Rainfall'
    chromance.speed = 0.01

def doUpdate():
    chromance.fadeAll()
    spawnTrails()

def spawnTrails():
    global lastTime, lastLocation, lastColour
    
    currentTime = time.ticks_ms()
    elapsed = currentTime - lastTime
    if chromance.getCurrent() >= (800) or elapsed <= 100: return
    lastTime = currentTime
    
    start = myRandom.pickRandomBut(options, lastLocation)
    colour = myRandom.pickRandomBut(rainColours, lastColour)
    
    lastLocation = start
    lastColour = colour
    
    chromance.createTrail(colour, start, 13, False)