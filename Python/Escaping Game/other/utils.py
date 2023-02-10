import numpy as np

def isStrictBetween(value,inf,sup):
    return value > inf and value < sup

def isBetween(value,inf,sup):
    return value>=inf and value<=sup


def rotate(point,centre,angle):
    x1, y1 = point
    xC, yC = centre
    x2=round(xC + (x1-xC)*np.cos(angle) + (y1-yC)*np.sin(angle))
    y2=round(yC - (x1-xC)*np.sin(angle) + (y1-yC)*np.cos(angle))
    return x2,y2

def geoliste(g):
    r=[i for i in range(0,len(g)) if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

def centrefenetre(fen):
    fen.update_idletasks()
    l,h,x,y=geoliste(fen.geometry())
    fen.geometry("%dx%d%+d%+d" % (l,h,(fen.winfo_screenwidth()-l)//2,(fen.winfo_screenheight()-h)//2))
