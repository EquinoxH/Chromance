import chromance, hub

distanceMoved = 0

class Trail():
    def __init__(self, colour, startingLED, lifetime, immortal, speed = 1, hasDeathEffect = False):
        self.colour = colour
        self.currentPosition = startingLED
        self.lifetime = lifetime
        self.isAtStart = True
        self.immortal = immortal
        self.direction = 1 if startingLED % 2 == 0 else -1
        self.speed = speed
        self.hasDeathEffect = hasDeathEffect
        
    def moveWithSpeed(self):
        for i in range(self.speed):
                self.move()
           
    def move(self):
        nextPosition = 0
        if hub.ledIsStartOrEnd(self.currentPosition) and not self.isAtStart:
            currentHub = hub.getConnectedHub(self.currentPosition)
            nextPosition = currentHub.getRandomLEDExcept(self.currentPosition)
            
            self.direction = 1 if nextPosition % 2 == 0 else -1
            self.isAtStart = True
        else:    
            nextPosition = self.currentPosition + self.direction
            self.isAtStart = False
        
        self.currentPosition = nextPosition
        self.show()
        if not self.immortal:
            self.lifetime -= 1
        
    def show(self):
        chromance.setLEDFromNumber(self.currentPosition, self.colour)
        
    def getCurrent(self):
        return self.speed * 360 * (self.colour[0] + self.colour[1] + self.colour[2]) / (3 * 255)