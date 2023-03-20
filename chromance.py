from strip import Strip
import hub, colours, time, profileManager
import shapes.trail, shapes.dot, shapes.segment, shapes.drawing, shapes.circle

maxCurrent = 9600

strip1 = Strip(0, 0, 84)
strip2 = Strip(1, 2, 154)
strip3 = Strip(2, 4, 168)
strip4 = Strip(3, 6, 154)
strips = [strip1, strip2, strip3, strip4]

trails = []
dots = []
drawings = []
circles = []

speed = 0.001
trackCurrent = False
profile = 'Embers'

def createTrail(colour, start = hub.getRandom().getRandomLED(), lifetime = 140, immortal = True, speed = 1, hasDeathEffect = False):
    trails.append(shapes.trail.Trail(colour, start, lifetime, immortal, speed, hasDeathEffect))

def createSegment(colour = colours.red, start = 0):
    segmentStart = 14 * start
    thisSegment = shapes.segment.Segment(colour, segmentStart)
    thisSegment.show()
    
def createDot(colour = colours.red, start = 0, lifetime = 10):
    dots.append(shapes.dot.Dot(colour, start, lifetime))

def createDrawing(colour = colours.red, segments = [0], lifetime = 10, maxCurrent = 9600, ledsPerUpdate = 1):
    drawings.append(shapes.drawing.Drawing(colour, segments, lifetime, maxCurrent, ledsPerUpdate))

def createCircle(colour = colours.red, hubID = 0, lifetime = 10):
    circles.append(shapes.circle.Circle(colour, hubID, lifetime))

def off():
    strip1.off()
    strip2.off()
    strip3.off()
    strip4.off()
    
def test():
    strip1.fill(testColour)
    strip2.fill(testColour)
    strip3.fill(testColour)
    strip4.fill(testColour)
    
def writeUpdates():
    strip1.write()
    strip2.write()
    strip3.write()
    strip4.write()
    
def getLED(stripID, index):
    return strips[stripID].colours[index]

def getLEDFromNumber(ledNumber):
    stripID = -1
    index = -1
    if ledNumber < 84:
        stripID = 0
        index = ledNumber
    elif ledNumber < 238:
        stripID = 1
        index = ledNumber - 84
    elif ledNumber < 406:
        stripID = 2
        index = ledNumber - 238
    else:
        stripID = 3
        index = ledNumber - 406
        
    return getLED(stripID, index)
    
def setLEDFromNumber(ledNumber, colour):
    stripID = -1
    index = -1
    if ledNumber < 84:
        stripID = 0
        index = ledNumber
    elif ledNumber < 238:
        stripID = 1
        index = ledNumber - 84
    elif ledNumber < 406:
        stripID = 2
        index = ledNumber - 238
    else:
        stripID = 3
        index = ledNumber - 406
        
    setLED(stripID, index, colour)
    
def setLED(stripID, index, colour):
    strips[stripID].setLED(index, colour)

def getCurrent():
    totalCurrent = 0
    for trail in trails: totalCurrent += trail.getCurrent()
    for dot in dots: totalCurrent += dot.getCurrent()
    for drawing in drawings: totalCurrent += drawing.getCurrent()
    for circle in circles: totalCurrent += circle.getCurrent()
    return totalCurrent

def getNumOnLEDs():
    onLEDCount = 0
    for strip in strips: onLEDCount += len(strip.onLEDs)
    return onLEDCount

# Loop Functions

def fadeAll():
    for strip in strips:
        strip.fadeAll()
        
def superFadeAll():
    for strip in strips:
        strip.superFadeAll()
        
def update():
    for trail in trails:
        if trail.lifetime <= 0:
            trails.remove(trail)
            if trail.hasDeathEffect and profile in profileManager.onDeathFunctions:
                profileManager.doDeathForCurrentProfile(profile, trail.currentPosition + trail.direction)
        else:
            trail.moveWithSpeed()
            
    for dot in dots:
        if dot.lifetime <= 0:
            dots.remove(dot)
        else:
            dot.update()
            
    for drawing in drawings:
        if drawing.lifetime <= 0:
            drawings.remove(drawing)
        else:
            drawing.update()
            
    for circle in circles:
        if circle.lifetime <= 0:
            circles.remove(circle)
        else:
            circle.update()