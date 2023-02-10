
from other.constants import Orientation, GuardType,LaserDirection,WarperSens

def createMap(canvas):
    canvas.createObjective(1200, 750)

    canvas.createWarper({'x0':30,'y0':30,'x1':310,'y1':310,'sens':WarperSens.BOTH})
    canvas.createWarper({'x0':810,'y0':810,'x1':1210,'y1':'810','sens':WarperSens.UNIC})
    canvas.createKey({'x':260,'y':600})
    canvas.createTimeSlower({'x':400,'y':50})
    canvas.createAlarm({'x':520,'y':650})

    canvas.createThief(10, 10, Orientation.SOUTH)

    canvas.createGuard({
        'x':360,'y':210,'orientation':Orientation.SOUTH,'type':GuardType.MOBIL,"speed":10,
        "path":[{'x':360,'y':210},{'x':360,'y':310},{'x':430,'y':310},{'x':430,'y':210}]})
    canvas.createGuard({
        'x':240,'y':240,'orientation':Orientation.WEST,'type':GuardType.MOBIL,'speed':5,
        "path":[{'x':240,'y':240},{'x':240,'y':150},{'x':140,'y':150},{'x':140,'y':240}]})
    canvas.createGuard({
        'x':740,'y':150,'orientation':Orientation.EAST,'type':GuardType.MOBIL,'speed':5,
        "path":[{'x':740,'y':150},{'x':810,'y':150},{'x':740,'y':150},{'x':740,'y':210}]})
    canvas.createGuard({
        'x':510,'y':510,'orientation':Orientation.EAST,'type':GuardType.ROTATER,'speed':500,
        "path":[Orientation.EAST,Orientation.NORTH,Orientation.WEST,Orientation.SOUTH],'reverse':False})
    canvas.createGuard({
        'x':1010,'y':510,'orientation':Orientation.SOUTH,'type':GuardType.ROTATER,'speed':500,
        "path":[Orientation.SOUTH,Orientation.WEST,Orientation.NORTH,Orientation.EAST],'reverse':False})
    canvas.createGuard({
        'x':1090,'y':510,'orientation':Orientation.EAST,'type':GuardType.ROTATER,'speed':500,
        "path":[Orientation.EAST,Orientation.SOUTH,Orientation.WEST,Orientation.NORTH],'reverse':False})
    canvas.createGuard({
        'x':1010,'y':430,'orientation':Orientation.WEST,'type':GuardType.ROTATER,'speed':500,
        "path":[Orientation.WEST,Orientation.NORTH,Orientation.EAST,Orientation.SOUTH],'reverse':False})
    canvas.createGuard({
        'x':1090,'y':430,'orientation':Orientation.NORTH,'type':GuardType.ROTATER,'speed':500,
        "path":[Orientation.NORTH,Orientation.EAST,Orientation.SOUTH,Orientation.WEST],'reverse':False})
    canvas.createGuard({'x':710,'y':710,'orientation':Orientation.NORTH,'type':GuardType.FIX})
    canvas.createGuard({
        'x':410,'y':510,'orientation':Orientation.SOUTH,'type':GuardType.MOBIL,'speed':10,
        "path":[{'x':410,'y':510},{'x':410,'y':710}]
    })
    canvas.createGuard({'x':110,'y':670,'orientation':Orientation.EAST,'type':GuardType.FIX})

    canvas.createLaser({'x0':120,'y0':500,'x1':200,'y1':500,'direction':LaserDirection.FIX})
    canvas.createLaser({'x0':60,'y0':500,'x1':60,'y1':700,'direction':LaserDirection.FIX})
    canvas.createLaser({
        'x0':120,'y0':550,'x1':200,'y1':550,'direction':LaserDirection.VERTICAL,
        'speed':5,'path':[(120,550),(120,650)],'phaseAller':True})
    canvas.createLaser({
        'x0':150,'y0':950,'x1':150,'y1':1030,'direction':LaserDirection.HORIZONTAL,
        'speed':5,'path':[(120,950),(230,950)],'phaseAller':True})

    canvas.createWall({'x':150,'y':160,'Lx':80,'Ly':70})
    canvas.createWall({'x':260,'y':110,'Lx':60,'Ly':160})
    canvas.createWall({'x':50,'y':110,'Lx':70,'Ly':160})
    canvas.createWall({'x':120,'y':50,'Lx':150,'Ly':80})
    canvas.createWall({'x':120,'y':270,'Lx':140,'Ly':30})
    canvas.createWall({'x':340,'y':330,'Lx':40,'Ly':30})
    canvas.createWall({'x':500,'y':440,'Lx':30,'Ly':40})
    canvas.createWall({'x':440,'y':490,'Lx':40,'Ly':40})
    canvas.createWall({'x':550,'y':490,'Lx':30,'Ly':40})
    canvas.createWall({'x':480,'y':550,'Lx':60,'Ly':30})
    canvas.createWall({'x':350,'y':510,'Lx':30,'Ly':30})
    canvas.createWall({'x':900,'y':440,'Lx':300,'Ly':60})
    canvas.createWall({'x':1020,'y':300,'Lx':60,'Ly':300})
    canvas.createWall({'x':470,'y':290,'Lx':30,'Ly':50})

    canvas.createGate({'x':400,'y':770,'longueur':60,'orientation':Orientation.EAST})
    canvas.createGate({'x':600,'y':500,'longueur':60,'orientation':Orientation.NORTH})
    canvas.createGate({'x':400,'y':180,'longueur':60,'orientation':Orientation.NORTH})




