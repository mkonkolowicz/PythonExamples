"""This is the nautical module"""
class Boat:
    """Boat class"""
    def __init__(self, propType, numHulls, name):
        self.proptype = propType
        self.numhulls = numHulls
        self.name = name
    def identifyvessel(self):
        """Provide vessel identification"""
        print("This is the vessel ", self.name)
    def identifydetails(self):
        """Provide vessel details"""
        print(self.identifyvessel, " w ", self.numhulls, " and driven by ", self.proptype)

class Fleet:
    """Fleet class"""
    def __init__(self):
        self.fleet = []
    def createfleet(self):
        """Make me a fleet"""
        self.fleet = Boat("Sail", 3 ,"SailCat"), Boat("Power", 2 ,"PowerCat"), Boat("Power", 1 ,"SpeedCat")
    def numberinfleet(self):
        """How many in the fleet"""
        print("Ther are ",len(self.fleet)," boats in the fleet")

FLEET = Fleet()
FLEET.createfleet()
FLEET.numberinfleet()
