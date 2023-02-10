# -*- coding: utf-8 -*-
"""
Input nom de jeu
"""

import tkinter as tk
import numpy as n
import pygame as p
import pygame.mixer as pm
import pygame.mixer_music as pmm

global Lmap
Lmap=[]
Map_dispo=10

# # Fonctions pour les menus # #
def Menu_principal():
    global Menu
    Menu = tk.Tk()
    Menu.geometry("800x500")
    centrefenetre(Menu)
    Menu.title("Nom du jeu - Menu principal")
    Menu.resizable(width=False, height=False)
    
    Case_Titre = tk.Frame(Menu,borderwidth=10,relief=tk.GROOVE)
    Case_Titre.pack(side=tk.TOP, pady=50)
    Titre = tk.Label(Case_Titre,text="Trouver un titre il faut",font="Arial 32")
    Titre.pack()
    
    Frame_jeu=tk.Frame(Menu,borderwidth=5, relief=tk.GROOVE)
    Frame_jeu.pack(side=tk.TOP, pady=10)
    bouton_jeu= tk.Button(Frame_jeu, text="Nouvelle partie", command= lambda fen=Menu,fonc=Newgame :chgmt_fen(fen,fonc))
    bouton_jeu.pack()
    
    Frame_info=tk.Frame(Menu,borderwidth=5, relief=tk.GROOVE)
    Frame_info.pack(side=tk.TOP, pady=10)
    bouton_info= tk.Button(Frame_info, text="A propos", command=Info)
    bouton_info.pack()
    
    Frame_quit = tk.Frame(Menu, borderwidth=5, relief=tk.GROOVE)
    Frame_quit.pack(side=tk.TOP, pady=10)
    bouton_quit=tk.Button(Frame_quit, text="Quitter", command=Menu.destroy)
    bouton_quit.pack()
    Menu.mainloop()

def Info():
    print("Jeu créé par moi")
    print("Musique : Land Below Fire Emblem Fates OST")

def Newgame():
    global Lmap
    Lmap=[]
    for i in range (Map_dispo):
        Lmap.append(eval("map"+str(i+1)))
    global Menu_Lvl
    Menu_Lvl= tk.Tk()
    Menu_Lvl.geometry("800x500")
    centrefenetre(Menu_Lvl)
    Menu_Lvl.title("Nom du jeu - Menu des niveaux")
    Menu_Lvl.resizable(width=False, height=False)

    Case_Titre = tk.Frame(Menu_Lvl,borderwidth=10,relief=tk.GROOVE)
    Case_Titre.grid(row=10,column=1,columnspan=8, pady=50) # Travailler sur le centrage
    Titre = tk.Label(Case_Titre,text="Choisissez un niveau",font="Arial 24")
    Titre.grid()
    for i in range (len(Lmap)):
        Case_niveau(i)
    
    Frame_quit = tk.Frame(Menu_Lvl, borderwidth=5, relief=tk.GROOVE)
    Frame_quit.grid(row=600,column=3,columnspan=3, pady=10)
    bouton_quit=tk.Button(Frame_quit, text="Retour au menu", command=lambda fen=Menu_Lvl,fonc=Menu_principal :chgmt_fen(fen,fonc))
    bouton_quit.grid()
    Menu_Lvl.mainloop()

