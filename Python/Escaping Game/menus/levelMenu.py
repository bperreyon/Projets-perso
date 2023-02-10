import tkinter as tk
from other.utils import centrefenetre
from other.constants import gameName
from .fenetreJeu import GameWindow


class LevelMenu(tk.Tk):

    levelAvailable = 1

    def __init__(self,mainMenu):
        super().__init__()
        self.geometry("800x500")
        centrefenetre(self)
        self.title(gameName+" - Menu des niveaux")
        self.resizable(width=False, height=False)

        Case_Titre = tk.Frame(self,borderwidth=10,relief=tk.GROOVE)
        Case_Titre.pack(side=tk.TOP,fill=tk.X)
        Titre = tk.Label(Case_Titre,text="Choisissez un niveau",font="Arial 24")
        Titre.pack()

        levelFrame = tk.Frame(self,borderwidth=5,relief=tk.GROOVE)
        levelFrame.pack(side=tk.TOP,fill=tk.BOTH,pady=50,ipady=50)

        for i in range (LevelMenu.levelAvailable):
            Bouton_Lvl = tk.Button(levelFrame,text="Lvl "+str(i+1),command=lambda level=i+1,menu=mainMenu: self.startLevel(level,menu))
            Bouton_Lvl.grid(column=i%8,row=100+(i//8)*10,padx=24,pady=10)
        
        Frame_quit = tk.Frame(self, borderwidth=5, relief=tk.GROOVE)
        Frame_quit.pack(side=tk.BOTTOM)
        bouton_quit=tk.Button(Frame_quit, text="Retour au menu", command=lambda menu=mainMenu : self.goBackToMainMenu(menu))
        bouton_quit.pack()
        self.mainloop()
    
    def startLevel(self,level,menu):
        self.destroy()
        newWindow = GameWindow(level,menu)

    def goBackToMainMenu(self,menu):
        self.destroy()
        menu.reload()
    
        