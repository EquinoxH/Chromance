import chromance, hub

class Dot():
    def __init__(self, colour, location, lifetime):
        self.colour = colour
        self.location = location
        self.lifetime = lifetime
        
    def update(self):
        self.lifetime -= 1
        self.show()
        
    def show(self):
        chromance.setLEDFromNumber(self.location, self.colour)
        
    def getCurrent(self):
        return 60 * ((self.colour[0] + self.colour[1] + self.colour[2]) / (3 * 255))