def Case_niveau(i):
    global Lmap
    global Menu_Lvl
    Case_Lvl = tk.Frame(Menu_Lvl,borderwidth=5,relief=tk.GROOVE)
    Case_Lvl.grid(column=i%8,row=100+(i//8)*10,padx=24,pady=10)
    Bouton_Lvl = tk.Button(Case_Lvl,text="Lvl "+str(i+1),command=lambda fen=Menu_Lvl,fonc=Lmap[i] :chgmt_fen(fen,fonc))
    Bouton_Lvl.grid()
      
def Pause():
    global Play
    Play = False
    global Menu_pause
    Menu_pause=tk.Tk()
    Menu_pause.geometry("800x500")
    centrefenetre(Menu_pause)
    Menu_pause.title("Nom du jeu - Pause")
    Menu_pause.resizable(width=False, height=False)
    
    Case_Titre = tk.Frame(Menu_pause,borderwidth=10,relief=tk.GROOVE)
    Case_Titre.pack(side=tk.TOP, pady=50)
    Titre = tk.Label(Case_Titre,text="Pause",font="Arial 24")
    Titre.pack()
    
    Frame_reprendre=tk.Frame(Menu_pause,borderwidth=5, relief=tk.GROOVE)
    Frame_reprendre.pack(side=tk.TOP, pady=10)
    bouton_reprendre= tk.Button(Frame_reprendre, text="Reprendre", command=lambda fen=Menu_pause,fonc=reprendre :chgmt_fen(fen,fonc))
    bouton_reprendre.pack()
    
    Frame_recommencer=tk.Frame(Menu_pause,borderwidth=5, relief=tk.GROOVE)
    Frame_recommencer.pack(side=tk.TOP, pady=10)
    bouton_recommencer= tk.Button(Frame_recommencer, text="Recommencer", command=lambda fen=Menu_pause,fonc=recommencer :chgmt_fen(fen,fonc))
    bouton_recommencer.pack()
    
    Frame_quit = tk.Frame(Menu_pause, borderwidth=5, relief=tk.GROOVE)
    Frame_quit.pack(side=tk.TOP, pady=10)
    bouton_quit=tk.Button(Frame_quit, text="Retour au menu", command=lambda fen=Menu_pause,fonc=quitter :chgmt_fen(fen,fonc))
    bouton_quit.pack()
    Menu_pause.mainloop()

def reprendre():
    global Play
    Play=True
    Mouvement_adverse()

def recommencer():
    global fenetre
    fenetre.destroy()
    eval("map"+str(Niveau))()  
    
def quitter():
    global fenetre
    pmm.stop()
    fenetre.destroy()
    Menu_principal()

def fenGO():
    global GO
    GO = tk.Tk()
    GO.geometry("800x500")
    centrefenetre(GO)
    GO.title("Game Over")
    GO.resizable(width=False, height=False)
    
    Case_Titre = tk.Frame(GO,borderwidth=10,relief=tk.GROOVE)
    Case_Titre.pack(side=tk.TOP, pady=50)
    Titre = tk.Label(Case_Titre,text="Vous avez perdu",font="Arial 24")
    Titre.pack()
    
    Frame_recommencer=tk.Frame(GO,borderwidth=5, relief=tk.GROOVE)
    Frame_recommencer.pack(side=tk.TOP, pady=10)
    bouton_recommencer= tk.Button(Frame_recommencer, text="Réessayer", command=lambda fen=GO,fonc=recommencer :chgmt_fen(fen,fonc))
    bouton_recommencer.pack()
    
    Frame_quit = tk.Frame(GO, borderwidth=5, relief=tk.GROOVE)
    Frame_quit.pack(side=tk.TOP, pady=10)
    bouton_quit=tk.Button(Frame_quit, text="Retour au menu", command=lambda fen=GO,fonc=quitter :chgmt_fen(fen,fonc))
    bouton_quit.pack()
    GO.mainloop()

def fenW():
    global W
    W = tk.Tk()
    W.geometry("800x500")
    centrefenetre(W)
    W.title("Fin de niveau")
    W.resizable(width=False, height=False)
    
    Case_Titre = tk.Frame(W,borderwidth=10,relief=tk.GROOVE)
    Case_Titre.pack(side=tk.TOP, pady=50)
    Titre = tk.Label(Case_Titre,text="Vous avez gagné",font="Arial 24")
    Titre.pack()
    
    Frame_recommencer=tk.Frame(W,borderwidth=5, relief=tk.GROOVE)
    Frame_recommencer.pack(side=tk.TOP, pady=10)
    bouton_recommencer= tk.Button(Frame_recommencer, text="Réessayer", command=lambda fen=W,fonc=recommencer :chgmt_fen(fen,fonc))
    bouton_recommencer.pack()
    
    Frame_Next_Lvl=tk.Frame(W,borderwidth=5, relief=tk.GROOVE)
    Frame_Next_Lvl.pack(side=tk.TOP, pady=10)
    bouton_Next_Lvl= tk.Button(Frame_Next_Lvl, text="Niveau suivant", command=lambda fen=W,fonc=Next_Lvl :chgmt_fen(fen,fonc))
    bouton_Next_Lvl.pack()
    
    Frame_quit = tk.Frame(W, borderwidth=5, relief=tk.GROOVE)
    Frame_quit.pack(side=tk.TOP, pady=10)
    bouton_quit=tk.Button(Frame_quit, text="Retour au menu", command=lambda fen=W,fonc=quitter :chgmt_fen(fen,fonc))
    bouton_quit.pack()
    W.mainloop()

def Next_Lvl():
    global fenetre
    fenetre.destroy()
    global Niveau
    eval("map"+str(Niveau+1))()

def geoliste(g):
    r=[i for i in range(0,len(g)) if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

def centrefenetre(fen):
    fen.update_idletasks()
    l,h,x,y=geoliste(fen.geometry())
    fen.geometry("%dx%d%+d%+d" % (l,h,(fen.winfo_screenwidth()-l)//2,(fen.winfo_screenheight()-h)//2))

def chgmt_fen(fen,fonc):
    fen.destroy()
    fonc()

# # Création des map # #

def create_map():
    print("createMap")
    global Zone_interdite
    Zone_interdite=[]
    global Info_garde
    Info_garde=[]
    global Vision
    Vision=[]
    global Objet
    Objet=[]
    global Teleporteur
    Teleporteur=[]
#    global Porte
#    Porte=[]
    global Laser
    Laser=[]
    global Inventaire
    Inventaire=[0]
    global Play
    Play = True
    global Tps_mvt
    Tps_mvt=100
    global Alarme_active
    Alarme_active=False
    global Temps_ralentit
    Temps_ralentit=False
    global testp
    testp=0
    
    global fenetre
    fenetre = tk.Tk()
    fenetre.attributes('-fullscreen',True )
    global Event
    Event=tk.Frame(fenetre,borderwidth=2, relief=tk.GROOVE,width=269,height=244)
    Event.pack_propagate(False)
    Event.pack(side=tk.LEFT)
    label=tk.Label(Event,text="Rapport des évènements \n",font="Arial 14")
    label.pack()
    tk.Label(Event,text="Cliquez sur la fenêtre avant de jouer").pack()
    global Info
    Info=[]
    global Tps_ecoule
    Tps_ecoule=0
    Tps_Score=tk.Frame(fenetre)
    Tps_Score.pack(side=tk.RIGHT)
    label2=tk.Label(Tps_Score,text="                       \n",font="Arial 14")
    label2.pack()
    global Aff_Temps
    Aff_Temps=tk.StringVar()
    Aff_Temps.set("Temps : "+str(Tps_ecoule/1000))
    label1=tk.Label(Tps_Score,textvariable=Aff_Temps)
    label1.pack()
    global Aff_cle
    Aff_cle=tk.StringVar()
    Aff_cle.set("Vous avez "+str(Inventaire[0])+" clé(s)")
    label3=tk.Label(Tps_Score,textvariable=Aff_cle)
    label3.pack()
    # création du canvas
    global canvas
    canvas = tk.Canvas(fenetre, width=Longueur_map, height=Largeur_map, bg="ivory",highlightthickness=False)
    p.init()
    pmm.load("MusiqueBG.wav")
    pmm.play(-1)
    global Son_alarme
    Son_alarme=pm.Sound("Alarme.wav")
    
def map1():
    print("map1")
    global Niveau
    Niveau=1
    create_map()
    



    # # Murs # #
    obstacle(150,160,80,70)
    obstacle(260,110,60,160)
    obstacle(50,110,70,160)
    obstacle(120,50,150,80)
    obstacle(120,270,150,30)
    obstacle(340,330,40,30)
    obstacle(500,440,30,40)
    obstacle(440,490,40,40)
    obstacle(550,490,30,40)
    obstacle(480,550,60,30)
    obstacle(350,510,30,30)
    obstacle(900,440,300,60)
    obstacle(1020,300,60,300)
    # # Objets # #
    Creation_alarme(120,800)
    Cle(260,800)
    Portail(400,770,60,"v")
    Portail(900,800,60,"h")
    TimeSlower(600,800)
    Plaque_tp(2,20,20,300,300)
    Plaque_tp(1,800,800,1200,800)
    # # Lasers alarme # #
    Creation_alarme2f(120,500,200,500)
    Creation_alarme2f(60,500,60,700)
    Creation_alarme2m("h",120,550,80,550,650,5)
    Creation_alarme2m("v",150,950,80,120,230,5)
    # # Objectif # #
    global objectif
    objectif = canvas.create_rectangle(1400,1000,1400+Taille_perso,1000+Taille_perso,fill="yellow")
    # # Personage # #
    global Perso
    Perso = canvas.create_rectangle(0,0,Taille_perso,Taille_perso,fill="violet")
    
    # # Gardes # #

    Creation_garde(350,200,420,300,350,200,1,-10)
    Creation_garde(130,140,230,230,230,230,3,-5)   
    Creation_garde(730,140,800,200,730,140,1,5)  
    Creation_garde2(500,500,1,-500)   # OK
    Creation_garde2(1000,500,1,500)  #  35 gauche 
    Creation_garde2(1080,500,1,-500)  # 35 droite et bas
    Creation_garde2(1000,420,1,-500)  # OK
    Creation_garde2(1080,420,1,500)   # 35 haut
    # obstacle au dessus ou à gauche --> 35
    Creation_garde2(700,700,4,0)
    Creation_garde(400,500,400,700,400,500,1,-10)
    Creation_garde2(100,660,1,0)  
    Mouvement_adverse()

    canvas.focus_set()
    canvas.bind("<Key>", clavier)
    canvas.pack(expand=1)
    fenetre.mainloop()

def map2():
    global Niveau
    Niveau=2
    create_map()
    
    # # Murs # #
    obstacle(0,0,1440,300)
    obstacle(0,300,210,360)
    obstacle(0,660,1440,390)
    obstacle(1250,300,210,360)
    obstacle(210,420,160,80)
    obstacle(520,300,160,200)
    obstacle(290,540,120,80)
    obstacle(490,540,120,80)
    obstacle(850,420,120,240)
    obstacle(970,300,120,40)
    # # Objectif # #
    global objectif
    objectif = canvas.create_rectangle(1090,630,1090+Taille_perso,630+Taille_perso,fill="yellow")
    # # Personage # #
    global Perso
    Perso = canvas.create_rectangle(250,350,250+Taille_perso,350+Taille_perso,fill="violet")
    # # Guardes # # 
    Creation_garde(380,460,490,460,380,460,1,5)
    Creation_garde(270,520,410,620,270,520,1,-5)
    Creation_garde(470,520,610,620,470,520,1,5)
    Creation_garde(750,510,750,630,750,510,1,5)
    Creation_garde2(680,480,1,500)
    Creation_garde2(830,480,3,500)
    Creation_garde2(750,350,2,0)
    Creation_garde2(980,640,4,0)
    Creation_garde2(1220,640,4,0)
    Creation_garde(1000,380,1080,500,1000,380,1,5)
    Creation_garde(1080,380,1200,460,1200,460,3,-5)
    Creation_garde(1000,500,1120,580,1080,500,1,-5)
    Creation_garde(1120,460,1200,580,1120,580,3,5)
    Mouvement_adverse()
    
    canvas.focus_set()
    canvas.bind("<Key>", clavier)
    canvas.pack(expand=1)
    fenetre.mainloop()

def map3():
    global Niveau
    Niveau=3
    create_map()
    
    # # Murs # #
    obstacle(100,0,120,350)
    obstacle(220,0,1220,100)
    obstacle(0,430,220,90)
    obstacle(910,180,170,340)
    obstacle(1200,260,100,60)
    obstacle(1070,380,120,60)
    obstacle(1310,380,130,60)
    obstacle(0,520,1080,160)
    obstacle(1070,600,140,160)
    obstacle(1290,600,150,350)
    obstacle(1080,840,210,100)
    obstacle(430,670,80,80)
    obstacle(310,730,80,100)
    obstacle(310,830,200,100)
    obstacle(0,670,80,260)
    obstacle(0,930,1440,120)
    # # Objectif # #
    global objectif
    objectif = canvas.create_rectangle(180,800,180+Taille_perso,800+Taille_perso,fill="yellow")
    # # Perso # #
    global Perso
    Perso = canvas.create_rectangle(0,0,Taille_perso,Taille_perso,fill="violet")
    # # Guardes # #
    for i in range (6):
        for j in range (4):
            Creation_garde2(260+120*i,120+120*j,2-(-1)**(i+j),500) 
    Creation_garde(1080,190,1200,190,1080,190,1,5)
    Creation_garde(1300,190,1420,190,1420,190,1,5)
    Creation_garde(1080,230,1200,230,1200,230,1,5)
    Creation_garde(1300,230,1420,230,1300,230,1,5)
    Creation_garde(1080,280,1170,280,1080,280,1,5)
    Creation_garde(1310,280,1400,280,1400,280,1,5)
    Creation_garde2(1240,390,1,800)
    Creation_garde2(1160,450,1,0)
    Creation_garde2(1320,450,3,0)
    Creation_garde(1115,450,1115,570,1115,450,1,-5)
    Creation_garde(1365,450,1365,570,1365,570,1,5)
    Creation_garde2(1240,540,1,500)
    Creation_garde(1080,580,1200,580,1080,580,1,5)
    Creation_garde(1300,580,1420,580,1420,580,1,5)
    for i in range(11):
        Creation_garde(550+50*i,680,550+50*i,740,550+50*i,680+10*abs(5-i),2-signe(5-i),1)
        Creation_garde(550+50*i,850,550+50*i,910,550+50*i,850+10*abs(5-i),2+signe(5-i),1)  
    Creation_garde(120,740,240,860,120,740,1,10)
    Creation_garde(120,740,240,860,240,740,2,10)
    Creation_garde(120,740,240,860,240,860,3,10)
    Creation_garde(120,740,240,860,120,860,4,10)
    
    Mouvement_adverse()
    
    canvas.focus_set()
    canvas.bind("<Key>", clavier)
    canvas.pack(expand=1)
    fenetre.mainloop()

def map4():
    global Niveau
    Niveau=4
    create_map()
    
    # # Murs # #
    obstacle(-20,60,90,330)
    obstacle(130,0,130,300)
    obstacle(130,320,130,60)
    obstacle(40,440,60,40)
    obstacle(160,440,60,40)
    obstacle(260,320,70,180)
    obstacle(-20,540,60,300)
    obstacle(-20,830,310,220)
    obstacle(90,540,240,120)
    obstacle(90,660,10,50)
    obstacle(90,780,10,50)
    obstacle(170,680,80,50)
    obstacle(170,760,80,50)
    obstacle(330,620,80,240)
    obstacle(290,920,180,130)
    obstacle(470,720,100,330)
    obstacle(570,840,210,210)
    obstacle(770,550,120,500)
    obstacle(410,620,160,40)
    obstacle(570,550,160,110)
    obstacle(720,660,10,50)
    obstacle(620,710,80,80)
    obstacle(330,320,50,150)
    obstacle(400,490,30,100)
    obstacle(570,470,10,80)
    obstacle(440,180,140,290)
    obstacle(370,180,70,80)
    obstacle(260,0,230,100)
    obstacle(490,0,140,130)
    obstacle(630,0,160,200)
    obstacle(790,0,100,500)
    obstacle(570,250,130,40)
    obstacle(690,250,30,110)
    obstacle(650,460,160,40)
    obstacle(620,340,30,160)
    obstacle(890,0,320,250)
    obstacle(890,800,320,250)
    obstacle(930,300,100,40)
    obstacle(1070,300,100,40)
    obstacle(950,400,60,90)
    obstacle(1090,400,60,90)
    obstacle(1020,560,60,90)
    obstacle(930,620,40,40)
    obstacle(1130,620,40,40)
    obstacle(970,700,160,60)
    obstacle(1210,0,230,490)
    obstacle(1210,550,140,400)
    obstacle(1210,950,80,100)
    # # Objectif # #
    global objectif
    objectif = canvas.create_rectangle(1400,1000,1400+Taille_perso,1000+Taille_perso,fill="yellow") 
    # # Personage # #
    global Perso
    Perso = canvas.create_rectangle(0,0,Taille_perso,Taille_perso,fill="violet")
    # # Guardes # #
    Creation_garde(130,300,240,300,130,300,1,5)
    Creation_garde(20,420,100,480,20,420,1,5)
    Creation_garde(140,420,220,480,200,480,3,-5)
    Creation_garde2(0,520,1,1000)
    Creation_garde2(0,520,3,1000)
    Creation_garde2(100,660,2,0)
    Creation_garde(150,660,250,730,150,680,2,-5)
    Creation_garde(150,740,250,810,150,740,1,-5)
    Creation_garde(330,860,390,860,330,860,1,5)
    Creation_garde2(470,700,1,700)
    Creation_garde(600,690,700,790,700,690,1,-5)
    Creation_garde(600,690,700,790,600,690,2,-5)
    Creation_garde(600,690,700,790,600,790,3,-5)
    Creation_garde(600,690,700,790,700,790,4,-5)
    Creation_garde2(330,470,1,0)
    Creation_garde(440,490,470,570,440,490,1,-5)
    Creation_garde(500,490,540,570,540,570,3,-5)
    Creation_garde(340,260,420,300,340,260,1,5)
    Creation_garde(260,160,330,240,330,160,2,5)
    Creation_garde2(470,100,1,1200)
    Creation_garde2(470,100,3,1200)
    Creation_garde(720,200,770,250,720,200,1,-5)
    Creation_garde(660,370,760,370,660,370,1,5)
    Creation_garde(660,430,760,430,760,430,3,5)
    Creation_garde2(620,500,1,700)
    Creation_garde(910,280,1030,340,910,280,1,-5)
    Creation_garde(910,280,1030,340,1030,340,3,-5)
    Creation_garde(1050,280,1170,340,1050,280,1,-5)
    Creation_garde(1050,280,1170,340,1170,340,3,-5)
    Creation_garde(930,380,1010,490,930,380,1,5)
    Creation_garde(930,380,1010,490,1010,490,3,5)
    Creation_garde(1070,380,1150,490,1070,380,1,-5)
    Creation_garde(1070,380,1150,490,1150,490,3,-5)
    Creation_garde(910,600,970,660,910,600,1,5)
    Creation_garde(1000,540,1080,650,1000,540,1,-5)
    Creation_garde(1000,540,1080,650,1080,650,3,-5)
    Creation_garde(1110,600,1170,660,1100,600,1,-5)
    Creation_garde(950,680,1130,760,1040,680,1,-5)
    Creation_garde(950,680,1130,760,1040,760,3,-5)

    Mouvement_adverse()
    
    canvas.focus_set()
    canvas.bind("<Key>", clavier)
    canvas.pack(expand=1)
    fenetre.mainloop()

def map5():
    global Niveau
    Niveau=5
    create_map()
    # # Murs # #
    obstacle(0,0,350,180)
    obstacle(0,180,50,160)
    obstacle(0,340,150,120)
    obstacle(0,460,70,80)
    obstacle(0,620,70,80)
    obstacle(0,700,150,350)
    obstacle(120,220,150,40)
    obstacle(290,180,20,160)
    obstacle(230,260,40,200)
    obstacle(150,540,80,80)
    obstacle(180,720,20,50)
    obstacle(180,810,20,50)
    obstacle(150,900,130,40)
    obstacle(150,940,520,110)
    obstacle(270,420,80,40)
    obstacle(310,460,40,80)
    obstacle(350,480,100,60)
    obstacle(310,620,280,80)
    obstacle(230,700,280,80)
    obstacle(230,780,50,40)
    obstacle(300,780,50,40)
    obstacle(370,780,30,40)
    obstacle(420,780,30,40)
    obstacle(490,780,20,40)
    obstacle(300,900,50,40)
    obstacle(370,900,30,40)
    obstacle(420,900,30,40)
    obstacle(490,900,180,40)
    obstacle(550,780,40,180)
    obstacle(350,0,260,40)
    obstacle(610,0,120,20)
    obstacle(330,340,20,80)
    obstacle(330,240,80,100)
    obstacle(410,320,60,20)
    obstacle(410,190,60,110)
    obstacle(410,140,120,60)
    obstacle(410,120,140,20)
    obstacle(550,120,60,80)
    obstacle(610,140,160,60)
    obstacle(490,240,40,60)
    obstacle(590,640,80,60)
    obstacle(670,640,100,180)
    obstacle(670,900,40,30)
    obstacle(670,1030,160,20)
    obstacle(790,820,40,110)
    obstacle(770,450,60,370)
    obstacle(670,430,160,20)
    obstacle(610,430,60,120)
    obstacle(610,400,40,30)
    obstacle(550,240,40,80)
    obstacle(590,240,80,60)
    obstacle(610,300,60,80)
    obstacle(670,340,80,70)
    obstacle(770,220,60,190)
    obstacle(830,220,80,880)
    obstacle(770,140,180,80)
    obstacle(730,0,220,140)
    obstacle(610,140,160,60)
    obstacle(550,120,60,80)
    obstacle(510,420,80,200)
    obstacle(430,380,160,40)
    obstacle(490,320,100,60)
    obstacle(950,0,80,100)
    obstacle(1030,0,80,40)
    obstacle(1110,0,330,100)
    obstacle(1190,100,250,120)
    obstacle(1230,220,210,240)
    obstacle(1330,460,110,80)
    obstacle(1230,540,210,240)
    obstacle(1190,780,250,270)
    obstacle(1110,900,80,150)
    obstacle(1030,960,80,90)
    obstacle(950,900,80,150)
    obstacle(910,780,40,270)
    obstacle(1030,260,60,160)
    obstacle(960,550,60,180)
    obstacle(1120,550,60,180)
    # # Objets # #
    Cle(660,70)
    Cle(740,1000)
    Cle(1060,920)
    Portail(60,540,80,"v")
    Portail(50,540,80,"v")
    Portail(1230,460,80,"v")
    Plaque_tp(1,10,570,1060,60)
    # # Lasers alarme # #
    Creation_alarme2f(600,40,600,120)
    Creation_alarme2f(710,910,790,910)
    Creation_alarme2f(910,300,1030,300)
#    Creation_alarme2f(950,840,990,840)
#    Creation_alarme2f(1150,840,1190,840)
    Creation_alarme2m("h",1020,880,100,820,880,5)
    Creation_alarme2m("v",260,820,80,260,510,5)
#    Creation_alarme2m("v",957,760,50,955,1045,2)
#    Creation_alarme2m("v",1185,760,50,1095,1185,2)
    # # Objectif # #
    global objectif
    objectif = canvas.create_rectangle(1280,490,1280+Taille_perso,490+Taille_perso,fill="yellow")
    # # Personage # #
    global Perso
    Perso = canvas.create_rectangle(710,510,710+Taille_perso,510+Taille_perso,fill="violet")
    # # Gardes # #
    Creation_garde(590,300,590,505,590,300,1,4)
    Creation_garde(670,410,810,410,670,410,1,4)
    Creation_garde2(670,320,1,1000)
    Creation_garde2(670,320,3,1000)
    Creation_garde2(750,200,1,1000)
    Creation_garde2(750,200,3,1000)
    Creation_garde(530,140,530,280,530,140,1,5)
    Creation_garde(410,300,510,300,410,300,1,5)
    Creation_garde(355,360,405,440,355,360,1,5)
    Creation_garde2(490,420,1,800)
    Creation_garde2(490,420,3,800)
    Creation_garde2(490,600,1,800)
    Creation_garde2(490,600,3,800)
    Creation_garde2(430,540,1,800)
    Creation_garde(130,520,230,620,130,520,1,-5)
    Creation_garde(130,520,230,620,230,620,3,-5)
    Creation_garde2(70,520,1,1000)
    Creation_garde2(70,620,1,-1000)
    Creation_garde(160,700,160,850,160,700,1,6)
    Creation_garde(200,700,200,850,200,850,3,-6)
    Creation_garde(280,780,280,920,280,780,1,5)
    Creation_garde(350,780,350,920,350,850,1,5)
    Creation_garde(400,780,400,920,400,920,1,5)
    Creation_garde(450,780,450,920,450,780,1,5)
    Creation_garde(470,780,470,920,470,920,1,5)
    Creation_garde(590,700,650,760,590,700,1,-5)
    Creation_garde(660,830,760,870,760,870,3,-5)
    Creation_garde(690,950,790,950,690,950,1,5)
    Creation_garde(150,270,150,380,150,270,1,3)
    Creation_garde(180,295,180,405,180,405,1,3)
    Creation_garde(210,320,210,430,210,320,1,3)
    Creation_garde2(270,400,1,900)
    Creation_garde2(270,400,3,900)
    Creation_garde(310,180,310,320,310,180,1,3)
    Creation_garde(360,60,380,120,360,60,1,-5)
    Creation_garde(620,30,700,110,620,30,1,5)
    Creation_garde(960,150,1030,200,960,150,1,5)
    Creation_garde(1090,150,1160,200,1160,200,3,5)
    Creation_garde(910,340,1010,340,910,340,1,5)
    Creation_garde(910,380,1010,380,1010,380,3,5)
    Creation_garde(1090,300,1210,300,1090,300,1,5)
    Creation_garde(1090,380,1210,380,1210,380,3,5)
    Creation_garde2(1140,340,1,500)
    Creation_garde2(930,490,1,600)
    Creation_garde2(1190,490,3,600)
    Creation_garde2(1100,590,1,500)
    Creation_garde2(1020,650,3,500)
    Creation_garde2(1100,710,1,500)
    Creation_garde2(920,720,4,0)
    Creation_garde2(1200,720,4,0)
    Creation_garde(1060,490,1060,720,1060,490,1,6)
    Creation_garde2(990,820,3,-700)
    Creation_garde2(1130,820,1,-700)
        
    Mouvement_adverse()
    canvas.focus_set()
    canvas.bind("<Key>", clavier)
    canvas.pack(expand=1)
    fenetre.mainloop()

def map6():
    print(6)

def map7():
    print(7)

def map8():
    print(8)

def map9():
    print(9)

def map10():
    print(10)

def map11():
    print(11)

def map12():
    print(12)

# # Fonctions annexes # # 
def signe(x):
    if x>=0:
        return 1
    else:
        return -1

def signe1(x):
    if x>0:
        return 3
    else:
        return 1

def signe3(x):
    if x>0:
        return 1
    else:
        return 3

def Add_Visionx(n,sens):
    if n==2 or (n==3 and sens>0) or(n==1 and sens<0):
        return Taille_perso
    else:
        return 0

def Add_Visiony(n,sens):
    if (n==3 and sens>0) or (n==1 and sens<0) or n==4:
        return Taille_perso
    else:
        return 0

def Reduce_Visionx(n,sens):
    if (n==2 and sens>0) or (n==4 and sens<0):
        return 10
    elif n==1 and sens<0:
        return 5
    else:
        return -1

def Reduce_Visionxr(n,sens):
    if n==3:
        return 5
    else:
        return -1

def Reduce_Visiony(n,sens):
    if n==3:
        return 10
    else:
        return -1

def Reduce_Visionyr(n,sens):
    if (n==4 and sens>0) or (n==2 and sens<0):
        return 5
    elif n==4 and sens<0:
        return -5
    else:
        return -1

def betweenL(x,a,b):
    m=a
    M=b
    if m>M:
        m,M = M,m
    if x>=m and x<=M:
        return True
    else:
        return False

def betweenS(x,a,b):
    m=a
    M=b
    if m>M:
        m,M = M,m
    if x>m and x<M:
        return True
    else:
        return False

def Suppr_List(L,i):
    return L[0:i]+L[i+1:]

def Add_info(texte):
    global Info
    global Event
    A=tk.Label(Event,text=texte)
    if len(Info)>6:
        for i in range (len(Info)-1):
            Info[i]=Info[i+1]
        Info[len(Info)-1]=texte
        for i in range(1,len(Event.winfo_children())):
            Event.winfo_children()[1].destroy()
        for i in range (len(Info)):
            tk.Label(Event,text=Info[i]).pack()
    else:
        Info.append(texte)
        A.pack()

# # Fonction canvas # #  
def rotation(objet,point,angle):
    global canvas
    Nombre_points= len(canvas.coords(objet))
    Nouvelle_coords=[]
    for i in range(0,Nombre_points,2):
        X0s=point[0] + (canvas.coords(objet)[i]-point[0])*n.cos(angle) + (canvas.coords(objet)[i+1]-point[1])*n.sin(angle)
        Nouvelle_coords.append(X0s)
        Y0s=point[1] - (canvas.coords(objet)[i]-point[0])*n.sin(angle) + (canvas.coords(objet)[i+1]-point[1])*n.cos(angle)
        Nouvelle_coords.append(Y0s)
    canvas.coords(objet,Nouvelle_coords)
 
def Vision_garde(x0,y0,Taille_vision,sens):
    global canvas
    if sens>0:
        V=canvas.create_polygon([x0+Taille_perso,y0+Taille_perso/4,x0+Taille_perso,y0+3/4*Taille_perso,x0+Taille_perso+Taille_vision,y0+3/4*Taille_perso+Pente_cone*Taille_vision,x0+Taille_perso+Taille_vision,y0+Taille_perso/4-Pente_cone*Taille_vision],outline="black",fill="yellow")
    else:
        V=canvas.create_polygon([x0,y0+Taille_perso/4,x0,y0+3/4*Taille_perso,x0-Taille_vision,y0+3/4*Taille_perso+Pente_cone*Taille_vision,x0-Taille_vision,y0+Taille_perso/4-Pente_cone*Taille_vision],outline="black",fill="yellow")
    return V

def Reduire_visionr(i):
    global Zone_interdite
    global Info_garde
    Info_garde[i][8]=0
    canvas.delete(Info_garde[i][7])
    Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0],canvas.coords(Info_garde[i][0])[1],Info_garde[i][8],1)
    Centre=((canvas.coords(Info_garde[i][0])[0]+canvas.coords(Info_garde[i][0])[2])/2,(canvas.coords(Info_garde[i][0])[1]+canvas.coords(Info_garde[i][0])[3])/2)
    rotation(Info_garde[i][7],Centre,-signe(Info_garde[i][5])*(Info_garde[i][6]-1)*n.pi/2)
    while (Restriction_mouvement(canvas.coords(Info_garde[i][7])[4],canvas.coords(Info_garde[i][7])[5],"L")) and (Restriction_mouvement(canvas.coords(Info_garde[i][7])[6],canvas.coords(Info_garde[i][7])[7],"L")) and Info_garde[i][8]<50:
        Info_garde[i][8]=Info_garde[i][8]+5 # 1 : + précis mais ralentit le jeu
        canvas.delete(Info_garde[i][7])
        Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0],canvas.coords(Info_garde[i][0])[1],Info_garde[i][8],1)
        rotation(Info_garde[i][7],Centre,-signe(Info_garde[i][5])*(Info_garde[i][6]-1)*n.pi/2)

def Reduire_vision(i):
    global Zone_interdite
    global Info_garde
   # print(Info_garde[i][6])
    Info_garde[i][8]=0
    canvas.delete(Info_garde[i][7])
    Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0],canvas.coords(Info_garde[i][0])[1],Info_garde[i][8],signe(Info_garde[i][5]))
    Centre=((canvas.coords(Info_garde[i][0])[0]+canvas.coords(Info_garde[i][0])[2])/2,(canvas.coords(Info_garde[i][0])[1]+canvas.coords(Info_garde[i][0])[3])/2)
    rotation(Info_garde[i][7],Centre,-signe(Info_garde[i][5])*(Info_garde[i][6]-1)*n.pi/2)
    while (Restriction_mouvement(canvas.coords(Info_garde[i][7])[4],canvas.coords(Info_garde[i][7])[5],"L")) and (Restriction_mouvement(canvas.coords(Info_garde[i][7])[6],canvas.coords(Info_garde[i][7])[7],"L")) and Info_garde[i][8]<50:
        Info_garde[i][8]=Info_garde[i][8]+5  # 1 : + précis mais ralentit le jeu
        canvas.delete(Info_garde[i][7])
        Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0],canvas.coords(Info_garde[i][0])[1],Info_garde[i][8],signe(Info_garde[i][5]))
        rotation(Info_garde[i][7],Centre,-signe(Info_garde[i][5])*(Info_garde[i][6]-1)*n.pi/2)
    
