import chromance, colours

stemSegments = [23, 33, 22, 11, 34, 10]
flowerSegments = [24, 21, 32, 37, 36, 35, 12, 13, 14, 9, 0, 27]

def setProfile():
    chromance.profile = 'Flower'
    chromance.speed = 0.01
    
def doUpdate():
    chromance.fadeAll()
    spawnSegments()

def spawnSegments():
    if chromance.getNumOnLEDs() != 0: return
    chromance.createDrawing(colours.green, stemSegments, 100, 633, 5)
    chromance.createDrawing(colours.deepPink, flowerSegments, 100, 1266, 5)
