from other.constants import characterSize,LaserDirection,Orientation,gateThickness

class Mur:
    def __init__(self,x,y,Lx,Ly,canvas):
        self.__x0 = x
        self.__y0 = y
        self.__x1 = x + Lx
        self.__y1 = y + Ly

        self.__drawing = canvas.create_rectangle(x,y,x+Lx,y+Ly,fill="black")

    def getCoord(self):
        return self.__x0,self.__y0,self.__x1,self.__y1

class Objectif:
    def __init__(self,x,y,canvas):
        self.__x=x
        self.__y=y
        self.__drawing = canvas.create_rectangle(x-characterSize,y-characterSize,x+characterSize,y+characterSize,fill="yellow")
    
    def getCoord(self):
        return self.__x,self.__y


class Laser:
    def __init__(self,x0,y0,x1,y1,direction,canvas,speed=0,path=[],phaseAller=0):
        if (direction==LaserDirection.FIX and (speed!=0 or len(path)!=0 or phaseAller!=0)):
            return
        if (direction==LaserDirection.HORIZONTAL and (speed==0 or len(path)==0 or phaseAller==0)):
            return
        if (direction==LaserDirection.VERTICAL and (speed==0 or len(path)==0 or phaseAller==0)):
            return

        self.__x0 = x0
        self.__y0 = y0
        self.__x1 = x1 
        self.__y1 = y1
        self.__direction = direction
        if (direction!=LaserDirection.FIX):
            self.__positionOne = path[0]
            self.__positionTwo = path[1]
            self.__speed = speed
            self.__phaseAller = phaseAller
        self.__drawing  = canvas.create_line(self.__x0,self.__y0,self.__x1,self.__y1,fill="red")

    def move(self,canvas):
        if (self.__direction==LaserDirection.VERTICAL):
            if (self.__phaseAller):
                self.__y0 += self.__speed 
                self.__y1 += self.__speed
                canvas.move(self.__drawing,0,self.__speed)
                if (self.__y0>=self.__positionTwo[1]):
                    self.__phaseAller = False
            else:
                self.__y0 -= self.__speed 
                self.__y1 -= self.__speed
                canvas.move(self.__drawing,0,-self.__speed)
                if (self.__y0<=self.__positionOne[1]):
                    self.__phaseAller = True   
        elif (self.__direction==LaserDirection.HORIZONTAL):
            if (self.__phaseAller):
                self.__x0 += self.__speed 
                self.__x1 += self.__speed
                canvas.move(self.__drawing,self.__speed,0)
                if (self.__x0>=self.__positionTwo[0]):
                    self.__phaseAller = False
            else:
                self.__x0 -= self.__speed 
                self.__x1 -= self.__speed
                canvas.move(self.__drawing,-self.__speed,0)
                if (self.__x0<=self.__positionOne[0]):
                    self.__phaseAller = True
        else:
            pass

    def getCoord(self):
        return min(self.__x0,self.__x1),min(self.__y0,self.__y1),max(self.__x0,self.__x1),max(self.__y0,self.__y1)


class Teleporteur:

    def __init__(self,x0,y0,x1,y1,canvas):
        self.__x0 = x0
        self.__y0 = y0
        self.__x1 = x1
        self.__y1 = y1
        self.__drawing = canvas.create_rectangle(x0-characterSize,y0-characterSize,x0+characterSize,y0+characterSize,fill='green')

    
    def animTeleport(self,perso,canvas):
        deltaT=[250,500,600,700,800,900,950]
        L1=[self.__x0-characterSize,self.__y0-characterSize,self.__x0+characterSize,self.__y0+characterSize]
        L2=[self.__x0-characterSize/2,self.__y0-characterSize/2,self.__x0+characterSize/2,self.__y0+characterSize/2]
        for i in range (len(deltaT)):
            if i%2==0:
                canvas.after(deltaT[i], lambda cible=perso, canvas=canvas, coord=L2 : self.warp(cible, canvas, coord))
            else:
                canvas.after(deltaT[i], lambda cible=perso, canvas=canvas, coord=L1 : self.warp(cible, canvas, coord))
            
        deltaT2 = [1000,1050,1100,1200,1300,1400,1500]
        L1bis=[self.__x1-characterSize,self.__y1-characterSize,self.__x1+characterSize,self.__y1+characterSize]
        L2bis=[self.__x1-characterSize/2,self.__y1-characterSize/2,self.__x1+characterSize/2,self.__y1+characterSize/2]
        for i in range (len(deltaT2)):
            if i%2==0:
                canvas.after(deltaT2[i], lambda cible=perso, canvas=canvas, coord=L1bis : self.warp(cible, canvas, coord))
            else:
                canvas.after(deltaT2[i], lambda cible=perso, canvas=canvas, coord=L2bis : self.warp(cible, canvas, coord))
        
        perso.setCoords(self.__x1,self.__y1)

    def warp(self,perso,canvas,coords):
        perso.setCoords((coords[0]+coords[2])/2,(coords[1]+coords[3])/2)
        canvas.coords(perso.getDrawing(),coords)
    
    def getCoord(self):
        return self.__x0,self.__y0


class Objet:
    def __init__(self,x,y,canvas):
        self._x = x
        self._y = y
        self._drawing = canvas.create_rectangle(x-characterSize,y-characterSize,x+characterSize,y+characterSize,fill="brown")

    def getCoord(self):
        return self._x,self._y
    
    
    def use(self):
        print("Object used")
    
    def getType(self):
        return self._objectType
    
    def getDrawing(self):
        return self._drawing

class Cle(Objet):

    def __init__(self,x,y,canvas):
        super().__init__(x, y,canvas)
        self._objectType = "Key"
    
    def use(self,canvas):
        canvas.addKeyToThief()

class TimeSlower(Objet):

    def __init__(self,x,y,canvas):
        super().__init__(x, y,canvas)
        self._objectType = "TimeSlower"
    
    def use(self,canvas):
        canvas.addTimeSlowerToThief()

class Alarm(Objet):

    def __init__(self,x,y,canvas):
        super().__init__(x, y,canvas)
        self._objectType = "Alarm"
    
    def use(self,canvas):
        canvas.ringAlarm()

class Gate:
    
    def __init__(self,x,y,longueur,orientation,canvas):
        self.__orientation = orientation
        self.__x0 = x
        self.__y0 = y
        if (orientation==Orientation.NORTH or orientation==Orientation.SOUTH):
            self.__x1 = x + longueur
            self.__y1 = y + gateThickness
        elif (orientation==Orientation.EAST or orientation==Orientation.WEST):
            self.__x1 = x + gateThickness
            self.__y1 = y + longueur
        self.__drawing = canvas.create_rectangle(self.__x0,self.__y0,self.__x1,self.__y1,fill='brown')

    def getCoord(self):
        return self.__x0,self.__y0,self.__x1,self.__y1
    
    def getOrientation(self):
        return self.__orientation
    
    def getDrawing(self):
        return self.__drawing


