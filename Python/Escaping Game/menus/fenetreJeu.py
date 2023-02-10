import tkinter as tk

from maps.canvas import GameCanvas
from other.constants import refreshFrameTime
from .pause import MenuPause
from .defaite import GameOverMenu
from .victoire import VictoryMenu

class GameWindow(tk.Tk):

    def __init__(self,niveau,menu):
        super().__init__()
        #self.attributes('-fullscreen',True)

        self.timeSinceBeginning = 0
        self.timeDisplayed =tk.StringVar()
        self.timeDisplayed.set(str(self.timeSinceBeginning/1000))
        self.numberOfKeys = 0
        self.numberOfKeysDisplayed = tk.StringVar()
        self.numberOfKeysDisplayed.set("Vous avez 0 clé")
        self.numberOfTimeSlowers = 0
        self.numberOfTimeSlowersDisplayed = tk.StringVar()
        self.numberOfTimeSlowersDisplayed.set("Vous avez 0 déphaseur temporel")
        self.level = niveau
        self.mainMenu = menu

        logFrame = tk.Frame(self)
        logFrame.pack(side=tk.RIGHT,fill=tk.Y)
        
        timeFrame = tk.Frame(logFrame,borderwidth=2, relief=tk.GROOVE)
        timeFrame.pack(side=tk.TOP,fill=tk.X)
        tk.Label(timeFrame,text="Temps écoulé",font="Arial 14").pack()
        tk.Label(timeFrame,textvariable=self.timeDisplayed).pack()
        
        
        inventoryFrame = tk.Frame(logFrame,borderwidth=2, relief=tk.GROOVE)
        inventoryFrame.pack(side=tk.TOP,fill=tk.X)
        tk.Label(inventoryFrame,text="Inventaire",font="Arial 14").pack()
        tk.Label(inventoryFrame,textvariable=self.numberOfKeysDisplayed).pack()
        tk.Label(inventoryFrame,textvariable=self.numberOfTimeSlowersDisplayed).pack()
        

        eventRecorder = tk.Frame(logFrame,borderwidth=2, relief=tk.GROOVE)
        eventRecorder.pack(side=tk.BOTTOM,fill=tk.X,ipady=100)
        tk.Label(eventRecorder,text="Rapport des évènements \n",font="Arial 14").pack()
        firstEvent = tk.Label(eventRecorder,text="Cliquez sur la fenêtre avant de jouer")
        firstEvent.pack()
  
        canvas = GameCanvas(self,niveau)

        canvas.pack(expand=1)

        self.canvas = canvas
        self.eventRecorder= eventRecorder
        self.eventInfo=[firstEvent]

        self.updateWindow()
        self.mainloop()
    
    def updateWindow(self):
        if (self.canvas.hasWon()):
            self.after(2000,lambda window=self: VictoryMenu(window))
        elif (self.canvas.hasLost()):
            self.after(2000,lambda window=self: GameOverMenu(window))
        elif (not self.canvas.doesPlay()):
            MenuPause(self)
        else:
            self.canvas.updateCanvas()
            self.timeSinceBeginning += refreshFrameTime
            self.timeDisplayed.set(str(self.timeSinceBeginning/1000))
            keyVariation = self.canvas.getKeyVariation()
            if (keyVariation!=0):
                self.addEventToRecorder(self.createInventoryVariationText('clé',keyVariation))
                self.numberOfKeys += keyVariation
                self.numberOfKeysDisplayed.set('Vous avez '+str(self.numberOfKeys)+' clé(s)')
                self.canvas.resetKeyVariation()
            timeSlowerVariation = self.canvas.getTimeSlowerVariation()
            if (timeSlowerVariation!=0):
                self.addEventToRecorder(self.createInventoryVariationText('déphaseur temporel',timeSlowerVariation))
                self.numberOfTimeSlowers += timeSlowerVariation
                self.numberOfTimeSlowersDisplayed.set('Vous avez '+str(self.numberOfTimeSlowers)+' déphaseur(s) temporels')
                self.canvas.resetTimeSlowerVariation()
            if (self.canvas.didAlarmJustRing()):
                self.addEventToRecorder("L'alarme retentit")
            if (self.canvas.isTimeSlowed()):
                self.after(refreshFrameTime*2,self.updateWindow)
            else:
                self.after(refreshFrameTime,self.updateWindow)


    def reload(self):
        self.destroy()
        self.__init__(self.level,self.mainMenu)
    
    def loadNextLevel(self):
        self.destroy()
        self.__init__(self.level+1,self.mainMenu)

    def goBackToMainMenu(self):
        self.destroy()
        self.mainMenu.reload()

    def addEventToRecorder(self,text):
        label = tk.Label(self.eventRecorder,text=text)
        if (len(self.eventInfo)<6):
            currentIPadY = self.eventRecorder.pack_info()['ipady']
            self.eventRecorder.pack(side=tk.BOTTOM,fill=tk.X,ipady=currentIPadY-10)
            label.pack()
            self.eventInfo.append(label)
        else:
            self.eventRecorder.winfo_children()[1].destroy()
            for eventRecord in self.eventRecorder.winfo_children():
                eventRecord.pack()
            label.pack()
            self.eventInfo.pop(0)
            self.eventInfo.append(label)
    

    def createInventoryVariationText(self,inventoryField,variation):
        if (variation==1):
            return 'Vous avez trouvé un(e) {} !'.format(inventoryField)
        elif (variation==-1):
            return 'Vous utilisez un(e) {}.'.format(inventoryField)