def Restriction_mouvement(x,y,Type):
    global Zone_interdite
    Possible = True
    i = 0
    while i < len(Zone_interdite) and Possible:
        if eval("between"+Type)(x,Zone_interdite[i][0],Zone_interdite[i][1]) and eval("between"+Type)(y,Zone_interdite[i][2],Zone_interdite[i][3]):
                Possible = False
        i=i+1
    return Possible

def clavier(event):
    if Play:
        touche = event.keysym
        if touche == "z" or touche == "s" or touche == "d" or touche == "q":
            Mouvement(touche)
        if touche == "Escape":
            Pause()
        if touche=="f":
            print(canvas.coords(Perso))
        if touche=="Return":
            Action()

def Mouvement(touche):
    global canvas
    global Perso
    global objectif
    global Last_moov
    if touche == "z" and canvas.coords(Perso)[1]>0 and Restriction_mouvement(canvas.coords(Perso)[0]+10, canvas.coords(Perso)[1]-8,"L"):
        canvas.move(Perso,0,-10)
    elif touche == "s" and canvas.coords(Perso)[1]<Largeur_map-Taille_perso and Restriction_mouvement(canvas.coords(Perso)[0]+10, canvas.coords(Perso)[1]+10+10,"L"):
       canvas.move(Perso,0,10)   
    elif touche == "d" and canvas.coords(Perso)[0]<Longueur_map-Taille_perso and Restriction_mouvement(canvas.coords(Perso)[0]+10+10, canvas.coords(Perso)[1]+10,"L"):
       canvas.move(Perso,10,0)        
    elif touche == "q" and canvas.coords(Perso)[0]>0 and Restriction_mouvement(canvas.coords(Perso)[0]-10+10, canvas.coords(Perso)[1]+10,"L"):
         canvas.move(Perso,-10,0)
    Last_moov=touche
    if Detection():
        Game_over()
    Detection_Laser()
    Test_TP()
    if canvas.coords(Perso)==canvas.coords(objectif):
        Victoire()

