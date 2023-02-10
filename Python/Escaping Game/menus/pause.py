import tkinter as tk
from other.utils import centrefenetre
from other.constants import gameName

class MenuPause(tk.Tk):

    def __init__(self,gameWindow):
        super().__init__()
        self.geometry("800x500")
        centrefenetre(self)
        self.title(gameName+" - Pause")
        self.resizable(width=False, height=False)

        Case_Titre = tk.Frame(self,borderwidth=10,relief=tk.GROOVE)
        Case_Titre.pack(side=tk.TOP, pady=50)
        Titre = tk.Label(Case_Titre,text="Pause",font="Arial 24")
        Titre.pack()
        
        Frame_reprendre=tk.Frame(self,borderwidth=5, relief=tk.GROOVE)
        Frame_reprendre.pack(side=tk.TOP, pady=10)
        bouton_reprendre= tk.Button(Frame_reprendre, text="Reprendre", command= lambda fen=gameWindow : self.reprendre(fen))
        bouton_reprendre.pack()
        
        Frame_recommencer=tk.Frame(self,borderwidth=5, relief=tk.GROOVE)
        Frame_recommencer.pack(side=tk.TOP, pady=10)
        bouton_recommencer= tk.Button(Frame_recommencer, text="Recommencer", command=lambda fen=gameWindow : self.recommencer(fen))
        bouton_recommencer.pack()
        
        Frame_quit = tk.Frame(self, borderwidth=5, relief=tk.GROOVE)
        Frame_quit.pack(side=tk.TOP, pady=10)
        bouton_quit=tk.Button(Frame_quit, text="Retour au menu", command=lambda fen=gameWindow : self.quitter(fen))
        bouton_quit.pack()
        self.mainloop()
    

    def reprendre(self,gameWindow):
        gameWindow.canvas.setPlay(True)
        gameWindow.updateWindow()
        self.destroy()
    
    def recommencer(self,gameWindow):
        self.destroy()
        gameWindow.reload()

    
    def quitter(self,gameWindow):
        self.destroy()
        gameWindow.goBackToMainMenu()
        
