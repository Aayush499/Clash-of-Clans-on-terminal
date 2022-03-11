import time
import colorama
from colorama import Fore, Back, Style

# custom modules
from extra import healthCOLOR, ROWS, COLS,X0, Y0



class King():

    def __init__(self, village,health, width):
        self.village = village
        self.x = X0  # (x, y) are coordinates of the centre
        self.y = Y0
        self.v = 1
        self.color = Back.BLUE
        self.char = 'B'
        self.attack = False
        self.health = health
        self.color = healthCOLOR[health]

    def reset(self):
        self.x = X0
        self.y = Y0

    def moveX(self, dirn=1):
        x = self.x
        if (x >= COLS-1  and dirn == 1):
            return
        if (x  <= 1 and dirn == -1):
            return
        
        self.village.layout[self.y][self.x] = Back.GREEN +  "_"
        self.x += self.v*dirn
    
    def moveY(self, dirn = 1):
        y = self.y
        if (y >= ROWS-1  and dirn == 1):
            return
        if (y  < 1 and dirn == -1):
            return
        self.village.layout[self.y][self.x] = Back.GREEN + "_"
        self.y += self.v*dirn

    def display(self):
        y = self.y
        x = self.x
        arr = self.village.layout
        if (x   <= 0):
            x = 0
        elif (x  >= COLS-1):
            x = COLS-1 
        if self.attack:
            color = Back.RED
        else:
            color = self.color
        
        arr[self.y][self.x] = color + self.char + Style.RESET_ALL
        self.village.layout = arr