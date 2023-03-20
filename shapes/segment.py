import chromance

class Segment():
    def __init__(self, colour, start):
        self.colour = colour
        self.start = start
        
    def show(self):
        direction = 1 if self.start % 2 == 0 else -1
        for i in range(13):
            led = self.start + (i * direction)
            chromance.setLEDFromNumber(led, self.colour)
            
    def getCurrent(self):
        return 14 * 60 * (self.colour[0] + self.colour[1] + self.colour[2]) / (3 * 255)
    
class GradientSegment():
    def __init__(self, colours, start):
        self.colours = colours
        self.currentColour = 0
        self.segmentID = start
        self.progress = 0
        
    def show(self):
        self.fillSegment(colours[0])
            
    def fillSegment(self, colour):
        direction = 1 if self.start % 2 == 0 else -1
        for i in range(13):
            led = self.start + (i * direction)
            chromance.setLEDFromNumber(led, self.colours[0])
        
    def update():
        startColour = self.colours[self.currentColour]
        nextIndex = 0
        if self.currentColour != len(self.colours) - 1:
            nextIndex = self.currentColour + 1
            
        endColour = self.colours[nextIndex]
        
        rDiff = startColour[0] - endColour[0]
        gDiff = startColour[1] - endColour[1]
        bDiff = startColour[2] - endColour[2]
            
        r = int(startColour[0] + ((self.progress / 100) * rDiff))
        g = int(startColour[1] + ((self.progress / 100) * gDiff))
        b = int(startColour[2] + ((self.progress / 100) * bDiff))
        
        self.fillSegment((r,g,b))
        
    def getCurrent(self):
        