import numpy as np
from enum import Enum


gameName = "ToBeFound"

characterSize = 10
alarmDuration = 8000
timeSlowDuration = 5000
refreshFrameTime = 100
mapWidth=1440
mapHeight=1050
gateThickness = 10

rotationAngles = {
    'NE':-np.pi/2, 'NS':np.pi, 'NW':np.pi/2,
    'ES':-np.pi/2, 'EW':np.pi, 'EN':np.pi/2,
    'SW':-np.pi/2, 'SN':np.pi, 'SE':np.pi/2,
    'WN':-np.pi/2, 'WE':np.pi, 'WS':np.pi/2,
    }

class Orientation(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

    def __add__(self,other):
        return self._value_+other._value_

class GuardType(Enum):
    MOBIL = "mobil"
    ROTATER = "rotater"
    FIX = "fix"

class LaserDirection(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    FIX = "fix"

class WarperSens(Enum):
    UNIC = "unic"
    BOTH = "both"