def Test_TP():
    global canvas
    global Perso
    global Teleporteur
    L=[canvas.coords(Perso)[0],canvas.coords(Perso)[1]]
    Recherche=False
    i=0
    while i<len(Teleporteur) and not Recherche:
        if L==Teleporteur[i][1:3]:
            Recherche=True
            Plaque=1
        elif L==Teleporteur[i][3:5]:
            Recherche=True
            Plaque=2
        else:
            pass
        i=i+1
    if Recherche:
        teleport(i-1,Plaque)

def Detection_Laser():
    global Laser
    global canvas
    global Perso
    X,Y=canvas.coords(Perso)[0],canvas.coords(Perso)[1]
    Vu = False
    i=0
    while i<len(Laser) and not Vu:
        Rayon=canvas.coords(Laser[i][1])
        if Rayon[1]==Rayon[3]:
            if (betweenL(X,Rayon[0],Rayon[2]) and betweenL(Rayon[1],Y,Y+Taille_perso)) or (betweenL(X+Taille_perso,Rayon[0],Rayon[2]) and betweenL(Rayon[1],Y,Y+Taille_perso)):
                Vu=True
        else:
            if (betweenL(Y,Rayon[1],Rayon[3]) and betweenL(Rayon[0],X,X+Taille_perso)) or (betweenL(Y+Taille_perso,Rayon[1],Rayon[3]) and betweenL(Rayon[0],X,X+Taille_perso)):
                Vu=True    
        i=i+1
    if Vu:
        AlarmeON()

