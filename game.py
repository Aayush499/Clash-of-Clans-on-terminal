from array import *
import colorama
import sys
import os
import math
import time
import copy
import time
from colorama import Fore, Back, Style
#from buildings import Hut, TownHall 
from king import King

WIDTH = HEIGHT =15

class Village():
    def __init__(self):
        self.layout = [[Back.GREEN+"_" +Style.RESET_ALL]* HEIGHT for _ in range(WIDTH)]
        self.size = (WIDTH, HEIGHT)
        self.townHallPos = (WIDTH/2, HEIGHT/2)
        self.hut1 = (WIDTH/2 - 5, HEIGHT/2)
        self.hut2 = (WIDTH/2 + 5, HEIGHT/2)
        self.hut3 = (WIDTH/2 , HEIGHT/2-7)
        self.hut4 = (WIDTH/2 - 5, HEIGHT/2+5)
        self.hut5 = (WIDTH/2 - 5, HEIGHT/2+10)
        

        self.raid = True
        self.King= King(self, 4, 1)


