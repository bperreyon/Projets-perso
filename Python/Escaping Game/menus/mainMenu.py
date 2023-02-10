import tkinter as tk
from other.utils import centrefenetre
from other.constants import gameName
from .levelMenu import LevelMenu

class MainMenu(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        centrefenetre(self)
        self.title(gameName+" - Menu principal")
        self.resizable(width=False, height=False)
        
        Case_Titre = tk.Frame(self,borderwidth=10,relief=tk.GROOVE)
        Case_Titre.pack(side=tk.TOP, pady=50)
        Titre = tk.Label(Case_Titre,text=gameName.upper(),font="Arial 32")
        Titre.pack()
        
        Frame_jeu=tk.Frame(self,borderwidth=5, relief=tk.GROOVE)
        Frame_jeu.pack(side=tk.TOP, pady=10)
        bouton_jeu= tk.Button(Frame_jeu, text="Nouvelle partie", command= self.newGame)
        bouton_jeu.pack()
        
        Frame_info=tk.Frame(self,borderwidth=5, relief=tk.GROOVE)
        Frame_info.pack(side=tk.TOP, pady=10)
        bouton_info= tk.Button(Frame_info, text="A propos", command=self.info)
        bouton_info.pack()
        
        Frame_quit = tk.Frame(self, borderwidth=5, relief=tk.GROOVE)
        Frame_quit.pack(side=tk.TOP, pady=10)
        bouton_quit=tk.Button(Frame_quit, text="Quitter", command=self.destroy)
        bouton_quit.pack()
        
        self.mainloop()
    

    def info(self):
        print("Jeu créé par moi")
        print("Musique : Land Below Fire Emblem Fates OST")
    

    def newGame(self):
        self.destroy()
        newWindow = LevelMenu(self)
    
    def reload(self):
        self.__init__()

    
