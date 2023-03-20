from machine import Pin
from neopixel import NeoPixel

import chromance, colours

network1 = NeoPixel(Pin(0), 84, timing = 1)
network2 = NeoPixel(Pin(2), 154, timing = 1)
network3 = NeoPixel(Pin(4), 168, timing = 1)
network4 = NeoPixel(Pin(6), 154, timing = 1)

networks = [network1, network2, network3, network4]

class Strip():
    def __init__(self, stripID, pin, ledCount):
        self.stripID = stripID
        self.leds = NeoPixel(Pin(pin), ledCount)
        self.ledCount = ledCount
        self.colours = [colours.off] * ledCount
        self.onLEDs = set()
        
    def fill(self, colour):
        self.leds.fill(colour)
        self.colours = [colour] * self.ledCount
        self.onLEDs = set(range(self.ledCount))
        self.leds.write()
        
    def setLED(self, index, colour):
        self.leds[index] = colour
        self.colours[index] = colour
        
        if colours.isOff(colour) and index in self.onLEDs:
            self.onLEDs.remove(index)
        elif index not in self.onLEDs:
            self.onLEDs.add(index)
        
    def write(self):
        self.leds.write()
        
    def fadeLED(self, index):
        newColour = tuple([int(0.6 * x) for x in self.colours[index]])
        self.colours[index] = newColour
        self.leds[index] = newColour
        if colours.isOff(newColour):
            self.onLEDs.remove(index)
            
    def fadeAll(self):
        for led in self.onLEDs:
            self.fadeLED(led)
            
    def superFadeLED(self, index):
        newColour = tuple([int(0.1 * x) for x in self.colours[index]])
        self.colours[index] = newColour
        self.leds[index] = newColour
        if colours.isOff(newColour):
            self.onLEDs.remove(index)
            
    def superFadeAll(self):
        for led in self.onLEDs:
            self.superFadeLED(led)
            
    def test(self):
        self.fill((64, 64,0))
        
    def off(self):
        self.fill(colours.off)
        self.onLEDs = set()