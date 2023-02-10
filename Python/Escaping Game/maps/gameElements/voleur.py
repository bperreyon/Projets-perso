from other.utils import isBetween, isStrictBetween
from other.constants import characterSize, mapHeight, mapWidth,Orientation
from .personnage import Personnage


class Voleur(Personnage):

    def __init__(self,x,y,orientation,canvas):
        super().__init__(x,y,orientation)
        self.__drawing = canvas.create_rectangle(x-characterSize,y-characterSize,x+characterSize,y+characterSize,fill="violet")
        self.__speed=5
        self.__inventory ={'key':0,'timeSlower':0}
    
    def move(self,canvas,touche):
        xBefore,yBefore = self._x,self._y
        if (touche=="z"):
            if (self._orientation==Orientation.NORTH):
                if (self.isUpMovementPossible(canvas.getWalls(),canvas.getObjects(),canvas.getGates())):
                    super().move("y",-self.__speed)
                    canvas.move(self.__drawing,0,-self.__speed)
            else:
                super().turn(Orientation.NORTH)

        elif (touche=="q"):
            if (self._orientation==Orientation.WEST):
                if (self.isLeftMovementPossible(canvas.getWalls(),canvas.getObjects(),canvas.getGates())):
                    super().move("x",-self.__speed)
                    canvas.move(self.__drawing,-self.__speed,0)
            else:
                super().turn(Orientation.WEST)

        elif (touche=="s"):
            if (self._orientation==Orientation.SOUTH):
                if (self.isDownMovementPossible(canvas.getWalls(),canvas.getObjects(),canvas.getGates())):
                    super().move("y",self.__speed)
                    canvas.move(self.__drawing,0,self.__speed)
            else:
                super().turn(Orientation.SOUTH)

        elif (touche=="d"):
            if (self._orientation==Orientation.EAST):
                if (self.isRightMovementPossible(canvas.getWalls(),canvas.getObjects(),canvas.getGates())):
                    super().move("x",self.__speed)
                    canvas.move(self.__drawing,self.__speed,0)
            else:
                super().turn(Orientation.EAST)
        
        # Post movement check
        canvas.isThiefSeen()
        canvas.isThiefOnObjective()
        canvas.isThiefDetected()
        if ((self._x!=xBefore) or (self._y!=yBefore)):
            canvas.isThiefOnWarper()
    
    def isUpMovementPossible(self,walls,objects,gates):
        ##Extrémité de la map
        if (self._y-characterSize-self.__speed<0):
            return False
        
        ## Murs
        i=0
        movementIsPossible = True
        while i<len(walls) and movementIsPossible:
            x0,y0,x1,y1 = walls[i].getCoord()
            if (self._y-characterSize==y1):
                if ((isStrictBetween(self._x-characterSize, x0, x1)) or (isStrictBetween(self._x+characterSize, x0, x1))):
                    return False
            i+=1

        ## Portes
        i=0
        while i<len(gates) and movementIsPossible:
            x0,y0,x1,y1 = gates[i].getCoord()
            if (self._y-characterSize==y1):
                if (gates[i].getOrientation()==Orientation.NORTH or gates[i].getOrientation()==Orientation.SOUTH):
                    if ((isStrictBetween(self._x-characterSize, x0, x1)) or (isStrictBetween(self._x+characterSize, x0, x1))):
                        return False
                else:
                    if ((isStrictBetween(x0, self._x-characterSize, self._x+characterSize)) or (isStrictBetween(x1, self._x-characterSize, self._x+characterSize))):
                        return False
            i+=1
        
        ## Objets
        i=0
        while i<len(objects) and movementIsPossible:
            x,y = objects[i].getCoord()
            if (self._y-2*characterSize==y):
                if ((self._x==x) or (isStrictBetween(self._x-characterSize, x-characterSize, x+characterSize)) or (isStrictBetween(self._x+characterSize, x-characterSize, x+characterSize))):
                    return False
            i += 1
        return movementIsPossible

    def isRightMovementPossible(self,walls,objects,gates):
        ##Extrémité de la map
        if (self._x+characterSize+self.__speed>mapWidth):
            return False
        
        ## Murs
        i=0
        movementIsPossible = True
        while i<len(walls) and movementIsPossible:
            x0,y0,x1,y1 = walls[i].getCoord()
            if (self._x+characterSize==x0):
                if ((isStrictBetween(self._y-characterSize, y0, y1)) or (isStrictBetween(self._y+characterSize, y0, y1))):
                    return False
            i+=1

        ## Portes
        i=0
        while i<len(gates) and movementIsPossible:
            x0,y0,x1,y1 = gates[i].getCoord()
            if (self._x+characterSize==x0):
                if (gates[i].getOrientation()==Orientation.EAST or gates[i].getOrientation()==Orientation.WEST):
                    if ((isStrictBetween(self._y-characterSize, y0, y1)) or (isStrictBetween(self._y+characterSize, y0, y1))):
                        return False
                else:
                    if ((isStrictBetween(y0, self._y-characterSize, self._y+characterSize)) or (isStrictBetween(y1, self._y-characterSize, self._y+characterSize))):
                        return False
            i+=1
        
        ## Objets
        i=0
        while i<len(objects) and movementIsPossible:
            x,y = objects[i].getCoord()
            if  (self._x+2*characterSize==x):
                if ((self._y==y) or (isStrictBetween(self._y-characterSize, y-characterSize, y+characterSize)) or (isStrictBetween(self._y+characterSize, y-characterSize, y+characterSize))):
                    return False
            i += 1
        return movementIsPossible

    def isDownMovementPossible(self,walls,objects,gates):
        ##Extrémité de la map
        if (self._y+characterSize+self.__speed>mapHeight):
            return False
        
        ## Murs
        i=0
        movementIsPossible = True
        while i<len(walls) and movementIsPossible:
            x0,y0,x1,y1 = walls[i].getCoord()
            if (self._y+characterSize==y0):
                if ((isStrictBetween(self._x-characterSize, x0, x1)) or (isStrictBetween(self._x+characterSize, x0, x1))):
                    return False
                
            i+=1

        ## Portes
        i=0
        while i<len(gates) and movementIsPossible:
            x0,y0,x1,y1 = gates[i].getCoord()
            if (self._y+characterSize==y0):
                if (gates[i].getOrientation()==Orientation.NORTH or gates[i].getOrientation()==Orientation.SOUTH):
                    if ((isStrictBetween(self._x-characterSize, x0, x1)) or (isStrictBetween(self._x+characterSize, x0, x1))):
                        return False
                else:
                    if ((isStrictBetween(x0, self._x-characterSize, self._x+characterSize)) or (isStrictBetween(x1, self._x-characterSize, self._x+characterSize))):
                        return False
            i+=1

        ## Objets
        i=0
        while i<len(objects) and movementIsPossible:
            x,y = objects[i].getCoord()
            if (self._y+2*characterSize==y):
                if ((self._x==x) or (isStrictBetween(self._x-characterSize, x-characterSize, x+characterSize)) or (isStrictBetween(self._x+characterSize, x-characterSize, x+characterSize))):
                    return False
            i += 1
        return movementIsPossible
    
    def isLeftMovementPossible(self,walls,objects,gates):
        ##Extrémité de la map
        if (self._x-characterSize-self.__speed<0):
            return False
        
        ## Murs
        i=0
        movementIsPossible = True
        while i<len(walls) and movementIsPossible:
            x0,y0,x1,y1 = walls[i].getCoord()
            if (self._x-characterSize==x1):
                if ((isStrictBetween(self._y-characterSize, y0, y1)) or (isStrictBetween(self._y+characterSize, y0, y1))):
                    return False
            i+=1

        ## Portes
        i=0
        while i<len(gates) and movementIsPossible:
            x0,y0,x1,y1 = gates[i].getCoord()
            if (self._x-characterSize==x1):
                if (gates[i].getOrientation()==Orientation.EAST or gates[i].getOrientation()==Orientation.WEST):
                    if ((isStrictBetween(self._y-characterSize, y0, y1)) or (isStrictBetween(self._y+characterSize, y0, y1))):
                        return False
                else:
                    if ((isStrictBetween(y0, self._y-characterSize, self._y+characterSize)) or (isStrictBetween(y1, self._y-characterSize, self._y+characterSize))):
                        return False
            i+=1
        
        ## Objets
        i=0
        while i<len(objects) and movementIsPossible:
            x,y = objects[i].getCoord()
            if (self._x-2*characterSize==x):
                if ((self._y==y) or (isStrictBetween(self._y-characterSize, y-characterSize, y+characterSize)) or (isStrictBetween(self._y+characterSize, y-characterSize, y+characterSize))):
                    return False
            i += 1
        return movementIsPossible

    def getDrawing(self):
        return self.__drawing
    
    def setCoords(self,x,y):
        self._x = x
        self._y = y
    
    def addItem(self,item):
        self.__inventory[item]+=1
    
    def removeItem(self,item):
        self.__inventory[item]-=1
    
    def hasItem(self,item):
        return self.__inventory[item]!=0
    
    