def Action():
    global Objet
    global canvas
    global Perso
    global Last_moov
    if Last_moov=="z":
        L=[canvas.coords(Perso)[0],canvas.coords(Perso)[1]-Taille_perso]
    elif Last_moov=="q":
        L=[canvas.coords(Perso)[0]-Taille_perso,canvas.coords(Perso)[1]]
    elif Last_moov=="s":
        L=[canvas.coords(Perso)[0],canvas.coords(Perso)[1]+Taille_perso]
    else:
        L=[canvas.coords(Perso)[0]+Taille_perso,canvas.coords(Perso)[1]]
    Recherche = False
    i=0
    while i<len(Objet) and not Recherche:
        if Objet[i][0]=="p":
            if Last_moov=="d" or Last_moov=="q":
                if (betweenL(canvas.coords(Objet[i][1])[0],L[0],L[0]+Taille_perso)) and (betweenL(L[1],canvas.coords(Objet[i][1])[1],canvas.coords(Objet[i][1])[3])):
                   Recherche = True
                   Type=Objet[i][0]
#            elif Last_moov=="q":
#                if (L[0]==canvas.coords(Objet[i][1])[0]) and (betweenL(L[1],canvas.coords(Objet[i][1])[1],canvas.coords(Objet[i][1])[3])):
#                   Recherche = True
#                   Type=Objet[i][0]
            else:
                if (betweenL(canvas.coords(Objet[i][1])[1],L[1],L[1]+Taille_perso)) and (betweenL(L[0],canvas.coords(Objet[i][1])[0],canvas.coords(Objet[i][1])[2])):
                   Recherche = True
                   Type=Objet[i][0]
        else:
            if canvas.coords(Objet[i][1])[0:2]==L:
                Recherche = True
                Type=Objet[i][0]
        i=i+1
    if Recherche:
        if Type=="a":
            AlarmeON()
