import colorama
from colorama import Fore, Back, Style

from extra import healthCOLOR
deathCheck = 0


def winCondition(bricks):
    if deathCheck == 6:
        return True
    
        
class Buildings:
    def __init__(self, game, x, y, health, character, width, height):
        self.health = health
        self.pos = (x,y)
        self.char = character
        self._color = healthCOLOR[health]
        self.w = width
        self.h = height
    
    def display(self):
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        arr = self.game.board
        for x in range(self.x, self.x+w):
            arr[y][x] = self._color + self._char
        arr[y][self.x + w] = Style.RESET_ALL + arr[y][self.x + w]
        self.game.board = arr


 