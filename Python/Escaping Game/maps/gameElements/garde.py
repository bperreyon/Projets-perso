from other.constants import rotationAngles, characterSize,refreshFrameTime, Orientation,GuardType

from .personnage import Personnage
from .vision import Vision


class Garde(Personnage):

    """
    @attributes:
        path: list of location that define the guard movement
        vision: object that represent the zone the guard can see
    """
    def __init__(self,x,y,orientation,guardType,canvas,path=[],speed=0,reverse=False):
        # Check arguments
        if (guardType==GuardType.MOBIL and (len(path)==0 or speed==0 or reverse)):
            return
        if (guardType==GuardType.ROTATER and (len(path)==0 or speed==0)):
            return
        if (guardType==GuardType.FIX and (len(path)!=0 or speed!=0 or reverse)):
            return
        super().__init__(x,y,orientation)

        self.__type = guardType
        self.__path = path
        self.__pathPart = 0
        self.__speed = speed
        self.__waitedFrame = 0
        self.__isBackwards = False
        self.__reverse = reverse
        self.__drawing = canvas.create_rectangle(x-characterSize,y-characterSize,x+characterSize,y+characterSize,fill="red")
        self.__vision = Vision(x, y, orientation, canvas)
    

    def move(self,canvas):
        if (self.__type==GuardType.MOBIL):
            destination = self.__path[self.__pathPart]

            if (destination['x']==self._x):
                if (destination['y']>self._y):
                    if (self._orientation==Orientation.SOUTH):
                        super().move("y",self.__speed)
                        canvas.move(self.__drawing,0,self.__speed)
                        self.__vision.move(0,self.__speed,canvas)
                    else:
                        self.turn(Orientation.SOUTH,canvas)

                elif(destination['y']<self._y):
                    if (self._orientation==Orientation.NORTH):
                        super().move("y",-self.__speed)
                        canvas.move(self.__drawing,0,-self.__speed)
                        self.__vision.move(0,-self.__speed,canvas)
                    else:
                        self.turn(Orientation.NORTH,canvas)

            elif (destination['y']==self._y):
                
                if (destination['x']>self._x):
                    if (self._orientation==Orientation.EAST):
                        super().move("x",self.__speed)
                        canvas.move(self.__drawing,self.__speed,0)
                        self.__vision.move(self.__speed,0,canvas)
                    else:
                        self.turn(Orientation.EAST,canvas)

                elif (destination['x']<self._x):
                    if (self._orientation==Orientation.WEST):
                        super().move("x",-self.__speed)
                        canvas.move(self.__drawing,-self.__speed,0)
                        self.__vision.move(-self.__speed,0,canvas)
                    else:
                        self.turn(Orientation.WEST,canvas)

            else:
                print("Error, not aligned with destination")
        
            # After movement
            if (self._x==destination['x'] and self._y == destination['y']):
                self.__pathPart+=1
                if (self.__pathPart>=len(self.__path)):
                    self.__pathPart=0
    
        elif (self.__type==GuardType.ROTATER):
            self.__waitedFrame+=1
            if (self.__waitedFrame*refreshFrameTime>self.__speed):
                self.__waitedFrame=0
                if (not self.__isBackwards):
                    self.__pathPart+=1
                else:
                    self.__pathPart-=1

                if (self.__pathPart>=len(self.__path)):
                    if (self.__reverse):
                        self.__pathPart-=2
                        self.__isBackwards = True
                    else:
                        self.__pathPart=0
                if (self.__pathPart==-1):
                    self.__isBackwards=False
                    self.__pathPart=1
                
                self.turn(self.__path[self.__pathPart], canvas)
        else:
            pass

            
    def turn(self,orientation,canvas):
        angle = rotationAngles[self._orientation+orientation]
        super().turn(orientation)
        self.__vision.turn((self._x,self._y),angle,canvas,orientation)

    def getVison(self):
        xV0,yV0,xV1,yV1 = self.__vision.getVisionCoords()
        guardCoords = super().getBorderCoord()
        xMin = min(xV0,xV1,guardCoords[0][0],guardCoords[1][0],guardCoords[2][0],guardCoords[3][0])
        xMax = max(xV0,xV1,guardCoords[0][0],guardCoords[1][0],guardCoords[2][0],guardCoords[3][0])
        yMin = min(yV0,yV1,guardCoords[0][1],guardCoords[1][1],guardCoords[2][1],guardCoords[3][1])
        yMax = max(yV0,yV1,guardCoords[0][1],guardCoords[1][1],guardCoords[2][1],guardCoords[3][1])
        return xMin,yMin,xMax,yMax