#            info=canvas.create_text(Largeur_map//2,10,text="Vous activez l'alarme !")
#            canvas.after(3000,canvas.delete(info))
        elif Type=="c":
            Recup_cle(i-1)
#            info=canvas.create_text(Largeur_map//2,10,text="Vous récupérez une clé !")
#            canvas.after(3000,canvas.delete(info))
        elif Type=="p":
            Ouvrir_porte(i-1)
        elif Type=="t":
            TimeSlow(i-1)
#            info=canvas.create_text(Largeur_map//2,10,text="Le temps est ralenti !")
#            canvas.after(3000,canvas.delete(info))
            
def Recup_cle(i):
    global canvas
    global Objet
    global Zone_interdite
    global Inventaire
    global Aff_cle
    Inventaire[0]=Inventaire[0]+1
    indice=Objet[i][2]
    canvas.delete(Objet[i][1])
    Objet=Suppr_List(Objet,i)
    Zone_interdite=Suppr_List(Zone_interdite,indice)
    for j in range (len(Objet)):
        if Objet[j][0]!="a":
            if Objet[j][2]>indice:
                Objet[j][2]=Objet[j][2]-1
    Add_info("Vous récupérez une clé !")
    Aff_cle.set("Vous avez "+str(Inventaire[0])+" clé(s)")

def Ouvrir_porte(i):
    global canvas
    global Objet
    global Zone_interdite
    global Inventaire
    global Aff_cle
    if Inventaire[0]>0:
        Inventaire[0]=Inventaire[0]-1
        indice=Objet[i][2]
        canvas.delete(Objet[i][1])
        Objet=Suppr_List(Objet,i)
        Zone_interdite=Suppr_List(Zone_interdite,indice)
        for j in range (len(Objet)):
            if Objet[j][0]!="a":
                if Objet[j][2]>indice:
                    Objet[j][2]=Objet[j][2]-1
        Add_info("La porte s'ouvre !")
        Aff_cle.set("Vous avez "+str(Inventaire[0])+" clé(s)")

    else:
        Add_info("La porte est fermé à clé ...")
    
def TimeSlow(i):
    global canvas
    global Objet
    global Zone_interdite
    global Tps_mvt
    global Tps_slow
    global Temps_ralentit
    Tps_mvt=Tps_mvt*3
    Tps_slow=0
    Temps_ralentit=True
    indice=Objet[i][2]
    canvas.delete(Objet[i][1])
    Objet=Suppr_List(Objet,i)
    Zone_interdite=Suppr_List(Zone_interdite,indice)
    for j in range (len(Objet)):
        if Objet[j][0]!="a":
            if Objet[j][2]>indice:
                Objet[j][2]=Objet[j][2]-1
    Add_info("Le temps est ralentit !")

def teleport(i,j):
    global canvas
    global Perso
    global Teleporteur
    if j==1:
        anim_teleport(Perso,Teleporteur[i][3],Teleporteur[i][4])
        #canvas.coords(Perso,[Teleporteur[i][3],Teleporteur[i][4],Teleporteur[i][3]+Taille_perso,Teleporteur[i][4]+Taille_perso])
    elif j==2 and Teleporteur[i][0]==2:
        anim_teleport(Perso,Teleporteur[i][1],Teleporteur[i][2])
        #canvas.coords(Perso,[Teleporteur[i][1],Teleporteur[i][2],Teleporteur[i][1]+Taille_perso,Teleporteur[i][2]+Taille_perso])
    else:
        pass
    
