import tkinter as tk

from other.utils import isBetween
from other.constants import mapHeight, mapWidth, characterSize, alarmDuration, refreshFrameTime,Orientation,GuardType,LaserDirection,WarperSens,timeSlowDuration
from .gameElements import *
from .config import *



class GameCanvas(tk.Canvas):

    def __init__(self,parent,niveau):
        super().__init__(parent,width=mapWidth, height=mapHeight, bg="ivory",highlightthickness=False)
        self.__guards = []
        self.__walls = []
        self.__lasers = []
        self.__warpers = []
        self.__objects = []
        self.__gates = []

        self.__isAlarmeActive = False
        self.__alarmTime = 0
        self.__animationInProcess = False
        self.__keyVariation = 0
        self.__isTimeSlowed = False
        self.__timeSlowCurrentDuration = 0
        self.__timeSlowerVariation = 0

        self.__play = True
        self.__win = False
        self.__lose = False
        

        self.focus_set()
        self.bind("<Key>",self.clavier)
        eval("map"+str(niveau)+".createMap")(self)

    ## Canvas creation
    def createThief(self,xLocation,yLocation,orientation):
        self.__thief = voleur.Voleur(xLocation,yLocation,orientation,self)

    def createGuard(self,guard):
        if (guard['type']==GuardType.MOBIL):
            newGuard = garde.Garde(guard['x'],guard['y'],guard['orientation'],guard['type'],self,guard["path"],guard["speed"])
        elif (guard['type']==GuardType.ROTATER):
            newGuard = garde.Garde(guard['x'],guard['y'],guard['orientation'],guard['type'],self,guard["path"],guard["speed"],guard['reverse'])
        elif (guard['type']==GuardType.FIX):
            newGuard = garde.Garde(guard['x'],guard['y'],guard['orientation'],guard['type'],self)
        self.__guards.append(newGuard)

    def createWall(self,wall):
        newWall = objets.Mur(wall["x"],wall["y"],wall["Lx"],wall["Ly"],self)
        self.__walls.append(newWall)

    def createObjective(self,xLocation,yLocation):
        self.__objective = objets.Objectif(xLocation, yLocation, self)

    def createLaser(self,laser):
        if (laser["direction"]==LaserDirection.HORIZONTAL or laser["direction"]==LaserDirection.VERTICAL):
            newLaser = objets.Laser(laser["x0"],laser["y0"],laser["x1"],laser["y1"],laser["direction"],self,laser["speed"],laser["path"],laser["phaseAller"])
        elif (laser["direction"]==LaserDirection.FIX):
            newLaser = objets.Laser(laser["x0"],laser["y0"],laser["x1"],laser["y1"],laser["direction"],self)
        self.__lasers.append(newLaser)

    def createWarper(self,warper):
        if (warper['sens']==WarperSens.BOTH):
            newWarper1 = objets.Teleporteur(warper['x0'],warper['y0'],warper['x1'],warper['y1'],self)
            newWarper2 = objets.Teleporteur(warper['x1'],warper['y1'],warper['x0'],warper['y0'],self)
            self.__warpers.append(newWarper1)
            self.__warpers.append(newWarper2)
        elif (warper['sens']==WarperSens.UNIC):
            newWarper = objets.Teleporteur(warper['x0'],warper['y0'],warper['x1'],warper['y1'],self)
            self.__warpers.append(newWarper)

    def createKey(self,key):
        newKey = objets.Cle(key['x'],key['y'],self)
        self.__objects.append(newKey)

    def createGate(self,gate):
        newGate = objets.Gate(gate['x'],gate['y'],gate['longueur'],gate['orientation'],self)
        self.__gates.append(newGate)

    def createTimeSlower(self,timeSlower):
        newTimeSlower = objets.TimeSlower(timeSlower['x'],timeSlower['y'],self)
        self.__objects.append(newTimeSlower)

    def createAlarm(self,alarm):
        newAlarm = objets.Alarm(alarm['x'],alarm['y'],self)
        self.__objects.append((newAlarm))

    ## Getter and setter
    def getWalls(self):
        return self.__walls
    
    def getObjects(self):
        return self.__objects
    
    def getGates(self):
        return self.__gates

    def doesPlay(self):
        return self.__play
    
    def setPlay(self,boolean):
        self.__play = boolean
    
    def hasWon(self):
        return self.__win
    
    def hasLost(self):
        return self.__lose

    def getKeyVariation(self):
        return self.__keyVariation
    
    def resetKeyVariation(self):
        self.__keyVariation = 0
    
    def getTimeSlowerVariation(self):
        return self.__timeSlowerVariation
    
    def resetTimeSlowerVariation(self):
        self.__timeSlowerVariation = 0

    def isTimeSlowed(self):
        return self.__isTimeSlowed
    
    def didAlarmJustRing(self):
        return self.__isAlarmeActive and self.__alarmTime<2*refreshFrameTime

    def getThiefDrawing(self):
        return self.__thief.getDrawing()

    ## Permanent jobs
    def updateCanvas(self):
        if (self.__play):
            if (self.__isAlarmeActive):
                for guard in self.__guards:
                    guard.move(self)
                self.__alarmTime += refreshFrameTime
                if (self.__alarmTime>=alarmDuration):
                    self.__alarmTime=0
                    self.__isAlarmeActive= False
            if (self.__isTimeSlowed):
                self.__timeSlowCurrentDuration += refreshFrameTime
                if (self.__timeSlowCurrentDuration>timeSlowDuration/2):
                    self.__isTimeSlowed = False
                    self.__timeSlowCurrentDuration = 0
            for guard in self.__guards:
                guard.move(self)
            for laser in self.__lasers:
                laser.move(self)
            self.isThiefSeen()
            self.isThiefDetected()

    def clavier(self,event):
        if (self.__play and not self.__animationInProcess):
            touche = event.keysym
            if touche == "z" or touche == "s" or touche == "d" or touche == "q":
                self.__thief.move(self,touche)
            if touche=="l":
                print(self.__thief.getCenterCoord())
                print(self.__thief.getBorderCoord())
                print("-- STOP --")
            if (touche=="Escape"):
                self.pause()
            if (touche=="Return"):
                self.isObjectClose()
                self.isGateClose()
            if (touche=="t"):
                self.useTimeSlower()
            if (touche =="m"):
                for guard in self.__guards:
                    guard.move(self)
        else:
            touche= event.keysym
            if (touche=="p"):
                self.__play=True
    
    ## Gameplay method
    def isThiefSeen(self):
        thiefCoords = self.__thief.getBorderCoord()
        i=0
        detected = False
        while i<len(self.__guards) and not detected:
            xMin,yMin,xMax,yMax = self.__guards[i].getVison()
            for coord in thiefCoords:
                if (isBetween(coord[0],xMin,xMax) and isBetween(coord[1],yMin,yMax)):
                    detected=True
            i += 1
        if (detected):
            self.gameOver()

    def isThiefOnObjective(self):
       if (self.__thief.getCenterCoord()==self.__objective.getCoord()):
            self.victory()
    
    def isThiefDetected(self):
        if(not self.__isAlarmeActive):
            x,y = self.__thief.getCenterCoord()
            i=0
            detected = False
            while i<len(self.__lasers) and not detected:
                xMin,yMin,xMax,yMax = self.__lasers[i].getCoord()
                # @debt : manage all lasers
                if (xMin==xMax):
                    if ((isBetween(y+characterSize, yMin, yMax) and isBetween(xMin, x-characterSize, x+characterSize)) or (isBetween(y-characterSize, yMin, yMax) and isBetween(xMin, x-characterSize, x+characterSize))):
                        detected=True
                elif (yMin==yMax):
                    if ((isBetween(x-characterSize, xMin, xMax) and isBetween(yMin, y-characterSize, y+characterSize)) or (isBetween(x+characterSize, xMin, xMax) and isBetween(yMin, y-characterSize, y+characterSize))):
                        detected=True
                i+=1
            if (detected):
                self.ringAlarm()
    
    def isThiefOnWarper(self):
        
        xThief,yThief = self.__thief.getCenterCoord()
        i=0
        onWarper = False
        while i<len(self.__warpers) and not onWarper:
            xWarper,yWarper = self.__warpers[i].getCoord()
            if ((xThief==xWarper) and (yThief==yWarper)):
                onWarper = True
            i+=1
        if (onWarper):
            self.__animationInProcess = True
            self.__warpers[i-1].animTeleport(self.__thief,self)
            self.__animationInProcess = False

    def isObjectClose(self):
        xThief, yThief = self.__thief.getCenterCoord()
        thiefOrientation = self.__thief.getOrientation()
        if (thiefOrientation==Orientation.NORTH):
            xLooked = xThief
            yLooked = yThief - 2*characterSize
        elif (thiefOrientation==Orientation.EAST):
            xLooked = xThief + 2*characterSize
            yLooked = yThief
        elif (thiefOrientation==Orientation.SOUTH):
            xLooked = xThief
            yLooked = yThief + 2*characterSize
        elif (thiefOrientation==Orientation.WEST):
            xLooked = xThief - 2*characterSize
            yLooked = yThief
        i=0
        objectFound = False
        while (i<len(self.__objects) and not objectFound):
            xObject, yObject = self.__objects[i].getCoord()
            if ((xLooked==xObject) and (yLooked==yObject)):
                objectFound = True
            i+=1
        if (objectFound):
            obj = self.__objects.pop(i-1)
            obj.use(self)
            self.delete(obj.getDrawing())

    def isGateClose(self):
        if (self.__thief.hasItem('key')):
            xThief, yThief = self.__thief.getCenterCoord()
            thiefOrientation = self.__thief.getOrientation()
            i=0
            gateClose = False
            while (i<len(self.__gates) and not gateClose):
                x0,y0,x1,y1 = self.__gates[i].getCoord()
                if (thiefOrientation==Orientation.NORTH):
                    if ((yThief-characterSize==y1)and(isBetween(xThief, x0, x1))):
                        gateClose = True
                elif (thiefOrientation==Orientation.EAST):
                    if ((xThief+characterSize==x0) and (isBetween(yThief, y0, y1))):
                        gateClose = True
                elif (thiefOrientation==Orientation.SOUTH):
                    if ((yThief+characterSize==y0) and (isBetween(xThief, x0, x1))):
                        gateClose = True
                elif (thiefOrientation==Orientation.WEST):
                    if ((xThief-characterSize==x1) and (isBetween(yThief, y0, y1))):
                        gateClose = True
                i+=1
            if (gateClose):
                self.removeKeyToThief()
                gate = self.__gates.pop(i-1)
                self.delete(gate.getDrawing())

    def gameOver(self):
        self.__play = False
        self.__lose = True
        self.create_text(740,525,text="Game over",font="Arial 40",fill="Red")

    def victory(self):
        self.__play = False
        self.__win = True
        self.create_text(740,525,text="Niveau terminé !",font="Arial 40",fill="Red")
    
    def ringAlarm(self):
        self.__isAlarmeActive = True
        self.__alarmTime = 0

    def pause(self):
        self.__play = False

    def addKeyToThief(self):
        self.__thief.addItem('key')
        self.__keyVariation = 1
    
    def removeKeyToThief(self):
        self.__thief.removeItem('key')
        self.__keyVariation = -1
    
    def addTimeSlowerToThief(self):
        self.__thief.addItem('timeSlower')
        self.__timeSlowerVariation = 1

    def useTimeSlower(self):
        if (self.__thief.hasItem('timeSlower') and not self.__isTimeSlowed):
            self.__thief.removeItem('timeSlower')
            self.__isTimeSlowed = True
            self.__timeSlowCurrentDuration = 0
            self.__timeSlowerVariation = -1
        