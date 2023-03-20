import chromance, shapes.dot, myRandom, time, colours

lastLED = -1
lastSegment = -1
lastTime = 0

class Drawing():
    def __init__(self, colour, segments, lifetime, maxCurrent, ledsPerUpdate):
        self.colour = colour
        self.segments = segments
        self.lifetime = lifetime
        self.current = colours.getCurrentForColour(self.colour)
        self.maxLEDs = maxCurrent / self.current
        self.ledsPerUpdate = ledsPerUpdate
        
        for segment in segments:
            print(f'segment: {segment}')
            chromance.createSegment(colour, segment)
        
    def getCurrent(self):
        return self.current * self.maxLEDs
        
    def update(self):
        self.lifetime -= 1