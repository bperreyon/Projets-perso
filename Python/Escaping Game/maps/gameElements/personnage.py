from other.constants import characterSize

class Personnage:
    """
    @attributes:
        x: horizontal location
        y: vertical location
        orientation: N/E/S/W
    """
    def __init__(self,x,y,orientation):
        self._x = x
        self._y = y
        self._orientation = orientation
    
    def move(self,direction,value):
        if (direction=="x"):
            self._x+=value
        elif (direction=="y"):
            self._y+=value
   
    def turn(self,orientation):
        self._orientation = orientation
    
    def getXCood(self):
        return self._x
    
    def getYCoord(self):
        return self._y
    
    def getCenterCoord(self):
        return self._x,self._y
    
    def getBorderCoord(self):
        return [
            (self._x - characterSize, self._y - characterSize),
            (self._x + characterSize, self._y - characterSize),
            (self._x - characterSize, self._y + characterSize),
            (self._x + characterSize, self._y + characterSize)
            ]

    def getOrientation(self):
        return self._orientation
    
 
