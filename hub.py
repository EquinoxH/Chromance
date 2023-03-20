import myRandom

class Hub:
    def __init__(self, hubID, numSlots, ledIDs, segmentIDs):
        self.hubID = hubID
        self.numSlots = numSlots
        self.ledIDs = ledIDs
        self.segmentIDs = segmentIDs
        
    def getRandomLED(self):
        return myRandom.pickRandom(self.ledIDs)
        
    def getRandomLEDExcept(self, exception):
        return myRandom.pickRandomBut(self.ledIDs, exception)
        
hubs = []
slots = [2,2,2,
         3,5,5,3,
         3,3,3,
         2,3,3,2,
         5,6,5,
         3,3,
         2,3,2,
         4,4,
         2]
hubLEDs = [[27, 28],
           [363, 364],
           [279, 280],
           [41, 83, 42],
           [14, 237, 13, 378, 377],
           [350, 349, 294, 392, 293],
           [266, 559, 265],
           [70, 223, 224],
           [391, 335, 336],
           [405, 545, 546],
           [55, 56],
           [139, 140, 0],
           [307, 461, 462],
           [251, 252],
           [69, 125, 126, 209, 210],
           [321, 322, 475, 476, 153, 154],
           [238, 531, 532, 447, 448],
           [489, 195, 196],
           [308, 517, 518],
           [111, 112],
           [490, 167, 168],
           [433, 434],
           [97, 98, 181, 182],
           [419, 420, 503, 504],
           [84, 406]]

hubSegments = [[1, 2],
               [25, 26],
               [19, 20],
               [2,3,5],
               [0, 1, 16, 26, 27],
               [20, 21, 24, 25, 28],
               [18, 19, 39],
               [5, 15, 16],
               [23, 24, 27],
               [28, 38, 39],
               [3, 4],
               [0, 9, 10],
               [21, 32, 33],
               [17, 18],
               [4, 8, 9, 14, 15],
               [10, 11, 22, 23, 33, 34],
               [17, 31, 32, 37, 38],
               [13, 14, 34],
               [22, 36, 37],
               [7, 8],
               [11, 12, 35],
               [30, 31],
               [6, 7, 12, 13],
               [29, 30, 35, 36],
               [6, 29]]

for i in range(25):
    hubs.append(Hub(i, slots[i], hubLEDs[i], hubSegments[i]))
    
def getRandom():
    return myRandom.pickRandom(hubs)

def getRandomExcept(exception):
    hubIDs = range(25)
    return hubs[myRandom.pickRandomBut(hubIDs, exception)]

def getConnectedHub(ledID):
    for hub in hubs:
        if ledID in hub.ledIDs:
            return hub
        
def ledIsStartOrEnd(ledID):
    if ledID % 14 == 0: return True
    if (ledID + 1) % 14 == 0: return True
    return False