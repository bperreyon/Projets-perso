
from other.utils import rotate, isStrictBetween,isBetween
from other.constants import characterSize,Orientation


class Vision:
    visionSize=50
    Pente_cone=characterSize/(2*visionSize)

    """
    @params
     orientation: N/E/S/W
    """
    def __init__(self,x,y,orientation,canvas):
        self.setCoordsAccordingToOrientation(x,y,orientation)
        self.__drawing = canvas.create_polygon(self.getDrawingPointsList(orientation),outline="black",fill="yellow")
        self.__isVisionReduced = False

    def move(self,dx,dy,canvas):
        orientation = self.getDirectionOrientation(dx, dy)
        if (not self.doesVisionNeedReducing(orientation,canvas)):
            self.__x0 += dx
            self.__y0 += dy
            self.__x1 += dx
            self.__y1 += dy
            canvas.move(self.__drawing,dx,dy)
        else:
            self.__x0 += dx
            self.__y0 += dy
            newCoords = self.getDrawingPointsList(orientation)
            canvas.coords(self.__drawing,newCoords)
    
    def turn(self,centre,angle,canvas,orientation):
        if (not self.__isVisionReduced):
            self.__x0, self.__y0 = rotate((self.__x0,self.__y0), centre, angle)
            self.__x1, self.__y1 = rotate((self.__x1,self.__y1), centre, angle)

            polygonCoords = canvas.coords(self.__drawing)
            newCoords = []
            for i in range(0,len(polygonCoords),2):
                newX, newY = rotate((polygonCoords[i],polygonCoords[i+1]), centre, angle)
                newCoords.append(newX)
                newCoords.append(newY)
            canvas.coords(self.__drawing,newCoords)
        else:
            self.setCoordsAccordingToOrientation(centre[0], centre[1], orientation)
            newCoords = self.getDrawingPointsList(orientation)
            canvas.coords(self.__drawing,newCoords)
    
    def getVisionCoords(self):
        return self.__x0,self.__y0,self.__x1,self.__y1
    
    def doesVisionNeedReducing(self,orientation,canvas):
        if (orientation==Orientation.NORTH):
            canvasItems = list(canvas.find_overlapping(self.__x0+1,self.__y0,self.__x1-1,self.__y1))
        elif (orientation==Orientation.EAST):
            canvasItems = list(canvas.find_overlapping(self.__x0,self.__y0+1,self.__x1,self.__y1-1))
        elif (orientation==Orientation.SOUTH):
            canvasItems = list(canvas.find_overlapping(self.__x0-1,self.__y0,self.__x1+1,self.__y1))
        elif (orientation==Orientation.WEST):
            canvasItems = list(canvas.find_overlapping(self.__x0,self.__y0-1,self.__x1,self.__y1+1))

        if (len(canvasItems)==2):
            return False
        self.__isVisionReduced = True
        return True


    def setCoordsAccordingToOrientation(self,x,y,orientation):
        if (orientation==Orientation.NORTH):
            self.__x0 = x - characterSize
            self.__y0 = y - characterSize
            self.__x1 = x + characterSize
            self.__y1 = y - characterSize - Vision.visionSize
        elif (orientation==Orientation.EAST):
            self.__x0 = x + characterSize
            self.__y0 = y - characterSize
            self.__x1 = x + characterSize + Vision.visionSize
            self.__y1 = y + characterSize
        elif (orientation==Orientation.SOUTH):
            self.__x0 = x + characterSize
            self.__y0 = y + characterSize
            self.__x1 = x - characterSize
            self.__y1 = y + characterSize + Vision.visionSize
        elif (orientation==Orientation.WEST):
            self.__x0 = x - characterSize
            self.__y0 = y + characterSize
            self.__x1 = x - characterSize - Vision.visionSize
            self.__y1 = y - characterSize
        
        
    def getDrawingPointsList(self,orientation):
        if (orientation == Orientation.NORTH):
            return [
                self.__x0+characterSize/2,self.__y0,
                self.__x0,self.__y1,
                self.__x1,self.__y1,
                self.__x1-characterSize/2,self.__y0
            ]
        elif (orientation == Orientation.EAST):
            return [
                self.__x0,self.__y0+characterSize/2,
                self.__x1,self.__y0,
                self.__x1,self.__y1,
                self.__x0,self.__y1-characterSize/2
            ]
        elif (orientation == Orientation.SOUTH):
           return [
                self.__x0-characterSize/2,self.__y0,
                self.__x0,self.__y1,
                self.__x1,self.__y1,
                self.__x1+characterSize/2,self.__y0
            ]
        elif (orientation == Orientation.WEST):
            return [
                self.__x0,self.__y0-characterSize/2,
                self.__x1,self.__y0,
                self.__x1,self.__y1,
                self.__x0,self.__y1+characterSize/2
            ]

    def getDirectionOrientation(self,dx,dy):
        if (dy<0):
            return Orientation.NORTH
        elif (dx>0):
            return Orientation.EAST
        elif (dy>0):
            return Orientation.SOUTH
        elif (dx<0):
            return Orientation.WEST

    