import chromance, colours

segments = [23, 27, 16, 15, 8, 7, 6, 29, 30, 31, 38, 28, 24]

def setProfile():
    chromance.profile = 'Heart'
    chromance.speed = 0.01
    
def doUpdate():
    spawnSegments()

def spawnSegments():
    if chromance.getNumOnLEDs() != 0: return
    chromance.createDrawing(colours.deepPink, segments, 100, chromance.maxCurrent, 5)