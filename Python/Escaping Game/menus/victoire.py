import tkinter as tk
from other.utils import centrefenetre


class VictoryMenu(tk.Tk):

    def __init__(self,gameWindow):
        super().__init__()
        self.geometry("800x500")
        centrefenetre(self)
        self.title("Fin de niveau")
        self.resizable(width=False, height=False)
        
        Case_Titre = tk.Frame(self,borderwidth=10,relief=tk.GROOVE)
        Case_Titre.pack(side=tk.TOP, pady=50)
        Titre = tk.Label(Case_Titre,text="Vous avez gagné",font="Arial 24")
        Titre.pack()
        
        Frame_recommencer=tk.Frame(self,borderwidth=5, relief=tk.GROOVE)
        Frame_recommencer.pack(side=tk.TOP, pady=10)
        bouton_recommencer= tk.Button(Frame_recommencer, text="Réessayer", command=lambda window=gameWindow: self.retry(window))
        bouton_recommencer.pack()
        
        Frame_Next_Lvl=tk.Frame(self,borderwidth=5, relief=tk.GROOVE)
        Frame_Next_Lvl.pack(side=tk.TOP, pady=10)
        bouton_Next_Lvl= tk.Button(Frame_Next_Lvl, text="Niveau suivant", command=lambda window=gameWindow: self.tryNextLevel(window))
        bouton_Next_Lvl.pack()
        
        Frame_quit = tk.Frame(self, borderwidth=5, relief=tk.GROOVE)
        Frame_quit.pack(side=tk.TOP, pady=10)
        bouton_quit=tk.Button(Frame_quit, text="Retour au menu", command=lambda window=gameWindow: self.goBackToMainMenu(window))
        bouton_quit.pack()
        self.mainloop()

    def retry(self,window):
        self.destroy()
        window.reload()
    
    def goBackToMainMenu(self,window):
        self.destroy()
        window.goBackToMainMenu()

    def tryNextLevel(self,window):
        self.destroy()
        window.loadNextLevel()