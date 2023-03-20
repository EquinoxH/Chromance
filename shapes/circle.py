import chromance, hub, colours

class Circle():
    def __init__(self, colour, hubID, lifetime):
        self.colour = colour
        self.hubID = hubID
        self.lifetime = lifetime
        self.draw()

    def getCurrent(self):
        return 60 * len(hub.hubs[self.hubID].ledIDs) * colours.getCurrentForColour(self.colour)

    def draw(self):
        center = hub.hubs[self.hubID]
        for led in center.ledIDs:
            chromance.setLEDFromNumber(led, self.colour)

    def update(self):
        self.draw()
        self.lifetime -= 1
        