def anim_teleport(objet,x,y):
    X,Y=canvas.coords(objet)[0],canvas.coords(objet)[1]
    Temps=[250,500,600,700,800,900,950,1000,1050,1100,1200,1300,1400,1500]
    L1=[X,Y,X+Taille_perso,Y+Taille_perso]
    L2=[X+5,Y+5,X+Taille_perso-5,Y+Taille_perso-5]
    for i in range (len(Temps)):
        if i%2==0:
            canvas.after(Temps[i], lambda cible=objet, coord=L2 : canvas.coords(cible,coord))
        else:
            canvas.after(Temps[i], lambda cible=objet, coord=L1 : canvas.coords(cible,coord))
        if i>=7:
            L1=[x,y,x+Taille_perso,y+Taille_perso]
            L2=[x+5,y+5,x+Taille_perso-5,y+Taille_perso-5]

def obstacle(x,y,Lx,Ly):
    global canvas
    global Zone_interdite
    canvas.create_rectangle(x,y,x+Lx,y+Ly,fill="black")
    Zone_interdite.append([x,x+Lx,y,y+Ly])

def Portail(x,y,taille,sens):
    global canvas
    global Objet
    global Zone_interdite
    if sens=="h":
        portail=canvas.create_rectangle(x,y,x+taille,y+10,fill="brown")
        Zone_interdite.append([x,x+taille,y,y+10])
    else:
        portail=canvas.create_rectangle(x,y,x+10,y+taille,fill="brown")
        Zone_interdite.append([x,x+10,y,y+taille])
    Objet.append(["p",portail,len(Zone_interdite)-1])
    
def Creation_alarme(x,y):
    global canvas
    global Objet
    global Zone_interdite
    alarme=canvas.create_rectangle(x,y,x+Taille_perso,y+Taille_perso,fill="brown")
    Zone_interdite.append([x,x+Taille_perso,y,y+Taille_perso])
    Objet.append(["a",alarme])

def Cle(x,y):
    global canvas
    global Objet
    global Zone_interdite
    cle=canvas.create_rectangle(x,y,x+Taille_perso,y+Taille_perso,fill="brown")
    Zone_interdite.append([x,x+Taille_perso,y,y+Taille_perso])
    Objet.append(["c",cle,len(Zone_interdite)-1])

def TimeSlower(x,y):
    global canvas
    global Objet
    global Zone_interdite
    TimeSlower=canvas.create_rectangle(x,y,x+Taille_perso,y+Taille_perso,fill="brown")
    Zone_interdite.append([x,x+Taille_perso,y,y+Taille_perso])
    Objet.append(["t",TimeSlower,len(Zone_interdite)-1])

def Plaque_tp(nb_sens,x1,y1,x2,y2):
    global canvas
    global Teleporteur
    canvas.create_rectangle(x1,y1,x1+Taille_perso,y1+Taille_perso,fill="green")
    canvas.create_rectangle(x2,y2,x2+Taille_perso,y2+Taille_perso,fill="green")
    Teleporteur.append([nb_sens,x1,y1,x2,y2])
    
def Creation_alarme2f(x1,y1,x2,y2):
    global canvas
    global Laser
    rayon=canvas.create_line(x1,y1,x2,y2,fill="red")
    Laser.append(["f",rayon])

def Creation_alarme2m(Type,x0,y0,l,P1,P2,dmouv):
    global canvas
    global Laser
    if Type=="h":
        rayon=canvas.create_line(x0,y0,x0+l,y0,fill="red")
    else:
        rayon=canvas.create_line(x0,y0,x0,y0+l,fill="red")
    Laser.append([Type,rayon,P1,P2,dmouv,1])
    
def Creation_garde(x0,y0,x1,y1,XD,YD,Phase,dmouv):
    global canvas
    global Info_garde
    global Vision
    Garde=canvas.create_rectangle(XD,YD,XD+Taille_perso,YD+Taille_perso,fill="red")
    V = Vision_garde(XD,YD,50,signe(dmouv))
    rotation(V,(XD+Taille_perso/2,YD+Taille_perso/2),-signe(dmouv)*(Phase-1)*n.pi/2)
    if dmouv<0:
        rotation(V,(XD+Taille_perso/2,YD+Taille_perso/2),n.pi)
    Info_garde.append([Garde,x0,y0,x1,y1,dmouv,Phase,V,50])
    Vision.append([canvas.coords(V)[0],canvas.coords(V)[1],canvas.coords(V)[4],canvas.coords(V)[5]])

def Creation_garde2(x0,y0,Phase,dt):
    Garde=canvas.create_rectangle(x0,y0,x0+Taille_perso,y0+Taille_perso,fill="red")
    V = Vision_garde(x0,y0,50,1)
    if dt==0:
        rotation(V,(x0+Taille_perso/2,y0+Taille_perso/2),-(Phase-1)*n.pi/2)
    Info_garde.append([Garde,x0,y0,1,-4,dt,Phase,V,50])
    Vision.append([canvas.coords(V)[0],canvas.coords(V)[1],canvas.coords(V)[4],canvas.coords(V)[5]])

def Mouvement_adverse():
    global fenetre
    global canvas
    global Info_garde
    global Vision
    global Alarme_active
    global Temps_ralentit
    global Tps_alarme
    global Tps_slow
    global Laser
    global testp
    global Tps_ecoule
    global Aff_Temps
    if Play:
        for i in range(len(Info_garde)):
            if Info_garde[i][4]<0:    #dmouv=0 --> Tourne sur lui-même
                if Info_garde[i][3]==abs(Info_garde[i][5])//100:
                    Info_garde[i][6]=Info_garde[i][6]+1
                    if Info_garde[i][6]==5:
                        Info_garde[i][6]=1
                    Reduire_visionr(i)
                    Info_garde[i][3]=1
                else:
                    Info_garde[i][3]=Info_garde[i][3]+1
            else:
                
                if Info_garde[i][6]==1:
                    if canvas.coords(Info_garde[i][0])[0]*signe(Info_garde[i][5])<Info_garde[i][signe1(Info_garde[i][5])]*signe(Info_garde[i][5]):
                        canvas.move(Info_garde[i][0],Info_garde[i][5],0)
                        
                        if Restriction_mouvement(canvas.coords(Info_garde[i][7])[4],canvas.coords(Info_garde[i][7])[5]-10,"L"):
                            canvas.move(Info_garde[i][7],Info_garde[i][5],0)
                        else:
                            Info_garde[i][8]=Info_garde[i][8]-abs(Info_garde[i][5])
                            canvas.delete(Info_garde[i][7])
                            Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0]-Info_garde[i][5],canvas.coords(Info_garde[i][0])[1],Info_garde[i][8],signe(Info_garde[i][5]))
                            canvas.move(Info_garde[i][7],Info_garde[i][5],0)
                   
                    else:
                        Info_garde[i][6]=2
                        Reduire_vision(i)    
                    
                if Info_garde[i][6]==2:
                    if canvas.coords(Info_garde[i][0])[1]<Info_garde[i][4]:
                        canvas.move(Info_garde[i][0],0,abs(Info_garde[i][5]))
                        
                        if Restriction_mouvement(canvas.coords(Info_garde[i][7])[4]+signe(Info_garde[i][5])*10,canvas.coords(Info_garde[i][7])[5],"L"):
                            canvas.move(Info_garde[i][7],0,abs(Info_garde[i][5]))
                        else:
                            Info_garde[i][8]=Info_garde[i][8]-abs(Info_garde[i][5])
                            canvas.delete(Info_garde[i][7])
                            Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0],canvas.coords(Info_garde[i][0])[1]+abs(Info_garde[i][5]),Info_garde[i][8],signe(Info_garde[i][5]))
                            Centre=((canvas.coords(Info_garde[i][0])[0]+canvas.coords(Info_garde[i][0])[2])/2,(canvas.coords(Info_garde[i][0])[1]+canvas.coords(Info_garde[i][0])[3])/2)
                            rotation(Info_garde[i][7],Centre,-signe(Info_garde[i][5])*n.pi/2) # Angle = Info_garde[i][6]-1
                            canvas.move(Info_garde[i][7],Info_garde[i][5],0)
                            
                    else:
                        Info_garde[i][6]=3
                        Reduire_vision(i)
                    
                if Info_garde[i][6]==3:
                    if canvas.coords(Info_garde[i][0])[0]*signe(Info_garde[i][5])>Info_garde[i][signe3(Info_garde[i][5])]*signe(Info_garde[i][5]):
                        canvas.move(Info_garde[i][0],-Info_garde[i][5],0)
                        
                        if Restriction_mouvement(canvas.coords(Info_garde[i][7])[4],canvas.coords(Info_garde[i][7])[5]+10,"L"):
                            canvas.move(Info_garde[i][7],-Info_garde[i][5],0)
                        else:
                            Info_garde[i][8]=Info_garde[i][8]-abs(Info_garde[i][5])
                            canvas.delete(Info_garde[i][7])
                            Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0]-Info_garde[i][5],canvas.coords(Info_garde[i][0])[1],Info_garde[i][8],signe(Info_garde[i][5]))
                            Centre=((canvas.coords(Info_garde[i][0])[0]+canvas.coords(Info_garde[i][0])[2])/2,(canvas.coords(Info_garde[i][0])[1]+canvas.coords(Info_garde[i][0])[3])/2)
                            rotation(Info_garde[i][7],Centre,n.pi)
                            canvas.move(Info_garde[i][7],-Info_garde[i][5],0)
                        
                    else:
                        Info_garde[i][6]=4
                        Reduire_vision(i)                
                    
                if Info_garde[i][6]==4:
                    if canvas.coords(Info_garde[i][0])[1]>Info_garde[i][2]:
                        canvas.move(Info_garde[i][0],0,-abs(Info_garde[i][5]))
                        
                        if Restriction_mouvement(canvas.coords(Info_garde[i][7])[4]-signe(Info_garde[i][5])*10,canvas.coords(Info_garde[i][7])[5],"L"):
                            canvas.move(Info_garde[i][7],0,-abs(Info_garde[i][5]))
                        else:
                            Info_garde[i][8]=Info_garde[i][8]-abs(Info_garde[i][5])
                            canvas.delete(Info_garde[i][7])
                            Info_garde[i][7]=Vision_garde(canvas.coords(Info_garde[i][0])[0],canvas.coords(Info_garde[i][0])[1]+abs(Info_garde[i][5]),Info_garde[i][8],signe(Info_garde[i][5]))
                            Centre=((canvas.coords(Info_garde[i][0])[0]+canvas.coords(Info_garde[i][0])[2])/2,(canvas.coords(Info_garde[i][0])[1]+canvas.coords(Info_garde[i][0])[3])/2)
                            rotation(Info_garde[i][7],Centre,signe(Info_garde[i][5])*n.pi/2) 
                            canvas.move(Info_garde[i][7],-Info_garde[i][5],0)
                            
                    else:
                        Info_garde[i][6]=1
                        Reduire_vision(i)
         
            Vision[i]=[canvas.coords(Info_garde[i][0])[0]+Add_Visionx(Info_garde[i][6],Info_garde[i][5]),canvas.coords(Info_garde[i][0])[1]+Add_Visiony(Info_garde[i][6],Info_garde[i][5]),canvas.coords(Info_garde[i][7])[4],canvas.coords(Info_garde[i][7])[5]]
        if Detection():
            Game_over()
        if not Alarme_active or (Alarme_active and (-1)**testp>0):
            for i in range (len(Laser)):
                if Laser[i][0]=="h":
                    canvas.move(Laser[i][1],0,Laser[i][4]*(-1)**Laser[i][5])
                    if canvas.coords(Laser[i][1])[1]<=Laser[i][2]:
                        Laser[i][5]=2
                    elif canvas.coords(Laser[i][1])[1]>=Laser[i][3]:
                        Laser[i][5]=1
                elif Laser[i][0]=="v":
                    canvas.move(Laser[i][1],Laser[i][4]*(-1)**Laser[i][5],0)
                    if canvas.coords(Laser[i][1])[0]<=Laser[i][2]:
                        Laser[i][5]=2
                    elif canvas.coords(Laser[i][1])[0]>=Laser[i][3]:
                        Laser[i][5]=1
        Detection_Laser()            
        #print(Info_garde[i][9])
        if Alarme_active:
            testp=testp+1
            Tps_alarme=Tps_alarme+Tps_mvt
            if Tps_alarme>10000:
                testp=0
                AlarmeOFF()
        if Temps_ralentit:
            Tps_slow=Tps_slow+Tps_mvt
            if Tps_slow>10000:
                SlowtimeOFF()
        if not Alarme_active:
            Tps_ecoule=Tps_ecoule+Tps_mvt
            Aff_Temps.set("Temps : "+str(Tps_ecoule/1000))
        elif Alarme_active and (-1)**testp>0:
            Tps_ecoule=Tps_ecoule+2*Tps_mvt
            Aff_Temps.set("Temps : "+str(Tps_ecoule/1000))
        fenetre.after(Tps_mvt,Mouvement_adverse)

def Detection():
    global canvas
    global Vision
    global Perso
    X=[canvas.coords(Perso)[0],canvas.coords(Perso)[0],canvas.coords(Perso)[2],canvas.coords(Perso)[2]]
    Y=[canvas.coords(Perso)[1],canvas.coords(Perso)[3],canvas.coords(Perso)[1],canvas.coords(Perso)[3]]
    i=0
    Vu= False
    while i<len(Vision) and not Vu:
        for j in range (4):
            if betweenL(X[j],Vision[i][0],Vision[i][2]) and betweenL(Y[j],Vision[i][1],Vision[i][3]):
                Vu = True
        i=i+1
    return Vu

def Game_over():
    global fenetre
    global canvas
    global Play
    Play=False
    canvas.create_text(740,525,text="Game over",font="Arial 40",fill="Red")
    fenetre.after(2000,fenGO)

def Victoire():
    global fenetre
    global canvas
    global Play
    global Map_dispo
    global Niveau
    Play=False
    if Niveau==Map_dispo:
        Map_dispo=Map_dispo+1
    canvas.create_text(740,525,text="Niveau terminé !",font="Arial 40",fill="Red")
    fenetre.after(2000,fenW)

def AlarmeON():
    global Alarme_active
    global Tps_mvt
    global Tps_alarme
    global Son_alarme
    Tps_alarme=0
    if not Alarme_active:
        Alarme_active=True
        Tps_mvt=Tps_mvt//2
        Add_info("L'alarme est activée !")
        Son_alarme.play()


def AlarmeOFF():
    global Alarme_active
    global Tps_mvt
    Alarme_active=False
    Tps_mvt=Tps_mvt*2

def SlowtimeOFF():
    global Temps_ralentit
    global Tps_mvt 
    Temps_ralentit=False
    Tps_mvt=Tps_mvt//3


# # Caractéristiques générales du canvas # #

Longueur_map =1440
Largeur_map=1050
Taille_perso=20
Taille_vision=50
Pente_cone=Taille_perso/(4*Taille_vision)


# # Programme # #
Menu_principal()